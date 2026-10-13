# Traffic run: result-2026-10-12-dataset-testbed-6-ring-avgwin/prob3-heuristic-c9-on/6-heuristic-c9on-matrix, 2026-10-12 14:02

25 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **1799939 / 1799950 packets (100.00%)**
- Deadline misses: **0 (0.00% of received)**; flows with zero misses: 25 / 25

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 8 | 100.00% | 18.6 | 0.00% |
| S2 | 6 | 100.00% | 27.1 | 0.00% |
| S3 | 11 | 100.00% | 139.5 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7276524.181] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7353537.579] rms   10 max   21 freq  -6310 +/-  13 delay    24 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[1045794.723] rms    8 max   20 freq  +2874 +/-   9 delay    50 +/-   0`
- Connectivity: 25 / 25 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 1 |
| S2 | 0 | 0 | 14 |
| S3 | 0 | 11 | 35 |

Switch queue drops (`ethtool -S` Q DROP) on the 19 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S3→S1 | 7 | 500 | 200.0 | 200.0 | 29.2 | 149991 | 149987 | 100.00% | 16.9 / 17.1 / 17.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 2 | 2 | S2→S1 | 6 | 400 | 200.0 | 200.0 | 43.3 | 149997 | 149997 | 100.00% | 31.0 / 31.1 / 31.3 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 3 | 4 | S1→S3 | 6 | 300 | 800.0 | 800.0 | 26.0 | 37500 | 37500 | 100.00% | 8.1 / 8.5 / 9.0 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 4 | 6 | S2→S1 | 6 | 100 | 400.0 | 400.0 | 33.0 | 74998 | 74998 | 100.00% | 9.8 / 10.3 / 11.1 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 5 | 7 | S2→S1 | 7 | 300 | 800.0 | 800.0 | 39.4 | 37499 | 37499 | 100.00% | 27.1 / 27.3 / 27.5 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 6 | 8 | S2→S3 | 7 | 100 | 800.0 | 800.0 | 500.2 | 37499 | 37499 | 100.00% | 487.9 / 488.1 / 488.3 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 7 | 9 | S3→S2 | 6 | 500 | 200.0 | 200.0 | 54.2 | 149990 | 149987 | 100.00% | 41.8 / 42.0 / 42.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 8 | 10 | S1→S3 | 6 | 100 | 800.0 | 800.0 | 22.7 | 37500 | 37500 | 100.00% | 5.0 / 5.4 / 5.8 | 0.1 | 0.2 | 0 | 0.00% | 0 |
| 9 | 12 | S2→S1 | 7 | 100 | 800.0 | 800.0 | 42.0 | 37499 | 37499 | 100.00% | 9.7 / 10.3 / 11.1 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 10 | 13 | S1→S2 | 6 | 300 | 400.0 | 400.0 | 39.4 | 74999 | 74999 | 100.00% | 15.9 / 16.6 / 18.2 | 0.2 | 0.3 | 0 | 0.00% | 0 |
| 11 | 14 | S1→S2 | 7 | 100 | 200.0 | 200.0 | 33.0 | 150000 | 150000 | 100.00% | 20.7 / 20.9 / 21.1 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 12 | 15 | S2→S3 | 6 | 400 | 400.0 | 400.0 | 115.5 | 74998 | 74998 | 100.00% | 23.8 / 28.5 / 33.1 | 3.8 | 7.6 | 0 | 0.00% | 0 |
| 13 | 17 | S2→S3 | 7 | 200 | 800.0 | 800.0 | 488.0 | 37499 | 37499 | 100.00% | 463.9 / 464.1 / 464.3 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 14 | 19 | S3→S1 | 6 | 500 | 400.0 | 400.0 | 29.2 | 74993 | 74991 | 100.00% | 16.9 / 17.1 / 17.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 15 | 20 | S3→S1 | 6 | 200 | 200.0 | 200.0 | 24.7 | 149991 | 149989 | 100.00% | 9.3 / 11.1 / 15.4 | 1.4 | 2.9 | 0 | 0.00% | 0 |
| 16 | 22 | S2→S3 | 6 | 300 | 400.0 | 400.0 | 196.2 | 74998 | 74998 | 100.00% | 70.7 / 71.9 / 76.0 | 1.4 | 1.2 | 0 | 0.00% | 0 |
| 17 | 25 | S1→S2 | 6 | 200 | 800.0 | 800.0 | 81.0 | 37500 | 37500 | 100.00% | 59.8 / 60.4 / 61.8 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 18 | 27 | S1→S3 | 6 | 400 | 800.0 | 800.0 | 27.8 | 37500 | 37500 | 100.00% | 10.0 / 10.7 / 11.5 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 19 | 32 | S1→S3 | 6 | 100 | 400.0 | 400.0 | 32.0 | 75000 | 75000 | 100.00% | 5.0 / 5.4 / 5.8 | 0.1 | 0.2 | 0 | 0.00% | 0 |
| 20 | 36 | S2→S1 | 7 | 500 | 800.0 | 800.0 | 45.8 | 37499 | 37499 | 100.00% | 22.5 / 23.1 / 23.8 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 21 | 38 | S2→S3 | 7 | 100 | 800.0 | 800.0 | 512.3 | 37500 | 37500 | 100.00% | 400.3 / 403.1 / 403.4 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 22 | 39 | S1→S3 | 7 | 300 | 800.0 | 800.0 | 511.0 | 37500 | 37500 | 100.00% | 477.0 / 477.5 / 477.9 | 0.1 | 0.1 | 0 | 0.00% | 0 |
| 23 | 40 | S1→S2 | 7 | 200 | 800.0 | 800.0 | 36.8 | 37500 | 37500 | 100.00% | 12.8 / 13.5 / 14.5 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 24 | 45 | S1→S3 | 6 | 500 | 400.0 | 400.0 | 90.2 | 75000 | 75000 | 100.00% | 11.4 / 11.8 / 12.2 | 0.1 | 0.2 | 0 | 0.00% | 0 |
| 25 | 50 | S1→S2 | 7 | 100 | 400.0 | 400.0 | 36.8 | 75000 | 75000 | 100.00% | 9.7 / 10.3 / 11.3 | 0.2 | 0.2 | 0 | 0.00% | 0 |
