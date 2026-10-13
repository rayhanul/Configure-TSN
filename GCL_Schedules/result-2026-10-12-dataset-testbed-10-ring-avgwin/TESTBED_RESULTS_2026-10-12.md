# Testbed results: result-2026-10-12-dataset-testbed-10-ring-avgwin (2026-10-12)

Independent export validation is recorded in [validation.json](validation.json) and each package’s `independent-verification.log`. Admission latency-report consistency failures remain; measured delivery does not establish deadline guarantees.

Each package's GCLs were deployed on all of its switch ports, its scheduled flows admitted (VLANs + MSTP, all switches in one MST region), every route pinged, then 30 s of traffic on S1, S2, S3 at once (NIC launch time, NIC RX timestamps). Latest run of each package.

Rows in pipeline order, each approach C9 off then on. **Rank** orders the packages by deadline misses, then frames lost, then max latency (1 = best). **Flows** = admitted / offered: every flow of the dataset's base flow set for SMT, heuristic and RL; the base schedule's flows plus the arriving candidates for Problem 3. **Lost** = sent − received. **Deadline misses** = received frames whose latency exceeded their flow's deadline (deadline = period), with their share of received frames. **Latency** = receiver NIC's RX timestamp − sender NIC's launch time over all received frames (min / frame-weighted avg / max). **Jitter** = per-flow standard deviation of latency: best flow / average over the package's flows / worst flow.

| Rank | Package | Flows (admitted / offered) | Sent | Received | Lost | Deadline misses (%) | Latency min / avg / max (µs) | Jitter stddev best / avg / worst flow (µs) |
|---|---|---|---|---|---|---|---|---|
| 7 | SMT C9-off | 11 / 20 | 1,012,478 | 1,012,478 | 0 | 2 (0.00%) | 33.5 / 62.3 / 233.7 | 0.1 / 0.2 / 0.8 |
| 10 | SMT C9-on | 11 / 20 | 1,012,482 | 1,006,223 | 6,259 | 245 (0.02%) | 13.7 / 75.4 / 320838.8 | 0.1 / 3161.7 / 9028.7 |
| 1 | heuristic C9-off | 11 / 20 | 1,012,480 | 1,012,480 | 0 | 0 (0.00%) | 9.7 / 43.9 / 71.9 | 0.1 / 1.4 / 8.8 |
| 9 | heuristic C9-on | 11 / 20 | 1,012,449 | 1,011,704 | 745 | 63 (0.01%) | 8.1 / 43.7 / 320777.1 | 0.1 / 1622.9 / 8927.4 |
| 1 | RL C9-off | 11 / 20 | 1,012,489 | 1,012,489 | 0 | 0 (0.00%) | 9.7 / 43.0 / 71.9 | 0.1 / 1.0 / 9.3 |
| 8 | RL C9-on | 11 / 20 | 1,012,481 | 1,012,481 | 0 | 30 (0.00%) | 8.1 / 24.6 / 301.2 | 0.1 / 0.5 / 3.8 |
| 6 | Problem 3 heuristic C9-off | 34 / 50 | 2,249,881 | 2,249,875 | 6 | 0 (0.00%) | 5.0 / 68.9 / 410.9 | 0.1 / 7.3 / 87.9 |
| 3 | Problem 3 heuristic C9-on | 33 / 50 | 2,174,946 | 2,174,946 | 0 | 0 (0.00%) | 5.0 / 35.8 / 206.0 | 0.1 / 1.6 / 44.9 |
| 4 | Problem 3 RL C9-off | 32 / 50 | 2,249,926 | 2,249,925 | 1 | 0 (0.00%) | 7.0 / 52.0 / 214.4 | 0.1 / 4.7 / 65.0 |
| 5 | Problem 3 RL C9-on | 38 / 50 | 2,699,834 | 2,699,833 | 1 | 0 (0.00%) | 5.0 / 36.7 / 263.0 | 0.1 / 2.5 / 53.8 |
| | **Total** | | **15,449,446** | **15,442,434** | **7,012** | **340 (0.00%)** | | |

## Details

**Received %** shows a lost frame even when it rounds to 100%. **No NIC ts** = received frames without a hardware timestamp (left out of latency). **Jitter RFC 3550** = mean |Δ latency| between consecutive frames, best flow / average / worst flow. **Worst latency, % of deadline** = the largest max latency / deadline over the package's flows. **Above e2e bound** = flows whose max latency exceeded the scheduler's own end-to-end bound.

| Package | Received % | No NIC ts | Jitter RFC 3550 best / avg / worst flow (µs) | Worst latency, % of deadline | Above e2e bound | Routes ping OK | Switch queue drops | Run (`results.md` inside) |
|---|---|---|---|---|---|---|---|---|
| SMT C9-off | 100.0000% | 0 | 0.0 / 0.0 / 0.0 | 117% | 1 | 11/11 | none | `smt-c9-off/10-t3600-c9off-minlat/results/results-2026-10-12` |
| SMT C9-on | 99.3818% | 0 | 0.0 / 5.1 / 17.3 | 160419% | 7 | 11/11 | sw01/p4 +1570, sw02/p4 +1940, sw03/p4 +6, sw07/p4 +2370, sw08/p4 +371 | `smt-c9-on/10-fair-retimed-c9on/results/results-2026-10-12` |
| heuristic C9-off | 100.0000% | 0 | 0.0 / 0.9 / 6.1 | 36% | 0 | 11/11 | none | `heuristic-c9-off/10-matrix-c9off/results/results-2026-10-12` |
| heuristic C9-on | 99.9264% | 0 | 0.0 / 3.2 / 17.4 | 40097% | 5 | 11/11 | sw02/p4 +370, sw08/p4 +370 | `heuristic-c9-on/10-matrix-c9on/results/results-2026-10-12` |
| RL C9-off | 100.0000% | 0 | 0.0 / 0.5 / 4.2 | 36% | 0 | 11/11 | none | `rl-c9-off/10-matrix-c9off/results/results-2026-10-12` |
| RL C9-on | 100.0000% | 0 | 0.0 / 0.1 / 0.2 | 151% | 2 | 11/11 | none | `rl-c9-on/10-matrix-c9on/results/results-2026-10-12` |
| Problem 3 heuristic C9-off | 99.9997% | 0 | 0.0 / 14.0 / 175.8 | 60% | 0 | 34/34 | none | `prob3-heuristic-c9-off/10-heuristic-c9off-matrix/results/results-2026-10-12` |
| Problem 3 heuristic C9-on | 100.0000% | 0 | 0.0 / 3.0 / 89.8 | 47% | 1 | 33/33 | none | `prob3-heuristic-c9-on/10-heuristic-c9on-matrix/results/results-2026-10-12` |
| Problem 3 RL C9-off | 99.99996% | 0 | 0.0 / 7.8 / 117.3 | 85% | 0 | 32/32 | none | `prob3-rl-c9-off/10-rl-c9off-matrix/results/results-2026-10-12` |
| Problem 3 RL C9-on | 99.99996% | 0 | 0.0 / 4.9 / 107.5 | 53% | 1 | 38/38 | none | `prob3-rl-c9-on/10-rl-c9on-matrix/results/results-2026-10-12` |

## Flows with misses or notable loss

- **SMT C9-off**: flow 3 (S1→S3): 150000/150000 received, 2 misses, latency 33.5 / 33.7 / 233.7 µs
- **SMT C9-on**: flow 3 (S1→S3): 150000/150000 received, 4 misses, latency 15.6 / 15.8 / 216.8 µs; flow 7 (S2→S3): 148416/150000 received, 23 misses, latency 30.6 / 76.0 / 320830.8 µs; flow 9 (S3→S2): 148421/149991 received, 50 misses, latency 38.6 / 105.6 / 320838.8 µs; flow 10 (S2→S1): 37129/37500 received, 44 misses, latency 31.0 / 293.5 / 320831.2 µs; flow 11 (S2→S3): 74208/75000 received, 11 misses, latency 30.6 / 73.9 / 320807.6 µs; flow 12 (S1→S2): 148430/150000 received, 67 misses, latency 33.4 / 100.8 / 320833.7 µs; flow 17 (S1→S2): 37130/37500 received, 46 misses, latency 30.9 / 293.8 / 320831.1 µs
- **heuristic C9-off**: no flow lost >100 frames or missed a deadline
- **heuristic C9-on**: flow 3 (S1→S3): 149992/149992 received, 1 misses, latency 12.6 / 13.0 / 200.6 µs; flow 10 (S2→S1): 37129/37499 received, 31 misses, latency 27.8 / 286.3 / 320777.1 µs; flow 17 (S1→S2): 37128/37498 received, 31 misses, latency 30.9 / 289.0 / 320739.9 µs
- **RL C9-off**: no flow lost >100 frames or missed a deadline
- **RL C9-on**: flow 9 (S3→S2): 149993/149993 received, 30 misses, latency 38.5 / 38.9 / 301.2 µs
- **Problem 3 heuristic C9-off**: no flow lost >100 frames or missed a deadline
- **Problem 3 heuristic C9-on**: no flow lost >100 frames or missed a deadline
- **Problem 3 RL C9-off**: no flow lost >100 frames or missed a deadline
- **Problem 3 RL C9-on**: no flow lost >100 frames or missed a deadline
