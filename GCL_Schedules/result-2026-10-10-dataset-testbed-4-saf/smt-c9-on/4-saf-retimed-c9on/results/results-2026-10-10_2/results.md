# Traffic run: result-2026-10-10-dataset-testbed-4-saf/smt-c9-on/4-saf-retimed-c9on, 2026-10-10 17:48

11 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **1001880 / 1012480 packets (98.95%)**
- Deadline misses: **314 (0.03% of received)**; flows with zero misses: 0 / 11

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 1 | 99.01% | 287.4 | 0.11% |
| S2 | 4 | 98.95% | 91.4 | 0.03% |
| S3 | 6 | 98.95% | 103.3 | 0.03% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7192691.373] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7194311.990] rms    9 max   19 freq  -6187 +/-  12 delay    24 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[886569.019] rms   39 max   53 freq  +3164 +/-  54 delay    48 +/-   0`
- Connectivity: 11 / 11 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 0 |
| S2 | 0 | 0 | 0 |
| S3 | 0 | 0 | 20 |

Switch queue drops (`ethtool -S` Q DROP) on the 17 gated ports: sw05/p4 +3140, sw06/p4 +3940, sw07/p4 +3150, sw08/p4 +370.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S3→S2 | 7 | 300 | 400.0 | 400.0 | 46.2 | 74994 | 74224 | 98.97% | 33.8 / 165.9 / 320034.1 | 6443.8 | 8.6 | 39 | 0.05% | 0 |
| 2 | 3 | S2→S3 | 7 | 100 | 400.0 | 400.0 | 42.0 | 75000 | 74210 | 98.95% | 21.0 / 64.4 / 320821.3 | 3707.7 | 8.7 | 18 | 0.02% | 0 |
| 3 | 6 | S1→S3 | 6 | 300 | 800.0 | 800.0 | 67.0 | 37500 | 37102 | 98.94% | 54.6 / 72.3 / 321655.0 | 2358.3 | 17.4 | 6 | 0.02% | 0 |
| 4 | 8 | S2→S3 | 7 | 500 | 200.0 | 200.0 | 54.2 | 150000 | 148420 | 98.95% | 41.8 / 87.3 / 320842.1 | 3797.3 | 4.3 | 36 | 0.02% | 0 |
| 5 | 9 | S1→S3 | 7 | 400 | 800.0 | 800.0 | 74.0 | 37500 | 37130 | 99.01% | 61.7 / 323.9 / 321772.4 | 9018.5 | 17.3 | 44 | 0.12% | 0 |
| 6 | 10 | S3→S2 | 6 | 400 | 400.0 | 400.0 | 51.0 | 74996 | 74206 | 98.95% | 38.6 / 82.0 / 319998.2 | 3703.6 | 8.6 | 18 | 0.02% | 0 |
| 7 | 13 | S1→S2 | 6 | 400 | 200.0 | 200.0 | 43.3 | 150000 | 148413 | 98.94% | 30.9 / 61.2 / 320031.2 | 3097.4 | 4.3 | 17 | 0.01% | 0 |
| 8 | 14 | S3→S2 | 6 | 500 | 200.0 | 200.0 | 56.1 | 149990 | 148410 | 98.95% | 43.7 / 89.2 / 320044.0 | 3794.0 | 4.3 | 38 | 0.03% | 0 |
| 9 | 18 | S2→S1 | 6 | 300 | 800.0 | 800.0 | 39.4 | 37500 | 37130 | 99.01% | 27.1 / 287.4 / 320027.1 | 8975.7 | 17.3 | 39 | 0.11% | 0 |
| 10 | 19 | S2→S3 | 6 | 500 | 400.0 | 400.0 | 54.2 | 75000 | 74231 | 98.97% | 41.8 / 174.0 / 320818.3 | 6446.7 | 8.7 | 39 | 0.05% | 0 |
| 11 | 20 | S1→S3 | 6 | 100 | 200.0 | 200.0 | 54.8 | 150000 | 148404 | 98.94% | 42.5 / 55.8 / 322271.3 | 2042.4 | 4.3 | 20 | 0.01% | 0 |
