# Testbed results: result-2026-10-09-dataset-testbed-4-avgwin (2026-10-10)

**Round 1, as generated** (the tables below up to "Final round"). These packages missed deadlines because of causes A, B, C and D, all since fixed; final results and causes: [../result-2026-10-10-dataset-testbed-4-saf/SUMMARY_REPORT_2026-10-10.md](../result-2026-10-10-dataset-testbed-4-saf/SUMMARY_REPORT_2026-10-10.md). The C9-on packages here are the originals (C9-on spaced for cut-through switches, cause B); their regenerated versions and final runs are in `../result-2026-10-10-dataset-testbed-4-saf/`.

Each package's GCLs were deployed on all of its switch ports (all live), its scheduled flows admitted (VLANs + MSTP, all 8 switches in one MST region), leftover VLAN interfaces removed on S1/S2/S3, every route pinged, then 30 s of traffic on S1, S2, S3 at once (NIC launch time, NIC RX timestamps). Full per-flow reports: `<package>/results/results-<date>/results.md`.

## Round 1: as generated, before the fixes

Rows in pipeline order, each approach C9 off then on. **Rank** orders the packages by deadline misses, then frames lost, then max latency (1 = best). **Flows** = admitted / offered: every flow of the dataset's base flow set for SMT, heuristic and RL; the base schedule's flows plus the arriving candidates for Problem 3. **Lost** = sent − received. **Deadline misses** = received frames whose latency exceeded their flow's deadline (deadline = period), with their share of received frames. **Latency** = receiver NIC's RX timestamp − sender NIC's launch time over all received frames (min / frame-weighted avg / max). **Jitter** = per-flow standard deviation of latency: best flow / average over the package's flows / worst flow.

| Rank | Package | Flows (admitted / offered) | Sent | Received | Lost | Deadline misses (%) | Latency min / avg / max (µs) | Jitter stddev best / avg / worst flow (µs) |
|---|---|---|---|---|---|---|---|---|
| 9 | SMT C9-off | 11 / 20 | 1,012,500 | 1,012,479 | 21 | 74,994 (7.41%) | 67.0 / 111.7 / 273.3 | 0.1 / 12.3 / 94.5 |
| 3 | SMT C9-on | 11 / 20 | 1,012,500 | 1,012,472 | 28 | 12,320 (1.22%) | 17.1 / 51.0 / 1198.1 | 0.1 / 15.1 / 138.6 |
| 8 | heuristic C9-off | 11 / 20 | 1,012,482 | 1,012,436 | 46 | 74,983 (7.41%) | 19.0 / 93.8 / 224.4 | 0.1 / 12.9 / 97.4 |
| 2 | heuristic C9-on | 11 / 20 | 1,012,500 | 1,012,475 | 25 | 1 (0.00%) | 15.8 / 32.4 / 428.0 | 0.1 / 2.9 / 18.0 |
| 1 | RL C9-off | 11 / 20 | 1,012,493 | 1,012,444 | 49 | 0 (0.00%) | 19.0 / 81.7 / 133.8 | 0.1 / 7.8 / 46.2 |
| 5 | RL C9-on | 11 / 20 | 1,012,500 | 1,012,477 | 23 | 27,392 (2.71%) | 16.9 / 56.2 / 422.1 | 0.1 / 17.3 / 176.1 |
| 10 | Problem 3 heuristic C9-off | 24 / 50 | 1,612,418 | 1,612,301 | 117 | 74,994 (4.65%) | 12.8 / 94.7 / 420.6 | 0.1 / 8.1 / 97.3 |
| 6 | Problem 3 heuristic C9-on | 29 / 50 | 2,137,495 | 2,137,174 | 321 | 37,499 (1.75%) | 9.7 / 49.7 / 568.3 | 0.1 / 9.9 / 197.7 |
| 7 | Problem 3 RL C9-off | 28 / 50 | 2,025,000 | 2,009,876 | 15,124 | 74,364 (3.70%) | 9.6 / 107.0 / 320964.9 | 0.2 / 1960.5 / 4668.9 |
| 4 | Problem 3 RL C9-on | 28 / 50 | 2,062,500 | 2,052,201 | 10,299 | 27,316 (1.33%) | 9.7 / 67.0 / 324839.5 | 0.1 / 2375.7 / 6468.4 |
| | **Total** | | **13,912,388** | **13,886,335** | **26,053** | **403,863 (2.91%)** | | |

### Details

**Received %** shows a lost frame even when it rounds to 100%. **No NIC ts** = received frames without a hardware timestamp (left out of latency). **Jitter RFC 3550** = mean |Δ latency| between consecutive frames, best flow / average / worst flow. **Worst latency, % of deadline** = the largest max latency / deadline over the package's flows. **Above e2e bound** = flows whose max latency exceeded the scheduler's own end-to-end bound.

| Package | Received % | No NIC ts | Jitter RFC 3550 best / avg / worst flow (µs) | Worst latency, % of deadline | Above e2e bound | Routes ping OK | Switch queue drops | Run (`results.md` inside) |
|---|---|---|---|---|---|---|---|---|
| SMT C9-off | 99.9979% | 0 | 0.0 / 24.4 / 189.0 | 137% | 3 | 11/11 | none | `smt-c9-off/4-t3600-c9off-minlat/results/results-2026-10-10` |
| SMT C9-on | 99.9972% | 0 | 0.1 / 14.5 / 141.2 | 150% | 4 | 11/11 | none | `smt-c9-on/4-fair-retimed-c9on/results/results-2026-10-10` |
| heuristic C9-off | 99.9955% | 0 | 0.0 / 25.2 / 194.8 | 112% | 2 | 11/11 | none | `heuristic-c9-off/4-matrix-c9off/results/results-2026-10-10` |
| heuristic C9-on | 99.9975% | 0 | 0.0 / 5.6 / 35.9 | 107% | 3 | 11/11 | none | `heuristic-c9-on/4-matrix-c9on/results/results-2026-10-10` |
| RL C9-off | 99.9952% | 0 | 0.0 / 15.3 / 92.3 | 67% | 4 | 11/11 | none | `rl-c9-off/4-matrix-c9off/results/results-2026-10-10` |
| RL C9-on | 99.9977% | 0 | 0.0 / 26.9 / 270.3 | 106% | 5 | 11/11 | none | `rl-c9-on/4-matrix-c9on/results/results-2026-10-10` |
| Problem 3 heuristic C9-off | 99.9927% | 0 | 0.0 / 15.9 / 194.6 | 129% | 3 | 24/24 | none | `prob3-heuristic-c9-off/4-heuristic-c9off-matrix/results/results-2026-10-10` |
| Problem 3 heuristic C9-on | 99.9850% | 0 | 0.0 / 19.6 / 395.3 | 107% | 11 | 29/29 | none | `prob3-heuristic-c9-on/4-heuristic-c9on-matrix/results/results-2026-10-10` |
| Problem 3 RL C9-off | 99.2531% | 0 | 0.0 / 22.1 / 147.1 | 160442% | 18 | 28/28 | sw03/p4 +12, sw05/p4 +3578, sw06/p4 +5569, sw07/p4 +4349, sw08/p4 +1573 | `prob3-rl-c9-off/4-rl-c9off-matrix/results/results-2026-10-10` |
| Problem 3 RL C9-on | 99.5007% | 0 | 0.1 / 20.1 / 278.9 | 160411% | 17 | 28/28 | sw03/p4 +11, sw05/p4 +1950, sw06/p4 +1172, sw07/p4 +5138, sw08/p4 +1969 | `prob3-rl-c9-on/4-rl-c9on-matrix/results/results-2026-10-10` |

### Flows with misses or notable loss

- **SMT C9-off**: flow 14 (S3→S2): 149990/150000 received, 74994 misses, latency 72.6 / 178.4 / 273.3 µs
- **SMT C9-on**: flow 9 (S1→S3): 37500/37500 received, 16 misses, latency 39.2 / 398.2 / 1198.1 µs; flow 14 (S3→S2): 149991/150000 received, 2 misses, latency 31.2 / 31.6 / 231.8 µs; flow 19 (S2→S3): 74999/75000 received, 12302 misses, latency 28.0 / 111.3 / 423.5 µs
- **heuristic C9-off**: flow 14 (S3→S2): 149970/149991 received, 74983 misses, latency 28.0 / 126.1 / 224.4 µs
- **heuristic C9-on**: flow 19 (S2→S3): 74999/75000 received, 1 misses, latency 28.1 / 46.7 / 428.0 µs
- **RL C9-off**: no flow lost >100 frames or missed a deadline
- **RL C9-on**: flow 19 (S2→S3): 75000/75000 received, 27392 misses, latency 28.1 / 190.2 / 422.1 µs
- **Problem 3 heuristic C9-off**: flow 14 (S3→S2): 149989/150000 received, 74993 misses, latency 28.0 / 126.0 / 224.4 µs; flow 20 (S1→S3): 149961/149977 received, 1 misses, latency 133.3 / 133.5 / 258.7 µs
- **Problem 3 heuristic C9-on**: flow 19 (S2→S3): 75000/75000 received, 37499 misses, latency 29.0 / 230.2 / 428.7 µs
- **Problem 3 RL C9-off**: flow 3 (S2→S3): 74211/75000 received, 18 misses, latency 83.3 / 139.6 / 320883.6 µs; flow 6 (S1→S3): 37099/37500 received, 0 misses, latency 134.2 / 134.5 / 715.6 µs; flow 7 (S1→S3): 37106/37500 received, 9 misses, latency 235.0 / 287.0 / 320851.2 µs; flow 8 (S2→S3): 148418/150000 received, 26 misses, latency 83.6 / 175.8 / 320883.6 µs; flow 9 (S1→S3): 37099/37500 received, 1 misses, latency 111.8 / 112.1 / 808.7 µs; flow 11 (S2→S1): 37107/37500 received, 8 misses, latency 30.9 / 100.1 / 320727.7 µs; flow 12 (S2→S3): 74208/75000 received, 13 misses, latency 87.5 / 157.7 / 320850.3 µs; flow 13 (S1→S2): 148409/150000 received, 9 misses, latency 19.1 / 39.4 / 320005.2 µs; flow 14 (S3→S2): 148397/150000 received, 37110 misses, latency 28.1 / 131.2 / 320811.3 µs; flow 15 (S3→S2): 148399/150000 received, 13 misses, latency 33.2 / 128.2 / 320778.1 µs; flow 18 (S2→S1): 37107/37500 received, 8 misses, latency 41.2 / 110.3 / 320738.0 µs; flow 19 (S2→S3): 74211/75000 received, 18 misses, latency 83.3 / 135.3 / 320859.6 µs; flow 20 (S1→S3): 148398/150000 received, 37104 misses, latency 133.3 / 172.1 / 1067.9 µs; flow 21 (S2→S1): 37107/37500 received, 8 misses, latency 21.5 / 90.7 / 320719.0 µs; flow 23 (S2→S1): 37105/37500 received, 7 misses, latency 15.9 / 76.7 / 320709.5 µs; flow 29 (S1→S2): 74204/75000 received, 4 misses, latency 9.6 / 44.9 / 319781.0 µs; flow 30 (S1→S2): 74204/75000 received, 4 misses, latency 30.0 / 47.6 / 319771.0 µs; flow 45 (S3→S1): 37101/37500 received, 4 misses, latency 154.3 / 189.4 / 320964.9 µs
- **Problem 3 RL C9-on**: flow 1 (S3→S2): 74213/75000 received, 13 misses, latency 21.0 / 76.9 / 319983.7 µs; flow 3 (S2→S3): 74204/75000 received, 7 misses, latency 25.2 / 51.3 / 320801.8 µs; flow 4 (S3→S2): 37106/37500 received, 6 misses, latency 53.8 / 108.1 / 319987.2 µs; flow 6 (S1→S3): 37102/37500 received, 3 misses, latency 34.5 / 60.6 / 320778.8 µs; flow 8 (S2→S3): 148407/150000 received, 13 misses, latency 28.1 / 76.3 / 320822.6 µs; flow 9 (S1→S3): 37110/37500 received, 23 misses, latency 397.2 / 493.7 / 324839.5 µs; flow 10 (S3→S2): 74212/75000 received, 12 misses, latency 23.8 / 76.1 / 319996.3 µs; flow 11 (S2→S1): 37107/37500 received, 7 misses, latency 58.5 / 118.6 / 319997.7 µs; flow 19 (S2→S3): 74231/75000 received, 27175 misses, latency 28.0 / 323.5 / 320823.3 µs; flow 20 (S1→S3): 148407/150000 received, 13 misses, latency 26.2 / 56.0 / 320802.8 µs; flow 21 (S2→S1): 37106/37500 received, 6 misses, latency 35.3 / 86.9 / 319979.3 µs; flow 22 (S2→S1): 37106/37500 received, 6 misses, latency 68.7 / 120.3 / 319888.6 µs; flow 23 (S2→S1): 37105/37500 received, 6 misses, latency 68.7 / 120.3 / 319691.2 µs; flow 42 (S1→S2): 37109/37500 received, 10 misses, latency 26.8 / 112.4 / 320719.7 µs; flow 48 (S1→S2): 37109/37500 received, 10 misses, latency 16.1 / 102.2 / 320709.8 µs; flow 50 (S2→S1): 37106/37500 received, 6 misses, latency 58.5 / 110.0 / 319658.5 µs


## Final round: C9-off packages (2026-10-10, fixes A and C in place)

Same packages as above (C9-off schedules unchanged), rerun after fix A (one NIC launch-time queue) and fix C (etf delta 600 µs). Fix D (wait for the spanning tree to settle) came later, but none of these runs hit the spanning-tree stall. Latest run of each package.

| Rank | Package | Flows (admitted / offered) | Sent | Received | Lost | Deadline misses (%) | Latency min / avg / max (µs) | Jitter stddev best / avg / worst flow (µs) |
|---|---|---|---|---|---|---|---|---|
| 1 | SMT C9-off | 11 / 20 | 1,012,445 | 1,012,445 | 0 | 0 (0.00%) | 66.8 / 90.0 / 133.7 | 0.1 / 0.1 / 0.1 |
| 5 | heuristic C9-off | 11 / 20 | 1,012,482 | 1,012,473 | 9 | 0 (0.00%) | 19.0 / 73.7 / 134.0 | 0.1 / 0.6 / 5.7 |
| 1 | RL C9-off | 11 / 20 | 1,012,488 | 1,012,488 | 0 | 0 (0.00%) | 19.1 / 72.0 / 133.7 | 0.1 / 1.8 / 18.7 |
| 4 | Problem 3 heuristic C9-off | 24 / 50 | 1,612,431 | 1,612,423 | 8 | 0 (0.00%) | 12.8 / 82.4 / 420.7 | 0.1 / 2.5 / 49.9 |
| 3 | Problem 3 RL C9-off | 28 / 50 | 2,024,967 | 2,024,967 | 0 | 0 (0.00%) | 9.7 / 67.4 / 235.5 | 0.1 / 2.6 / 25.0 |
| | **Total** | | **6,674,813** | **6,674,796** | **17** | **0 (0.00%)** | | |

### Details

**Received %** shows a lost frame even when it rounds to 100%. **No NIC ts** = received frames without a hardware timestamp (left out of latency). **Jitter RFC 3550** = mean |Δ latency| between consecutive frames, best flow / average / worst flow. **Worst latency, % of deadline** = the largest max latency / deadline over the package's flows. **Above e2e bound** = flows whose max latency exceeded the scheduler's own end-to-end bound.

| Package | Received % | No NIC ts | Jitter RFC 3550 best / avg / worst flow (µs) | Worst latency, % of deadline | Above e2e bound | Routes ping OK | Switch queue drops | Run (`results.md` inside) |
|---|---|---|---|---|---|---|---|---|
| SMT C9-off | 100.0000% | 0 | 0.0 / 0.0 / 0.1 | 67% | 1 | 11/11 | none | `smt-c9-off/4-t3600-c9off-minlat/results/results-2026-10-10_5` |
| heuristic C9-off | 99.9991% | 0 | 0.0 / 0.6 / 6.6 | 67% | 0 | 11/11 | none | `heuristic-c9-off/4-matrix-c9off/results/results-2026-10-10_3` |
| RL C9-off | 100.0000% | 0 | 0.0 / 3.5 / 37.4 | 67% | 0 | 11/11 | none | `rl-c9-off/4-matrix-c9off/results/results-2026-10-10_3` |
| Problem 3 heuristic C9-off | 99.9995% | 0 | 0.0 / 4.6 / 99.8 | 75% | 0 | 24/24 | none | `prob3-heuristic-c9-off/4-heuristic-c9off-matrix/results/results-2026-10-10_3` |
| Problem 3 RL C9-off | 100.0000% | 0 | 0.0 / 4.8 / 50.0 | 67% | 0 | 28/28 | none | `prob3-rl-c9-off/4-rl-c9off-matrix/results/results-2026-10-10_4` |

### Flows with misses or notable loss

- **SMT C9-off**: no flow lost >100 frames or missed a deadline
- **heuristic C9-off**: no flow lost >100 frames or missed a deadline
- **RL C9-off**: no flow lost >100 frames or missed a deadline
- **Problem 3 heuristic C9-off**: no flow lost >100 frames or missed a deadline
- **Problem 3 RL C9-off**: no flow lost >100 frames or missed a deadline
