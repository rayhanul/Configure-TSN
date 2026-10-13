# Traffic run: result-2026-10-13-dataset-testbed-13-tree-avgwin/rl-c9-off/13-matrix-c9off, 2026-10-13 13:53

20 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **1012484 / 1012484 packets (100.00%)**
- Deadline misses: **0 (0.00% of received)**; flows with zero misses: 11 / 20

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 2 | 100.00% | 20.9 | 0.00% |
| S2 | 4 | 100.00% | 32.5 | 0.00% |
| S3 | 5 | 100.00% | 93.1 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7276524.181] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7439398.781] rms    6 max   14 freq  -6477 +/-   8 delay    24 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[1131655.811] rms   46 max   90 freq  +2214 +/-  62 delay    50 +/-   0`
- Connectivity: 11 / 11 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 0 |
| S2 | 0 | 0 | 1 |
| S3 | 0 | 0 | 15 |

Switch queue drops (`ethtool -S` Q DROP) on the 17 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S3→S2 | None | 400 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 2 | 2 | S1→S2 | None | 200 | 800.0 | 800.0 | – | 0 | – | – | – | – | – | – | – | – |
| 3 | 3 | S1→S3 | 7 | 400 | 400.0 | 400.0 | 145.7 | 75000 | 75000 | 100.00% | 97.8 / 98.0 / 98.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 4 | 4 | S2→S3 | None | 300 | 800.0 | 800.0 | – | 0 | – | – | – | – | – | – | – | – |
| 5 | 5 | S3→S2 | 6 | 500 | 200.0 | 200.0 | 95.8 | 149993 | 149993 | 100.00% | 28.0 / 28.7 / 30.7 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 6 | 6 | S3→S1 | None | 400 | 800.0 | 800.0 | – | 0 | – | – | – | – | – | – | – | – |
| 7 | 7 | S3→S1 | None | 100 | 200.0 | 200.0 | – | 0 | – | – | – | – | – | – | – | – |
| 8 | 8 | S3→S2 | 6 | 500 | 800.0 | 800.0 | 95.8 | 37497 | 37497 | 100.00% | 72.3 / 72.6 / 73.6 | 0.1 | 0.1 | 0 | 0.00% | 0 |
| 9 | 9 | S3→S2 | 6 | 200 | 400.0 | 400.0 | 95.8 | 74995 | 74995 | 100.00% | 57.4 / 57.8 / 58.2 | 0.1 | 0.2 | 0 | 0.00% | 0 |
| 10 | 10 | S2→S1 | 6 | 300 | 200.0 | 200.0 | 79.1 | 150000 | 150000 | 100.00% | 15.9 / 16.6 / 18.5 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 11 | 11 | S2→S3 | None | 500 | 200.0 | 200.0 | – | 0 | – | – | – | – | – | – | – | – |
| 12 | 12 | S2→S3 | None | 400 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 13 | 13 | S2→S1 | 7 | 500 | 400.0 | 400.0 | 79.1 | 75000 | 75000 | 100.00% | 29.3 / 29.5 / 29.7 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 14 | 14 | S1→S2 | 6 | 200 | 200.0 | 200.0 | 79.1 | 150000 | 150000 | 100.00% | 12.8 / 13.5 / 23.5 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 15 | 15 | S1→S3 | 6 | 100 | 800.0 | 800.0 | 159.1 | 37500 | 37500 | 100.00% | 123.7 / 123.9 / 124.1 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 16 | 16 | S1→S3 | None | 100 | 200.0 | 200.0 | – | 0 | – | – | – | – | – | – | – | – |
| 17 | 17 | S2→S3 | 7 | 100 | 800.0 | 800.0 | 96.4 | 37499 | 37499 | 100.00% | 84.0 / 84.2 / 84.5 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 18 | 18 | S2→S1 | None | 400 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 19 | 19 | S2→S3 | 6 | 200 | 200.0 | 200.0 | 95.8 | 150000 | 150000 | 100.00% | 83.4 / 83.6 / 83.8 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 20 | 20 | S2→S3 | 6 | 300 | 400.0 | 400.0 | 108.6 | 75000 | 75000 | 100.00% | 96.2 / 96.4 / 96.6 | 0.1 | 0.0 | 0 | 0.00% | 0 |
