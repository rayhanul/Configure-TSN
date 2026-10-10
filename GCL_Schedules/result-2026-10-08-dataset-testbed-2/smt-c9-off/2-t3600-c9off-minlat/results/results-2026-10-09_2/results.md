# Traffic run: result-2026-10-08-dataset-testbed-2/smt-c9-off/2-t3600-c9off-minlat, 2026-10-09 16:52

20 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **937473 / 1012500 packets (92.59%)**
- Deadline misses: **75001 (8.00% of received)**; flows with zero misses: 8 / 20

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 4 | 100.00% | 150.4 | 22.22% |
| S2 | 5 | 100.00% | 70.5 | 0.00% |
| S3 | 2 | 33.33% | 33.9 | 0.02% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7101051.924] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7104562.030] rms   14 max   25 freq  -6414 +/-  19 delay    18 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[796819.184] rms   29 max   68 freq  +2970 +/-  39 delay    45 +/-   0`
- Connectivity: 10 / 11 sender routes answered ping (failed: 11)

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 0 |
| S2 | 0 | 3 | 0 |
| S3 | 0 | 24 | 0 |

Switch queue drops (`ethtool -S` Q DROP) on the 27 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S1→S2 | 7 | 500 | 200.0 | 200.0 | 79.0 | 150000 | 150000 | 100.00% | 66.7 / 67.0 / 67.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 2 | 2 | S3→S2 | None | 100 | 800.0 | 800.0 | – | 0 | – | – | – | – | – | – | – | – |
| 3 | 3 | S1→S2 | None | 500 | 200.0 | 200.0 | – | 0 | – | – | – | – | – | – | – | – |
| 4 | 4 | S1→S3 | 6 | 400 | 800.0 | 800.0 | 45.8 | 37500 | 37500 | 100.00% | 33.5 / 33.9 / 833.7 | 10.9 | 0.3 | 7 | 0.02% | 0 |
| 5 | 5 | S1→S2 | None | 500 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 6 | 6 | S2→S1 | None | 100 | 800.0 | 800.0 | – | 0 | – | – | – | – | – | – | – | – |
| 7 | 7 | S3→S1 | 6 | 300 | 400.0 | 400.0 | 45.8 | 75000 | 74995 | 99.99% | 36.4 / 433.7 / 433.9 | 1.5 | 0.0 | 74994 | 100.00% | 0 |
| 8 | 8 | S1→S2 | None | 500 | 800.0 | 800.0 | – | 0 | – | – | – | – | – | – | – | – |
| 9 | 9 | S1→S2 | 7 | 400 | 200.0 | 200.0 | 79.7 | 150000 | 150000 | 100.00% | 67.4 / 67.6 / 67.8 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 10 | 10 | S3→S2 | 6 | 300 | 800.0 | 800.0 | 79.0 | 37500 | 37498 | 99.99% | 66.7 / 67.0 / 67.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 11 | 11 | S2→S3 | 7 | 300 | 400.0 | 400.0 | 83.5 | 75000 | 0 | 0.00% | – | – | – | – | – | – |
| 12 | 12 | S2→S1 | 6 | 200 | 800.0 | 800.0 | 79.0 | 37500 | 37499 | 100.00% | 66.8 / 67.0 / 67.1 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 13 | 13 | S3→S1 | None | 100 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 14 | 14 | S3→S2 | 6 | 500 | 200.0 | 200.0 | 91.8 | 150000 | 149988 | 99.99% | 79.5 / 79.8 / 80.0 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 15 | 15 | S2→S3 | None | 400 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 16 | 16 | S2→S1 | 7 | 100 | 400.0 | 400.0 | 79.0 | 75000 | 74999 | 100.00% | 66.8 / 67.0 / 67.1 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 17 | 17 | S3→S2 | None | 200 | 200.0 | 200.0 | – | 0 | – | – | – | – | – | – | – | – |
| 18 | 18 | S2→S1 | 7 | 400 | 200.0 | 200.0 | 83.5 | 150000 | 149999 | 100.00% | 71.3 / 71.4 / 71.6 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 19 | 19 | S2→S1 | None | 100 | 200.0 | 200.0 | – | 0 | – | – | – | – | – | – | – | – |
| 20 | 20 | S3→S2 | 7 | 300 | 400.0 | 400.0 | 79.0 | 75000 | 74995 | 99.99% | 66.7 / 67.0 / 67.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
