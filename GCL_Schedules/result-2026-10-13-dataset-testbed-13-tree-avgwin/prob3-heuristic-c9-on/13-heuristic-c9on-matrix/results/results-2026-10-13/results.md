# Traffic run: result-2026-10-13-dataset-testbed-13-tree-avgwin/prob3-heuristic-c9-on/13-heuristic-c9on-matrix, 2026-10-13 13:59

25 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **1837459 / 1837459 packets (100.00%)**
- Deadline misses: **0 (0.00% of received)**; flows with zero misses: 25 / 25

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 7 | 100.00% | 73.6 | 0.00% |
| S2 | 11 | 100.00% | 46.6 | 0.00% |
| S3 | 7 | 100.00% | 61.4 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7276524.181] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7439764.500] rms   21 max   56 freq  -6454 +/-  29 delay    27 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[1132022.031] rms   33 max   52 freq  +2273 +/-  45 delay    49 +/-   0`
- Connectivity: 25 / 25 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 0 |
| S2 | 0 | 0 | 0 |
| S3 | 0 | 12 | 41 |

Switch queue drops (`ethtool -S` Q DROP) on the 17 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S3→S2 | 6 | 400 | 400.0 | 400.0 | 109.1 | 74996 | 74996 | 100.00% | 23.8 / 59.6 / 94.9 | 34.9 | 69.8 | 0 | 0.00% | 0 |
| 2 | 2 | S1→S2 | 6 | 200 | 800.0 | 800.0 | 406.1 | 37500 | 37500 | 100.00% | 29.6 / 33.9 / 34.1 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 3 | 3 | S1→S3 | 7 | 400 | 400.0 | 400.0 | 74.0 | 75000 | 75000 | 100.00% | 50.0 / 50.8 / 52.1 | 0.3 | 0.3 | 0 | 0.00% | 0 |
| 4 | 5 | S3→S2 | 6 | 500 | 200.0 | 200.0 | 54.2 | 149990 | 149990 | 100.00% | 42.1 / 42.3 / 68.3 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 5 | 6 | S3→S1 | 7 | 400 | 800.0 | 800.0 | 73.9 | 37499 | 37499 | 100.00% | 43.5 / 44.3 / 45.3 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 6 | 8 | S3→S2 | 7 | 500 | 800.0 | 800.0 | 54.2 | 37498 | 37498 | 100.00% | 28.1 / 28.7 / 29.5 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 7 | 9 | S3→S2 | 6 | 200 | 400.0 | 400.0 | 43.0 | 74996 | 74996 | 100.00% | 30.9 / 31.1 / 35.1 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 8 | 10 | S2→S1 | 7 | 300 | 200.0 | 200.0 | 39.4 | 150000 | 150000 | 100.00% | 27.4 / 27.5 / 27.7 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 9 | 13 | S2→S1 | 7 | 500 | 400.0 | 400.0 | 45.8 | 75000 | 75000 | 100.00% | 25.3 / 25.9 / 26.6 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 10 | 14 | S1→S2 | 7 | 200 | 200.0 | 200.0 | 36.9 | 150000 | 150000 | 100.00% | 24.8 / 25.0 / 25.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 11 | 15 | S1→S3 | 7 | 100 | 800.0 | 800.0 | 61.8 | 37500 | 37500 | 100.00% | 28.4 / 29.2 / 30.5 | 0.3 | 0.2 | 0 | 0.00% | 0 |
| 12 | 17 | S2→S3 | 6 | 100 | 800.0 | 800.0 | 38.2 | 37500 | 37500 | 100.00% | 15.2 / 15.4 / 15.6 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 13 | 19 | S2→S3 | 6 | 200 | 200.0 | 200.0 | 43.0 | 150000 | 150000 | 100.00% | 16.0 / 16.7 / 17.6 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 14 | 20 | S2→S3 | 6 | 300 | 400.0 | 400.0 | 49.7 | 75000 | 75000 | 100.00% | 37.6 / 37.8 / 38.0 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 15 | 23 | S3→S1 | 6 | 400 | 400.0 | 400.0 | 289.0 | 74995 | 74995 | 100.00% | 195.7 / 204.9 / 213.7 | 8.6 | 17.2 | 0 | 0.00% | 0 |
| 16 | 26 | S3→S1 | 7 | 300 | 800.0 | 800.0 | 95.4 | 37498 | 37498 | 100.00% | 74.8 / 75.5 / 76.2 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 17 | 29 | S3→S1 | 6 | 100 | 400.0 | 400.0 | 212.5 | 74996 | 74996 | 100.00% | 110.1 / 119.3 / 128.1 | 8.6 | 17.2 | 0 | 0.00% | 0 |
| 18 | 30 | S1→S2 | 7 | 300 | 200.0 | 200.0 | 107.2 | 150000 | 150000 | 100.00% | 21.3 / 63.5 / 86.9 | 25.8 | 32.6 | 0 | 0.00% | 0 |
| 19 | 31 | S1→S3 | 7 | 400 | 800.0 | 800.0 | 419.5 | 37500 | 37500 | 100.00% | 405.9 / 406.1 / 406.3 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 20 | 37 | S3→S1 | 7 | 200 | 800.0 | 800.0 | 236.8 | 37498 | 37498 | 100.00% | 25.4 / 26.5 / 27.6 | 0.3 | 0.2 | 0 | 0.00% | 0 |
| 21 | 41 | S1→S2 | 7 | 500 | 400.0 | 400.0 | 106.9 | 75000 | 75000 | 100.00% | 29.6 / 62.4 / 95.3 | 32.6 | 65.3 | 0 | 0.00% | 0 |
| 22 | 44 | S1→S3 | 7 | 400 | 800.0 | 800.0 | 332.8 | 37500 | 37500 | 100.00% | 41.4 / 42.2 / 43.8 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 23 | 45 | S3→S2 | 7 | 300 | 400.0 | 400.0 | 219.2 | 74995 | 74995 | 100.00% | 19.8 / 20.7 / 21.9 | 0.3 | 0.3 | 0 | 0.00% | 0 |
| 24 | 48 | S3→S2 | 7 | 200 | 800.0 | 800.0 | 54.1 | 37498 | 37498 | 100.00% | 19.7 / 20.4 / 21.2 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 25 | 49 | S1→S2 | 6 | 100 | 800.0 | 800.0 | 701.1 | 37500 | 37500 | 100.00% | 165.3 / 165.7 / 166.1 | 0.1 | 0.1 | 0 | 0.00% | 0 |
