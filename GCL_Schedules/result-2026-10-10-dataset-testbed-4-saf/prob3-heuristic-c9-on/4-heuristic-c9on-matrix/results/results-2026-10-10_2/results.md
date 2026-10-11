# Traffic run: result-2026-10-10-dataset-testbed-4-saf/prob3-heuristic-c9-on/4-heuristic-c9on-matrix, 2026-10-10 18:26

27 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **1912361 / 1912365 packets (100.00%)**
- Deadline misses: **0 (0.00% of received)**; flows with zero misses: 27 / 27

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 10 | 100.00% | 59.8 | 0.00% |
| S2 | 11 | 100.00% | 28.5 | 0.00% |
| S3 | 6 | 100.00% | 38.7 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7192691.373] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7196588.414] rms   12 max   26 freq  -6201 +/-  14 delay    25 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[888845.819] rms   32 max   60 freq  +3032 +/-  44 delay    49 +/-   0`
- Connectivity: 27 / 27 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 92 |
| S2 | 0 | 0 | 0 |
| S3 | 0 | 4 | 43 |

Switch queue drops (`ethtool -S` Q DROP) on the 17 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S3→S2 | 7 | 300 | 400.0 | 400.0 | 46.2 | 74996 | 74996 | 100.00% | 33.8 / 34.0 / 34.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 2 | 2 | S1→S2 | 6 | 300 | 400.0 | 400.0 | 39.4 | 74990 | 74990 | 100.00% | 15.9 / 16.6 / 17.4 | 0.2 | 0.3 | 0 | 0.00% | 0 |
| 3 | 3 | S2→S3 | 7 | 100 | 400.0 | 400.0 | 42.0 | 75000 | 75000 | 100.00% | 21.0 / 21.2 / 21.4 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 4 | 4 | S3→S2 | 7 | 400 | 800.0 | 800.0 | 207.7 | 37497 | 37496 | 100.00% | 23.8 / 24.7 / 25.6 | 0.3 | 0.2 | 0 | 0.00% | 0 |
| 5 | 5 | S3→S1 | 6 | 200 | 400.0 | 400.0 | 65.6 | 74995 | 74995 | 100.00% | 32.4 / 36.8 / 40.6 | 3.7 | 7.3 | 0 | 0.00% | 0 |
| 6 | 6 | S1→S3 | 6 | 300 | 800.0 | 800.0 | 67.0 | 37495 | 37495 | 100.00% | 39.9 / 40.8 / 41.8 | 0.3 | 0.2 | 0 | 0.00% | 0 |
| 7 | 8 | S2→S3 | 7 | 500 | 200.0 | 200.0 | 54.2 | 150000 | 150000 | 100.00% | 41.8 / 42.0 / 42.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 8 | 9 | S1→S3 | 7 | 400 | 800.0 | 800.0 | 74.0 | 37496 | 37496 | 100.00% | 61.7 / 61.9 / 62.1 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 9 | 10 | S3→S2 | 6 | 400 | 400.0 | 400.0 | 51.0 | 74995 | 74995 | 100.00% | 38.6 / 38.8 / 39.0 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 10 | 11 | S2→S1 | 6 | 200 | 800.0 | 800.0 | 36.8 | 37500 | 37500 | 100.00% | 12.8 / 13.5 / 17.5 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 11 | 13 | S1→S2 | 6 | 400 | 200.0 | 200.0 | 43.3 | 149980 | 149980 | 100.00% | 21.9 / 22.7 / 36.9 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 12 | 14 | S3→S2 | 6 | 500 | 200.0 | 200.0 | 56.1 | 149992 | 149991 | 100.00% | 30.9 / 31.6 / 33.2 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 13 | 15 | S3→S2 | 7 | 300 | 200.0 | 200.0 | 46.1 | 149991 | 149990 | 100.00% | 19.8 / 29.0 / 33.1 | 4.8 | 6.1 | 0 | 0.00% | 0 |
| 14 | 18 | S2→S1 | 6 | 300 | 800.0 | 800.0 | 39.4 | 37500 | 37500 | 100.00% | 27.1 / 27.3 / 27.5 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 15 | 19 | S2→S3 | 6 | 500 | 400.0 | 400.0 | 54.2 | 75000 | 75000 | 100.00% | 28.1 / 28.7 / 29.5 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 16 | 20 | S1→S3 | 6 | 100 | 200.0 | 200.0 | 54.8 | 149980 | 149980 | 100.00% | 42.5 / 42.7 / 42.9 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 17 | 21 | S2→S1 | 6 | 400 | 800.0 | 800.0 | 47.0 | 37500 | 37500 | 100.00% | 19.1 / 21.5 / 26.9 | 2.9 | 2.2 | 0 | 0.00% | 0 |
| 18 | 22 | S2→S1 | 6 | 300 | 800.0 | 800.0 | 47.0 | 37500 | 37500 | 100.00% | 16.4 / 20.6 / 21.4 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 19 | 23 | S2→S1 | 6 | 300 | 800.0 | 800.0 | 40.6 | 37500 | 37500 | 100.00% | 15.9 / 16.6 / 17.4 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 20 | 24 | S3→S1 | 7 | 300 | 800.0 | 800.0 | 420.2 | 37498 | 37498 | 100.00% | 399.3 / 400.0 / 408.2 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 21 | 29 | S1→S2 | 6 | 100 | 400.0 | 400.0 | 39.4 | 74988 | 74988 | 100.00% | 9.6 / 10.3 / 11.1 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 22 | 30 | S1→S2 | 6 | 500 | 400.0 | 400.0 | 45.8 | 74988 | 74988 | 100.00% | 22.5 / 23.1 / 23.8 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 23 | 35 | S3→S1 | 6 | 400 | 400.0 | 400.0 | 161.6 | 74996 | 74995 | 100.00% | 38.1 / 39.9 / 41.4 | 0.7 | 1.4 | 0 | 0.00% | 0 |
| 24 | 42 | S1→S2 | 7 | 200 | 800.0 | 800.0 | 693.8 | 37495 | 37495 | 100.00% | 91.7 / 91.9 / 92.1 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 25 | 45 | S3→S1 | 6 | 500 | 800.0 | 800.0 | 111.4 | 37497 | 37497 | 100.00% | 44.7 / 48.0 / 49.7 | 1.6 | 1.2 | 0 | 0.00% | 0 |
| 26 | 48 | S1→S2 | 6 | 300 | 800.0 | 800.0 | 39.4 | 37496 | 37496 | 100.00% | 15.9 / 16.6 / 17.4 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 27 | 50 | S2→S1 | 7 | 300 | 800.0 | 800.0 | 500.2 | 37500 | 37500 | 100.00% | 15.9 / 16.6 / 17.4 | 0.2 | 0.2 | 0 | 0.00% | 0 |
