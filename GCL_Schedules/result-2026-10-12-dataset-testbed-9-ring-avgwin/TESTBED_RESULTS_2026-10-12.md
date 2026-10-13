# Testbed results: result-2026-10-12-dataset-testbed-9-ring-avgwin (2026-10-12)

Independent export validation is recorded in [validation.json](validation.json) and each package’s `independent-verification.log`. Admission latency-report consistency failures remain; measured delivery does not establish deadline guarantees.

Each package's GCLs were deployed on all of its switch ports, its scheduled flows admitted (VLANs + MSTP, all switches in one MST region), every route pinged, then 30 s of traffic on S1, S2, S3 at once (NIC launch time, NIC RX timestamps). Latest run of each package.

Rows in pipeline order, each approach C9 off then on. **Rank** orders the packages by deadline misses, then frames lost, then max latency (1 = best). **Flows** = admitted / offered: every flow of the dataset's base flow set for SMT, heuristic and RL; the base schedule's flows plus the arriving candidates for Problem 3. **Lost** = sent − received. **Deadline misses** = received frames whose latency exceeded their flow's deadline (deadline = period), with their share of received frames. **Latency** = receiver NIC's RX timestamp − sender NIC's launch time over all received frames (min / frame-weighted avg / max). **Jitter** = per-flow standard deviation of latency: best flow / average over the package's flows / worst flow.

| Rank | Package | Flows (admitted / offered) | Sent | Received | Lost | Deadline misses (%) | Latency min / avg / max (µs) | Jitter stddev best / avg / worst flow (µs) |
|---|---|---|---|---|---|---|---|---|
| 8 | SMT C9-off | 11 / 20 | 862,439 | 862,427 | 12 | 6 (0.00%) | 33.4 / 54.6 / 233.7 | 0.1 / 0.2 / 1.3 |
| 10 | SMT C9-on | 11 / 20 | 862,484 | 857,793 | 4,691 | 175 (0.02%) | 12.4 / 68.5 / 320841.9 | 0.1 / 3508.0 / 9089.4 |
| 1 | heuristic C9-off | 11 / 20 | 862,479 | 862,479 | 0 | 0 (0.00%) | 9.7 / 35.0 / 73.0 | 0.1 / 0.6 / 5.1 |
| 5 | heuristic C9-on | 11 / 20 | 862,478 | 862,472 | 6 | 0 (0.00%) | 9.7 / 18.7 / 42.2 | 0.1 / 0.6 / 2.3 |
| 1 | RL C9-off | 11 / 20 | 862,492 | 862,492 | 0 | 0 (0.00%) | 9.7 / 36.9 / 73.0 | 0.1 / 0.1 / 0.2 |
| 6 | RL C9-on | 11 / 20 | 862,442 | 862,432 | 10 | 0 (0.00%) | 9.7 / 19.1 / 42.2 | 0.1 / 0.3 / 2.1 |
| 7 | Problem 3 heuristic C9-off | 35 / 50 | 2,287,385 | 2,287,372 | 13 | 1 (0.00%) | 5.0 / 39.5 / 268.0 | 0.1 / 3.9 / 46.6 |
| 4 | Problem 3 heuristic C9-on | 37 / 50 | 2,362,386 | 2,362,383 | 3 | 0 (0.00%) | 6.6 / 29.1 / 316.1 | 0.1 / 3.3 / 74.7 |
| 3 | Problem 3 RL C9-off | 33 / 50 | 2,287,326 | 2,287,325 | 1 | 0 (0.00%) | 6.6 / 36.8 / 159.4 | 0.1 / 2.8 / 51.9 |
| 9 | Problem 3 RL C9-on | 37 / 50 | 2,512,414 | 2,504,512 | 7,902 | 126 (0.01%) | 6.6 / 55.1 / 320818.3 | 0.1 / 1345.4 / 5454.4 |
| | **Total** | | **14,624,325** | **14,611,687** | **12,638** | **308 (0.00%)** | | |

## Details

**Received %** shows a lost frame even when it rounds to 100%. **No NIC ts** = received frames without a hardware timestamp (left out of latency). **Jitter RFC 3550** = mean |Δ latency| between consecutive frames, best flow / average / worst flow. **Worst latency, % of deadline** = the largest max latency / deadline over the package's flows. **Above e2e bound** = flows whose max latency exceeded the scheduler's own end-to-end bound.

| Package | Received % | No NIC ts | Jitter RFC 3550 best / avg / worst flow (µs) | Worst latency, % of deadline | Above e2e bound | Routes ping OK | Switch queue drops | Run (`results.md` inside) |
|---|---|---|---|---|---|---|---|---|
| SMT C9-off | 99.9986% | 0 | 0.0 / 0.0 / 0.2 | 117% | 1 | 11/11 | none | `smt-c9-off/9-t3600-c9off-minlat/results/results-2026-10-12` |
| SMT C9-on | 99.4561% | 0 | 0.0 / 8.3 / 17.3 | 160412% | 8 | 11/11 | sw01/p4 +371, sw02/p4 +370, sw07/p4 +1975, sw08/p4 +1975 | `smt-c9-on/9-fair-retimed-c9on/results/results-2026-10-12` |
| heuristic C9-off | 100.0000% | 0 | 0.0 / 0.7 / 6.0 | 29% | 0 | 11/11 | none | `heuristic-c9-off/9-matrix-c9off/results/results-2026-10-12` |
| heuristic C9-on | 99.9993% | 0 | 0.0 / 0.9 / 4.3 | 14% | 0 | 11/11 | none | `heuristic-c9-on/9-matrix-c9on/results/results-2026-10-12` |
| RL C9-off | 100.0000% | 0 | 0.0 / 0.1 / 0.2 | 28% | 0 | 11/11 | none | `rl-c9-off/9-matrix-c9off/results/results-2026-10-12` |
| RL C9-on | 99.9988% | 0 | 0.0 / 0.5 / 4.3 | 10% | 0 | 11/11 | none | `rl-c9-on/9-matrix-c9on/results/results-2026-10-12` |
| Problem 3 heuristic C9-off | 99.9994% | 0 | 0.0 / 7.2 / 93.3 | 104% | 2 | 35/35 | none | `prob3-heuristic-c9-off/9-heuristic-c9off-matrix/results/results-2026-10-12` |
| Problem 3 heuristic C9-on | 99.9999% | 0 | 0.0 / 6.3 / 149.4 | 41% | 1 | 37/37 | none | `prob3-heuristic-c9-on/9-heuristic-c9on-matrix/results/results-2026-10-12` |
| Problem 3 RL C9-off | 99.99996% | 0 | 0.0 / 5.3 / 103.8 | 40% | 0 | 33/33 | none | `prob3-rl-c9-off/9-rl-c9off-matrix/results/results-2026-10-12` |
| Problem 3 RL C9-on | 99.6855% | 0 | 0.0 / 9.9 / 117.2 | 160409% | 13 | 37/37 | sw01/p4 +1569, sw02/p4 +1169, sw05/p4 +4, sw06/p4 +3, sw07/p4 +2376, sw08/p4 +2776 | `prob3-rl-c9-on/9-rl-c9on-matrix/results/results-2026-10-12` |

## Flows with misses or notable loss

- **SMT C9-off**: flow 14 (S1→S3): 149991/149991 received, 6 misses, latency 33.4 / 33.7 / 233.7 µs
- **SMT C9-on**: flow 6 (S2→S3): 148420/150000 received, 28 misses, latency 22.9 / 77.0 / 320823.1 µs; flow 7 (S2→S1): 74210/75000 received, 16 misses, latency 20.7 / 76.8 / 320820.9 µs; flow 8 (S2→S3): 37105/37500 received, 6 misses, latency 38.6 / 90.4 / 320753.7 µs; flow 9 (S3→S2): 37128/37499 received, 59 misses, latency 41.8 / 309.2 / 320841.9 µs; flow 12 (S1→S2): 37130/37500 received, 37 misses, latency 24.5 / 284.3 / 320824.6 µs; flow 14 (S1→S3): 150000/150000 received, 6 misses, latency 15.6 / 15.8 / 216.8 µs; flow 16 (S2→S1): 74210/75000 received, 16 misses, latency 37.7 / 89.5 / 320798.4 µs; flow 20 (S2→S1): 37105/37500 received, 7 misses, latency 24.5 / 76.4 / 320752.7 µs
- **heuristic C9-off**: no flow lost >100 frames or missed a deadline
- **heuristic C9-on**: no flow lost >100 frames or missed a deadline
- **RL C9-off**: no flow lost >100 frames or missed a deadline
- **RL C9-on**: no flow lost >100 frames or missed a deadline
- **Problem 3 heuristic C9-off**: flow 18 (S3→S1): 149991/149991 received, 1 misses, latency 11.4 / 11.8 / 207.1 µs
- **Problem 3 heuristic C9-on**: no flow lost >100 frames or missed a deadline
- **Problem 3 RL C9-off**: no flow lost >100 frames or missed a deadline
- **Problem 3 RL C9-on**: flow 2 (S3→S2): 37105/37498 received, 8 misses, latency 109.3 / 178.0 / 320586.2 µs; flow 6 (S2→S3): 148410/149994 received, 21 misses, latency 17.7 / 63.5 / 320818.3 µs; flow 7 (S2→S1): 74205/74998 received, 9 misses, latency 9.7 / 49.0 / 320783.3 µs; flow 8 (S2→S3): 37103/37499 received, 5 misses, latency 35.8 / 79.3 / 320751.8 µs; flow 12 (S1→S2): 37110/37500 received, 11 misses, latency 24.8 / 118.9 / 320791.5 µs; flow 14 (S1→S3): 150000/150000 received, 1 misses, latency 12.8 / 13.2 / 200.8 µs; flow 16 (S2→S1): 74205/74998 received, 9 misses, latency 33.5 / 74.7 / 320768.9 µs; flow 19 (S3→S2): 74207/74995 received, 16 misses, latency 26.6 / 132.4 / 320783.6 µs; flow 20 (S2→S1): 37104/37500 received, 5 misses, latency 24.8 / 68.0 / 320723.1 µs; flow 22 (S1→S2): 74218/75000 received, 20 misses, latency 12.8 / 98.9 / 320606.2 µs; flow 23 (S2→S1): 74206/75000 received, 8 misses, latency 14.1 / 103.0 / 320712.4 µs; flow 29 (S2→S3): 37104/37500 received, 5 misses, latency 138.1 / 181.2 / 320369.5 µs; flow 40 (S3→S2): 37104/37497 received, 8 misses, latency 36.4 / 105.7 / 320603.9 µs
