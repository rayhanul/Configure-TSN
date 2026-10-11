"""Combined testbed table of every package in a result folder.

    python3 summarize_testbed.py <result-dir> [date] [--run latest|first] [--groups G ...]
                                 [--include PKG_DIR ...] [--stdout]
        -> <result-dir>/TESTBED_RESULTS_<date>.md (or stdout)

--run picks each package's latest (default) or first results-* run; --include adds packages from
other result folders (e.g. unchanged C9-off packages of an earlier round); --groups limits the table
to these groups (smt-c9-off, rl-c9-on, ...). Other scripts import it: package_stats() measures one
run, tables() renders the main table, the details table and the per-flow notes.
"""
import argparse, datetime, glob, json, os, re, sys

ORDER = ["smt-c9-off", "smt-c9-on", "heuristic-c9-off", "heuristic-c9-on", "rl-c9-off", "rl-c9-on",
         "prob3-heuristic-c9-off", "prob3-heuristic-c9-on", "prob3-rl-c9-off", "prob3-rl-c9-on"]
LABEL = {"smt": "SMT", "heuristic": "heuristic", "rl": "RL",
         "prob3-heuristic": "Problem 3 heuristic", "prob3-rl": "Problem 3 RL"}

LEGEND = (
    "Rows in pipeline order, each approach C9 off then on. **Rank** orders the packages by deadline "
    "misses, then frames lost, then max latency (1 = best). **Flows** = admitted / offered: every flow "
    "of the dataset's base flow set for SMT, heuristic and RL; the base schedule's flows plus the "
    "arriving candidates for Problem 3. **Lost** = sent − received. **Deadline misses** = received frames whose "
    "latency exceeded their flow's deadline (deadline = period), with their share of received frames. "
    "**Latency** = receiver NIC's RX timestamp − sender NIC's launch time over all received frames "
    "(min / frame-weighted avg / max). **Jitter** = per-flow standard deviation of latency: best "
    "flow / average over the package's flows / worst flow.")
DETAILS_LEGEND = (
    "**Received %** shows a lost frame even when it rounds to 100%. **No NIC ts** = received frames "
    "without a hardware timestamp (left out of latency). **Jitter RFC 3550** = mean |Δ latency| between "
    "consecutive frames, best flow / average / worst flow. **Worst latency, % of deadline** = the largest max "
    "latency / deadline over the package's flows. **Above e2e bound** = flows whose max latency exceeded "
    "the scheduler's own end-to-end bound.")


def label(group, many=False, pkg=""):
    base, _, c9 = group.rpartition("-c9-")
    name = f"{LABEL.get(base, base)} C9-{c9}" if c9 else group
    return f"{name} ({pkg})" if many else name


def num(x):
    x = x.strip().replace(",", "")
    return int(x) if x.isdigit() else 0


def flows_offered(pkg):
    """(admitted, offered) for a package directory."""
    flows = json.load(open(os.path.join(pkg, "schedule.json")))["flows"]
    admitted = sum(1 for f in flows if f.get("scheduled"))
    rep = os.path.join(pkg, "report.md")
    if os.path.exists(rep):                       # Problem 3: base schedule + arriving candidates
        t = open(rep).read()
        w = re.search(r"^\| W \(base, unchanged\) \| (\d+) \|", t, re.M)
        a = re.search(r"^\| \+ this run's arrivals \| \d+ \| (\d+) \|", t, re.M)
        if w and a:
            return admitted, int(w[1]) + int(a[1])
    return admitted, len(flows)


def package_stats(pkg, run_md):
    """Every number of the tables for one package and one run (results.md)."""
    t = open(run_md).read()
    admitted, offered = flows_offered(pkg)
    hdr, s = None, dict(sent=0, rx=0, miss=0, nots=0, lmin=None, lmax=0.0, wsum=0.0,
                        jsd=[], jrfc=[], worst=0.0, above=0, bad=[])
    for line in t.splitlines():
        c = [x.strip() for x in line.split("|")][1:-1]
        if c and c[0] == "#":
            hdr = c
            continue
        if not (hdr and c and c[0].isdigit() and len(c) == len(hdr)):
            continue
        r = dict(zip(hdr, c))
        if r.get("received", "–") in ("–", "") or num(r.get("sent", "0")) == 0:
            continue                                          # not scheduled in this package
        sent, rx, miss = num(r["sent"]), num(r["received"]), num(r.get("deadline misses", "0"))
        s["sent"] += sent; s["rx"] += rx; s["miss"] += miss; s["nots"] += num(r.get("no NIC ts", "0"))
        lat = r.get("latency min / avg / max (µs)", "–")
        if lat.count("/") == 2:
            mn, av, mx = (float(v) for v in lat.split("/"))
            s["lmin"] = mn if s["lmin"] is None else min(s["lmin"], mn)
            s["lmax"] = max(s["lmax"], mx); s["wsum"] += av * rx
            dl = float(r.get("deadline (µs)", "0") or 0)
            if dl:
                s["worst"] = max(s["worst"], mx / dl)
            e2e = r.get("schedule e2e (µs)", "–")
            if e2e not in ("–", "") and mx > float(e2e):
                s["above"] += 1
        for key, dst in (("jitter stddev (µs)", "jsd"), ("jitter RFC 3550 (µs)", "jrfc")):
            v = r.get(key, "–")
            if v not in ("–", ""):
                s[dst].append(float(v))
        if miss or sent - rx > 100:
            s["bad"].append(f"flow {r['id']} ({r.get('route', '')}): {rx}/{sent} received, {miss} misses, "
                            f"latency {lat} µs")
    ping = re.search(r"Connectivity: (\d+) / (\d+) sender routes answered ping(?: \(failed: ([^)]+)\))?", t)
    q = re.search(r"Q DROP\) on the \d+ gated ports: (.*)\.", t)
    return dict(admitted=admitted, offered=offered, **s,
                ping=(f"{ping[1]}/{ping[2]}" + (f" (failed: {ping[3]})" if ping[3] else "")) if ping else "?",
                qdrop=q[1] if q else "?", run=run_md)


def pct(rx, sent):
    if not sent:
        return "–"
    if rx == sent:
        return "100.0000%"
    for d in range(4, 9):                      # enough decimals that a lost frame never shows 100%
        v = f"{100 * rx / sent:.{d}f}"
        if float(v) < 100:
            return v + "%"
    return f"{100 * rx / sent}%"


def f1(x):
    return f"{x:.1f}"


def tables(entries, base):
    """entries: [(group, pkg_dir, stats or None)] in display order -> markdown lines."""
    many = {g: sum(1 for e in entries if e[0] == g) > 1 for g, _, _ in entries}
    done = [e for e in entries if e[2]]
    order = sorted(done, key=lambda e: (e[2]["miss"], e[2]["sent"] - e[2]["rx"], e[2]["lmax"]))
    rank = {id(e): i + 1 for i, e in enumerate(order)}
    for i in range(1, len(order)):                             # ties share a rank
        a, b = order[i - 1][2], order[i][2]
        if (a["miss"], a["sent"] - a["rx"], a["lmax"]) == (b["miss"], b["sent"] - b["rx"], b["lmax"]):
            rank[id(order[i])] = rank[id(order[i - 1])]
    L = ["| Rank | Package | Flows (admitted / offered) | Sent | Received | Lost | Deadline misses (%) | "
         "Latency min / avg / max (µs) | Jitter stddev best / avg / worst flow (µs) |",
         "|---|---|---|---|---|---|---|---|---|"]
    T = [0, 0, 0]
    for e in entries:
        g, pkg, s = e
        name = label(g, many[g], os.path.basename(pkg.rstrip("/")))
        if not s:
            L.append(f"| – | {name} | – | – | – | – | not run | – | – |")
            continue
        T = [T[0] + s["sent"], T[1] + s["rx"], T[2] + s["miss"]]
        lat = (f"{f1(s['lmin'])} / {f1(s['wsum'] / s['rx'])} / {f1(s['lmax'])}" if s["rx"] and s["lmin"] is not None
               else "–")
        jit = f"{f1(min(s['jsd']))} / {f1(sum(s['jsd']) / len(s['jsd']))} / {f1(max(s['jsd']))}" if s["jsd"] else "–"
        L.append(f"| {rank[id(e)]} | {name} | {s['admitted']} / {s['offered']} | {s['sent']:,} | {s['rx']:,} | "
                 f"{s['sent'] - s['rx']:,} | {s['miss']:,} ({100 * s['miss'] / s['rx'] if s['rx'] else 0:.2f}%) | "
                 f"{lat} | {jit} |")
    if T[0] and len(done) > 1:
        L.append(f"| | **Total** | | **{T[0]:,}** | **{T[1]:,}** | **{T[0] - T[1]:,}** | "
                 f"**{T[2]:,} ({100 * T[2] / T[1] if T[1] else 0:.2f}%)** | | |")
    D = ["| Package | Received % | No NIC ts | Jitter RFC 3550 best / avg / worst flow (µs) | Worst latency, % of deadline | "
         "Above e2e bound | Routes ping OK | Switch queue drops | Run (`results.md` inside) |",
         "|---|---|---|---|---|---|---|---|---|"]
    notes = []
    for g, pkg, s in entries:
        if not s:
            continue
        name = label(g, many[g], os.path.basename(pkg.rstrip("/")))
        rfc = f"{f1(min(s['jrfc']))} / {f1(sum(s['jrfc']) / len(s['jrfc']))} / {f1(max(s['jrfc']))}" if s["jrfc"] else "–"
        run = os.path.relpath(os.path.dirname(s["run"]), base)
        D.append(f"| {name} | {pct(s['rx'], s['sent'])} | {s['nots']:,} | {rfc} | {100 * s['worst']:.0f}% | "
                 f"{s['above']} | {s['ping']} | {s['qdrop']} | `{run}` |")
        notes.append(f"- **{name}**: " + ("; ".join(s["bad"]) if s["bad"]
                                          else "no flow lost >100 frames or missed a deadline"))
    return L, D, notes


def collect(base, groups=ORDER, run="latest", include=()):
    """[(group, pkg_dir, stats or None)] for the packages of base (+ include), in ORDER."""
    pkgs = [(g, p) for g in groups for p in sorted(glob.glob(os.path.join(base, g, "*", "")))]
    for p in include:
        p = p.rstrip("/") + "/"
        pkgs.append((os.path.basename(os.path.dirname(p.rstrip("/"))), p))
    pkgs.sort(key=lambda gp: ORDER.index(gp[0]) if gp[0] in ORDER else len(ORDER))
    out = []
    for g, p in pkgs:
        runs = [r for r in glob.glob(os.path.join(p, "results", "results-*", "results.md"))
                if re.search(r"Delivered: \*\*", open(r).read())]
        runs.sort(key=lambda r: (os.path.basename(os.path.dirname(r)).split("_")[0],
                                 int((os.path.basename(os.path.dirname(r)).split("_") + ["1"])[1])))
        out.append((g, p, package_stats(p, runs[0 if run == "first" else -1]) if runs else None))
    # a base package derived from another (C9-on retimed from C9-off, enlarged from SMT) lists only the
    # flows it carries: offer every base package the dataset's full base flow set, the largest one here
    base = [len(json.load(open(os.path.join(p, "schedule.json")))["flows"])
            for g, p, _ in out if not g.startswith("prob3")]
    for g, p, st in out:
        if st and base and not g.startswith("prob3"):
            st["offered"] = max(base)
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("base")
    ap.add_argument("date", nargs="?", default=datetime.date.today().isoformat())
    ap.add_argument("--run", choices=["latest", "first"], default="latest")
    ap.add_argument("--groups", nargs="*", default=ORDER)
    ap.add_argument("--include", nargs="*", default=[])
    ap.add_argument("--stdout", action="store_true")
    a = ap.parse_args()
    entries = collect(a.base, a.groups, a.run, a.include)
    main_t, det, notes = tables(entries, a.base)
    L = [f"# Testbed results: {os.path.basename(a.base.rstrip('/'))} ({a.date})", "",
         "Each package's GCLs were deployed on all of its switch ports, its scheduled flows admitted "
         "(VLANs + MSTP, all switches in one MST region), every route pinged, then 30 s of traffic on S1, "
         "S2, S3 at once (NIC launch time, NIC RX timestamps). "
         f"{'First' if a.run == 'first' else 'Latest'} run of each package.", "", LEGEND, ""] + main_t + \
        ["", "## Details", "", DETAILS_LEGEND, ""] + det + ["", "## Flows with misses or notable loss", ""] + notes
    text = "\n".join(L) + "\n"
    if a.stdout:
        sys.stdout.write(text)
    else:
        out = os.path.join(a.base, f"TESTBED_RESULTS_{a.date}.md")
        open(out, "w").write(text)
        print(text)


if __name__ == "__main__":
    main()
