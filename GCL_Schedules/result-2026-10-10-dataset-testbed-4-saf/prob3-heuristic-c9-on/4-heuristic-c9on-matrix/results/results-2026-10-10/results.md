# Traffic run: result-2026-10-10-dataset-testbed-4-saf/prob3-heuristic-c9-on/4-heuristic-c9on-matrix, 2026-10-10 15:40

27 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **1912445 / 1912497 packets (100.00%)**
- Deadline misses: **0 (0.00% of received)**; flows with zero misses: 27 / 27

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 10 | 100.00% | 59.8 | 0.00% |
| S2 | 11 | 100.00% | 28.5 | 0.00% |
| S3 | 6 | 100.00% | 38.7 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7173666.135] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7186660.768] rms    6 max   10 freq  -6218 +/-   8 delay    22 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[878917.673] rms   26 max   45 freq  +3175 +/-  35 delay    49 +/-   0`
- Connectivity: 27 / 27 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 0 |
| S2 | 0 | 3 | 0 |
| S3 | 0 | 49 | 0 |

Switch queue drops (`ethtool -S` Q DROP) on the 17 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S3→S2 | 7 | 300 | 400.0 | 400.0 | 46.2 | 75000 | 74996 | 99.99% | 33.8 / 34.0 / 34.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 2 | 2 | S1→S2 | 6 | 300 | 400.0 | 400.0 | 39.4 | 75000 | 75000 | 100.00% | 15.8 / 16.6 / 17.5 | 0.2 | 0.3 | 0 | 0.00% | 0 |
| 3 | 3 | S2→S3 | 7 | 100 | 400.0 | 400.0 | 42.0 | 75000 | 74999 | 100.00% | 21.0 / 21.2 / 21.4 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 4 | 4 | S3→S2 | 7 | 400 | 800.0 | 800.0 | 207.7 | 37500 | 37496 | 99.99% | 23.7 / 24.7 / 26.8 | 0.3 | 0.2 | 0 | 0.00% | 0 |
| 5 | 5 | S3→S1 | 6 | 200 | 400.0 | 400.0 | 65.6 | 75000 | 74994 | 99.99% | 32.4 / 36.8 / 40.6 | 3.7 | 7.3 | 0 | 0.00% | 0 |
| 6 | 6 | S1→S3 | 6 | 300 | 800.0 | 800.0 | 67.0 | 37499 | 37499 | 100.00% | 39.8 / 40.8 / 41.7 | 0.3 | 0.2 | 0 | 0.00% | 0 |
| 7 | 8 | S2→S3 | 7 | 500 | 200.0 | 200.0 | 54.2 | 150000 | 149999 | 100.00% | 41.8 / 42.0 / 42.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 8 | 9 | S1→S3 | 7 | 400 | 800.0 | 800.0 | 74.0 | 37500 | 37500 | 100.00% | 61.6 / 61.9 / 62.1 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 9 | 10 | S3→S2 | 6 | 400 | 400.0 | 400.0 | 51.0 | 74999 | 74994 | 99.99% | 38.6 / 38.8 / 42.8 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 10 | 11 | S2→S1 | 6 | 200 | 800.0 | 800.0 | 36.8 | 37500 | 37500 | 100.00% | 12.8 / 13.5 / 14.2 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 11 | 13 | S1→S2 | 6 | 400 | 200.0 | 200.0 | 43.3 | 150000 | 150000 | 100.00% | 21.8 / 22.6 / 37.1 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 12 | 14 | S3→S2 | 6 | 500 | 200.0 | 200.0 | 56.1 | 150000 | 149989 | 99.99% | 30.9 / 31.6 / 88.6 | 0.3 | 0.2 | 0 | 0.00% | 0 |
| 13 | 15 | S3→S2 | 7 | 300 | 200.0 | 200.0 | 46.1 | 150000 | 149989 | 99.99% | 19.8 / 28.9 / 45.9 | 4.8 | 6.1 | 0 | 0.00% | 0 |
| 14 | 18 | S2→S1 | 6 | 300 | 800.0 | 800.0 | 39.4 | 37500 | 37500 | 100.00% | 27.1 / 27.3 / 27.5 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 15 | 19 | S2→S3 | 6 | 500 | 400.0 | 400.0 | 54.2 | 74999 | 74999 | 100.00% | 28.0 / 28.7 / 30.4 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 16 | 20 | S1→S3 | 6 | 100 | 200.0 | 200.0 | 54.8 | 150000 | 150000 | 100.00% | 42.4 / 42.7 / 42.9 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 17 | 21 | S2→S1 | 6 | 400 | 800.0 | 800.0 | 47.0 | 37500 | 37500 | 100.00% | 19.1 / 21.4 / 26.9 | 2.8 | 2.0 | 0 | 0.00% | 0 |
| 18 | 22 | S2→S1 | 6 | 300 | 800.0 | 800.0 | 47.0 | 37500 | 37500 | 100.00% | 16.5 / 20.6 / 21.5 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 19 | 23 | S2→S1 | 6 | 300 | 800.0 | 800.0 | 40.6 | 37500 | 37499 | 100.00% | 15.9 / 16.6 / 17.4 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 20 | 24 | S3→S1 | 7 | 300 | 800.0 | 800.0 | 420.2 | 37500 | 37499 | 100.00% | 399.3 / 400.0 / 408.1 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 21 | 29 | S1→S2 | 6 | 100 | 400.0 | 400.0 | 39.4 | 75000 | 75000 | 100.00% | 9.7 / 10.3 / 11.0 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 22 | 30 | S1→S2 | 6 | 500 | 400.0 | 400.0 | 45.8 | 75000 | 75000 | 100.00% | 22.4 / 23.1 / 23.8 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 23 | 35 | S3→S1 | 6 | 400 | 400.0 | 400.0 | 161.6 | 75000 | 74995 | 99.99% | 38.0 / 39.9 / 54.6 | 0.7 | 1.4 | 0 | 0.00% | 0 |
| 24 | 42 | S1→S2 | 7 | 200 | 800.0 | 800.0 | 693.8 | 37500 | 37500 | 100.00% | 91.7 / 91.9 / 92.1 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 25 | 45 | S3→S1 | 6 | 500 | 800.0 | 800.0 | 111.4 | 37500 | 37498 | 99.99% | 44.7 / 48.1 / 62.9 | 1.5 | 1.2 | 0 | 0.00% | 0 |
| 26 | 48 | S1→S2 | 6 | 300 | 800.0 | 800.0 | 39.4 | 37500 | 37500 | 100.00% | 15.9 / 16.6 / 17.4 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 27 | 50 | S2→S1 | 7 | 300 | 800.0 | 800.0 | 500.2 | 37500 | 37500 | 100.00% | 15.9 / 16.6 / 17.5 | 0.2 | 0.2 | 0 | 0.00% | 0 |
