#!/usr/bin/env python3
"""Wait until the spanning tree on every switch has been quiet for QUIET seconds.

    python3 wait_stp_quiet.py --topology <topology.json> [--quiet 10] [--timeout 180]

After `configureManager.py --mstp --apply` (and after --reset), mstpd keeps re-converging for a while:
on 2026-10-10 sw08 blocked all its ports every ~4.5 s for ~25 s after the admit, each time for ~280 ms on
its switch-to-switch ports. A test started inside that window loses ~1% of its frames and sees ~320 ms
latencies on every flow through the blocked ports. Start traffic only after this script returns 0.

Quiet = no br0 port state change in the kernel log and no topology change in any MSTI, on every switch,
for QUIET seconds. Exit 1 on timeout."""
import argparse, json, os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import configureManager as cm  # noqa: E402

# seconds since the last br0 port state change, and the smallest "time since topology change" of all MSTIs
PROBE = ("up=$(cut -d' ' -f1 /proc/uptime); "
         "last=$(dmesg | grep -E 'br0: port .* entered' | tail -1 | sed 's/^\\[ *\\([0-9.]*\\)\\].*/\\1/'); "
         "tc=$(for t in $(mstpctl showmstilist br0 | tail -n +2); do mstpctl showtree br0 $t; done "
         "| awk '/time since topology change/{print $5}' | sort -n | head -1); "
         "echo $up ${last:-0} ${tc:-999999}")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--topology", required=True)
    ap.add_argument("--quiet", type=float, default=10.0, help="required quiet time in s (default 10)")
    ap.add_argument("--timeout", type=float, default=180.0, help="give up after this many s (default 180)")
    a = ap.parse_args()
    topo = json.load(open(a.topology))
    sws = sorted(k for k, v in topo.items() if v.get("type") == "sw")
    conn = {s: cm.ssh_connect(topo[s]["ip"], topo[s].get("username", "root"), topo[s].get("password", ""))
            for s in sws}
    t0 = time.time()
    while True:
        age = {}
        for s, c in conn.items():
            _, o, _ = c.exec_command(PROBE)
            up, last, tc = (float(x) for x in o.read().decode().split())
            age[s] = min(up - last, tc)
        waited = time.time() - t0
        if min(age.values()) >= a.quiet:
            print(f"spanning tree quiet on all {len(sws)} switches after {waited:.0f} s "
                  f"(least quiet: {min(age, key=age.get)}, {min(age.values()):.0f} s)")
            return 0
        if waited > a.timeout:
            busy = ", ".join(f"{s} {v:.1f} s" for s, v in sorted(age.items()) if v < a.quiet)
            print(f"spanning tree still changing after {waited:.0f} s: {busy}")
            return 1
        time.sleep(1)


if __name__ == "__main__":
    sys.exit(main())
