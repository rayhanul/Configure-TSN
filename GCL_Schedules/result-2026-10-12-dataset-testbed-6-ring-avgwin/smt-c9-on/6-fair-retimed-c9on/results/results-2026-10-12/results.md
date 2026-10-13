# Traffic run: result-2026-10-12-dataset-testbed-6-ring-avgwin/smt-c9-on/6-fair-retimed-c9on, 2026-10-12 13:21

10 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **1012452 / 1012459 packets (100.00%)**
- Deadline misses: **7 (0.00% of received)**; flows with zero misses: 9 / 10

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 7 | 100.00% | 20.9 | 0.00% |
| S2 | 2 | 100.00% | 31.5 | 0.00% |
| S3 | 1 | 100.00% | 14.0 | 0.02% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7276524.181] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7351082.096] rms    9 max   18 freq  -6350 +/-  11 delay    23 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[1043339.365] rms    8 max   16 freq  +2945 +/-  11 delay    50 +/-   0`
- Connectivity: 10 / 10 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 0 |
| S2 | 0 | 0 | 0 |
| S3 | 0 | 7 | 41 |

Switch queue drops (`ethtool -S` Q DROP) on the 19 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S3→S1 | 7 | 500 | 200.0 | 200.0 | 29.2 | 149987 | 149985 | 100.00% | 16.9 / 17.1 / 17.3 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 2 | 2 | S2→S1 | 6 | 400 | 200.0 | 200.0 | 43.3 | 150000 | 150000 | 100.00% | 31.0 / 31.2 / 31.3 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 3 | 4 | S1→S3 | 6 | 300 | 800.0 | 800.0 | 26.0 | 37500 | 37500 | 100.00% | 13.7 / 14.0 / 815.0 | 10.9 | 0.3 | 7 | 0.02% | 0 |
| 4 | 6 | S2→S1 | 6 | 100 | 400.0 | 400.0 | 33.0 | 75000 | 75000 | 100.00% | 20.7 / 20.9 / 21.1 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 5 | 7 | S2→S1 | 7 | 300 | 800.0 | 800.0 | 39.4 | 37500 | 37500 | 100.00% | 27.1 / 27.3 / 27.5 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 6 | 9 | S3→S2 | 6 | 500 | 200.0 | 200.0 | 54.2 | 149987 | 149985 | 100.00% | 41.8 / 42.0 / 42.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 7 | 12 | S2→S1 | 7 | 100 | 800.0 | 800.0 | 42.0 | 37500 | 37500 | 100.00% | 29.7 / 29.9 / 30.0 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 8 | 14 | S1→S2 | 7 | 100 | 200.0 | 200.0 | 33.0 | 150000 | 150000 | 100.00% | 20.7 / 20.9 / 21.1 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 9 | 19 | S3→S1 | 6 | 500 | 400.0 | 400.0 | 29.2 | 74998 | 74997 | 100.00% | 16.9 / 17.1 / 17.3 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 10 | 20 | S3→S1 | 6 | 200 | 200.0 | 200.0 | 24.7 | 149987 | 149985 | 100.00% | 12.4 / 12.6 / 12.8 | 0.1 | 0.0 | 0 | 0.00% | 0 |
