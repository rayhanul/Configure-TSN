# Packet loss around a GCL update, 2026-10-09 11:51

Package `GCL_Schedules/prob3-heuristic-c9-off-hw/1-heuristic-c9off-matrix`, 42 flows (S1, S2, S3 running; all end stations). Update: mesh-8 (27 ports), sequential, immediate, TCP_NODELAY off, to `../GCL_Schedules/prob3-heuristic-c9-off-hw/1-heuristic-c9off-matrix/gcl`.

- Update 1 (update): first command at +10000.6 ms, network on the new lists after **2743.3 ms** (commands back after 2746.7 ms), 27/27 ports live.

| phase | from (ms) | length (ms) | sent | lost | loss % | lost/s | deadline misses | latency p50 / p99 / max (µs) |
|---|---|---|---|---|---|---|---|---|
| before | 0.0 | 10000.6 | 1062428 | 100 | 0.009 | 10.0 | 0 | 19.8 / 598.1 / 598.4 |
| during update 1 | 10000.6 | 2743.3 | 291472 | 0 | 0.000 | 0.0 | 0 | 19.8 / 598.1 / 598.4 |
| after update 1 | 12744.0 | 17256.0 | 1833471 | 119 | 0.006 | 6.9 | 1 | 19.8 / 598.1 / 598.4 |

Switch queue drops (Q DROP) during the run: none.

| flow | sent | lost | deadline misses |
|---|---|---|---|
| 1 | 150000 | 11 | 1 |
| 3 | 150000 | 13 | 0 |
| 4 | 37500 | 0 | 0 |
| 5 | 74984 | 11 | 0 |
| 6 | 74988 | 8 | 0 |
| 7 | 37491 | 5 | 0 |
| 8 | 37491 | 5 | 0 |
| 9 | 150000 | 12 | 0 |
| 10 | 37500 | 0 | 0 |
| 11 | 37500 | 0 | 0 |
| 12 | 37494 | 5 | 0 |
| 13 | 75000 | 0 | 0 |
| 14 | 150000 | 0 | 0 |
| 15 | 74982 | 11 | 0 |
| 16 | 150000 | 13 | 0 |
| 17 | 37490 | 5 | 0 |
| 18 | 75000 | 11 | 0 |
| 19 | 75000 | 10 | 0 |
| 20 | 150000 | 12 | 0 |
| 22 | 74986 | 13 | 0 |
| 23 | 150000 | 0 | 0 |
| 25 | 37500 | 0 | 0 |
| 26 | 75000 | 11 | 0 |
| 27 | 37500 | 0 | 0 |
| 29 | 74985 | 8 | 0 |
| 30 | 75000 | 5 | 0 |
| 32 | 75000 | 0 | 0 |
| 34 | 150000 | 0 | 0 |
| 35 | 75000 | 11 | 0 |
| 36 | 37491 | 5 | 0 |
| 37 | 37500 | 0 | 0 |
| 38 | 37489 | 5 | 0 |
| 39 | 37500 | 0 | 0 |
| 40 | 37500 | 0 | 0 |
| 41 | 150000 | 13 | 0 |
| 42 | 75000 | 11 | 0 |
| 43 | 37500 | 0 | 0 |
| 45 | 75000 | 0 | 0 |
| 46 | 37500 | 0 | 0 |
| 47 | 37500 | 0 | 0 |
| 49 | 75000 | 5 | 0 |
| 50 | 75000 | 0 | 0 |
