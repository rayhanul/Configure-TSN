# Testbed results after the fixes

Only runs with all four fixes in place are listed. These are the final round of dataset 4,
2026-10-10: **all 10 packages delivered 100.00% of their frames with 0 deadline misses**.
Datasets 1-3 have no runs since the fixes (see the end).

The fixes:
**A** pcp 6 and pcp 7 share one NIC launch-time queue (`time-sync-gptp/gptp.sh`);
**B** C9-on schedules wait for store-and-forward (`store_and_forward` in RL-TSN's hw profile);
**C** etf delta 600 µs (`gptp.sh`, `Spawning-Flows/gen_traffic.py`);
**D** wait for the spanning tree to settle after admission (`Network-Configure-Manager/wait_stp_quiet.py`).

Every run: 8 TTTech switches in a tree, 3 end stations (S1, S2, S3), 1 Gb/s, 800 µs GCL cycle, 30 s
of traffic, NIC launch time on send and NIC hardware timestamps on receive. A deadline miss is a
frame whose latency exceeds its deadline (deadline = period); lost = sent but not received.

## Best results (dataset 4, ranked)

Ranked by deadline misses, then frames lost, then max latency.

| Rank | Package | Flows | Delivered | Lost | Deadline misses | Max latency | Run |
|---|---|---|---|---|---|---|---|
| 1 | RL C9-on | 11 | 100.00% | 0 | 0 | 44.5 µs | `result-2026-10-10-dataset-testbed-4-saf/rl-c9-on/4-matrix-c9on/results/results-2026-10-10_2` |
| 2 | SMT C9-off | 11 | 100.00% | 0 | 0 | 133.7 µs | `result-2026-10-09-dataset-testbed-4-avgwin/smt-c9-off/4-t3600-c9off-minlat/results/results-2026-10-10_5` |
| 2 | RL C9-off | 11 | 100.00% | 0 | 0 | 133.7 µs | `result-2026-10-09-dataset-testbed-4-avgwin/rl-c9-off/4-matrix-c9off/results/results-2026-10-10_3` |
| 4 | Problem 3 RL C9-off | 28 | 100.00% | 0 | 0 | 235.5 µs | `result-2026-10-09-dataset-testbed-4-avgwin/prob3-rl-c9-off/4-rl-c9off-matrix/results/results-2026-10-10_4` |
| 5 | Problem 3 RL C9-on | 29 | 100.00% | 1 | 0 | 139.8 µs | `result-2026-10-10-dataset-testbed-4-saf/prob3-rl-c9-on/4-rl-c9on-matrix/results/results-2026-10-10_2` |
| 6 | SMT C9-on | 11 | 100.00% | 4 | 0 | 62.1 µs | `result-2026-10-10-dataset-testbed-4-saf/smt-c9-on/4-saf-retimed-c9on/results/results-2026-10-10_3` |
| 7 | Problem 3 heuristic C9-on | 27 | 100.00% | 4 | 0 | 408.2 µs | `result-2026-10-10-dataset-testbed-4-saf/prob3-heuristic-c9-on/4-heuristic-c9on-matrix/results/results-2026-10-10_2` |
| 8 | heuristic C9-on | 11 | 100.00% | 8 | 0 | 156.6 µs | `result-2026-10-10-dataset-testbed-4-saf/heuristic-c9-on/4-matrix-c9on/results/results-2026-10-10_2` |
| 9 | Problem 3 heuristic C9-off | 24 | 100.00% | 8 | 0 | 420.7 µs | `result-2026-10-09-dataset-testbed-4-avgwin/prob3-heuristic-c9-off/4-heuristic-c9off-matrix/results/results-2026-10-10_3` |
| 10 | heuristic C9-off | 11 | 100.00% | 9 | 0 | 134.0 µs | `result-2026-10-09-dataset-testbed-4-avgwin/heuristic-c9-off/4-matrix-c9off/results/results-2026-10-10_3` |

- **Fewest misses and losses:** the four packages with 0 misses and 0 lost frames: RL C9-on, SMT
  C9-off, RL C9-off and Problem 3 RL C9-off. The largest of them, Problem 3 RL C9-off, carries 28
  flows.
- **Lowest latency:** RL C9-on (44.5 µs worst case), then SMT C9-on (62.1 µs).
- The few lost frames (34 in 13.6 million across all packages) are launch-time drops on the sending
  hosts; the switches dropped nothing.

Each run's full per-flow report is `<run>/results.md`. The causes, the earlier rounds and how each
fix changed the results: [result-2026-10-10-dataset-testbed-4-saf/SUMMARY_REPORT_2026-10-10.md](result-2026-10-10-dataset-testbed-4-saf/SUMMARY_REPORT_2026-10-10.md).

## Not run since the fixes

Datasets 1, 2 and 3. They were generated for the original cabling with loops; the testbed is now
cabled as a tree (`network-topology/network-topology-rtas-2027-tree.json`), so they need
regenerating on it before running.
