# Packet loss around a GCL update, 2026-10-08 14:15

Package `GCL_Schedules/dataset-testbed-2_2026-10-08/2-rl-c9on-matrix-S2rx`, 3 flows (S1, S2 running; skipped S3). Update: mesh-8 (27 ports), batched, immediate, TCP_NODELAY on, to `../GCL_Schedules/dataset-testbed-2_2026-10-08/2-rl-c9off-matrix/gcl`.

- Update 1 (update): first command at +10000.3 ms, network on the new lists after **313.8 ms** (commands back after 317.9 ms), 27/27 ports live.
- Update 2 (restore): first command at +20000.2 ms, network on the new lists after **313.1 ms** (commands back after 318.1 ms), 27/27 ports live.

| phase | from (ms) | length (ms) | sent | lost | loss % | lost/s | deadline misses | latency p50 / p99 / max (µs) |
|---|---|---|---|---|---|---|---|---|
| before | 0.0 | 10000.3 | 112503 | 4 | 0.004 | 0.4 | 0 | 29.7 / 81.5 / 81.6 |
| during update 1 | 10000.3 | 313.8 | 3529 | 0 | 0.000 | 0.0 | 493 | 107.8 / 267.1 / 267.1 |
| after update 1 | 10314.1 | 9686.1 | 108970 | 4 | 0.004 | 0.4 | 0 | 107.8 / 131.8 / 131.8 |
| during update 2 | 20000.2 | 313.1 | 3521 | 0 | 0.000 | 0.0 | 188 | 81.4 / 306.4 / 306.5 |
| after update 2 | 20313.3 | 9686.7 | 108977 | 2 | 0.002 | 0.2 | 0 | 29.7 / 81.5 / 155.4 |

Switch queue drops (Q DROP) during the run: none.

| flow | sent | lost | deadline misses |
|---|---|---|---|
| 1 | 150000 | 5 | 680 |
| 8 | 37500 | 2 | 0 |
| 9 | 150000 | 3 | 1 |
