# Traffic run: result-2026-10-12-dataset-testbed-6-ring-avgwin/prob3-rl-c9-on/6-rl-c9on-matrix, 2026-10-12 14:18

27 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **2024946 / 2024948 packets (100.00%)**
- Deadline misses: **1 (0.00% of received)**; flows with zero misses: 26 / 27

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 7 | 100.00% | 18.0 | 0.00% |
| S2 | 9 | 100.00% | 37.4 | 0.00% |
| S3 | 11 | 100.00% | 58.0 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7276524.181] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7354505.562] rms   11 max   20 freq  -6289 +/-  14 delay    24 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[1046762.957] rms   22 max   61 freq  +2874 +/-  30 delay    49 +/-   0`
- Connectivity: 27 / 27 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 0 |
| S2 | 0 | 0 | 0 |
| S3 | 0 | 2 | 52 |

Switch queue drops (`ethtool -S` Q DROP) on the 19 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S3→S1 | 7 | 500 | 200.0 | 200.0 | 29.2 | 149991 | 149990 | 100.00% | 16.9 / 17.1 / 17.3 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 2 | 2 | S2→S1 | 6 | 400 | 200.0 | 200.0 | 43.3 | 150000 | 150000 | 100.00% | 31.0 / 31.2 / 33.0 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 3 | 3 | S3→S2 | 7 | 100 | 200.0 | 200.0 | 54.4 | 149990 | 149990 | 100.00% | 42.1 / 42.4 / 42.6 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 4 | 4 | S1→S3 | 6 | 300 | 800.0 | 800.0 | 26.0 | 37500 | 37500 | 100.00% | 8.1 / 8.5 / 9.2 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 5 | 6 | S2→S1 | 6 | 100 | 400.0 | 400.0 | 33.0 | 75000 | 75000 | 100.00% | 9.8 / 10.3 / 11.4 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 6 | 7 | S2→S1 | 7 | 300 | 800.0 | 800.0 | 39.4 | 37500 | 37500 | 100.00% | 27.1 / 27.3 / 27.5 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 7 | 8 | S2→S3 | 7 | 100 | 800.0 | 800.0 | 300.2 | 37500 | 37500 | 100.00% | 12.1 / 12.8 / 13.7 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 8 | 9 | S3→S2 | 6 | 500 | 200.0 | 200.0 | 54.2 | 149990 | 149990 | 100.00% | 41.8 / 42.0 / 208.6 | 0.4 | 0.0 | 1 | 0.00% | 0 |
| 9 | 10 | S1→S3 | 6 | 100 | 800.0 | 800.0 | 22.7 | 37500 | 37500 | 100.00% | 5.0 / 5.4 / 5.8 | 0.1 | 0.2 | 0 | 0.00% | 0 |
| 10 | 11 | S3→S2 | 6 | 500 | 800.0 | 800.0 | 61.8 | 37498 | 37498 | 100.00% | 41.2 / 41.9 / 42.5 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 11 | 12 | S2→S1 | 7 | 100 | 800.0 | 800.0 | 42.0 | 37500 | 37500 | 100.00% | 9.7 / 10.3 / 11.1 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 12 | 13 | S1→S2 | 7 | 300 | 400.0 | 400.0 | 118.7 | 75000 | 75000 | 100.00% | 15.9 / 55.2 / 94.1 | 38.6 | 77.3 | 0 | 0.00% | 0 |
| 13 | 14 | S1→S2 | 7 | 100 | 200.0 | 200.0 | 33.0 | 150000 | 150000 | 100.00% | 20.7 / 20.9 / 21.1 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 14 | 15 | S2→S3 | 7 | 400 | 400.0 | 400.0 | 50.9 | 75000 | 75000 | 100.00% | 32.6 / 33.2 / 33.8 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 15 | 17 | S2→S3 | 7 | 200 | 800.0 | 800.0 | 233.6 | 37500 | 37500 | 100.00% | 208.5 / 208.8 / 209.6 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 16 | 18 | S3→S2 | 7 | 100 | 400.0 | 400.0 | 120.6 | 74995 | 74995 | 100.00% | 18.1 / 18.4 / 18.6 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 17 | 19 | S3→S1 | 6 | 500 | 400.0 | 400.0 | 29.2 | 74995 | 74994 | 100.00% | 16.9 / 17.1 / 17.3 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 18 | 20 | S3→S1 | 6 | 200 | 200.0 | 200.0 | 24.7 | 149989 | 149989 | 100.00% | 6.6 / 9.8 / 181.3 | 2.8 | 5.6 | 0 | 0.00% | 0 |
| 19 | 22 | S2→S3 | 7 | 300 | 400.0 | 400.0 | 49.9 | 75000 | 75000 | 100.00% | 24.1 / 25.0 / 25.9 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 20 | 25 | S1→S2 | 6 | 200 | 800.0 | 800.0 | 156.2 | 37500 | 37500 | 100.00% | 62.5 / 62.9 / 63.3 | 0.1 | 0.1 | 0 | 0.00% | 0 |
| 21 | 27 | S1→S3 | 6 | 400 | 800.0 | 800.0 | 63.4 | 37500 | 37500 | 100.00% | 51.1 / 51.3 / 51.5 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 22 | 32 | S1→S3 | 6 | 100 | 400.0 | 400.0 | 200.0 | 75000 | 75000 | 100.00% | 5.0 / 96.7 / 188.3 | 91.3 | 182.6 | 0 | 0.00% | 0 |
| 23 | 38 | S2→S3 | 6 | 100 | 800.0 | 800.0 | 135.7 | 37500 | 37500 | 100.00% | 12.0 / 12.8 / 14.0 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 24 | 39 | S1→S3 | 6 | 300 | 800.0 | 800.0 | 63.7 | 37500 | 37500 | 100.00% | 42.0 / 42.2 / 42.4 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 25 | 40 | S1→S2 | 6 | 200 | 800.0 | 800.0 | 312.3 | 37500 | 37500 | 100.00% | 26.6 / 27.1 / 27.6 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 26 | 45 | S1→S3 | 7 | 500 | 400.0 | 400.0 | 220.8 | 75000 | 75000 | 100.00% | 11.4 / 108.9 / 206.5 | 97.2 | 194.3 | 0 | 0.00% | 0 |
| 27 | 50 | S1→S2 | 6 | 100 | 400.0 | 400.0 | 320.3 | 75000 | 75000 | 100.00% | 9.7 / 42.8 / 76.2 | 32.5 | 65.0 | 0 | 0.00% | 0 |
