# Traffic run: rerun-dataset-11-tree-rstp-settled/prob3-heuristic-c9-on/11-heuristic-c9on-matrix, 2026-10-13 15:54

27 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **1724952 / 1724952 packets (100.00%)**
- Deadline misses: **0 (0.00% of received)**; flows with zero misses: 27 / 27

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 13 | 100.00% | 54.3 | 0.00% |
| S2 | 10 | 100.00% | 35.6 | 0.00% |
| S3 | 4 | 100.00% | 32.0 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7276524.181] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7446691.554] rms   12 max   21 freq  -6395 +/-  16 delay    23 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[1138949.211] rms   29 max   57 freq  +2239 +/-  39 delay    49 +/-   0`
- Connectivity: 27 / 27 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 0 |
| S2 | 0 | 0 | 0 |
| S3 | 0 | 0 | 48 |

Switch queue drops (`ethtool -S` Q DROP) on the 17 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S1→S2 | 7 | 500 | 200.0 | 200.0 | 45.8 | 150000 | 150000 | 100.00% | 33.5 / 33.7 / 33.9 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 2 | 2 | S3→S2 | 7 | 400 | 200.0 | 200.0 | 58.6 | 149991 | 149991 | 100.00% | 43.3 / 43.7 / 44.1 | 0.1 | 0.1 | 0 | 0.00% | 0 |
| 3 | 3 | S1→S2 | 6 | 500 | 400.0 | 400.0 | 46.5 | 75000 | 75000 | 100.00% | 34.1 / 34.3 / 34.6 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 4 | 5 | S2→S1 | 6 | 200 | 200.0 | 200.0 | 36.9 | 150000 | 150000 | 100.00% | 18.5 / 21.3 / 28.6 | 3.9 | 4.5 | 0 | 0.00% | 0 |
| 5 | 7 | S2→S1 | 6 | 300 | 800.0 | 800.0 | 39.4 | 37500 | 37500 | 100.00% | 27.1 / 27.3 / 27.5 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 6 | 8 | S3→S2 | 7 | 500 | 200.0 | 200.0 | 59.3 | 149991 | 149991 | 100.00% | 28.0 / 46.7 / 47.4 | 2.8 | 0.7 | 0 | 0.00% | 0 |
| 7 | 9 | S3→S2 | 6 | 100 | 800.0 | 800.0 | 38.2 | 37496 | 37496 | 100.00% | 23.0 / 27.1 / 27.8 | 0.7 | 0.4 | 0 | 0.00% | 0 |
| 8 | 10 | S3→S1 | 7 | 300 | 400.0 | 400.0 | 66.3 | 74996 | 74996 | 100.00% | 31.5 / 32.8 / 34.0 | 0.3 | 0.3 | 0 | 0.00% | 0 |
| 9 | 13 | S1→S3 | 7 | 300 | 800.0 | 800.0 | 66.2 | 37500 | 37500 | 100.00% | 31.7 / 32.8 / 34.0 | 0.3 | 0.3 | 0 | 0.00% | 0 |
| 10 | 15 | S2→S3 | 7 | 300 | 800.0 | 800.0 | 46.1 | 37500 | 37500 | 100.00% | 19.8 / 20.7 / 21.6 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 11 | 16 | S3→S1 | 7 | 500 | 400.0 | 400.0 | 325.1 | 74995 | 74995 | 100.00% | 44.7 / 172.5 / 299.9 | 126.8 | 253.7 | 0 | 0.00% | 0 |
| 12 | 17 | S1→S2 | 6 | 400 | 400.0 | 400.0 | 63.4 | 75000 | 75000 | 100.00% | 26.5 / 26.7 / 26.9 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 13 | 18 | S2→S3 | 7 | 500 | 800.0 | 800.0 | 54.2 | 37500 | 37500 | 100.00% | 28.1 / 28.8 / 29.9 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 14 | 19 | S3→S1 | 6 | 400 | 800.0 | 800.0 | 132.8 | 37496 | 37496 | 100.00% | 48.2 / 48.4 / 48.6 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 15 | 20 | S1→S2 | 6 | 500 | 400.0 | 400.0 | 47.1 | 75000 | 75000 | 100.00% | 34.8 / 35.0 / 35.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 16 | 23 | S2→S1 | 7 | 300 | 800.0 | 800.0 | 39.4 | 37500 | 37500 | 100.00% | 15.8 / 16.6 / 17.6 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 17 | 25 | S2→S1 | 7 | 300 | 800.0 | 800.0 | 200.0 | 37500 | 37500 | 100.00% | 15.8 / 16.6 / 17.4 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 18 | 27 | S1→S2 | 6 | 500 | 800.0 | 800.0 | 64.0 | 37500 | 37500 | 100.00% | 22.5 / 23.1 / 24.4 | 0.3 | 0.2 | 0 | 0.00% | 0 |
| 19 | 28 | S2→S1 | 7 | 400 | 800.0 | 800.0 | 49.9 | 37500 | 37500 | 100.00% | 19.4 / 21.5 / 22.2 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 20 | 35 | S2→S1 | 6 | 500 | 400.0 | 400.0 | 45.8 | 75000 | 75000 | 100.00% | 22.5 / 23.1 / 23.9 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 21 | 36 | S2→S1 | 6 | 500 | 800.0 | 800.0 | 45.8 | 37500 | 37500 | 100.00% | 22.5 / 23.1 / 23.8 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 22 | 37 | S3→S1 | 6 | 500 | 800.0 | 800.0 | 158.7 | 37496 | 37496 | 100.00% | 111.0 / 111.5 / 112.1 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 23 | 39 | S3→S1 | 7 | 500 | 400.0 | 400.0 | 249.9 | 74995 | 74995 | 100.00% | 129.4 / 130.0 / 130.8 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 24 | 46 | S1→S3 | 7 | 500 | 800.0 | 800.0 | 79.0 | 37500 | 37500 | 100.00% | 44.7 / 45.7 / 46.8 | 0.3 | 0.2 | 0 | 0.00% | 0 |
| 25 | 48 | S3→S2 | 6 | 500 | 800.0 | 800.0 | 64.3 | 37496 | 37496 | 100.00% | 28.0 / 28.7 / 29.5 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 26 | 49 | S1→S2 | 6 | 300 | 800.0 | 800.0 | 64.0 | 37500 | 37500 | 100.00% | 15.9 / 16.6 / 17.4 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 27 | 50 | S2→S1 | 7 | 400 | 800.0 | 800.0 | 107.5 | 37500 | 37500 | 100.00% | 19.1 / 19.8 / 20.6 | 0.2 | 0.2 | 0 | 0.00% | 0 |
