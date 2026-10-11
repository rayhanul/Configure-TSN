# Packet loss around a GCL update, 2026-10-11 01:23

Package `GCL_Schedules/result-2026-10-10-dataset-testbed-5-avgwin/prob3-rl-c9-on/5-rl-c9on-matrix`, 29 flows (S1, S2, S3 running; all end stations). Update: dataset-5-affected (17 ports), sequential, immediate, TCP_NODELAY off, to `GCL_Schedules/result-2026-10-10-dataset-testbed-5-avgwin/prob3-heuristic-c9-on/5-heuristic-c9on-matrix/gcl`.

- Update 1 (update): first command at +10070.8 ms, network on the new lists after **1694.8 ms** (commands back after 1698.6 ms), 17/17 ports live.

| phase | from (ms) | length (ms) | sent | lost | loss % | lost/s | deadline misses | latency p50 / p99 / max (µs) |
|---|---|---|---|---|---|---|---|---|
| before | 0.0 | 10070.8 | 730140 | 0 | 0.000 | 0.0 | 0 | 40.7 / 186.7 / 187.2 |
| during update 1 | 10070.8 | 1694.8 | 122863 | 0 | 0.000 | 0.0 | 9021 | 53.3 / 443.7 / 450.2 |
| after update 1 | 11765.6 | 18234.4 | 1321955 | 0 | 0.000 | 0.0 | 91164 | 65.4 / 443.7 / 443.8 |

Switch queue drops (Q DROP) during the run: none.

| flow | sent | lost | deadline misses |
|---|---|---|---|
| 1 | 37498 | 0 | 0 |
| 2 | 150000 | 0 | 0 |
| 3 | 37500 | 0 | 0 |
| 4 | 37500 | 0 | 0 |
| 5 | 37500 | 0 | 0 |
| 6 | 75000 | 0 | 0 |
| 7 | 74996 | 0 | 49342 |
| 8 | 149991 | 0 | 50843 |
| 9 | 75000 | 0 | 0 |
| 10 | 150000 | 0 | 0 |
| 11 | 74999 | 0 | 0 |
| 12 | 149991 | 0 | 0 |
| 13 | 37500 | 0 | 0 |
| 14 | 150000 | 0 | 0 |
| 15 | 150000 | 0 | 0 |
| 16 | 37498 | 0 | 0 |
| 17 | 75000 | 0 | 0 |
| 18 | 75000 | 0 | 0 |
| 19 | 74996 | 0 | 0 |
| 22 | 37498 | 0 | 0 |
| 28 | 37500 | 0 | 0 |
| 30 | 37499 | 0 | 0 |
| 31 | 37497 | 0 | 0 |
| 37 | 37500 | 0 | 0 |
| 38 | 149999 | 0 | 0 |
| 39 | 74999 | 0 | 0 |
| 43 | 37497 | 0 | 0 |
| 45 | 37500 | 0 | 0 |
| 50 | 37500 | 0 | 0 |
