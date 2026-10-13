# Testbed results: result-2026-10-12-dataset-testbed-6-ring-avgwin (2026-10-12)
Final live configuration: **Problem 3 RL C9-on**, 27 scheduled flows, 800,000 ns cycle; all 19 operational GCLs independently read back and matched the package after all ten benchmarks completed.

Prior independent-validation findings remain: all four admission exports have latency-report consistency failures, and C9-off RL has a recomputed latency 80 ns over a deadline. See [validation details](VALIDATION.md). These are single 30-second measurements per package, not proof of deadline guarantees.

Each package's GCLs were deployed on all of its switch ports, its scheduled flows admitted (VLANs + MSTP, all switches in one MST region), every route pinged, then 30 s of traffic on S1, S2, S3 at once (NIC launch time, NIC RX timestamps). Latest run of each package.

Rows in pipeline order, each approach C9 off then on. **Rank** orders the packages by deadline misses, then frames lost, then max latency (1 = best). **Flows** = admitted / offered: every flow of the dataset's base flow set for SMT, heuristic and RL; the base schedule's flows plus the arriving candidates for Problem 3. **Lost** = sent − received. **Deadline misses** = received frames whose latency exceeded their flow's deadline (deadline = period), with their share of received frames. **Latency** = receiver NIC's RX timestamp − sender NIC's launch time over all received frames (min / frame-weighted avg / max). **Jitter** = per-flow standard deviation of latency: best flow / average over the package's flows / worst flow.

| Rank | Package | Flows (admitted / offered) | Sent | Received | Lost | Deadline misses (%) | Latency min / avg / max (µs) | Jitter stddev best / avg / worst flow (µs) |
|---|---|---|---|---|---|---|---|---|
| 8 | SMT C9-off | 10 / 20 | 1,012,447 | 1,012,447 | 0 | 5 (0.00%) | 20.5 / 53.6 / 834.1 | 0.1 / 1.1 / 9.2 |
| 9 | SMT C9-on | 10 / 20 | 1,012,459 | 1,012,452 | 7 | 7 (0.00%) | 12.4 / 23.8 / 815.0 | 0.1 / 1.2 / 10.9 |
| 2 | heuristic C9-off | 10 / 20 | 1,012,470 | 1,012,470 | 0 | 0 (0.00%) | 8.1 / 48.1 / 83.8 | 0.1 / 0.1 / 0.2 |
| 1 | heuristic C9-on | 10 / 20 | 1,012,470 | 1,012,470 | 0 | 0 (0.00%) | 8.1 / 21.8 / 42.3 | 0.1 / 0.3 / 1.4 |
| 4 | RL C9-off | 10 / 20 | 1,012,449 | 1,012,437 | 12 | 0 (0.00%) | 8.1 / 47.3 / 83.8 | 0.1 / 0.1 / 0.2 |
| 5 | RL C9-on | 10 / 20 | 1,012,460 | 1,012,459 | 1 | 1 (0.00%) | 6.6 / 21.7 / 217.1 | 0.1 / 0.4 / 2.8 |
| 10 | Problem 3 heuristic C9-off | 25 / 50 | 1,799,968 | 1,794,077 | 5,891 | 125 (0.01%) | 5.0 / 78.5 / 320817.7 | 0.1 / 1745.7 / 6533.7 |
| 3 | Problem 3 heuristic C9-on | 25 / 50 | 1,799,950 | 1,799,939 | 11 | 0 (0.00%) | 5.0 / 58.8 / 488.3 | 0.1 / 0.4 / 3.8 |
| 7 | Problem 3 RL C9-off | 27 / 50 | 2,099,945 | 2,099,874 | 71 | 1 (0.00%) | 5.0 / 56.2 / 602.8 | 0.1 / 0.2 / 1.4 |
| 6 | Problem 3 RL C9-on | 27 / 50 | 2,024,948 | 2,024,946 | 2 | 1 (0.00%) | 5.0 / 36.7 / 209.6 | 0.1 / 9.8 / 97.2 |
| | **Total** | | **13,799,566** | **13,793,571** | **5,995** | **140 (0.00%)** | | |

## Details

**Received %** shows a lost frame even when it rounds to 100%. **No NIC ts** = received frames without a hardware timestamp (left out of latency). **Jitter RFC 3550** = mean |Δ latency| between consecutive frames, best flow / average / worst flow. **Worst latency, % of deadline** = the largest max latency / deadline over the package's flows. **Above e2e bound** = flows whose max latency exceeded the scheduler's own end-to-end bound.

| Package | Received % | No NIC ts | Jitter RFC 3550 best / avg / worst flow (µs) | Worst latency, % of deadline | Above e2e bound | Routes ping OK | Switch queue drops | Run (`results.md` inside) |
|---|---|---|---|---|---|---|---|---|
| SMT C9-off | 100.0000% | 0 | 0.0 / 0.1 / 0.3 | 104% | 1 | 10/10 | none | `smt-c9-off/6-t3600-c9off-minlat/results/results-2026-10-12` |
| SMT C9-on | 99.9993% | 0 | 0.0 / 0.0 / 0.3 | 102% | 1 | 10/10 | none | `smt-c9-on/6-fair-retimed-c9on/results/results-2026-10-12` |
| heuristic C9-off | 100.0000% | 0 | 0.0 / 0.1 / 0.2 | 42% | 0 | 10/10 | none | `heuristic-c9-off/6-matrix-c9off/results/results-2026-10-12` |
| heuristic C9-on | 100.0000% | 0 | 0.0 / 0.3 / 2.9 | 21% | 0 | 10/10 | none | `heuristic-c9-on/6-matrix-c9on/results/results-2026-10-12` |
| RL C9-off | 99.9988% | 0 | 0.0 / 0.1 / 0.2 | 42% | 0 | 10/10 | none | `rl-c9-off/6-matrix-c9off/results/results-2026-10-12` |
| RL C9-on | 99.9999% | 0 | 0.0 / 0.6 / 5.6 | 109% | 1 | 10/10 | none | `rl-c9-on/6-matrix-c9on/results/results-2026-10-12` |
| Problem 3 heuristic C9-off | 99.6727% | 0 | 0.0 / 5.7 / 33.7 | 160406% | 10 | 25/25 | sw01/p4 +1573, sw02/p4 +769, sw06/p4 +2, sw07/p4 +1974, sw08/p4 +1573 | `prob3-heuristic-c9-off/6-heuristic-c9off-matrix/results/results-2026-10-12` |
| Problem 3 heuristic C9-on | 99.9994% | 0 | 0.0 / 0.6 / 7.6 | 61% | 0 | 25/25 | none | `prob3-heuristic-c9-on/6-heuristic-c9on-matrix/results/results-2026-10-12` |
| Problem 3 RL C9-off | 99.9966% | 0 | 0.0 / 0.1 / 0.9 | 301% | 1 | 27/27 | none | `prob3-rl-c9-off/6-rl-c9off-matrix/results/results-2026-10-12` |
| Problem 3 RL C9-on | 99.9999% | 0 | 0.0 / 19.5 / 194.3 | 104% | 2 | 27/27 | none | `prob3-rl-c9-on/6-rl-c9on-matrix/results/results-2026-10-12` |

## Flows with misses or notable loss

- **SMT C9-off**: flow 4 (S1→S3): 37495/37495 received, 5 misses, latency 33.8 / 34.1 / 834.1 µs
- **SMT C9-on**: flow 4 (S1→S3): 37500/37500 received, 7 misses, latency 13.7 / 14.0 / 815.0 µs
- **heuristic C9-off**: no flow lost >100 frames or missed a deadline
- **heuristic C9-on**: no flow lost >100 frames or missed a deadline
- **RL C9-off**: no flow lost >100 frames or missed a deadline
- **RL C9-on**: flow 1 (S3→S1): 149991/149991 received, 1 misses, latency 16.9 / 17.1 / 217.1 µs
- **Problem 3 heuristic C9-off**: flow 6 (S2→S1): 74213/75000 received, 15 misses, latency 71.3 / 135.7 / 320808.7 µs; flow 7 (S2→S1): 37107/37500 received, 8 misses, latency 47.3 / 116.0 / 320788.9 µs; flow 9 (S3→S2): 148418/149991 received, 32 misses, latency 83.4 / 150.0 / 320812.5 µs; flow 12 (S2→S1): 37107/37500 received, 8 misses, latency 47.0 / 115.7 / 320766.5 µs; flow 15 (S2→S3): 74211/75000 received, 13 misses, latency 23.9 / 84.3 / 320817.7 µs; flow 22 (S2→S3): 74210/75000 received, 12 misses, latency 19.8 / 72.2 / 320738.2 µs; flow 25 (S1→S2): 37115/37500 received, 16 misses, latency 116.0 / 252.0 / 320791.1 µs; flow 38 (S2→S3): 37105/37500 received, 6 misses, latency 21.0 / 94.3 / 320796.1 µs; flow 40 (S1→S2): 37114/37500 received, 15 misses, latency 30.2 / 158.0 / 320705.6 µs
- **Problem 3 heuristic C9-on**: no flow lost >100 frames or missed a deadline
- **Problem 3 RL C9-off**: flow 9 (S3→S2): 149979/149991 received, 1 misses, latency 83.4 / 83.6 / 602.8 µs
- **Problem 3 RL C9-on**: flow 9 (S3→S2): 149990/149990 received, 1 misses, latency 41.8 / 42.0 / 208.6 µs
