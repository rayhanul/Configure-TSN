# Traffic run: result-2026-10-09-dataset-testbed-4-avgwin/rl-c9-on/4-matrix-c9on, 2026-10-10 09:41

20 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **1012477 / 1012500 packets (100.00%)**
- Deadline misses: **27392 (2.71% of received)**; flows with zero misses: 10 / 20

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 1 | 100.00% | 17.1 | 0.00% |
| S2 | 4 | 99.99% | 24.7 | 0.00% |
| S3 | 6 | 100.00% | 85.9 | 5.22% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7160963.398] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7165082.478] rms   12 max   19 freq  -6199 +/-  14 delay    21 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[857339.383] rms   48 max  120 freq  +3031 +/-  67 delay    47 +/-   0`
- Connectivity: 11 / 11 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 0 |
| S2 | 0 | 0 | 0 |
| S3 | 0 | 23 | 0 |

Switch queue drops (`ethtool -S` Q DROP) on the 17 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S3→S2 | 6 | 300 | 400.0 | 400.0 | 33.4 | 75000 | 74994 | 99.99% | 21.0 / 21.2 / 53.0 | 0.1 | 0.1 | 0 | 0.00% | 0 |
| 2 | 2 | S1→S2 | None | 300 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 3 | 3 | S2→S3 | 7 | 100 | 400.0 | 400.0 | 33.4 | 75000 | 75000 | 100.00% | 25.2 / 25.4 / 26.9 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 4 | 4 | S3→S2 | None | 400 | 800.0 | 800.0 | – | 0 | – | – | – | – | – | – | – | – |
| 5 | 5 | S3→S1 | None | 200 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 6 | 6 | S1→S3 | 7 | 300 | 800.0 | 800.0 | 46.8 | 37500 | 37500 | 100.00% | 34.5 / 34.7 / 35.1 | 0.1 | 0.1 | 0 | 0.00% | 0 |
| 7 | 7 | S1→S3 | None | 100 | 800.0 | 800.0 | – | 0 | – | – | – | – | – | – | – | – |
| 8 | 8 | S2→S3 | 7 | 500 | 200.0 | 200.0 | 33.4 | 150000 | 150000 | 100.00% | 28.1 / 52.6 / 60.5 | 6.4 | 12.8 | 0 | 0.00% | 0 |
| 9 | 9 | S1→S3 | 6 | 400 | 800.0 | 800.0 | 45.8 | 37500 | 37500 | 100.00% | 397.1 / 397.6 / 401.1 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 10 | 10 | S3→S2 | 6 | 400 | 400.0 | 400.0 | 33.4 | 75000 | 74995 | 99.99% | 23.8 / 24.7 / 355.3 | 1.2 | 0.3 | 0 | 0.00% | 0 |
| 11 | 11 | S2→S1 | None | 200 | 800.0 | 800.0 | – | 0 | – | – | – | – | – | – | – | – |
| 12 | 12 | S2→S3 | None | 100 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 13 | 13 | S1→S2 | 7 | 400 | 200.0 | 200.0 | 29.2 | 150000 | 150000 | 100.00% | 19.1 / 19.8 / 20.6 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 14 | 14 | S3→S2 | 7 | 500 | 200.0 | 200.0 | 42.0 | 150000 | 149988 | 99.99% | 31.0 / 31.3 / 31.8 | 0.1 | 0.1 | 0 | 0.00% | 0 |
| 15 | 15 | S3→S2 | None | 300 | 200.0 | 200.0 | – | 0 | – | – | – | – | – | – | – | – |
| 16 | 16 | S1→S2 | None | 100 | 200.0 | 200.0 | – | 0 | – | – | – | – | – | – | – | – |
| 17 | 17 | S2→S1 | None | 400 | 200.0 | 200.0 | – | 0 | – | – | – | – | – | – | – | – |
| 18 | 18 | S2→S1 | 7 | 300 | 800.0 | 800.0 | 29.2 | 37500 | 37500 | 100.00% | 16.9 / 17.1 / 17.4 | 0.1 | 0.1 | 0 | 0.00% | 0 |
| 19 | 19 | S2→S3 | 6 | 500 | 400.0 | 400.0 | 34.0 | 75000 | 75000 | 100.00% | 28.1 / 190.2 / 422.1 | 176.1 | 270.3 | 27392 | 36.52% | 0 |
| 20 | 20 | S1→S3 | 7 | 100 | 200.0 | 200.0 | 46.2 | 150000 | 150000 | 100.00% | 26.2 / 32.3 / 39.7 | 5.9 | 11.8 | 0 | 0.00% | 0 |
