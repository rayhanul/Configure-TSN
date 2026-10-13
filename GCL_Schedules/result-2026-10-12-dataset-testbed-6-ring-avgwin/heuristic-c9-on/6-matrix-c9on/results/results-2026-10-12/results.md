# Traffic run: result-2026-10-12-dataset-testbed-6-ring-avgwin/heuristic-c9-on/6-matrix-c9on, 2026-10-12 13:33

10 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **1012470 / 1012470 packets (100.00%)**
- Deadline misses: **0 (0.00% of received)**; flows with zero misses: 10 / 10

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 7 | 100.00% | 18.3 | 0.00% |
| S2 | 2 | 100.00% | 31.5 | 0.00% |
| S3 | 1 | 100.00% | 8.5 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7276524.181] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7351832.180] rms   10 max   20 freq  -6313 +/-  14 delay    24 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[1044089.571] rms    5 max    9 freq  +2904 +/-   6 delay    49 +/-   0`
- Connectivity: 10 / 10 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 0 |
| S2 | 0 | 0 | 0 |
| S3 | 0 | 0 | 30 |

Switch queue drops (`ethtool -S` Q DROP) on the 19 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S3→S1 | 7 | 500 | 200.0 | 200.0 | 29.2 | 149991 | 149991 | 100.00% | 16.9 / 17.1 / 17.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 2 | 2 | S2→S1 | 6 | 400 | 200.0 | 200.0 | 43.3 | 150000 | 150000 | 100.00% | 30.9 / 31.1 / 31.3 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 3 | 4 | S1→S3 | 6 | 300 | 800.0 | 800.0 | 26.0 | 37500 | 37500 | 100.00% | 8.1 / 8.5 / 9.0 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 4 | 6 | S2→S1 | 6 | 100 | 400.0 | 400.0 | 33.0 | 75000 | 75000 | 100.00% | 9.8 / 10.3 / 11.1 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 5 | 7 | S2→S1 | 7 | 300 | 800.0 | 800.0 | 39.4 | 37500 | 37500 | 100.00% | 27.1 / 27.3 / 27.5 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 6 | 9 | S3→S2 | 6 | 500 | 200.0 | 200.0 | 54.2 | 149990 | 149990 | 100.00% | 41.8 / 42.0 / 42.3 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 7 | 12 | S2→S1 | 7 | 100 | 800.0 | 800.0 | 42.0 | 37500 | 37500 | 100.00% | 9.7 / 10.3 / 11.1 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 8 | 14 | S1→S2 | 7 | 100 | 200.0 | 200.0 | 33.0 | 150000 | 150000 | 100.00% | 20.7 / 20.9 / 21.1 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 9 | 19 | S3→S1 | 6 | 500 | 400.0 | 400.0 | 29.2 | 74998 | 74998 | 100.00% | 16.9 / 17.1 / 17.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 10 | 20 | S3→S1 | 6 | 200 | 200.0 | 200.0 | 24.7 | 149991 | 149991 | 100.00% | 9.3 / 11.1 / 12.8 | 1.4 | 2.9 | 0 | 0.00% | 0 |
