# Testbed results: result-2026-10-13-dataset-testbed-11-tree-avgwin (2026-10-13)

Independent export validation is recorded in [validation.json](validation.json) and each package's `independent-verification.log`. Admission latency-report consistency failures remain; measured delivery does not establish deadline guarantees.

Each package's GCLs were deployed on all of its switch ports, its scheduled flows admitted (VLANs + MSTP, all switches in one MST region), every route pinged, then 30 s of traffic on S1, S2, S3 at once (NIC launch time, NIC RX timestamps). Latest run of each package.

Rows in pipeline order, each approach C9 off then on. **Rank** orders the packages by deadline misses, then frames lost, then max latency (1 = best). **Flows** = admitted / offered: every flow of the dataset's base flow set for SMT, heuristic and RL; the base schedule's flows plus the arriving candidates for Problem 3. **Lost** = sent − received. **Deadline misses** = received frames whose latency exceeded their flow's deadline (deadline = period), with their share of received frames. **Latency** = receiver NIC's RX timestamp − sender NIC's launch time over all received frames (min / frame-weighted avg / max). **Jitter** = per-flow standard deviation of latency: best flow / average over the package's flows / worst flow.

| Rank | Package | Flows (admitted / offered) | Sent | Received | Lost | Deadline misses (%) | Latency min / avg / max (µs) | Jitter stddev best / avg / worst flow (µs) |
|---|---|---|---|---|---|---|---|---|
| 10 | SMT C9-off | 10 / 20 | 937,475 | 749,975 | 187,500 | 12 (0.00%) | 66.8 / 80.7 / 267.1 | 0.1 / 0.3 / 1.8 |
| 9 | SMT C9-on | 10 / 20 | 937,451 | 937,451 | 0 | 5 (0.00%) | 24.5 / 38.0 / 409.5 | 0.1 / 0.4 / 3.1 |
| 3 | heuristic C9-off | 10 / 20 | 937,461 | 937,461 | 0 | 0 (0.00%) | 28.0 / 61.5 / 109.2 | 0.1 / 0.1 / 0.2 |
| 2 | heuristic C9-on | 10 / 20 | 937,463 | 937,463 | 0 | 0 (0.00%) | 18.5 / 34.2 / 49.2 | 0.1 / 0.4 / 2.8 |
| 4 | RL C9-off | 10 / 20 | 937,475 | 937,475 | 0 | 0 (0.00%) | 28.4 / 70.5 / 109.6 | 0.1 / 0.1 / 0.2 |
| 1 | RL C9-on | 10 / 20 | 937,469 | 937,469 | 0 | 0 (0.00%) | 18.5 / 34.3 / 47.3 | 0.1 / 0.4 / 2.5 |
| 6 | Problem 3 heuristic C9-off | 29 / 50 | 1,912,421 | 1,912,421 | 0 | 0 (0.00%) | 17.0 / 67.1 / 571.9 | 0.1 / 1.5 / 21.2 |
| 7 | Problem 3 heuristic C9-on | 27 / 50 | 1,724,947 | 1,724,944 | 3 | 0 (0.00%) | 15.9 / 43.5 / 300.0 | 0.1 / 5.1 / 126.8 |
| 5 | Problem 3 RL C9-off | 25 / 50 | 1,687,457 | 1,687,457 | 0 | 0 (0.00%) | 28.0 / 91.5 / 308.8 | 0.1 / 1.6 / 27.8 |
| 8 | Problem 3 RL C9-on | 27 / 50 | 1,912,426 | 1,912,404 | 22 | 0 (0.00%) | 15.9 / 43.8 / 173.1 | 0.1 / 4.3 / 72.1 |
| | **Total** | | **12,862,045** | **12,674,520** | **187,525** | **17 (0.00%)** | | |

## Details

**Received %** shows a lost frame even when it rounds to 100%. **No NIC ts** = received frames without a hardware timestamp (left out of latency). **Jitter RFC 3550** = mean |Δ latency| between consecutive frames, best flow / average / worst flow. **Worst latency, % of deadline** = the largest max latency / deadline over the package's flows. **Above e2e bound** = flows whose max latency exceeded the scheduler's own end-to-end bound.

| Package | Received % | No NIC ts | Jitter RFC 3550 best / avg / worst flow (µs) | Worst latency, % of deadline | Above e2e bound | Routes ping OK | Switch queue drops | Run (`results.md` inside) |
|---|---|---|---|---|---|---|---|---|
| SMT C9-off | 79.9995% | 0 | 0.0 / 0.0 / 0.1 | 134% | 1 | 8/10 (failed: 5, 7) | none | `smt-c9-off/11-t3600-c9off-minlat/results/results-2026-10-13` |
| SMT C9-on | 100.0000% | 0 | 0.0 / 0.0 / 0.1 | 102% | 2 | 10/10 | none | `smt-c9-on/11-fair-retimed-c9on/results/results-2026-10-13` |
| heuristic C9-off | 100.0000% | 0 | 0.0 / 0.1 / 0.2 | 36% | 0 | 10/10 | none | `heuristic-c9-off/11-matrix-c9off/results/results-2026-10-13` |
| heuristic C9-on | 100.0000% | 0 | 0.0 / 0.1 / 0.7 | 25% | 0 | 10/10 | none | `heuristic-c9-on/11-matrix-c9on/results/results-2026-10-13` |
| RL C9-off | 100.0000% | 0 | 0.0 / 0.1 / 0.2 | 42% | 0 | 10/10 | none | `rl-c9-off/11-matrix-c9off/results/results-2026-10-13` |
| RL C9-on | 100.0000% | 0 | 0.0 / 0.1 / 0.5 | 24% | 0 | 10/10 | none | `rl-c9-on/11-matrix-c9on/results/results-2026-10-13` |
| Problem 3 heuristic C9-off | 100.0000% | 0 | 0.0 / 2.2 / 42.4 | 71% | 0 | 29/29 | none | `prob3-heuristic-c9-off/11-heuristic-c9off-matrix/results/results-2026-10-13` |
| Problem 3 heuristic C9-on | 99.9998% | 0 | 0.0 / 9.7 / 253.7 | 75% | 0 | 27/27 | none | `prob3-heuristic-c9-on/11-heuristic-c9on-matrix/results/results-2026-10-13` |
| Problem 3 RL C9-off | 100.0000% | 0 | 0.0 / 3.0 / 55.7 | 45% | 0 | 25/25 | none | `prob3-rl-c9-off/11-rl-c9off-matrix/results/results-2026-10-13` |
| Problem 3 RL C9-on | 99.9988% | 0 | 0.0 / 8.0 / 144.2 | 62% | 0 | 27/27 | none | `prob3-rl-c9-on/11-rl-c9on-matrix/results/results-2026-10-13` |

## Flows with misses or notable loss

- **SMT C9-off**: flow 1 (S1→S2): 150000/150000 received, 12 misses, latency 66.8 / 67.0 / 267.1 µs; flow 5 (S2→S1): 0/150000 received, 0 misses, latency – µs; flow 7 (S2→S1): 0/37500 received, 0 misses, latency – µs
- **SMT C9-on**: flow 20 (S1→S2): 74995/74995 received, 5 misses, latency 34.8 / 35.0 / 409.5 µs
- **heuristic C9-off**: no flow lost >100 frames or missed a deadline
- **heuristic C9-on**: no flow lost >100 frames or missed a deadline
- **RL C9-off**: no flow lost >100 frames or missed a deadline
- **RL C9-on**: no flow lost >100 frames or missed a deadline
- **Problem 3 heuristic C9-off**: no flow lost >100 frames or missed a deadline
- **Problem 3 heuristic C9-on**: no flow lost >100 frames or missed a deadline
- **Problem 3 RL C9-off**: no flow lost >100 frames or missed a deadline
- **Problem 3 RL C9-on**: no flow lost >100 frames or missed a deadline
