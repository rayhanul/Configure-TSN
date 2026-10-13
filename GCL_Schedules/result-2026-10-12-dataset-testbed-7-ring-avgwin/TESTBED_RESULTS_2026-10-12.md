# Testbed results: result-2026-10-12-dataset-testbed-7-ring-avgwin (2026-10-12)

Independent export validation is recorded in [validation.json](validation.json) and each package’s `independent-verification.log`. Admission latency-report consistency failures remain; measured delivery does not establish deadline guarantees.

Each package's GCLs were deployed on all of its switch ports, its scheduled flows admitted (VLANs + MSTP, all switches in one MST region), every route pinged, then 30 s of traffic on S1, S2, S3 at once (NIC launch time, NIC RX timestamps). Latest run of each package.

Rows in pipeline order, each approach C9 off then on. **Rank** orders the packages by deadline misses, then frames lost, then max latency (1 = best). **Flows** = admitted / offered: every flow of the dataset's base flow set for SMT, heuristic and RL; the base schedule's flows plus the arriving candidates for Problem 3. **Lost** = sent − received. **Deadline misses** = received frames whose latency exceeded their flow's deadline (deadline = period), with their share of received frames. **Latency** = receiver NIC's RX timestamp − sender NIC's launch time over all received frames (min / frame-weighted avg / max). **Jitter** = per-flow standard deviation of latency: best flow / average over the package's flows / worst flow.

| Rank | Package | Flows (admitted / offered) | Sent | Received | Lost | Deadline misses (%) | Latency min / avg / max (µs) | Jitter stddev best / avg / worst flow (µs) |
|---|---|---|---|---|---|---|---|---|
| 4 | SMT C9-off | 11 / 20 | 1,012,475 | 1,012,475 | 0 | 0 (0.00%) | 33.5 / 60.7 / 83.8 | 0.1 / 0.1 / 0.1 |
| 10 | SMT C9-on | 11 / 20 | 1,012,469 | 1,005,015 | 7,454 | 224 (0.02%) | 10.5 / 73.1 / 320842.1 | 0.1 / 3540.3 / 9066.0 |
| 2 | heuristic C9-off | 11 / 20 | 1,012,468 | 1,012,468 | 0 | 0 (0.00%) | 22.0 / 49.2 / 67.2 | 0.1 / 0.1 / 0.2 |
| 8 | heuristic C9-on | 11 / 20 | 1,012,461 | 1,012,455 | 6 | 0 (0.00%) | 10.5 / 23.3 / 42.3 | 0.1 / 0.4 / 3.6 |
| 3 | RL C9-off | 11 / 20 | 1,012,477 | 1,012,477 | 0 | 0 (0.00%) | 21.5 / 49.0 / 67.5 | 0.1 / 0.7 / 6.3 |
| 1 | RL C9-on | 11 / 20 | 1,012,422 | 1,012,422 | 0 | 0 (0.00%) | 5.0 / 22.5 / 42.5 | 0.1 / 0.6 / 3.6 |
| 7 | Problem 3 heuristic C9-off | 29 / 50 | 2,174,724 | 2,174,724 | 0 | 0 (0.00%) | 6.6 / 45.2 / 336.5 | 0.1 / 3.8 / 72.1 |
| 6 | Problem 3 heuristic C9-on | 29 / 50 | 2,062,457 | 2,062,457 | 0 | 0 (0.00%) | 5.0 / 24.6 / 293.6 | 0.1 / 0.3 / 3.6 |
| 5 | Problem 3 RL C9-off | 28 / 50 | 1,912,453 | 1,912,453 | 0 | 0 (0.00%) | 5.0 / 45.8 / 131.4 | 0.1 / 2.0 / 15.6 |
| 9 | Problem 3 RL C9-on | 31 / 50 | 2,174,813 | 2,174,788 | 25 | 1 (0.00%) | 5.0 / 27.1 / 296.3 | 0.1 / 0.6 / 6.2 |
| | **Total** | | **14,399,219** | **14,391,734** | **7,485** | **225 (0.00%)** | | |

## Details

**Received %** shows a lost frame even when it rounds to 100%. **No NIC ts** = received frames without a hardware timestamp (left out of latency). **Jitter RFC 3550** = mean |Δ latency| between consecutive frames, best flow / average / worst flow. **Worst latency, % of deadline** = the largest max latency / deadline over the package's flows. **Above e2e bound** = flows whose max latency exceeded the scheduler's own end-to-end bound.

| Package | Received % | No NIC ts | Jitter RFC 3550 best / avg / worst flow (µs) | Worst latency, % of deadline | Above e2e bound | Routes ping OK | Switch queue drops | Run (`results.md` inside) |
|---|---|---|---|---|---|---|---|---|
| SMT C9-off | 100.0000% | 0 | 0.0 / 0.0 / 0.0 | 42% | 0 | 11/11 | sw02/p5 +48 | `smt-c9-off/7-t3600-c9off-minlat/results/results-2026-10-12` |
| SMT C9-on | 99.2638% | 0 | 0.0 / 7.5 / 17.3 | 160413% | 8 | 11/11 | sw01/p4 +1574, sw02/p4 +4740, sw02/p5 +52, sw07/p4 +770, sw08/p4 +370 | `smt-c9-on/7-fair-retimed-c9on/results/results-2026-10-12` |
| heuristic C9-off | 100.0000% | 0 | 0.0 / 0.0 / 0.2 | 34% | 0 | 11/11 | none | `heuristic-c9-off/7-matrix-c9off/results/results-2026-10-12` |
| heuristic C9-on | 99.9994% | 0 | 0.0 / 0.7 / 7.2 | 14% | 0 | 11/11 | none | `heuristic-c9-on/7-matrix-c9on/results/results-2026-10-12` |
| RL C9-off | 100.0000% | 0 | 0.0 / 1.2 / 12.6 | 34% | 0 | 11/11 | none | `rl-c9-off/7-matrix-c9off/results/results-2026-10-12` |
| RL C9-on | 100.0000% | 0 | 0.0 / 0.9 / 7.2 | 15% | 1 | 11/11 | none | `rl-c9-on/7-matrix-c9on/results/results-2026-10-12` |
| Problem 3 heuristic C9-off | 100.0000% | 0 | 0.0 / 3.7 / 68.8 | 42% | 0 | 29/29 | none | `prob3-heuristic-c9-off/7-heuristic-c9off-matrix/results/results-2026-10-12` |
| Problem 3 heuristic C9-on | 100.0000% | 0 | 0.0 / 0.5 / 7.2 | 37% | 0 | 29/29 | none | `prob3-heuristic-c9-on/7-heuristic-c9on-matrix/results/results-2026-10-12` |
| Problem 3 RL C9-off | 100.0000% | 0 | 0.0 / 3.1 / 30.4 | 34% | 0 | 28/28 | none | `prob3-rl-c9-off/7-rl-c9off-matrix/results/results-2026-10-12` |
| Problem 3 RL C9-on | 99.9989% | 0 | 0.0 / 1.0 / 12.5 | 113% | 4 | 31/31 | none | `prob3-rl-c9-on/7-rl-c9on-matrix/results/results-2026-10-12` |

## Flows with misses or notable loss

- **SMT C9-off**: no flow lost >100 frames or missed a deadline
- **SMT C9-on**: flow 1 (S1→S2): 148422/149998 received, 28 misses, latency 24.5 / 78.3 / 320024.7 µs; flow 3 (S2→S3): 74230/75000 received, 63 misses, latency 41.8 / 176.2 / 320842.1 µs; flow 5 (S1→S2): 37106/37500 received, 6 misses, latency 24.5 / 76.2 / 319951.6 µs; flow 7 (S2→S1): 37130/37500 received, 59 misses, latency 33.5 / 300.2 / 320033.7 µs; flow 12 (S1→S2): 148414/149998 received, 20 misses, latency 26.4 / 63.5 / 320026.5 µs; flow 15 (S1→S2): 74208/74999 received, 11 misses, latency 27.1 / 66.0 / 320004.6 µs; flow 19 (S1→S2): 37105/37500 received, 5 misses, latency 24.5 / 67.7 / 319957.2 µs; flow 20 (S3→S2): 148417/149991 received, 32 misses, latency 25.8 / 92.4 / 320826.0 µs
- **heuristic C9-off**: no flow lost >100 frames or missed a deadline
- **heuristic C9-on**: no flow lost >100 frames or missed a deadline
- **RL C9-off**: no flow lost >100 frames or missed a deadline
- **RL C9-on**: no flow lost >100 frames or missed a deadline
- **Problem 3 heuristic C9-off**: no flow lost >100 frames or missed a deadline
- **Problem 3 heuristic C9-on**: no flow lost >100 frames or missed a deadline
- **Problem 3 RL C9-off**: no flow lost >100 frames or missed a deadline
- **Problem 3 RL C9-on**: flow 20 (S3→S2): 149963/149966 received, 1 misses, latency 25.8 / 26.0 / 226.0 µs
