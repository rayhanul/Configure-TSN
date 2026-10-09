# Packet loss around a GCL update, 2026-10-09 12:41

Package `GCL_Schedules/dataset-testbed-2_2026-10-09/2-heuristic-c9off-matrix-25flows`, 25 flows (S1, S2, S3 running; all end stations). Update: mesh-8 (27 ports), sequential, immediate, TCP_NODELAY off, to `../GCL_Schedules/dataset-testbed-2_2026-10-09/2-heuristic-c9on-matrix/gcl`.

- Update 1 (update): first command at +10000.1 ms, network on the new lists after **2612.6 ms** (commands back after 2615.0 ms), 27/27 ports live.

| phase | from (ms) | length (ms) | sent | lost | loss % | lost/s | deadline misses | latency p50 / p99 / max (µs) |
|---|---|---|---|---|---|---|---|---|
| before | 0.0 | 10000.1 | 650005 | 0 | 0.000 | 0.0 | 50000 | 31.0 / 296.5 / 296.9 |
| during update 1 | 10000.1 | 2612.6 | 169812 | 6 | 0.004 | 2.3 | 11433 | 36.2 / 396.6 / 397.0 |
| after update 1 | 12612.8 | 17387.2 | 1130183 | 36 | 0.003 | 2.1 | 173864 | 43.5 / 396.6 / 397.0 |

Switch queue drops (Q DROP) during the run: none.

| flow | sent | lost | deadline misses |
|---|---|---|---|
| 1 | 150000 | 0 | 59777 |
| 4 | 37500 | 0 | 0 |
| 6 | 37500 | 0 | 0 |
| 7 | 75000 | 5 | 0 |
| 9 | 150000 | 0 | 87765 |
| 10 | 37500 | 2 | 0 |
| 11 | 75000 | 1 | 0 |
| 12 | 37500 | 0 | 0 |
| 13 | 75000 | 5 | 0 |
| 14 | 150000 | 10 | 87755 |
| 15 | 75000 | 0 | 0 |
| 16 | 75000 | 1 | 0 |
| 18 | 150000 | 1 | 0 |
| 20 | 75000 | 5 | 0 |
| 22 | 37500 | 0 | 0 |
| 23 | 75000 | 0 | 0 |
| 26 | 75000 | 1 | 0 |
| 29 | 75000 | 0 | 0 |
| 34 | 150000 | 9 | 0 |
| 36 | 75000 | 1 | 0 |
| 37 | 37500 | 0 | 0 |
| 40 | 37500 | 0 | 0 |
| 48 | 75000 | 1 | 0 |
| 49 | 75000 | 0 | 0 |
| 50 | 37500 | 0 | 0 |
