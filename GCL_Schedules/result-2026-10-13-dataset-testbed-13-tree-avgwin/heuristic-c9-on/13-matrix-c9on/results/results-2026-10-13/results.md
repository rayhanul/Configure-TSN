# Traffic run: result-2026-10-13-dataset-testbed-13-tree-avgwin/heuristic-c9-on/13-matrix-c9on, 2026-10-13 13:51

11 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **1012482 / 1012482 packets (100.00%)**
- Deadline misses: **0 (0.00% of received)**; flows with zero misses: 11 / 11

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 2 | 100.00% | 26.8 | 0.00% |
| S2 | 4 | 100.00% | 32.5 | 0.00% |
| S3 | 5 | 100.00% | 28.7 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7276524.181] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7439277.622] rms   10 max   16 freq  -6452 +/-  11 delay    25 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[1131534.277] rms   41 max   65 freq  +2331 +/-  56 delay    49 +/-   0`
- Connectivity: 11 / 11 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 0 |
| S2 | 0 | 0 | 0 |
| S3 | 0 | 0 | 18 |

Switch queue drops (`ethtool -S` Q DROP) on the 17 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 3 | S1→S3 | 7 | 400 | 400.0 | 400.0 | 74.0 | 75000 | 75000 | 100.00% | 49.6 / 50.5 / 51.5 | 0.2 | 0.3 | 0 | 0.00% | 0 |
| 2 | 5 | S3→S2 | 6 | 500 | 200.0 | 200.0 | 54.2 | 149991 | 149991 | 100.00% | 41.8 / 42.0 / 42.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 3 | 8 | S3→S2 | 7 | 500 | 800.0 | 800.0 | 54.2 | 37497 | 37497 | 100.00% | 28.0 / 28.7 / 29.6 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 4 | 9 | S3→S2 | 6 | 200 | 400.0 | 400.0 | 43.0 | 74994 | 74994 | 100.00% | 30.6 / 30.8 / 31.0 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 5 | 10 | S2→S1 | 7 | 300 | 200.0 | 200.0 | 39.4 | 150000 | 150000 | 100.00% | 27.0 / 27.3 / 27.5 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 6 | 13 | S2→S1 | 7 | 500 | 400.0 | 400.0 | 45.8 | 75000 | 75000 | 100.00% | 25.0 / 25.7 / 27.7 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 7 | 14 | S1→S2 | 7 | 200 | 200.0 | 200.0 | 36.9 | 150000 | 150000 | 100.00% | 24.5 / 24.7 / 25.0 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 8 | 15 | S1→S3 | 7 | 100 | 800.0 | 800.0 | 61.8 | 37500 | 37500 | 100.00% | 28.1 / 28.9 / 29.9 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 9 | 17 | S2→S3 | 6 | 100 | 800.0 | 800.0 | 38.2 | 37500 | 37500 | 100.00% | 14.9 / 15.1 / 15.4 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 10 | 19 | S2→S3 | 6 | 200 | 200.0 | 200.0 | 43.0 | 150000 | 150000 | 100.00% | 16.0 / 16.8 / 17.9 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 11 | 20 | S2→S3 | 6 | 300 | 400.0 | 400.0 | 49.7 | 75000 | 75000 | 100.00% | 37.3 / 37.5 / 37.8 | 0.1 | 0.0 | 0 | 0.00% | 0 |
