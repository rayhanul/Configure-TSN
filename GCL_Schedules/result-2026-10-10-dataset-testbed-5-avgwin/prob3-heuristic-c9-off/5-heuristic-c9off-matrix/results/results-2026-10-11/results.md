# Traffic run: result-2026-10-10-dataset-testbed-5-avgwin/prob3-heuristic-c9-off/5-heuristic-c9off-matrix, 2026-10-11 00:31

24 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **1499951 / 1499951 packets (100.00%)**
- Deadline misses: **0 (0.00% of received)**; flows with zero misses: 24 / 24

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 7 | 100.00% | 78.8 | 0.00% |
| S2 | 6 | 100.00% | 60.7 | 0.00% |
| S3 | 11 | 100.00% | 78.9 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7192691.373] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7218479.212] rms    6 max   13 freq  -6210 +/-   8 delay    25 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[910736.618] rms   41 max   69 freq  +2968 +/-  53 delay    48 +/-   0`
- Connectivity: 24 / 24 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 5 |
| S2 | 0 | 0 | 0 |
| S3 | 0 | 0 | 44 |

Switch queue drops (`ethtool -S` Q DROP) on the 17 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S3→S1 | 6 | 200 | 800.0 | 800.0 | 412.5 | 37496 | 37496 | 100.00% | 25.5 / 26.5 / 310.8 | 1.5 | 0.3 | 0 | 0.00% | 0 |
| 2 | 2 | S2→S3 | 6 | 300 | 200.0 | 200.0 | 95.8 | 150000 | 150000 | 100.00% | 19.8 / 20.8 / 22.0 | 0.3 | 0.3 | 0 | 0.00% | 0 |
| 3 | 3 | S1→S2 | 6 | 100 | 800.0 | 800.0 | 84.2 | 37499 | 37499 | 100.00% | 49.6 / 49.8 / 50.1 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 4 | 4 | S1→S3 | 7 | 300 | 800.0 | 800.0 | 429.1 | 37499 | 37499 | 100.00% | 330.2 / 330.4 / 330.6 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 5 | 5 | S2→S3 | 7 | 100 | 800.0 | 800.0 | 95.8 | 37500 | 37500 | 100.00% | 83.4 / 83.6 / 83.8 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 6 | 6 | S2→S3 | 7 | 200 | 400.0 | 400.0 | 320.6 | 75000 | 75000 | 100.00% | 71.6 / 88.4 / 105.3 | 16.6 | 33.3 | 0 | 0.00% | 0 |
| 7 | 9 | S2→S1 | 7 | 500 | 400.0 | 400.0 | 79.1 | 75000 | 75000 | 100.00% | 33.3 / 34.0 / 34.8 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 8 | 10 | S1→S2 | 7 | 500 | 200.0 | 200.0 | 79.1 | 150000 | 150000 | 100.00% | 66.8 / 67.0 / 67.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 9 | 11 | S2→S3 | 6 | 500 | 400.0 | 400.0 | 103.7 | 75000 | 75000 | 100.00% | 57.8 / 58.0 / 58.3 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 10 | 12 | S3→S2 | 7 | 500 | 200.0 | 200.0 | 95.8 | 149988 | 149988 | 100.00% | 58.4 / 58.6 / 83.5 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 11 | 13 | S1→S3 | 6 | 400 | 800.0 | 800.0 | 145.7 | 37499 | 37499 | 100.00% | 121.3 / 121.7 / 122.4 | 0.1 | 0.2 | 0 | 0.00% | 0 |
| 12 | 16 | S3→S2 | 7 | 200 | 800.0 | 800.0 | 97.0 | 37497 | 37497 | 100.00% | 33.6 / 37.8 / 41.9 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 13 | 17 | S1→S2 | 6 | 400 | 400.0 | 400.0 | 83.6 | 75000 | 75000 | 100.00% | 71.2 / 71.4 / 71.7 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 14 | 18 | S1→S3 | 6 | 400 | 400.0 | 400.0 | 212.5 | 74999 | 74999 | 100.00% | 38.0 / 75.9 / 113.1 | 36.7 | 73.3 | 0 | 0.00% | 0 |
| 15 | 19 | S3→S2 | 7 | 500 | 400.0 | 400.0 | 96.4 | 74991 | 74991 | 100.00% | 58.4 / 58.6 / 62.7 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 16 | 22 | S3→S1 | 6 | 100 | 800.0 | 800.0 | 610.6 | 37496 | 37496 | 100.00% | 285.6 / 285.9 / 287.6 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 17 | 28 | S1→S3 | 6 | 500 | 800.0 | 800.0 | 386.2 | 37499 | 37499 | 100.00% | 87.6 / 94.5 / 95.3 | 0.1 | 0.1 | 0 | 0.00% | 0 |
| 18 | 30 | S2→S3 | 6 | 100 | 800.0 | 800.0 | 95.7 | 37500 | 37500 | 100.00% | 49.2 / 49.4 / 49.6 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 19 | 31 | S3→S1 | 6 | 500 | 800.0 | 800.0 | 512.6 | 37499 | 37499 | 100.00% | 117.2 / 118.5 / 120.0 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 20 | 34 | S3→S1 | 7 | 300 | 400.0 | 400.0 | 187.2 | 74994 | 74994 | 100.00% | 45.2 / 46.0 / 46.9 | 0.2 | 0.3 | 0 | 0.00% | 0 |
| 21 | 37 | S2→S3 | 7 | 400 | 800.0 | 800.0 | 245.8 | 37500 | 37500 | 100.00% | 30.1 / 32.8 / 33.0 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 22 | 43 | S3→S1 | 6 | 300 | 800.0 | 800.0 | 395.8 | 37495 | 37495 | 100.00% | 94.1 / 95.2 / 96.4 | 0.3 | 0.3 | 0 | 0.00% | 0 |
| 23 | 45 | S1→S3 | 6 | 200 | 800.0 | 800.0 | 206.7 | 37500 | 37500 | 100.00% | 100.4 / 101.2 / 183.7 | 0.7 | 0.2 | 0 | 0.00% | 0 |
| 24 | 50 | S2→S1 | 7 | 500 | 800.0 | 800.0 | 79.0 | 37500 | 37500 | 100.00% | 22.5 / 23.1 / 23.8 | 0.2 | 0.2 | 0 | 0.00% | 0 |
