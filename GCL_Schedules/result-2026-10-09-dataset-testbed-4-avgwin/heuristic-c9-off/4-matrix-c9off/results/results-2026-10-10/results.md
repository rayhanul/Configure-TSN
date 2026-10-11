# Traffic run: result-2026-10-09-dataset-testbed-4-avgwin/heuristic-c9-off/4-matrix-c9off, 2026-10-10 09:11

11 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **1012436 / 1012482 packets (100.00%)**
- Deadline misses: **74983 (7.41% of received)**; flows with zero misses: 10 / 11

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 1 | 100.00% | 42.0 | 0.00% |
| S2 | 4 | 99.99% | 73.9 | 16.67% |
| S3 | 6 | 100.00% | 114.6 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7160963.398] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7163330.328] rms    6 max   12 freq  -6169 +/-   8 delay    21 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[855587.358] rms   14 max   21 freq  +2911 +/-  17 delay    47 +/-   0`
- Connectivity: 11 / 11 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 0 |
| S2 | 0 | 2 | 0 |
| S3 | 0 | 44 | 18 |

Switch queue drops (`ethtool -S` Q DROP) on the 17 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S3→S2 | 7 | 300 | 400.0 | 400.0 | 95.8 | 74996 | 74984 | 99.98% | 83.7 / 83.9 / 84.1 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 2 | 3 | S2→S3 | 7 | 100 | 400.0 | 400.0 | 95.8 | 75000 | 75000 | 100.00% | 83.7 / 83.9 / 84.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 3 | 6 | S1→S3 | 6 | 300 | 800.0 | 800.0 | 145.7 | 37500 | 37500 | 100.00% | 133.6 / 133.8 / 134.1 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 4 | 8 | S2→S3 | 6 | 500 | 200.0 | 200.0 | 95.8 | 150000 | 150000 | 100.00% | 83.7 / 121.8 / 160.0 | 37.9 | 75.8 | 0 | 0.00% | 0 |
| 5 | 9 | S1→S3 | 6 | 400 | 800.0 | 800.0 | 145.7 | 37500 | 37500 | 100.00% | 111.2 / 111.4 / 111.7 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 6 | 10 | S3→S2 | 7 | 400 | 400.0 | 400.0 | 95.8 | 74995 | 74984 | 99.99% | 58.9 / 61.5 / 61.7 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 7 | 13 | S1→S2 | 6 | 400 | 200.0 | 200.0 | 79.1 | 150000 | 150000 | 100.00% | 19.0 / 22.8 / 32.6 | 5.2 | 6.1 | 0 | 0.00% | 0 |
| 8 | 14 | S3→S2 | 6 | 500 | 200.0 | 200.0 | 95.8 | 149991 | 149970 | 99.99% | 28.0 / 126.1 / 224.4 | 97.4 | 194.8 | 74983 | 50.00% | 0 |
| 9 | 18 | S2→S1 | 6 | 300 | 800.0 | 800.0 | 79.1 | 37500 | 37499 | 100.00% | 41.4 / 42.0 / 42.6 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 10 | 19 | S2→S3 | 7 | 500 | 400.0 | 400.0 | 95.8 | 75000 | 74999 | 100.00% | 83.7 / 83.9 / 84.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 11 | 20 | S1→S3 | 6 | 100 | 200.0 | 200.0 | 145.7 | 150000 | 150000 | 100.00% | 133.6 / 133.8 / 138.0 | 0.1 | 0.0 | 0 | 0.00% | 0 |
