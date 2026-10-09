# Traffic run: dataset-testbed-2_2026-10-09/2-heuristic-c9off-matrix-25flows, 2026-10-09 12:38

25 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **1949961 / 1950000 packets (100.00%)**
- Deadline misses: **150000 (7.69% of received)**; flows with zero misses: 24 / 25

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 9 | 100.00% | 31.4 | 0.00% |
| S2 | 5 | 100.00% | 110.6 | 26.67% |
| S3 | 11 | 100.00% | 43.7 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7048158.236] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7089293.994] rms    7 max   15 freq  -6331 +/-   8 delay    18 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[781551.273] rms    8 max   11 freq  +2961 +/-  10 delay    44 +/-   0`

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 0 |
| S2 | 0 | 1 | 0 |
| S3 | 0 | 47 | 0 |

Switch queue drops (`ethtool -S` Q DROP) on the 27 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S1→S2 | 6 | 500 | 200.0 | 200.0 | 41.9 | 150000 | 150000 | 100.00% | 200.2 / 201.1 / 204.5 | 1.1 | 1.3 | 150000 | 100.00% | 0 |
| 2 | 4 | S1→S3 | 6 | 400 | 800.0 | 800.0 | 18.9 | 37500 | 37500 | 100.00% | 12.1 / 12.5 / 13.0 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 3 | 6 | S2→S1 | 6 | 100 | 800.0 | 800.0 | 76.2 | 37500 | 37500 | 100.00% | 73.8 / 74.0 / 78.9 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 4 | 7 | S3→S1 | 6 | 300 | 400.0 | 400.0 | 16.0 | 75000 | 74995 | 99.99% | 15.8 / 16.2 / 17.5 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 5 | 9 | S1→S2 | 7 | 400 | 200.0 | 200.0 | 43.2 | 150000 | 150000 | 100.00% | 34.5 / 41.8 / 44.5 | 2.5 | 5.0 | 0 | 0.00% | 0 |
| 6 | 10 | S3→S2 | 6 | 300 | 800.0 | 800.0 | 30.7 | 37500 | 37498 | 99.99% | 183.2 / 183.4 / 185.0 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 7 | 11 | S2→S3 | 7 | 300 | 400.0 | 400.0 | 31.7 | 75000 | 75000 | 100.00% | 29.3 / 29.5 / 29.8 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 8 | 12 | S2→S1 | 7 | 200 | 800.0 | 800.0 | 29.4 | 37500 | 37500 | 100.00% | 26.3 / 26.5 / 26.7 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 9 | 13 | S3→S1 | 7 | 100 | 400.0 | 400.0 | 16.0 | 75000 | 74995 | 99.99% | 5.0 / 5.4 / 20.5 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 10 | 14 | S3→S2 | 7 | 500 | 200.0 | 200.0 | 37.4 | 150000 | 149989 | 99.99% | 42.4 / 76.7 / 168.1 | 52.4 | 62.4 | 0 | 0.00% | 0 |
| 11 | 15 | S2→S3 | 6 | 400 | 400.0 | 400.0 | 118.1 | 75000 | 75000 | 100.00% | 79.6 / 97.4 / 115.2 | 17.6 | 35.2 | 0 | 0.00% | 0 |
| 12 | 16 | S2→S1 | 7 | 100 | 400.0 | 400.0 | 29.4 | 75000 | 75000 | 100.00% | 30.5 / 30.7 / 30.8 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 13 | 18 | S2→S1 | 7 | 400 | 200.0 | 200.0 | 34.2 | 150000 | 150000 | 100.00% | 31.0 / 35.3 / 39.6 | 4.2 | 8.3 | 0 | 0.00% | 0 |
| 14 | 20 | S3→S2 | 7 | 300 | 400.0 | 400.0 | 33.0 | 75000 | 74995 | 99.99% | 38.1 / 99.0 / 160.4 | 60.7 | 121.4 | 0 | 0.00% | 0 |
| 15 | 22 | S2→S3 | 6 | 100 | 800.0 | 800.0 | 79.7 | 37500 | 37500 | 100.00% | 9.7 / 10.3 / 11.1 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 16 | 23 | S1→S3 | 7 | 400 | 400.0 | 400.0 | 302.4 | 75000 | 75000 | 100.00% | 9.7 / 153.3 / 296.9 | 143.2 | 286.3 | 0 | 0.00% | 0 |
| 17 | 26 | S2→S3 | 7 | 200 | 400.0 | 400.0 | 31.7 | 75000 | 75000 | 100.00% | 29.0 / 29.2 / 29.4 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 18 | 29 | S1→S3 | 6 | 500 | 400.0 | 400.0 | 20.8 | 75000 | 75000 | 100.00% | 11.4 / 11.8 / 12.7 | 0.1 | 0.2 | 0 | 0.00% | 0 |
| 19 | 34 | S3→S1 | 7 | 400 | 200.0 | 200.0 | 18.9 | 150000 | 149990 | 99.99% | 9.7 / 10.2 / 27.8 | 0.2 | 0.1 | 0 | 0.00% | 0 |
| 20 | 36 | S2→S3 | 7 | 100 | 400.0 | 400.0 | 29.4 | 75000 | 75000 | 100.00% | 25.0 / 25.2 / 25.4 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 21 | 37 | S2→S3 | 6 | 100 | 800.0 | 800.0 | 83.5 | 37500 | 37500 | 100.00% | 9.7 / 10.3 / 11.1 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 22 | 40 | S2→S1 | 6 | 100 | 800.0 | 800.0 | 80.0 | 37500 | 37500 | 100.00% | 71.9 / 72.1 / 77.0 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 23 | 48 | S2→S3 | 7 | 400 | 400.0 | 400.0 | 34.2 | 75000 | 75000 | 100.00% | 19.0 / 19.8 / 20.6 | 0.2 | 0.3 | 0 | 0.00% | 0 |
| 24 | 49 | S2→S1 | 6 | 200 | 400.0 | 400.0 | 83.8 | 75000 | 74999 | 100.00% | 68.1 / 69.2 / 77.8 | 1.0 | 1.9 | 0 | 0.00% | 0 |
| 25 | 50 | S1→S3 | 6 | 300 | 800.0 | 800.0 | 16.0 | 37500 | 37500 | 100.00% | 19.8 / 20.2 / 21.3 | 0.2 | 0.2 | 0 | 0.00% | 0 |
