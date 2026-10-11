# Traffic run: result-2026-10-10-dataset-testbed-4-saf/heuristic-c9-on/4-matrix-c9on, 2026-10-10 17:58

11 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **1012440 / 1012448 packets (100.00%)**
- Deadline misses: **0 (0.00% of received)**; flows with zero misses: 11 / 11

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 1 | 100.00% | 27.5 | 0.00% |
| S2 | 4 | 100.00% | 30.5 | 0.00% |
| S3 | 6 | 100.00% | 38.9 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7192691.373] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7194893.075] rms    8 max   13 freq  -6214 +/-  11 delay    23 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[887149.729] rms   36 max   79 freq  +3011 +/-  50 delay    49 +/-   0`
- Connectivity: 11 / 11 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 28 |
| S2 | 0 | 0 | 0 |
| S3 | 0 | 8 | 24 |

Switch queue drops (`ethtool -S` Q DROP) on the 17 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S3→S2 | 7 | 300 | 400.0 | 400.0 | 46.2 | 74993 | 74991 | 100.00% | 34.0 / 34.3 / 156.6 | 0.5 | 0.0 | 0 | 0.00% | 0 |
| 2 | 3 | S2→S3 | 7 | 100 | 400.0 | 400.0 | 42.0 | 75000 | 75000 | 100.00% | 21.3 / 21.5 / 21.7 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 3 | 6 | S1→S3 | 6 | 300 | 800.0 | 800.0 | 67.0 | 37498 | 37498 | 100.00% | 40.0 / 41.1 / 42.0 | 0.3 | 0.2 | 0 | 0.00% | 0 |
| 4 | 8 | S2→S3 | 7 | 500 | 200.0 | 200.0 | 54.2 | 150000 | 150000 | 100.00% | 42.1 / 42.3 / 42.5 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 5 | 9 | S1→S3 | 7 | 400 | 800.0 | 800.0 | 74.0 | 37498 | 37498 | 100.00% | 61.9 / 62.1 / 62.3 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 6 | 10 | S3→S2 | 6 | 400 | 400.0 | 400.0 | 51.0 | 74993 | 74991 | 100.00% | 38.9 / 39.1 / 39.3 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 7 | 13 | S1→S2 | 6 | 400 | 200.0 | 200.0 | 43.3 | 149992 | 149992 | 100.00% | 22.2 / 22.9 / 37.9 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 8 | 14 | S3→S2 | 6 | 500 | 200.0 | 200.0 | 56.1 | 149990 | 149986 | 100.00% | 31.2 / 31.9 / 32.7 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 9 | 18 | S2→S1 | 6 | 300 | 800.0 | 800.0 | 39.4 | 37500 | 37500 | 100.00% | 27.3 / 27.5 / 27.7 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 10 | 19 | S2→S3 | 6 | 500 | 400.0 | 400.0 | 54.2 | 75000 | 75000 | 100.00% | 28.0 / 28.7 / 29.6 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 11 | 20 | S1→S3 | 6 | 100 | 200.0 | 200.0 | 54.8 | 149984 | 149984 | 100.00% | 42.7 / 42.9 / 43.1 | 0.1 | 0.0 | 0 | 0.00% | 0 |
