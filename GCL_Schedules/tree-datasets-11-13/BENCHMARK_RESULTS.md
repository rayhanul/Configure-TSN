# Tree datasets 4, 5, 11–13: physical benchmark comparison

Active final package: dataset 13, Problem 3 RL C9-on, 28 scheduled flows; 17/17 operational GCLs matched the exported schedule. Final 30-second trial: 1,949,898 received of 1,949,915 sent, 17 lost, deadline misses 0 (0.00%). See [deployment-state.json](deployment-state.json).

Five distinct traffic draws (datasets 4 and 5 run 2026-10-10/11; 11–13 with seeds 47–49 run 2026-10-13), same eight-switch tree topology and hardware profile. Each dataset contains 20 initial flows and 30 additional flows. The previous scheduling pipeline was retained, including one million RL steps, C9 off/on, max overlay, three-frame minimum windows, average-size new windows, and per-instance admission.

Fifty schedule packages were deployed sequentially. Each package was checked for live GCLs, admitted with VLAN/MSTP configuration, checked for spanning-tree quiet and route connectivity, and measured with 30 seconds of traffic on all end stations.

For datasets 11–13, hardware replay passed for 30/30 packages; independent export validation passed for 18/30. The existing admission latency-report validation limitations remain; see each result directory's `validation.json` and package `independent-verification.log`. Physical measurements are single trials, not proof of deadline guarantees.

| Dataset | Package | Scheduled / offered | Sent | Received | Lost | Deadline misses (%) | Latency min / avg / max (µs) | Jitter best / avg / worst (µs) |
|---|---|---|---|---|---|---|---|---|
| 4 | SMT C9-off | 11 / 20 | 1,012,445 | 1,012,445 | 0 | 0 (0.00%) | 66.8 / 90.0 / 133.7 | 0.1 / 0.1 / 0.1 |
| 4 | SMT C9-on | 11 / 20 | 1,012,484 | 1,012,480 | 4 | 0 (0.00%) | 21.0 / 39.1 / 62.1 | 0.1 / 0.1 / 0.2 |
| 4 | heuristic C9-off | 11 / 20 | 1,012,482 | 1,012,473 | 9 | 0 (0.00%) | 19.0 / 73.7 / 134.0 | 0.1 / 0.6 / 5.7 |
| 4 | heuristic C9-on | 11 / 20 | 1,012,448 | 1,012,440 | 8 | 0 (0.00%) | 21.3 / 34.7 / 156.6 | 0.1 / 0.2 / 0.5 |
| 4 | RL C9-off | 11 / 20 | 1,012,488 | 1,012,488 | 0 | 0 (0.00%) | 19.1 / 72.0 / 133.7 | 0.1 / 1.8 / 18.7 |
| 4 | RL C9-on | 11 / 20 | 1,012,483 | 1,012,483 | 0 | 0 (0.00%) | 21.0 / 33.6 / 44.5 | 0.1 / 0.1 / 0.3 |
| 4 | Problem 3 heuristic C9-off | 24 / 50 | 1,612,431 | 1,612,423 | 8 | 0 (0.00%) | 12.8 / 82.4 / 420.7 | 0.1 / 2.5 / 49.9 |
| 4 | Problem 3 heuristic C9-on | 27 / 50 | 1,912,365 | 1,912,361 | 4 | 0 (0.00%) | 9.6 / 38.6 / 408.2 | 0.1 / 0.6 / 4.8 |
| 4 | Problem 3 RL C9-off | 28 / 50 | 2,024,967 | 2,024,967 | 0 | 0 (0.00%) | 9.7 / 67.4 / 235.5 | 0.1 / 2.6 / 25.0 |
| 4 | Problem 3 RL C9-on | 29 / 50 | 2,024,957 | 2,024,956 | 1 | 0 (0.00%) | 9.7 / 36.9 / 139.8 | 0.1 / 2.2 / 49.5 |
| 5 | SMT C9-off | 10 / 20 | 824,986 | 824,986 | 0 | 2 (0.00%) | 49.9 / 79.1 / 471.9 | 0.1 / 0.3 / 2.1 |
| 5 | SMT C9-on | 10 / 20 | 824,984 | 824,979 | 5 | 15 (0.00%) | 26.1 / 37.5 / 242.2 | 0.1 / 0.3 / 1.9 |
| 5 | heuristic C9-off | 10 / 20 | 824,985 | 824,985 | 0 | 0 (0.00%) | 19.7 / 54.8 / 122.5 | 0.1 / 0.1 / 0.2 |
| 5 | heuristic C9-on | 10 / 20 | 824,981 | 824,981 | 0 | 0 (0.00%) | 9.8 / 32.6 / 62.3 | 0.1 / 0.2 / 1.2 |
| 5 | RL C9-off | 10 / 20 | 824,985 | 824,984 | 1 | 0 (0.00%) | 19.8 / 65.9 / 122.4 | 0.1 / 3.3 / 31.6 |
| 5 | RL C9-on | 10 / 20 | 824,976 | 824,975 | 1 | 0 (0.00%) | 9.8 / 34.1 / 51.7 | 0.1 / 0.1 / 0.2 |
| 5 | Problem 3 heuristic C9-off | 24 / 50 | 1,499,951 | 1,499,951 | 0 | 0 (0.00%) | 19.8 / 72.5 / 330.6 | 0.1 / 2.4 / 36.7 |
| 5 | Problem 3 heuristic C9-on | 28 / 50 | 1,874,962 | 1,874,962 | 0 | 0 (0.00%) | 9.8 / 55.8 / 277.7 | 0.1 / 3.4 / 45.1 |
| 5 | Problem 3 RL C9-off | 25 / 50 | 1,874,949 | 1,874,935 | 14 | 2 (0.00%) | 19.8 / 96.3 / 884.0 | 0.1 / 2.9 / 31.5 |
| 5 | Problem 3 RL C9-on | 29 / 50 | 2,174,809 | 2,174,808 | 1 | 0 (0.00%) | 10.2 / 47.3 / 187.3 | 0.1 / 0.4 / 4.5 |
| 11 | SMT C9-off | 10 / 20 | 937,475 | 749,975 | 187,500 | 12 (0.00%) | 66.8 / 80.7 / 267.1 | 0.1 / 0.3 / 1.8 |
| 11 | SMT C9-on | 10 / 20 | 937,451 | 937,451 | 0 | 5 (0.00%) | 24.5 / 38.0 / 409.5 | 0.1 / 0.4 / 3.1 |
| 11 | heuristic C9-off | 10 / 20 | 937,461 | 937,461 | 0 | 0 (0.00%) | 28.0 / 61.5 / 109.2 | 0.1 / 0.1 / 0.2 |
| 11 | heuristic C9-on | 10 / 20 | 937,463 | 937,463 | 0 | 0 (0.00%) | 18.5 / 34.2 / 49.2 | 0.1 / 0.4 / 2.8 |
| 11 | RL C9-off | 10 / 20 | 937,475 | 937,475 | 0 | 0 (0.00%) | 28.4 / 70.5 / 109.6 | 0.1 / 0.1 / 0.2 |
| 11 | RL C9-on | 10 / 20 | 937,469 | 937,469 | 0 | 0 (0.00%) | 18.5 / 34.3 / 47.3 | 0.1 / 0.4 / 2.5 |
| 11 | Problem 3 heuristic C9-off | 29 / 50 | 1,912,421 | 1,912,421 | 0 | 0 (0.00%) | 17.0 / 67.1 / 571.9 | 0.1 / 1.5 / 21.2 |
| 11 | Problem 3 heuristic C9-on | 27 / 50 | 1,724,947 | 1,724,944 | 3 | 0 (0.00%) | 15.9 / 43.5 / 300.0 | 0.1 / 5.1 / 126.8 |
| 11 | Problem 3 RL C9-off | 25 / 50 | 1,687,457 | 1,687,457 | 0 | 0 (0.00%) | 28.0 / 91.5 / 308.8 | 0.1 / 1.6 / 27.8 |
| 11 | Problem 3 RL C9-on | 27 / 50 | 1,912,426 | 1,912,404 | 22 | 0 (0.00%) | 15.9 / 43.8 / 173.1 | 0.1 / 4.3 / 72.1 |
| 12 | SMT C9-off | 11 / 20 | 937,439 | 937,433 | 6 | 7 (0.00%) | 67.0 / 88.8 / 934.0 | 0.1 / 1.1 / 10.9 |
| 12 | SMT C9-on | 11 / 20 | 937,491 | 937,491 | 0 | 5 (0.00%) | 24.5 / 39.7 / 267.1 | 0.1 / 0.5 / 3.0 |
| 12 | heuristic C9-off | 11 / 20 | 937,482 | 937,482 | 0 | 0 (0.00%) | 15.9 / 55.5 / 133.9 | 0.1 / 0.3 / 1.1 |
| 12 | heuristic C9-on | 11 / 20 | 937,483 | 931,961 | 5,522 | 94 (0.01%) | 17.3 / 69.7 / 320949.9 | 0.1 / 2825.8 / 8921.5 |
| 12 | RL C9-off | 11 / 20 | 937,483 | 937,483 | 0 | 0 (0.00%) | 12.8 / 58.2 / 134.2 | 0.1 / 3.3 / 33.3 |
| 12 | RL C9-on | 11 / 20 | 937,477 | 931,941 | 5,536 | 78 (0.01%) | 17.0 / 61.0 / 320827.9 | 0.1 / 2041.2 / 8921.0 |
| 12 | Problem 3 heuristic C9-off | 34 / 50 | 2,212,455 | 2,212,455 | 0 | 0 (0.00%) | 12.1 / 49.5 / 141.7 | 0.1 / 1.1 / 17.5 |
| 12 | Problem 3 heuristic C9-on | 36 / 50 | 2,362,422 | 2,347,716 | 14,706 | 111 (0.00%) | 12.0 / 55.6 / 320971.4 | 0.1 / 1684.8 / 5454.8 |
| 12 | Problem 3 RL C9-off | 33 / 50 | 2,212,460 | 2,212,460 | 0 | 0 (0.00%) | 9.7 / 58.5 / 249.2 | 0.1 / 2.7 / 43.4 |
| 12 | Problem 3 RL C9-on | 37 / 50 | 2,587,462 | 2,570,739 | 16,723 | 128 (0.00%) | 11.0 / 55.0 / 320990.9 | 0.1 / 1584.1 / 6534.9 |
| 13 | SMT C9-off | 11 / 20 | 1,012,450 | 1,012,440 | 10 | 4 (0.00%) | 66.8 / 82.8 / 267.1 | 0.1 / 0.2 / 1.1 |
| 13 | SMT C9-on | 11 / 20 | 1,012,451 | 1,012,441 | 10 | 0 (0.00%) | 24.8 / 34.9 / 62.4 | 0.1 / 0.1 / 0.1 |
| 13 | heuristic C9-off | 11 / 20 | 1,012,487 | 1,012,487 | 0 | 0 (0.00%) | 12.8 / 46.0 / 133.8 | 0.1 / 0.6 / 4.7 |
| 13 | heuristic C9-on | 11 / 20 | 1,012,482 | 1,012,482 | 0 | 0 (0.00%) | 14.9 / 29.8 / 51.5 | 0.1 / 0.1 / 0.2 |
| 13 | RL C9-off | 11 / 20 | 1,012,484 | 1,012,484 | 0 | 0 (0.00%) | 12.8 / 52.4 / 124.1 | 0.1 / 0.1 / 0.2 |
| 13 | RL C9-on | 11 / 20 | 1,012,475 | 1,012,468 | 7 | 0 (0.00%) | 14.9 / 29.6 / 52.6 | 0.1 / 0.4 / 2.7 |
| 13 | Problem 3 heuristic C9-off | 23 / 50 | 1,574,904 | 1,574,883 | 21 | 0 (0.00%) | 12.8 / 64.1 / 313.9 | 0.1 / 2.4 / 38.8 |
| 13 | Problem 3 heuristic C9-on | 25 / 50 | 1,837,459 | 1,837,459 | 0 | 0 (0.00%) | 15.2 / 57.4 / 406.3 | 0.1 / 4.6 / 34.9 |
| 13 | Problem 3 RL C9-off | 27 / 50 | 1,987,471 | 1,987,471 | 0 | 0 (0.00%) | 12.9 / 82.3 / 239.2 | 0.1 / 2.5 / 38.8 |
| 13 | Problem 3 RL C9-on | 28 / 50 | 1,949,915 | 1,949,898 | 17 | 0 (0.00%) | 15.2 / 55.6 / 290.5 | 0.1 / 5.9 / 120.5 |

Full dataset reports:

- [Dataset 4](../result-2026-10-10-dataset-testbed-4-saf/TESTBED_RESULTS_2026-10-10.md)
- [Dataset 5](../result-2026-10-10-dataset-testbed-5-avgwin/TESTBED_RESULTS_2026-10-11.md)
- [Dataset 11](../result-2026-10-13-dataset-testbed-11-tree-avgwin/TESTBED_RESULTS_2026-10-13.md)
- [Dataset 12](../result-2026-10-13-dataset-testbed-12-tree-avgwin/TESTBED_RESULTS_2026-10-13.md)
- [Dataset 13](../result-2026-10-13-dataset-testbed-13-tree-avgwin/TESTBED_RESULTS_2026-10-13.md)
