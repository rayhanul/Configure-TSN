# Packet loss around a GCL update, 2026-10-08 14:13

Package `GCL_Schedules/dataset-testbed-2_2026-10-08/2-rl-c9on-matrix-S2rx`, 3 flows (S1, S2 running; skipped S3). Update: mesh-8 (27 ports), sequential, immediate, TCP_NODELAY off, to each port’s own current list.

- Update 1 (update): first command at +10000.1 ms, network on the new lists after **2370.3 ms** (commands back after 2373.1 ms), 27/27 ports live.

| phase | from (ms) | length (ms) | sent | lost | loss % | lost/s | deadline misses | latency p50 / p99 / max (µs) |
|---|---|---|---|---|---|---|---|---|
| before | 0.0 | 10000.1 | 112502 | 0 | 0.000 | 0.0 | 0 | 29.7 / 81.5 / 81.5 |
| during update 1 | 10000.1 | 2370.3 | 26664 | 2 | 0.008 | 0.8 | 0 | 29.7 / 81.5 / 81.5 |
| after update 1 | 12370.4 | 17629.6 | 198334 | 4 | 0.002 | 0.2 | 0 | 29.7 / 81.5 / 81.5 |

Switch queue drops (Q DROP) during the run: none.

| flow | sent | lost | deadline misses |
|---|---|---|---|
| 1 | 150000 | 3 | 0 |
| 8 | 37500 | 1 | 0 |
| 9 | 150000 | 2 | 0 |
