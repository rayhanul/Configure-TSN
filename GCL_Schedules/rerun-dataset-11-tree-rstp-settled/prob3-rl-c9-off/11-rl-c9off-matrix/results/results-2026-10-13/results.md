# Traffic run: rerun-dataset-11-tree-rstp-settled/prob3-rl-c9-off/11-rl-c9off-matrix, 2026-10-13 15:57

25 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **1687408 / 1687410 packets (100.00%)**
- Deadline misses: **0 (0.00% of received)**; flows with zero misses: 25 / 25

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 12 | 100.00% | 102.7 | 0.00% |
| S2 | 7 | 100.00% | 74.6 | 0.00% |
| S3 | 6 | 100.00% | 107.7 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7276524.181] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7446862.805] rms    9 max   20 freq  -6386 +/-  12 delay    23 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[1139120.461] rms   51 max  103 freq  +2246 +/-  69 delay    50 +/-   0`
- Connectivity: 25 / 25 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 52 |
| S2 | 0 | 0 | 0 |
| S3 | 0 | 2 | 38 |

Switch queue drops (`ethtool -S` Q DROP) on the 17 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S1→S2 | 6 | 500 | 200.0 | 200.0 | 79.1 | 149986 | 149986 | 100.00% | 67.0 / 67.2 / 70.6 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 2 | 2 | S3→S2 | 6 | 400 | 200.0 | 200.0 | 95.8 | 149991 | 149991 | 100.00% | 67.2 / 71.4 / 71.6 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 3 | 3 | S1→S2 | 7 | 500 | 400.0 | 400.0 | 83.6 | 74992 | 74992 | 100.00% | 71.5 / 71.7 / 71.9 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 4 | 4 | S2→S3 | 6 | 500 | 400.0 | 400.0 | 108.2 | 75000 | 75000 | 100.00% | 28.0 / 28.7 / 30.2 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 5 | 5 | S2→S1 | 7 | 200 | 200.0 | 200.0 | 79.1 | 150000 | 150000 | 100.00% | 53.5 / 53.9 / 54.3 | 0.1 | 0.1 | 0 | 0.00% | 0 |
| 6 | 7 | S2→S1 | 7 | 300 | 800.0 | 800.0 | 79.1 | 37500 | 37500 | 100.00% | 28.7 / 29.4 / 30.1 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 7 | 8 | S3→S2 | 6 | 500 | 200.0 | 200.0 | 96.4 | 149991 | 149991 | 100.00% | 84.3 / 84.5 / 84.7 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 8 | 9 | S3→S2 | 7 | 100 | 800.0 | 800.0 | 95.8 | 37498 | 37498 | 100.00% | 83.7 / 83.9 / 84.1 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 9 | 10 | S3→S1 | 7 | 300 | 400.0 | 400.0 | 145.7 | 74996 | 74995 | 100.00% | 108.0 / 108.6 / 109.1 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 10 | 12 | S2→S3 | 6 | 300 | 400.0 | 400.0 | 126.4 | 75000 | 75000 | 100.00% | 58.7 / 86.8 / 114.9 | 27.8 | 55.7 | 0 | 0.00% | 0 |
| 11 | 13 | S1→S3 | 7 | 300 | 800.0 | 800.0 | 366.4 | 37496 | 37496 | 100.00% | 308.6 / 308.9 / 309.1 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 12 | 15 | S2→S3 | 6 | 300 | 800.0 | 800.0 | 134.1 | 37500 | 37500 | 100.00% | 80.7 / 88.5 / 89.0 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 13 | 16 | S3→S1 | 7 | 500 | 400.0 | 400.0 | 193.0 | 74995 | 74995 | 100.00% | 180.9 / 181.1 / 181.3 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 14 | 17 | S1→S2 | 6 | 400 | 400.0 | 400.0 | 109.8 | 74991 | 74991 | 100.00% | 97.7 / 97.9 / 98.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 15 | 18 | S2→S3 | 7 | 500 | 800.0 | 800.0 | 95.8 | 37500 | 37500 | 100.00% | 83.7 / 83.9 / 84.1 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 16 | 19 | S3→S1 | 7 | 400 | 800.0 | 800.0 | 380.2 | 37496 | 37496 | 100.00% | 172.3 / 172.5 / 172.7 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 17 | 20 | S1→S2 | 7 | 500 | 400.0 | 400.0 | 84.2 | 74990 | 74990 | 100.00% | 46.8 / 50.9 / 51.1 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 18 | 23 | S2→S1 | 6 | 300 | 800.0 | 800.0 | 115.8 | 37500 | 37500 | 100.00% | 103.8 / 104.0 / 104.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 19 | 25 | S2→S1 | 6 | 300 | 800.0 | 800.0 | 175.7 | 37500 | 37500 | 100.00% | 84.7 / 85.1 / 88.8 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 20 | 28 | S2→S1 | 7 | 400 | 800.0 | 800.0 | 79.0 | 37500 | 37500 | 100.00% | 54.3 / 61.9 / 62.1 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 21 | 36 | S2→S1 | 6 | 500 | 800.0 | 800.0 | 183.0 | 37500 | 37500 | 100.00% | 171.0 / 171.2 / 171.4 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 22 | 37 | S3→S1 | 6 | 500 | 800.0 | 800.0 | 145.6 | 37498 | 37498 | 100.00% | 133.6 / 133.8 / 134.0 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 23 | 39 | S3→S1 | 6 | 500 | 400.0 | 400.0 | 216.0 | 74997 | 74996 | 100.00% | 112.8 / 121.6 / 132.8 | 8.6 | 17.2 | 0 | 0.00% | 0 |
| 24 | 46 | S1→S3 | 6 | 500 | 800.0 | 800.0 | 233.3 | 37493 | 37493 | 100.00% | 149.1 / 149.6 / 150.1 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 25 | 50 | S2→S1 | 7 | 400 | 800.0 | 800.0 | 79.0 | 37500 | 37500 | 100.00% | 44.9 / 52.5 / 52.7 | 0.1 | 0.0 | 0 | 0.00% | 0 |
