# Traffic run: result-2026-10-09-dataset-testbed-4-avgwin/rl-c9-off/4-matrix-c9off, 2026-10-10 09:32

20 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **1012444 / 1012493 packets (100.00%)**
- Deadline misses: **0 (0.00% of received)**; flows with zero misses: 11 / 20

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 1 | 100.00% | 41.8 | 0.00% |
| S2 | 4 | 99.99% | 59.5 | 0.00% |
| S3 | 6 | 100.00% | 103.6 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7160963.398] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7164545.492] rms   14 max   25 freq  -6183 +/-  20 delay    19 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[856803.147] rms   33 max   69 freq  +2964 +/-  42 delay    49 +/-   0`
- Connectivity: 11 / 11 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 19 | 7 |
| S2 | 0 | 6 | 0 |
| S3 | 0 | 25 | 0 |

Switch queue drops (`ethtool -S` Q DROP) on the 17 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S3→S2 | 7 | 300 | 400.0 | 400.0 | 95.8 | 75000 | 74994 | 99.99% | 83.4 / 83.6 / 108.6 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 2 | 2 | S1→S2 | None | 300 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 3 | 3 | S2→S3 | 7 | 100 | 400.0 | 400.0 | 95.8 | 75000 | 74998 | 100.00% | 83.4 / 83.6 / 83.9 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 4 | 4 | S3→S2 | None | 400 | 800.0 | 800.0 | – | 0 | – | – | – | – | – | – | – | – |
| 5 | 5 | S3→S1 | None | 200 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 6 | 6 | S1→S3 | 6 | 300 | 800.0 | 800.0 | 145.7 | 37499 | 37497 | 99.99% | 133.4 / 133.6 / 133.8 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 7 | 7 | S1→S3 | None | 100 | 800.0 | 800.0 | – | 0 | – | – | – | – | – | – | – | – |
| 8 | 8 | S2→S3 | 6 | 500 | 200.0 | 200.0 | 95.8 | 150000 | 149997 | 100.00% | 83.4 / 102.8 / 122.3 | 19.2 | 38.4 | 0 | 0.00% | 0 |
| 9 | 9 | S1→S3 | 6 | 400 | 800.0 | 800.0 | 145.7 | 37499 | 37496 | 99.99% | 111.0 / 111.2 / 111.4 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 10 | 10 | S3→S2 | 7 | 400 | 400.0 | 400.0 | 95.8 | 75000 | 74994 | 99.99% | 83.4 / 83.6 / 86.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 11 | 11 | S2→S1 | None | 200 | 800.0 | 800.0 | – | 0 | – | – | – | – | – | – | – | – |
| 12 | 12 | S2→S3 | None | 100 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 13 | 13 | S1→S2 | 6 | 400 | 200.0 | 200.0 | 79.1 | 149997 | 149990 | 100.00% | 19.0 / 20.0 / 80.4 | 0.4 | 0.5 | 0 | 0.00% | 0 |
| 14 | 14 | S3→S2 | 6 | 500 | 200.0 | 200.0 | 95.8 | 150000 | 149987 | 99.99% | 28.0 / 74.9 / 121.3 | 46.2 | 92.3 | 0 | 0.00% | 0 |
| 15 | 15 | S3→S2 | None | 300 | 200.0 | 200.0 | – | 0 | – | – | – | – | – | – | – | – |
| 16 | 16 | S1→S2 | None | 100 | 200.0 | 200.0 | – | 0 | – | – | – | – | – | – | – | – |
| 17 | 17 | S2→S1 | None | 400 | 200.0 | 200.0 | – | 0 | – | – | – | – | – | – | – | – |
| 18 | 18 | S2→S1 | 6 | 300 | 800.0 | 800.0 | 79.1 | 37500 | 37500 | 100.00% | 41.2 / 41.8 / 42.3 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 19 | 19 | S2→S3 | 7 | 500 | 400.0 | 400.0 | 95.8 | 75000 | 74999 | 100.00% | 83.4 / 83.6 / 83.9 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 20 | 20 | S1→S3 | 6 | 100 | 200.0 | 200.0 | 145.7 | 149998 | 149992 | 100.00% | 95.9 / 114.8 / 133.8 | 18.7 | 37.4 | 0 | 0.00% | 0 |
