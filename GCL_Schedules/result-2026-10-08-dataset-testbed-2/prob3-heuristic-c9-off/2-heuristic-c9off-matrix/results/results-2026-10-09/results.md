# Traffic run: result-2026-10-08-dataset-testbed-2/prob3-heuristic-c9-off/2-heuristic-c9off-matrix, 2026-10-09 15:57

22 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **452677 / 1649990 packets (27.44%)**
- Deadline misses: **2527 (0.56% of received)**; flows with zero misses: 5 / 22

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 8 | 66.86% | 2566.9 | 0.26% |
| S2 | 5 | 0.28% | 1179588.8 | 97.71% |
| S3 | 9 | 14.29% | 29.0 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7101051.924] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7101246.396] rms   28 max   68 freq  -6400 +/-  39 delay    19 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[793503.799] rms   40 max   71 freq  +2937 +/-  49 delay    43 +/-   0`
- Connectivity: 15 / 22 sender routes answered ping (failed: 11, 15, 22, 26, 36, 37, 48)

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 0 |
| S2 | 0 | 34 | 10 |
| S3 | 0 | 31 | 0 |

Switch queue drops (`ethtool -S` Q DROP) on the 27 gated ports: sw08/p2 +560893, sw08/p5 +186346.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S1→S2 | 7 | 500 | 200.0 | 200.0 | 79.0 | 150000 | 462 | 0.31% | 166.4 / 816884.7 / 999737.7 | 378732.5 | 128370.3 | 440 | 95.24% | 0 |
| 2 | 4 | S1→S3 | 6 | 400 | 800.0 | 800.0 | 45.8 | 37500 | 37500 | 100.00% | 33.5 / 33.7 / 33.9 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 3 | 6 | S2→S1 | 6 | 100 | 800.0 | 800.0 | 79.0 | 37500 | 216 | 0.58% | 118.5 / 836854.6 / 998721.3 | 359183.3 | 275099.2 | 186 | 86.11% | 0 |
| 4 | 7 | S3→S1 | 6 | 300 | 400.0 | 400.0 | 45.8 | 75000 | 74994 | 99.99% | 36.1 / 75.6 / 75.8 | 0.2 | 0.0 | 0 | 0.00% | 0 |
| 5 | 9 | S1→S2 | 7 | 400 | 200.0 | 200.0 | 79.7 | 150000 | 446 | 0.30% | 145.6 / 845737.9 / 999716.9 | 352917.1 | 132985.3 | 439 | 98.43% | 0 |
| 6 | 10 | S3→S2 | 6 | 300 | 800.0 | 800.0 | 79.0 | 37500 | 93 | 0.25% | 224475.5 / 2056789.6 / 2998279.7 | 507169.6 | 301985.3 | 93 | 100.00% | 0 |
| 7 | 11 | S2→S3 | 7 | 300 | 400.0 | 400.0 | 83.5 | 74995 | 0 | 0.00% | – | – | – | – | – | – |
| 8 | 12 | S2→S1 | 6 | 200 | 800.0 | 800.0 | 79.0 | 37500 | 246 | 0.66% | 54.3 / 856036.2 / 998732.3 | 340505.1 | 241435.3 | 216 | 87.80% | 0 |
| 9 | 13 | S3→S1 | 7 | 100 | 400.0 | 400.0 | 233.9 | 75000 | 74994 | 99.99% | 190.0 / 190.4 / 195.3 | 0.1 | 0.2 | 0 | 0.00% | 0 |
| 10 | 14 | S3→S2 | 6 | 500 | 200.0 | 200.0 | 91.8 | 150000 | 348 | 0.23% | 224157.1 / 2089986.5 / 2998350.4 | 542721.5 | 167662.2 | 348 | 100.00% | 0 |
| 11 | 15 | S2→S3 | 6 | 400 | 400.0 | 400.0 | 333.4 | 75000 | 0 | 0.00% | – | – | – | – | – | – |
| 12 | 16 | S2→S1 | 7 | 100 | 400.0 | 400.0 | 79.0 | 74997 | 74992 | 99.99% | 21.6 / 25.0 / 256.5 | 4.6 | 0.2 | 0 | 0.00% | 0 |
| 13 | 18 | S2→S1 | 7 | 400 | 200.0 | 200.0 | 83.5 | 150000 | 149984 | 99.99% | 59.2 / 65.6 / 303.1 | 6.8 | 11.9 | 30 | 0.02% | 0 |
| 14 | 20 | S3→S2 | 7 | 300 | 400.0 | 400.0 | 79.0 | 75000 | 223 | 0.30% | 124.0 / 812183.9 / 999520.9 | 382980.8 | 266521.7 | 216 | 96.86% | 0 |
| 15 | 22 | S2→S3 | 6 | 100 | 800.0 | 800.0 | 375.0 | 37500 | 0 | 0.00% | – | – | – | – | – | – |
| 16 | 26 | S2→S3 | 7 | 200 | 400.0 | 400.0 | 79.0 | 74998 | 0 | 0.00% | – | – | – | – | – | – |
| 17 | 36 | S2→S3 | 7 | 100 | 400.0 | 400.0 | 129.0 | 75000 | 0 | 0.00% | – | – | – | – | – | – |
| 18 | 37 | S2→S3 | 6 | 100 | 800.0 | 800.0 | 290.6 | 37500 | 0 | 0.00% | – | – | – | – | – | – |
| 19 | 40 | S2→S1 | 6 | 100 | 800.0 | 800.0 | 145.3 | 37500 | 216 | 0.58% | 107.0 / 836842.9 / 998709.4 | 359183.1 | 275099.1 | 186 | 86.11% | 0 |
| 20 | 48 | S2→S3 | 7 | 400 | 400.0 | 400.0 | 132.8 | 75000 | 0 | 0.00% | – | – | – | – | – | – |
| 21 | 49 | S2→S1 | 6 | 200 | 400.0 | 400.0 | 281.0 | 75000 | 463 | 0.62% | 75.0 / 781117.2 / 998679.7 | 404227.6 | 128024.3 | 373 | 80.56% | 0 |
| 22 | 50 | S1→S3 | 6 | 300 | 800.0 | 800.0 | 255.4 | 37500 | 37500 | 100.00% | 24.1 / 24.3 / 24.5 | 0.1 | 0.0 | 0 | 0.00% | 0 |
