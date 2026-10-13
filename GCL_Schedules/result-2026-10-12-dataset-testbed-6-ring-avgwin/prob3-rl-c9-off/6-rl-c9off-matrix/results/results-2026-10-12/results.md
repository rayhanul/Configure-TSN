# Traffic run: result-2026-10-12-dataset-testbed-6-ring-avgwin/prob3-rl-c9-off/6-rl-c9off-matrix, 2026-10-12 14:10

27 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **2099874 / 2099945 packets (100.00%)**
- Deadline misses: **1 (0.00% of received)**; flows with zero misses: 26 / 27

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 7 | 100.00% | 40.2 | 0.00% |
| S2 | 9 | 100.00% | 67.6 | 0.00% |
| S3 | 11 | 100.00% | 57.7 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7276524.181] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7354019.694] rms   25 max   65 freq  -6296 +/-  35 delay    25 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[1046276.962] rms    8 max   13 freq  +2845 +/-   9 delay    49 +/-   0`
- Connectivity: 27 / 27 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 2 | 0 |
| S2 | 0 | 0 | 0 |
| S3 | 0 | 71 | 55 |

Switch queue drops (`ethtool -S` Q DROP) on the 19 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S3→S1 | 6 | 500 | 200.0 | 200.0 | 45.8 | 149990 | 149978 | 99.99% | 33.5 / 33.7 / 33.9 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 2 | 2 | S2→S1 | 7 | 400 | 200.0 | 200.0 | 79.1 | 150000 | 150000 | 100.00% | 66.8 / 67.0 / 67.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 3 | 3 | S3→S2 | 7 | 100 | 200.0 | 200.0 | 95.7 | 149990 | 149979 | 99.99% | 42.3 / 42.8 / 43.7 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 4 | 4 | S1→S3 | 6 | 300 | 800.0 | 800.0 | 45.8 | 37500 | 37500 | 100.00% | 8.1 / 8.5 / 9.5 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 5 | 6 | S2→S1 | 6 | 100 | 400.0 | 400.0 | 83.6 | 75000 | 75000 | 100.00% | 71.3 / 71.5 / 71.6 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 6 | 7 | S2→S1 | 6 | 300 | 800.0 | 800.0 | 84.2 | 37500 | 37500 | 100.00% | 47.3 / 47.5 / 47.6 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 7 | 8 | S2→S3 | 7 | 100 | 800.0 | 800.0 | 95.7 | 37500 | 37500 | 100.00% | 39.4 / 39.6 / 39.8 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 8 | 9 | S3→S2 | 6 | 500 | 200.0 | 200.0 | 95.8 | 149991 | 149979 | 99.99% | 83.4 / 83.6 / 602.8 | 1.3 | 0.0 | 1 | 0.00% | 0 |
| 9 | 10 | S1→S3 | 6 | 100 | 800.0 | 800.0 | 611.2 | 37500 | 37500 | 100.00% | 582.3 / 582.5 / 582.7 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 10 | 11 | S3→S2 | 7 | 500 | 800.0 | 800.0 | 95.7 | 37498 | 37494 | 99.99% | 35.2 / 35.5 / 35.6 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 11 | 12 | S2→S1 | 6 | 100 | 800.0 | 800.0 | 79.1 | 37500 | 37500 | 100.00% | 24.9 / 25.1 / 25.6 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 12 | 13 | S1→S2 | 6 | 300 | 400.0 | 400.0 | 133.8 | 75000 | 75000 | 100.00% | 95.9 / 100.3 / 100.4 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 13 | 14 | S1→S2 | 7 | 100 | 200.0 | 200.0 | 79.1 | 150000 | 150000 | 100.00% | 52.4 / 52.8 / 53.4 | 0.1 | 0.1 | 0 | 0.00% | 0 |
| 14 | 15 | S2→S3 | 6 | 400 | 400.0 | 400.0 | 400.0 | 75000 | 75000 | 100.00% | 23.8 / 24.7 / 25.7 | 0.3 | 0.3 | 0 | 0.00% | 0 |
| 15 | 16 | S3→S2 | 7 | 200 | 200.0 | 200.0 | 95.7 | 149989 | 149978 | 99.99% | 83.4 / 83.6 / 83.8 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 16 | 17 | S2→S3 | 7 | 200 | 800.0 | 800.0 | 95.7 | 37500 | 37500 | 100.00% | 16.1 / 16.8 / 17.6 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 17 | 19 | S3→S1 | 7 | 500 | 400.0 | 400.0 | 46.5 | 74997 | 74990 | 99.99% | 11.5 / 11.8 / 12.2 | 0.1 | 0.2 | 0 | 0.00% | 0 |
| 18 | 20 | S3→S1 | 7 | 200 | 200.0 | 200.0 | 45.8 | 149990 | 149976 | 99.99% | 17.2 / 20.4 / 20.6 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 19 | 22 | S2→S3 | 7 | 300 | 400.0 | 400.0 | 178.9 | 75000 | 75000 | 100.00% | 20.7 / 21.4 / 22.1 | 0.5 | 0.9 | 0 | 0.00% | 0 |
| 20 | 25 | S1→S2 | 6 | 200 | 800.0 | 800.0 | 307.5 | 37500 | 37500 | 100.00% | 12.9 / 95.4 / 95.6 | 1.4 | 0.1 | 0 | 0.00% | 0 |
| 21 | 27 | S1→S3 | 7 | 400 | 800.0 | 800.0 | 45.8 | 37500 | 37500 | 100.00% | 33.5 / 33.7 / 33.9 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 22 | 32 | S1→S3 | 7 | 100 | 400.0 | 400.0 | 45.8 | 75000 | 75000 | 100.00% | 5.0 / 5.4 / 5.8 | 0.1 | 0.2 | 0 | 0.00% | 0 |
| 23 | 38 | S2→S3 | 7 | 100 | 800.0 | 800.0 | 95.7 | 37500 | 37500 | 100.00% | 33.5 / 33.7 / 33.9 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 24 | 39 | S1→S3 | 7 | 300 | 800.0 | 800.0 | 45.8 | 37500 | 37500 | 100.00% | 24.1 / 24.3 / 24.5 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 25 | 40 | S1→S2 | 6 | 200 | 800.0 | 800.0 | 212.8 | 37500 | 37500 | 100.00% | 85.7 / 90.0 / 90.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 26 | 45 | S1→S3 | 7 | 500 | 400.0 | 400.0 | 45.8 | 75000 | 75000 | 100.00% | 11.4 / 11.8 / 12.2 | 0.1 | 0.2 | 0 | 0.00% | 0 |
| 27 | 50 | S1→S2 | 7 | 100 | 400.0 | 400.0 | 79.0 | 75000 | 75000 | 100.00% | 40.7 / 41.2 / 41.7 | 0.2 | 0.2 | 0 | 0.00% | 0 |
