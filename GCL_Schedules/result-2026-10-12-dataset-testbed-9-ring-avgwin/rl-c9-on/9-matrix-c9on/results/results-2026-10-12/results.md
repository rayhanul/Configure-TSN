# Traffic run: result-2026-10-12-dataset-testbed-9-ring-avgwin/rl-c9-on/9-matrix-c9on, 2026-10-12 16:14

20 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **862432 / 862442 packets (100.00%)**
- Deadline misses: **0 (0.00% of received)**; flows with zero misses: 11 / 20

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 6 | 100.00% | 17.7 | 0.00% |
| S2 | 2 | 100.00% | 33.4 | 0.00% |
| S3 | 3 | 100.00% | 17.8 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7276524.181] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7361457.977] rms    8 max   17 freq  -6383 +/-  10 delay    24 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[1053714.368] rms   25 max   67 freq  +2163 +/-  34 delay    50 +/-   0`
- Connectivity: 11 / 11 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 7 |
| S2 | 0 | 0 | 0 |
| S3 | 0 | 10 | 51 |

Switch queue drops (`ethtool -S` Q DROP) on the 19 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S3→S1 | 6 | 200 | 800.0 | 800.0 | 24.7 | 37493 | 37491 | 99.99% | 12.4 / 12.6 / 12.7 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 2 | 2 | S3→S2 | None | 100 | 800.0 | 800.0 | – | 0 | – | – | – | – | – | – | – | – |
| 3 | 3 | S3→S2 | None | 200 | 200.0 | 200.0 | – | 0 | – | – | – | – | – | – | – | – |
| 4 | 4 | S3→S1 | 7 | 100 | 400.0 | 400.0 | 33.4 | 74985 | 74983 | 100.00% | 21.0 / 21.2 / 21.4 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 5 | 5 | S1→S3 | None | 300 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 6 | 6 | S2→S3 | 6 | 100 | 200.0 | 200.0 | 40.7 | 150000 | 150000 | 100.00% | 17.4 / 18.1 / 20.3 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 7 | 7 | S2→S1 | 6 | 100 | 400.0 | 400.0 | 33.0 | 75000 | 75000 | 100.00% | 9.7 / 10.3 / 11.1 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 8 | 8 | S2→S3 | 6 | 400 | 800.0 | 800.0 | 51.0 | 37500 | 37500 | 100.00% | 35.6 / 36.0 / 36.4 | 0.1 | 0.2 | 0 | 0.00% | 0 |
| 9 | 9 | S3→S2 | 7 | 500 | 800.0 | 800.0 | 54.2 | 37495 | 37493 | 99.99% | 41.8 / 42.0 / 42.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 10 | 10 | S3→S1 | 6 | 400 | 200.0 | 200.0 | 27.9 | 149976 | 149972 | 100.00% | 9.7 / 10.2 / 10.6 | 0.2 | 0.1 | 0 | 0.00% | 0 |
| 11 | 11 | S2→S1 | None | 300 | 800.0 | 800.0 | – | 0 | – | – | – | – | – | – | – | – |
| 12 | 12 | S1→S2 | 6 | 200 | 800.0 | 800.0 | 36.9 | 37499 | 37499 | 100.00% | 24.5 / 24.7 / 24.9 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 13 | 13 | S2→S3 | None | 300 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 14 | 14 | S1→S3 | 6 | 400 | 200.0 | 200.0 | 27.9 | 149994 | 149994 | 100.00% | 12.6 / 13.0 / 20.2 | 0.1 | 0.1 | 0 | 0.00% | 0 |
| 15 | 15 | S2→S1 | None | 500 | 200.0 | 200.0 | – | 0 | – | – | – | – | – | – | – | – |
| 16 | 16 | S2→S1 | 6 | 500 | 400.0 | 400.0 | 50.0 | 75000 | 75000 | 100.00% | 33.2 / 35.7 / 38.0 | 2.1 | 4.3 | 0 | 0.00% | 0 |
| 17 | 17 | S2→S1 | None | 500 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 18 | 18 | S3→S1 | None | 500 | 200.0 | 200.0 | – | 0 | – | – | – | – | – | – | – | – |
| 19 | 19 | S3→S2 | None | 300 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 20 | 20 | S2→S1 | 6 | 200 | 800.0 | 800.0 | 36.9 | 37500 | 37500 | 100.00% | 24.6 / 24.7 / 24.9 | 0.1 | 0.0 | 0 | 0.00% | 0 |
