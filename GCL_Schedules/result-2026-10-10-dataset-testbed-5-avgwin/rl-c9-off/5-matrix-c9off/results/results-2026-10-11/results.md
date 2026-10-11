# Traffic run: result-2026-10-10-dataset-testbed-5-avgwin/rl-c9-off/5-matrix-c9off, 2026-10-11 00:16

20 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **824984 / 824985 packets (100.00%)**
- Deadline misses: **0 (0.00% of received)**; flows with zero misses: 10 / 20

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 1 | 100.00% | 34.2 | 0.00% |
| S2 | 6 | 100.00% | 69.0 | 0.00% |
| S3 | 3 | 100.00% | 69.2 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7192691.373] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7217579.596] rms   10 max   20 freq  -6219 +/-  14 delay    26 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[909837.254] rms   42 max   67 freq  +3032 +/-  58 delay    50 +/-   0`
- Connectivity: 10 / 10 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 0 |
| S2 | 0 | 0 | 0 |
| S3 | 0 | 1 | 15 |

Switch queue drops (`ethtool -S` Q DROP) on the 17 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S3→S1 | None | 200 | 800.0 | 800.0 | – | 0 | – | – | – | – | – | – | – | – |
| 2 | 2 | S2→S3 | 6 | 300 | 200.0 | 200.0 | 95.8 | 150000 | 150000 | 100.00% | 19.8 / 52.3 / 84.1 | 31.6 | 63.2 | 0 | 0.00% | 0 |
| 3 | 3 | S1→S2 | 6 | 100 | 800.0 | 800.0 | 84.2 | 37500 | 37500 | 100.00% | 49.9 / 50.1 / 50.3 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 4 | 4 | S1→S3 | None | 300 | 800.0 | 800.0 | – | 0 | – | – | – | – | – | – | – | – |
| 5 | 5 | S2→S3 | 7 | 100 | 800.0 | 800.0 | 95.8 | 37500 | 37500 | 100.00% | 83.7 / 83.9 / 84.1 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 6 | 6 | S2→S3 | None | 200 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 7 | 7 | S3→S2 | None | 500 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 8 | 8 | S3→S1 | None | 500 | 200.0 | 200.0 | – | 0 | – | – | – | – | – | – | – | – |
| 9 | 9 | S2→S1 | 7 | 500 | 400.0 | 400.0 | 79.1 | 75000 | 75000 | 100.00% | 33.6 / 34.2 / 35.0 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 10 | 10 | S1→S2 | 7 | 500 | 200.0 | 200.0 | 79.1 | 150000 | 150000 | 100.00% | 67.0 / 67.2 / 67.4 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 11 | 11 | S2→S3 | None | 500 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 12 | 12 | S3→S2 | 7 | 500 | 200.0 | 200.0 | 95.8 | 149992 | 149991 | 100.00% | 83.6 / 83.9 / 84.1 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 13 | 13 | S1→S3 | 6 | 400 | 800.0 | 800.0 | 145.7 | 37500 | 37500 | 100.00% | 121.6 / 122.0 / 122.4 | 0.1 | 0.2 | 0 | 0.00% | 0 |
| 14 | 14 | S1→S3 | None | 100 | 200.0 | 200.0 | – | 0 | – | – | – | – | – | – | – | – |
| 15 | 15 | S2→S3 | None | 500 | 200.0 | 200.0 | – | 0 | – | – | – | – | – | – | – | – |
| 16 | 16 | S3→S2 | 7 | 200 | 800.0 | 800.0 | 97.0 | 37498 | 37498 | 100.00% | 38.0 / 42.3 / 42.5 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 17 | 17 | S1→S2 | 6 | 400 | 400.0 | 400.0 | 83.6 | 75000 | 75000 | 100.00% | 71.5 / 71.7 / 71.9 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 18 | 18 | S1→S3 | None | 400 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 19 | 19 | S3→S2 | 7 | 500 | 400.0 | 400.0 | 96.4 | 74995 | 74995 | 100.00% | 58.8 / 63.1 / 63.3 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 20 | 20 | S1→S2 | None | 400 | 200.0 | 200.0 | – | 0 | – | – | – | – | – | – | – | – |
