# Traffic run: result-2026-10-13-dataset-testbed-13-tree-avgwin/smt-c9-on/13-fair-retimed-c9on, 2026-10-13 13:47

11 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **1012441 / 1012451 packets (100.00%)**
- Deadline misses: **0 (0.00% of received)**; flows with zero misses: 11 / 11

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 2 | 100.00% | 29.7 | 0.00% |
| S2 | 4 | 100.00% | 33.9 | 0.00% |
| S3 | 5 | 100.00% | 39.1 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7276524.181] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7439042.318] rms   17 max   31 freq  -6480 +/-  17 delay    24 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[1131299.097] rms   29 max   38 freq  +2290 +/-  38 delay    49 +/-   0`
- Connectivity: 11 / 11 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 2 |
| S2 | 0 | 0 | 8 |
| S3 | 0 | 10 | 39 |

Switch queue drops (`ethtool -S` Q DROP) on the 17 gated ports: sw02/p4 +48.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 3 | S1→S3 | 7 | 400 | 400.0 | 400.0 | 74.0 | 75000 | 75000 | 100.00% | 61.9 / 62.1 / 62.4 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 2 | 5 | S3→S2 | 6 | 500 | 200.0 | 200.0 | 54.2 | 149976 | 149971 | 100.00% | 42.1 / 42.3 / 42.5 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 3 | 8 | S3→S2 | 7 | 500 | 800.0 | 800.0 | 54.2 | 37495 | 37493 | 99.99% | 42.1 / 42.3 / 42.5 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 4 | 9 | S3→S2 | 6 | 200 | 400.0 | 400.0 | 43.0 | 74990 | 74987 | 100.00% | 30.9 / 31.1 / 31.3 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 5 | 10 | S2→S1 | 7 | 300 | 200.0 | 200.0 | 39.4 | 149996 | 149996 | 100.00% | 27.4 / 27.6 / 27.7 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 6 | 13 | S2→S1 | 7 | 500 | 400.0 | 400.0 | 45.8 | 75000 | 75000 | 100.00% | 33.8 / 34.0 / 34.1 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 7 | 14 | S1→S2 | 7 | 200 | 200.0 | 200.0 | 36.9 | 149998 | 149998 | 100.00% | 24.8 / 25.0 / 25.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 8 | 15 | S1→S3 | 7 | 100 | 800.0 | 800.0 | 61.8 | 37500 | 37500 | 100.00% | 40.3 / 40.5 / 40.8 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 9 | 17 | S2→S3 | 6 | 100 | 800.0 | 800.0 | 38.2 | 37500 | 37500 | 100.00% | 26.1 / 26.3 / 26.5 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 10 | 19 | S2→S3 | 6 | 200 | 200.0 | 200.0 | 43.0 | 149997 | 149997 | 100.00% | 30.9 / 31.1 / 31.3 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 11 | 20 | S2→S3 | 6 | 300 | 400.0 | 400.0 | 49.7 | 74999 | 74999 | 100.00% | 37.6 / 37.8 / 38.0 | 0.1 | 0.0 | 0 | 0.00% | 0 |
