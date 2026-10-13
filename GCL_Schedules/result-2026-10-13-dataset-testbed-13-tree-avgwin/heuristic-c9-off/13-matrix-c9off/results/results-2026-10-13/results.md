# Traffic run: result-2026-10-13-dataset-testbed-13-tree-avgwin/heuristic-c9-off/13-matrix-c9off, 2026-10-13 13:49

11 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **1012487 / 1012487 packets (100.00%)**
- Deadline misses: **0 (0.00% of received)**; flows with zero misses: 11 / 11

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 2 | 100.00% | 20.9 | 0.00% |
| S2 | 4 | 100.00% | 34.7 | 0.00% |
| S3 | 5 | 100.00% | 73.5 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7276524.181] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7439160.474] rms   15 max   27 freq  -6475 +/-  16 delay    24 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[1131418.129] rms   29 max   50 freq  +2289 +/-  23 delay    50 +/-   0`
- Connectivity: 11 / 11 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 0 |
| S2 | 0 | 0 | 1 |
| S3 | 0 | 0 | 12 |

Switch queue drops (`ethtool -S` Q DROP) on the 17 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 3 | S1→S3 | 7 | 400 | 400.0 | 400.0 | 145.7 | 75000 | 75000 | 100.00% | 133.4 / 133.6 / 133.8 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 2 | 5 | S3→S2 | 6 | 500 | 200.0 | 200.0 | 95.8 | 149992 | 149992 | 100.00% | 28.0 / 31.5 / 40.5 | 4.7 | 5.6 | 0 | 0.00% | 0 |
| 3 | 8 | S3→S2 | 6 | 500 | 800.0 | 800.0 | 95.8 | 37499 | 37499 | 100.00% | 61.2 / 61.6 / 62.2 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 4 | 9 | S3→S2 | 6 | 200 | 400.0 | 400.0 | 95.8 | 74997 | 74997 | 100.00% | 69.8 / 70.2 / 70.6 | 0.1 | 0.2 | 0 | 0.00% | 0 |
| 5 | 10 | S2→S1 | 6 | 300 | 200.0 | 200.0 | 79.1 | 150000 | 150000 | 100.00% | 15.9 / 16.6 / 17.8 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 6 | 13 | S2→S1 | 7 | 500 | 400.0 | 400.0 | 79.1 | 75000 | 75000 | 100.00% | 29.3 / 29.5 / 29.7 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 7 | 14 | S1→S2 | 6 | 200 | 200.0 | 200.0 | 79.1 | 150000 | 150000 | 100.00% | 12.8 / 13.5 / 31.2 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 8 | 15 | S1→S3 | 6 | 100 | 800.0 | 800.0 | 159.1 | 37500 | 37500 | 100.00% | 123.8 / 124.0 / 124.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 9 | 17 | S2→S3 | 7 | 100 | 800.0 | 800.0 | 96.4 | 37499 | 37499 | 100.00% | 84.1 / 84.3 / 84.5 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 10 | 19 | S2→S3 | 6 | 200 | 200.0 | 200.0 | 95.8 | 150000 | 150000 | 100.00% | 16.0 / 16.8 / 18.3 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 11 | 20 | S2→S3 | 6 | 300 | 400.0 | 400.0 | 108.6 | 75000 | 75000 | 100.00% | 96.3 / 96.5 / 96.7 | 0.1 | 0.0 | 0 | 0.00% | 0 |
