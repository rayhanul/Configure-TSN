# Traffic run: result-2026-10-09-dataset-testbed-4-avgwin/prob3-heuristic-c9-off/4-heuristic-c9off-matrix, 2026-10-10 16:54

24 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **1612416 / 1612485 packets (100.00%)**
- Deadline misses: **0 (0.00% of received)**; flows with zero misses: 24 / 24

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 8 | 100.00% | 88.7 | 0.00% |
| S2 | 10 | 99.99% | 65.5 | 0.00% |
| S3 | 6 | 100.00% | 103.4 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7173666.135] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7191090.380] rms   25 max   68 freq  -6192 +/-  35 delay    21 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[883347.283] rms   42 max   94 freq  +3195 +/-  58 delay    48 +/-   0`
- Connectivity: 24 / 24 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 41 | 15 |
| S2 | 0 | 1 | 0 |
| S3 | 0 | 28 | 0 |

Switch queue drops (`ethtool -S` Q DROP) on the 17 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S3→S2 | 7 | 300 | 400.0 | 400.0 | 95.8 | 75000 | 74995 | 99.99% | 83.4 / 83.6 / 83.8 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 2 | 2 | S1→S2 | 7 | 300 | 400.0 | 400.0 | 312.3 | 74999 | 74993 | 99.99% | 200.2 / 250.3 / 301.3 | 49.9 | 99.8 | 0 | 0.00% | 0 |
| 3 | 3 | S2→S3 | 7 | 100 | 400.0 | 400.0 | 95.8 | 75000 | 75000 | 100.00% | 83.4 / 83.6 / 83.9 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 4 | 4 | S3→S2 | 6 | 400 | 800.0 | 800.0 | 95.7 | 37500 | 37497 | 99.99% | 23.8 / 24.7 / 59.3 | 0.3 | 0.2 | 0 | 0.00% | 0 |
| 5 | 6 | S1→S3 | 6 | 300 | 800.0 | 800.0 | 145.7 | 37498 | 37496 | 99.99% | 133.4 / 133.6 / 133.8 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 6 | 8 | S2→S3 | 6 | 500 | 200.0 | 200.0 | 95.8 | 150000 | 150000 | 100.00% | 83.4 / 83.6 / 83.9 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 7 | 9 | S1→S3 | 6 | 400 | 800.0 | 800.0 | 145.7 | 37498 | 37496 | 99.99% | 111.0 / 111.2 / 111.4 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 8 | 10 | S3→S2 | 7 | 400 | 400.0 | 400.0 | 95.8 | 75000 | 74996 | 99.99% | 58.7 / 61.2 / 320.4 | 1.0 | 0.0 | 0 | 0.00% | 0 |
| 9 | 11 | S2→S1 | 7 | 200 | 800.0 | 800.0 | 533.4 | 37500 | 37500 | 100.00% | 12.8 / 13.5 / 14.2 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 10 | 13 | S1→S2 | 6 | 400 | 200.0 | 200.0 | 79.1 | 149997 | 149989 | 99.99% | 19.1 / 23.1 / 67.0 | 5.7 | 6.6 | 0 | 0.00% | 0 |
| 11 | 14 | S3→S2 | 6 | 500 | 200.0 | 200.0 | 95.8 | 150000 | 149990 | 99.99% | 28.0 / 28.7 / 37.1 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 12 | 18 | S2→S1 | 6 | 300 | 800.0 | 800.0 | 79.1 | 37500 | 37500 | 100.00% | 41.1 / 41.8 / 42.4 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 13 | 19 | S2→S3 | 7 | 500 | 400.0 | 400.0 | 95.8 | 75000 | 75000 | 100.00% | 83.4 / 83.6 / 83.9 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 14 | 20 | S1→S3 | 6 | 100 | 200.0 | 200.0 | 145.7 | 149998 | 149990 | 99.99% | 133.4 / 133.6 / 133.8 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 15 | 21 | S2→S1 | 6 | 400 | 800.0 | 800.0 | 79.0 | 37500 | 37500 | 100.00% | 32.5 / 33.1 / 33.7 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 16 | 22 | S2→S1 | 7 | 300 | 800.0 | 800.0 | 512.3 | 37500 | 37499 | 100.00% | 411.8 / 412.5 / 420.1 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 17 | 23 | S2→S1 | 6 | 300 | 800.0 | 800.0 | 79.0 | 37500 | 37500 | 100.00% | 23.0 / 23.7 / 24.3 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 18 | 24 | S3→S1 | 7 | 300 | 800.0 | 800.0 | 233.0 | 37500 | 37497 | 99.99% | 99.8 / 102.9 / 110.0 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 19 | 29 | S1→S2 | 6 | 100 | 400.0 | 400.0 | 141.4 | 74998 | 74994 | 99.99% | 20.4 / 21.8 / 177.3 | 1.5 | 2.6 | 0 | 0.00% | 0 |
| 20 | 30 | S1→S2 | 6 | 500 | 400.0 | 400.0 | 83.5 | 74998 | 74994 | 99.99% | 42.8 / 43.2 / 43.6 | 0.1 | 0.2 | 0 | 0.00% | 0 |
| 21 | 42 | S1→S2 | 7 | 200 | 800.0 | 800.0 | 233.0 | 37500 | 37497 | 99.99% | 187.7 / 190.2 / 190.4 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 22 | 45 | S3→S1 | 6 | 500 | 800.0 | 800.0 | 145.6 | 37500 | 37497 | 99.99% | 63.3 / 64.0 / 67.3 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 23 | 48 | S1→S2 | 6 | 300 | 800.0 | 800.0 | 141.4 | 37499 | 37496 | 99.99% | 33.2 / 33.4 / 35.8 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 24 | 50 | S2→S1 | 7 | 300 | 800.0 | 800.0 | 129.0 | 37500 | 37500 | 100.00% | 16.4 / 18.3 / 25.2 | 0.2 | 0.2 | 0 | 0.00% | 0 |
