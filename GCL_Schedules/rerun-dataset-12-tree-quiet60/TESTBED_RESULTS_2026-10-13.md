# Testbed results: rerun-dataset-12-tree-quiet60 (2026-10-13)

Each package's GCLs were deployed on all of its switch ports, its scheduled flows admitted (VLANs + MSTP, all switches in one MST region), every route pinged, then 30 s of traffic on S1, S2, S3 at once (NIC launch time, NIC RX timestamps). Latest run of each package.

Rows in pipeline order, each approach C9 off then on. **Rank** orders the packages by deadline misses, then frames lost, then max latency (1 = best). **Flows** = admitted / offered: every flow of the dataset's base flow set for SMT, heuristic and RL; the base schedule's flows plus the arriving candidates for Problem 3. **Lost** = sent − received. **Deadline misses** = received frames whose latency exceeded their flow's deadline (deadline = period), with their share of received frames. **Latency** = receiver NIC's RX timestamp − sender NIC's launch time over all received frames (min / frame-weighted avg / max). **Jitter** = per-flow standard deviation of latency: best flow / average over the package's flows / worst flow.

| Rank | Package | Flows (admitted / offered) | Sent | Received | Lost | Deadline misses (%) | Latency min / avg / max (µs) | Jitter stddev best / avg / worst flow (µs) |
|---|---|---|---|---|---|---|---|---|
| 10 | SMT C9-off | 11 / 20 | 937,488 | 937,488 | 0 | 6 (0.00%) | 67.0 / 88.8 / 934.0 | 0.1 / 1.0 / 10.1 |
| 9 | SMT C9-on | 11 / 20 | 937,484 | 937,484 | 0 | 6 (0.00%) | 24.5 / 39.7 / 267.2 | 0.1 / 0.5 / 3.2 |
| 3 | heuristic C9-off | 11 / 20 | 937,493 | 937,493 | 0 | 0 (0.00%) | 15.8 / 55.5 / 133.9 | 0.1 / 0.3 / 1.1 |
| 2 | heuristic C9-on | 11 / 20 | 937,485 | 937,485 | 0 | 0 (0.00%) | 17.0 / 38.0 / 67.2 | 0.1 / 0.1 / 0.2 |
| 7 | RL C9-off | 11 / 20 | 937,424 | 937,411 | 13 | 0 (0.00%) | 12.8 / 58.4 / 134.3 | 0.1 / 3.3 / 33.3 |
| 1 | RL C9-on | 11 / 20 | 937,485 | 937,485 | 0 | 0 (0.00%) | 17.0 / 35.8 / 64.7 | 0.1 / 0.1 / 0.1 |
| 5 | Problem 3 heuristic C9-off | 34 / 50 | 2,212,467 | 2,212,466 | 1 | 0 (0.00%) | 12.1 / 49.5 / 141.8 | 0.1 / 1.0 / 14.1 |
| 6 | Problem 3 heuristic C9-on | 36 / 50 | 2,362,462 | 2,362,459 | 3 | 0 (0.00%) | 10.8 / 40.6 / 163.8 | 0.1 / 0.7 / 12.8 |
| 4 | Problem 3 RL C9-off | 33 / 50 | 2,212,472 | 2,212,472 | 0 | 0 (0.00%) | 9.7 / 58.4 / 249.0 | 0.1 / 2.8 / 43.4 |
| 8 | Problem 3 RL C9-on | 37 / 50 | 2,587,422 | 2,587,401 | 21 | 0 (0.00%) | 10.9 / 40.0 / 181.7 | 0.1 / 0.4 / 3.2 |
| | **Total** | | **14,999,682** | **14,999,644** | **38** | **12 (0.00%)** | | |

## Details

**Received %** shows a lost frame even when it rounds to 100%. **No NIC ts** = received frames without a hardware timestamp (left out of latency). **Jitter RFC 3550** = mean |Δ latency| between consecutive frames, best flow / average / worst flow. **Worst latency, % of deadline** = the largest max latency / deadline over the package's flows. **Above e2e bound** = flows whose max latency exceeded the scheduler's own end-to-end bound.

| Package | Received % | No NIC ts | Jitter RFC 3550 best / avg / worst flow (µs) | Worst latency, % of deadline | Above e2e bound | Routes ping OK | Switch queue drops | Run (`results.md` inside) |
|---|---|---|---|---|---|---|---|---|
| SMT C9-off | 100.0000% | 0 | 0.0 / 0.0 / 0.3 | 117% | 1 | 11/11 | none | `smt-c9-off/12-t3600-c9off-minlat/results/results-2026-10-13` |
| SMT C9-on | 100.0000% | 0 | 0.0 / 0.2 / 2.4 | 134% | 2 | 11/11 | none | `smt-c9-on/12-fair-retimed-c9on/results/results-2026-10-13` |
| heuristic C9-off | 100.0000% | 0 | 0.0 / 0.2 / 0.5 | 67% | 0 | 11/11 | none | `heuristic-c9-off/12-matrix-c9off/results/results-2026-10-13` |
| heuristic C9-on | 100.0000% | 0 | 0.0 / 0.0 / 0.2 | 34% | 0 | 11/11 | none | `heuristic-c9-on/12-matrix-c9on/results/results-2026-10-13` |
| RL C9-off | 99.9986% | 0 | 0.0 / 6.0 / 64.2 | 67% | 0 | 11/11 | none | `rl-c9-off/12-matrix-c9off/results/results-2026-10-13` |
| RL C9-on | 100.0000% | 0 | 0.0 / 0.0 / 0.2 | 27% | 0 | 11/11 | none | `rl-c9-on/12-matrix-c9on/results/results-2026-10-13` |
| Problem 3 heuristic C9-off | 99.99995% | 0 | 0.0 / 1.0 / 26.0 | 35% | 0 | 34/34 | none | `prob3-heuristic-c9-off/12-heuristic-c9off-matrix/results/results-2026-10-13` |
| Problem 3 heuristic C9-on | 99.9999% | 0 | 0.0 / 1.2 / 25.6 | 41% | 0 | 36/36 | none | `prob3-heuristic-c9-on/12-heuristic-c9on-matrix/results/results-2026-10-13` |
| Problem 3 RL C9-off | 100.0000% | 0 | 0.0 / 4.9 / 86.7 | 67% | 0 | 33/33 | none | `prob3-rl-c9-off/12-rl-c9off-matrix/results/results-2026-10-13` |
| Problem 3 RL C9-on | 99.9992% | 0 | 0.0 / 0.7 / 6.5 | 34% | 0 | 37/37 | none | `prob3-rl-c9-on/12-rl-c9on-matrix/results/results-2026-10-13` |

## Flows with misses or notable loss

- **SMT C9-off**: flow 19 (S1→S3): 37500/37500 received, 6 misses, latency 133.6 / 134.0 / 934.0 µs
- **SMT C9-on**: flow 2 (S1→S2): 150000/150000 received, 2 misses, latency 38.5 / 38.8 / 238.9 µs; flow 12 (S1→S3): 150000/150000 received, 4 misses, latency 66.8 / 67.0 / 267.2 µs
- **heuristic C9-off**: no flow lost >100 frames or missed a deadline
- **heuristic C9-on**: no flow lost >100 frames or missed a deadline
- **RL C9-off**: no flow lost >100 frames or missed a deadline
- **RL C9-on**: no flow lost >100 frames or missed a deadline
- **Problem 3 heuristic C9-off**: no flow lost >100 frames or missed a deadline
- **Problem 3 heuristic C9-on**: no flow lost >100 frames or missed a deadline
- **Problem 3 RL C9-off**: no flow lost >100 frames or missed a deadline
- **Problem 3 RL C9-on**: no flow lost >100 frames or missed a deadline
