#!/usr/bin/env python3
"""
run_experiment.py -- run gen_traffic.py on every end station at once and write a dated results folder.

    python3 run_experiment.py --pkg ../GCL_Schedules/prob3-rl-c9-on/1-rl-c9on-matrix --duration 30 --ping

Frames are sent by the sender's NIC at their scheduled launch time and timestamped by the
receiver's NIC (needs 'gptp.sh launchtime on' on every node). --no-rt: no real-time processes.

Assumes the package's GCLs are deployed and its flows admitted (endpoints.json). Runs locally on
the CNC node and over SSH (configureManager.ssh_connect; sudo password from the topology file) on
the others (override a node's sudo password with <NODE>_PW=..., e.g. S3_PW). All senders start at the same CLOCK_TAI instant, after every receiver is listening.
Output: <pkg>/results/results-<YYYY-MM-DD>/results_<node>.log and results.md (per-flow delivery,
latency, jitter, deadline misses).
"""

import argparse
import datetime
import json
import os
import re
import subprocess
import sys
import threading
import time

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(REPO, "Network-Configure-Manager"))
import configureManager as cm  # noqa: E402

REMOTE_DIR = "/tmp/spawning-flows-test"
SENDER_RE = re.compile(r"id=(\d+) sender: (\d+) packet\(s\) sent(?:, (\d+) skipped)?")
RECV_RE = re.compile(r"id=(\d+) receiver: (\d+) received, latency ns min/avg/max = (-?\d+)/(-?\d+)/(-?\d+), "
                     r"jitter ns stddev/rfc3550 = (\d+)/(\d+), deadline=(\d+)ns, misses=(\d+), no_nic_ts=(\d+)")
RECV0_RE = re.compile(r"id=(\d+) receiver: 0 packets received")


class Node:
    """Run shell commands on an end station: locally on the CNC, over SSH otherwise."""

    def __init__(self, name, topo):
        self.name, self.t = name, dict(topo[name])
        if os.environ.get(f"{name}_PW"):  # sudo password override, e.g. S3_PW=... (never stored in a file)
            self.t["password"] = os.environ[f"{name}_PW"]
        self.local = bool(self.t.get("cnc"))
        self.client = None if self.local else cm.ssh_connect(self.t["ip"], self.t["username"],
                                                             self.t.get("password", ""))

    def run(self, cmd, sudo=False, timeout=60):
        if self.local:
            full = f"sudo -n {cmd}" if sudo else cmd  # redirects stay outside sudo: logs owned by the user
            p = subprocess.run(full, shell=True, capture_output=True, text=True, timeout=timeout)
            return p.returncode, p.stdout, p.stderr
        if sudo:
            cmd = f"sudo -S -p '' sh -c {sh_quote(cmd)}"
        stdin, stdout, stderr = self.client.exec_command(cmd, timeout=timeout)
        if sudo:
            stdin.write(self.t.get("password", "") + "\n")
            stdin.flush()
            stdin.channel.shutdown_write()  # a wrong password then fails instead of waiting for a retry
        out, err = stdout.read().decode(), stderr.read().decode()
        return stdout.channel.recv_exit_status(), out, err

    def put(self, files):
        self.run(f"mkdir -p {REMOTE_DIR}")
        sftp = self.client.open_sftp()
        for local, name in files:
            sftp.put(local, f"{REMOTE_DIR}/{name}")
        sftp.close()

    def get(self, name, local):
        sftp = self.client.open_sftp()
        sftp.get(f"{REMOTE_DIR}/{name}", local)
        sftp.close()


def sh_quote(s):
    return "'" + s.replace("'", "'\\''") + "'"


def nic_ifaces(endpoints, node):
    """VLAN interfaces of a node's streams and the physical NIC under them."""
    vlans = sorted({s["iface"] for s in endpoints[node]["streams"].values()})
    return vlans, sorted({v.split(".")[0] for v in vlans})


def preflight(nodes, endpoints):
    """abort if a generator is still running; record TAI offset and PTP state per node; require the
    launch-time queues and map socket priority 5 to PCP 6 on the VLANs."""
    info = {}
    for n in nodes:
        vlans, nics = nic_ifaces(endpoints, n.name)
        n.run("sysctl -qw net.core.rmem_max=33554432", sudo=True)  # lets gen_traffic.py use 4 MiB SO_RCVBUF
        _, etf, _ = n.run(f"tc qdisc show dev {nics[0]} | grep -c 'etf.*offload on'")
        if etf.strip() != "2":
            sys.exit(f"[FATAL] {n.name}: no launch-time queues on {nics[0]}; run "
                     f"'sudo ./gptp.sh launchtime on' (time-sync-gptp/) there first")
        n.run("; ".join(f"ip link set dev {v} type vlan egress-qos-map 5:6" for v in vlans), sudo=True)
        _, out, _ = n.run("pgrep -af 'gen_traffic.py' | grep -v pgrep || true")
        if out.strip():
            sys.exit(f"[FATAL] gen_traffic.py already running on {n.name}:\n{out}")
        _, tai, _ = n.run("python3 -c \"import time; print(round(time.clock_gettime(time.CLOCK_TAI) - time.time(), 1))\"")
        _, svc, _ = n.run("systemctl is-active tsn-ptp4l tsn-phc2sys | paste -sd/")
        _, last, _ = n.run("journalctl -u tsn-ptp4l -n 1 -o cat --no-pager", sudo=True)
        info[n.name] = {"tai": tai.strip(), "ptp": svc.strip(), "ptp4l": last.strip(), "nic": nics[0]}
        print(f"  {n.name}: TAI offset {tai.strip()} s, ptp4l/phc2sys {svc.strip()}")
    # the common start time is a CLOCK_TAI instant: a node without the 37 s TAI offset would start 37 s late
    bad = [k for k, v in info.items() if abs(float(v["tai"] or 0) - 37) > 0.5]
    if bad:
        sys.exit(f"[FATAL] kernel TAI offset not 37 s on {', '.join(bad)}: run 'sudo ./gptp.sh tai' "
                 f"(time-sync-gptp/) there first")
    return info


def host_counters(nodes, info):
    """per node: UDP receive-buffer drops and launch-time (etf) drops, both cumulative."""
    c = {}
    for n in nodes:
        nic = info[n.name]["nic"]
        _, out, _ = n.run("nstat -az UdpRcvbufErrors | awk '/UdpRcvbufErrors/{print $2}'; "
                          f"tc -s qdisc show dev {nic} | grep -A1 '^qdisc etf' | grep -o 'dropped [0-9]*' "
                          "| awk '{s+=$2} END{print s+0}'")
        v = (out.split() + ["0", "0"])[:2]
        c[n.name] = {"rcvbuf": int(v[0] or 0), "etf": int(v[1] or 0)}
    return c


def switch_drops(topo, pkg):
    """cumulative 'Q DROP' counter of every switch port the package's GCLs gate."""
    ports = {}
    for f in sorted(os.listdir(os.path.join(pkg, "gcl"))):
        m = re.match(r"^(\w+)-(p\d+)\.cfg$", f)
        if m:
            ports.setdefault(m[1], []).append(m[2])
    drops = {}
    for sw, plist in ports.items():
        t = topo.get(sw, {})
        try:
            client = cm.ssh_connect(t["ip"], t.get("username", "root"), t.get("password", ""))
            cmd = "; ".join(f"echo {p} $(ethtool -S sw0{p} | awk '/Q DROP/{{print $3}}')" for p in plist)
            _, stdout, _ = client.exec_command(cmd, timeout=30)
            for line in stdout.read().decode().split("\n"):
                parts = line.split()
                if len(parts) == 2:
                    drops[f"{sw}/{parts[0]}"] = int(parts[1])
            client.close()
        except Exception as e:  # a missing reading must not abort the run
            print(f"  [WARN] {sw}: {e}")
        time.sleep(1)  # the switches' sshd drops rapid reconnects
    return drops


def ping_check(nodes, endpoints):
    """one 2-packet ping per sender stream, all in parallel per node."""
    results = {}
    for n in nodes:
        lines = []
        for s in endpoints[n.name]["streams"].values():
            if s["role"] == "sender":
                lines.append(f"(ping -I {s['iface']} -c 2 -W 2 {s['peer_ip']} >/dev/null 2>&1 "
                             f"&& echo {s['flow_id']} OK || echo {s['flow_id']} FAIL) &")
        _, out, _ = n.run(" ".join(lines) + " wait", timeout=60)
        for line in out.split("\n"):
            if line.strip():
                fid, res = line.split()
                results[int(fid)] = (n.name, res)
    bad = {f: v for f, v in results.items() if v[1] != "OK"}
    print(f"  {len(results)} sender routes pinged, {len(bad)} failed" + (f": {sorted(bad)}" if bad else ""))
    return results


def run_traffic(nodes, pkg, out_dir, duration, lead, extra):
    files = [(os.path.join(HERE, "gen_traffic.py"), "gen_traffic.py")] + [
        (os.path.join(pkg, f), f) for f in ("schedule.json", "endpoints.json", "basetime.json")]
    for n in nodes:
        if not n.local:
            n.put(files)
    start_at = time.clock_gettime(time.CLOCK_TAI) + lead
    print(f"  senders start at TAI {start_at:.3f} ({lead} s from now), run {duration} s")

    def one(n):
        log = os.path.join(out_dir, f"results_{n.name}.log")
        args = f"--node {n.name} --run --duration {duration} --start-at {start_at:.6f} {extra}"
        if n.local:
            cmd = (f"python3 {HERE}/gen_traffic.py --schedule {pkg}/schedule.json "
                   f"--endpoints {pkg}/endpoints.json --basetime {pkg}/basetime.json {args} > {log} 2>&1")
            n.run(cmd, sudo=True, timeout=duration + lead + 60)
        else:
            cmd = (f"cd {REMOTE_DIR} && python3 gen_traffic.py --schedule schedule.json "
                   f"--endpoints endpoints.json --basetime basetime.json {args} > run_{n.name}.log 2>&1")
            n.run(cmd, sudo=True, timeout=duration + lead + 60)
            n.get(f"run_{n.name}.log", log)

    threads = [threading.Thread(target=one, args=(n,)) for n in nodes]
    for t in threads:
        t.start()
    for t in threads:
        t.join()


def parse_logs(out_dir, node_names):
    sent, recv, skipped = {}, {}, {}
    for name in node_names:
        path = os.path.join(out_dir, f"results_{name}.log")
        if not os.path.exists(path):
            continue
        for line in open(path):
            if m := SENDER_RE.search(line):
                sent[int(m[1])] = int(m[2])
                skipped[int(m[1])] = int(m[3] or 0)
            elif m := RECV_RE.search(line):
                v = [int(x) if x is not None else None for x in m.groups()]
                recv[v[0]] = dict(node=name, n=v[1], min=v[2], avg=v[3], max=v[4],
                                  sd=v[5], rfc=v[6], deadline=v[7], miss=v[8], no_ts=v[9])
            elif m := RECV0_RE.search(line):
                recv[int(m[1])] = dict(node=name, n=0)
    return sent, recv, skipped


def pct(a, b):
    return 100.0 * a / b if b else 0.0


def write_report(out_dir, pkg, schedule, sent, recv, skipped, info, pings, duration, started, mode, before, after):
    flows = sorted(schedule["flows"], key=lambda f: f["id"])
    us = lambda ns: f"{ns / 1000:.1f}"  # noqa: E731
    rows, tot_sent, tot_recv, tot_miss = [], 0, 0, 0
    per_node = {}
    for i, f in enumerate(flows, 1):
        s, r = sent.get(f["id"], 0), recv.get(f["id"])
        route = f"{f['src']}→{f['dst']}"
        if r is None:
            rows.append(f"| {i} | {f['id']} | {route} | {f['pcp']} | {f['size']} | {us(f['period'])} | "
                        f"{us(f['deadline'])} | {us(f.get('e2e_ns', 0))} | {s} | – | – | – | – | – | – | – | – |")
            continue
        n = r["n"] + (r.get("no_ts") or 0)
        tot_sent, tot_recv = tot_sent + s, tot_recv + n
        pn = per_node.setdefault(r["node"], dict(flows=0, sent=0, recv=0, miss=0, lat=0))
        pn["flows"] += 1; pn["sent"] += s; pn["recv"] += n
        if n:
            tot_miss += r["miss"]; pn["miss"] += r["miss"]; pn["lat"] += r["avg"] * r["n"]
            rows.append(f"| {i} | {f['id']} | {route} | {f['pcp']} | {f['size']} | {us(f['period'])} | "
                        f"{us(f['deadline'])} | {us(f.get('e2e_ns', 0))} | {s} | {n} | {pct(n, s):.2f}% | "
                        f"{us(r['min'])} / {us(r['avg'])} / {us(r['max'])} | {us(r['sd'])} | {us(r['rfc'])} | "
                        f"{r['miss']} | {pct(r['miss'], r['n']):.2f}% | {r['no_ts']} |")
        else:
            rows.append(f"| {i} | {f['id']} | {route} | {f['pcp']} | {f['size']} | {us(f['period'])} | "
                        f"{us(f['deadline'])} | {us(f.get('e2e_ns', 0))} | {s} | 0 | 0.00% | – | – | – | – | – | – |")

    met = sum(1 for f in flows if (r := recv.get(f["id"])) and r["n"] and r["miss"] == 0)
    name = os.path.relpath(pkg, os.path.join(REPO, "GCL_Schedules"))
    L = [f"# Traffic run: {name}, {started:%Y-%m-%d %H:%M}", "",
         f"{len(flows)} flows, {duration} s, S1/S2/S3 concurrently, all senders starting at the same "
         f"TAI instant on the GCL grid (`basetime.json`). Mode: {mode}. Raw output: `results_<node>.log`.", "",
         "## Summary", "",
         f"- Delivered: **{tot_recv} / {tot_sent} packets ({pct(tot_recv, tot_sent):.2f}%)**",
         f"- Deadline misses: **{tot_miss} ({pct(tot_miss, tot_recv):.2f}% of received)**; "
         f"flows with zero misses: {met} / {len(flows)}",
         "", "| receiving node | flows | delivered | avg latency (µs) | deadline misses |", "|---|---|---|---|---|"]
    for nn in sorted(per_node):
        p = per_node[nn]
        L.append(f"| {nn} | {p['flows']} | {pct(p['recv'], p['sent']):.2f}% | "
                 f"{p['lat'] / p['recv'] / 1000 if p['recv'] else 0:.1f} | {pct(p['miss'], p['recv']):.2f}% |")
    L += ["", "Setup at start:", ""]
    for nn in sorted(info):
        v = info[nn]
        L.append(f"- {nn}: ptp4l/phc2sys {v['ptp']}, CLOCK_TAI − UTC {v['tai']} s"
                 + (f", ptp4l `{v['ptp4l']}`" if v["ptp4l"] else ""))
    if pings:
        bad = sorted(f for f, v in pings.items() if v[1] != "OK")
        L.append(f"- Connectivity: {len(pings) - len(bad)} / {len(pings)} sender routes answered ping"
                 + (f" (failed: {', '.join(map(str, bad))})" if bad else ""))
    L += ["", "## Drop counters (during the run)", "",
          "| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |",
          "|---|---|---|---|"]
    skip_by_node = {}
    for f in flows:
        if f["src"] in after["hosts"]:
            skip_by_node[f["src"]] = skip_by_node.get(f["src"], 0) + skipped.get(f["id"], 0)
    for nn in sorted(after["hosts"]):
        b, a = before["hosts"][nn], after["hosts"][nn]
        L.append(f"| {nn} | {a['rcvbuf'] - b['rcvbuf']} | {a['etf'] - b['etf']} | {skip_by_node.get(nn, 0)} |")
    sw = {k: after["switches"][k] - before["switches"].get(k, 0) for k in after["switches"]}
    nz = {k: v for k, v in sw.items() if v}
    L += ["", f"Switch queue drops (`ethtool -S` Q DROP) on the {len(sw)} gated ports: "
          + (", ".join(f"{k} +{v}" for k, v in sorted(nz.items())) if nz else "none") + "."]
    L += ["", "## Per flow", "",
          "Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC "
          "sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC "
          "clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end "
          "bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between "
          "consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without "
          "a hardware timestamp (counted as received, left out of latency).", "",
          "| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | "
          "received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | "
          "deadline misses | miss % | no NIC ts |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"] + rows
    with open(os.path.join(out_dir, "results.md"), "w") as fh:
        fh.write("\n".join(L) + "\n")
    print("\n".join(L[:14]))


def main():
    ap = argparse.ArgumentParser(description="Run gen_traffic.py on all end stations and write dated results")
    ap.add_argument("--pkg", required=True, help="schedule package dir (schedule.json, endpoints.json, basetime.json)")
    ap.add_argument("--topology", default=os.path.join(REPO, "network-topology", "network-topology-rtas-2027.json"))
    ap.add_argument("--duration", type=int, default=30)
    ap.add_argument("--lead", type=float, default=8, help="seconds from launch to the common sender start")
    ap.add_argument("--ping", action="store_true", help="ping every sender route first")
    ap.add_argument("--rt", action=argparse.BooleanOptionalAction, default=True,
                    help="real-time sender/receiver processes (default; see gen_traffic.py)")
    args = ap.parse_args()

    pkg = os.path.abspath(args.pkg)
    for f in ("schedule.json", "endpoints.json", "basetime.json"):
        if not os.path.exists(os.path.join(pkg, f)):
            sys.exit(f"[FATAL] {pkg}/{f} missing")
    topo = json.load(open(args.topology))
    endpoints = json.load(open(os.path.join(pkg, "endpoints.json")))
    schedule = json.load(open(os.path.join(pkg, "schedule.json")))
    names = sorted(n for n in endpoints if endpoints[n].get("streams"))

    started = datetime.datetime.now()
    out_dir = os.path.join(pkg, "results", started.strftime("results-%Y-%m-%d"))
    k = 2
    while os.path.exists(out_dir):  # second run on the same day: results-<date>_2, _3, ...
        out_dir = os.path.join(pkg, "results", started.strftime("results-%Y-%m-%d") + f"_{k}")
        k += 1
    os.makedirs(out_dir)
    print(f"Results: {out_dir}\nConnecting to {', '.join(names)} ...")
    nodes = [Node(n, topo) for n in names]
    print("Preflight:")
    info = preflight(nodes, endpoints)
    pings = None
    if args.ping:
        print("Connectivity:")
        pings = ping_check(nodes, endpoints)
    print("Counters before:")
    before = {"hosts": host_counters(nodes, info), "switches": switch_drops(topo, pkg)}
    print("Traffic:")
    extra = "--rt" if args.rt else "--no-rt"
    run_traffic(nodes, pkg, out_dir, args.duration, args.lead, extra)
    print("Counters after:")
    after = {"hosts": host_counters(nodes, info), "switches": switch_drops(topo, pkg)}
    sent, recv, skipped = parse_logs(out_dir, names)
    mode = "NIC launch time, NIC RX timestamps" + (", real-time processes" if args.rt else "")
    print()
    write_report(out_dir, pkg, schedule, sent, recv, skipped, info, pings, args.duration, started,
                 mode, before, after)
    print(f"\nFull report: {os.path.join(out_dir, 'results.md')}")


if __name__ == "__main__":
    main()
