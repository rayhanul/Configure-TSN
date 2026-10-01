# Traffic run: heuristic-c9-off/1-matrix-c9off, 2026-10-01 16:13

10 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time, NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **1462427 / 1462494 packets (100.00%)**
- Deadline misses: **75003 (5.13% of received)**; flows with zero misses: 8 / 10

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 4 | 100.00% | 40.7 | 0.00% |
| S2 | 2 | 99.99% | 12.5 | 0.00% |
| S3 | 4 | 100.00% | 34.3 | 10.53% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[6405595.467] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[6411035.203] rms   12 max   26 freq  -6340 +/-  17 delay    18 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[103339.664] rms   24 max   67 freq  +2676 +/-  32 delay    48 +/-   0`
- Connectivity: 10 / 10 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 29 | 6 |
| S2 | 0 | 0 | 0 |
| S3 | 0 | 43 | 0 |

Switch queue drops (`ethtool -S` Q DROP) on the 27 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S3→S1 | 7 | 500 | 800.0 | 800.0 | 16.7 | 37500 | 37498 | 99.99% | 13.1 / 13.3 / 13.5 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 2 | 4 | S1→S3 | 6 | 300 | 100.0 | 100.0 | 11.7 | 299996 | 299975 | 99.99% | 8.1 / 16.1 / 204.8 | 13.1 | 15.2 | 3 | 0.00% | 0 |
| 3 | 5 | S2→S1 | 7 | 200 | 200.0 | 200.0 | 16.8 | 150000 | 150000 | 100.00% | 15.5 / 86.6 / 157.7 | 70.9 | 141.8 | 0 | 0.00% | 0 |
| 4 | 8 | S2→S3 | 6 | 100 | 800.0 | 800.0 | 12.8 | 37500 | 37500 | 100.00% | 17.7 / 18.6 / 19.3 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 5 | 10 | S1→S3 | 7 | 100 | 400.0 | 400.0 | 7.5 | 74998 | 74991 | 99.99% | 67.0 / 67.2 / 67.5 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 6 | 12 | S2→S1 | 6 | 100 | 400.0 | 400.0 | 13.3 | 75000 | 75000 | 100.00% | 14.3 / 52.1 / 89.5 | 37.2 | 74.4 | 0 | 0.00% | 0 |
| 7 | 15 | S2→S3 | 6 | 400 | 100.0 | 100.0 | 24.8 | 300000 | 300000 | 100.00% | 19.1 / 46.2 / 116.1 | 40.1 | 52.8 | 75000 | 25.00% | 0 |
| 8 | 16 | S3→S2 | 6 | 200 | 800.0 | 800.0 | 16.8 | 37500 | 37498 | 99.99% | 12.8 / 13.5 / 15.8 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 9 | 18 | S3→S2 | 6 | 100 | 200.0 | 200.0 | 12.8 | 150000 | 149988 | 99.99% | 9.7 / 12.3 / 21.7 | 3.4 | 4.0 | 0 | 0.00% | 0 |
| 10 | 20 | S3→S1 | 6 | 200 | 100.0 | 100.0 | 9.3 | 300000 | 299977 | 99.99% | 6.6 / 18.3 / 97.5 | 29.9 | 22.7 | 0 | 0.00% | 0 |
