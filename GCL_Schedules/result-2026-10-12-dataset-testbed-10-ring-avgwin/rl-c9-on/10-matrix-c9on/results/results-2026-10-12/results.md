# Traffic run: result-2026-10-12-dataset-testbed-10-ring-avgwin/rl-c9-on/10-matrix-c9on, 2026-10-12 16:35

20 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **1012481 / 1012481 packets (100.00%)**
- Deadline misses: **30 (0.00% of received)**; flows with zero misses: 10 / 20

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 4 | 100.00% | 14.1 | 0.00% |
| S2 | 3 | 100.00% | 34.5 | 0.01% |
| S3 | 4 | 100.00% | 22.4 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7276524.181] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7362750.852] rms   13 max   24 freq  -6375 +/-  18 delay    25 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[1055007.238] rms  390 max  423 freq  +2407 +/- 104 delay    48 +/-   0`
- Connectivity: 11 / 11 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 0 |
| S2 | 0 | 0 | 0 |
| S3 | 0 | 0 | 19 |

Switch queue drops (`ethtool -S` Q DROP) on the 19 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S3→S1 | 6 | 400 | 400.0 | 400.0 | 27.9 | 74996 | 74996 | 100.00% | 9.7 / 10.2 / 10.6 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 2 | 2 | S3→S2 | None | 300 | 800.0 | 800.0 | – | 0 | – | – | – | – | – | – | – | – |
| 3 | 3 | S1→S3 | 6 | 400 | 200.0 | 200.0 | 27.9 | 150000 | 150000 | 100.00% | 12.6 / 13.0 / 105.9 | 0.6 | 0.1 | 0 | 0.00% | 0 |
| 4 | 4 | S1→S3 | None | 500 | 200.0 | 200.0 | – | 0 | – | – | – | – | – | – | – | – |
| 5 | 5 | S3→S1 | 7 | 400 | 800.0 | 800.0 | 31.1 | 37497 | 37497 | 100.00% | 18.8 / 19.0 / 19.1 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 6 | 6 | S1→S3 | None | 500 | 800.0 | 800.0 | – | 0 | – | – | – | – | – | – | – | – |
| 7 | 7 | S2→S3 | 7 | 200 | 200.0 | 200.0 | 43.0 | 150000 | 150000 | 100.00% | 30.6 / 30.9 / 31.1 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 8 | 8 | S1→S3 | None | 100 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 9 | 9 | S3→S2 | 7 | 400 | 200.0 | 200.0 | 51.0 | 149993 | 149993 | 100.00% | 38.5 / 38.9 / 301.2 | 3.8 | 0.1 | 30 | 0.02% | 0 |
| 10 | 10 | S2→S1 | 6 | 400 | 800.0 | 800.0 | 43.3 | 37500 | 37500 | 100.00% | 27.8 / 28.3 / 28.7 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 11 | 11 | S2→S3 | 7 | 200 | 400.0 | 400.0 | 43.0 | 75000 | 75000 | 100.00% | 27.6 / 28.0 / 29.0 | 0.1 | 0.2 | 0 | 0.00% | 0 |
| 12 | 12 | S1→S2 | 7 | 500 | 200.0 | 200.0 | 45.8 | 150000 | 150000 | 100.00% | 30.6 / 31.0 / 31.5 | 0.1 | 0.1 | 0 | 0.00% | 0 |
| 13 | 13 | S3→S2 | None | 100 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 14 | 14 | S2→S1 | None | 300 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 15 | 15 | S3→S1 | 6 | 300 | 400.0 | 400.0 | 26.0 | 74995 | 74995 | 100.00% | 8.1 / 8.6 / 9.0 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 16 | 16 | S3→S1 | None | 500 | 200.0 | 200.0 | – | 0 | – | – | – | – | – | – | – | – |
| 17 | 17 | S1→S2 | 6 | 400 | 800.0 | 800.0 | 43.3 | 37500 | 37500 | 100.00% | 30.8 / 31.1 / 31.4 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 18 | 18 | S1→S3 | 6 | 200 | 400.0 | 400.0 | 30.8 | 75000 | 75000 | 100.00% | 18.5 / 18.7 / 18.9 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 19 | 19 | S3→S1 | None | 200 | 800.0 | 800.0 | – | 0 | – | – | – | – | – | – | – | – |
| 20 | 20 | S2→S3 | None | 500 | 200.0 | 200.0 | – | 0 | – | – | – | – | – | – | – | – |
