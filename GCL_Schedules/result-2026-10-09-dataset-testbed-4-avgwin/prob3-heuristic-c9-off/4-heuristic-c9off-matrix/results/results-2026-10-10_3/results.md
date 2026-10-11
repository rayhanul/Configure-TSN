# Traffic run: result-2026-10-09-dataset-testbed-4-avgwin/prob3-heuristic-c9-off/4-heuristic-c9off-matrix, 2026-10-10 18:53

24 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **1612423 / 1612431 packets (100.00%)**
- Deadline misses: **0 (0.00% of received)**; flows with zero misses: 24 / 24

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 8 | 100.00% | 89.0 | 0.00% |
| S2 | 10 | 100.00% | 65.7 | 0.00% |
| S3 | 6 | 100.00% | 103.7 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7192691.373] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7198230.670] rms   24 max   63 freq  -6184 +/-  30 delay    25 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[890488.325] rms   51 max  111 freq  +3063 +/-  70 delay    48 +/-   0`
- Connectivity: 24 / 24 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 0 |
| S2 | 0 | 0 | 0 |
| S3 | 0 | 8 | 69 |

Switch queue drops (`ethtool -S` Q DROP) on the 17 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S3→S2 | 7 | 300 | 400.0 | 400.0 | 95.8 | 74987 | 74985 | 100.00% | 83.6 / 83.9 / 84.1 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 2 | 2 | S1→S2 | 7 | 300 | 400.0 | 400.0 | 312.3 | 75000 | 75000 | 100.00% | 200.4 / 250.6 / 301.2 | 49.9 | 99.8 | 0 | 0.00% | 0 |
| 3 | 3 | S2→S3 | 7 | 100 | 400.0 | 400.0 | 95.8 | 75000 | 75000 | 100.00% | 83.7 / 83.9 / 84.1 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 4 | 4 | S3→S2 | 6 | 400 | 800.0 | 800.0 | 95.7 | 37493 | 37492 | 100.00% | 23.8 / 24.7 / 26.5 | 0.3 | 0.2 | 0 | 0.00% | 0 |
| 5 | 6 | S1→S3 | 6 | 300 | 800.0 | 800.0 | 145.7 | 37500 | 37500 | 100.00% | 133.6 / 133.8 / 134.0 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 6 | 8 | S2→S3 | 6 | 500 | 200.0 | 200.0 | 95.8 | 150000 | 150000 | 100.00% | 83.7 / 83.9 / 84.1 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 7 | 9 | S1→S3 | 6 | 400 | 800.0 | 800.0 | 145.7 | 37500 | 37500 | 100.00% | 111.2 / 111.4 / 111.6 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 8 | 10 | S3→S2 | 7 | 400 | 400.0 | 400.0 | 95.8 | 74988 | 74987 | 100.00% | 58.8 / 61.5 / 61.7 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 9 | 11 | S2→S1 | 7 | 200 | 800.0 | 800.0 | 533.4 | 37500 | 37500 | 100.00% | 12.8 / 13.5 / 14.3 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 10 | 13 | S1→S2 | 6 | 400 | 200.0 | 200.0 | 79.1 | 150000 | 150000 | 100.00% | 19.0 / 23.1 / 40.5 | 5.7 | 6.6 | 0 | 0.00% | 0 |
| 11 | 14 | S3→S2 | 6 | 500 | 200.0 | 200.0 | 95.8 | 149976 | 149973 | 100.00% | 28.0 / 28.7 / 31.6 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 12 | 18 | S2→S1 | 6 | 300 | 800.0 | 800.0 | 79.1 | 37500 | 37500 | 100.00% | 41.4 / 42.0 / 42.6 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 13 | 19 | S2→S3 | 7 | 500 | 400.0 | 400.0 | 95.8 | 75000 | 75000 | 100.00% | 83.7 / 83.9 / 84.1 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 14 | 20 | S1→S3 | 6 | 100 | 200.0 | 200.0 | 145.7 | 150000 | 150000 | 100.00% | 133.6 / 133.8 / 134.0 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 15 | 21 | S2→S1 | 6 | 400 | 800.0 | 800.0 | 79.0 | 37500 | 37500 | 100.00% | 32.7 / 33.4 / 34.0 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 16 | 22 | S2→S1 | 7 | 300 | 800.0 | 800.0 | 512.3 | 37500 | 37500 | 100.00% | 412.1 / 412.8 / 420.7 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 17 | 23 | S2→S1 | 6 | 300 | 800.0 | 800.0 | 79.0 | 37500 | 37500 | 100.00% | 23.3 / 23.9 / 24.6 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 18 | 24 | S3→S1 | 7 | 300 | 800.0 | 800.0 | 233.0 | 37494 | 37494 | 100.00% | 102.5 / 103.2 / 110.7 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 19 | 29 | S1→S2 | 6 | 100 | 400.0 | 400.0 | 141.4 | 75000 | 75000 | 100.00% | 20.6 / 22.1 / 24.3 | 1.3 | 2.6 | 0 | 0.00% | 0 |
| 20 | 30 | S1→S2 | 6 | 500 | 400.0 | 400.0 | 83.5 | 75000 | 75000 | 100.00% | 43.1 / 43.4 / 43.9 | 0.1 | 0.2 | 0 | 0.00% | 0 |
| 21 | 42 | S1→S2 | 7 | 200 | 800.0 | 800.0 | 233.0 | 37500 | 37500 | 100.00% | 190.2 / 190.4 / 190.6 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 22 | 45 | S3→S1 | 6 | 500 | 800.0 | 800.0 | 145.6 | 37493 | 37492 | 100.00% | 63.5 / 64.2 / 65.0 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 23 | 48 | S1→S2 | 6 | 300 | 800.0 | 800.0 | 141.4 | 37500 | 37500 | 100.00% | 33.4 / 33.6 / 34.5 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 24 | 50 | S2→S1 | 7 | 300 | 800.0 | 800.0 | 129.0 | 37500 | 37500 | 100.00% | 16.1 / 18.6 / 25.9 | 0.2 | 0.2 | 0 | 0.00% | 0 |
