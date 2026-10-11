# Traffic run: result-2026-10-09-dataset-testbed-4-avgwin/smt-c9-off/4-t3600-c9off-minlat, 2026-10-10 19:32

20 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **1012445 / 1012445 packets (100.00%)**
- Deadline misses: **0 (0.00% of received)**; flows with zero misses: 11 / 20

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 1 | 100.00% | 67.0 | 0.00% |
| S2 | 4 | 100.00% | 74.4 | 0.00% |
| S3 | 6 | 100.00% | 105.0 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7192691.373] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7200571.512] rms   18 max   24 freq  -6209 +/-  14 delay    25 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[892828.667] rms   29 max   59 freq  +3075 +/-  34 delay    47 +/-   0`
- Connectivity: 11 / 11 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 39 |
| S2 | 0 | 0 | 0 |
| S3 | 0 | 0 | 16 |

Switch queue drops (`ethtool -S` Q DROP) on the 17 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S3→S2 | 7 | 300 | 400.0 | 400.0 | 95.8 | 74996 | 74996 | 100.00% | 83.4 / 83.6 / 83.8 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 2 | 2 | S1→S2 | None | 300 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 3 | 3 | S2→S3 | 7 | 100 | 400.0 | 400.0 | 95.8 | 75000 | 75000 | 100.00% | 83.4 / 83.6 / 83.8 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 4 | 4 | S3→S2 | None | 400 | 800.0 | 800.0 | – | 0 | – | – | – | – | – | – | – | – |
| 5 | 5 | S3→S1 | None | 200 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 6 | 6 | S1→S3 | 6 | 300 | 800.0 | 800.0 | 145.7 | 37495 | 37495 | 100.00% | 133.3 / 133.5 / 133.7 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 7 | 7 | S1→S3 | None | 100 | 800.0 | 800.0 | – | 0 | – | – | – | – | – | – | – | – |
| 8 | 8 | S2→S3 | 6 | 500 | 200.0 | 200.0 | 95.8 | 150000 | 150000 | 100.00% | 83.4 / 83.6 / 83.8 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 9 | 9 | S1→S3 | 6 | 400 | 800.0 | 800.0 | 145.7 | 37498 | 37498 | 100.00% | 133.3 / 133.5 / 133.7 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 10 | 10 | S3→S2 | 7 | 400 | 400.0 | 400.0 | 95.8 | 74996 | 74996 | 100.00% | 83.4 / 83.6 / 83.8 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 11 | 11 | S2→S1 | None | 200 | 800.0 | 800.0 | – | 0 | – | – | – | – | – | – | – | – |
| 12 | 12 | S2→S3 | None | 100 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 13 | 13 | S1→S2 | 6 | 400 | 200.0 | 200.0 | 79.1 | 149987 | 149987 | 100.00% | 66.8 / 67.0 / 83.8 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 14 | 14 | S3→S2 | 6 | 500 | 200.0 | 200.0 | 95.8 | 149992 | 149992 | 100.00% | 72.2 / 72.6 / 73.0 | 0.1 | 0.1 | 0 | 0.00% | 0 |
| 15 | 15 | S3→S2 | None | 300 | 200.0 | 200.0 | – | 0 | – | – | – | – | – | – | – | – |
| 16 | 16 | S1→S2 | None | 100 | 200.0 | 200.0 | – | 0 | – | – | – | – | – | – | – | – |
| 17 | 17 | S2→S1 | None | 400 | 200.0 | 200.0 | – | 0 | – | – | – | – | – | – | – | – |
| 18 | 18 | S2→S1 | 6 | 300 | 800.0 | 800.0 | 79.1 | 37500 | 37500 | 100.00% | 66.8 / 67.0 / 67.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 19 | 19 | S2→S3 | 7 | 500 | 400.0 | 400.0 | 95.8 | 75000 | 75000 | 100.00% | 83.4 / 83.6 / 83.8 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 20 | 20 | S1→S3 | 6 | 100 | 200.0 | 200.0 | 145.7 | 149981 | 149981 | 100.00% | 133.3 / 133.6 / 133.7 | 0.1 | 0.0 | 0 | 0.00% | 0 |
