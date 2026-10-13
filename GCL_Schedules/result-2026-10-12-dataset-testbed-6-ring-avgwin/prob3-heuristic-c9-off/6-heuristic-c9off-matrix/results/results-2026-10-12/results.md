# Traffic run: result-2026-10-12-dataset-testbed-6-ring-avgwin/prob3-heuristic-c9-off/6-heuristic-c9off-matrix, 2026-10-12 13:54

25 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **1794077 / 1799968 packets (99.67%)**
- Deadline misses: **125 (0.01% of received)**; flows with zero misses: 16 / 25

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 8 | 99.78% | 56.2 | 0.00% |
| S2 | 6 | 99.55% | 95.2 | 0.01% |
| S3 | 11 | 99.65% | 91.2 | 0.01% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7276524.181] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7353054.715] rms    8 max   11 freq  -6294 +/-  10 delay    24 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[1045311.859] rms    5 max   11 freq  +2829 +/-   6 delay    50 +/-   0`
- Connectivity: 25 / 25 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 0 |
| S2 | 0 | 0 | 0 |
| S3 | 0 | 0 | 32 |

Switch queue drops (`ethtool -S` Q DROP) on the 19 gated ports: sw01/p4 +1573, sw02/p4 +769, sw06/p4 +2, sw07/p4 +1974, sw08/p4 +1573.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S3→S1 | 6 | 500 | 200.0 | 200.0 | 45.8 | 149990 | 149990 | 100.00% | 33.5 / 33.7 / 96.5 | 0.2 | 0.0 | 0 | 0.00% | 0 |
| 2 | 2 | S2→S1 | 7 | 400 | 200.0 | 200.0 | 79.1 | 150000 | 150000 | 100.00% | 66.8 / 67.0 / 67.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 3 | 4 | S1→S3 | 6 | 300 | 800.0 | 800.0 | 45.8 | 37500 | 37500 | 100.00% | 8.1 / 8.5 / 12.1 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 4 | 6 | S2→S1 | 6 | 100 | 400.0 | 400.0 | 83.6 | 75000 | 74213 | 98.95% | 71.3 / 135.7 / 320808.7 | 4520.8 | 8.7 | 15 | 0.02% | 0 |
| 5 | 7 | S2→S1 | 6 | 300 | 800.0 | 800.0 | 84.2 | 37500 | 37107 | 98.95% | 47.3 / 116.0 / 320788.9 | 4669.0 | 17.3 | 8 | 0.02% | 0 |
| 6 | 8 | S2→S3 | 7 | 100 | 800.0 | 800.0 | 500.2 | 37500 | 37500 | 100.00% | 487.9 / 488.1 / 488.3 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 7 | 9 | S3→S2 | 6 | 500 | 200.0 | 200.0 | 95.8 | 149991 | 148418 | 98.95% | 83.4 / 150.0 / 320812.5 | 4593.9 | 4.3 | 32 | 0.02% | 0 |
| 8 | 10 | S1→S3 | 6 | 100 | 800.0 | 800.0 | 45.8 | 37500 | 37500 | 100.00% | 5.0 / 5.4 / 21.0 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 9 | 12 | S2→S1 | 6 | 100 | 800.0 | 800.0 | 79.1 | 37500 | 37107 | 98.95% | 47.0 / 115.7 / 320766.5 | 4668.7 | 17.3 | 8 | 0.02% | 0 |
| 10 | 13 | S1→S2 | 7 | 300 | 400.0 | 400.0 | 185.3 | 75000 | 75000 | 100.00% | 15.9 / 16.6 / 17.4 | 0.2 | 0.3 | 0 | 0.00% | 0 |
| 11 | 14 | S1→S2 | 7 | 100 | 200.0 | 200.0 | 79.1 | 150000 | 150000 | 100.00% | 50.2 / 52.8 / 53.8 | 0.3 | 0.1 | 0 | 0.00% | 0 |
| 12 | 15 | S2→S3 | 6 | 400 | 400.0 | 400.0 | 200.0 | 75000 | 74211 | 98.95% | 23.9 / 84.3 / 320817.7 | 4214.8 | 16.3 | 13 | 0.02% | 0 |
| 13 | 17 | S2→S3 | 7 | 200 | 800.0 | 800.0 | 429.1 | 37500 | 37500 | 100.00% | 400.5 / 401.4 / 401.6 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 14 | 19 | S3→S1 | 7 | 500 | 400.0 | 400.0 | 46.5 | 74996 | 74996 | 100.00% | 11.4 / 11.8 / 14.1 | 0.1 | 0.2 | 0 | 0.00% | 0 |
| 15 | 20 | S3→S1 | 7 | 200 | 200.0 | 200.0 | 45.8 | 149991 | 149991 | 100.00% | 20.3 / 20.4 / 24.7 | 0.2 | 0.0 | 0 | 0.00% | 0 |
| 16 | 22 | S2→S3 | 6 | 300 | 400.0 | 400.0 | 149.4 | 75000 | 74210 | 98.95% | 19.8 / 72.2 / 320738.2 | 4051.2 | 8.9 | 12 | 0.02% | 0 |
| 17 | 25 | S1→S2 | 6 | 200 | 800.0 | 800.0 | 150.1 | 37500 | 37115 | 98.97% | 116.0 / 252.0 / 320791.1 | 6533.7 | 17.4 | 16 | 0.04% | 0 |
| 18 | 27 | S1→S3 | 6 | 400 | 800.0 | 800.0 | 45.8 | 37500 | 37500 | 100.00% | 9.7 / 10.2 / 16.1 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 19 | 32 | S1→S3 | 6 | 100 | 400.0 | 400.0 | 116.5 | 75000 | 75000 | 100.00% | 5.1 / 6.9 / 8.3 | 0.3 | 0.3 | 0 | 0.00% | 0 |
| 20 | 36 | S2→S1 | 7 | 500 | 800.0 | 800.0 | 95.7 | 37500 | 37500 | 100.00% | 57.4 / 59.3 / 59.5 | 0.2 | 0.0 | 0 | 0.00% | 0 |
| 21 | 38 | S2→S3 | 6 | 100 | 800.0 | 800.0 | 191.7 | 37500 | 37105 | 98.95% | 21.0 / 94.3 / 320796.1 | 4054.0 | 33.7 | 6 | 0.02% | 0 |
| 22 | 39 | S1→S3 | 6 | 300 | 800.0 | 800.0 | 45.8 | 37500 | 37500 | 100.00% | 8.1 / 8.5 / 9.0 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 23 | 40 | S1→S2 | 6 | 200 | 800.0 | 800.0 | 129.0 | 37500 | 37114 | 98.97% | 30.2 / 158.0 / 320705.6 | 6334.4 | 17.5 | 15 | 0.04% | 0 |
| 24 | 45 | S1→S3 | 6 | 500 | 400.0 | 400.0 | 45.8 | 75000 | 75000 | 100.00% | 11.4 / 11.8 / 12.8 | 0.1 | 0.2 | 0 | 0.00% | 0 |
| 25 | 50 | S1→S2 | 7 | 100 | 400.0 | 400.0 | 79.0 | 75000 | 75000 | 100.00% | 38.4 / 41.2 / 42.0 | 0.3 | 0.2 | 0 | 0.00% | 0 |
