#!/usr/bin/env bash
# Deploy every schedule package of a result folder on the physical testbed, one by one, measure it, and
# write the combined table <result-dir>/TESTBED_RESULTS_<date>.md.
#
#   S3_PW=... S1_PW=... ./run_testbed.sh <result-dir> [group ...]
#
#   result-dir  e.g. result-2026-10-09-dataset-testbed-4-avgwin (a package = <group>/<name>/ with schedule.json)
#   group       only these groups (smt-c9-off, rl-c9-on, ...); default: all ten
# Environment:
#   S1_PW, S2_PW, S3_PW  sudo passwords of the end stations (empty = passwordless sudo)
#   TOPO       topology file (default: network-topology/network-topology-rtas-2027-tree.json)
#   DURATION   seconds of traffic per package (default 30)
#   STP_QUIET  seconds without any spanning-tree change on all switches before traffic starts (default 15)
#
# Per package: build stream-realizable.csv from schedule.json, push + activate the GCLs, tear down the
# previous package and admit this one (VLANs + MSTP), remove stale VLAN interfaces on S1/S2/S3, ping every
# route, then DURATION s of traffic (run_experiment.py). The per-flow report lands in
# <package>/results/results-<date>[_n]/results.md; the console log of each package in <result-dir>/testbed-logs/.
#
# Before the first run: gPTP synced and launch time on, on every end station
# (time-sync-gptp/gptp.sh launchtime on; ETF_DELTA_NS there must equal the one in Spawning-Flows/gen_traffic.py).
set -euo pipefail
REPO=$(cd "$(dirname "$0")/../.." && pwd)
[ $# -ge 1 ] && [ -d "$1" ] || { sed -n '2,22p' "$0"; exit 1; }
B=$(cd "$1" && pwd); shift
TOPO=$(realpath "${TOPO:-$REPO/network-topology/network-topology-rtas-2027-tree.json}")
DURATION=${DURATION:-30}
GROUPS_=${*:-smt-c9-off smt-c9-on heuristic-c9-off heuristic-c9-on rl-c9-off rl-c9-on \
              prob3-heuristic-c9-off prob3-heuristic-c9-on prob3-rl-c9-off prob3-rl-c9-on}
PW=(--password "S1=${S1_PW:-}" --password "S2=${S2_PW:-}" --password "S3=${S3_PW:-}")
export S1_PW="${S1_PW:-}" S2_PW="${S2_PW:-}" S3_PW="${S3_PW:-}"
LOGS=$B/testbed-logs; mkdir -p "$LOGS"
RAN=0

for GRP in $GROUPS_; do
  for PKG in "$B/$GRP"/*/; do
    PKG=${PKG%/}; [ -f "$PKG/schedule.json" ] || continue
    RAN=$((RAN + 1))
    L=$LOGS/${GRP}_$(basename "$PKG").log; : > "$L"
    echo "=== $(date +%H:%M:%S) $GRP/$(basename "$PKG")"
    # scheduled flows from schedule.json, with the numeric ids gen_traffic.py looks up there
    # (offsets.csv labels Problem 3's admitted extra flows "a-<n>", which match nothing in schedule.json)
    python3 - "$PKG" <<'PY'
import csv, json, sys
pkg = sys.argv[1]; flows = [f for f in json.load(open(pkg + "/schedule.json"))["flows"] if f.get("scheduled")]
with open(pkg + "/stream-realizable.csv", "w", newline="") as fh:
    w = csv.writer(fh); w.writerow(["id", "src", "dst", "route", "size", "period", "deadline", "jitter"])
    for f in flows:
        w.writerow([f["id"], f["src"], f["dst"], "[" + "->".join(f["route"]) + "]", f["size"], f["period"],
                    f["deadline"], f.get("jitter_ns") or f["deadline"]])
PY
    echo "  flows to admit: $(($(wc -l < "$PKG/stream-realizable.csv") - 1))"
    python3 "$REPO/deploy-GCL/configure_gcl.py" --gcl-dir "$PKG/gcl" --topology "$TOPO" --apply >> "$L" 2>&1
    echo "  GCL: $(grep -c ': LIVE' "$L")/$(ls "$PKG/gcl" | wc -l) ports live"
    live=$(grep -c ': LIVE' "$L" || true)
    expected=$(find "$PKG/gcl" -maxdepth 1 -name '*.cfg' | wc -l)
    [ "$live" -eq "$expected" ] || { echo "GCL activation failed: $live/$expected ports"; exit 1; }
    (cd "$REPO/Network-Configure-Manager" &&
     python3 "$TASK_ROOT/configure_batch.py" --topology "$TOPO" --reset --hard --apply "${PW[@]}" >> "$L" 2>&1 &&
     python3 "$TASK_ROOT/configure_batch.py" --topology "$TOPO" --csv "$PKG/stream-realizable.csv" \
             --endpoints "$PKG/endpoints.json" --mstp --apply "${PW[@]}" >> "$L" 2>&1)
    grep -E "MST region|different MST regions" "$L" | sed 's/^/  /'
    # leftover VLAN interfaces of earlier packages answer ARP for the same addresses: remove them
    (cd "$REPO/Spawning-Flows" && python3 - "$PKG" "$TOPO" >> "$L" 2>&1 <<'PY'
import json, sys
import run_experiment as rx
pkg, topo = sys.argv[1], json.load(open(sys.argv[2])); ep = json.load(open(pkg + "/endpoints.json"))
for name in ("S1", "S2", "S3"):
    n = rx.Node(name, topo); want = {s["iface"] for s in ep.get(name, {}).get("streams", {}).values()}
    have = [l.split()[0].split("@")[0] for l in n.run("ip -br link | grep '^enp1s0\\.'")[1].split("\n") if l.strip()]
    extra = [i for i in have if i not in want]
    if extra:
        n.run("; ".join(f"ip link del {i}" for i in extra), sudo=True)
    n.run("for i in $(ip -br link | awk '/^enp1s0\\./{split($1,a,\"@\"); print a[1]}'); do ip neigh flush dev $i; done", sudo=True)
    print("CLEAN", name, "removed", extra)
PY
    )
    # mstpd keeps re-converging for ~25 s after the admit and blocks ports for ~280 ms at a time; traffic
    # started inside that window loses ~1% and sees ~320 ms latencies (2026-10-10), so wait it out
    python3 "$REPO/Network-Configure-Manager/wait_stp_quiet.py" --topology "$TOPO" --quiet "${STP_QUIET:-15}" \
        2>&1 | tee -a "$L" | grep -v -i banner | sed 's/^/  /'
    (cd "$REPO/Spawning-Flows" &&
     python3 run_experiment.py --pkg "$PKG" --topology "$TOPO" --duration "$DURATION" --ping >> "$L" 2>&1)
    grep -E "sender routes pinged|Delivered:|Deadline misses:|Full report" "$L" | sed 's/^/  /'
  done
done
echo "=== $(date +%H:%M:%S) all done: $RAN package(s)"
[ "$RAN" -gt 0 ] || { echo "no package matched: $GROUPS_ (summary not written)"; exit 1; }
TAG=$(date +%F); [ -e "$B/TESTBED_RESULTS_$TAG.md" ] && TAG=$(date +%F_%H%M)   # never overwrite an earlier table
python3 "$REPO/GCL_Schedules/summarize_testbed.py" "$B" "$TAG" > /dev/null &&
  echo "summary: $B/TESTBED_RESULTS_$TAG.md"
