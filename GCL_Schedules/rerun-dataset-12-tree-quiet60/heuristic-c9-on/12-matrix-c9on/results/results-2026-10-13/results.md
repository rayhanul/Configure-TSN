# Traffic run: rerun-dataset-12-tree-quiet60/heuristic-c9-on/12-matrix-c9on, 2026-10-13 15:14

11 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **937485 / 937485 packets (100.00%)**
- Deadline misses: **0 (0.00% of received)**; flows with zero misses: 11 / 11

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 3 | 100.00% | 33.0 | 0.00% |
| S2 | 4 | 100.00% | 28.6 | 0.00% |
| S3 | 4 | 100.00% | 58.5 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7276524.181] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7444302.215] rms    6 max   11 freq  -6412 +/-   9 delay    25 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[1136559.745] rms   33 max   54 freq  +2185 +/-  45 delay    49 +/-   0`
- Connectivity: 11 / 11 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 0 |
| S2 | 0 | 0 | 0 |
| S3 | 0 | 0 | 15 |

Switch queue drops (`ethtool -S` Q DROP) on the 17 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 2 | S1→S2 | 6 | 400 | 200.0 | 200.0 | 51.0 | 150000 | 150000 | 100.00% | 38.6 / 38.8 / 39.0 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 2 | 4 | S1→S3 | 6 | 300 | 800.0 | 800.0 | 66.3 | 37500 | 37500 | 100.00% | 45.4 / 46.1 / 46.9 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 3 | 5 | S3→S2 | 7 | 100 | 200.0 | 200.0 | 38.2 | 149991 | 149991 | 100.00% | 25.8 / 26.0 / 26.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 4 | 7 | S3→S1 | 6 | 500 | 800.0 | 800.0 | 79.1 | 37498 | 37498 | 100.00% | 63.9 / 64.3 / 64.8 | 0.2 | 0.1 | 0 | 0.00% | 0 |
| 5 | 8 | S2→S1 | 7 | 300 | 200.0 | 200.0 | 39.4 | 150000 | 150000 | 100.00% | 27.1 / 27.3 / 27.5 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 6 | 9 | S3→S2 | 6 | 200 | 400.0 | 400.0 | 43.0 | 74996 | 74996 | 100.00% | 17.0 / 17.2 / 17.9 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 7 | 11 | S2→S1 | 7 | 300 | 800.0 | 800.0 | 39.4 | 37500 | 37500 | 100.00% | 24.1 / 24.6 / 25.1 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 8 | 12 | S1→S3 | 6 | 500 | 200.0 | 200.0 | 79.1 | 150000 | 150000 | 100.00% | 66.8 / 67.0 / 67.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 9 | 14 | S1→S2 | 7 | 200 | 400.0 | 400.0 | 36.9 | 75000 | 75000 | 100.00% | 24.6 / 24.7 / 25.0 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 10 | 18 | S2→S3 | 6 | 300 | 800.0 | 800.0 | 54.5 | 37500 | 37500 | 100.00% | 33.5 / 33.7 / 33.9 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 11 | 19 | S1→S3 | 6 | 400 | 800.0 | 800.0 | 74.0 | 37500 | 37500 | 100.00% | 61.7 / 61.9 / 62.1 | 0.1 | 0.0 | 0 | 0.00% | 0 |
