# Traffic run: rerun-dataset-11-tree-rstp-settled/rl-c9-on/11-matrix-c9on, 2026-10-13 15:49

20 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **937466 / 937467 packets (100.00%)**
- Deadline misses: **0 (0.00% of received)**; flows with zero misses: 10 / 20

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 3 | 100.00% | 24.2 | 0.00% |
| S2 | 6 | 100.00% | 38.7 | 0.00% |
| S3 | 1 | 100.00% | 28.8 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7276524.181] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7446350.175] rms   25 max   66 freq  -6378 +/-  34 delay    24 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[1138607.711] rms   39 max   52 freq  +2279 +/-  53 delay    48 +/-   0`
- Connectivity: 10 / 10 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 0 |
| S2 | 0 | 0 | 0 |
| S3 | 0 | 1 | 33 |

Switch queue drops (`ethtool -S` Q DROP) on the 17 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S1→S2 | 7 | 500 | 200.0 | 200.0 | 45.8 | 150000 | 150000 | 100.00% | 33.5 / 33.7 / 33.9 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 2 | 2 | S3→S2 | 7 | 400 | 200.0 | 200.0 | 58.6 | 149987 | 149986 | 100.00% | 43.2 / 43.7 / 44.1 | 0.1 | 0.1 | 0 | 0.00% | 0 |
| 3 | 3 | S1→S2 | 6 | 500 | 400.0 | 400.0 | 46.5 | 75000 | 75000 | 100.00% | 34.1 / 34.3 / 34.5 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 4 | 4 | S2→S3 | None | 500 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 5 | 5 | S2→S1 | 6 | 200 | 200.0 | 200.0 | 36.9 | 150000 | 150000 | 100.00% | 18.5 / 19.1 / 19.8 | 0.2 | 0.1 | 0 | 0.00% | 0 |
| 6 | 6 | S3→S1 | None | 200 | 200.0 | 200.0 | – | 0 | – | – | – | – | – | – | – | – |
| 7 | 7 | S2→S1 | 6 | 300 | 800.0 | 800.0 | 39.4 | 37500 | 37500 | 100.00% | 27.1 / 27.3 / 27.5 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 8 | 8 | S3→S2 | 7 | 500 | 200.0 | 200.0 | 59.3 | 149988 | 149988 | 100.00% | 28.0 / 46.6 / 47.3 | 3.0 | 0.8 | 0 | 0.00% | 0 |
| 9 | 9 | S3→S2 | 6 | 100 | 800.0 | 800.0 | 38.2 | 37498 | 37498 | 100.00% | 23.0 / 23.4 / 23.8 | 0.1 | 0.1 | 0 | 0.00% | 0 |
| 10 | 10 | S3→S1 | 7 | 300 | 400.0 | 400.0 | 66.3 | 74994 | 74994 | 100.00% | 31.6 / 32.8 / 34.1 | 0.3 | 0.3 | 0 | 0.00% | 0 |
| 11 | 11 | S1→S3 | None | 100 | 200.0 | 200.0 | – | 0 | – | – | – | – | – | – | – | – |
| 12 | 12 | S2→S3 | None | 300 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 13 | 13 | S1→S3 | None | 300 | 800.0 | 800.0 | – | 0 | – | – | – | – | – | – | – | – |
| 14 | 14 | S3→S1 | None | 400 | 200.0 | 200.0 | – | 0 | – | – | – | – | – | – | – | – |
| 15 | 15 | S2→S3 | None | 300 | 800.0 | 800.0 | – | 0 | – | – | – | – | – | – | – | – |
| 16 | 16 | S3→S1 | None | 500 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 17 | 17 | S1→S2 | None | 400 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 18 | 18 | S2→S3 | 7 | 500 | 800.0 | 800.0 | 54.2 | 37500 | 37500 | 100.00% | 28.0 / 28.8 / 29.6 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 19 | 19 | S3→S1 | None | 400 | 800.0 | 800.0 | – | 0 | – | – | – | – | – | – | – | – |
| 20 | 20 | S1→S2 | 6 | 500 | 400.0 | 400.0 | 47.1 | 75000 | 75000 | 100.00% | 34.8 / 35.0 / 35.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
