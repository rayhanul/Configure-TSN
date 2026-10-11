# Dataset 5 physical TSN testbed summary (2026-10-11)

All 10 original packages in `result-2026-10-10-dataset-testbed-5-avgwin` were deployed sequentially and measured for 30 seconds each on S1, S2, and S3. Every package was confirmed live on 17/17 gated switch ports, all admitted routes answered ping, and all eight switches shared one MST region. Spanning-tree stability was checked before each measurement.

Across all runs: 12,374,568 packets sent, 12,374,546 received, 22 lost, and 19 deadline misses. 7/10 packages had zero deadline misses. No switch queue drops were recorded, and every received packet used a NIC hardware timestamp.

| Package | Flows admitted / offered | Sent | Lost | Deadline misses | Average / maximum latency (µs) |
|---|---:|---:|---:|---:|---:|
| SMT C9-off | 10/20 | 824,986 | 0 | 2 | 79.08 / 471.9 |
| SMT C9-on | 10/20 | 824,984 | 5 | 15 | 37.54 / 242.2 |
| heuristic C9-off | 10/20 | 824,985 | 0 | 0 | 54.82 / 122.5 |
| heuristic C9-on | 10/20 | 824,981 | 0 | 0 | 32.64 / 62.3 |
| RL C9-off | 10/20 | 824,985 | 1 | 0 | 65.90 / 122.4 |
| RL C9-on | 10/20 | 824,976 | 1 | 0 | 34.13 / 51.7 |
| Problem 3 heuristic C9-off | 24/50 | 1,499,951 | 0 | 0 | 72.51 / 330.6 |
| Problem 3 heuristic C9-on | 28/50 | 1,874,962 | 0 | 0 | 55.75 / 277.7 |
| Problem 3 RL C9-off | 25/50 | 1,874,949 | 14 | 2 | 96.33 / 884.0 |
| Problem 3 RL C9-on | 29/50 | 2,174,809 | 1 | 0 | 47.29 / 187.3 |

Problem 3 RL C9-on carried the most flows (29), with average latency 47.29 µs, maximum latency 187.3 µs, one lost packet, and zero deadline misses. Both Problem 3 heuristic runs had zero packet loss and zero deadline misses. Problem 3 RL C9-off had 14 lost packets and two deadline misses. The SMT baselines had two (C9-off) and fifteen (C9-on) deadline misses. These are individual 30-second runs; the admitted flow sets differ between Problem 3 methods.

Latency is the receiver NIC hardware timestamp minus the scheduled NIC launch time. Lost = sent minus received; sender-skipped frames are not counted as sent or lost.

The testbed is left configured with `prob3-rl-c9-on/5-rl-c9on-matrix`, the last tested package. The traffic experiment itself has ended.

The first deployment attempt stalled because rejected SSH key attempts left unauthenticated connections open. After the user authorized stopping that attempt, its processes were stopped, connection cleanup was fixed in `Network-Configure-Manager/configureManager.py`, and the complete sweep was restarted. The fix passed a targeted rejected-key cleanup check and real switch connection checks; the successful sweep recorded no SSH banner errors. First-attempt logs are retained in `attempt-1-ssh-failure/`.

Full per-flow results and jitter: [TESTBED_RESULTS_2026-10-11.md](TESTBED_RESULTS_2026-10-11.md). Machine-readable summary: [TESTBED_SUMMARY_2026-10-11.csv](TESTBED_SUMMARY_2026-10-11.csv). Detailed deployment logs: `testbed-logs/`.
