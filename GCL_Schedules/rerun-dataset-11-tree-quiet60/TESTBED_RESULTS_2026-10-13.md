# Testbed results: rerun-dataset-11-tree-quiet60 (2026-10-13)

Each package's GCLs were deployed on all of its switch ports, its scheduled flows admitted (VLANs + MSTP, all switches in one MST region), every route pinged, then 30 s of traffic on S1, S2, S3 at once (NIC launch time, NIC RX timestamps). Latest run of each package.

Rows in pipeline order, each approach C9 off then on. **Rank** orders the packages by deadline misses, then frames lost, then max latency (1 = best). **Flows** = admitted / offered: every flow of the dataset's base flow set for SMT, heuristic and RL; the base schedule's flows plus the arriving candidates for Problem 3. **Lost** = sent − received. **Deadline misses** = received frames whose latency exceeded their flow's deadline (deadline = period), with their share of received frames. **Latency** = receiver NIC's RX timestamp − sender NIC's launch time over all received frames (min / frame-weighted avg / max). **Jitter** = per-flow standard deviation of latency: best flow / average over the package's flows / worst flow.

| Rank | Package | Flows (admitted / offered) | Sent | Received | Lost | Deadline misses (%) | Latency min / avg / max (µs) | Jitter stddev best / avg / worst flow (µs) |
|---|---|---|---|---|---|---|---|---|
| 8 | SMT C9-off | 10 / 20 | 937,433 | 937,425 | 8 | 14 (0.00%) | 66.8 / 78.0 / 267.1 | 0.1 / 0.3 / 1.9 |
| 7 | SMT C9-on | 10 / 20 | 937,448 | 937,448 | 0 | 5 (0.00%) | 24.6 / 38.0 / 409.5 | 0.1 / 0.4 / 3.1 |
| 4 | heuristic C9-off | 10 / 20 | 937,464 | 937,461 | 3 | 0 (0.00%) | 28.0 / 61.5 / 109.1 | 0.1 / 0.1 / 0.2 |
| 1 | heuristic C9-on | 10 / 20 | 937,475 | 937,475 | 0 | 0 (0.00%) | 18.7 / 34.0 / 47.6 | 0.1 / 0.8 / 7.2 |
| 2 | RL C9-off | 10 / 20 | 937,475 | 937,475 | 0 | 0 (0.00%) | 28.7 / 70.7 / 109.5 | 0.1 / 0.1 / 0.2 |
| 9 | RL C9-on | 10 / 20 | 937,438 | 935,542 | 1,896 | 83 (0.01%) | 18.6 / 62.3 / 320835.4 | 0.1 / 2476.6 / 8347.4 |
| 6 | Problem 3 heuristic C9-off | 29 / 50 | 1,912,446 | 1,912,443 | 3 | 0 (0.00%) | 16.8 / 67.4 / 571.6 | 0.1 / 1.8 / 24.3 |
| 3 | Problem 3 heuristic C9-on | 27 / 50 | 1,724,957 | 1,724,956 | 1 | 0 (0.00%) | 15.9 / 43.4 / 300.0 | 0.1 / 5.1 / 126.8 |
| 10 | Problem 3 RL C9-off | 25 / 50 | 1,687,427 | 1,679,575 | 7,852 | 120 (0.01%) | 16.0 / 114.4 / 321157.7 | 0.1 / 1980.1 / 5447.8 |
| 5 | Problem 3 RL C9-on | 27 / 50 | 1,912,459 | 1,912,456 | 3 | 0 (0.00%) | 15.8 / 43.4 / 173.7 | 0.1 / 4.4 / 72.2 |
| | **Total** | | **12,862,022** | **12,852,256** | **9,766** | **222 (0.00%)** | | |

## Details

**Received %** shows a lost frame even when it rounds to 100%. **No NIC ts** = received frames without a hardware timestamp (left out of latency). **Jitter RFC 3550** = mean |Δ latency| between consecutive frames, best flow / average / worst flow. **Worst latency, % of deadline** = the largest max latency / deadline over the package's flows. **Above e2e bound** = flows whose max latency exceeded the scheduler's own end-to-end bound.

| Package | Received % | No NIC ts | Jitter RFC 3550 best / avg / worst flow (µs) | Worst latency, % of deadline | Above e2e bound | Routes ping OK | Switch queue drops | Run (`results.md` inside) |
|---|---|---|---|---|---|---|---|---|
| SMT C9-off | 99.9991% | 0 | 0.0 / 0.0 / 0.1 | 134% | 1 | 10/10 | none | `smt-c9-off/11-t3600-c9off-minlat/results/results-2026-10-13` |
| SMT C9-on | 100.0000% | 0 | 0.0 / 0.0 / 0.1 | 102% | 2 | 10/10 | none | `smt-c9-on/11-fair-retimed-c9on/results/results-2026-10-13` |
| heuristic C9-off | 99.9997% | 0 | 0.0 / 0.1 / 0.2 | 36% | 0 | 10/10 | none | `heuristic-c9-off/11-matrix-c9off/results/results-2026-10-13` |
| heuristic C9-on | 100.0000% | 0 | 0.0 / 0.5 / 3.7 | 24% | 0 | 10/10 | none | `heuristic-c9-on/11-matrix-c9on/results/results-2026-10-13` |
| RL C9-off | 100.0000% | 0 | 0.0 / 0.1 / 0.2 | 42% | 0 | 10/10 | none | `rl-c9-off/11-matrix-c9off/results/results-2026-10-13` |
| RL C9-on | 99.7977% | 0 | 0.0 / 3.0 / 9.4 | 160410% | 5 | 10/10 | sw01/p4 +166, sw02/p4 +759, sw08/p2 +10, sw08/p4 +956 | `rl-c9-on/11-matrix-c9on/results/results-2026-10-13` |
| Problem 3 heuristic C9-off | 99.9998% | 0 | 0.0 / 2.9 / 42.1 | 71% | 0 | 29/29 | none | `prob3-heuristic-c9-off/11-heuristic-c9off-matrix/results/results-2026-10-13` |
| Problem 3 heuristic C9-on | 99.9999% | 0 | 0.0 / 9.7 / 253.6 | 75% | 0 | 27/27 | none | `prob3-heuristic-c9-on/11-heuristic-c9on-matrix/results/results-2026-10-13` |
| Problem 3 RL C9-off | 99.5347% | 0 | 0.0 / 6.0 / 60.0 | 160436% | 13 | 25/25 | sw01/p4 +3341, sw02/p4 +2115, sw07/p4 +1502, sw08/p2 +4, sw08/p4 +888 | `prob3-rl-c9-off/11-rl-c9off-matrix/results/results-2026-10-13` |
| Problem 3 RL C9-on | 99.9998% | 0 | 0.0 / 8.3 / 144.4 | 62% | 0 | 27/27 | none | `prob3-rl-c9-on/11-rl-c9on-matrix/results/results-2026-10-13` |

## Flows with misses or notable loss

- **SMT C9-off**: flow 1 (S1→S2): 150000/150000 received, 14 misses, latency 66.8 / 67.0 / 267.1 µs
- **SMT C9-on**: flow 20 (S1→S2): 74997/74997 received, 5 misses, latency 34.8 / 35.0 / 409.5 µs
- **heuristic C9-off**: no flow lost >100 frames or missed a deadline
- **heuristic C9-on**: no flow lost >100 frames or missed a deadline
- **RL C9-off**: no flow lost >100 frames or missed a deadline
- **RL C9-on**: flow 3 (S1→S2): 74611/74993 received, 13 misses, latency 34.1 / 89.9 / 320835.4 µs; flow 5 (S2→S1): 149236/150000 received, 25 misses, latency 18.6 / 72.4 / 320819.2 µs; flow 7 (S2→S1): 37308/37500 received, 6 misses, latency 27.1 / 78.6 / 320784.8 µs; flow 9 (S3→S2): 37329/37499 received, 27 misses, latency 23.0 / 247.9 / 320784.5 µs; flow 20 (S1→S2): 74610/74993 received, 12 misses, latency 34.8 / 86.3 / 320835.1 µs
- **Problem 3 heuristic C9-off**: no flow lost >100 frames or missed a deadline
- **Problem 3 heuristic C9-on**: no flow lost >100 frames or missed a deadline
- **Problem 3 RL C9-off**: flow 1 (S1→S2): 148779/149989 received, 16 misses, latency 67.0 / 101.6 / 320867.1 µs; flow 2 (S3→S2): 148774/149990 received, 10 misses, latency 67.0 / 92.9 / 320871.2 µs; flow 4 (S2→S3): 74400/75000 received, 13 misses, latency 28.0 / 84.4 / 320805.1 µs; flow 8 (S3→S2): 148775/149991 received, 10 misses, latency 84.3 / 106.0 / 320853.0 µs; flow 12 (S2→S3): 74398/74999 received, 12 misses, latency 58.7 / 138.2 / 320771.8 µs; flow 15 (S2→S3): 37199/37500 received, 6 misses, latency 80.7 / 139.9 / 320696.6 µs; flow 17 (S1→S2): 74387/74992 received, 8 misses, latency 97.7 / 132.3 / 320837.1 µs; flow 23 (S2→S1): 37204/37500 received, 11 misses, latency 103.8 / 197.7 / 320787.6 µs; flow 25 (S2→S1): 37204/37500 received, 10 misses, latency 84.7 / 170.3 / 320488.0 µs; flow 36 (S2→S1): 37204/37500 received, 10 misses, latency 171.1 / 256.4 / 320397.4 µs; flow 37 (S3→S1): 37195/37499 received, 3 misses, latency 133.6 / 159.6 / 321157.7 µs; flow 39 (S3→S1): 74388/74996 received, 6 misses, latency 112.8 / 147.4 / 321137.4 µs; flow 46 (S1→S3): 37197/37499 received, 5 misses, latency 149.1 / 192.5 / 320992.8 µs
- **Problem 3 RL C9-on**: no flow lost >100 frames or missed a deadline
