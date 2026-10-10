# Traffic run: result-2026-10-08-dataset-testbed-2/prob3-heuristic-c9-on/2-heuristic-c9on-matrix, 2026-10-09 16:11

25 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **1499844 / 1949972 packets (76.92%)**
- Deadline misses: **4 (0.00% of received)**; flows with zero misses: 17 / 25

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 9 | 99.99% | 22.0 | 0.00% |
| S2 | 5 | 99.99% | 29.5 | 0.00% |
| S3 | 11 | 33.33% | 120.3 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7101051.924] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7102101.238] rms   35 max   90 freq  -6410 +/-  48 delay    19 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[794358.390] rms   31 max   42 freq  +3002 +/-  42 delay    46 +/-   0`
- Connectivity: 18 / 25 sender routes answered ping (failed: 11, 15, 22, 26, 36, 37, 48)

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 69 | 10 |
| S2 | 0 | 38 | 18 |
| S3 | 0 | 33 | 0 |

Switch queue drops (`ethtool -S` Q DROP) on the 27 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S1→S2 | 7 | 500 | 200.0 | 200.0 | 41.9 | 149997 | 149981 | 99.99% | 29.6 / 29.9 / 229.9 | 1.0 | 0.0 | 4 | 0.00% | 0 |
| 2 | 4 | S1→S3 | 6 | 400 | 800.0 | 800.0 | 20.8 | 37500 | 37495 | 99.99% | 9.7 / 10.1 / 27.4 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 3 | 6 | S2→S1 | 7 | 100 | 800.0 | 800.0 | 29.1 | 37500 | 37498 | 99.99% | 16.9 / 17.1 / 17.3 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 4 | 7 | S3→S1 | 7 | 300 | 400.0 | 400.0 | 20.8 | 75000 | 74999 | 100.00% | 8.5 / 8.8 / 13.0 | 0.1 | 0.1 | 0 | 0.00% | 0 |
| 5 | 9 | S1→S2 | 6 | 400 | 200.0 | 200.0 | 29.8 | 149997 | 149978 | 99.99% | 19.0 / 19.8 / 192.2 | 0.7 | 0.2 | 0 | 0.00% | 0 |
| 6 | 10 | S3→S2 | 6 | 300 | 800.0 | 800.0 | 29.1 | 37500 | 37499 | 100.00% | 16.8 / 17.1 / 17.4 | 0.1 | 0.1 | 0 | 0.00% | 0 |
| 7 | 11 | S2→S3 | 7 | 300 | 400.0 | 400.0 | 29.1 | 74995 | 0 | 0.00% | – | – | – | – | – | – |
| 8 | 12 | S2→S1 | 7 | 200 | 800.0 | 800.0 | 29.1 | 37500 | 37497 | 99.99% | 12.8 / 13.5 / 14.2 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 9 | 13 | S3→S1 | 7 | 100 | 400.0 | 400.0 | 20.8 | 75000 | 74991 | 99.99% | 5.0 / 5.4 / 5.9 | 0.1 | 0.2 | 0 | 0.00% | 0 |
| 10 | 14 | S3→S2 | 6 | 500 | 200.0 | 200.0 | 29.1 | 150000 | 149990 | 99.99% | 22.5 / 45.6 / 68.9 | 22.6 | 45.0 | 0 | 0.00% | 0 |
| 11 | 15 | S2→S3 | 6 | 400 | 400.0 | 400.0 | 29.1 | 75000 | 0 | 0.00% | – | – | – | – | – | – |
| 12 | 16 | S2→S1 | 6 | 100 | 400.0 | 400.0 | 29.1 | 74994 | 74987 | 99.99% | 16.9 / 83.8 / 150.7 | 66.7 | 133.4 | 0 | 0.00% | 0 |
| 13 | 18 | S2→S1 | 6 | 400 | 200.0 | 200.0 | 29.1 | 150000 | 149984 | 99.99% | 19.0 / 19.8 / 67.0 | 0.3 | 0.2 | 0 | 0.00% | 0 |
| 14 | 20 | S3→S2 | 6 | 300 | 400.0 | 400.0 | 29.1 | 75000 | 74999 | 100.00% | 16.7 / 22.6 / 23.1 | 0.8 | 0.4 | 0 | 0.00% | 0 |
| 15 | 22 | S2→S3 | 7 | 100 | 800.0 | 800.0 | 176.3 | 37500 | 0 | 0.00% | – | – | – | – | – | – |
| 16 | 23 | S1→S3 | 6 | 400 | 400.0 | 400.0 | 159.4 | 74999 | 74987 | 99.98% | 9.7 / 78.7 / 147.5 | 68.6 | 137.2 | 0 | 0.00% | 0 |
| 17 | 26 | S2→S3 | 7 | 200 | 400.0 | 400.0 | 139.2 | 75000 | 0 | 0.00% | – | – | – | – | – | – |
| 18 | 29 | S1→S3 | 6 | 500 | 400.0 | 400.0 | 159.7 | 74997 | 74985 | 99.98% | 11.4 / 75.0 / 138.4 | 63.2 | 126.4 | 0 | 0.00% | 0 |
| 19 | 34 | S3→S1 | 7 | 400 | 200.0 | 200.0 | 33.3 | 150000 | 149989 | 99.99% | 9.7 / 10.2 / 72.1 | 0.3 | 0.1 | 0 | 0.00% | 0 |
| 20 | 36 | S2→S3 | 6 | 100 | 400.0 | 400.0 | 283.5 | 74994 | 0 | 0.00% | – | – | – | – | – | – |
| 21 | 37 | S2→S3 | 7 | 100 | 800.0 | 800.0 | 176.6 | 37500 | 0 | 0.00% | – | – | – | – | – | – |
| 22 | 40 | S2→S1 | 7 | 100 | 800.0 | 800.0 | 71.0 | 37500 | 37499 | 100.00% | 44.9 / 45.5 / 46.3 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 23 | 48 | S2→S3 | 7 | 400 | 400.0 | 400.0 | 200.0 | 75000 | 0 | 0.00% | – | – | – | – | – | – |
| 24 | 49 | S2→S1 | 6 | 200 | 400.0 | 400.0 | 29.1 | 74999 | 74990 | 99.99% | 12.8 / 13.4 / 14.3 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 25 | 50 | S1→S3 | 7 | 300 | 800.0 | 800.0 | 416.6 | 37500 | 37496 | 99.99% | 404.1 / 404.5 / 404.9 | 0.1 | 0.2 | 0 | 0.00% | 0 |
