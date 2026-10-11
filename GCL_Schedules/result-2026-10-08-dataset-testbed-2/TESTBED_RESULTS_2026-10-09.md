# Testbed results: result-2026-10-08-dataset-testbed-2 (2026-10-09)

Each package's GCLs were deployed on all 27 switch ports (all live), its scheduled flows admitted (VLANs + MSTP, all 8 switches in one MST region), leftover VLAN interfaces removed on S1/S2/S3, every route pinged, then 30 s of traffic on S1, S2, S3 at once (NIC launch time, NIC RX timestamps). Full per-flow reports: `<package>/results/results-<date>/results.md`.

Rows in pipeline order, each approach C9 off then on. **Rank** orders the packages by deadline misses, then frames lost, then max latency (1 = best). **Flows** = admitted / offered: every flow of the dataset's base flow set for SMT, heuristic and RL; the base schedule's flows plus the arriving candidates for Problem 3. **Lost** = sent − received. **Deadline misses** = received frames whose latency exceeded their flow's deadline (deadline = period), with their share of received frames. **Latency** = receiver NIC's RX timestamp − sender NIC's launch time over all received frames (min / frame-weighted avg / max). **Jitter** = per-flow standard deviation of latency: best flow / average over the package's flows / worst flow.

| Rank | Package | Flows (admitted / offered) | Sent | Received | Lost | Deadline misses (%) | Latency min / avg / max (µs) | Jitter stddev best / avg / worst flow (µs) |
|---|---|---|---|---|---|---|---|---|
| 5 | SMT C9-off | 11 / 20 | 1,012,500 | 937,473 | 75,027 | 75,001 (8.00%) | 33.5 / 97.9 / 833.7 | 0.1 / 1.3 / 10.9 |
| 3 | SMT C9-on | 11 / 20 | 1,012,493 | 1,012,477 | 16 | 14 (0.00%) | 8.8 / 38.8 / 813.5 | 0.1 / 18.4 / 72.3 |
| 4 | Problem 3 heuristic C9-off | 22 / 50 | 1,649,990 | 452,677 | 1,197,313 | 2,527 (0.56%) | 21.6 / 6233.8 / 2998350.4 | 0.1 / 241842.2 / 542721.5 |
| 2 | Problem 3 heuristic C9-on | 25 / 50 | 1,949,972 | 1,499,844 | 450,128 | 4 (0.00%) | 5.0 / 39.6 / 404.9 | 0.1 / 12.5 / 68.6 |
| 1 | Problem 3 RL C9-off | 26 / 50 | 1,912,475 | 1,687,384 | 225,091 | 1 (0.00%) | 8.5 / 63.2 / 360.8 | 0.1 / 0.7 / 6.4 |
| 6 | Problem 3 RL C9-on | 32 / 50 | 2,549,967 | 2,099,884 | 450,083 | 149,986 (7.14%) | 8.1 / 56.8 / 498.2 | 0.1 / 7.8 / 75.8 |
| | **Total** | | **10,087,397** | **7,689,739** | **2,397,658** | **227,533 (2.96%)** | | |

## Details

**Received %** shows a lost frame even when it rounds to 100%. **No NIC ts** = received frames without a hardware timestamp (left out of latency). **Jitter RFC 3550** = mean |Δ latency| between consecutive frames, best flow / average / worst flow. **Worst latency, % of deadline** = the largest max latency / deadline over the package's flows. **Above e2e bound** = flows whose max latency exceeded the scheduler's own end-to-end bound.

| Package | Received % | No NIC ts | Jitter RFC 3550 best / avg / worst flow (µs) | Worst latency, % of deadline | Above e2e bound | Routes ping OK | Switch queue drops | Run (`results.md` inside) |
|---|---|---|---|---|---|---|---|---|
| SMT C9-off | 92.5899% | 0 | 0.0 / 0.0 / 0.3 | 108% | 2 | 10/11 (failed: 11) | none | `smt-c9-off/2-t3600-c9off-minlat/results/results-2026-10-09_2` |
| SMT C9-on | 99.9984% | 0 | 0.0 / 32.4 / 144.7 | 102% | 5 | 11/11 | none | `smt-c9-on/2-fair-retimed-c9on/results/results-2026-10-09` |
| Problem 3 heuristic C9-off | 27.4351% | 0 | 0.0 / 127813.0 / 301985.3 | 1499175% | 12 | 15/22 (failed: 11, 15, 22, 26, 36, 37, 48) | sw08/p2 +560893, sw08/p5 +186346 | `prob3-heuristic-c9-off/2-heuristic-c9off-matrix/results/results-2026-10-09` |
| Problem 3 heuristic C9-on | 76.9162% | 0 | 0.0 / 24.7 / 137.2 | 115% | 7 | 18/25 (failed: 11, 15, 22, 26, 36, 37, 48) | none | `prob3-heuristic-c9-on/2-heuristic-c9on-matrix/results/results-2026-10-09` |
| Problem 3 RL C9-off | 88.2304% | 0 | 0.0 / 0.9 / 12.8 | 180% | 2 | 22/26 (failed: 11, 15, 22, 37) | none | `prob3-rl-c9-off/2-rl-c9off-matrix/results/results-2026-10-09` |
| Problem 3 RL C9-on | 82.3495% | 0 | 0.0 / 15.0 / 151.5 | 111% | 3 | 25/32 (failed: 11, 15, 22, 26, 36, 37, 48) | none | `prob3-rl-c9-on/2-rl-c9on-matrix/results/results-2026-10-09` |

## Flows with misses or notable loss

- **SMT C9-off**: flow 4 (S1→S3): 37500/37500 received, 7 misses, latency 33.5 / 33.9 / 833.7 µs; flow 7 (S3→S1): 74995/75000 received, 74994 misses, latency 36.4 / 433.7 / 433.9 µs; flow 11 (S2→S3): 0/75000 received, 0 misses, latency – µs
- **SMT C9-on**: flow 4 (S1→S3): 37500/37500 received, 14 misses, latency 9.7 / 10.4 / 813.5 µs
- **Problem 3 heuristic C9-off**: flow 1 (S1→S2): 462/150000 received, 440 misses, latency 166.4 / 816884.7 / 999737.7 µs; flow 6 (S2→S1): 216/37500 received, 186 misses, latency 118.5 / 836854.6 / 998721.3 µs; flow 9 (S1→S2): 446/150000 received, 439 misses, latency 145.6 / 845737.9 / 999716.9 µs; flow 10 (S3→S2): 93/37500 received, 93 misses, latency 224475.5 / 2056789.6 / 2998279.7 µs; flow 11 (S2→S3): 0/74995 received, 0 misses, latency – µs; flow 12 (S2→S1): 246/37500 received, 216 misses, latency 54.3 / 856036.2 / 998732.3 µs; flow 14 (S3→S2): 348/150000 received, 348 misses, latency 224157.1 / 2089986.5 / 2998350.4 µs; flow 15 (S2→S3): 0/75000 received, 0 misses, latency – µs; flow 18 (S2→S1): 149984/150000 received, 30 misses, latency 59.2 / 65.6 / 303.1 µs; flow 20 (S3→S2): 223/75000 received, 216 misses, latency 124.0 / 812183.9 / 999520.9 µs; flow 22 (S2→S3): 0/37500 received, 0 misses, latency – µs; flow 26 (S2→S3): 0/74998 received, 0 misses, latency – µs; flow 36 (S2→S3): 0/75000 received, 0 misses, latency – µs; flow 37 (S2→S3): 0/37500 received, 0 misses, latency – µs; flow 40 (S2→S1): 216/37500 received, 186 misses, latency 107.0 / 836842.9 / 998709.4 µs; flow 48 (S2→S3): 0/75000 received, 0 misses, latency – µs; flow 49 (S2→S1): 463/75000 received, 373 misses, latency 75.0 / 781117.2 / 998679.7 µs
- **Problem 3 heuristic C9-on**: flow 1 (S1→S2): 149981/149997 received, 4 misses, latency 29.6 / 29.9 / 229.9 µs; flow 11 (S2→S3): 0/74995 received, 0 misses, latency – µs; flow 15 (S2→S3): 0/75000 received, 0 misses, latency – µs; flow 22 (S2→S3): 0/37500 received, 0 misses, latency – µs; flow 26 (S2→S3): 0/75000 received, 0 misses, latency – µs; flow 36 (S2→S3): 0/74994 received, 0 misses, latency – µs; flow 37 (S2→S3): 0/37500 received, 0 misses, latency – µs; flow 48 (S2→S3): 0/75000 received, 0 misses, latency – µs
- **Problem 3 RL C9-off**: flow 11 (S2→S3): 0/75000 received, 0 misses, latency – µs; flow 14 (S3→S2): 149965/149991 received, 1 misses, latency 79.6 / 79.8 / 360.8 µs; flow 15 (S2→S3): 0/75000 received, 0 misses, latency – µs; flow 22 (S2→S3): 0/37500 received, 0 misses, latency – µs; flow 37 (S2→S3): 0/37500 received, 0 misses, latency – µs
- **Problem 3 RL C9-on**: flow 11 (S2→S3): 0/74993 received, 0 misses, latency – µs; flow 14 (S3→S2): 149990/150000 received, 74996 misses, latency 69.4 / 145.7 / 222.2 µs; flow 15 (S2→S3): 0/74993 received, 0 misses, latency – µs; flow 18 (S2→S1): 149984/150000 received, 74990 misses, latency 20.0 / 143.7 / 219.9 µs; flow 22 (S2→S3): 0/37493 received, 0 misses, latency – µs; flow 26 (S2→S3): 0/75000 received, 0 misses, latency – µs; flow 36 (S2→S3): 0/75000 received, 0 misses, latency – µs; flow 37 (S2→S3): 0/37500 received, 0 misses, latency – µs; flow 48 (S2→S3): 0/75000 received, 0 misses, latency – µs
