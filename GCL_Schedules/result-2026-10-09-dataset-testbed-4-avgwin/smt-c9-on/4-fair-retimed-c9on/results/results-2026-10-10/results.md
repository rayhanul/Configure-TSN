# Traffic run: result-2026-10-09-dataset-testbed-4-avgwin/smt-c9-on/4-fair-retimed-c9on, 2026-10-10 09:01

11 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **1012472 / 1012500 packets (100.00%)**
- Deadline misses: **12320 (1.22% of received)**; flows with zero misses: 8 / 11

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 1 | 100.00% | 17.3 | 0.00% |
| S2 | 4 | 99.99% | 24.8 | 0.00% |
| S3 | 6 | 100.00% | 75.9 | 2.35% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7160963.398] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7162705.045] rms   10 max   17 freq  -6138 +/-  13 delay    20 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[854961.950] rms   50 max  127 freq  +2963 +/-  69 delay    48 +/-   0`
- Connectivity: 11 / 11 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 0 |
| S2 | 0 | 5 | 0 |
| S3 | 0 | 23 | 0 |

Switch queue drops (`ethtool -S` Q DROP) on the 17 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S3→S2 | 6 | 300 | 400.0 | 400.0 | 33.4 | 75000 | 74993 | 99.99% | 21.3 / 21.5 / 26.7 | 0.1 | 0.1 | 0 | 0.00% | 0 |
| 2 | 3 | S2→S3 | 7 | 100 | 400.0 | 400.0 | 33.4 | 75000 | 74999 | 100.00% | 21.4 / 25.6 / 25.9 | 0.4 | 0.1 | 0 | 0.00% | 0 |
| 3 | 6 | S1→S3 | 7 | 300 | 800.0 | 800.0 | 46.8 | 37500 | 37500 | 100.00% | 34.7 / 35.0 / 35.4 | 0.1 | 0.1 | 0 | 0.00% | 0 |
| 4 | 8 | S2→S3 | 7 | 500 | 200.0 | 200.0 | 33.4 | 150000 | 149998 | 100.00% | 28.0 / 52.6 / 59.5 | 6.8 | 12.9 | 0 | 0.00% | 0 |
| 5 | 9 | S1→S3 | 6 | 400 | 800.0 | 800.0 | 45.8 | 37500 | 37500 | 100.00% | 39.2 / 398.2 / 1198.1 | 16.7 | 0.5 | 16 | 0.04% | 0 |
| 6 | 10 | S3→S2 | 6 | 400 | 400.0 | 400.0 | 33.4 | 75000 | 74993 | 99.99% | 23.8 / 24.7 / 25.6 | 0.3 | 0.3 | 0 | 0.00% | 0 |
| 7 | 13 | S1→S2 | 7 | 400 | 200.0 | 200.0 | 29.2 | 150000 | 150000 | 100.00% | 19.0 / 19.8 / 20.6 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 8 | 14 | S3→S2 | 7 | 500 | 200.0 | 200.0 | 42.0 | 150000 | 149991 | 99.99% | 31.2 / 31.6 / 231.8 | 0.7 | 0.1 | 2 | 0.00% | 0 |
| 9 | 18 | S2→S1 | 7 | 300 | 800.0 | 800.0 | 29.2 | 37500 | 37499 | 100.00% | 17.1 / 17.3 / 17.7 | 0.1 | 0.1 | 0 | 0.00% | 0 |
| 10 | 19 | S2→S3 | 6 | 500 | 400.0 | 400.0 | 34.0 | 75000 | 74999 | 100.00% | 28.0 / 111.3 / 423.5 | 138.6 | 141.2 | 12302 | 16.40% | 0 |
| 11 | 20 | S1→S3 | 7 | 100 | 200.0 | 200.0 | 46.2 | 150000 | 150000 | 100.00% | 34.1 / 36.3 / 38.7 | 2.1 | 4.1 | 0 | 0.00% | 0 |
