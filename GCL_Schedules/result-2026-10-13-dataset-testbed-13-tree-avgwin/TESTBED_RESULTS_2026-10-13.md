# Testbed results: result-2026-10-13-dataset-testbed-13-tree-avgwin (2026-10-13)

Independent export validation is recorded in [validation.json](validation.json) and each package's `independent-verification.log`. Admission latency-report consistency failures remain; measured delivery does not establish deadline guarantees.

Each package's GCLs were deployed on all of its switch ports, its scheduled flows admitted (VLANs + MSTP, all switches in one MST region), every route pinged, then 30 s of traffic on S1, S2, S3 at once (NIC launch time, NIC RX timestamps). Latest run of each package.

Rows in pipeline order, each approach C9 off then on. **Rank** orders the packages by deadline misses, then frames lost, then max latency (1 = best). **Flows** = admitted / offered: every flow of the dataset's base flow set for SMT, heuristic and RL; the base schedule's flows plus the arriving candidates for Problem 3. **Lost** = sent − received. **Deadline misses** = received frames whose latency exceeded their flow's deadline (deadline = period), with their share of received frames. **Latency** = receiver NIC's RX timestamp − sender NIC's launch time over all received frames (min / frame-weighted avg / max). **Jitter** = per-flow standard deviation of latency: best flow / average over the package's flows / worst flow.

| Rank | Package | Flows (admitted / offered) | Sent | Received | Lost | Deadline misses (%) | Latency min / avg / max (µs) | Jitter stddev best / avg / worst flow (µs) |
|---|---|---|---|---|---|---|---|---|
| 10 | SMT C9-off | 11 / 20 | 1,012,450 | 1,012,440 | 10 | 4 (0.00%) | 66.8 / 82.8 / 267.1 | 0.1 / 0.2 / 1.1 |
| 7 | SMT C9-on | 11 / 20 | 1,012,451 | 1,012,441 | 10 | 0 (0.00%) | 24.8 / 34.9 / 62.4 | 0.1 / 0.1 / 0.1 |
| 3 | heuristic C9-off | 11 / 20 | 1,012,487 | 1,012,487 | 0 | 0 (0.00%) | 12.8 / 46.0 / 133.8 | 0.1 / 0.6 / 4.7 |
| 1 | heuristic C9-on | 11 / 20 | 1,012,482 | 1,012,482 | 0 | 0 (0.00%) | 14.9 / 29.8 / 51.5 | 0.1 / 0.1 / 0.2 |
| 2 | RL C9-off | 11 / 20 | 1,012,484 | 1,012,484 | 0 | 0 (0.00%) | 12.8 / 52.4 / 124.1 | 0.1 / 0.1 / 0.2 |
| 6 | RL C9-on | 11 / 20 | 1,012,475 | 1,012,468 | 7 | 0 (0.00%) | 14.9 / 29.6 / 52.6 | 0.1 / 0.4 / 2.7 |
| 9 | Problem 3 heuristic C9-off | 23 / 50 | 1,574,904 | 1,574,883 | 21 | 0 (0.00%) | 12.8 / 64.1 / 313.9 | 0.1 / 2.4 / 38.8 |
| 5 | Problem 3 heuristic C9-on | 25 / 50 | 1,837,459 | 1,837,459 | 0 | 0 (0.00%) | 15.2 / 57.4 / 406.3 | 0.1 / 4.6 / 34.9 |
| 4 | Problem 3 RL C9-off | 27 / 50 | 1,987,471 | 1,987,471 | 0 | 0 (0.00%) | 12.9 / 82.3 / 239.2 | 0.1 / 2.5 / 38.8 |
| 8 | Problem 3 RL C9-on | 28 / 50 | 1,949,915 | 1,949,898 | 17 | 0 (0.00%) | 15.2 / 55.6 / 290.5 | 0.1 / 5.9 / 120.5 |
| | **Total** | | **13,424,578** | **13,424,513** | **65** | **4 (0.00%)** | | |

## Details

**Received %** shows a lost frame even when it rounds to 100%. **No NIC ts** = received frames without a hardware timestamp (left out of latency). **Jitter RFC 3550** = mean |Δ latency| between consecutive frames, best flow / average / worst flow. **Worst latency, % of deadline** = the largest max latency / deadline over the package's flows. **Above e2e bound** = flows whose max latency exceeded the scheduler's own end-to-end bound.

| Package | Received % | No NIC ts | Jitter RFC 3550 best / avg / worst flow (µs) | Worst latency, % of deadline | Above e2e bound | Routes ping OK | Switch queue drops | Run (`results.md` inside) |
|---|---|---|---|---|---|---|---|---|
| SMT C9-off | 99.9990% | 0 | 0.0 / 0.0 / 0.1 | 134% | 1 | 11/11 | none | `smt-c9-off/13-t3600-c9off-minlat/results/results-2026-10-13` |
| SMT C9-on | 99.9990% | 0 | 0.0 / 0.0 / 0.0 | 21% | 0 | 11/11 | sw02/p4 +48 | `smt-c9-on/13-fair-retimed-c9on/results/results-2026-10-13` |
| heuristic C9-off | 100.0000% | 0 | 0.0 / 0.6 / 5.6 | 33% | 0 | 11/11 | none | `heuristic-c9-off/13-matrix-c9off/results/results-2026-10-13` |
| heuristic C9-on | 100.0000% | 0 | 0.0 / 0.1 / 0.3 | 21% | 0 | 11/11 | none | `heuristic-c9-on/13-matrix-c9on/results/results-2026-10-13` |
| RL C9-off | 100.0000% | 0 | 0.0 / 0.1 / 0.2 | 42% | 0 | 11/11 | none | `rl-c9-off/13-matrix-c9off/results/results-2026-10-13` |
| RL C9-on | 99.9993% | 0 | 0.0 / 0.6 / 5.4 | 21% | 0 | 11/11 | none | `rl-c9-on/13-matrix-c9on/results/results-2026-10-13` |
| Problem 3 heuristic C9-off | 99.9987% | 0 | 0.0 / 4.5 / 77.6 | 39% | 0 | 23/23 | none | `prob3-heuristic-c9-off/13-heuristic-c9off-matrix/results/results-2026-10-13` |
| Problem 3 heuristic C9-on | 100.0000% | 0 | 0.0 / 8.2 / 69.8 | 53% | 1 | 25/25 | none | `prob3-heuristic-c9-on/13-heuristic-c9on-matrix/results/results-2026-10-13` |
| Problem 3 RL C9-off | 100.0000% | 0 | 0.0 / 4.7 / 77.6 | 60% | 0 | 27/27 | none | `prob3-rl-c9-off/13-rl-c9off-matrix/results/results-2026-10-13` |
| Problem 3 RL C9-on | 99.9991% | 0 | 0.0 / 11.5 / 235.1 | 73% | 0 | 28/28 | none | `prob3-rl-c9-on/13-rl-c9on-matrix/results/results-2026-10-13` |

## Flows with misses or notable loss

- **SMT C9-off**: flow 14 (S1→S2): 150000/150000 received, 4 misses, latency 66.8 / 67.0 / 267.1 µs
- **SMT C9-on**: no flow lost >100 frames or missed a deadline
- **heuristic C9-off**: no flow lost >100 frames or missed a deadline
- **heuristic C9-on**: no flow lost >100 frames or missed a deadline
- **RL C9-off**: no flow lost >100 frames or missed a deadline
- **RL C9-on**: no flow lost >100 frames or missed a deadline
- **Problem 3 heuristic C9-off**: no flow lost >100 frames or missed a deadline
- **Problem 3 heuristic C9-on**: no flow lost >100 frames or missed a deadline
- **Problem 3 RL C9-off**: no flow lost >100 frames or missed a deadline
- **Problem 3 RL C9-on**: no flow lost >100 frames or missed a deadline
