#!/usr/bin/env python3
"""
measure_update.py -- time a GCL (802.1Qbv) schedule update on every switch of a topology.

    python3 measure_update.py                                   # dry-run: ports per topology
    python3 measure_update.py --apply                           # all topologies, 20 reps each
    python3 measure_update.py --apply --scenario mesh-8 --strategy batched --mode coordinated

Each update pushes one GCL to every port of the topology (topologies.json: named subgraphs of the
physical mesh) the way deploy-GCL/configure_gcl.py does -- upload the list, `tsntool st wrcl`,
`tsntool st configure` -- and timestamps every step on two PTP-synchronised clocks:

  CNC (CLOCK_TAI)             t_send ---- t_open ---- t_ack ...................... t_done
                               | channel open | exec request |                       ^
  switch (PTP CurrentTime)                          a --upload-- b --wrcl-- c --configure-- d
                                                                                       ...  cct
  send       = a - t_send   CNC issues the command -> the switch starts executing it
  switch     = d - a        exact on-switch time (write the list b-a, wrcl c-b, configure d-c)
  activation = cct - c      `configure` issued -> the hardware runs the new list (ConfigChangeTime);
                            usually inside the configure call, at the next cycle boundary
  return     = t_done - d   result back at the CNC

Network update time = last port's ConfigChangeTime - first command sent.

The GCL written is each port's own current OperControlList (read once at start), so by default the
switches' gate behaviour does not change; --entries N writes an all-gates-open list of N entries
instead and restores the original lists at the end.

Strategies: sequential (one port at a time, like configure_gcl.py), parallel (one thread per
switch, one SSH command per port), batched (one thread and ONE SSH command per switch).
Modes: immediate (each port activates at its next cycle boundary once configured; basetime = the
switch's own clock, which the driver treats as "in the past" and rounds up -- it logs
"AdminBaseTime in the past!" and bumps ConfigChangeError, and applies the list) and coordinated
(one common basetime --lead-seconds ahead, meant to switch every port at the same instant).
Measured 2026-10-08: these switches ignore the basetime (AdminBaseTime reads back 0, also when
written through sysfs) and always switch at the next cycle boundary after `configure`, so
coordinated behaves like immediate.

Output: results/<date>/ports.csv (one row per port update), runs.csv (one row per network update),
summary.md. plot_update.py draws the figures.
"""

import argparse
import csv
import datetime
import json
import os
import socket
import statistics
import sys
import threading
import time

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(REPO, "deploy-GCL"))
import configure_gcl as cg  # noqa: E402

PORT_PREFIX = "sw0"
REMOTE_FILE = "/home/root/gclbench_{iface}.cfg"  # not /tmp: small tmpfs on these boards (deploy-GCL/README.md)
STRATEGIES = ("sequential", "parallel", "batched")
MODES = ("immediate", "coordinated")


def tai_ns():
    return time.clock_gettime_ns(time.CLOCK_TAI)


def ts_ns(s):
    """'1791481334.057600000' -> ns"""
    sec, _, frac = s.strip().partition(".")
    return int(sec) * 1_000_000_000 + int((frac + "000000000")[:9])


def ns_str(ns):
    return f"{ns // 1_000_000_000}.{ns % 1_000_000_000:09d}"


# ---------------------------------------------------------------- topology

def resolve_ports(scn, topo):
    """scenario -> {switch: [port, ...]} (ports on its links, both ends, plus host ports)."""
    if "ports" in scn:
        return {sw: sorted(p) for sw, p in scn["ports"].items()}
    sws = set(scn["switches"])
    edges = scn.get("edges")
    if edges is None:
        edges = {tuple(sorted((sw, l["node"]))) for sw in sws for l in topo[sw]["links"].values()
                 if l.get("node") in sws}
    ports = {sw: set() for sw in sws}
    for a, b in edges:
        for x, y in ((a, b), (b, a)):
            p = [p for p, l in topo[x]["links"].items() if l.get("node") == y]
            if not p:
                raise ValueError(f"no link {x} -> {y} in the topology")
            ports[x].add(p[0])
    if scn.get("hosts"):
        for sw in sws:
            for p, l in topo[sw]["links"].items():
                if topo.get(l.get("node"), {}).get("type") == "end-station":
                    ports[sw].add(p)
    return {sw: sorted(p) for sw, p in ports.items() if p}


def load_scenarios(path, topo, names=None):
    with open(path) as f:
        scns = {k: v for k, v in json.load(f).items() if not k.startswith("_")}
    if names:
        missing = [n for n in names if n not in scns]
        if missing:
            sys.exit(f"[FATAL] unknown scenario(s) {missing}; have {sorted(scns)}")
        scns = {n: scns[n] for n in names}
    return {n: resolve_ports(s, topo) for n, s in scns.items()}


# ---------------------------------------------------------------- SSH

def connect(topo, switches, nodelay=False, retries=4):
    """one persistent SSH session per switch; returns clients and connect time (ms) per switch.
    clients[sw] is replaced in place by reconnect() if its session drops."""
    clients, conn_ms = {}, {}
    for sw in sorted(switches):
        _RECONNECT[sw] = lambda sw=sw: connect(topo, [sw], nodelay, retries)[0][sw]
        d = topo[sw]
        for attempt in range(retries):
            try:
                t0 = time.perf_counter()
                c = cg.ssh_connect(d["ip"], d["username"], d.get("password") or "")
                conn_ms[sw] = (time.perf_counter() - t0) * 1e3
                break
            except Exception as e:  # sshd drops rapid reconnects ("Error reading SSH protocol banner")
                if attempt == retries - 1:
                    raise
                print(f"  [retry] {sw}: {e}")
                time.sleep(1 + attempt)
        # paramiko leaves Nagle on; with delayed ACKs a command can wait ~40 ms to leave the CNC
        c.get_transport().sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1 if nodelay else 0)
        clients[sw] = c
        time.sleep(0.3)
    return clients, conn_ms


_RECONNECT = {}


def reconnect(clients, sw):
    try:
        clients[sw].close()
    except Exception:
        pass
    clients[sw] = _RECONNECT[sw]()


def exec_timed(client, script):
    """run one shell command; CNC TAI timestamps at send, channel open, exec accepted, result in."""
    tr = client.get_transport()
    t_send = tai_ns()
    ch = tr.open_session()
    t_open = tai_ns()
    ch.exec_command(script)  # waits for sshd to accept the exec request
    t_ack = tai_ns()
    out = ch.makefile("r").read().decode(errors="replace")
    err = ch.makefile_stderr("r").read().decode(errors="replace")
    rc = ch.recv_exit_status()
    t_done = tai_ns()
    ch.close()
    return dict(t_send=t_send, t_open=t_open, t_ack=t_ack, t_done=t_done), out, err, rc


def run(client, cmd):
    _, out, err, rc = exec_timed(client, cmd)
    return rc, out, err


# ---------------------------------------------------------------- GCL content

def snapshot(clients, ports):
    """current OperControlList + OperCycleTime of every port: {(sw, iface): (text, cycle)}."""
    snap = {}
    for sw, plist in ports.items():
        for p in plist:
            iface = PORT_PREFIX + p
            rc, out, err = run(clients[sw], f"tsntool st rdocl {iface}; echo CYCLE "
                                            f"$(cat /sys/class/net/{iface}/ieee8021ST/OperCycleTime)")
            lines = out.strip().splitlines()
            if rc or not lines or not lines[-1].startswith("CYCLE "):
                raise RuntimeError(f"{sw}/{iface}: could not read its GCL: {err or out}")
            text = "".join(l.strip() + "\n" for l in lines[:-1] if l.strip())
            snap[(sw, iface)] = (text, lines[-1].split()[1])
    return snap


def all_open_gcl(n, cycle, tick_ns=320):
    """n entries, all gates open, each a whole number of ticks, summing to the cycle."""
    num, den = map(int, cycle.split("/"))
    ticks = num * 1_000_000_000 // den // tick_ns
    if not 1 <= n <= min(255, ticks):
        raise ValueError(f"--entries {n} out of range")
    each = [ticks // n] * n
    each[-1] += ticks - sum(each)
    return "".join(f"sgs {t * tick_ns} 0xFF\n" for t in each)


def port_script(iface, content, cycle, basetime):
    """upload + wrcl + configure one port; timestamps from the switch's PTP clock (`read`: no fork).
    The here-document's temp file goes to /home/root: /tmp is a small tmpfs shared with the switch's
    logs and can be full (sw04, 2026-10-08), which silently writes an empty list. (The echo builtin
    avoids the temp file but takes ~150 ms for a 16-entry list on these switches.)
    basetime None = immediate: the switch's own current time, so the port activates at its next
    cycle boundary."""
    s = f"/sys/class/net/{iface}/ieee8021ST"
    f = REMOTE_FILE.format(iface=iface)
    bt = basetime or "$c"
    return (f"S={s}; read a < $S/CurrentTime\n"
            f"TMPDIR=/home/root cat > {f} <<'GCLEOF'\n{content}GCLEOF\n"
            f"read b < $S/CurrentTime; tsntool st wrcl {iface} {f}; r1=$?\n"
            f"read c < $S/CurrentTime; tsntool st configure {bt} {cycle} 0 {iface}; r2=$?\n"
            f"read d < $S/CurrentTime; read e < $S/ConfigChangeTime\n"
            f"echo \"T {iface} $a $b $c $d $r1 $r2 $e\"\n")


# ---------------------------------------------------------------- one network update

def update_network(clients, ports, contents, strategy, mode, lead_s=3.0):
    """push contents[(sw, iface)] = (text, cycle) to every port; returns (rows, basetime_ns)."""
    basetime_ns = tai_ns() + int(lead_s * 1e9) if mode == "coordinated" else None
    bt = ns_str(basetime_ns) if basetime_ns else None
    rows, lock = [], threading.Lock()

    def do_switch(sw):
        ifaces = [PORT_PREFIX + p for p in ports[sw]]
        groups = [ifaces] if strategy == "batched" else [[i] for i in ifaces]
        for g in groups:
            script = "".join(port_script(i, *contents[(sw, i)], bt) for i in g)
            try:
                tm, out, err, rc = exec_timed(clients[sw], script)
            except Exception as e:  # session dropped: record the ports as failed, reconnect, go on
                now = tai_ns()
                with lock:
                    rows.extend(dict(switch=sw, iface=i, exec_ports=len(g), pos_in_exec=k, t_send=now,
                                     t_done=now, error=f"ssh: {e}") for k, i in enumerate(g))
                reconnect(clients, sw)
                continue
            got = {}
            for line in out.splitlines():
                v = line.split()
                if len(v) == 9 and v[0] == "T":
                    got[v[1]] = v[2:]
            for k, iface in enumerate(g):
                r = dict(switch=sw, iface=iface, exec_ports=len(g), pos_in_exec=k, **tm)
                if iface in got:
                    a, b, c, d, r1, r2, e = got[iface]
                    r.update(sw_a=ts_ns(a), sw_b=ts_ns(b), sw_c=ts_ns(c), sw_d=ts_ns(d),
                             rc_wrcl=int(r1), rc_configure=int(r2), cct=ts_ns(e))
                else:
                    r.update(error=(err or out or f"rc {rc}").strip()[:200])
                with lock:
                    rows.append(r)

    if strategy == "sequential":
        for sw in sorted(ports):
            do_switch(sw)
    else:
        th = [threading.Thread(target=do_switch, args=(sw,)) for sw in sorted(ports)]
        for t in th:
            t.start()
        for t in th:
            t.join()
    return rows, basetime_ns


def derive(rows, basetime_ns=None):
    """per-port ms metrics (added to rows in place) and the network-level summary of one update."""
    ok = [r for r in rows if "cct" in r]
    t0 = min(r["t_send"] for r in rows)
    ms = lambda x: x / 1e6  # noqa: E731
    by_exec = {}
    for r in ok:
        by_exec.setdefault((r["switch"], r["t_send"]), []).append(r)
    for grp in by_exec.values():
        grp.sort(key=lambda r: r["pos_in_exec"])
        for k, r in enumerate(grp):
            first, last = k == 0, k == len(grp) - 1
            r["send_ms"] = ms(r["sw_a"] - (r["t_send"] if first else grp[k - 1]["sw_d"]))
            r["chan_open_ms"] = ms(r["t_open"] - r["t_send"]) if first else 0.0
            r["exec_ack_ms"] = ms(r["t_ack"] - r["t_open"]) if first else 0.0
            r["shell_start_ms"] = ms(r["sw_a"] - r["t_ack"]) if first else r["send_ms"]
            r["upload_ms"] = ms(r["sw_b"] - r["sw_a"])
            r["wrcl_ms"] = ms(r["sw_c"] - r["sw_b"])
            r["configure_ms"] = ms(r["sw_d"] - r["sw_c"])
            r["switch_ms"] = ms(r["sw_d"] - r["sw_a"])
            r["activation_ms"] = ms(r["cct"] - r["sw_c"])  # often < configure_ms: the hardware switches mid-call
            r["return_ms"] = ms(r["t_done"] - r["sw_d"]) if last else 0.0
            r["rtt_ms"] = ms(r["t_done"] - r["t_send"])
            r["port_update_ms"] = ms(r["cct"] - r["t_send"])
            r["live"] = int(r["rc_wrcl"] == 0 and r["rc_configure"] == 0 and
                            (r["cct"] >= basetime_ns - 1_000_000 if basetime_ns else r["cct"] >= r["sw_c"]))
    live = [r for r in ok if r["live"]]
    ok = live  # a port that did not take the new list keeps an old ConfigChangeTime
    run = dict(ports=len(rows), live_ports=len(live), switches=len({r["switch"] for r in rows}),
               ssh_commands=len({(r["switch"], r["t_send"]) for r in rows}),
               commands_ms=ms(max(r["t_done"] for r in rows) - t0))
    if ok:
        cct = [r["cct"] for r in ok]
        last_cfg = max(r["sw_d"] for r in ok)
        run.update(update_ms=ms(max(cct) - t0),            # network running the new GCL everywhere
                   configured_ms=ms(last_cfg - t0),        # last `configure` returned on its switch
                   activation_spread_ms=ms(max(cct) - min(cct)),  # old and new GCLs mixed in the network
                   send_ms_sum=sum(r["send_ms"] for r in ok),
                   switch_ms_sum=sum(r["switch_ms"] for r in ok),
                   switch_ms_max_per_switch=max(
                       sum(r["switch_ms"] for r in ok if r["switch"] == sw) for sw in {r["switch"] for r in ok}),
                   t_first_send=t0, t_last_cct=max(cct), t_first_cct=min(cct))
        if basetime_ns:
            run["basetime_margin_ms"] = ms(basetime_ns - last_cfg)  # >0: every port configured in time
    return run


def wait_until(t_ns):
    d = t_ns - tai_ns()
    if d > 0:
        time.sleep(d / 1e9)


# ---------------------------------------------------------------- report

PORT_COLS = ["scenario", "strategy", "mode", "entries", "nodelay", "rep", "switch", "iface", "exec_ports",
             "pos_in_exec", "t_send", "t_open", "t_ack", "sw_a", "sw_b", "sw_c", "sw_d", "cct", "t_done",
             "rc_wrcl", "rc_configure", "live", "send_ms", "chan_open_ms", "exec_ack_ms", "shell_start_ms",
             "upload_ms", "wrcl_ms", "configure_ms", "switch_ms", "activation_ms", "return_ms", "rtt_ms",
             "port_update_ms", "error"]
RUN_COLS = ["scenario", "strategy", "mode", "entries", "nodelay", "rep", "switches", "ports", "live_ports",
            "ssh_commands", "update_ms", "commands_ms", "configured_ms", "activation_spread_ms",
            "send_ms_sum", "switch_ms_sum", "switch_ms_max_per_switch", "basetime_margin_ms",
            "t_first_send", "t_first_cct", "t_last_cct"]


def q(vals, p):
    vals = sorted(vals)
    return vals[min(len(vals) - 1, int(round(p * (len(vals) - 1))))] if vals else float("nan")


def write_summary(path, runs, port_rows, conn_ms, meta):
    L = [f"# GCL update timing, {meta['started']}", "",
         f"Testbed: {meta['note']}. {meta['reps']} repetitions per row; values are median "
         f"(p5-p95) in ms. GCL per port: {meta['content']}. TCP_NODELAY: {'on' if meta['nodelay'] else 'off'}.",
         "", "SSH session setup per switch (once, not part of any update): " +
         ", ".join(f"{sw} {v:.0f}" for sw, v in sorted(conn_ms.items())) + " ms.", "",
         "## Network update time", "",
         "update = first command sent -> last port running the new GCL (its ConfigChangeTime). "
         "commands = first command sent -> last result back at the CNC. mixed = time old and new "
         "GCLs coexist in the network (last - first ConfigChangeTime). send / switch = sums over "
         "all ports of command-send time and exact on-switch time.", "",
         "| topology | switches | ports | strategy | mode | update | commands | mixed | send (sum) | switch (sum) | live ports |",
         "|---|---|---|---|---|---|---|---|---|---|---|"]
    keys = sorted({(r["scenario"], r["strategy"], r["mode"]) for r in runs},
                  key=lambda k: (meta["order"].index(k[0]), STRATEGIES.index(k[1]), k[2]))
    f = lambda v: f"{statistics.median(v):.1f} ({q(v, .05):.1f}-{q(v, .95):.1f})" if v else "–"  # noqa: E731
    for k in keys:
        rs = [r for r in runs if (r["scenario"], r["strategy"], r["mode"]) == k]
        col = lambda c: [r[c] for r in rs if r.get(c) is not None]  # noqa: E731
        L.append(f"| {k[0]} | {rs[0]['switches']} | {rs[0]['ports']} | {k[1]} | {k[2]} | {f(col('update_ms'))} | "
                 f"{f(col('commands_ms'))} | {f(col('activation_spread_ms'))} | {f(col('send_ms_sum'))} | "
                 f"{f(col('switch_ms_sum'))} | {sum(r['live_ports'] for r in rs)}/{sum(r['ports'] for r in rs)} |")
    L += ["", "## Per port: where the time goes", "",
          "send = CNC issues the command -> the switch starts running it (channel open + exec request + "
          "shell start). switch = exact time on the switch: upload (write the list to a file) + "
          "`tsntool st wrcl` + `tsntool st configure`. activation = configure issued -> hardware runs "
          "the new list (ConfigChangeTime). return = result back at the CNC. Per-port send counts only the first port of a "
          "batched command.", "",
          "| strategy | mode | send | chan open | exec req | shell start | upload | wrcl | configure | switch | activation | return | RTT |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for st in STRATEGIES:
        for mo in MODES:
            rs = [r for r in port_rows if r["strategy"] == st and r["mode"] == mo and r.get("live")]
            if not rs:
                continue
            first = [r for r in rs if r["pos_in_exec"] == 0]
            last = [r for r in rs if r["pos_in_exec"] == r["exec_ports"] - 1]
            g = lambda c, src=rs: f"{statistics.median([r[c] for r in src]):.2f}"  # noqa: E731
            L.append(f"| {st} | {mo} | {g('send_ms', first)} | {g('chan_open_ms', first)} | "
                     f"{g('exec_ack_ms', first)} | {g('shell_start_ms', first)} | {g('upload_ms')} | "
                     f"{g('wrcl_ms')} | {g('configure_ms')} | {g('switch_ms')} | {g('activation_ms')} | "
                     f"{g('return_ms', last)} | {g('rtt_ms', first)} |")
    with open(path, "w") as fh:
        fh.write("\n".join(L) + "\n")
    return L


def write_csv(path, cols, rows):
    with open(path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow({k: (f"{v:.4f}" if isinstance(v, float) else v) for k, v in r.items()})


def new_out_dir(base, stem):
    d, k = os.path.join(base, stem), 2
    while os.path.exists(d):
        d, k = os.path.join(base, f"{stem}_{k}"), k + 1
    os.makedirs(d)
    return d


def main():
    ap = argparse.ArgumentParser(description="Time GCL updates on every switch of a topology")
    ap.add_argument("--topology", default=os.path.join(REPO, "network-topology", "network-topology-rtas-2027.json"))
    ap.add_argument("--scenarios", default=os.path.join(HERE, "topologies.json"))
    ap.add_argument("--scenario", nargs="*", help="scenario names (default: all in --scenarios)")
    ap.add_argument("--strategy", nargs="*", default=list(STRATEGIES), choices=STRATEGIES)
    ap.add_argument("--mode", nargs="*", default=["immediate"], choices=MODES)
    ap.add_argument("--reps", type=int, default=20)
    ap.add_argument("--gap", type=float, default=0.3, help="seconds between updates")
    ap.add_argument("--lead-seconds", type=float, default=3.0, help="coordinated mode: basetime lead")
    ap.add_argument("--entries", type=int, default=None,
                    help="write an all-gates-open list of N entries instead of each port's own list "
                         "(restored at the end)")
    ap.add_argument("--nodelay", action="store_true", help="TCP_NODELAY on the SSH sockets")
    ap.add_argument("--out", default=None, help="output dir (default results/<date>[_k])")
    ap.add_argument("--apply", action="store_true", help="actually update the switches (default: dry-run)")
    args = ap.parse_args()

    topo = json.load(open(args.topology))
    scns = load_scenarios(args.scenarios, topo, args.scenario)
    for name, ports in scns.items():
        n = sum(len(p) for p in ports.values())
        print(f"{name}: {len(ports)} switch(es), {n} port(s): "
              + ", ".join(f"{sw}[{' '.join(p)}]" for sw, p in sorted(ports.items())))
    if not args.apply:
        print("\nDry-run only. Re-run with --apply to update the switches.")
        return 0

    started = datetime.datetime.now()
    out = args.out or new_out_dir(os.path.join(HERE, "results"), started.strftime("results-%Y-%m-%d"))
    os.makedirs(out, exist_ok=True)
    all_sw = {sw for p in scns.values() for sw in p}
    all_ports = {}
    for p in scns.values():
        for sw, pl in p.items():
            all_ports.setdefault(sw, set()).update(pl)
    all_ports = {sw: sorted(p) for sw, p in all_ports.items()}

    print(f"\nResults: {out}\nConnecting to {len(all_sw)} switch(es) ...")
    clients, conn_ms = connect(topo, all_sw, args.nodelay)
    print("Reading every port's current GCL ...")
    snap = snapshot(clients, all_ports)
    os.makedirs(os.path.join(out, "snapshot"), exist_ok=True)
    for (sw, iface), (text, cyc) in snap.items():
        with open(os.path.join(out, "snapshot", f"{sw}-{iface}.cfg"), "w") as fh:
            fh.write(f"# OperCycleTime {cyc}\n{text}")
    contents = ({k: (all_open_gcl(args.entries, cyc), cyc) for k, (_, cyc) in snap.items()}
                if args.entries else snap)

    runs, port_rows = [], []
    try:
        for name, ports in scns.items():
            for st in args.strategy:
                for mo in args.mode:
                    for rep in range(args.reps):
                        rows, bt = update_network(clients, ports, contents, st, mo, args.lead_seconds)
                        res = derive(rows, bt)
                        tag = dict(scenario=name, strategy=st, mode=mo, entries=args.entries or "own",
                                   nodelay=int(args.nodelay), rep=rep)
                        runs.append({**tag, **res})
                        port_rows += [{**tag, **r} for r in rows]
                        errs = [f"{r['switch']}/{r['iface']}: {r['error']}" for r in rows if r.get("error")]
                        print(f"  {name:9s} {st:10s} {mo:11s} rep {rep + 1:2d}: update "
                              f"{res.get('update_ms', float('nan')):7.1f} ms, commands {res['commands_ms']:7.1f} ms, "
                              f"live {res['live_ports']}/{res['ports']}" + (f"  ERR {errs[:2]}" if errs else ""))
                        if bt:
                            wait_until(max(bt, res.get("t_last_cct", 0)) + 200_000_000)
                        time.sleep(args.gap)
    finally:
        if args.entries:
            print("Restoring every port's original GCL ...")
            rows, _ = update_network(clients, all_ports, snap, "batched", "immediate")
            res = derive(rows)
            print(f"  restored {res['live_ports']}/{res['ports']} port(s)")
        for sw, c in clients.items():
            try:
                run(c, "rm -f " + REMOTE_FILE.format(iface="*"))
            except Exception:
                pass
            c.close()
        write_csv(os.path.join(out, "ports.csv"), PORT_COLS, port_rows)
        write_csv(os.path.join(out, "runs.csv"), RUN_COLS, runs)
        if runs:
            meta = dict(started=started.strftime("%Y-%m-%d %H:%M"), reps=args.reps, nodelay=args.nodelay,
                        order=list(scns), note="8 TTTech switches, CNC S2 on sw08 via the management LAN",
                        content=(f"all-open, {args.entries} entries" if args.entries
                                 else "each port's own OperControlList (gates unchanged)"))
            L = write_summary(os.path.join(out, "summary.md"), runs, port_rows, conn_ms, meta)
            print("\n" + "\n".join(L))
        with open(os.path.join(out, "meta.json"), "w") as fh:
            json.dump(dict(args=vars(args), connect_ms=conn_ms,
                           scenarios={n: p for n, p in scns.items()}), fh, indent=2)
    return 0


if __name__ == "__main__":
    sys.exit(main())
