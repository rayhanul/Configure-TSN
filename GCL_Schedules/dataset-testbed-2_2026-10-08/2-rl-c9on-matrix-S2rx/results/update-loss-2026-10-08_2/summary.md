# Packet loss around a GCL update, 2026-10-08 14:14

Package `GCL_Schedules/dataset-testbed-2_2026-10-08/2-rl-c9on-matrix-S2rx`, 3 flows (S1, S2 running; skipped S3). Update: mesh-8 (27 ports), sequential, immediate, TCP_NODELAY off, to `../GCL_Schedules/dataset-testbed-2_2026-10-08/2-rl-c9off-matrix/gcl`.

- Update 1 (update): first command at +10000.1 ms, network on the new lists after **2485.7 ms** (commands back after 2490.4 ms), 27/27 ports live.
- Update 2 (restore): first command at +20000.1 ms, network on the new lists after **2531.3 ms** (commands back after 2534.9 ms), 27/27 ports live.

| phase | from (ms) | length (ms) | sent | lost | loss % | lost/s | deadline misses | latency p50 / p99 / max (µs) |
|---|---|---|---|---|---|---|---|---|
| before | 0.0 | 10000.1 | 112502 | 3 | 0.003 | 0.3 | 0 | 29.7 / 81.5 / 81.5 |
| during update 1 | 10000.1 | 2485.7 | 27963 | 0 | 0.000 | 0.0 | 1 | 93.7 / 192.2 / 254.9 |
| after update 1 | 12485.8 | 7514.3 | 84537 | 3 | 0.004 | 0.4 | 0 | 107.7 / 131.7 / 131.8 |
| during update 2 | 20000.1 | 2531.3 | 28476 | 0 | 0.000 | 0.0 | 0 | 67.0 / 131.8 / 131.8 |
| after update 2 | 22531.4 | 7468.6 | 84022 | 2 | 0.002 | 0.3 | 0 | 29.7 / 81.5 / 81.5 |

Switch queue drops (Q DROP) during the run: none.

| flow | sent | lost | deadline misses |
|---|---|---|---|
| 1 | 150000 | 4 | 0 |
| 8 | 37500 | 1 | 0 |
| 9 | 150000 | 3 | 1 |
