# Traffic run: result-2026-10-13-dataset-testbed-13-tree-avgwin/prob3-heuristic-c9-off/13-heuristic-c9off-matrix, 2026-10-13 13:57

23 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **1574883 / 1574904 packets (100.00%)**
- Deadline misses: **0 (0.00% of received)**; flows with zero misses: 23 / 23

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 6 | 100.00% | 70.4 | 0.00% |
| S2 | 10 | 100.00% | 52.7 | 0.00% |
| S3 | 7 | 100.00% | 77.9 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7276524.181] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7439640.093] rms   11 max   18 freq  -6463 +/-  15 delay    26 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[1131897.149] rms   26 max   45 freq  +2265 +/-  36 delay    50 +/-   0`
- Connectivity: 23 / 23 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 0 |
| S2 | 0 | 0 | 0 |
| S3 | 0 | 35 | 96 |

Switch queue drops (`ethtool -S` Q DROP) on the 17 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S3→S2 | 6 | 400 | 400.0 | 400.0 | 95.7 | 74986 | 74984 | 100.00% | 35.4 / 44.4 / 53.5 | 8.6 | 17.2 | 0 | 0.00% | 0 |
| 2 | 2 | S1→S2 | 7 | 200 | 800.0 | 800.0 | 312.3 | 37500 | 37500 | 100.00% | 100.0 / 100.3 / 101.4 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 3 | 3 | S1→S3 | 7 | 400 | 400.0 | 400.0 | 145.7 | 75000 | 75000 | 100.00% | 133.3 / 133.5 / 133.8 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 4 | 5 | S3→S2 | 6 | 500 | 200.0 | 200.0 | 95.8 | 149976 | 149971 | 100.00% | 28.0 / 31.5 / 40.5 | 4.7 | 5.5 | 0 | 0.00% | 0 |
| 5 | 6 | S3→S1 | 7 | 400 | 800.0 | 800.0 | 412.5 | 37495 | 37494 | 100.00% | 313.5 / 313.7 / 313.9 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 6 | 8 | S3→S2 | 6 | 500 | 800.0 | 800.0 | 95.8 | 37494 | 37492 | 99.99% | 61.2 / 61.6 / 62.2 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 7 | 9 | S3→S2 | 6 | 200 | 400.0 | 400.0 | 95.8 | 74991 | 74988 | 100.00% | 69.9 / 70.2 / 71.1 | 0.1 | 0.2 | 0 | 0.00% | 0 |
| 8 | 10 | S2→S1 | 6 | 300 | 200.0 | 200.0 | 79.1 | 150000 | 150000 | 100.00% | 15.9 / 16.6 / 17.4 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 9 | 13 | S2→S1 | 7 | 500 | 400.0 | 400.0 | 79.1 | 75000 | 75000 | 100.00% | 29.4 / 29.5 / 29.7 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 10 | 14 | S1→S2 | 6 | 200 | 200.0 | 200.0 | 79.1 | 150000 | 150000 | 100.00% | 12.8 / 14.1 / 31.3 | 1.1 | 1.3 | 0 | 0.00% | 0 |
| 11 | 15 | S1→S3 | 6 | 100 | 800.0 | 800.0 | 159.1 | 37500 | 37500 | 100.00% | 123.7 / 123.9 / 124.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 12 | 17 | S2→S3 | 7 | 100 | 800.0 | 800.0 | 96.4 | 37500 | 37500 | 100.00% | 84.1 / 84.3 / 84.5 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 13 | 19 | S2→S3 | 6 | 200 | 200.0 | 200.0 | 95.8 | 150000 | 150000 | 100.00% | 15.9 / 16.8 / 17.9 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 14 | 20 | S2→S3 | 6 | 300 | 400.0 | 400.0 | 108.6 | 75000 | 75000 | 100.00% | 96.2 / 96.4 / 96.7 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 15 | 26 | S3→S1 | 6 | 300 | 800.0 | 800.0 | 203.8 | 37492 | 37490 | 99.99% | 116.1 / 116.5 / 117.3 | 0.1 | 0.2 | 0 | 0.00% | 0 |
| 16 | 31 | S1→S3 | 6 | 400 | 800.0 | 800.0 | 151.7 | 37500 | 37500 | 100.00% | 104.5 / 104.7 / 105.0 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 17 | 32 | S2→S1 | 7 | 400 | 800.0 | 800.0 | 150.1 | 37500 | 37500 | 100.00% | 52.0 / 52.7 / 54.5 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 18 | 37 | S3→S1 | 6 | 200 | 800.0 | 800.0 | 201.3 | 37492 | 37490 | 99.99% | 95.6 / 96.0 / 112.2 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 19 | 41 | S1→S2 | 6 | 500 | 400.0 | 400.0 | 134.7 | 75000 | 75000 | 100.00% | 22.5 / 61.9 / 101.3 | 38.8 | 77.6 | 0 | 0.00% | 0 |
| 20 | 44 | S1→S3 | 6 | 400 | 800.0 | 800.0 | 151.7 | 37500 | 37500 | 100.00% | 95.1 / 95.3 / 95.5 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 21 | 45 | S3→S2 | 6 | 300 | 400.0 | 400.0 | 95.7 | 74985 | 74983 | 100.00% | 19.9 / 20.7 / 23.9 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 22 | 48 | S3→S2 | 7 | 200 | 800.0 | 800.0 | 612.5 | 37493 | 37491 | 99.99% | 101.8 / 102.0 / 103.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 23 | 49 | S1→S2 | 7 | 100 | 800.0 | 800.0 | 224.6 | 37500 | 37500 | 100.00% | 212.4 / 212.6 / 212.8 | 0.1 | 0.0 | 0 | 0.00% | 0 |
