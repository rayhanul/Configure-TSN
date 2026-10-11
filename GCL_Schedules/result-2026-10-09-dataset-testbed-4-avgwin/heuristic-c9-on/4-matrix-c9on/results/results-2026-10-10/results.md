# Traffic run: result-2026-10-09-dataset-testbed-4-avgwin/heuristic-c9-on/4-matrix-c9on, 2026-10-10 09:22

11 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **1012475 / 1012500 packets (100.00%)**
- Deadline misses: **1 (0.00% of received)**; flows with zero misses: 10 / 11

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 1 | 100.00% | 16.6 | 0.00% |
| S2 | 4 | 100.00% | 24.7 | 0.00% |
| S3 | 6 | 100.00% | 40.2 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7160963.398] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7163951.245] rms   14 max   29 freq  -6175 +/-  19 delay    21 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[856208.276] rms   33 max   87 freq  +3004 +/-  43 delay    47 +/-   0`
- Connectivity: 11 / 11 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 0 |
| S2 | 0 | 5 | 0 |
| S3 | 0 | 20 | 0 |

Switch queue drops (`ethtool -S` Q DROP) on the 17 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S3→S2 | 6 | 300 | 400.0 | 400.0 | 33.4 | 75000 | 74996 | 99.99% | 21.0 / 21.2 / 46.1 | 0.1 | 0.1 | 0 | 0.00% | 0 |
| 2 | 3 | S2→S3 | 7 | 100 | 400.0 | 400.0 | 33.4 | 75000 | 74998 | 100.00% | 21.4 / 25.4 / 26.9 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 3 | 6 | S1→S3 | 7 | 300 | 800.0 | 800.0 | 46.8 | 37500 | 37500 | 100.00% | 34.5 / 34.7 / 35.1 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 4 | 8 | S2→S3 | 7 | 500 | 200.0 | 200.0 | 33.4 | 150000 | 149999 | 100.00% | 28.1 / 52.6 / 60.6 | 6.4 | 12.8 | 0 | 0.00% | 0 |
| 5 | 9 | S1→S3 | 6 | 400 | 800.0 | 800.0 | 45.8 | 37500 | 37500 | 100.00% | 39.0 / 43.8 / 44.7 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 6 | 10 | S3→S2 | 6 | 400 | 400.0 | 400.0 | 33.4 | 75000 | 74995 | 99.99% | 23.8 / 24.7 / 26.7 | 0.3 | 0.3 | 0 | 0.00% | 0 |
| 7 | 13 | S1→S2 | 7 | 400 | 200.0 | 200.0 | 29.2 | 150000 | 150000 | 100.00% | 19.1 / 19.8 / 20.6 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 8 | 14 | S3→S2 | 7 | 500 | 200.0 | 200.0 | 42.0 | 150000 | 149989 | 99.99% | 31.0 / 31.4 / 31.7 | 0.1 | 0.1 | 0 | 0.00% | 0 |
| 9 | 18 | S2→S1 | 7 | 300 | 800.0 | 800.0 | 29.2 | 37500 | 37499 | 100.00% | 15.8 / 16.6 / 28.2 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 10 | 19 | S2→S3 | 6 | 500 | 400.0 | 400.0 | 34.0 | 75000 | 74999 | 100.00% | 28.1 / 46.7 / 428.0 | 18.0 | 35.9 | 1 | 0.00% | 0 |
| 11 | 20 | S1→S3 | 7 | 100 | 200.0 | 200.0 | 46.2 | 150000 | 150000 | 100.00% | 25.4 / 32.3 / 39.8 | 5.9 | 11.8 | 0 | 0.00% | 0 |
