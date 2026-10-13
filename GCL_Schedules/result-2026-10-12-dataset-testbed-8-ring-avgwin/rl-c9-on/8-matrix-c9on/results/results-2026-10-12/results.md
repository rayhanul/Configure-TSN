# Traffic run: result-2026-10-12-dataset-testbed-8-ring-avgwin/rl-c9-on/8-matrix-c9on, 2026-10-12 15:53

20 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **862115 / 862485 packets (99.96%)**
- Deadline misses: **31 (0.00% of received)**; flows with zero misses: 9 / 20

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 4 | 100.00% | 14.0 | 0.00% |
| S2 | 1 | 100.00% | 28.4 | 0.00% |
| S3 | 5 | 99.92% | 41.6 | 0.01% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7276524.181] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7360215.214] rms    9 max   14 freq  -6385 +/-  11 delay    24 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[1052472.983] rms   22 max   58 freq  +2219 +/-  30 delay    50 +/-   0`
- Connectivity: 10 / 10 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 0 |
| S2 | 0 | 0 | 0 |
| S3 | 0 | 0 | 15 |

Switch queue drops (`ethtool -S` Q DROP) on the 19 gated ports: sw03/p4 +1, sw07/p4 +369.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S2→S1 | None | 300 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 2 | 2 | S2→S1 | 7 | 100 | 400.0 | 400.0 | 40.7 | 75000 | 75000 | 100.00% | 28.4 / 28.6 / 28.8 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 3 | 3 | S3→S1 | None | 500 | 800.0 | 800.0 | – | 0 | – | – | – | – | – | – | – | – |
| 4 | 4 | S1→S3 | None | 300 | 800.0 | 800.0 | – | 0 | – | – | – | – | – | – | – | – |
| 5 | 5 | S1→S3 | 6 | 100 | 800.0 | 800.0 | 22.8 | 37500 | 37500 | 100.00% | 10.4 / 10.7 / 10.9 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 6 | 6 | S2→S3 | 7 | 100 | 200.0 | 200.0 | 48.1 | 150000 | 150000 | 100.00% | 35.7 / 36.0 / 36.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 7 | 7 | S2→S3 | None | 200 | 800.0 | 800.0 | – | 0 | – | – | – | – | – | – | – | – |
| 8 | 8 | S1→S2 | None | 300 | 200.0 | 200.0 | – | 0 | – | – | – | – | – | – | – | – |
| 9 | 9 | S3→S1 | 6 | 100 | 400.0 | 400.0 | 22.8 | 74995 | 74995 | 100.00% | 5.1 / 5.4 / 5.9 | 0.1 | 0.2 | 0 | 0.00% | 0 |
| 10 | 10 | S1→S3 | 6 | 100 | 200.0 | 200.0 | 22.8 | 150000 | 150000 | 100.00% | 5.0 / 5.4 / 88.0 | 0.3 | 0.1 | 0 | 0.00% | 0 |
| 11 | 11 | S3→S2 | None | 300 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 12 | 12 | S2→S3 | 6 | 500 | 800.0 | 800.0 | 60.6 | 37500 | 37130 | 99.01% | 38.9 / 297.3 / 320743.7 | 8925.2 | 17.4 | 31 | 0.08% | 0 |
| 13 | 13 | S3→S1 | 7 | 200 | 800.0 | 800.0 | 28.6 | 37497 | 37497 | 100.00% | 9.3 / 9.7 / 10.2 | 0.1 | 0.1 | 0 | 0.00% | 0 |
| 14 | 14 | S2→S3 | None | 300 | 200.0 | 200.0 | – | 0 | – | – | – | – | – | – | – | – |
| 15 | 15 | S3→S1 | None | 300 | 200.0 | 200.0 | – | 0 | – | – | – | – | – | – | – | – |
| 16 | 16 | S1→S2 | None | 200 | 200.0 | 200.0 | – | 0 | – | – | – | – | – | – | – | – |
| 17 | 17 | S1→S3 | None | 300 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 18 | 18 | S3→S1 | 6 | 400 | 400.0 | 400.0 | 27.9 | 74993 | 74993 | 100.00% | 9.7 / 10.2 / 20.0 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 19 | 19 | S1→S3 | 7 | 300 | 400.0 | 400.0 | 26.0 | 75000 | 75000 | 100.00% | 13.6 / 13.9 / 14.1 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 20 | 20 | S1→S2 | 7 | 500 | 200.0 | 200.0 | 45.8 | 150000 | 150000 | 100.00% | 27.8 / 28.4 / 29.1 | 0.2 | 0.1 | 0 | 0.00% | 0 |
