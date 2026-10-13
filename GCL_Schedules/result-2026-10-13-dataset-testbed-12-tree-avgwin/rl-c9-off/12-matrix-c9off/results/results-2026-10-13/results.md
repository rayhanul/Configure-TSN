# Traffic run: result-2026-10-13-dataset-testbed-12-tree-avgwin/rl-c9-off/12-matrix-c9off, 2026-10-13 13:32

20 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **937483 / 937483 packets (100.00%)**
- Deadline misses: **0 (0.00% of received)**; flows with zero misses: 11 / 20

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 3 | 100.00% | 31.2 | 0.00% |
| S2 | 4 | 100.00% | 51.9 | 0.00% |
| S3 | 4 | 100.00% | 92.2 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7276524.181] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7438162.905] rms    7 max   16 freq  -6478 +/-  10 delay    24 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[1130420.061] rms   27 max   57 freq  +2269 +/-  36 delay    49 +/-   0`
- Connectivity: 11 / 11 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 0 |
| S2 | 0 | 0 | 0 |
| S3 | 0 | 0 | 17 |

Switch queue drops (`ethtool -S` Q DROP) on the 17 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S1→S2 | None | 400 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 2 | 2 | S1→S2 | 7 | 400 | 200.0 | 200.0 | 79.1 | 150000 | 150000 | 100.00% | 54.8 / 55.3 / 56.5 | 0.3 | 0.2 | 0 | 0.00% | 0 |
| 3 | 3 | S3→S1 | None | 200 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 4 | 4 | S1→S3 | 7 | 300 | 800.0 | 800.0 | 145.7 | 37500 | 37500 | 100.00% | 83.8 / 84.0 / 84.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 5 | 5 | S3→S2 | 7 | 100 | 200.0 | 200.0 | 95.8 | 149991 | 149991 | 100.00% | 54.7 / 58.0 / 59.0 | 1.3 | 0.7 | 0 | 0.00% | 0 |
| 6 | 6 | S1→S3 | None | 300 | 800.0 | 800.0 | – | 0 | – | – | – | – | – | – | – | – |
| 7 | 7 | S3→S1 | 6 | 500 | 800.0 | 800.0 | 145.7 | 37497 | 37497 | 100.00% | 77.8 / 78.6 / 79.5 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 8 | 8 | S2→S1 | 6 | 300 | 200.0 | 200.0 | 79.1 | 150000 | 150000 | 100.00% | 15.8 / 16.6 / 18.5 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 9 | 9 | S3→S2 | 6 | 200 | 400.0 | 400.0 | 95.8 | 74995 | 74995 | 100.00% | 70.9 / 71.1 / 71.3 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 10 | 10 | S1→S3 | None | 500 | 200.0 | 200.0 | – | 0 | – | – | – | – | – | – | – | – |
| 11 | 11 | S2→S1 | 7 | 300 | 800.0 | 800.0 | 79.1 | 37500 | 37500 | 100.00% | 41.8 / 42.0 / 42.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 12 | 12 | S1→S3 | 7 | 500 | 200.0 | 200.0 | 146.0 | 150000 | 150000 | 100.00% | 56.2 / 89.2 / 134.2 | 33.3 | 64.2 | 0 | 0.00% | 0 |
| 13 | 13 | S2→S3 | None | 100 | 800.0 | 800.0 | – | 0 | – | – | – | – | – | – | – | – |
| 14 | 14 | S1→S2 | 7 | 200 | 400.0 | 400.0 | 83.6 | 75000 | 75000 | 100.00% | 12.8 / 13.5 / 14.8 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 15 | 15 | S2→S3 | None | 500 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 16 | 16 | S3→S2 | None | 400 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 17 | 17 | S1→S2 | None | 300 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 18 | 18 | S2→S3 | 6 | 300 | 800.0 | 800.0 | 95.8 | 37500 | 37500 | 100.00% | 83.4 / 83.6 / 83.9 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 19 | 19 | S1→S3 | 6 | 400 | 800.0 | 800.0 | 145.7 | 37500 | 37500 | 100.00% | 120.9 / 121.1 / 121.4 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 20 | 20 | S2→S3 | None | 200 | 200.0 | 200.0 | – | 0 | – | – | – | – | – | – | – | – |
