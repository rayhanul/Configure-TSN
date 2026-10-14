# Traffic run: rerun-dataset-11-tree-quiet60/heuristic-c9-on/11-matrix-c9on, 2026-10-13 14:52

10 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **937475 / 937475 packets (100.00%)**
- Deadline misses: **0 (0.00% of received)**; flows with zero misses: 10 / 10

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 3 | 100.00% | 24.3 | 0.00% |
| S2 | 6 | 100.00% | 38.3 | 0.00% |
| S3 | 1 | 100.00% | 28.7 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7276524.181] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7442933.767] rms   22 max   56 freq  -6328 +/-  28 delay    24 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[1135191.049] rms   53 max   94 freq  +2426 +/-  72 delay    49 +/-   0`
- Connectivity: 10 / 10 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 0 |
| S2 | 0 | 0 | 0 |
| S3 | 0 | 0 | 25 |

Switch queue drops (`ethtool -S` Q DROP) on the 17 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S1→S2 | 7 | 500 | 200.0 | 200.0 | 45.8 | 150000 | 150000 | 100.00% | 33.7 / 33.9 / 34.1 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 2 | 2 | S3→S2 | 7 | 400 | 200.0 | 200.0 | 58.6 | 149991 | 149991 | 100.00% | 43.5 / 43.9 / 44.3 | 0.1 | 0.1 | 0 | 0.00% | 0 |
| 3 | 3 | S1→S2 | 6 | 500 | 400.0 | 400.0 | 46.5 | 75000 | 75000 | 100.00% | 34.4 / 34.6 / 34.8 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 4 | 5 | S2→S1 | 6 | 200 | 200.0 | 200.0 | 36.9 | 150000 | 150000 | 100.00% | 18.7 / 19.3 / 19.9 | 0.2 | 0.1 | 0 | 0.00% | 0 |
| 5 | 7 | S2→S1 | 6 | 300 | 800.0 | 800.0 | 39.4 | 37500 | 37500 | 100.00% | 27.3 / 27.5 / 27.7 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 6 | 8 | S3→S2 | 7 | 500 | 200.0 | 200.0 | 59.3 | 149990 | 149990 | 100.00% | 28.0 / 44.0 / 47.6 | 7.2 | 3.7 | 0 | 0.00% | 0 |
| 7 | 9 | S3→S2 | 6 | 100 | 800.0 | 800.0 | 38.2 | 37498 | 37498 | 100.00% | 23.2 / 23.6 / 24.0 | 0.1 | 0.1 | 0 | 0.00% | 0 |
| 8 | 10 | S3→S1 | 7 | 300 | 400.0 | 400.0 | 66.3 | 74996 | 74996 | 100.00% | 31.5 / 32.8 / 34.0 | 0.3 | 0.3 | 0 | 0.00% | 0 |
| 9 | 18 | S2→S3 | 7 | 500 | 800.0 | 800.0 | 54.2 | 37500 | 37500 | 100.00% | 28.1 / 28.7 / 29.6 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 10 | 20 | S1→S2 | 6 | 500 | 400.0 | 400.0 | 47.1 | 75000 | 75000 | 100.00% | 35.0 / 35.2 / 35.4 | 0.1 | 0.0 | 0 | 0.00% | 0 |
