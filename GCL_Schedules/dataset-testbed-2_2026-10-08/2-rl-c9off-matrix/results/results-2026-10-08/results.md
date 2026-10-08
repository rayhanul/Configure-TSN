# Traffic run: dataset-testbed-2_2026-10-08/2-rl-c9off-matrix, 2026-10-08 01:11

26 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **1912467 / 1912500 packets (100.00%)**
- Deadline misses: **37499 (1.96% of received)**; flows with zero misses: 25 / 26

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 9 | 100.00% | 63.4 | 5.26% |
| S2 | 11 | 100.00% | 75.9 | 0.00% |
| S3 | 6 | 100.00% | 81.4 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[6915791.454] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[6961688.474] rms   12 max   18 freq  -6819 +/-  15 delay    17 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[653993.185] rms    6 max   10 freq  +3196 +/-   7 delay    50 +/-   0`
- Connectivity: 26 / 26 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 0 |
| S2 | 0 | 3 | 0 |
| S3 | 0 | 30 | 0 |

Switch queue drops (`ethtool -S` Q DROP) on the 27 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S1→S2 | 7 | 500 | 200.0 | 200.0 | 79.0 | 150000 | 150000 | 100.00% | 66.8 / 67.0 / 67.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 2 | 2 | S3→S2 | 6 | 100 | 800.0 | 800.0 | 93.4 | 37500 | 37498 | 99.99% | 56.5 / 56.7 / 56.9 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 3 | 3 | S1→S2 | 6 | 500 | 200.0 | 200.0 | 156.2 | 150000 | 150000 | 100.00% | 129.5 / 141.3 / 144.3 | 4.9 | 5.6 | 0 | 0.00% | 0 |
| 4 | 4 | S1→S3 | 6 | 400 | 800.0 | 800.0 | 45.8 | 37500 | 37500 | 100.00% | 33.5 / 33.7 / 33.9 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 5 | 6 | S2→S1 | 6 | 100 | 800.0 | 800.0 | 150.1 | 37500 | 37500 | 100.00% | 44.2 / 44.4 / 44.6 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 6 | 7 | S3→S1 | 6 | 300 | 400.0 | 400.0 | 45.8 | 75000 | 74995 | 99.99% | 79.2 / 79.6 / 80.1 | 0.1 | 0.2 | 0 | 0.00% | 0 |
| 7 | 8 | S1→S2 | 6 | 500 | 800.0 | 800.0 | 144.0 | 37500 | 37500 | 100.00% | 123.1 / 123.3 / 123.5 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 8 | 9 | S1→S2 | 7 | 400 | 200.0 | 200.0 | 79.7 | 150000 | 150000 | 100.00% | 46.0 / 46.2 / 46.4 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 9 | 10 | S3→S2 | 6 | 300 | 800.0 | 800.0 | 79.0 | 37500 | 37498 | 99.99% | 66.8 / 67.0 / 67.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 10 | 11 | S2→S3 | 7 | 300 | 400.0 | 400.0 | 83.5 | 75000 | 74999 | 100.00% | 43.8 / 44.4 / 45.0 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 11 | 12 | S2→S1 | 6 | 200 | 800.0 | 800.0 | 79.0 | 37500 | 37500 | 100.00% | 55.2 / 55.5 / 55.7 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 12 | 13 | S3→S1 | 7 | 100 | 400.0 | 400.0 | 137.9 | 75000 | 74995 | 99.99% | 33.8 / 34.0 / 34.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 13 | 14 | S3→S2 | 6 | 500 | 200.0 | 200.0 | 91.8 | 150000 | 149989 | 99.99% | 79.6 / 79.8 / 80.0 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 14 | 15 | S2→S3 | 6 | 400 | 400.0 | 400.0 | 84.8 | 75000 | 74999 | 100.00% | 72.5 / 74.0 / 75.5 | 1.3 | 2.6 | 0 | 0.00% | 0 |
| 15 | 16 | S2→S1 | 7 | 100 | 400.0 | 400.0 | 79.0 | 75000 | 75000 | 100.00% | 66.8 / 67.0 / 67.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 16 | 18 | S2→S1 | 7 | 400 | 200.0 | 200.0 | 83.5 | 150000 | 150000 | 100.00% | 59.2 / 66.0 / 72.6 | 6.4 | 12.8 | 0 | 0.00% | 0 |
| 17 | 19 | S2→S1 | 6 | 100 | 200.0 | 200.0 | 84.2 | 150000 | 150000 | 100.00% | 13.1 / 95.7 / 213.4 | 77.3 | 138.8 | 37499 | 25.00% | 0 |
| 18 | 20 | S3→S2 | 7 | 300 | 400.0 | 400.0 | 79.0 | 75000 | 74995 | 99.99% | 42.4 / 42.6 / 42.8 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 19 | 21 | S1→S2 | 6 | 400 | 800.0 | 800.0 | 94.7 | 37500 | 37500 | 100.00% | 65.2 / 65.4 / 65.6 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 20 | 22 | S2→S3 | 6 | 100 | 800.0 | 800.0 | 79.0 | 37500 | 37500 | 100.00% | 13.2 / 13.4 / 13.6 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 21 | 28 | S1→S2 | 6 | 200 | 800.0 | 800.0 | 96.3 | 37500 | 37500 | 100.00% | 55.7 / 55.9 / 56.1 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 22 | 37 | S2→S3 | 7 | 100 | 800.0 | 800.0 | 400.0 | 37500 | 37500 | 100.00% | 306.8 / 307.0 / 307.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 23 | 40 | S2→S1 | 6 | 100 | 800.0 | 800.0 | 82.2 | 37500 | 37500 | 100.00% | 11.3 / 13.0 / 13.6 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 24 | 41 | S1→S2 | 7 | 500 | 800.0 | 800.0 | 163.5 | 37500 | 37500 | 100.00% | 30.3 / 32.7 / 32.9 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 25 | 49 | S2→S1 | 6 | 200 | 400.0 | 400.0 | 79.7 | 75000 | 74999 | 100.00% | 41.8 / 42.0 / 42.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 26 | 50 | S1→S3 | 6 | 300 | 800.0 | 800.0 | 85.1 | 37500 | 37500 | 100.00% | 60.1 / 60.3 / 60.5 | 0.1 | 0.0 | 0 | 0.00% | 0 |
