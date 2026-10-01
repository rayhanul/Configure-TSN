# Traffic run: heuristic-c9-off/1-matrix-c9off, 2026-10-01 16:04

10 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time, NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **411707 / 1462492 packets (28.15%)**
- Deadline misses: **31 (0.01% of received)**; flows with zero misses: 5 / 10

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 4 | 42.71% | 118.4 | 0.01% |
| S2 | 2 | 0.00% | 0.0 | 0.00% |
| S3 | 4 | 26.31% | 102.5 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[6405595.467] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[6410455.579] rms   26 max   51 freq  -6362 +/-  33 delay    19 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s
- Connectivity: 8 / 10 sender routes answered ping (failed: 8, 15)

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 24 | 0 |
| S2 | 0 | 0 | 0 |
| S3 | 0 | 4 | 8 |

Switch queue drops (`ethtool -S` Q DROP) on the 27 gated ports: sw01/p3 +8, sw02/p3 +3169, sw08/p4 +771.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S3→S1 | 7 | 500 | 800.0 | 800.0 | 16.7 | 149998 | 0 | 0.00% | – | – | – | – | – | – |
| 2 | 4 | S1→S3 | 6 | 300 | 100.0 | 100.0 | 11.7 | 300000 | 37492 | 12.50% | 269.8 / 273.3 / 273.8 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 3 | 5 | S2→S1 | 7 | 200 | 200.0 | 200.0 | 16.8 | 150000 | 150000 | 100.00% | 14.8 / 86.5 / 157.7 | 70.8 | 141.7 | 0 | 0.00% | 0 |
| 4 | 8 | S2→S3 | 6 | 100 | 800.0 | 800.0 | 12.8 | 37500 | 37500 | 100.00% | 62.5 / 63.2 / 64.1 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 5 | 10 | S1→S3 | 7 | 100 | 400.0 | 400.0 | 7.5 | 75000 | 37487 | 49.98% | 48.9 / 49.1 / 49.4 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 6 | 12 | S2→S1 | 6 | 100 | 400.0 | 400.0 | 13.3 | 75000 | 74229 | 98.97% | 12.9 / 182.7 / 320796.6 | 6432.9 | 84.8 | 31 | 0.04% | 0 |
| 7 | 15 | S2→S3 | 6 | 400 | 100.0 | 100.0 | 24.8 | 300000 | 74999 | 25.00% | 62.6 / 63.4 / 64.5 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 8 | 16 | S3→S2 | 6 | 200 | 800.0 | 800.0 | 16.8 | 149998 | 0 | 0.00% | – | – | – | – | – | – |
| 9 | 18 | S3→S2 | 6 | 100 | 200.0 | 200.0 | 12.8 | 74999 | 0 | 0.00% | – | – | – | – | – | – |
| 10 | 20 | S3→S1 | 6 | 200 | 100.0 | 100.0 | 9.3 | 149997 | 0 | 0.00% | – | – | – | – | – | – |
