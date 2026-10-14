# Traffic run: rerun-dataset-12-tree-quiet60/heuristic-c9-off/12-matrix-c9off, 2026-10-13 15:12

11 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **937493 / 937493 packets (100.00%)**
- Deadline misses: **0 (0.00% of received)**; flows with zero misses: 11 / 11

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 3 | 100.00% | 31.2 | 0.00% |
| S2 | 4 | 100.00% | 55.4 | 0.00% |
| S3 | 4 | 100.00% | 76.5 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7276524.181] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7444137.979] rms    9 max   16 freq  -6422 +/-  12 delay    22 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[1136395.009] rms   17 max   34 freq  +2111 +/-  15 delay    47 +/-   0`
- Connectivity: 11 / 11 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 0 |
| S2 | 0 | 0 | 0 |
| S3 | 0 | 0 | 7 |

Switch queue drops (`ethtool -S` Q DROP) on the 17 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 2 | S1→S2 | 7 | 400 | 200.0 | 200.0 | 79.1 | 150000 | 150000 | 100.00% | 54.8 / 55.3 / 56.6 | 0.3 | 0.2 | 0 | 0.00% | 0 |
| 2 | 4 | S1→S3 | 7 | 300 | 800.0 | 800.0 | 145.7 | 37500 | 37500 | 100.00% | 83.8 / 84.0 / 84.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 3 | 5 | S3→S2 | 7 | 100 | 200.0 | 200.0 | 95.8 | 149993 | 149993 | 100.00% | 54.8 / 58.1 / 75.3 | 1.1 | 0.5 | 0 | 0.00% | 0 |
| 4 | 7 | S3→S1 | 6 | 500 | 800.0 | 800.0 | 145.7 | 37500 | 37500 | 100.00% | 77.8 / 78.6 / 79.5 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 5 | 8 | S2→S1 | 6 | 300 | 200.0 | 200.0 | 79.1 | 150000 | 150000 | 100.00% | 15.8 / 16.6 / 17.4 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 6 | 9 | S3→S2 | 6 | 200 | 400.0 | 400.0 | 95.8 | 75000 | 75000 | 100.00% | 83.4 / 83.6 / 83.8 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 7 | 11 | S2→S1 | 7 | 300 | 800.0 | 800.0 | 79.1 | 37500 | 37500 | 100.00% | 41.8 / 42.0 / 42.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 8 | 12 | S1→S3 | 7 | 500 | 200.0 | 200.0 | 146.0 | 150000 | 150000 | 100.00% | 67.1 / 68.0 / 133.9 | 0.4 | 0.2 | 0 | 0.00% | 0 |
| 9 | 14 | S1→S2 | 7 | 200 | 400.0 | 400.0 | 83.6 | 75000 | 75000 | 100.00% | 21.6 / 22.2 / 22.7 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 10 | 18 | S2→S3 | 6 | 300 | 800.0 | 800.0 | 95.8 | 37500 | 37500 | 100.00% | 57.9 / 58.5 / 59.1 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 11 | 19 | S1→S3 | 6 | 400 | 800.0 | 800.0 | 145.7 | 37500 | 37500 | 100.00% | 120.9 / 121.1 / 121.3 | 0.1 | 0.0 | 0 | 0.00% | 0 |
