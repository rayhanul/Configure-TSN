# Testbed results: rerun-dataset-11-tree-rstp-settled (2026-10-13)

Each package's GCLs were deployed on all of its switch ports, its scheduled flows admitted (VLANs + MSTP, all switches in one MST region), every route pinged, then 30 s of traffic on S1, S2, S3 at once (NIC launch time, NIC RX timestamps). Latest run of each package.

Rows in pipeline order, each approach C9 off then on. **Rank** orders the packages by deadline misses, then frames lost, then max latency (1 = best). **Flows** = admitted / offered: every flow of the dataset's base flow set for SMT, heuristic and RL; the base schedule's flows plus the arriving candidates for Problem 3. **Lost** = sent − received. **Deadline misses** = received frames whose latency exceeded their flow's deadline (deadline = period), with their share of received frames. **Latency** = receiver NIC's RX timestamp − sender NIC's launch time over all received frames (min / frame-weighted avg / max). **Jitter** = per-flow standard deviation of latency: best flow / average over the package's flows / worst flow.

| Rank | Package | Flows (admitted / offered) | Sent | Received | Lost | Deadline misses (%) | Latency min / avg / max (µs) | Jitter stddev best / avg / worst flow (µs) |
|---|---|---|---|---|---|---|---|---|
| 10 | SMT C9-off | 10 / 20 | 937,478 | 937,478 | 0 | 13 (0.00%) | 66.8 / 77.9 / 267.1 | 0.1 / 0.3 / 1.9 |
| 9 | SMT C9-on | 10 / 20 | 937,471 | 937,471 | 0 | 6 (0.00%) | 24.5 / 38.0 / 409.5 | 0.1 / 0.5 / 3.4 |
| 8 | heuristic C9-off | 10 / 20 | 937,438 | 937,422 | 16 | 0 (0.00%) | 28.1 / 61.2 / 108.9 | 0.1 / 0.1 / 0.2 |
| 5 | heuristic C9-on | 10 / 20 | 937,466 | 937,464 | 2 | 0 (0.00%) | 18.5 / 34.2 / 47.4 | 0.1 / 0.4 / 3.1 |
| 1 | RL C9-off | 10 / 20 | 937,464 | 937,464 | 0 | 0 (0.00%) | 28.7 / 70.7 / 109.4 | 0.1 / 0.1 / 0.2 |
| 4 | RL C9-on | 10 / 20 | 937,467 | 937,466 | 1 | 0 (0.00%) | 18.5 / 34.2 / 47.3 | 0.1 / 0.4 / 3.0 |
| 3 | Problem 3 heuristic C9-off | 29 / 50 | 1,912,454 | 1,912,454 | 0 | 0 (0.00%) | 16.7 / 67.3 / 571.6 | 0.1 / 1.7 / 23.6 |
| 2 | Problem 3 heuristic C9-on | 27 / 50 | 1,724,952 | 1,724,952 | 0 | 0 (0.00%) | 15.8 / 43.4 / 299.9 | 0.1 / 5.1 / 126.8 |
| 6 | Problem 3 RL C9-off | 25 / 50 | 1,687,410 | 1,687,408 | 2 | 0 (0.00%) | 28.0 / 91.7 / 309.1 | 0.1 / 1.6 / 27.8 |
| 7 | Problem 3 RL C9-on | 27 / 50 | 1,912,453 | 1,912,446 | 7 | 0 (0.00%) | 15.9 / 43.4 / 173.4 | 0.1 / 4.4 / 72.2 |
| | **Total** | | **12,862,053** | **12,862,025** | **28** | **19 (0.00%)** | | |

## Details

**Received %** shows a lost frame even when it rounds to 100%. **No NIC ts** = received frames without a hardware timestamp (left out of latency). **Jitter RFC 3550** = mean |Δ latency| between consecutive frames, best flow / average / worst flow. **Worst latency, % of deadline** = the largest max latency / deadline over the package's flows. **Above e2e bound** = flows whose max latency exceeded the scheduler's own end-to-end bound.

| Package | Received % | No NIC ts | Jitter RFC 3550 best / avg / worst flow (µs) | Worst latency, % of deadline | Above e2e bound | Routes ping OK | Switch queue drops | Run (`results.md` inside) |
|---|---|---|---|---|---|---|---|---|
| SMT C9-off | 100.0000% | 0 | 0.0 / 0.0 / 0.1 | 134% | 1 | 10/10 | none | `smt-c9-off/11-t3600-c9off-minlat/results/results-2026-10-13` |
| SMT C9-on | 100.0000% | 0 | 0.0 / 0.0 / 0.1 | 102% | 2 | 10/10 | none | `smt-c9-on/11-fair-retimed-c9on/results/results-2026-10-13` |
| heuristic C9-off | 99.9983% | 0 | 0.0 / 0.1 / 0.2 | 36% | 0 | 10/10 | none | `heuristic-c9-off/11-matrix-c9off/results/results-2026-10-13` |
| heuristic C9-on | 99.9998% | 0 | 0.0 / 0.2 / 0.8 | 24% | 0 | 10/10 | none | `heuristic-c9-on/11-matrix-c9on/results/results-2026-10-13` |
| RL C9-off | 100.0000% | 0 | 0.0 / 0.1 / 0.2 | 42% | 0 | 10/10 | none | `rl-c9-off/11-matrix-c9off/results/results-2026-10-13` |
| RL C9-on | 99.9999% | 0 | 0.0 / 0.2 / 0.8 | 24% | 0 | 10/10 | none | `rl-c9-on/11-matrix-c9on/results/results-2026-10-13` |
| Problem 3 heuristic C9-off | 100.0000% | 0 | 0.0 / 2.7 / 42.1 | 71% | 0 | 29/29 | none | `prob3-heuristic-c9-off/11-heuristic-c9off-matrix/results/results-2026-10-13` |
| Problem 3 heuristic C9-on | 100.0000% | 0 | 0.0 / 9.7 / 253.7 | 75% | 0 | 27/27 | none | `prob3-heuristic-c9-on/11-heuristic-c9on-matrix/results/results-2026-10-13` |
| Problem 3 RL C9-off | 99.9999% | 0 | 0.0 / 3.0 / 55.7 | 45% | 0 | 25/25 | none | `prob3-rl-c9-off/11-rl-c9off-matrix/results/results-2026-10-13` |
| Problem 3 RL C9-on | 99.9996% | 0 | 0.0 / 8.3 / 144.4 | 50% | 0 | 27/27 | none | `prob3-rl-c9-on/11-rl-c9on-matrix/results/results-2026-10-13` |

## Flows with misses or notable loss

- **SMT C9-off**: flow 1 (S1→S2): 150000/150000 received, 13 misses, latency 66.8 / 67.0 / 267.1 µs
- **SMT C9-on**: flow 20 (S1→S2): 75000/75000 received, 6 misses, latency 34.8 / 35.0 / 409.5 µs
- **heuristic C9-off**: no flow lost >100 frames or missed a deadline
- **heuristic C9-on**: no flow lost >100 frames or missed a deadline
- **RL C9-off**: no flow lost >100 frames or missed a deadline
- **RL C9-on**: no flow lost >100 frames or missed a deadline
- **Problem 3 heuristic C9-off**: no flow lost >100 frames or missed a deadline
- **Problem 3 heuristic C9-on**: no flow lost >100 frames or missed a deadline
- **Problem 3 RL C9-off**: no flow lost >100 frames or missed a deadline
- **Problem 3 RL C9-on**: no flow lost >100 frames or missed a deadline
