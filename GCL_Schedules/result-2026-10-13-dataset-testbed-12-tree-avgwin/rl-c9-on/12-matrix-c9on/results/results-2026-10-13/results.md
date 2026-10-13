# Traffic run: result-2026-10-13-dataset-testbed-12-tree-avgwin/rl-c9-on/12-matrix-c9on, 2026-10-13 13:34

20 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **931941 / 937477 packets (99.41%)**
- Deadline misses: **78 (0.01% of received)**; flows with zero misses: 7 / 20

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 3 | 99.83% | 47.1 | 0.00% |
| S2 | 4 | 99.47% | 52.7 | 0.01% |
| S3 | 4 | 98.94% | 87.2 | 0.01% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7276524.181] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7438280.057] rms    8 max   15 freq  -6454 +/-  11 delay    24 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[1130536.961] rms   34 max   43 freq  +2324 +/-  42 delay    50 +/-   0`
- Connectivity: 11 / 11 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 4 |
| S2 | 0 | 0 | 3 |
| S3 | 0 | 0 | 16 |

Switch queue drops (`ethtool -S` Q DROP) on the 17 gated ports: sw01/p4 +1172, sw02/p4 +3970, sw07/p4 +394.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S1→S2 | None | 400 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 2 | 2 | S1→S2 | 6 | 400 | 200.0 | 200.0 | 51.0 | 150000 | 148412 | 98.94% | 38.6 / 66.7 / 320038.8 | 2984.3 | 4.3 | 13 | 0.01% | 0 |
| 3 | 3 | S3→S1 | None | 200 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 4 | 4 | S1→S3 | 6 | 300 | 800.0 | 800.0 | 66.3 | 37499 | 37098 | 98.93% | 51.1 / 51.5 / 89.4 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 5 | 5 | S3→S2 | 7 | 100 | 200.0 | 200.0 | 38.2 | 149991 | 149991 | 100.00% | 25.8 / 26.0 / 26.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 6 | 6 | S1→S3 | None | 300 | 800.0 | 800.0 | – | 0 | – | – | – | – | – | – | – | – |
| 7 | 7 | S3→S1 | 6 | 500 | 800.0 | 800.0 | 79.1 | 37497 | 37106 | 98.96% | 64.0 / 149.9 / 320827.9 | 5212.2 | 17.4 | 11 | 0.03% | 0 |
| 8 | 8 | S2→S1 | 7 | 300 | 200.0 | 200.0 | 39.4 | 149999 | 149999 | 100.00% | 27.1 / 27.3 / 27.5 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 9 | 9 | S3→S2 | 6 | 200 | 400.0 | 400.0 | 43.0 | 74996 | 74215 | 98.96% | 17.0 / 107.0 / 320817.2 | 5334.4 | 8.7 | 23 | 0.03% | 0 |
| 10 | 10 | S1→S3 | None | 500 | 200.0 | 200.0 | – | 0 | – | – | – | – | – | – | – | – |
| 11 | 11 | S2→S1 | 7 | 300 | 800.0 | 800.0 | 39.4 | 37499 | 37499 | 100.00% | 21.4 / 24.6 / 25.0 | 0.3 | 0.2 | 0 | 0.00% | 0 |
| 12 | 12 | S1→S3 | 6 | 500 | 200.0 | 200.0 | 79.1 | 149999 | 148395 | 98.93% | 54.3 / 54.5 / 110.7 | 0.2 | 0.0 | 0 | 0.00% | 0 |
| 13 | 13 | S2→S3 | None | 100 | 800.0 | 800.0 | – | 0 | – | – | – | – | – | – | – | – |
| 14 | 14 | S1→S2 | 7 | 200 | 400.0 | 400.0 | 36.9 | 74999 | 74999 | 100.00% | 24.5 / 24.7 / 24.9 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 15 | 15 | S2→S3 | None | 500 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 16 | 16 | S3→S2 | None | 400 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 17 | 17 | S1→S2 | None | 300 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 18 | 18 | S2→S3 | 6 | 300 | 800.0 | 800.0 | 54.5 | 37499 | 37129 | 99.01% | 20.6 / 279.1 / 320750.3 | 8921.0 | 17.3 | 31 | 0.08% | 0 |
| 19 | 19 | S1→S3 | 6 | 400 | 800.0 | 800.0 | 74.0 | 37499 | 37098 | 98.93% | 61.7 / 61.9 / 67.0 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 20 | 20 | S2→S3 | None | 200 | 200.0 | 200.0 | – | 0 | – | – | – | – | – | – | – | – |
