# Traffic run: result-2026-10-13-dataset-testbed-12-tree-avgwin/heuristic-c9-off/12-matrix-c9off, 2026-10-13 13:28

11 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **937482 / 937482 packets (100.00%)**
- Deadline misses: **0 (0.00% of received)**; flows with zero misses: 11 / 11

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 3 | 100.00% | 31.2 | 0.00% |
| S2 | 4 | 100.00% | 55.4 | 0.00% |
| S3 | 4 | 100.00% | 76.5 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7276524.181] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7437927.604] rms    8 max   13 freq  -6516 +/-  11 delay    26 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[1130185.134] rms   43 max   60 freq  +2216 +/-  54 delay    49 +/-   0`
- Connectivity: 11 / 11 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 0 |
| S2 | 0 | 0 | 0 |
| S3 | 0 | 0 | 18 |

Switch queue drops (`ethtool -S` Q DROP) on the 17 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 2 | S1→S2 | 7 | 400 | 200.0 | 200.0 | 79.1 | 150000 | 150000 | 100.00% | 54.8 / 55.3 / 56.4 | 0.3 | 0.2 | 0 | 0.00% | 0 |
| 2 | 4 | S1→S3 | 7 | 300 | 800.0 | 800.0 | 145.7 | 37500 | 37500 | 100.00% | 83.7 / 83.9 / 84.1 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 3 | 5 | S3→S2 | 7 | 100 | 200.0 | 200.0 | 95.8 | 149990 | 149990 | 100.00% | 54.7 / 58.1 / 59.1 | 1.1 | 0.6 | 0 | 0.00% | 0 |
| 4 | 7 | S3→S1 | 6 | 500 | 800.0 | 800.0 | 145.7 | 37498 | 37498 | 100.00% | 77.8 / 78.6 / 79.4 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 5 | 8 | S2→S1 | 6 | 300 | 200.0 | 200.0 | 79.1 | 150000 | 150000 | 100.00% | 15.9 / 16.6 / 17.4 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 6 | 9 | S3→S2 | 6 | 200 | 400.0 | 400.0 | 95.8 | 74994 | 74994 | 100.00% | 83.4 / 83.6 / 83.8 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 7 | 11 | S2→S1 | 7 | 300 | 800.0 | 800.0 | 79.1 | 37500 | 37500 | 100.00% | 41.8 / 42.0 / 42.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 8 | 12 | S1→S3 | 7 | 500 | 200.0 | 200.0 | 146.0 | 150000 | 150000 | 100.00% | 67.0 / 68.0 / 133.9 | 0.3 | 0.2 | 0 | 0.00% | 0 |
| 9 | 14 | S1→S2 | 7 | 200 | 400.0 | 400.0 | 83.6 | 75000 | 75000 | 100.00% | 21.6 / 22.2 / 22.7 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 10 | 18 | S2→S3 | 6 | 300 | 800.0 | 800.0 | 95.8 | 37500 | 37500 | 100.00% | 57.8 / 58.4 / 59.0 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 11 | 19 | S1→S3 | 6 | 400 | 800.0 | 800.0 | 145.7 | 37500 | 37500 | 100.00% | 120.8 / 121.0 / 121.3 | 0.1 | 0.0 | 0 | 0.00% | 0 |
