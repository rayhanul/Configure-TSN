# Traffic run: dataset-testbed-2_2026-10-08/2-rl-c9on-matrix-S2rx, 2026-10-08 10:05

32 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **1537444 / 1537500 packets (100.00%)**
- Deadline misses: **74994 (4.88% of received)**; flows with zero misses: 17 / 32

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 2 | 99.99% | 57.1 | 0.00% |
| S2 | 10 | 99.99% | 63.1 | 8.70% |
| S3 | 6 | 100.00% | 45.6 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[6992545.937] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[6993733.920] rms   25 max   67 freq  -6291 +/-  34 delay    19 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[686039.259] rms    7 max   13 freq  +2838 +/-   7 delay    48 +/-   0`
- Connectivity: 18 / 18 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 0 |
| S2 | 0 | 0 | 0 |
| S3 | 0 | 60 | 0 |

Switch queue drops (`ethtool -S` Q DROP) on the 27 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S1→S2 | 7 | 500 | 200.0 | 200.0 | 41.9 | 150000 | 150000 | 100.00% | 29.6 / 29.8 / 30.0 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 2 | 2 | S3→S2 | 6 | 100 | 800.0 | 800.0 | 43.5 | 37500 | 37497 | 99.99% | 9.7 / 10.3 / 329.6 | 1.7 | 0.2 | 0 | 0.00% | 0 |
| 3 | 4 | S1→S3 | 6 | 400 | 800.0 | 800.0 | 20.8 | 37500 | 37500 | 100.00% | 9.7 / 10.1 / 10.6 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 4 | 6 | S2→S1 | 7 | 100 | 800.0 | 800.0 | 29.1 | 0 | – | – | – | – | – | – | – | – |
| 5 | 7 | S3→S1 | 7 | 300 | 400.0 | 400.0 | 20.8 | 75000 | 74994 | 99.99% | 8.5 / 8.8 / 28.4 | 0.1 | 0.1 | 0 | 0.00% | 0 |
| 6 | 8 | S1→S2 | 6 | 500 | 800.0 | 800.0 | 146.2 | 37500 | 37500 | 100.00% | 81.2 / 81.4 / 81.6 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 7 | 9 | S1→S2 | 6 | 400 | 200.0 | 200.0 | 29.8 | 150000 | 150000 | 100.00% | 19.0 / 19.8 / 21.9 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 8 | 10 | S3→S2 | 6 | 300 | 800.0 | 800.0 | 29.1 | 37500 | 37497 | 99.99% | 16.8 / 17.1 / 17.4 | 0.1 | 0.1 | 0 | 0.00% | 0 |
| 9 | 11 | S2→S3 | 7 | 300 | 400.0 | 400.0 | 29.1 | 0 | – | – | – | – | – | – | – | – |
| 10 | 12 | S2→S1 | 7 | 200 | 800.0 | 800.0 | 29.1 | 0 | – | – | – | – | – | – | – | – |
| 11 | 13 | S3→S1 | 7 | 100 | 400.0 | 400.0 | 133.8 | 75000 | 74995 | 99.99% | 90.5 / 105.4 / 120.4 | 14.6 | 29.1 | 0 | 0.00% | 0 |
| 12 | 14 | S3→S2 | 6 | 500 | 200.0 | 200.0 | 29.1 | 150000 | 149987 | 99.99% | 42.7 / 145.7 / 222.2 | 75.8 | 151.6 | 74994 | 50.00% | 0 |
| 13 | 15 | S2→S3 | 6 | 400 | 400.0 | 400.0 | 52.2 | 0 | – | – | – | – | – | – | – | – |
| 14 | 16 | S2→S1 | 6 | 100 | 400.0 | 400.0 | 29.1 | 0 | – | – | – | – | – | – | – | – |
| 15 | 17 | S3→S2 | 7 | 200 | 200.0 | 200.0 | 105.9 | 150000 | 149988 | 99.99% | 93.6 / 93.8 / 94.0 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 16 | 18 | S2→S1 | 6 | 400 | 200.0 | 200.0 | 29.1 | 0 | – | – | – | – | – | – | – | – |
| 17 | 19 | S2→S1 | 7 | 100 | 200.0 | 200.0 | 45.8 | 0 | – | – | – | – | – | – | – | – |
| 18 | 20 | S3→S2 | 6 | 300 | 400.0 | 400.0 | 29.1 | 75000 | 74993 | 99.99% | 17.0 / 24.2 / 24.8 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 19 | 22 | S2→S3 | 6 | 100 | 800.0 | 800.0 | 39.7 | 0 | – | – | – | – | – | – | – | – |
| 20 | 23 | S1→S3 | 6 | 400 | 400.0 | 400.0 | 20.8 | 75000 | 75000 | 100.00% | 9.7 / 10.1 / 11.2 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 21 | 24 | S3→S2 | 6 | 200 | 800.0 | 800.0 | 68.5 | 37500 | 37496 | 99.99% | 13.8 / 55.5 / 56.6 | 6.0 | 1.5 | 0 | 0.00% | 0 |
| 22 | 26 | S2→S3 | 7 | 200 | 400.0 | 400.0 | 92.2 | 0 | – | – | – | – | – | – | – | – |
| 23 | 29 | S1→S3 | 6 | 500 | 400.0 | 400.0 | 52.2 | 75000 | 75000 | 100.00% | 11.4 / 13.5 / 15.4 | 1.7 | 3.4 | 0 | 0.00% | 0 |
| 24 | 30 | S1→S3 | 6 | 300 | 200.0 | 200.0 | 32.6 | 150000 | 150000 | 100.00% | 8.1 / 9.0 / 11.1 | 0.8 | 0.9 | 0 | 0.00% | 0 |
| 25 | 35 | S3→S2 | 7 | 400 | 800.0 | 800.0 | 138.6 | 37500 | 37497 | 99.99% | 82.0 / 82.2 / 82.4 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 26 | 36 | S2→S3 | 7 | 100 | 400.0 | 400.0 | 92.2 | 0 | – | – | – | – | – | – | – | – |
| 27 | 37 | S2→S3 | 7 | 100 | 800.0 | 800.0 | 275.2 | 0 | – | – | – | – | – | – | – | – |
| 28 | 40 | S2→S1 | 6 | 100 | 800.0 | 800.0 | 29.1 | 0 | – | – | – | – | – | – | – | – |
| 29 | 42 | S1→S3 | 6 | 500 | 200.0 | 200.0 | 32.6 | 150000 | 150000 | 100.00% | 11.4 / 11.8 / 12.4 | 0.1 | 0.1 | 0 | 0.00% | 0 |
| 30 | 48 | S2→S3 | 7 | 400 | 400.0 | 400.0 | 42.9 | 0 | – | – | – | – | – | – | – | – |
| 31 | 49 | S2→S1 | 7 | 200 | 400.0 | 400.0 | 52.8 | 0 | – | – | – | – | – | – | – | – |
| 32 | 50 | S1→S3 | 7 | 300 | 800.0 | 800.0 | 510.1 | 37500 | 37500 | 100.00% | 497.8 / 498.1 / 498.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
