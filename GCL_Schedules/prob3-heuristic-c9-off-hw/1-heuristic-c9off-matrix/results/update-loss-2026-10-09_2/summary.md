# Packet loss around a GCL update, 2026-10-09 11:50

Package `GCL_Schedules/prob3-heuristic-c9-off-hw/1-heuristic-c9off-matrix`, 42 flows (S1, S2, S3 running; all end stations). Update: mesh-8 (27 ports), sequential, immediate, TCP_NODELAY off, to `../GCL_Schedules/prob3-heuristic-c9-off-hw/1-heuristic-c9off-matrix/gcl`.

- Update 1 (update): first command at +10000.1 ms, network on the new lists after **2631.5 ms** (commands back after 2634.2 ms), 27/27 ports live.

| phase | from (ms) | length (ms) | sent | lost | loss % | lost/s | deadline misses | latency p50 / p99 / max (µs) |
|---|---|---|---|---|---|---|---|---|
| before | 0.0 | 10000.1 | 1062516 | 121 | 0.011 | 12.1 | 0 | 19.8 / 598.1 / 598.4 |
| during update 1 | 10000.1 | 2631.5 | 279582 | 0 | 0.000 | 0.0 | 0 | 19.9 / 598.1 / 598.4 |
| after update 1 | 12631.6 | 17368.4 | 1845099 | 172 | 0.009 | 9.9 | 0 | 19.8 / 598.1 / 598.4 |

Switch queue drops (Q DROP) during the run: none.

| flow | sent | lost | deadline misses |
|---|---|---|---|
| 1 | 150000 | 16 | 0 |
| 3 | 150000 | 14 | 0 |
| 4 | 37500 | 0 | 0 |
| 5 | 74962 | 19 | 0 |
| 6 | 74964 | 14 | 0 |
| 7 | 37480 | 8 | 0 |
| 8 | 37479 | 8 | 0 |
| 9 | 150000 | 11 | 0 |
| 10 | 37500 | 0 | 0 |
| 11 | 37500 | 3 | 0 |
| 12 | 37482 | 10 | 0 |
| 13 | 75000 | 0 | 0 |
| 14 | 150000 | 0 | 0 |
| 15 | 74962 | 18 | 0 |
| 16 | 150000 | 14 | 0 |
| 17 | 37479 | 8 | 0 |
| 18 | 75000 | 6 | 0 |
| 19 | 75000 | 6 | 0 |
| 20 | 150000 | 19 | 0 |
| 22 | 74967 | 22 | 0 |
| 23 | 150000 | 0 | 0 |
| 25 | 37500 | 0 | 0 |
| 26 | 75000 | 7 | 0 |
| 27 | 37500 | 0 | 0 |
| 29 | 74961 | 13 | 0 |
| 30 | 75000 | 7 | 0 |
| 32 | 75000 | 0 | 0 |
| 34 | 150000 | 0 | 0 |
| 35 | 75000 | 7 | 0 |
| 36 | 37482 | 10 | 0 |
| 37 | 37500 | 4 | 0 |
| 38 | 37479 | 8 | 0 |
| 39 | 37500 | 0 | 0 |
| 40 | 37500 | 0 | 0 |
| 41 | 150000 | 15 | 0 |
| 42 | 75000 | 7 | 0 |
| 43 | 37500 | 4 | 0 |
| 45 | 75000 | 0 | 0 |
| 46 | 37500 | 4 | 0 |
| 47 | 37500 | 4 | 0 |
| 49 | 75000 | 7 | 0 |
| 50 | 75000 | 0 | 0 |
