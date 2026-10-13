# Traffic run: result-2026-10-12-dataset-testbed-10-ring-avgwin/heuristic-c9-off/10-matrix-c9off, 2026-10-12 16:29

11 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **1012480 / 1012480 packets (100.00%)**
- Deadline misses: **0 (0.00% of received)**; flows with zero misses: 11 / 11

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 4 | 100.00% | 29.1 | 0.00% |
| S2 | 3 | 100.00% | 66.1 | 0.00% |
| S3 | 4 | 100.00% | 34.7 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7276524.181] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7362370.336] rms   29 max   76 freq  -6364 +/-  38 delay    24 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[1054627.104] rms    8 max   14 freq  +2198 +/-  10 delay    49 +/-   0`
- Connectivity: 11 / 11 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 0 |
| S2 | 0 | 0 | 1 |
| S3 | 0 | 0 | 19 |

Switch queue drops (`ethtool -S` Q DROP) on the 19 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S3→S1 | 7 | 400 | 400.0 | 400.0 | 45.8 | 74997 | 74997 | 100.00% | 33.8 / 33.9 / 34.1 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 2 | 3 | S1→S3 | 6 | 400 | 200.0 | 200.0 | 45.8 | 150000 | 150000 | 100.00% | 9.7 / 13.2 / 25.9 | 5.2 | 6.1 | 0 | 0.00% | 0 |
| 3 | 5 | S3→S1 | 7 | 400 | 800.0 | 800.0 | 45.8 | 37498 | 37498 | 100.00% | 9.7 / 10.2 / 10.6 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 4 | 7 | S2→S3 | 7 | 200 | 200.0 | 200.0 | 108.6 | 149999 | 149999 | 100.00% | 63.4 / 63.9 / 65.9 | 0.2 | 0.1 | 0 | 0.00% | 0 |
| 5 | 9 | S3→S2 | 7 | 400 | 200.0 | 200.0 | 95.8 | 149990 | 149990 | 100.00% | 59.7 / 60.3 / 60.9 | 0.2 | 0.1 | 0 | 0.00% | 0 |
| 6 | 10 | S2→S1 | 6 | 400 | 800.0 | 800.0 | 83.6 | 37500 | 37500 | 100.00% | 71.5 / 71.7 / 71.9 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 7 | 11 | S2→S3 | 6 | 200 | 400.0 | 400.0 | 96.4 | 75000 | 75000 | 100.00% | 17.1 / 19.8 / 59.2 | 8.8 | 3.7 | 0 | 0.00% | 0 |
| 8 | 12 | S1→S2 | 6 | 500 | 200.0 | 200.0 | 83.6 | 150000 | 150000 | 100.00% | 71.5 / 71.7 / 71.9 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 9 | 15 | S3→S1 | 7 | 300 | 400.0 | 400.0 | 45.8 | 74996 | 74996 | 100.00% | 12.2 / 12.3 / 12.5 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 10 | 17 | S1→S2 | 7 | 400 | 800.0 | 800.0 | 79.1 | 37500 | 37500 | 100.00% | 67.0 / 67.2 / 67.4 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 11 | 18 | S1→S3 | 6 | 200 | 400.0 | 400.0 | 45.8 | 75000 | 75000 | 100.00% | 33.7 / 34.0 / 36.0 | 0.4 | 0.2 | 0 | 0.00% | 0 |
