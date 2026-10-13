# Traffic run: result-2026-10-12-dataset-testbed-7-ring-avgwin/rl-c9-on/7-matrix-c9on, 2026-10-12 15:32

20 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **1012422 / 1012422 packets (100.00%)**
- Deadline misses: **0 (0.00% of received)**; flows with zero misses: 11 / 20

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 4 | 100.00% | 12.8 | 0.00% |
| S2 | 6 | 100.00% | 25.5 | 0.00% |
| S3 | 1 | 100.00% | 42.3 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7276524.181] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7358977.205] rms    7 max   15 freq  -6462 +/-  10 delay    24 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[1051235.099] rms   29 max   72 freq  +2509 +/-  40 delay    47 +/-   0`
- Connectivity: 11 / 11 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 44 |
| S2 | 0 | 0 | 0 |
| S3 | 0 | 0 | 34 |

Switch queue drops (`ethtool -S` Q DROP) on the 19 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S1→S2 | 7 | 200 | 200.0 | 200.0 | 36.9 | 149987 | 149987 | 100.00% | 24.8 / 25.0 / 25.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 2 | 2 | S3→S2 | None | 200 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 3 | 3 | S2→S3 | 7 | 500 | 400.0 | 400.0 | 54.2 | 75000 | 75000 | 100.00% | 42.1 / 42.3 / 42.5 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 4 | 4 | S1→S3 | None | 100 | 800.0 | 800.0 | – | 0 | – | – | – | – | – | – | – | – |
| 5 | 5 | S1→S2 | 7 | 200 | 800.0 | 800.0 | 36.9 | 37497 | 37497 | 100.00% | 24.8 / 25.0 / 25.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 6 | 6 | S1→S2 | None | 300 | 200.0 | 200.0 | – | 0 | – | – | – | – | – | – | – | – |
| 7 | 7 | S2→S1 | 6 | 500 | 800.0 | 800.0 | 45.8 | 37500 | 37500 | 100.00% | 22.5 / 23.1 / 23.8 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 8 | 8 | S3→S1 | 7 | 500 | 400.0 | 400.0 | 33.7 | 74994 | 74994 | 100.00% | 14.2 / 18.2 / 22.0 | 3.6 | 7.2 | 0 | 0.00% | 0 |
| 9 | 9 | S3→S1 | 7 | 100 | 200.0 | 200.0 | 22.8 | 149988 | 149988 | 100.00% | 5.0 / 6.8 / 29.8 | 2.4 | 2.8 | 0 | 0.00% | 0 |
| 10 | 10 | S3→S2 | None | 300 | 200.0 | 200.0 | – | 0 | – | – | – | – | – | – | – | – |
| 11 | 11 | S2→S3 | None | 200 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 12 | 12 | S1→S2 | 6 | 300 | 200.0 | 200.0 | 51.0 | 149981 | 149981 | 100.00% | 26.1 / 27.2 / 27.4 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 13 | 13 | S1→S3 | None | 300 | 800.0 | 800.0 | – | 0 | – | – | – | – | – | – | – | – |
| 14 | 14 | S3→S1 | None | 500 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 15 | 15 | S1→S2 | 6 | 300 | 400.0 | 400.0 | 39.4 | 74993 | 74993 | 100.00% | 21.6 / 22.2 / 22.8 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 16 | 16 | S2→S3 | None | 400 | 800.0 | 800.0 | – | 0 | – | – | – | – | – | – | – | – |
| 17 | 17 | S1→S3 | None | 400 | 200.0 | 200.0 | – | 0 | – | – | – | – | – | – | – | – |
| 18 | 18 | S3→S1 | 6 | 300 | 400.0 | 400.0 | 26.0 | 74995 | 74995 | 100.00% | 13.9 / 14.1 / 14.3 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 19 | 19 | S1→S2 | 6 | 200 | 800.0 | 800.0 | 36.9 | 37498 | 37498 | 100.00% | 24.8 / 25.0 / 25.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 20 | 20 | S3→S2 | 6 | 100 | 200.0 | 200.0 | 38.2 | 149989 | 149989 | 100.00% | 26.1 / 26.3 / 26.5 | 0.1 | 0.0 | 0 | 0.00% | 0 |
