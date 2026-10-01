# Traffic run: heuristic-c9-off/1-matrix-c9off, 2026-10-01 16:10

10 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time, NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **1124955 / 1462500 packets (76.92%)**
- Deadline misses: **1 (0.00% of received)**; flows with zero misses: 7 / 10

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 4 | 100.00% | 40.5 | 0.00% |
| S2 | 2 | 99.99% | 12.5 | 0.00% |
| S3 | 4 | 52.63% | 26.3 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[6405595.467] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[6410863.943] rms   23 max   55 freq  -6347 +/-  31 delay    18 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[103169.405] rms   24 max   51 freq  +2841 +/-  33 delay    48 +/-   0`
- Connectivity: 8 / 10 sender routes answered ping (failed: 8, 15)

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 0 |
| S2 | 0 | 1 | 0 |
| S3 | 0 | 44 | 0 |

Switch queue drops (`ethtool -S` Q DROP) on the 27 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S3→S1 | 7 | 500 | 800.0 | 800.0 | 16.7 | 37500 | 37497 | 99.99% | 13.1 / 13.3 / 13.5 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 2 | 4 | S1→S3 | 6 | 300 | 100.0 | 100.0 | 11.7 | 300000 | 300000 | 100.00% | 8.1 / 16.0 / 39.0 | 13.0 | 15.1 | 0 | 0.00% | 0 |
| 3 | 5 | S2→S1 | 7 | 200 | 200.0 | 200.0 | 16.8 | 150000 | 149999 | 100.00% | 15.5 / 86.6 / 157.6 | 70.9 | 141.8 | 0 | 0.00% | 0 |
| 4 | 8 | S2→S3 | 6 | 100 | 800.0 | 800.0 | 12.8 | 37500 | 0 | 0.00% | – | – | – | – | – | – |
| 5 | 10 | S1→S3 | 7 | 100 | 400.0 | 400.0 | 7.5 | 75000 | 75000 | 100.00% | 67.0 / 67.2 / 67.4 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 6 | 12 | S2→S1 | 6 | 100 | 400.0 | 400.0 | 13.3 | 75000 | 75000 | 100.00% | 12.9 / 51.2 / 92.3 | 38.1 | 76.2 | 0 | 0.00% | 0 |
| 7 | 15 | S2→S3 | 6 | 400 | 100.0 | 100.0 | 24.8 | 300000 | 0 | 0.00% | – | – | – | – | – | – |
| 8 | 16 | S3→S2 | 6 | 200 | 800.0 | 800.0 | 16.8 | 37500 | 37496 | 99.99% | 12.9 / 13.5 / 14.2 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 9 | 18 | S3→S2 | 6 | 100 | 200.0 | 200.0 | 12.8 | 150000 | 149987 | 99.99% | 9.7 / 12.3 / 20.4 | 3.4 | 4.0 | 0 | 0.00% | 0 |
| 10 | 20 | S3→S1 | 6 | 200 | 100.0 | 100.0 | 9.3 | 300000 | 299976 | 99.99% | 6.6 / 18.3 / 100.3 | 29.9 | 22.7 | 1 | 0.00% | 0 |
