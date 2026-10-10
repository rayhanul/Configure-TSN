# Traffic run: result-2026-10-08-dataset-testbed-2/smt-c9-on/2-fair-retimed-c9on, 2026-10-09 15:18

11 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **1012477 / 1012493 packets (100.00%)**
- Deadline misses: **14 (0.00% of received)**; flows with zero misses: 10 / 11

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 4 | 100.00% | 44.9 | 0.00% |
| S2 | 5 | 100.00% | 40.0 | 0.00% |
| S3 | 2 | 100.00% | 15.1 | 0.01% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7099122.120] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7098895.497] rms    8 max   15 freq  -6411 +/-  11 delay    17 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[791152.024] rms   24 max   62 freq  +2834 +/-  33 delay    47 +/-   0`
- Connectivity: 11 / 11 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 0 |
| S2 | 0 | 0 | 7 |
| S3 | 0 | 16 | 0 |

Switch queue drops (`ethtool -S` Q DROP) on the 27 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S1→S2 | 7 | 500 | 200.0 | 200.0 | 41.9 | 150000 | 150000 | 100.00% | 29.9 / 30.1 / 30.3 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 2 | 4 | S1→S3 | 6 | 400 | 800.0 | 800.0 | 20.8 | 37500 | 37500 | 100.00% | 9.7 / 10.4 / 813.5 | 15.5 | 0.5 | 14 | 0.04% | 0 |
| 3 | 7 | S3→S1 | 7 | 300 | 400.0 | 400.0 | 20.8 | 75000 | 74999 | 100.00% | 8.8 / 9.0 / 9.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 4 | 9 | S1→S2 | 6 | 400 | 200.0 | 200.0 | 29.8 | 150000 | 150000 | 100.00% | 19.0 / 19.8 / 20.6 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 5 | 10 | S3→S2 | 6 | 300 | 800.0 | 800.0 | 29.1 | 37500 | 37498 | 99.99% | 17.1 / 19.6 / 20.1 | 0.8 | 0.4 | 0 | 0.00% | 0 |
| 6 | 11 | S2→S3 | 7 | 300 | 400.0 | 400.0 | 29.1 | 74999 | 74999 | 100.00% | 17.1 / 17.4 / 17.7 | 0.1 | 0.1 | 0 | 0.00% | 0 |
| 7 | 12 | S2→S1 | 7 | 200 | 800.0 | 800.0 | 29.1 | 37499 | 37499 | 100.00% | 17.1 / 17.3 / 17.5 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 8 | 14 | S3→S2 | 6 | 500 | 200.0 | 200.0 | 29.1 | 150000 | 149990 | 99.99% | 22.5 / 47.4 / 72.4 | 24.3 | 48.6 | 0 | 0.00% | 0 |
| 9 | 16 | S2→S1 | 6 | 100 | 400.0 | 400.0 | 29.1 | 74999 | 74999 | 100.00% | 17.3 / 95.0 / 167.6 | 72.3 | 144.7 | 0 | 0.00% | 0 |
| 10 | 18 | S2→S1 | 6 | 400 | 200.0 | 200.0 | 29.1 | 149996 | 149996 | 100.00% | 19.0 / 44.7 / 70.0 | 24.6 | 49.2 | 0 | 0.00% | 0 |
| 11 | 20 | S3→S2 | 6 | 300 | 400.0 | 400.0 | 29.1 | 75000 | 74997 | 100.00% | 25.3 / 95.3 / 167.6 | 64.1 | 113.2 | 0 | 0.00% | 0 |
