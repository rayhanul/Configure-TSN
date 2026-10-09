# Packet loss around a GCL update, 2026-10-09 12:39

Package `GCL_Schedules/dataset-testbed-2_2026-10-09/2-heuristic-c9off-matrix-25flows`, 25 flows (S1, S2, S3 running; all end stations). Update: mesh-8 (27 ports), sequential, immediate, TCP_NODELAY off, to `../GCL_Schedules/dataset-testbed-2_2026-10-09/2-heuristic-c9on-matrix/gcl`.

- Update 1 (update): first command at +10000.1 ms, network on the new lists after **2618.3 ms** (commands back after 2623.5 ms), 27/27 ports live.

| phase | from (ms) | length (ms) | sent | lost | loss % | lost/s | deadline misses | latency p50 / p99 / max (µs) |
|---|---|---|---|---|---|---|---|---|
| before | 0.0 | 10000.1 | 650016 | 7526 | 1.158 | 752.6 | 48532 | 30.8 / 296.5 / 321089.5 |
| during update 1 | 10000.1 | 2618.3 | 170181 | 0 | 0.000 | 0.0 | 11633 | 36.1 / 396.6 / 397.0 |
| after update 1 | 12618.4 | 17381.6 | 1129803 | 44 | 0.004 | 2.5 | 173804 | 43.6 / 396.6 / 397.0 |

Switch queue drops (Q DROP) during the run: sw01/p3 +20, sw01/p4 +369, sw02/p2 +790, sw02/p3 +1573, sw03/p3 +4, sw03/p4 +1, sw05/p2 +1573, sw07/p3 +1573, sw08/p4 +1569.

| flow | sent | lost | deadline misses |
|---|---|---|---|
| 1 | 150000 | 1590 | 58211 |
| 4 | 37500 | 398 | 8 |
| 6 | 37500 | 399 | 3 |
| 7 | 75000 | 776 | 32 |
| 9 | 150000 | 15 | 87824 |
| 10 | 37500 | 372 | 31 |
| 11 | 75000 | 0 | 0 |
| 12 | 37500 | 0 | 0 |
| 13 | 75000 | 5 | 0 |
| 14 | 150000 | 12 | 87812 |
| 15 | 75000 | 796 | 8 |
| 16 | 75000 | 0 | 0 |
| 18 | 150000 | 0 | 0 |
| 20 | 75000 | 5 | 0 |
| 22 | 37500 | 397 | 4 |
| 23 | 75000 | 7 | 0 |
| 26 | 75000 | 0 | 0 |
| 29 | 75000 | 795 | 14 |
| 34 | 150000 | 11 | 0 |
| 36 | 75000 | 0 | 0 |
| 37 | 37500 | 398 | 3 |
| 40 | 37500 | 400 | 3 |
| 48 | 75000 | 0 | 0 |
| 49 | 75000 | 796 | 8 |
| 50 | 37500 | 398 | 8 |
