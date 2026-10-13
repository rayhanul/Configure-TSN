# Traffic run: result-2026-10-13-dataset-testbed-12-tree-avgwin/heuristic-c9-on/12-matrix-c9on, 2026-10-13 13:30

11 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **931961 / 937483 packets (99.41%)**
- Deadline misses: **94 (0.01% of received)**; flows with zero misses: 4 / 11

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 3 | 99.83% | 47.3 | 0.00% |
| S2 | 4 | 99.47% | 53.0 | 0.01% |
| S3 | 4 | 98.95% | 117.8 | 0.02% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7276524.181] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7438044.753] rms    7 max   11 freq  -6505 +/-   9 delay    26 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[1130302.283] rms   34 max   60 freq  +2245 +/-  45 delay    49 +/-   0`
- Connectivity: 11 / 11 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 0 |
| S2 | 0 | 0 | 0 |
| S3 | 0 | 0 | 17 |

Switch queue drops (`ethtool -S` Q DROP) on the 17 gated ports: sw01/p4 +1172, sw02/p4 +3980, sw07/p4 +370.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 2 | S1→S2 | 6 | 400 | 200.0 | 200.0 | 51.0 | 150000 | 148408 | 98.94% | 38.9 / 67.1 / 320838.9 | 2992.5 | 4.3 | 13 | 0.01% | 0 |
| 2 | 4 | S1→S3 | 6 | 300 | 800.0 | 800.0 | 66.3 | 37500 | 37102 | 98.94% | 45.7 / 72.3 / 320904.1 | 2878.1 | 17.5 | 3 | 0.01% | 0 |
| 3 | 5 | S3→S2 | 7 | 100 | 200.0 | 200.0 | 38.2 | 149991 | 149991 | 100.00% | 26.1 / 26.3 / 26.5 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 4 | 7 | S3→S1 | 6 | 500 | 800.0 | 800.0 | 79.1 | 37497 | 37106 | 98.96% | 64.2 / 150.1 / 320864.6 | 5207.2 | 17.4 | 10 | 0.03% | 0 |
| 5 | 8 | S2→S1 | 7 | 300 | 200.0 | 200.0 | 39.4 | 150000 | 150000 | 100.00% | 27.4 / 27.6 / 27.7 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 6 | 9 | S3→S2 | 6 | 200 | 400.0 | 400.0 | 43.0 | 74995 | 74214 | 98.96% | 17.3 / 107.2 / 320817.3 | 5330.7 | 8.7 | 21 | 0.03% | 0 |
| 7 | 11 | S2→S1 | 7 | 300 | 800.0 | 800.0 | 39.4 | 37500 | 37500 | 100.00% | 21.7 / 24.8 / 25.3 | 0.3 | 0.2 | 0 | 0.00% | 0 |
| 8 | 12 | S1→S3 | 6 | 500 | 200.0 | 200.0 | 79.1 | 150000 | 148408 | 98.94% | 67.1 / 93.1 / 320949.9 | 2875.8 | 4.3 | 13 | 0.01% | 0 |
| 9 | 14 | S1→S2 | 7 | 200 | 400.0 | 400.0 | 36.9 | 75000 | 75000 | 100.00% | 24.8 / 25.0 / 25.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 10 | 18 | S2→S3 | 6 | 300 | 800.0 | 800.0 | 54.5 | 37500 | 37130 | 99.01% | 33.8 / 291.8 / 320762.6 | 8921.5 | 17.3 | 31 | 0.08% | 0 |
| 11 | 19 | S1→S3 | 6 | 400 | 800.0 | 800.0 | 74.0 | 37500 | 37102 | 98.94% | 62.0 / 88.0 / 320881.7 | 2877.8 | 17.3 | 3 | 0.01% | 0 |
