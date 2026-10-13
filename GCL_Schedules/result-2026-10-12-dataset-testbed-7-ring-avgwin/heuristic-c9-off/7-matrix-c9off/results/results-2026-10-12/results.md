# Traffic run: result-2026-10-12-dataset-testbed-7-ring-avgwin/heuristic-c9-off/7-matrix-c9off, 2026-10-12 15:23

11 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **1012468 / 1012468 packets (100.00%)**
- Deadline misses: **0 (0.00% of received)**; flows with zero misses: 11 / 11

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 4 | 100.00% | 35.1 | 0.00% |
| S2 | 6 | 100.00% | 55.6 | 0.00% |
| S3 | 1 | 100.00% | 61.7 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7276524.181] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7358400.175] rms    8 max   15 freq  -6698 +/-  11 delay    22 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[1050657.944] rms    5 max   11 freq  +2753 +/-   7 delay    49 +/-   0`
- Connectivity: 11 / 11 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 6 |
| S2 | 0 | 0 | 1 |
| S3 | 0 | 0 | 25 |

Switch queue drops (`ethtool -S` Q DROP) on the 19 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S1→S2 | 6 | 200 | 200.0 | 200.0 | 79.1 | 149998 | 149998 | 100.00% | 66.8 / 67.0 / 67.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 2 | 3 | S2→S3 | 7 | 500 | 400.0 | 400.0 | 95.8 | 74999 | 74999 | 100.00% | 61.2 / 61.7 / 62.4 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 3 | 5 | S1→S2 | 7 | 200 | 800.0 | 800.0 | 79.1 | 37499 | 37499 | 100.00% | 22.0 / 22.2 / 22.4 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 4 | 7 | S2→S1 | 7 | 500 | 800.0 | 800.0 | 83.6 | 37500 | 37500 | 100.00% | 44.5 / 45.0 / 45.5 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 5 | 8 | S3→S1 | 6 | 500 | 400.0 | 400.0 | 45.8 | 74997 | 74997 | 100.00% | 33.5 / 33.7 / 33.9 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 6 | 9 | S3→S1 | 7 | 100 | 200.0 | 200.0 | 45.8 | 149990 | 149990 | 100.00% | 33.5 / 33.7 / 33.9 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 7 | 12 | S1→S2 | 7 | 300 | 200.0 | 200.0 | 79.1 | 149998 | 149998 | 100.00% | 66.8 / 67.0 / 67.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 8 | 15 | S1→S2 | 7 | 300 | 400.0 | 400.0 | 83.6 | 74999 | 74999 | 100.00% | 44.4 / 44.6 / 44.8 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 9 | 18 | S3→S1 | 6 | 300 | 400.0 | 400.0 | 46.5 | 74997 | 74997 | 100.00% | 34.2 / 34.3 / 34.5 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 10 | 19 | S1→S2 | 7 | 200 | 800.0 | 800.0 | 79.1 | 37500 | 37500 | 100.00% | 66.8 / 67.0 / 67.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 11 | 20 | S3→S2 | 6 | 100 | 200.0 | 200.0 | 95.8 | 149991 | 149991 | 100.00% | 42.0 / 43.8 / 44.0 | 0.1 | 0.0 | 0 | 0.00% | 0 |
