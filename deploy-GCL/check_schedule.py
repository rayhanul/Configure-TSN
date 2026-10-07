#!/usr/bin/env python3
"""
check_schedule.py
-----------------
Pre-deploy check: replay a schedule package's flows through its own gcl/*.cfg gates the way
the TTTech switches actually forward, and report every flow whose latency would exceed its
deadline -- before the package is pushed with configure_gcl.py.

The scheduler's e2e_ns is not enough: it is computed with the scheduler's own timing model,
which can disagree with the hardware. In particular a C9-on package assumes the next hop's
window may open proc_delay_ns after the previous hop's window opens (cut-through), but the
switches are store-and-forward: a frame is only ready at the next hop after it has been fully
received plus the switch's relay delay. A frame that reaches a window it no longer fits in
waits for the next window of its queue on that port, which can be hundreds of µs away.

Hardware model (TTTech switches, 1 Gb/s), per egress port:
  - store-and-forward: ready at the next hop = start of transmission + frame time + hop delay
    (`tsntool brport getdelays`: independent rx+relay+tx = 1740-4020 ns; replaying the
    heuristic-c9-off run fits 2100 ns with a guard band, or 3000 ns without one)
  - strict priority between the TT queues (7 over 6), FIFO within a queue
  - a frame starts only if its gate is open and max(frame time, guard band) fits before the gate
    closes (windows of ~2.1 µs on the testbed carried no frame, not even a 0.96 µs one)
  - senders launch each frame at basetime + n*period + first-hop psi_ns (NIC launch time),
    switches run their gate cycle on the same grid (basetime.json)
The model reproduces the heuristic-c9-off/1-matrix-c9off run (results-2026-10-01_3) to within
2 µs mean per-flow latency.

Run:
    python3 check_schedule.py --pkg ../GCL_Schedules/<package>/<run>
    python3 check_schedule.py --pkg <pkg> --results <pkg>/results/<run>/results.md   # vs measured
Exit status 1 if any flow would miss its deadline at any of the hop delays checked.
"""

import argparse
import bisect
import heapq
import json
import os
import re
import sys

TT_QUEUES = (7, 6)  # strict priority order
FILENAME_RE = re.compile(r"^(?P<port>[A-Za-z0-9]+-p\d+)\.cfg$")


def load_gates(gcl_dir, cycle_ns):
    """{port: (boundaries, {queue: (open_starts, open_ends)})}, open intervals over two cycles
    so a window wrapping the cycle end stays one interval."""
    gates = {}
    for name in sorted(os.listdir(gcl_dir)):
        m = FILENAME_RE.match(name)
        if not m:
            continue
        t, entries = 0, []
        with open(os.path.join(gcl_dir, name)) as f:
            for line in f:
                x = line.split("#")[0].split()
                if len(x) == 3 and x[0] == "sgs":
                    d = int(float(x[1]))
                    entries.append((t, t + d, int(x[2], 0)))
                    t += d
        if t != cycle_ns:
            raise ValueError(f"{name}: entries sum to {t} ns, cycle is {cycle_ns} ns")
        open_iv = {}
        for q in TT_QUEUES:
            iv = []
            for base in (0, cycle_ns):
                for s, e, mask in entries:
                    if mask >> q & 1:
                        if iv and iv[-1][1] == base + s:
                            iv[-1][1] = base + e
                        else:
                            iv.append([base + s, base + e])
            open_iv[q] = ([a for a, _ in iv], [b for _, b in iv])
        gates[m["port"]] = ([e for _, e, _ in entries], open_iv)
    return gates


def simulate(schedule, gates, hop_delay_ns, guard_ns, cycles):
    """Latencies (ns, launch -> start of transmission at the last switch) per flow id."""
    cycle = schedule["cycle_ns"]
    hw = schedule["hw"]
    ns_per_byte = 8e9 / hw.get("link_rate_bps", 1_000_000_000)
    overhead = hw.get("frame_overhead_bytes", 20)
    flows = [f for f in schedule["flows"] if f.get("scheduled") and f.get("hops")]
    horizon = cycle * cycles

    missing = sorted({h["port"] for f in flows for h in f["hops"][1:]} - set(gates))
    if missing:
        raise ValueError(f"no gcl/*.cfg for egress port(s): {', '.join(missing)}")

    events, seq = [], 0

    def push(t, *data):
        nonlocal seq
        seq += 1
        heapq.heappush(events, (t, seq) + data)

    def open_until(port, q, t):
        starts, ends = gates[port][1][q]
        tc = t % cycle
        i = bisect.bisect_right(starts, tc) - 1
        return t - tc + ends[i] if i >= 0 and tc < ends[i] else None

    def next_change(port, t):
        bounds = gates[port][0]
        tc = t % cycle
        i = bisect.bisect_right(bounds, tc)
        return t - tc + (bounds[i] if i < len(bounds) else cycle)

    queues = {p: {q: [] for q in TT_QUEUES} for p in gates}
    busy = dict.fromkeys(gates, 0)
    lat = {f["id"]: [] for f in flows}
    sent = dict.fromkeys(lat, 0)
    for f in flows:
        c = round((f["size"] + overhead) * ns_per_byte)
        for n in range(horizon // f["period"]):
            t0 = n * f["period"] + f["hops"][0]["psi_ns"]
            sent[f["id"]] += 1
            push(t0 + c + hop_delay_ns, f, 1, t0, c)

    def try_send(port, t):
        if busy[port] > t:
            return
        for q in TT_QUEUES:
            if not queues[port][q]:
                continue
            end = open_until(port, q, t)
            f, hop, t0, c = queues[port][q][0]
            if end is None or t + max(c, guard_ns) > end:
                continue
            queues[port][q].pop(0)
            busy[port] = t + c
            if hop + 1 < len(f["hops"]):
                push(t + c + hop_delay_ns, f, hop + 1, t0, c)
            else:
                lat[f["id"]].append(t - t0)
            push(t + c, None, port)
            return
        if any(queues[port].values()):
            push(next_change(port, t), None, port)

    while events:
        t, _, f, *rest = heapq.heappop(events)
        if t > horizon + 3 * cycle:
            break
        if f is None:
            try_send(rest[0], t)
        else:
            hop, t0, c = rest
            h = f["hops"][hop]
            queues[h["port"]][h["queue"]].append((f, hop, t0, c))
            try_send(h["port"], t)
    return flows, lat, sent


def load_measured(path):
    """{flow id: (min, avg, max) µs} from a run_experiment.py results.md."""
    meas = {}
    with open(path) as f:
        for line in f:
            c = [x.strip() for x in line.split("|")]
            if len(c) > 12 and c[1].isdigit():
                lat = next((x for x in c[3:] if x.count("/") == 2), None)
                if lat:
                    meas[c[2]] = tuple(float(v) for v in lat.split("/"))
    return meas


def main():
    ap = argparse.ArgumentParser(description="Check a GCL schedule package against the switches' "
                                             "store-and-forward behavior before deploying it")
    ap.add_argument("--pkg", required=True, help="package directory (schedule.json + gcl/)")
    ap.add_argument("--hop-delay-ns", default="2100,3000,4020",
                    help="comma-separated per-hop delays to check, beyond the frame time "
                         "(default 2100,3000,4020: fitted values and the getdelays maximum)")
    ap.add_argument("--guard-ns", type=int, default=2400,
                    help="time that must remain before a gate closes for any frame to start "
                         "(default 2400, the smallest value that fits the testbed runs)")
    ap.add_argument("--cycles", type=int, default=4, help="cycles to simulate (default 4)")
    ap.add_argument("--results", help="results.md of a testbed run, to compare against")
    ap.add_argument("-v", "--verbose", action="store_true", help="print every flow, not just misses")
    args = ap.parse_args()

    with open(os.path.join(args.pkg, "schedule.json")) as f:
        schedule = json.load(f)
    gates = load_gates(os.path.join(args.pkg, "gcl"), schedule["cycle_ns"])
    delays = [int(x) for x in args.hop_delay_ns.split(",")]
    meas = load_measured(args.results) if args.results else {}

    worst = {}  # flow id -> (max latency, hop delay it occurred at)
    stats = {}  # (flow id, hop delay) -> (min, avg, max, received, sent)
    flows = []
    for d in delays:
        flows, lat, sent = simulate(schedule, gates, d, args.guard_ns, args.cycles)
        for f in flows:
            L = lat[f["id"]]
            mx = max(L) if L else float("inf")
            stats[f["id"], d] = (min(L) if L else None, sum(L) / len(L) if L else None, mx,
                                 len(L), sent[f["id"]])
            if f["id"] not in worst or mx > worst[f["id"]][0]:
                worst[f["id"]] = (mx, d)

    print(f"{args.pkg}: {len(flows)} flows, hop delays {delays} ns, guard {args.guard_ns} ns, "
          f"{args.cycles} cycles")
    print(f"{'id':>8} {'route':<8} {'pcp':>3} {'period':>7} {'deadline':>8} {'sched e2e':>9} "
          f"{'worst (µs)':>10} {'@hop delay':>10}  {'measured min/avg/max':>22}")
    misses = []
    for f in flows:
        mx, d = worst[f["id"]]
        miss = mx > f["deadline"]
        if miss:
            misses.append(f["id"])
        if not (miss or args.verbose):
            continue
        m = meas.get(str(f["id"]))
        ms = "/".join(f"{v:.1f}" for v in m) if m else ""
        route = f"{f['src']}→{f['dst']}"
        mxs = f"{mx / 1000:.1f}" if mx != float("inf") else "lost"
        print(f"{f['id']:>8} {route:<8} {f['pcp']:>3} {f['period'] / 1000:>7.0f} "
              f"{f['deadline'] / 1000:>8.0f} {f['e2e_ns'] / 1000:>9.1f} {mxs:>10} {d:>10}  "
              f"{ms:>22}" + ("  <-- MISS" if miss else ""))
    if misses:
        print(f"\nFAIL: {len(misses)} flow(s) would miss their deadline on the switches: {misses}")
        print("Regenerate the package with store-and-forward timing (C9 off) and a per-hop delay "
              "that covers the switches (see this script's docstring) before deploying it.")
        return 1
    print("\nPASS: every flow meets its deadline at every hop delay checked.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
