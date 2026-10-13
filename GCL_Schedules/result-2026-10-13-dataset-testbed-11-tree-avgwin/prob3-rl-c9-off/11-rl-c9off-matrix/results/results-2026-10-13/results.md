# Traffic run: result-2026-10-13-dataset-testbed-11-tree-avgwin/prob3-rl-c9-off/11-rl-c9off-matrix, 2026-10-13 13:20

25 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **1687457 / 1687457 packets (100.00%)**
- Deadline misses: **0 (0.00% of received)**; flows with zero misses: 25 / 25

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 12 | 100.00% | 102.5 | 0.00% |
| S2 | 7 | 100.00% | 74.3 | 0.00% |
| S3 | 6 | 100.00% | 107.5 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7276524.181] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7437438.094] rms   10 max   15 freq  -6555 +/-  14 delay    24 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[1129695.374] rms   42 max   78 freq  +2300 +/-  55 delay    49 +/-   0`
- Connectivity: 25 / 25 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 0 |
| S2 | 0 | 0 | 7 |
| S3 | 0 | 0 | 36 |

Switch queue drops (`ethtool -S` Q DROP) on the 17 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S1→S2 | 6 | 500 | 200.0 | 200.0 | 79.1 | 150000 | 150000 | 100.00% | 66.8 / 67.0 / 70.3 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 2 | 2 | S3→S2 | 6 | 400 | 200.0 | 200.0 | 95.8 | 149991 | 149991 | 100.00% | 66.9 / 71.1 / 71.3 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 3 | 3 | S1→S2 | 7 | 500 | 400.0 | 400.0 | 83.6 | 75000 | 75000 | 100.00% | 71.2 / 71.4 / 71.6 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 4 | 4 | S2→S3 | 6 | 500 | 400.0 | 400.0 | 108.2 | 74999 | 74999 | 100.00% | 28.0 / 28.7 / 29.6 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 5 | 5 | S2→S1 | 7 | 200 | 200.0 | 200.0 | 79.1 | 149999 | 149999 | 100.00% | 53.2 / 53.6 / 54.0 | 0.1 | 0.1 | 0 | 0.00% | 0 |
| 6 | 7 | S2→S1 | 7 | 300 | 800.0 | 800.0 | 79.1 | 37500 | 37500 | 100.00% | 28.5 / 29.1 / 29.9 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 7 | 8 | S3→S2 | 6 | 500 | 200.0 | 200.0 | 96.4 | 149990 | 149990 | 100.00% | 84.0 / 84.2 / 84.4 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 8 | 9 | S3→S2 | 7 | 100 | 800.0 | 800.0 | 95.8 | 37499 | 37499 | 100.00% | 83.4 / 83.6 / 83.8 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 9 | 10 | S3→S1 | 7 | 300 | 400.0 | 400.0 | 145.7 | 74995 | 74995 | 100.00% | 107.7 / 108.3 / 109.3 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 10 | 12 | S2→S3 | 6 | 300 | 400.0 | 400.0 | 126.4 | 74999 | 74999 | 100.00% | 58.5 / 86.5 / 114.6 | 27.8 | 55.7 | 0 | 0.00% | 0 |
| 11 | 13 | S1→S3 | 7 | 300 | 800.0 | 800.0 | 366.4 | 37500 | 37500 | 100.00% | 308.4 / 308.6 / 308.8 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 12 | 15 | S2→S3 | 6 | 300 | 800.0 | 800.0 | 134.1 | 37500 | 37500 | 100.00% | 87.8 / 88.2 / 88.8 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 13 | 16 | S3→S1 | 7 | 500 | 400.0 | 400.0 | 193.0 | 74995 | 74995 | 100.00% | 180.7 / 180.9 / 181.1 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 14 | 17 | S1→S2 | 6 | 400 | 400.0 | 400.0 | 109.8 | 75000 | 75000 | 100.00% | 97.5 / 97.7 / 97.9 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 15 | 18 | S2→S3 | 7 | 500 | 800.0 | 800.0 | 95.8 | 37500 | 37500 | 100.00% | 83.4 / 83.6 / 83.8 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 16 | 19 | S3→S1 | 7 | 400 | 800.0 | 800.0 | 380.2 | 37498 | 37498 | 100.00% | 172.1 / 172.3 / 172.5 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 17 | 20 | S1→S2 | 7 | 500 | 400.0 | 400.0 | 84.2 | 75000 | 75000 | 100.00% | 50.4 / 50.6 / 50.8 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 18 | 23 | S2→S1 | 6 | 300 | 800.0 | 800.0 | 115.8 | 37500 | 37500 | 100.00% | 103.6 / 103.8 / 104.0 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 19 | 25 | S2→S1 | 6 | 300 | 800.0 | 800.0 | 175.7 | 37499 | 37499 | 100.00% | 84.4 / 84.9 / 88.6 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 20 | 28 | S2→S1 | 7 | 400 | 800.0 | 800.0 | 79.0 | 37499 | 37499 | 100.00% | 54.1 / 61.7 / 61.9 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 21 | 36 | S2→S1 | 6 | 500 | 800.0 | 800.0 | 183.0 | 37499 | 37499 | 100.00% | 170.8 / 171.0 / 171.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 22 | 37 | S3→S1 | 6 | 500 | 800.0 | 800.0 | 145.6 | 37499 | 37499 | 100.00% | 133.3 / 133.5 / 133.7 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 23 | 39 | S3→S1 | 6 | 500 | 400.0 | 400.0 | 216.0 | 74997 | 74997 | 100.00% | 108.7 / 121.4 / 132.7 | 8.6 | 17.2 | 0 | 0.00% | 0 |
| 24 | 46 | S1→S3 | 6 | 500 | 800.0 | 800.0 | 233.3 | 37500 | 37500 | 100.00% | 148.9 / 149.4 / 149.9 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 25 | 50 | S2→S1 | 7 | 400 | 800.0 | 800.0 | 79.0 | 37499 | 37499 | 100.00% | 44.7 / 52.3 / 52.5 | 0.1 | 0.0 | 0 | 0.00% | 0 |
