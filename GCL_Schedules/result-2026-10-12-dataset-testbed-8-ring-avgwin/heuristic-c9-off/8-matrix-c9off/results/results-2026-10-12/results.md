# Traffic run: result-2026-10-12-dataset-testbed-8-ring-avgwin/heuristic-c9-off/8-matrix-c9off, 2026-10-12 15:47

10 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **862489 / 862489 packets (100.00%)**
- Deadline misses: **0 (0.00% of received)**; flows with zero misses: 10 / 10

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 4 | 100.00% | 11.8 | 0.00% |
| S2 | 1 | 100.00% | 67.2 | 0.00% |
| S3 | 5 | 100.00% | 22.7 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7276524.181] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7359864.892] rms   12 max   16 freq  -6398 +/-  17 delay    25 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[1052122.410] rms   10 max   18 freq  +2314 +/-   7 delay    50 +/-   0`
- Connectivity: 10 / 10 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 0 |
| S2 | 0 | 0 | 0 |
| S3 | 0 | 0 | 11 |

Switch queue drops (`ethtool -S` Q DROP) on the 19 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 2 | S2→S1 | 6 | 100 | 400.0 | 400.0 | 83.6 | 75000 | 75000 | 100.00% | 9.7 / 10.3 / 11.1 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 2 | 5 | S1→S3 | 6 | 100 | 800.0 | 800.0 | 45.8 | 37500 | 37500 | 100.00% | 33.8 / 34.0 / 34.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 3 | 6 | S2→S3 | 6 | 100 | 200.0 | 200.0 | 95.8 | 150000 | 150000 | 100.00% | 12.0 / 12.8 / 13.8 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 4 | 9 | S3→S1 | 6 | 100 | 400.0 | 400.0 | 45.8 | 74995 | 74995 | 100.00% | 5.1 / 5.4 / 5.9 | 0.1 | 0.2 | 0 | 0.00% | 0 |
| 5 | 10 | S1→S3 | 7 | 100 | 200.0 | 200.0 | 45.8 | 150000 | 150000 | 100.00% | 33.8 / 34.0 / 34.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 6 | 12 | S2→S3 | 7 | 500 | 800.0 | 800.0 | 95.8 | 37500 | 37500 | 100.00% | 34.1 / 34.3 / 34.5 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 7 | 13 | S3→S1 | 7 | 200 | 800.0 | 800.0 | 45.8 | 37499 | 37499 | 100.00% | 6.6 / 7.0 / 7.4 | 0.1 | 0.2 | 0 | 0.00% | 0 |
| 8 | 18 | S3→S1 | 7 | 400 | 400.0 | 400.0 | 45.8 | 74995 | 74995 | 100.00% | 21.7 / 22.1 / 25.5 | 0.1 | 0.2 | 0 | 0.00% | 0 |
| 9 | 19 | S1→S3 | 7 | 300 | 400.0 | 400.0 | 46.2 | 75000 | 75000 | 100.00% | 8.1 / 8.5 / 9.3 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 10 | 20 | S1→S2 | 6 | 500 | 200.0 | 200.0 | 79.1 | 150000 | 150000 | 100.00% | 67.0 / 67.2 / 67.5 | 0.1 | 0.0 | 0 | 0.00% | 0 |
