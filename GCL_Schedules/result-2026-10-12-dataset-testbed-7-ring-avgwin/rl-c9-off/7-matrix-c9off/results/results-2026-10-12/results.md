# Traffic run: result-2026-10-12-dataset-testbed-7-ring-avgwin/rl-c9-off/7-matrix-c9off, 2026-10-12 15:30

20 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **1012477 / 1012477 packets (100.00%)**
- Deadline misses: **0 (0.00% of received)**; flows with zero misses: 11 / 20

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 4 | 100.00% | 33.9 | 0.00% |
| S2 | 6 | 100.00% | 55.8 | 0.00% |
| S3 | 1 | 100.00% | 61.9 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7276524.181] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7358857.925] rms    9 max   16 freq  -6491 +/-  12 delay    25 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[1051115.945] rms    6 max   12 freq  +2621 +/-   8 delay    48 +/-   0`
- Connectivity: 11 / 11 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 0 |
| S2 | 0 | 0 | 0 |
| S3 | 0 | 0 | 23 |

Switch queue drops (`ethtool -S` Q DROP) on the 19 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S1→S2 | 6 | 200 | 200.0 | 200.0 | 79.1 | 150000 | 150000 | 100.00% | 67.0 / 67.2 / 67.5 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 2 | 2 | S3→S2 | None | 200 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 3 | 3 | S2→S3 | 7 | 500 | 400.0 | 400.0 | 95.8 | 75000 | 75000 | 100.00% | 61.4 / 61.9 / 62.6 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 4 | 4 | S1→S3 | None | 100 | 800.0 | 800.0 | – | 0 | – | – | – | – | – | – | – | – |
| 5 | 5 | S1→S2 | 7 | 200 | 800.0 | 800.0 | 79.1 | 37500 | 37500 | 100.00% | 22.2 / 22.4 / 22.6 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 6 | 6 | S1→S2 | None | 300 | 200.0 | 200.0 | – | 0 | – | – | – | – | – | – | – | – |
| 7 | 7 | S2→S1 | 7 | 500 | 800.0 | 800.0 | 83.6 | 37500 | 37500 | 100.00% | 44.7 / 45.2 / 45.9 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 8 | 8 | S3→S1 | 6 | 500 | 400.0 | 400.0 | 45.8 | 74996 | 74996 | 100.00% | 33.8 / 34.0 / 34.1 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 9 | 9 | S3→S1 | 7 | 100 | 200.0 | 200.0 | 45.8 | 149992 | 149992 | 100.00% | 33.8 / 34.0 / 34.1 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 10 | 10 | S3→S2 | None | 300 | 200.0 | 200.0 | – | 0 | – | – | – | – | – | – | – | – |
| 11 | 11 | S2→S3 | None | 200 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 12 | 12 | S1→S2 | 7 | 300 | 200.0 | 200.0 | 79.1 | 150000 | 150000 | 100.00% | 67.0 / 67.2 / 67.5 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 13 | 13 | S1→S3 | None | 300 | 800.0 | 800.0 | – | 0 | – | – | – | – | – | – | – | – |
| 14 | 14 | S3→S1 | None | 500 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 15 | 15 | S1→S2 | 7 | 300 | 400.0 | 400.0 | 83.6 | 75000 | 75000 | 100.00% | 44.6 / 44.8 / 45.1 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 16 | 16 | S2→S3 | None | 400 | 800.0 | 800.0 | – | 0 | – | – | – | – | – | – | – | – |
| 17 | 17 | S1→S3 | None | 400 | 200.0 | 200.0 | – | 0 | – | – | – | – | – | – | – | – |
| 18 | 18 | S3→S1 | 6 | 300 | 400.0 | 400.0 | 46.5 | 74996 | 74996 | 100.00% | 21.5 / 28.3 / 34.8 | 6.3 | 12.6 | 0 | 0.00% | 0 |
| 19 | 19 | S1→S2 | 7 | 200 | 800.0 | 800.0 | 79.1 | 37500 | 37500 | 100.00% | 67.0 / 67.2 / 67.4 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 20 | 20 | S3→S2 | 6 | 100 | 200.0 | 200.0 | 95.8 | 149993 | 149993 | 100.00% | 43.8 / 44.0 / 44.3 | 0.1 | 0.0 | 0 | 0.00% | 0 |
