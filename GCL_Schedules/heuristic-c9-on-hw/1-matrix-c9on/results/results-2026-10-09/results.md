# Traffic run: heuristic-c9-on-hw/1-matrix-c9on, 2026-10-09 12:59

10 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **937459 / 937500 packets (100.00%)**
- Deadline misses: **37498 (4.00% of received)**; flows with zero misses: 9 / 10

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 4 | 99.99% | 43.1 | 8.33% |
| S2 | 2 | 100.00% | 23.5 | 0.00% |
| S3 | 4 | 100.00% | 136.4 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7048158.236] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7090558.459] rms   12 max   14 freq  -6383 +/-  16 delay    18 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[782816.613] rms    9 max   16 freq  +2841 +/-  13 delay    44 +/-   0`

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 0 |
| S2 | 0 | 3 | 0 |
| S3 | 0 | 44 | 0 |

Switch queue drops (`ethtool -S` Q DROP) on the 27 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S3→S1 | 6 | 500 | 200.0 | 200.0 | 12.5 | 150000 | 149990 | 99.99% | 11.8 / 100.2 / 200.6 | 74.0 | 142.2 | 37498 | 25.00% | 0 |
| 2 | 4 | S1→S3 | 7 | 300 | 800.0 | 800.0 | 10.9 | 37500 | 37500 | 100.00% | 289.5 / 289.7 / 289.9 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 3 | 5 | S2→S1 | 6 | 200 | 400.0 | 400.0 | 19.2 | 75000 | 75000 | 100.00% | 13.8 / 23.8 / 24.0 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 4 | 8 | S2→S3 | 6 | 100 | 800.0 | 800.0 | 19.2 | 37500 | 37499 | 100.00% | 16.8 / 17.1 / 17.3 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 5 | 9 | S3→S2 | 7 | 500 | 200.0 | 200.0 | 20.8 | 150000 | 149989 | 99.99% | 22.5 / 23.1 / 62.2 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 6 | 14 | S1→S2 | 6 | 100 | 200.0 | 200.0 | 19.2 | 150000 | 150000 | 100.00% | 9.6 / 23.9 / 131.5 | 36.5 | 27.2 | 0 | 0.00% | 0 |
| 7 | 15 | S2→S3 | 7 | 400 | 400.0 | 400.0 | 20.2 | 75000 | 74999 | 100.00% | 19.0 / 180.8 / 342.1 | 161.0 | 322.0 | 0 | 0.00% | 0 |
| 8 | 17 | S2→S3 | 6 | 200 | 800.0 | 800.0 | 19.2 | 37500 | 37499 | 100.00% | 12.8 / 13.5 / 14.2 | 0.2 | 0.1 | 0 | 0.00% | 0 |
| 9 | 19 | S3→S1 | 6 | 500 | 400.0 | 400.0 | 12.5 | 75000 | 74994 | 99.99% | 12.0 / 14.7 / 382.0 | 1.3 | 0.1 | 0 | 0.00% | 0 |
| 10 | 20 | S3→S1 | 7 | 200 | 200.0 | 200.0 | 12.2 | 150000 | 149989 | 99.99% | 9.8 / 10.0 / 43.4 | 0.1 | 0.0 | 0 | 0.00% | 0 |
