# Traffic run: result-2026-10-12-dataset-testbed-7-ring-avgwin/heuristic-c9-on/7-matrix-c9on, 2026-10-12 15:26

11 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **1012455 / 1012461 packets (100.00%)**
- Deadline misses: **0 (0.00% of received)**; flows with zero misses: 11 / 11

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 4 | 100.00% | 15.6 | 0.00% |
| S2 | 6 | 100.00% | 25.3 | 0.00% |
| S3 | 1 | 100.00% | 42.0 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7276524.181] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7358628.048] rms   10 max   18 freq  -6572 +/-  13 delay    24 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[1050885.441] rms    8 max   11 freq  +2707 +/-  11 delay    48 +/-   0`
- Connectivity: 11 / 11 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 0 |
| S2 | 0 | 0 | 0 |
| S3 | 0 | 6 | 39 |

Switch queue drops (`ethtool -S` Q DROP) on the 19 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S1→S2 | 7 | 200 | 200.0 | 200.0 | 36.9 | 150000 | 150000 | 100.00% | 24.5 / 24.7 / 25.0 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 2 | 3 | S2→S3 | 7 | 500 | 400.0 | 400.0 | 54.2 | 75000 | 75000 | 100.00% | 41.8 / 42.0 / 42.3 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 3 | 5 | S1→S2 | 7 | 200 | 800.0 | 800.0 | 36.9 | 37500 | 37500 | 100.00% | 24.5 / 24.7 / 25.0 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 4 | 7 | S2→S1 | 6 | 500 | 800.0 | 800.0 | 45.8 | 37500 | 37500 | 100.00% | 33.5 / 33.7 / 33.9 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 5 | 8 | S3→S1 | 7 | 500 | 400.0 | 400.0 | 33.7 | 74993 | 74992 | 100.00% | 14.0 / 18.0 / 21.7 | 3.6 | 7.2 | 0 | 0.00% | 0 |
| 6 | 9 | S3→S1 | 7 | 100 | 200.0 | 200.0 | 22.8 | 149986 | 149984 | 100.00% | 10.5 / 10.7 / 10.8 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 7 | 12 | S1→S2 | 6 | 300 | 200.0 | 200.0 | 51.0 | 150000 | 150000 | 100.00% | 25.8 / 27.0 / 27.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 8 | 15 | S1→S2 | 6 | 300 | 400.0 | 400.0 | 39.4 | 75000 | 75000 | 100.00% | 21.4 / 21.9 / 22.5 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 9 | 18 | S3→S1 | 6 | 300 | 400.0 | 400.0 | 26.0 | 74994 | 74993 | 100.00% | 13.7 / 13.9 / 14.0 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 10 | 19 | S1→S2 | 6 | 200 | 800.0 | 800.0 | 36.9 | 37500 | 37500 | 100.00% | 24.5 / 24.7 / 25.0 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 11 | 20 | S3→S2 | 6 | 100 | 200.0 | 200.0 | 38.2 | 149988 | 149986 | 100.00% | 25.8 / 26.0 / 26.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
