"""Combined testbed table of every package in a result folder (latest results-* run of each package).
    python3 summarize_testbed.py <result-dir> [date]   -> <result-dir>/TESTBED_RESULTS_<date>.md"""
import datetime, glob, json, os, re, sys
B = sys.argv[1]
num = lambda x: int(x) if x.strip().isdigit() else 0
ORDER = ["smt-c9-off", "smt-c9-on", "heuristic-c9-off", "heuristic-c9-on", "rl-c9-off", "rl-c9-on",
         "prob3-heuristic-c9-off", "prob3-heuristic-c9-on", "prob3-rl-c9-off", "prob3-rl-c9-on"]
DATE = sys.argv[2] if len(sys.argv) > 2 else datetime.date.today().isoformat()
L = [f"# Testbed results: {os.path.basename(B.rstrip('/'))} ({DATE})", "",
     "Each package's GCLs were deployed on all of its switch ports (all live), its scheduled flows admitted "
     "(VLANs + MSTP, all 8 switches in one MST region), leftover VLAN interfaces removed on S1/S2/S3, every "
     "route pinged, then 30 s of traffic on S1, S2, S3 at once (NIC launch time, NIC RX timestamps). Full per-flow "
     "reports: `<package>/results/results-<date>/results.md`.", "",
     "| package | approach | flows | routes ping OK | delivered | lost | deadline misses | flows with misses | switch queue drops |",
     "|---|---|---|---|---|---|---|---|---|"]
details = []
for grp in ORDER:
    for pkg in sorted(glob.glob(f"{B}/{grp}/*/")):
        runs = sorted(glob.glob(pkg + "results/results-*/results.md"), key=os.path.getmtime)
        name = f"{grp}/{os.path.basename(pkg.rstrip('/'))}"
        n_sched = sum(1 for f in json.load(open(pkg + "schedule.json"))["flows"] if f.get("scheduled"))
        if not runs or not re.search(r"Delivered: \*\*", open(runs[-1]).read()):
            L.append(f"| `{name}` | {grp} | {n_sched} | pending | | | | | |"); continue
        t = open(runs[-1]).read()
        m = re.search(r"Delivered: \*\*(\d+) / (\d+) packets \(([\d.]+)%\)", t)
        d = re.search(r"Deadline misses: \*\*(\d+) \(([\d.]+)% of received\)", t)
        pg = re.search(r"Connectivity: (\d+) / (\d+) sender routes answered ping(?: \(failed: ([^)]+)\))?", t)
        q = re.search(r"Q DROP\) on the \d+ gated ports: (.*)\.", t)
        rows = [r.split("|") for r in t.splitlines() if re.match(r"\| \d+ \| \d+ \|", r)]
        bad = []
        for r in rows:
            fid, route, sent, recv, miss = r[2].strip(), r[3].strip(), r[9].strip(), r[10].strip(), r[15].strip()
            if recv == "–":
                continue                                   # not scheduled in this package
            lost = num(sent) - num(recv)
            if num(miss) or lost > 100:
                bad.append(f"flow {fid} ({route}): {recv}/{sent} received, {num(miss)} misses, latency {r[12].strip()} µs")
        n_bad = sum(1 for r in rows if r[10].strip() not in ("–",) and num(r[15]))
        lost = int(m[2]) - int(m[1])
        L.append(f"| `{name}` | {grp} | {n_sched} | {(pg[1] + '/' + pg[2] + (' (failed: ' + pg[3] + ')' if pg[3] else '')) if pg else '?'} | "
                 f"{m[3]}% | {lost:,} | {int(d[1]):,} ({d[2]}%) | {n_bad} | {q[1] if q else '?'} |")
        details.append(f"- **{name}** (`{os.path.relpath(runs[-1], B)}`): " + ("; ".join(bad) if bad else "no flow lost >100 frames or missed a deadline"))
L += ["", "## Flows with misses or notable loss", ""] + details
out = f"{B}/TESTBED_RESULTS_{DATE}.md"
open(out, "w").write("\n".join(L) + "\n")
print("\n".join(L))
