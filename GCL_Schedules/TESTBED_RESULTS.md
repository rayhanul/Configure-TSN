# Testbed results after the fixes

Only runs with all four fixes in place are listed. These are the final round of dataset 4,
2026-10-10: **all 10 packages had 0 deadline misses; 34 of 13.6 million frames were lost**.
Datasets 1-3 have no runs since the fixes (see the end).

The fixes:
**A** pcp 6 and pcp 7 share one NIC launch-time queue (`time-sync-gptp/gptp.sh`);
**B** C9-on schedules wait for store-and-forward (`store_and_forward` in RL-TSN's hw profile);
**C** etf delta 600 µs (`gptp.sh`, `Spawning-Flows/gen_traffic.py`);
**D** wait for the spanning tree to settle after admission (`Network-Configure-Manager/wait_stp_quiet.py`).

Every run: 8 TTTech switches in a tree, 3 end stations (S1, S2, S3), 1 Gb/s, 800 µs GCL cycle, 30 s
of traffic, NIC launch time on send and NIC hardware timestamps on receive. A deadline miss is a
frame whose latency exceeds its deadline (deadline = period); lost = sent but not received.

## Results after the fixes (dataset 4)

Ten packages: SMT, heuristic, RL and Problem 3 (heuristic and RL), each with C9 off and C9 on.

Rows in pipeline order, each approach C9 off then on. **Rank** orders the packages by deadline misses, then frames lost, then max latency (1 = best). **Flows** = admitted / offered: every flow of the dataset's base flow set for SMT, heuristic and RL; the base schedule's flows plus the arriving candidates for Problem 3. **Lost** = sent − received. **Deadline misses** = received frames whose latency exceeded their flow's deadline (deadline = period), with their share of received frames. **Latency** = receiver NIC's RX timestamp − sender NIC's launch time over all received frames (min / frame-weighted avg / max). **Jitter** = per-flow standard deviation of latency: best flow / average over the package's flows / worst flow.

| Rank | Package | Flows (admitted / offered) | Sent | Received | Lost | Deadline misses (%) | Latency min / avg / max (µs) | Jitter stddev best / avg / worst flow (µs) |
|---|---|---|---|---|---|---|---|---|
| 2 | SMT C9-off | 11 / 20 | 1,012,445 | 1,012,445 | 0 | 0 (0.00%) | 66.8 / 90.0 / 133.7 | 0.1 / 0.1 / 0.1 |
| 6 | SMT C9-on | 11 / 20 | 1,012,484 | 1,012,480 | 4 | 0 (0.00%) | 21.0 / 39.1 / 62.1 | 0.1 / 0.1 / 0.2 |
| 10 | heuristic C9-off | 11 / 20 | 1,012,482 | 1,012,473 | 9 | 0 (0.00%) | 19.0 / 73.7 / 134.0 | 0.1 / 0.6 / 5.7 |
| 8 | heuristic C9-on | 11 / 20 | 1,012,448 | 1,012,440 | 8 | 0 (0.00%) | 21.3 / 34.7 / 156.6 | 0.1 / 0.2 / 0.5 |
| 2 | RL C9-off | 11 / 20 | 1,012,488 | 1,012,488 | 0 | 0 (0.00%) | 19.1 / 72.0 / 133.7 | 0.1 / 1.8 / 18.7 |
| 1 | RL C9-on | 11 / 20 | 1,012,483 | 1,012,483 | 0 | 0 (0.00%) | 21.0 / 33.6 / 44.5 | 0.1 / 0.1 / 0.3 |
| 9 | Problem 3 heuristic C9-off | 24 / 50 | 1,612,431 | 1,612,423 | 8 | 0 (0.00%) | 12.8 / 82.4 / 420.7 | 0.1 / 2.5 / 49.9 |
| 7 | Problem 3 heuristic C9-on | 27 / 50 | 1,912,365 | 1,912,361 | 4 | 0 (0.00%) | 9.6 / 38.6 / 408.2 | 0.1 / 0.6 / 4.8 |
| 4 | Problem 3 RL C9-off | 28 / 50 | 2,024,967 | 2,024,967 | 0 | 0 (0.00%) | 9.7 / 67.4 / 235.5 | 0.1 / 2.6 / 25.0 |
| 5 | Problem 3 RL C9-on | 29 / 50 | 2,024,957 | 2,024,956 | 1 | 0 (0.00%) | 9.7 / 36.9 / 139.8 | 0.1 / 2.2 / 49.5 |
| | **Total** | | **13,649,550** | **13,649,516** | **34** | **0 (0.00%)** | | |

### Details

**Received %** shows a lost frame even when it rounds to 100%. **No NIC ts** = received frames without a hardware timestamp (left out of latency). **Jitter RFC 3550** = mean |Δ latency| between consecutive frames, best flow / average / worst flow. **Worst latency, % of deadline** = the largest max latency / deadline over the package's flows. **Above e2e bound** = flows whose max latency exceeded the scheduler's own end-to-end bound.

| Package | Received % | No NIC ts | Jitter RFC 3550 best / avg / worst flow (µs) | Worst latency, % of deadline | Above e2e bound | Routes ping OK | Switch queue drops | Run (`results.md` inside) |
|---|---|---|---|---|---|---|---|---|
| SMT C9-off | 100.0000% | 0 | 0.0 / 0.0 / 0.1 | 67% | 1 | 11/11 | none | `result-2026-10-09-dataset-testbed-4-avgwin/smt-c9-off/4-t3600-c9off-minlat/results/results-2026-10-10_5` |
| SMT C9-on | 99.9996% | 0 | 0.0 / 0.0 / 0.0 | 24% | 1 | 11/11 | none | `result-2026-10-10-dataset-testbed-4-saf/smt-c9-on/4-saf-retimed-c9on/results/results-2026-10-10_3` |
| heuristic C9-off | 99.9991% | 0 | 0.0 / 0.6 / 6.6 | 67% | 0 | 11/11 | none | `result-2026-10-09-dataset-testbed-4-avgwin/heuristic-c9-off/4-matrix-c9off/results/results-2026-10-10_3` |
| heuristic C9-on | 99.9992% | 0 | 0.0 / 0.1 / 0.2 | 39% | 1 | 11/11 | none | `result-2026-10-10-dataset-testbed-4-saf/heuristic-c9-on/4-matrix-c9on/results/results-2026-10-10_2` |
| RL C9-off | 100.0000% | 0 | 0.0 / 3.5 / 37.4 | 67% | 0 | 11/11 | none | `result-2026-10-09-dataset-testbed-4-avgwin/rl-c9-off/4-matrix-c9off/results/results-2026-10-10_3` |
| RL C9-on | 100.0000% | 0 | 0.0 / 0.1 / 0.2 | 21% | 0 | 11/11 | none | `result-2026-10-10-dataset-testbed-4-saf/rl-c9-on/4-matrix-c9on/results/results-2026-10-10_2` |
| Problem 3 heuristic C9-off | 99.9995% | 0 | 0.0 / 4.6 / 99.8 | 75% | 0 | 24/24 | none | `result-2026-10-09-dataset-testbed-4-avgwin/prob3-heuristic-c9-off/4-heuristic-c9off-matrix/results/results-2026-10-10_3` |
| Problem 3 heuristic C9-on | 99.9998% | 0 | 0.0 / 0.8 / 7.3 | 51% | 0 | 27/27 | none | `result-2026-10-10-dataset-testbed-4-saf/prob3-heuristic-c9-on/4-heuristic-c9on-matrix/results/results-2026-10-10_2` |
| Problem 3 RL C9-off | 100.0000% | 0 | 0.0 / 4.8 / 50.0 | 67% | 0 | 28/28 | none | `result-2026-10-09-dataset-testbed-4-avgwin/prob3-rl-c9-off/4-rl-c9off-matrix/results/results-2026-10-10_4` |
| Problem 3 RL C9-on | 99.99995% | 0 | 0.0 / 3.9 / 98.9 | 35% | 0 | 29/29 | none | `result-2026-10-10-dataset-testbed-4-saf/prob3-rl-c9-on/4-rl-c9on-matrix/results/results-2026-10-10_2` |

### Takeaways

- **Deadlines:** 0 misses in all 10 packages (13,649,516 frames received).
- **Delivery:** 34 of 13,649,550 frames lost (0.0002%), all launch-time drops on the
  sending hosts; the switches dropped nothing. Four packages lost none: RL C9-on, SMT C9-off, RL
  C9-off and Problem 3 RL C9-off (the largest, 28 flows).
- **Latency:** C9-on packages average 34-39 µs against 67-90 µs for C9-off; RL C9-on has the lowest
  worst case (44.5 µs, 21% of its deadline) and jitter (0.3 µs worst-flow stddev).
- **Admission:** Problem 3 RL C9-on admits the most flows, 29 of 50.
- **Jitter above a few µs** (up to 49.9 µs stddev) comes from a few flows whose latency differs
  between the instances of a cycle (far-apart min and max); their frames still meet the deadline.
- **Margin:** every frame arrived within 75% of its deadline, within 51% in the C9-on packages.

Each run's full per-flow report is `<run>/results.md`. The causes, the earlier rounds and how each
fix changed the results: [result-2026-10-10-dataset-testbed-4-saf/SUMMARY_REPORT_2026-10-10.md](result-2026-10-10-dataset-testbed-4-saf/SUMMARY_REPORT_2026-10-10.md).

## Not run since the fixes

Datasets 1, 2 and 3. They were generated for the original cabling with loops; the testbed is now
cabled as a tree (`network-topology/network-topology-rtas-2027-tree.json`), so they need
regenerating on it before running.
