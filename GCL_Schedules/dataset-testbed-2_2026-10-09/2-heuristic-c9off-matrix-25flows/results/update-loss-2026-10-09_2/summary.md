# Packet loss around a GCL update, 2026-10-09 12:40

Package `GCL_Schedules/dataset-testbed-2_2026-10-09/2-heuristic-c9off-matrix-25flows`, 25 flows (S1, S2, S3 running; all end stations). Update: mesh-8 (27 ports), sequential, immediate, TCP_NODELAY off, to `../GCL_Schedules/dataset-testbed-2_2026-10-09/2-heuristic-c9on-matrix/gcl`.

- Update 1 (update): first command at +10000.1 ms, network on the new lists after **2961.8 ms** (commands back after 2965.6 ms), 27/27 ports live.

| phase | from (ms) | length (ms) | sent | lost | loss % | lost/s | deadline misses | latency p50 / p99 / max (µs) |
|---|---|---|---|---|---|---|---|---|
| before | 0.0 | 10000.1 | 650005 | 41 | 0.006 | 4.1 | 50000 | 31.0 / 296.5 / 318.9 |
| during update 1 | 10000.1 | 2961.8 | 192510 | 0 | 0.000 | 0.0 | 12381 | 36.1 / 396.6 / 397.0 |
| after update 1 | 12961.9 | 17038.1 | 1107414 | 63 | 0.006 | 3.7 | 170344 | 43.6 / 396.6 / 433.3 |

Switch queue drops (Q DROP) during the run: none.

| flow | sent | lost | deadline misses |
|---|---|---|---|
| 1 | 149993 | 8 | 60853 |
| 4 | 37496 | 1 | 0 |
| 6 | 37500 | 0 | 0 |
| 7 | 74995 | 11 | 0 |
| 9 | 149989 | 8 | 85936 |
| 10 | 37497 | 5 | 0 |
| 11 | 75000 | 0 | 0 |
| 12 | 37500 | 0 | 0 |
| 13 | 74994 | 8 | 0 |
| 14 | 149991 | 21 | 85936 |
| 15 | 75000 | 0 | 0 |
| 16 | 75000 | 0 | 0 |
| 18 | 150000 | 0 | 0 |
| 20 | 74995 | 12 | 0 |
| 22 | 37500 | 0 | 0 |
| 23 | 74997 | 4 | 0 |
| 26 | 75000 | 0 | 0 |
| 29 | 74996 | 6 | 0 |
| 34 | 149990 | 19 | 0 |
| 36 | 75000 | 0 | 0 |
| 37 | 37500 | 0 | 0 |
| 40 | 37500 | 0 | 0 |
| 48 | 75000 | 0 | 0 |
| 49 | 75000 | 0 | 0 |
| 50 | 37496 | 1 | 0 |
