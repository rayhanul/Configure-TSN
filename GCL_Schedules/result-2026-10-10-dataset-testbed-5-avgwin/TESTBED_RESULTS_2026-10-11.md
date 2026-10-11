# Testbed results: result-2026-10-10-dataset-testbed-5-avgwin (2026-10-11)

Each package's GCLs were deployed on all of its switch ports, its scheduled flows admitted (VLANs + MSTP, all switches in one MST region), every route pinged, then 30 s of traffic on S1, S2, S3 at once (NIC launch time, NIC RX timestamps). Latest run of each package.

Rows in pipeline order, each approach C9 off then on. **Rank** orders the packages by deadline misses, then frames lost, then max latency (1 = best). **Flows** = admitted / offered: every flow of the dataset's base flow set for SMT, heuristic and RL; the base schedule's flows plus the arriving candidates for Problem 3. **Lost** = sent − received. **Deadline misses** = received frames whose latency exceeded their flow's deadline (deadline = period), with their share of received frames. **Latency** = receiver NIC's RX timestamp − sender NIC's launch time over all received frames (min / frame-weighted avg / max). **Jitter** = per-flow standard deviation of latency: best flow / average over the package's flows / worst flow.

| Rank | Package | Flows (admitted / offered) | Sent | Received | Lost | Deadline misses (%) | Latency min / avg / max (µs) | Jitter stddev best / avg / worst flow (µs) |
|---|---|---|---|---|---|---|---|---|
| 8 | SMT C9-off | 10 / 20 | 824,986 | 824,986 | 0 | 2 (0.00%) | 49.9 / 79.1 / 471.9 | 0.1 / 0.3 / 2.1 |
| 10 | SMT C9-on | 10 / 20 | 824,984 | 824,979 | 5 | 15 (0.00%) | 26.1 / 37.5 / 242.2 | 0.1 / 0.3 / 1.9 |
| 2 | heuristic C9-off | 10 / 20 | 824,985 | 824,985 | 0 | 0 (0.00%) | 19.7 / 54.8 / 122.5 | 0.1 / 0.1 / 0.2 |
| 1 | heuristic C9-on | 10 / 20 | 824,981 | 824,981 | 0 | 0 (0.00%) | 9.8 / 32.6 / 62.3 | 0.1 / 0.2 / 1.2 |
| 6 | RL C9-off | 10 / 20 | 824,985 | 824,984 | 1 | 0 (0.00%) | 19.8 / 65.9 / 122.4 | 0.1 / 3.3 / 31.6 |
| 5 | RL C9-on | 10 / 20 | 824,976 | 824,975 | 1 | 0 (0.00%) | 9.8 / 34.1 / 51.7 | 0.1 / 0.1 / 0.2 |
| 4 | Problem 3 heuristic C9-off | 24 / 50 | 1,499,951 | 1,499,951 | 0 | 0 (0.00%) | 19.8 / 72.5 / 330.6 | 0.1 / 2.4 / 36.7 |
| 3 | Problem 3 heuristic C9-on | 28 / 50 | 1,874,962 | 1,874,962 | 0 | 0 (0.00%) | 9.8 / 55.8 / 277.7 | 0.1 / 3.4 / 45.1 |
| 9 | Problem 3 RL C9-off | 25 / 50 | 1,874,949 | 1,874,935 | 14 | 2 (0.00%) | 19.8 / 96.3 / 884.0 | 0.1 / 2.9 / 31.5 |
| 7 | Problem 3 RL C9-on | 29 / 50 | 2,174,809 | 2,174,808 | 1 | 0 (0.00%) | 10.2 / 47.3 / 187.3 | 0.1 / 0.4 / 4.5 |
| | **Total** | | **12,374,568** | **12,374,546** | **22** | **19 (0.00%)** | | |

## Details

**Received %** shows a lost frame even when it rounds to 100%. **No NIC ts** = received frames without a hardware timestamp (left out of latency). **Jitter RFC 3550** = mean |Δ latency| between consecutive frames, best flow / average / worst flow. **Worst latency, % of deadline** = the largest max latency / deadline over the package's flows. **Above e2e bound** = flows whose max latency exceeded the scheduler's own end-to-end bound.

| Package | Received % | No NIC ts | Jitter RFC 3550 best / avg / worst flow (µs) | Worst latency, % of deadline | Above e2e bound | Routes ping OK | Switch queue drops | Run (`results.md` inside) |
|---|---|---|---|---|---|---|---|---|
| SMT C9-off | 100.0000% | 0 | 0.0 / 0.0 / 0.0 | 118% | 1 | 10/10 | none | `smt-c9-off/5-t3600-c9off-minlat/results/results-2026-10-10` |
| SMT C9-on | 99.9994% | 0 | 0.0 / 0.0 / 0.0 | 121% | 2 | 10/10 | none | `smt-c9-on/5-fair-retimed-c9on/results/results-2026-10-10` |
| heuristic C9-off | 100.0000% | 0 | 0.0 / 0.1 / 0.2 | 34% | 0 | 10/10 | none | `heuristic-c9-off/5-matrix-c9off/results/results-2026-10-11` |
| heuristic C9-on | 100.0000% | 0 | 0.0 / 0.2 / 1.5 | 20% | 0 | 10/10 | none | `heuristic-c9-on/5-matrix-c9on/results/results-2026-10-11` |
| RL C9-off | 99.9999% | 0 | 0.0 / 6.4 / 63.2 | 42% | 0 | 10/10 | none | `rl-c9-off/5-matrix-c9off/results/results-2026-10-11` |
| RL C9-on | 99.9999% | 0 | 0.0 / 0.1 / 0.2 | 21% | 0 | 10/10 | none | `rl-c9-on/5-matrix-c9on/results/results-2026-10-11` |
| Problem 3 heuristic C9-off | 100.0000% | 0 | 0.0 / 4.5 / 73.3 | 42% | 0 | 24/24 | none | `prob3-heuristic-c9-off/5-heuristic-c9off-matrix/results/results-2026-10-11` |
| Problem 3 heuristic C9-on | 100.0000% | 0 | 0.0 / 5.1 / 73.6 | 94% | 0 | 28/28 | none | `prob3-heuristic-c9-on/5-heuristic-c9on-matrix/results/results-2026-10-11` |
| Problem 3 RL C9-off | 99.9993% | 0 | 0.0 / 4.6 / 62.9 | 342% | 2 | 25/25 | none | `prob3-rl-c9-off/5-rl-c9off-matrix/results/results-2026-10-11` |
| Problem 3 RL C9-on | 99.99995% | 0 | 0.0 / 0.6 / 9.0 | 44% | 0 | 29/29 | none | `prob3-rl-c9-on/5-rl-c9on-matrix/results/results-2026-10-11` |

## Flows with misses or notable loss

- **SMT C9-off**: flow 17 (S1→S2): 75000/75000 received, 2 misses, latency 71.5 / 71.7 / 471.9 µs
- **SMT C9-on**: flow 10 (S1→S2): 150000/150000 received, 14 misses, latency 33.7 / 33.9 / 234.2 µs; flow 12 (S3→S2): 149990/149992 received, 1 misses, latency 42.0 / 42.2 / 242.2 µs
- **heuristic C9-off**: no flow lost >100 frames or missed a deadline
- **heuristic C9-on**: no flow lost >100 frames or missed a deadline
- **RL C9-off**: no flow lost >100 frames or missed a deadline
- **RL C9-on**: no flow lost >100 frames or missed a deadline
- **Problem 3 heuristic C9-off**: no flow lost >100 frames or missed a deadline
- **Problem 3 heuristic C9-on**: no flow lost >100 frames or missed a deadline
- **Problem 3 RL C9-off**: flow 7 (S3→S2): 74994/74995 received, 1 misses, latency 144.8 / 145.1 / 884.0 µs; flow 12 (S3→S2): 149986/149989 received, 1 misses, latency 83.4 / 83.6 / 683.6 µs
- **Problem 3 RL C9-on**: no flow lost >100 frames or missed a deadline
