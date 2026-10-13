# Traffic run: result-2026-10-13-dataset-testbed-13-tree-avgwin/prob3-rl-c9-off/13-rl-c9off-matrix, 2026-10-13 14:01

27 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **1987471 / 1987471 packets (100.00%)**
- Deadline misses: **0 (0.00% of received)**; flows with zero misses: 27 / 27

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 7 | 100.00% | 83.3 | 0.00% |
| S2 | 10 | 100.00% | 78.7 | 0.00% |
| S3 | 10 | 100.00% | 85.4 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7276524.181] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7439889.662] rms   11 max   19 freq  -6469 +/-  12 delay    24 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[1132147.444] rms   52 max  106 freq  +2284 +/-  71 delay    48 +/-   0`
- Connectivity: 27 / 27 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 1 |
| S2 | 0 | 0 | 0 |
| S3 | 0 | 0 | 28 |

Switch queue drops (`ethtool -S` Q DROP) on the 17 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S3→S2 | 7 | 400 | 400.0 | 400.0 | 249.9 | 74998 | 74998 | 100.00% | 237.7 / 238.3 / 239.2 | 0.5 | 1.0 | 0 | 0.00% | 0 |
| 2 | 2 | S1→S2 | 7 | 200 | 800.0 | 800.0 | 312.3 | 37500 | 37500 | 100.00% | 100.3 / 103.6 / 103.8 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 3 | 3 | S1→S3 | 7 | 400 | 400.0 | 400.0 | 145.7 | 75000 | 75000 | 100.00% | 101.2 / 101.4 / 101.6 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 4 | 5 | S3→S2 | 6 | 500 | 200.0 | 200.0 | 95.8 | 149990 | 149990 | 100.00% | 28.0 / 28.7 / 32.6 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 5 | 6 | S3→S1 | 7 | 400 | 800.0 | 800.0 | 145.6 | 37500 | 37500 | 100.00% | 133.3 / 133.5 / 133.7 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 6 | 8 | S3→S2 | 6 | 500 | 800.0 | 800.0 | 95.8 | 37500 | 37500 | 100.00% | 75.3 / 75.9 / 76.6 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 7 | 9 | S3→S2 | 6 | 200 | 400.0 | 400.0 | 95.8 | 74999 | 74999 | 100.00% | 57.4 / 57.8 / 58.2 | 0.1 | 0.2 | 0 | 0.00% | 0 |
| 8 | 10 | S2→S1 | 6 | 300 | 200.0 | 200.0 | 79.1 | 150000 | 150000 | 100.00% | 15.8 / 16.6 / 18.6 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 9 | 11 | S2→S3 | 7 | 500 | 200.0 | 200.0 | 95.7 | 150000 | 150000 | 100.00% | 50.0 / 50.7 / 51.4 | 0.2 | 0.1 | 0 | 0.00% | 0 |
| 10 | 12 | S2→S3 | 7 | 400 | 400.0 | 400.0 | 97.6 | 75000 | 75000 | 100.00% | 85.3 / 85.6 / 85.8 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 11 | 13 | S2→S1 | 7 | 500 | 400.0 | 400.0 | 79.1 | 75000 | 75000 | 100.00% | 29.3 / 29.5 / 29.7 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 12 | 14 | S1→S2 | 6 | 200 | 200.0 | 200.0 | 79.1 | 150000 | 150000 | 100.00% | 12.9 / 14.1 / 30.8 | 1.1 | 1.3 | 0 | 0.00% | 0 |
| 13 | 15 | S1→S3 | 6 | 100 | 800.0 | 800.0 | 159.1 | 37500 | 37500 | 100.00% | 123.8 / 124.0 / 124.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 14 | 17 | S2→S3 | 7 | 100 | 800.0 | 800.0 | 96.4 | 37500 | 37500 | 100.00% | 84.1 / 84.3 / 84.5 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 15 | 18 | S2→S1 | 6 | 400 | 400.0 | 400.0 | 109.8 | 75000 | 75000 | 100.00% | 66.8 / 67.0 / 67.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 16 | 19 | S2→S3 | 6 | 200 | 200.0 | 200.0 | 95.8 | 150000 | 150000 | 100.00% | 83.4 / 83.6 / 83.8 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 17 | 20 | S2→S3 | 6 | 300 | 400.0 | 400.0 | 108.6 | 75000 | 75000 | 100.00% | 96.2 / 96.4 / 96.6 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 18 | 23 | S3→S1 | 7 | 400 | 400.0 | 400.0 | 212.8 | 74993 | 74993 | 100.00% | 174.9 / 176.0 / 179.4 | 0.9 | 1.8 | 0 | 0.00% | 0 |
| 19 | 26 | S3→S1 | 7 | 300 | 800.0 | 800.0 | 212.8 | 37500 | 37500 | 100.00% | 149.5 / 150.3 / 200.7 | 1.1 | 0.3 | 0 | 0.00% | 0 |
| 20 | 31 | S1→S3 | 6 | 400 | 800.0 | 800.0 | 151.7 | 37500 | 37500 | 100.00% | 104.6 / 104.8 / 105.0 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 21 | 37 | S3→S1 | 7 | 200 | 800.0 | 800.0 | 212.8 | 37500 | 37500 | 100.00% | 139.3 / 187.9 / 190.5 | 0.8 | 0.0 | 0 | 0.00% | 0 |
| 22 | 38 | S1→S3 | 6 | 300 | 400.0 | 400.0 | 145.6 | 74999 | 74999 | 100.00% | 97.4 / 97.6 / 97.8 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 23 | 41 | S1→S2 | 6 | 500 | 400.0 | 400.0 | 134.7 | 75000 | 75000 | 100.00% | 22.5 / 61.9 / 101.3 | 38.8 | 77.6 | 0 | 0.00% | 0 |
| 24 | 44 | S1→S3 | 6 | 400 | 800.0 | 800.0 | 151.7 | 37500 | 37500 | 100.00% | 95.1 / 95.3 / 95.5 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 25 | 45 | S3→S2 | 6 | 300 | 400.0 | 400.0 | 95.7 | 74998 | 74998 | 100.00% | 22.2 / 45.0 / 67.9 | 22.3 | 44.6 | 0 | 0.00% | 0 |
| 26 | 48 | S3→S2 | 7 | 200 | 800.0 | 800.0 | 216.3 | 37494 | 37494 | 100.00% | 204.1 / 204.3 / 204.5 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 27 | 49 | S1→S2 | 7 | 100 | 800.0 | 800.0 | 341.4 | 37500 | 37500 | 100.00% | 212.4 / 212.6 / 213.0 | 0.1 | 0.0 | 0 | 0.00% | 0 |
