# Ring datasets 7–10: physical benchmark comparison

Final live configuration: **dataset 10, Problem 3 RL C9-on, 38 scheduled flows**, cycle 800,000 ns. All 19 operational GCLs were read back after the benchmarks and matched the package. Final trial: 2,699,833 / 2,699,834 packets delivered, zero deadline misses.

Four distinct traffic draws (seeds 43–46), same eight-switch ring topology and hardware profile. Each dataset contains 20 initial flows and 30 additional flows. The previous scheduling pipeline was retained, including one million RL steps, C9 off/on, max overlay, three-frame minimum windows, average-size new windows, and per-instance admission.

Forty schedule packages were deployed sequentially. Each package was checked for live GCLs, admitted with VLAN/MSTP configuration, checked for spanning-tree quiet and route connectivity, and measured with 30 seconds of traffic on all end stations.

The existing admission latency-report validation limitations remain; see each result directory's `validation.json` and package `independent-verification.log`. Physical measurements are single trials, not proof of deadline guarantees.

| Dataset | Package | Scheduled / offered | Sent | Received | Lost | Deadline misses (%) | Latency min / avg / max (µs) | Jitter best / avg / worst (µs) |
|---|---|---|---|---|---|---|---|---|
| 7 | SMT C9-off | 11 / 20 | 1,012,475 | 1,012,475 | 0 | 0 (0.00%) | 33.5 / 60.7 / 83.8 | 0.1 / 0.1 / 0.1 |
| 7 | SMT C9-on | 11 / 20 | 1,012,469 | 1,005,015 | 7,454 | 224 (0.02%) | 10.5 / 73.1 / 320842.1 | 0.1 / 3540.3 / 9066.0 |
| 7 | heuristic C9-off | 11 / 20 | 1,012,468 | 1,012,468 | 0 | 0 (0.00%) | 22.0 / 49.2 / 67.2 | 0.1 / 0.1 / 0.2 |
| 7 | heuristic C9-on | 11 / 20 | 1,012,461 | 1,012,455 | 6 | 0 (0.00%) | 10.5 / 23.3 / 42.3 | 0.1 / 0.4 / 3.6 |
| 7 | RL C9-off | 11 / 20 | 1,012,477 | 1,012,477 | 0 | 0 (0.00%) | 21.5 / 49.0 / 67.5 | 0.1 / 0.7 / 6.3 |
| 7 | RL C9-on | 11 / 20 | 1,012,422 | 1,012,422 | 0 | 0 (0.00%) | 5.0 / 22.5 / 42.5 | 0.1 / 0.6 / 3.6 |
| 7 | Problem 3 heuristic C9-off | 29 / 50 | 2,174,724 | 2,174,724 | 0 | 0 (0.00%) | 6.6 / 45.2 / 336.5 | 0.1 / 3.8 / 72.1 |
| 7 | Problem 3 heuristic C9-on | 29 / 50 | 2,062,457 | 2,062,457 | 0 | 0 (0.00%) | 5.0 / 24.6 / 293.6 | 0.1 / 0.3 / 3.6 |
| 7 | Problem 3 RL C9-off | 28 / 50 | 1,912,453 | 1,912,453 | 0 | 0 (0.00%) | 5.0 / 45.8 / 131.4 | 0.1 / 2.0 / 15.6 |
| 7 | Problem 3 RL C9-on | 31 / 50 | 2,174,813 | 2,174,788 | 25 | 1 (0.00%) | 5.0 / 27.1 / 296.3 | 0.1 / 0.6 / 6.2 |
| 8 | SMT C9-off | 10 / 20 | 862,487 | 862,487 | 0 | 6 (0.00%) | 33.5 / 53.7 / 833.7 | 0.1 / 1.1 / 10.1 |
| 8 | SMT C9-on | 10 / 20 | 862,498 | 862,498 | 0 | 4 (0.00%) | 9.3 / 22.6 / 385.6 | 0.1 / 0.3 / 1.4 |
| 8 | heuristic C9-off | 10 / 20 | 862,489 | 862,489 | 0 | 0 (0.00%) | 5.1 / 27.1 / 67.5 | 0.1 / 0.1 / 0.2 |
| 8 | heuristic C9-on | 10 / 20 | 862,491 | 862,491 | 0 | 0 (0.00%) | 5.0 / 19.9 / 40.1 | 0.1 / 0.1 / 0.2 |
| 8 | RL C9-off | 10 / 20 | 862,489 | 862,489 | 0 | 0 (0.00%) | 8.1 / 30.6 / 67.2 | 0.1 / 0.1 / 0.2 |
| 8 | RL C9-on | 10 / 20 | 862,485 | 862,115 | 370 | 31 (0.00%) | 5.0 / 30.9 / 320743.7 | 0.1 / 892.6 / 8925.2 |
| 8 | Problem 3 heuristic C9-off | 33 / 50 | 2,099,904 | 2,099,904 | 0 | 0 (0.00%) | 5.1 / 30.2 / 307.5 | 0.1 / 0.4 / 6.9 |
| 8 | Problem 3 heuristic C9-on | 39 / 50 | 2,849,863 | 2,842,766 | 7,097 | 121 (0.00%) | 5.0 / 33.0 / 320830.8 | 0.1 / 1218.0 / 5078.3 |
| 8 | Problem 3 RL C9-off | 34 / 50 | 2,324,942 | 2,324,940 | 2 | 0 (0.00%) | 8.1 / 47.9 / 296.3 | 0.1 / 2.8 / 44.5 |
| 8 | Problem 3 RL C9-on | 38 / 50 | 2,699,163 | 2,693,260 | 5,903 | 121 (0.00%) | 5.0 / 54.7 / 320825.7 | 0.1 / 1185.9 / 8513.8 |
| 9 | SMT C9-off | 11 / 20 | 862,439 | 862,427 | 12 | 6 (0.00%) | 33.4 / 54.6 / 233.7 | 0.1 / 0.2 / 1.3 |
| 9 | SMT C9-on | 11 / 20 | 862,484 | 857,793 | 4,691 | 175 (0.02%) | 12.4 / 68.5 / 320841.9 | 0.1 / 3508.0 / 9089.4 |
| 9 | heuristic C9-off | 11 / 20 | 862,479 | 862,479 | 0 | 0 (0.00%) | 9.7 / 35.0 / 73.0 | 0.1 / 0.6 / 5.1 |
| 9 | heuristic C9-on | 11 / 20 | 862,478 | 862,472 | 6 | 0 (0.00%) | 9.7 / 18.7 / 42.2 | 0.1 / 0.6 / 2.3 |
| 9 | RL C9-off | 11 / 20 | 862,492 | 862,492 | 0 | 0 (0.00%) | 9.7 / 36.9 / 73.0 | 0.1 / 0.1 / 0.2 |
| 9 | RL C9-on | 11 / 20 | 862,442 | 862,432 | 10 | 0 (0.00%) | 9.7 / 19.1 / 42.2 | 0.1 / 0.3 / 2.1 |
| 9 | Problem 3 heuristic C9-off | 35 / 50 | 2,287,385 | 2,287,372 | 13 | 1 (0.00%) | 5.0 / 39.5 / 268.0 | 0.1 / 3.9 / 46.6 |
| 9 | Problem 3 heuristic C9-on | 37 / 50 | 2,362,386 | 2,362,383 | 3 | 0 (0.00%) | 6.6 / 29.1 / 316.1 | 0.1 / 3.3 / 74.7 |
| 9 | Problem 3 RL C9-off | 33 / 50 | 2,287,326 | 2,287,325 | 1 | 0 (0.00%) | 6.6 / 36.8 / 159.4 | 0.1 / 2.8 / 51.9 |
| 9 | Problem 3 RL C9-on | 37 / 50 | 2,512,414 | 2,504,512 | 7,902 | 126 (0.01%) | 6.6 / 55.1 / 320818.3 | 0.1 / 1345.4 / 5454.4 |
| 10 | SMT C9-off | 11 / 20 | 1,012,478 | 1,012,478 | 0 | 2 (0.00%) | 33.5 / 62.3 / 233.7 | 0.1 / 0.2 / 0.8 |
| 10 | SMT C9-on | 11 / 20 | 1,012,482 | 1,006,223 | 6,259 | 245 (0.02%) | 13.7 / 75.4 / 320838.8 | 0.1 / 3161.7 / 9028.7 |
| 10 | heuristic C9-off | 11 / 20 | 1,012,480 | 1,012,480 | 0 | 0 (0.00%) | 9.7 / 43.9 / 71.9 | 0.1 / 1.4 / 8.8 |
| 10 | heuristic C9-on | 11 / 20 | 1,012,449 | 1,011,704 | 745 | 63 (0.01%) | 8.1 / 43.7 / 320777.1 | 0.1 / 1622.9 / 8927.4 |
| 10 | RL C9-off | 11 / 20 | 1,012,489 | 1,012,489 | 0 | 0 (0.00%) | 9.7 / 43.0 / 71.9 | 0.1 / 1.0 / 9.3 |
| 10 | RL C9-on | 11 / 20 | 1,012,481 | 1,012,481 | 0 | 30 (0.00%) | 8.1 / 24.6 / 301.2 | 0.1 / 0.5 / 3.8 |
| 10 | Problem 3 heuristic C9-off | 34 / 50 | 2,249,881 | 2,249,875 | 6 | 0 (0.00%) | 5.0 / 68.9 / 410.9 | 0.1 / 7.3 / 87.9 |
| 10 | Problem 3 heuristic C9-on | 33 / 50 | 2,174,946 | 2,174,946 | 0 | 0 (0.00%) | 5.0 / 35.8 / 206.0 | 0.1 / 1.6 / 44.9 |
| 10 | Problem 3 RL C9-off | 32 / 50 | 2,249,926 | 2,249,925 | 1 | 0 (0.00%) | 7.0 / 52.0 / 214.4 | 0.1 / 4.7 / 65.0 |
| 10 | Problem 3 RL C9-on | 38 / 50 | 2,699,834 | 2,699,833 | 1 | 0 (0.00%) | 5.0 / 36.7 / 263.0 | 0.1 / 2.5 / 53.8 |

Full dataset reports:

- [Dataset 7](../result-2026-10-12-dataset-testbed-7-ring-avgwin/TESTBED_RESULTS_2026-10-12.md)
- [Dataset 8](../result-2026-10-12-dataset-testbed-8-ring-avgwin/TESTBED_RESULTS_2026-10-12.md)
- [Dataset 9](../result-2026-10-12-dataset-testbed-9-ring-avgwin/TESTBED_RESULTS_2026-10-12.md)
- [Dataset 10](../result-2026-10-12-dataset-testbed-10-ring-avgwin/TESTBED_RESULTS_2026-10-12.md)
