# Traffic run: rerun-dataset-11-tree-rstp-settled/heuristic-c9-off/11-matrix-c9off, 2026-10-13 15:40

10 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **937422 / 937438 packets (100.00%)**
- Deadline misses: **0 (0.00% of received)**; flows with zero misses: 10 / 10

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 3 | 100.00% | 65.7 | 0.00% |
| S2 | 6 | 100.00% | 61.3 | 0.00% |
| S3 | 1 | 100.00% | 28.8 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7276524.181] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7445859.436] rms   13 max   20 freq  -6398 +/-  16 delay    25 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[1138116.842] rms   35 max   59 freq  +2372 +/-  48 delay    47 +/-   0`
- Connectivity: 10 / 10 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 0 |
| S2 | 0 | 0 | 0 |
| S3 | 0 | 16 | 62 |

Switch queue drops (`ethtool -S` Q DROP) on the 17 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S1→S2 | 6 | 500 | 200.0 | 200.0 | 79.1 | 150000 | 150000 | 100.00% | 66.8 / 67.0 / 70.4 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 2 | 2 | S3→S2 | 6 | 400 | 200.0 | 200.0 | 95.8 | 149977 | 149971 | 100.00% | 66.8 / 71.1 / 71.3 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 3 | 3 | S1→S2 | 7 | 500 | 400.0 | 400.0 | 83.6 | 75000 | 75000 | 100.00% | 71.2 / 71.5 / 71.7 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 4 | 5 | S2→S1 | 7 | 200 | 200.0 | 200.0 | 79.1 | 150000 | 150000 | 100.00% | 53.2 / 53.6 / 54.0 | 0.1 | 0.1 | 0 | 0.00% | 0 |
| 5 | 7 | S2→S1 | 7 | 300 | 800.0 | 800.0 | 79.1 | 37500 | 37500 | 100.00% | 28.4 / 29.2 / 29.9 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 6 | 8 | S3→S2 | 6 | 500 | 200.0 | 200.0 | 96.4 | 149978 | 149972 | 100.00% | 47.8 / 49.5 / 49.7 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 7 | 9 | S3→S2 | 7 | 100 | 800.0 | 800.0 | 95.8 | 37494 | 37493 | 100.00% | 46.9 / 47.2 / 47.5 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 8 | 10 | S3→S1 | 7 | 300 | 400.0 | 400.0 | 145.7 | 74989 | 74986 | 100.00% | 107.7 / 108.3 / 108.9 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 9 | 18 | S2→S3 | 7 | 500 | 800.0 | 800.0 | 95.8 | 37500 | 37500 | 100.00% | 28.1 / 28.8 / 29.6 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 10 | 20 | S1→S2 | 7 | 500 | 400.0 | 400.0 | 84.2 | 75000 | 75000 | 100.00% | 50.4 / 50.7 / 50.9 | 0.1 | 0.0 | 0 | 0.00% | 0 |
