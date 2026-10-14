# Traffic run: rerun-dataset-11-tree-rstp-settled/prob3-rl-c9-on/11-rl-c9on-matrix, 2026-10-13 16:00

27 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **1912446 / 1912453 packets (100.00%)**
- Deadline misses: **0 (0.00% of received)**; flows with zero misses: 27 / 27

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 13 | 100.00% | 41.2 | 0.00% |
| S2 | 6 | 100.00% | 38.2 | 0.00% |
| S3 | 8 | 100.00% | 55.0 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7276524.181] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7447034.069] rms    6 max    9 freq  -6389 +/-   8 delay    24 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[1139290.969] rms   31 max   46 freq  +2233 +/-  34 delay    48 +/-   0`
- Connectivity: 27 / 27 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 0 |
| S2 | 0 | 1 | 2 |
| S3 | 0 | 6 | 45 |

Switch queue drops (`ethtool -S` Q DROP) on the 17 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S1→S2 | 7 | 500 | 200.0 | 200.0 | 45.8 | 150000 | 150000 | 100.00% | 33.7 / 34.0 / 34.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 2 | 2 | S3→S2 | 7 | 400 | 200.0 | 200.0 | 58.6 | 149992 | 149991 | 100.00% | 43.5 / 43.9 / 44.3 | 0.1 | 0.1 | 0 | 0.00% | 0 |
| 3 | 3 | S1→S2 | 6 | 500 | 400.0 | 400.0 | 46.5 | 75000 | 75000 | 100.00% | 34.4 / 34.6 / 34.8 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 4 | 4 | S2→S3 | 7 | 500 | 400.0 | 400.0 | 67.2 | 75000 | 75000 | 100.00% | 42.7 / 42.9 / 43.1 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 5 | 5 | S2→S1 | 6 | 200 | 200.0 | 200.0 | 36.9 | 150000 | 149999 | 100.00% | 18.8 / 19.3 / 19.9 | 0.2 | 0.1 | 0 | 0.00% | 0 |
| 6 | 6 | S3→S1 | 7 | 200 | 200.0 | 200.0 | 136.3 | 149991 | 149989 | 100.00% | 25.4 / 62.3 / 99.1 | 35.8 | 71.6 | 0 | 0.00% | 0 |
| 7 | 7 | S2→S1 | 6 | 300 | 800.0 | 800.0 | 39.4 | 37500 | 37500 | 100.00% | 27.4 / 27.5 / 27.7 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 8 | 8 | S3→S2 | 7 | 500 | 200.0 | 200.0 | 59.3 | 149991 | 149990 | 100.00% | 28.0 / 43.5 / 47.6 | 7.6 | 4.1 | 0 | 0.00% | 0 |
| 9 | 9 | S3→S2 | 6 | 100 | 800.0 | 800.0 | 38.2 | 37497 | 37497 | 100.00% | 23.3 / 23.6 / 24.0 | 0.1 | 0.1 | 0 | 0.00% | 0 |
| 10 | 10 | S3→S1 | 7 | 300 | 400.0 | 400.0 | 66.3 | 74995 | 74994 | 100.00% | 31.6 / 32.8 / 33.9 | 0.3 | 0.3 | 0 | 0.00% | 0 |
| 11 | 12 | S2→S3 | 7 | 300 | 400.0 | 400.0 | 207.7 | 75000 | 75000 | 100.00% | 19.7 / 20.8 / 21.7 | 0.2 | 0.3 | 0 | 0.00% | 0 |
| 12 | 13 | S1→S3 | 6 | 300 | 800.0 | 800.0 | 139.2 | 37500 | 37500 | 100.00% | 115.9 / 116.7 / 117.6 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 13 | 15 | S2→S3 | 6 | 300 | 800.0 | 800.0 | 54.1 | 37500 | 37500 | 100.00% | 19.8 / 20.7 / 21.5 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 14 | 16 | S3→S1 | 7 | 500 | 400.0 | 400.0 | 125.1 | 74995 | 74994 | 100.00% | 94.0 / 94.6 / 95.3 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 15 | 18 | S2→S3 | 7 | 500 | 800.0 | 800.0 | 54.2 | 37500 | 37500 | 100.00% | 28.0 / 28.7 / 29.5 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 16 | 19 | S3→S1 | 6 | 400 | 800.0 | 800.0 | 98.9 | 37497 | 37497 | 100.00% | 86.9 / 87.1 / 87.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 17 | 20 | S1→S2 | 6 | 500 | 400.0 | 400.0 | 47.1 | 75000 | 75000 | 100.00% | 35.0 / 35.2 / 35.5 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 18 | 23 | S2→S1 | 7 | 300 | 800.0 | 800.0 | 39.4 | 37500 | 37500 | 100.00% | 27.4 / 27.5 / 27.7 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 19 | 25 | S2→S1 | 6 | 300 | 800.0 | 800.0 | 39.4 | 37500 | 37500 | 100.00% | 15.9 / 16.6 / 17.4 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 20 | 28 | S2→S1 | 7 | 400 | 800.0 | 800.0 | 191.0 | 37500 | 37500 | 100.00% | 19.1 / 19.8 / 20.6 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 21 | 35 | S2→S1 | 6 | 500 | 400.0 | 400.0 | 45.8 | 74999 | 74999 | 100.00% | 22.5 / 23.1 / 23.8 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 22 | 36 | S2→S1 | 6 | 500 | 800.0 | 800.0 | 45.8 | 37499 | 37499 | 100.00% | 22.5 / 23.1 / 23.8 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 23 | 37 | S3→S1 | 6 | 500 | 800.0 | 800.0 | 492.2 | 37497 | 37497 | 100.00% | 54.0 / 57.5 / 57.6 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 24 | 40 | S2→S3 | 6 | 500 | 400.0 | 400.0 | 215.4 | 75000 | 75000 | 100.00% | 28.0 / 101.0 / 173.4 | 72.2 | 144.4 | 0 | 0.00% | 0 |
| 25 | 42 | S2→S3 | 7 | 300 | 400.0 | 400.0 | 46.1 | 75000 | 75000 | 100.00% | 19.7 / 20.7 / 21.6 | 0.2 | 0.3 | 0 | 0.00% | 0 |
| 26 | 46 | S1→S3 | 7 | 500 | 800.0 | 800.0 | 149.8 | 37500 | 37500 | 100.00% | 122.4 / 123.1 / 124.2 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 27 | 50 | S2→S1 | 7 | 400 | 800.0 | 800.0 | 102.4 | 37500 | 37500 | 100.00% | 19.0 / 19.8 / 20.6 | 0.2 | 0.2 | 0 | 0.00% | 0 |
