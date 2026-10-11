# Traffic run: result-2026-10-09-dataset-testbed-4-avgwin/rl-c9-off/4-matrix-c9off, 2026-10-10 16:36

20 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **1003390 / 1012500 packets (99.10%)**
- Deadline misses: **160 (0.02% of received)**; flows with zero misses: 3 / 20

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 1 | 99.01% | 299.6 | 0.08% |
| S2 | 4 | 99.29% | 75.5 | 0.01% |
| S3 | 6 | 98.94% | 139.8 | 0.02% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7173666.135] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7189972.597] rms   12 max   19 freq  -6204 +/-  15 delay    22 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[882230.509] rms   34 max   47 freq  +3105 +/-  47 delay    50 +/-   0`
- Connectivity: 11 / 11 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 0 |
| S2 | 0 | 0 | 0 |
| S3 | 0 | 26 | 0 |

Switch queue drops (`ethtool -S` Q DROP) on the 17 gated ports: sw05/p4 +1573, sw06/p4 +3979, sw07/p4 +3162, sw08/p4 +370.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S3→S2 | 7 | 300 | 400.0 | 400.0 | 95.8 | 75000 | 74994 | 99.99% | 32.8 / 83.1 / 83.8 | 5.2 | 0.0 | 0 | 0.00% | 0 |
| 2 | 2 | S1→S2 | None | 300 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 3 | 3 | S2→S3 | 7 | 100 | 400.0 | 400.0 | 95.8 | 75000 | 74213 | 98.95% | 83.4 / 152.2 / 320883.5 | 4672.6 | 8.7 | 18 | 0.02% | 0 |
| 4 | 4 | S3→S2 | None | 400 | 800.0 | 800.0 | – | 0 | – | – | – | – | – | – | – | – |
| 5 | 5 | S3→S1 | None | 200 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 6 | 6 | S1→S3 | 6 | 300 | 800.0 | 800.0 | 145.7 | 37500 | 37098 | 98.93% | 133.3 / 133.5 / 438.7 | 1.6 | 0.0 | 0 | 0.00% | 0 |
| 7 | 7 | S1→S3 | None | 100 | 800.0 | 800.0 | – | 0 | – | – | – | – | – | – | – | – |
| 8 | 8 | S2→S3 | 6 | 500 | 200.0 | 200.0 | 95.8 | 150000 | 148426 | 98.95% | 83.4 / 150.1 / 320883.5 | 4598.4 | 4.3 | 36 | 0.02% | 0 |
| 9 | 9 | S1→S3 | 6 | 400 | 800.0 | 800.0 | 145.7 | 37500 | 37102 | 98.94% | 110.9 / 137.1 / 321712.6 | 2884.7 | 17.4 | 4 | 0.01% | 0 |
| 10 | 10 | S3→S2 | 7 | 400 | 400.0 | 400.0 | 95.8 | 75000 | 74993 | 99.99% | 58.5 / 83.4 / 83.8 | 2.6 | 0.0 | 0 | 0.00% | 0 |
| 11 | 11 | S2→S1 | None | 200 | 800.0 | 800.0 | – | 0 | – | – | – | – | – | – | – | – |
| 12 | 12 | S2→S3 | None | 100 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 13 | 13 | S1→S2 | 6 | 400 | 200.0 | 200.0 | 79.1 | 150000 | 148409 | 98.94% | 19.0 / 48.0 / 320804.9 | 2991.7 | 4.8 | 13 | 0.01% | 0 |
| 14 | 14 | S3→S2 | 6 | 500 | 200.0 | 200.0 | 95.8 | 150000 | 148414 | 98.94% | 28.0 / 95.1 / 320811.5 | 4594.6 | 4.5 | 32 | 0.02% | 0 |
| 15 | 15 | S3→S2 | None | 300 | 200.0 | 200.0 | – | 0 | – | – | – | – | – | – | – | – |
| 16 | 16 | S1→S2 | None | 100 | 200.0 | 200.0 | – | 0 | – | – | – | – | – | – | – | – |
| 17 | 17 | S2→S1 | None | 400 | 200.0 | 200.0 | – | 0 | – | – | – | – | – | – | – | – |
| 18 | 18 | S2→S1 | 6 | 300 | 800.0 | 800.0 | 79.1 | 37500 | 37130 | 99.01% | 41.2 / 299.6 / 320737.5 | 8921.3 | 17.4 | 31 | 0.08% | 0 |
| 19 | 19 | S2→S3 | 7 | 500 | 400.0 | 400.0 | 95.8 | 75000 | 74213 | 98.95% | 83.4 / 148.0 / 320859.5 | 4526.2 | 8.7 | 18 | 0.02% | 0 |
| 20 | 20 | S1→S3 | 6 | 100 | 200.0 | 200.0 | 145.7 | 150000 | 148398 | 98.93% | 95.9 / 121.3 / 321565.9 | 1441.9 | 41.8 | 8 | 0.01% | 0 |
