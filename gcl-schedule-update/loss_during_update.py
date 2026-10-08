#!/usr/bin/env python3
"""
loss_during_update.py -- packet loss before, during and after a GCL update on the live network.

    D=../GCL_Schedules/dataset-testbed-2_2026-10-08/2-rl-c9on-matrix-S2rx
    python3 loss_during_update.py --pkg $D --scenario mesh-8 --strategy sequential --update-at 10 --duration 30
    python3 loss_during_update.py --pkg $D --target-gcl <other pkg>/gcl --update-at 10 --restore-at 20

Runs the package's flows (gen_traffic.py with --packet-log, every frame logged on both ends) on the
end stations that can be reached (S3 needs S3_PW=...), and while traffic runs updates the GCL of
every port of --scenario with measure_update.py's code. By default each port gets its own current
list back (the update itself is the only change); --target-gcl writes another package's lists
instead, and --restore-at puts the original lists back (they are always restored at the end).

Every frame is identified by its flow and launch time, so a frame is lost if it was sent and never
received. Phases, per update: before = up to the first command sent; during = first command sent ->
last port running the new list (ConfigChangeTime); after = the rest.

Output: <pkg>/results/update-loss-<date>[_k]/ with the update timeline (updates.json, ports.csv),
per-bin counts (bins.csv), per-phase table (summary.md), raw packet logs, and loss_timeline.png
(plot_update.py loss <dir>).
"""

import argparse
import datetime
import json
import os
import sys
import threading
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(REPO, "Spawning-Flows"))
import measure_update as mu  # noqa: E402
import run_experiment as rx  # noqa: E402  (also puts configureManager on the path)
import configure_gcl as cg  # noqa: E402


def available_nodes(endpoints, topo):
    """end stations with streams that we can sudo on: the CNC, or a password in env/topology."""
    names, skipped = [], []
    for n in sorted(endpoints):
        if not endpoints[n].get("streams"):
            continue
        t = topo[n]
        if t.get("cnc") or os.environ.get(f"{n}_PW") or not cg.needs_prompt(t.get("password")):
            names.append(n)
        else:
            skipped.append(n)
    return names, skipped


def target_contents(gcl_dir, ports, snap):
    """another package's lists for every port of the scenario, rounded to the 320 ns tick."""
    files = cg.discover_ports(gcl_dir)
    contents = {}
    for sw, plist in ports.items():
        for p in plist:
            iface = mu.PORT_PREFIX + p
            cyc = snap[(sw, iface)][1]
            num, den = map(int, cyc.split("/"))
            if p not in files.get(sw, {}):
                contents[(sw, iface)] = snap[(sw, iface)]  # no list for this port: keep its own
                continue
            with open(files[sw][p]) as f:
                entries = cg.parse_cfg_entries(cg.strip_trailing_comments(f.read()))
            entries = cg.round_to_tick(entries, 320, num * 1_000_000_000 // den)
            contents[(sw, iface)] = (cg.render_cfg_entries(entries), cyc)
    return contents


def start_traffic(nodes, pkg, out, duration, start_at, extra):
    """gen_traffic.py --packet-log on every node; returns threads to join."""
    files = [(os.path.join(REPO, "Spawning-Flows", "gen_traffic.py"), "gen_traffic.py")] + [
        (os.path.join(pkg, f), f) for f in ("schedule.json", "endpoints.json", "basetime.json")]
    for n in nodes:
        if not n.local:
            n.put(files)

    def one(n):
        args = f"--node {n.name} --run --duration {duration} --start-at {start_at:.6f} {extra}"
        log = os.path.join(out, f"results_{n.name}.log")
        if n.local:
            n.run(f"python3 {REPO}/Spawning-Flows/gen_traffic.py --schedule {pkg}/schedule.json "
                  f"--endpoints {pkg}/endpoints.json --basetime {pkg}/basetime.json {args} "
                  f"--packet-log {out}/pk_{n.name} > {log} 2>&1", sudo=True, timeout=duration + 120)
            return
        n.run(f"cd {rx.REMOTE_DIR} && rm -f pk_{n.name}.* && python3 gen_traffic.py --schedule schedule.json "
              f"--endpoints endpoints.json --basetime basetime.json {args} --packet-log pk_{n.name} "
              f"> run_{n.name}.log 2>&1", sudo=True, timeout=duration + 120)
        n.get(f"run_{n.name}.log", log)
        for ext in ("tx", "rx"):
            try:
                n.get(f"pk_{n.name}.{ext}", os.path.join(out, f"pk_{n.name}.{ext}"))
            except OSError:
                pass  # no senders / receivers on this node

    th = [threading.Thread(target=one, args=(n,)) for n in nodes]
    for t in th:
        t.start()
    return th


def load_logs(out, names):
    tx, rcv = [], []
    for n in names:
        for ext, cols, dst in (("tx", 2, tx), ("rx", 3, rcv)):
            p = os.path.join(out, f"pk_{n}.{ext}")
            if os.path.exists(p) and os.path.getsize(p):
                dst.append(np.fromfile(p, dtype=np.int64).reshape(-1, cols))
    tx = np.concatenate(tx) if tx else np.zeros((0, 2), np.int64)
    rcv = np.concatenate(rcv) if rcv else np.zeros((0, 3), np.int64)
    return tx, rcv


def analyse(tx, rcv, schedule, endpoints, names, start_ns, end_ns, updates, bin_ms):
    """per-bin and per-phase sent / lost / deadline misses, for flows whose both ends ran."""
    role = {}
    for n in names:
        for s in endpoints[n]["streams"].values():
            role.setdefault(int(s["flow_id"]), set()).add(s["role"])
    flows = sorted(f for f, r in role.items() if r == {"sender", "receiver"})
    deadline = {f["id"]: f["deadline"] for f in schedule["flows"]}
    tx = tx[np.isin(tx[:, 0], flows)]
    rcv = rcv[np.isin(rcv[:, 0], flows)]
    # a frame = (flow, launch time); received if that pair shows up at the receiver
    key = lambda f, t: f.astype(np.int64) * (1 << 40) + (t - start_ns + (1 << 38))  # noqa: E731
    got = np.isin(key(tx[:, 0], tx[:, 1]), key(rcv[:, 0], rcv[:, 1]))
    lat = rcv[:, 2] - rcv[:, 1]
    has_ts = rcv[:, 2] > 0
    miss = has_ts & (lat > np.array([deadline[int(f)] for f in rcv[:, 0]]))

    t_tx = (tx[:, 1] - start_ns) / 1e6  # ms since traffic start
    t_rx = (rcv[:, 1] - start_ns) / 1e6
    edges = np.arange(0, (end_ns - start_ns) / 1e6 + bin_ms, bin_ms)
    sent_b = np.histogram(t_tx, edges)[0]
    lost_b = np.histogram(t_tx[~got], edges)[0]
    miss_b = np.histogram(t_rx[miss], edges)[0]
    lat_max = np.full(len(edges) - 1, np.nan)
    idx = np.clip(np.digitize(t_rx[has_ts], edges) - 1, 0, len(edges) - 2)
    np.fmax.at(lat_max, idx, lat[has_ts] / 1e3)
    bins = dict(t_ms=edges[:-1], sent=sent_b, lost=lost_b, deadline_miss=miss_b, max_latency_us=lat_max)

    # phases: before the first update, then during/after each update
    marks = [("before", start_ns)]
    for i, u in enumerate(updates, 1):
        marks += [(f"during update {i}", u["t_first_send"]), (f"after update {i}", u["t_last_cct"])]
    marks.append(("end", end_ns))
    phases = []
    for (name, a), (_, b) in zip(marks, marks[1:]):
        s = (tx[:, 1] >= a) & (tx[:, 1] < b)
        r = (rcv[:, 1] >= a) & (rcv[:, 1] < b)
        n_s, n_l = int(s.sum()), int((s & ~got).sum())
        lr = lat[r & has_ts] / 1e3
        phases.append(dict(phase=name, start_ms=(a - start_ns) / 1e6, length_ms=(b - a) / 1e6, sent=n_s,
                           lost=n_l, loss_pct=100 * n_l / n_s if n_s else 0.0,
                           lost_per_s=n_l / ((b - a) / 1e9) if b > a else 0.0,
                           deadline_miss=int((r & miss).sum()),
                           lat_p50_us=float(np.median(lr)) if len(lr) else float("nan"),
                           lat_p99_us=float(np.percentile(lr, 99)) if len(lr) else float("nan"),
                           lat_max_us=float(lr.max()) if len(lr) else float("nan")))
    per_flow = []
    for f in flows:
        s = tx[:, 0] == f
        per_flow.append(dict(flow=f, sent=int(s.sum()), lost=int((s & ~got).sum()),
                             deadline_miss=int(miss[rcv[:, 0] == f].sum())))
    return flows, bins, phases, per_flow


def main():
    ap = argparse.ArgumentParser(description="Packet loss before/during/after a GCL update under traffic")
    ap.add_argument("--pkg", required=True, help="the LIVE package (schedule.json, endpoints.json, basetime.json)")
    ap.add_argument("--topology", default=os.path.join(REPO, "network-topology", "network-topology-rtas-2027.json"))
    ap.add_argument("--scenarios", default=os.path.join(HERE, "topologies.json"))
    ap.add_argument("--scenario", default="mesh-8")
    ap.add_argument("--strategy", default="sequential", choices=mu.STRATEGIES)
    ap.add_argument("--mode", default="immediate", choices=mu.MODES)
    ap.add_argument("--nodelay", action="store_true")
    ap.add_argument("--target-gcl", default=None,
                    help="dir of <switch>-<port>.cfg to update to (default: each port's own list)")
    ap.add_argument("--duration", type=float, default=30)
    ap.add_argument("--update-at", type=float, default=10, help="seconds after traffic start")
    ap.add_argument("--restore-at", type=float, default=None,
                    help="seconds after traffic start to put the original lists back (with --target-gcl)")
    ap.add_argument("--lead", type=float, default=8, help="seconds from launch to the common sender start")
    ap.add_argument("--bin-ms", type=float, default=10)
    args = ap.parse_args()

    pkg = os.path.abspath(args.pkg)
    topo = json.load(open(args.topology))
    endpoints = json.load(open(os.path.join(pkg, "endpoints.json")))
    schedule = json.load(open(os.path.join(pkg, "schedule.json")))
    ports = mu.load_scenarios(args.scenarios, topo, [args.scenario])[args.scenario]
    names, skipped = available_nodes(endpoints, topo)
    if skipped:
        print(f"[info] no sudo password for {', '.join(skipped)} (set <NODE>_PW): their flows are left out")

    started = datetime.datetime.now()
    out = mu.new_out_dir(os.path.join(pkg, "results"), started.strftime("update-loss-%Y-%m-%d"))
    print(f"Results: {out}\nSwitches ({args.scenario}): connecting, reading current GCLs ...")
    clients, conn_ms = mu.connect(topo, ports, args.nodelay)
    snap = mu.snapshot(clients, ports)
    target = target_contents(args.target_gcl, ports, snap) if args.target_gcl else snap
    print(f"End stations: {', '.join(names)}")
    nodes = [rx.Node(n, topo) for n in names]
    info = rx.preflight(nodes, endpoints)
    drops_before = rx.switch_drops(topo, pkg)

    start_ns = int((time.clock_gettime(time.CLOCK_TAI) + args.lead) * 1e9)
    end_ns = start_ns + int(args.duration * 1e9)
    extra = "--rt --lead-us 1000"
    print(f"Traffic: {args.duration:g} s from TAI {start_ns / 1e9:.3f}; update at +{args.update_at:g} s"
          + (f", restore at +{args.restore_at:g} s" if args.restore_at else ""))
    th = start_traffic(nodes, pkg, out, args.duration, start_ns / 1e9, extra)

    plan = [(args.update_at, target, "update")]
    if args.restore_at is not None:
        plan.append((args.restore_at, snap, "restore"))
    updates, port_rows = [], []
    restored = args.restore_at is not None or not args.target_gcl
    try:
        for at, contents, label in plan:
            mu.wait_until(start_ns + int(at * 1e9))
            rows, bt = mu.update_network(clients, ports, contents, args.strategy, args.mode)
            res = mu.derive(rows, bt)
            updates.append(dict(label=label, **res))
            port_rows += [dict(scenario=args.scenario, strategy=args.strategy, mode=args.mode,
                               rep=len(updates), **r) for r in rows]
            print(f"  {label} at +{(res['t_first_send'] - start_ns) / 1e9:.3f} s: update {res['update_ms']:.1f} ms, "
                  f"commands {res['commands_ms']:.1f} ms, live {res['live_ports']}/{res['ports']}")
        for t in th:
            t.join()
    finally:
        if not restored:
            rows, _ = mu.update_network(clients, ports, snap, "batched", "immediate")
            print(f"  original lists restored on {mu.derive(rows)['live_ports']} port(s)")
        for c in clients.values():
            c.close()
    drops_after = rx.switch_drops(topo, pkg)

    tx, rcv = load_logs(out, names)
    flows, bins, phases, per_flow = analyse(tx, rcv, schedule, endpoints, names, start_ns, end_ns,
                                            updates, args.bin_ms)
    mu.write_csv(os.path.join(out, "ports.csv"), ["scenario", "strategy", "mode", "rep"] + mu.PORT_COLS[6:], port_rows)
    with open(os.path.join(out, "bins.csv"), "w") as fh:
        fh.write("t_ms,sent,lost,deadline_miss,max_latency_us\n")
        for i in range(len(bins["t_ms"])):
            fh.write(f"{bins['t_ms'][i]:.3f},{bins['sent'][i]},{bins['lost'][i]},{bins['deadline_miss'][i]},"
                     f"{'' if np.isnan(bins['max_latency_us'][i]) else round(bins['max_latency_us'][i], 2)}\n")
    sw_drops = {k: drops_after[k] - drops_before.get(k, 0) for k in drops_after}
    meta = dict(pkg=os.path.relpath(pkg, REPO), scenario=args.scenario, strategy=args.strategy, mode=args.mode,
                nodelay=args.nodelay, target_gcl=args.target_gcl, start_ns=start_ns, end_ns=end_ns,
                bin_ms=args.bin_ms, nodes=names, skipped_nodes=skipped, flows=flows,
                updates=[{k: v for k, v in u.items()} for u in updates], phases=phases, per_flow=per_flow,
                switch_qdrops=sw_drops, connect_ms=conn_ms, ptp={k: v["ptp"] for k, v in info.items()})
    with open(os.path.join(out, "updates.json"), "w") as fh:
        json.dump(meta, fh, indent=2, default=float)

    L = [f"# Packet loss around a GCL update, {started:%Y-%m-%d %H:%M}", "",
         f"Package `{meta['pkg']}`, {len(flows)} flows ({', '.join(names)} running; "
         f"{'skipped ' + ', '.join(skipped) if skipped else 'all end stations'}). Update: {args.scenario} "
         f"({sum(len(p) for p in ports.values())} ports), {args.strategy}, {args.mode}, TCP_NODELAY "
         f"{'on' if args.nodelay else 'off'}, to "
         f"{'`' + args.target_gcl + '`' if args.target_gcl else 'each port’s own current list'}.", ""]
    for i, u in enumerate(updates, 1):
        L.append(f"- Update {i} ({u['label']}): first command at +{(u['t_first_send'] - start_ns) / 1e6:.1f} ms, "
                 f"network on the new lists after **{u['update_ms']:.1f} ms** (commands back after "
                 f"{u['commands_ms']:.1f} ms), {u['live_ports']}/{u['ports']} ports live.")
    L += ["", "| phase | from (ms) | length (ms) | sent | lost | loss % | lost/s | deadline misses | latency p50 / p99 / max (µs) |",
          "|---|---|---|---|---|---|---|---|---|"]
    for p in phases:
        L.append(f"| {p['phase']} | {p['start_ms']:.1f} | {p['length_ms']:.1f} | {p['sent']} | {p['lost']} | "
                 f"{p['loss_pct']:.3f} | {p['lost_per_s']:.1f} | {p['deadline_miss']} | "
                 f"{p['lat_p50_us']:.1f} / {p['lat_p99_us']:.1f} / {p['lat_max_us']:.1f} |")
    nz = {k: v for k, v in sw_drops.items() if v}
    L += ["", "Switch queue drops (Q DROP) during the run: "
          + (", ".join(f"{k} +{v}" for k, v in sorted(nz.items())) if nz else "none") + ".", "",
          "| flow | sent | lost | deadline misses |", "|---|---|---|---|"]
    L += [f"| {f['flow']} | {f['sent']} | {f['lost']} | {f['deadline_miss']} |" for f in per_flow]
    with open(os.path.join(out, "summary.md"), "w") as fh:
        fh.write("\n".join(L) + "\n")
    print("\n".join(L))
    try:
        import plot_update
        plot_update.plot_loss(out)
    except Exception as e:  # matplotlib may be unusable in this interpreter
        print(f"\n[info] no plot ({e}); run: python3 plot_update.py loss {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
