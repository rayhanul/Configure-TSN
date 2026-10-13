# Testbed results: result-2026-10-12-dataset-testbed-8-ring-avgwin (2026-10-12)

Independent export validation is recorded in [validation.json](validation.json) and each package’s `independent-verification.log`. Admission latency-report consistency failures remain; measured delivery does not establish deadline guarantees.

Each package's GCLs were deployed on all of its switch ports, its scheduled flows admitted (VLANs + MSTP, all switches in one MST region), every route pinged, then 30 s of traffic on S1, S2, S3 at once (NIC launch time, NIC RX timestamps). Latest run of each package.

Rows in pipeline order, each approach C9 off then on. **Rank** orders the packages by deadline misses, then frames lost, then max latency (1 = best). **Flows** = admitted / offered: every flow of the dataset's base flow set for SMT, heuristic and RL; the base schedule's flows plus the arriving candidates for Problem 3. **Lost** = sent − received. **Deadline misses** = received frames whose latency exceeded their flow's deadline (deadline = period), with their share of received frames. **Latency** = receiver NIC's RX timestamp − sender NIC's launch time over all received frames (min / frame-weighted avg / max). **Jitter** = per-flow standard deviation of latency: best flow / average over the package's flows / worst flow.

| Rank | Package | Flows (admitted / offered) | Sent | Received | Lost | Deadline misses (%) | Latency min / avg / max (µs) | Jitter stddev best / avg / worst flow (µs) |
|---|---|---|---|---|---|---|---|---|
| 7 | SMT C9-off | 10 / 20 | 862,487 | 862,487 | 0 | 6 (0.00%) | 33.5 / 53.7 / 833.7 | 0.1 / 1.1 / 10.1 |
| 6 | SMT C9-on | 10 / 20 | 862,498 | 862,498 | 0 | 4 (0.00%) | 9.3 / 22.6 / 385.6 | 0.1 / 0.3 / 1.4 |
| 3 | heuristic C9-off | 10 / 20 | 862,489 | 862,489 | 0 | 0 (0.00%) | 5.1 / 27.1 / 67.5 | 0.1 / 0.1 / 0.2 |
| 1 | heuristic C9-on | 10 / 20 | 862,491 | 862,491 | 0 | 0 (0.00%) | 5.0 / 19.9 / 40.1 | 0.1 / 0.1 / 0.2 |
| 2 | RL C9-off | 10 / 20 | 862,489 | 862,489 | 0 | 0 (0.00%) | 8.1 / 30.6 / 67.2 | 0.1 / 0.1 / 0.2 |
| 8 | RL C9-on | 10 / 20 | 862,485 | 862,115 | 370 | 31 (0.00%) | 5.0 / 30.9 / 320743.7 | 0.1 / 892.6 / 8925.2 |
| 4 | Problem 3 heuristic C9-off | 33 / 50 | 2,099,904 | 2,099,904 | 0 | 0 (0.00%) | 5.1 / 30.2 / 307.5 | 0.1 / 0.4 / 6.9 |
| 10 | Problem 3 heuristic C9-on | 39 / 50 | 2,849,863 | 2,842,766 | 7,097 | 121 (0.00%) | 5.0 / 33.0 / 320830.8 | 0.1 / 1218.0 / 5078.3 |
| 5 | Problem 3 RL C9-off | 34 / 50 | 2,324,942 | 2,324,940 | 2 | 0 (0.00%) | 8.1 / 47.9 / 296.3 | 0.1 / 2.8 / 44.5 |
| 9 | Problem 3 RL C9-on | 38 / 50 | 2,699,163 | 2,693,260 | 5,903 | 121 (0.00%) | 5.0 / 54.7 / 320825.7 | 0.1 / 1185.9 / 8513.8 |
| | **Total** | | **15,148,811** | **15,135,439** | **13,372** | **283 (0.00%)** | | |

## Details

**Received %** shows a lost frame even when it rounds to 100%. **No NIC ts** = received frames without a hardware timestamp (left out of latency). **Jitter RFC 3550** = mean |Δ latency| between consecutive frames, best flow / average / worst flow. **Worst latency, % of deadline** = the largest max latency / deadline over the package's flows. **Above e2e bound** = flows whose max latency exceeded the scheduler's own end-to-end bound.

| Package | Received % | No NIC ts | Jitter RFC 3550 best / avg / worst flow (µs) | Worst latency, % of deadline | Above e2e bound | Routes ping OK | Switch queue drops | Run (`results.md` inside) |
|---|---|---|---|---|---|---|---|---|
| SMT C9-off | 100.0000% | 0 | 0.0 / 0.0 / 0.3 | 104% | 1 | 10/10 | none | `smt-c9-off/8-t3600-c9off-minlat/results/results-2026-10-12` |
| SMT C9-on | 100.0000% | 0 | 0.0 / 0.0 / 0.1 | 106% | 2 | 10/10 | none | `smt-c9-on/8-fair-retimed-c9on/results/results-2026-10-12` |
| heuristic C9-off | 100.0000% | 0 | 0.0 / 0.1 / 0.2 | 34% | 0 | 10/10 | none | `heuristic-c9-off/8-matrix-c9off/results/results-2026-10-12` |
| heuristic C9-on | 100.0000% | 0 | 0.0 / 0.1 / 0.2 | 18% | 0 | 10/10 | none | `heuristic-c9-on/8-matrix-c9on/results/results-2026-10-12` |
| RL C9-off | 100.0000% | 0 | 0.0 / 0.1 / 0.2 | 34% | 0 | 10/10 | none | `rl-c9-off/8-matrix-c9off/results/results-2026-10-12` |
| RL C9-on | 99.9571% | 0 | 0.0 / 1.8 / 17.4 | 40093% | 2 | 10/10 | sw03/p4 +1, sw07/p4 +369 | `rl-c9-on/8-matrix-c9on/results/results-2026-10-12` |
| Problem 3 heuristic C9-off | 100.0000% | 0 | 0.0 / 0.7 / 13.6 | 38% | 0 | 33/33 | none | `prob3-heuristic-c9-off/8-heuristic-c9off-matrix/results/results-2026-10-12` |
| Problem 3 heuristic C9-on | 99.7510% | 0 | 0.0 / 8.3 / 89.8 | 160402% | 12 | 39/39 | sw01/p4 +1172, sw02/p4 +2769, sw06/p4 +7, sw07/p4 +1573, sw08/p2 +7, sw08/p4 +1569 | `prob3-heuristic-c9-on/8-heuristic-c9on-matrix/results/results-2026-10-12` |
| Problem 3 RL C9-off | 99.9999% | 0 | 0.0 / 4.9 / 89.0 | 37% | 0 | 34/34 | none | `prob3-rl-c9-off/8-rl-c9off-matrix/results/results-2026-10-12` |
| Problem 3 RL C9-on | 99.7813% | 0 | 0.0 / 8.7 / 76.8 | 160410% | 9 | 38/38 | sw01/p4 +371, sw02/p4 +3178, sw07/p4 +771, sw08/p2 +3, sw08/p4 +1573 | `prob3-rl-c9-on/8-rl-c9on-matrix/results/results-2026-10-12` |

## Flows with misses or notable loss

- **SMT C9-off**: flow 5 (S1→S3): 37500/37500 received, 6 misses, latency 33.5 / 33.8 / 833.7 µs
- **SMT C9-on**: flow 10 (S1→S3): 150000/150000 received, 4 misses, latency 10.4 / 10.7 / 212.0 µs
- **heuristic C9-off**: no flow lost >100 frames or missed a deadline
- **heuristic C9-on**: no flow lost >100 frames or missed a deadline
- **RL C9-off**: no flow lost >100 frames or missed a deadline
- **RL C9-on**: flow 12 (S2→S3): 37130/37500 received, 31 misses, latency 38.9 / 297.3 / 320743.7 µs
- **Problem 3 heuristic C9-off**: no flow lost >100 frames or missed a deadline
- **Problem 3 heuristic C9-on**: flow 1 (S2→S1): 74203/74988 received, 16 misses, latency 15.9 / 80.8 / 319999.9 µs; flow 7 (S2→S3): 37106/37499 received, 8 misses, latency 35.4 / 104.7 / 320745.0 µs; flow 8 (S1→S2): 148412/150000 received, 18 misses, latency 15.8 / 51.1 / 320804.8 µs; flow 11 (S3→S2): 74213/74996 received, 20 misses, latency 19.8 / 108.8 / 320830.8 µs; flow 12 (S2→S3): 37105/37498 received, 8 misses, latency 39.0 / 107.9 / 320755.0 µs; flow 21 (S3→S2): 37106/37498 received, 9 misses, latency 12.1 / 90.4 / 320811.0 µs; flow 22 (S2→S3): 74211/74998 received, 15 misses, latency 19.8 / 119.3 / 320713.2 µs; flow 26 (S1→S2): 74205/75000 received, 7 misses, latency 9.7 / 40.5 / 320588.9 µs; flow 28 (S2→S1): 37102/37494 received, 8 misses, latency 15.9 / 85.1 / 319990.5 µs; flow 32 (S2→S1): 37107/37499 received, 8 misses, latency 23.0 / 91.6 / 319711.4 µs; flow 46 (S1→S2): 37103/37500 received, 4 misses, latency 19.1 / 54.5 / 320783.0 µs
- **Problem 3 RL C9-off**: no flow lost >100 frames or missed a deadline
- **Problem 3 RL C9-on**: flow 1 (S2→S1): 74212/74999 received, 15 misses, latency 15.9 / 80.9 / 320800.2 µs; flow 7 (S2→S3): 37113/37499 received, 15 misses, latency 129.2 / 257.2 / 320745.4 µs; flow 8 (S1→S2): 148364/149953 received, 16 misses, latency 18.8 / 54.0 / 320819.2 µs; flow 12 (S2→S3): 37114/37499 received, 16 misses, latency 39.2 / 175.4 / 320755.3 µs; flow 21 (S3→S2): 37126/37500 received, 28 misses, latency 22.3 / 256.8 / 320825.7 µs; flow 26 (S1→S2): 74146/74941 received, 8 misses, latency 89.8 / 124.6 / 320771.8 µs; flow 28 (S2→S1): 37106/37499 received, 8 misses, latency 15.9 / 85.2 / 320790.9 µs; flow 32 (S2→S1): 37106/37499 received, 8 misses, latency 22.5 / 91.6 / 320732.6 µs; flow 44 (S1→S2): 74158/74953 received, 7 misses, latency 107.4 / 171.8 / 320601.7 µs
