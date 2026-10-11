# Packet loss around a GCL update, 2026-10-11 01:22

Package `GCL_Schedules/result-2026-10-10-dataset-testbed-5-avgwin/prob3-rl-c9-on/5-rl-c9on-matrix`, 29 flows (S1, S2, S3 running; all end stations). Update: dataset-5-affected (17 ports), sequential, immediate, TCP_NODELAY off, to `GCL_Schedules/result-2026-10-10-dataset-testbed-5-avgwin/prob3-heuristic-c9-on/5-heuristic-c9on-matrix/gcl`.

- Update 1 (update): first command at +10078.4 ms, network on the new lists after **1573.8 ms** (commands back after 1578.8 ms), 17/17 ports live.

| phase | from (ms) | length (ms) | sent | lost | loss % | lost/s | deadline misses | latency p50 / p99 / max (µs) |
|---|---|---|---|---|---|---|---|---|
| before | 0.0 | 10078.4 | 730558 | 0 | 0.000 | 0.0 | 0 | 39.7 / 186.7 / 187.3 |
| during update 1 | 10078.4 | 1573.8 | 114095 | 0 | 0.000 | 0.0 | 8338 | 50.5 / 443.6 / 461.4 |
| after update 1 | 11652.2 | 18347.8 | 1330203 | 4 | 0.000 | 0.2 | 91738 | 68.9 / 443.7 / 443.8 |

Switch queue drops (Q DROP) during the run: none.

| flow | sent | lost | deadline misses |
|---|---|---|---|
| 1 | 37496 | 0 | 0 |
| 2 | 150000 | 0 | 0 |
| 3 | 37497 | 0 | 0 |
| 4 | 37493 | 0 | 0 |
| 5 | 37499 | 0 | 0 |
| 6 | 75000 | 0 | 0 |
| 7 | 74994 | 0 | 49363 |
| 8 | 149987 | 1 | 50713 |
| 9 | 74998 | 0 | 0 |
| 10 | 149977 | 0 | 0 |
| 11 | 75000 | 0 | 0 |
| 12 | 149988 | 1 | 0 |
| 13 | 37495 | 0 | 0 |
| 14 | 149980 | 0 | 0 |
| 15 | 150000 | 0 | 0 |
| 16 | 37495 | 0 | 0 |
| 17 | 74994 | 0 | 0 |
| 18 | 74993 | 0 | 0 |
| 19 | 74994 | 0 | 0 |
| 22 | 37496 | 0 | 0 |
| 28 | 37495 | 0 | 0 |
| 30 | 37500 | 0 | 0 |
| 31 | 37496 | 1 | 0 |
| 37 | 37499 | 0 | 0 |
| 38 | 150000 | 0 | 0 |
| 39 | 75000 | 0 | 0 |
| 43 | 37496 | 1 | 0 |
| 45 | 37494 | 0 | 0 |
| 50 | 37500 | 0 | 0 |
