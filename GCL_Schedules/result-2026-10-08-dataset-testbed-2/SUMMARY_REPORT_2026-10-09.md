# Summary report: result-2026-10-08-dataset-testbed-2 on the physical testbed

All six schedule packages for dataset-testbed 2 were deployed and measured on the 8-switch
testbed on 2026-10-09. Per-package numbers and per-flow details:
[TESTBED_RESULTS_2026-10-09.md](TESTBED_RESULTS_2026-10-09.md); full per-flow reports:
`<package>/results/results-<date>/results.md` (the latest run of each package).

## Bottom line

- **No package delivered everything**, because one physical route -- **S2→S3 over
  sw08-sw06-sw03-sw01** -- was blocked by MSTP in every package that uses it (all six, 1-7 flows
  each). This is a network-configuration fault, not a schedule fault (see below).
- **Leaving that route out, four of the six schedules deliver 99.99-100% of their frames**, and
  the deadline misses that remain come from specific flows of the C9-on and SMT C9-off schedules.
- **SMT C9-on is the only package with all routes up: 100.00% delivered, 14 misses** (isolated
  late frames of one flow).
- **Problem 3 heuristic C9-off is the outlier** (27.44%): besides the blocked route, sw08 dropped
  almost all traffic into S2 and S2's pcp-6 traffic -- the known, still unexplained sw08 problem.

## Results

| package | approach | flows | routes OK | delivered | deadline misses | without the S2→S3 route: delivered / misses |
|---|---|---|---|---|---|---|
| `smt-c9-off/2-t3600-c9off-minlat` | SMT, C9 off | 11 | 10/11 | 92.59% | 75,001 (8.00%) | **100.00%** / 75,001 |
| `smt-c9-on/2-fair-retimed-c9on` | SMT, C9 on | 11 | 11/11 | **100.00%** | **14 (0.00%)** | 100.00% / 14 |
| `prob3-heuristic-c9-off/2-heuristic-c9off-matrix` | Problem 3 heuristic, C9 off | 22 | 15/22 | 27.44% | 2,527 (0.56%) | 37.72% / 2,527 |
| `prob3-heuristic-c9-on/2-heuristic-c9on-matrix` | Problem 3 heuristic, C9 on | 25 | 18/25 | 76.92% | 4 (0.00%) | **99.99%** / 4 |
| `prob3-rl-c9-off/2-rl-c9off-matrix` | Problem 3 RL, C9 off | 26 | 22/26 | 88.23% | 1 (0.00%) | **99.99%** / 1 |
| `prob3-rl-c9-on/2-rl-c9on-matrix` | Problem 3 RL, C9 on | 32 | 25/32 | 82.35% | 149,986 (7.14%) | **100.00%** / 149,986 |

"Without the S2→S3 route" counts only the flows whose route was not blocked (all S2→S3 flows ride
the one blocked path). The few lost frames that remain there (16-139 per package) are host-side:
sender launch-time (etf) drops and late sends; the switches dropped nothing except in the
heuristic C9-off package.

## Where the deadline misses come from

| package | flow(s) | what happens |
|---|---|---|
| SMT C9-off | flow 7 (S3→S1, 400 µs period) | every frame held exactly one period at sw01 or sw02 (433.7 µs vs a 400 µs deadline), although `deploy-GCL/check_schedule.py` passes the package; not yet explained |
| SMT C9-off / C9-on | flow 4 (S1→S3) | 7 / 14 isolated frames per 30 s held one 800 µs cycle (up to 834 µs) |
| Problem 3 RL C9-on | flows 14 (S3→S2) and 18 (S2→S1), 200 µs period | exactly half of each flow's frames late (latency up to ~220 µs): one of the two instances per window pattern misses its window -- the same C9-on effect seen in earlier tests (windows spaced for cut-through forwarding on store-and-forward switches) |
| Problem 3 heuristic C9-off | flows into S2 and S2's pcp-6 flows | the few frames that got through waited 0.8-3 s at sw08 (see sw08 below) |

## Open problems

1. **S2→S3 route blocked by MSTP (all packages).** Each route gets its own MSTI, rooted at the
   route's last switch (sw01 for S2→S3). sw01's CIST root port (port 4, towards sw03, the CIST
   root) is exactly where the route enters sw01, and mstpd gives that port the *Master* role in
   the route's MSTI; sw03 then reaches the MSTI root via sw04 instead, and sw06's port to sw03
   ends up Alternate/discarding. The region is consistent (one digest) and all ports are now
   point-to-point, so neither of those causes it. Fix to try next: pick each MSTI's root (or the
   CIST root/costs) so the root's CIST root port never lies on the route, then rerun.
2. **sw08 drops (Problem 3 heuristic C9-off).** 560,893 frames dropped on sw08 port 2 (to S2) and
   186,346 on port 5 (to sw07); delivered frames waited up to 3 s, so a queue on sw08 effectively
   never opened. Seen before on another package (`prob3-rl-c9-on/1-rl-c9on-matrix-S1S2`: holding
   only sw08's gates open removed the loss), mechanism still unknown; it did not occur in the
   other five packages.
3. **Flow 7 in SMT C9-off** (above): needs a per-hop test (widen its window on one switch at a time).

## Problems found and fixed during the runs

- **Split MST region** (`Network-Configure-Manager/configureManager.py`, documented in
  `README.md`): old VLAN-to-tree mappings had split the switches into four MST regions, which
  blocked every S2→S1 flow in some packages. MSTP is now applied to all 8 switches with their
  tables reset first, and every run checks that all switches share one digest (they did).
- **Non point-to-point ports**: six cabled ports (sw01-sw03, sw03-sw06, sw01-sw02, sw02-sw04
  links and the S1/S3 ports) were configured `admin point-to-point no`; `build_mstp()` now sets
  every cabled port to point-to-point. This did not clear problem 1.
- **Report and ping-check crashes** (`Spawning-Flows/run_experiment.py`): unscheduled flows
  crashed the report; stray shell output crashed the ping check.
- **Flow ids**: `offsets.csv` labels Problem 3's admitted extra flows `a-<n>`, which match nothing
  in `schedule.json`; the admitted flow list is now built from `schedule.json`.

Runs made before these fixes were discarded.

## Method

For each package: GCLs pushed and activated on all 27 switch ports (all live); the scheduled flows
admitted (VLANs, addresses, MSTP; all switches in one region) after a full teardown of the
previous package; leftover VLAN interfaces on S1/S2/S3 removed; every route pinged; then 30 s of
traffic on S1, S2, S3 at once, sent at each flow's scheduled time with NIC launch time and
timestamped by the receiving NIC. Deadline = period.

These packages were generated before the measured hardware profile (per-hop delay 4,000 ns, no
propagation delay, against the measured 4,020 + 80 ns).
