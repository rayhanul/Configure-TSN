# Traffic run: result-2026-10-12-dataset-testbed-9-ring-avgwin/heuristic-c9-off/9-matrix-c9off, 2026-10-12 16:08

11 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **862479 / 862479 packets (100.00%)**
- Deadline misses: **0 (0.00% of received)**; flows with zero misses: 11 / 11

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 6 | 100.00% | 30.8 | 0.00% |
| S2 | 2 | 100.00% | 56.4 | 0.00% |
| S3 | 3 | 100.00% | 35.8 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7276524.181] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7361094.254] port 1 (enp1s0): assuming the grand master role`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[1053352.770] rms    6 max   11 freq  +2171 +/-   8 delay    50 +/-   0`
- Connectivity: 11 / 11 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 2 |
| S2 | 0 | 0 | 0 |
| S3 | 0 | 0 | 19 |

Switch queue drops (`ethtool -S` Q DROP) on the 19 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S3→S1 | 6 | 200 | 800.0 | 800.0 | 54.5 | 37497 | 37497 | 100.00% | 42.2 / 42.3 / 42.5 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 2 | 4 | S3→S1 | 7 | 100 | 400.0 | 400.0 | 45.8 | 74997 | 74997 | 100.00% | 19.2 / 19.5 / 19.9 | 0.1 | 0.2 | 0 | 0.00% | 0 |
| 3 | 6 | S2→S3 | 7 | 100 | 200.0 | 200.0 | 95.8 | 150000 | 150000 | 100.00% | 54.8 / 55.3 / 57.1 | 0.2 | 0.1 | 0 | 0.00% | 0 |
| 4 | 7 | S2→S1 | 7 | 100 | 400.0 | 400.0 | 79.1 | 75000 | 75000 | 100.00% | 38.0 / 38.6 / 39.2 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 5 | 8 | S2→S3 | 6 | 400 | 800.0 | 800.0 | 95.8 | 37500 | 37500 | 100.00% | 47.5 / 48.3 / 49.0 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 6 | 9 | S3→S2 | 7 | 500 | 800.0 | 800.0 | 95.8 | 37497 | 37497 | 100.00% | 72.3 / 72.6 / 73.0 | 0.1 | 0.1 | 0 | 0.00% | 0 |
| 7 | 10 | S3→S1 | 7 | 400 | 200.0 | 200.0 | 45.8 | 149990 | 149990 | 100.00% | 33.5 / 33.7 / 33.9 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 8 | 12 | S1→S2 | 7 | 200 | 800.0 | 800.0 | 79.1 | 37500 | 37500 | 100.00% | 39.7 / 40.2 / 40.9 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 9 | 14 | S1→S3 | 6 | 400 | 200.0 | 200.0 | 45.8 | 149998 | 149998 | 100.00% | 9.7 / 13.1 / 22.3 | 5.1 | 6.0 | 0 | 0.00% | 0 |
| 10 | 16 | S2→S1 | 7 | 500 | 400.0 | 400.0 | 79.8 | 75000 | 75000 | 100.00% | 22.5 / 23.1 / 23.8 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 11 | 20 | S2→S1 | 6 | 200 | 800.0 | 800.0 | 79.1 | 37500 | 37500 | 100.00% | 30.0 / 30.2 / 30.4 | 0.1 | 0.0 | 0 | 0.00% | 0 |
