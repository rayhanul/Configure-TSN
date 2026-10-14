# Traffic run: rerun-dataset-12-tree-quiet60/rl-c9-off/12-matrix-c9off, 2026-10-13 15:17

20 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **937411 / 937424 packets (100.00%)**
- Deadline misses: **0 (0.00% of received)**; flows with zero misses: 11 / 20

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 3 | 100.00% | 31.3 | 0.00% |
| S2 | 4 | 100.00% | 52.1 | 0.00% |
| S3 | 4 | 100.00% | 92.4 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7276524.181] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7444465.956] rms   10 max   15 freq  -6405 +/-  13 delay    24 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[1136722.870] rms   58 max   92 freq  +2278 +/-  79 delay    49 +/-   0`
- Connectivity: 11 / 11 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 31 |
| S2 | 0 | 0 | 0 |
| S3 | 0 | 13 | 45 |

Switch queue drops (`ethtool -S` Q DROP) on the 17 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S1→S2 | None | 400 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 2 | 2 | S1→S2 | 7 | 400 | 200.0 | 200.0 | 79.1 | 149991 | 149991 | 100.00% | 55.0 / 55.5 / 56.7 | 0.3 | 0.2 | 0 | 0.00% | 0 |
| 3 | 3 | S3→S1 | None | 200 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 4 | 4 | S1→S3 | 7 | 300 | 800.0 | 800.0 | 145.7 | 37498 | 37498 | 100.00% | 84.0 / 84.2 / 84.4 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 5 | 5 | S3→S2 | 7 | 100 | 200.0 | 200.0 | 95.8 | 149975 | 149967 | 99.99% | 55.0 / 58.3 / 59.7 | 1.2 | 0.6 | 0 | 0.00% | 0 |
| 6 | 6 | S1→S3 | None | 300 | 800.0 | 800.0 | – | 0 | – | – | – | – | – | – | – | – |
| 7 | 7 | S3→S1 | 6 | 500 | 800.0 | 800.0 | 145.7 | 37493 | 37492 | 100.00% | 78.0 / 78.8 / 79.7 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 8 | 8 | S2→S1 | 6 | 300 | 200.0 | 200.0 | 79.1 | 150000 | 150000 | 100.00% | 15.9 / 16.6 / 17.4 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 9 | 9 | S3→S2 | 6 | 200 | 400.0 | 400.0 | 95.8 | 74987 | 74983 | 99.99% | 71.2 / 71.4 / 71.6 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 10 | 10 | S1→S3 | None | 500 | 200.0 | 200.0 | – | 0 | – | – | – | – | – | – | – | – |
| 11 | 11 | S2→S1 | 7 | 300 | 800.0 | 800.0 | 79.1 | 37500 | 37500 | 100.00% | 42.0 / 42.3 / 42.5 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 12 | 12 | S1→S3 | 7 | 500 | 200.0 | 200.0 | 146.0 | 149988 | 149988 | 100.00% | 56.5 / 89.4 / 134.3 | 33.3 | 64.2 | 0 | 0.00% | 0 |
| 13 | 13 | S2→S3 | None | 100 | 800.0 | 800.0 | – | 0 | – | – | – | – | – | – | – | – |
| 14 | 14 | S1→S2 | 7 | 200 | 400.0 | 400.0 | 83.6 | 74994 | 74994 | 100.00% | 12.8 / 13.5 / 14.2 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 15 | 15 | S2→S3 | None | 500 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 16 | 16 | S3→S2 | None | 400 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 17 | 17 | S1→S2 | None | 300 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 18 | 18 | S2→S3 | 6 | 300 | 800.0 | 800.0 | 95.8 | 37500 | 37500 | 100.00% | 83.7 / 83.9 / 84.1 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 19 | 19 | S1→S3 | 6 | 400 | 800.0 | 800.0 | 145.7 | 37498 | 37498 | 100.00% | 121.1 / 121.3 / 121.5 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 20 | 20 | S2→S3 | None | 200 | 200.0 | 200.0 | – | 0 | – | – | – | – | – | – | – | – |
