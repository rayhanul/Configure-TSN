# Tree datasets 11 and 12: rerun comparison

Each final package received a 30-second trial after successful connectivity checks and 60 seconds of spanning-tree quiet. Schedules, admitted flows, GCL entries and traffic settings are unchanged; their hashes are recorded in comparison.json. The physical forwarding configuration maps traffic VLANs to CIST and uses RSTP, appropriate for this connected tree. Dataset 11 was rerun in full after this final configuration was established; its earlier intermediate trials are preserved in rerun-dataset-11-tree-quiet60. A minimum 60-second hardware-settling delay was added from dataset 12 heuristic C9-off onward and applies to the final dataset 11 pass. The first two dataset 12 trials used the quiet check without that minimum elapsed delay. These settings are recorded in comparison.json. See [ROOT_CAUSE.md](ROOT_CAUSE.md).

Original and intermediate measurements are preserved. Final trials were chosen by the documented configuration pass, never by measured performance. These are single trials, not a statistical guarantee. The existing admission export latency-report validation failures remain.

| Dataset | Trial | Sent | Received | Lost | Deadline misses | Packages with zero misses |
|---|---|---|---|---|---|---|
| 11 | original | 12,862,045 | 12,674,520 | 187,525 | 17 | 8 / 10 |
| 11 | rerun | 12,862,053 | 12,862,025 | 28 | 19 | 8 / 10 |
| 12 | original | 14,999,654 | 14,957,161 | 42,493 | 423 | 4 / 10 |
| 12 | rerun | 14,999,682 | 14,999,644 | 38 | 12 | 8 / 10 |

| Dataset | Approach | Scheduled flows | Forwarding protocol | Lost: original → rerun | Misses: original → rerun | Rerun route pings | Rerun max latency (µs) |
|---|---|---|---|---|---|---|---|
| 11 | SMT C9-off | 10 | RSTP / CIST | 187,500 → 0 | 12 → 13 | 10/10 | 267.1 |
| 11 | SMT C9-on | 10 | RSTP / CIST | 0 → 0 | 5 → 6 | 10/10 | 409.5 |
| 11 | heuristic C9-off | 10 | RSTP / CIST | 0 → 16 | 0 → 0 | 10/10 | 108.9 |
| 11 | heuristic C9-on | 10 | RSTP / CIST | 0 → 2 | 0 → 0 | 10/10 | 47.4 |
| 11 | RL C9-off | 10 | RSTP / CIST | 0 → 0 | 0 → 0 | 10/10 | 109.4 |
| 11 | RL C9-on | 10 | RSTP / CIST | 0 → 1 | 0 → 0 | 10/10 | 47.3 |
| 11 | Problem 3 heuristic C9-off | 29 | RSTP / CIST | 0 → 0 | 0 → 0 | 29/29 | 571.6 |
| 11 | Problem 3 heuristic C9-on | 27 | RSTP / CIST | 3 → 0 | 0 → 0 | 27/27 | 299.9 |
| 11 | Problem 3 RL C9-off | 25 | RSTP / CIST | 0 → 2 | 0 → 0 | 25/25 | 309.1 |
| 11 | Problem 3 RL C9-on | 27 | RSTP / CIST | 22 → 7 | 0 → 0 | 27/27 | 173.4 |
| 12 | SMT C9-off | 11 | RSTP / CIST | 6 → 0 | 7 → 6 | 11/11 | 934.0 |
| 12 | SMT C9-on | 11 | RSTP / CIST | 0 → 0 | 5 → 6 | 11/11 | 267.2 |
| 12 | heuristic C9-off | 11 | RSTP / CIST | 0 → 0 | 0 → 0 | 11/11 | 133.9 |
| 12 | heuristic C9-on | 11 | RSTP / CIST | 5,522 → 0 | 94 → 0 | 11/11 | 67.2 |
| 12 | RL C9-off | 11 | RSTP / CIST | 0 → 13 | 0 → 0 | 11/11 | 134.3 |
| 12 | RL C9-on | 11 | RSTP / CIST | 5,536 → 0 | 78 → 0 | 11/11 | 64.7 |
| 12 | Problem 3 heuristic C9-off | 34 | RSTP / CIST | 0 → 1 | 0 → 0 | 34/34 | 141.8 |
| 12 | Problem 3 heuristic C9-on | 36 | RSTP / CIST | 14,706 → 3 | 111 → 0 | 36/36 | 163.8 |
| 12 | Problem 3 RL C9-off | 33 | RSTP / CIST | 0 → 0 | 0 → 0 | 33/33 | 249.0 |
| 12 | Problem 3 RL C9-on | 37 | RSTP / CIST | 16,723 → 21 | 128 → 0 | 37/37 | 181.7 |

Hardware replay passes for 20/20 final packages. Independent export verification passes for 12/20; all eight admission exports retain the documented latency-report consistency failures.

Full measurement reports:

- [Dataset 11 final confirmation](../rerun-dataset-11-tree-rstp-settled/TESTBED_RESULTS_2026-10-13.md)
- [Dataset 12 rerun](../rerun-dataset-12-tree-quiet60/TESTBED_RESULTS_2026-10-13.md)
- [Dataset 11 intermediate trials](../rerun-dataset-11-tree-quiet60/TESTBED_RESULTS_2026-10-13.md)
- [Comparison data and unchanged schedule hashes](comparison.json)

Active package: dataset 11 RL admission C9-on, 27 flows; 17/17 operational GCLs match and ports are forwarding. See [deployment-state.json](deployment-state.json).
