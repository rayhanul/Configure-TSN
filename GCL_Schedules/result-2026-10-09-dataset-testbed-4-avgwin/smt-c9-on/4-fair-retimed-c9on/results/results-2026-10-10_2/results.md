# Traffic run: result-2026-10-09-dataset-testbed-4-avgwin/smt-c9-on/4-fair-retimed-c9on, 2026-10-10 11:21

11 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **1012473 / 1012500 packets (100.00%)**
- Deadline misses: **26764 (2.64% of received)**; flows with zero misses: 9 / 11

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 1 | 100.00% | 17.1 | 0.00% |
| S2 | 4 | 99.99% | 24.7 | 0.00% |
| S3 | 6 | 100.00% | 86.6 | 5.10% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7160963.398] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7171088.069] rms   27 max   70 freq  -6188 +/-  35 delay    20 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[863345.349] rms   28 max   72 freq  +2949 +/-  38 delay    49 +/-   0`
- Connectivity: 11 / 11 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 0 |
| S2 | 0 | 0 | 0 |
| S3 | 0 | 27 | 0 |

Switch queue drops (`ethtool -S` Q DROP) on the 17 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S3→S2 | 6 | 300 | 400.0 | 400.0 | 33.4 | 75000 | 74993 | 99.99% | 21.0 / 21.2 / 46.3 | 0.1 | 0.1 | 0 | 0.00% | 0 |
| 2 | 3 | S2→S3 | 7 | 100 | 400.0 | 400.0 | 33.4 | 75000 | 75000 | 100.00% | 21.4 / 25.4 / 27.0 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 3 | 6 | S1→S3 | 7 | 300 | 800.0 | 800.0 | 46.8 | 37500 | 37500 | 100.00% | 34.5 / 34.7 / 35.1 | 0.1 | 0.1 | 0 | 0.00% | 0 |
| 4 | 8 | S2→S3 | 7 | 500 | 200.0 | 200.0 | 33.4 | 150000 | 150000 | 100.00% | 28.0 / 52.6 / 60.5 | 6.4 | 12.8 | 0 | 0.00% | 0 |
| 5 | 9 | S1→S3 | 6 | 400 | 800.0 | 800.0 | 45.8 | 37500 | 37500 | 100.00% | 397.1 / 397.9 / 1198.2 | 16.0 | 0.5 | 15 | 0.04% | 0 |
| 6 | 10 | S3→S2 | 6 | 400 | 400.0 | 400.0 | 33.4 | 75000 | 74992 | 99.99% | 23.8 / 24.7 / 26.3 | 0.3 | 0.3 | 0 | 0.00% | 0 |
| 7 | 13 | S1→S2 | 7 | 400 | 200.0 | 200.0 | 29.2 | 150000 | 150000 | 100.00% | 19.0 / 19.8 / 20.7 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 8 | 14 | S3→S2 | 7 | 500 | 200.0 | 200.0 | 42.0 | 150000 | 149988 | 99.99% | 31.0 / 31.3 / 31.7 | 0.1 | 0.1 | 0 | 0.00% | 0 |
| 9 | 18 | S2→S1 | 7 | 300 | 800.0 | 800.0 | 29.2 | 37500 | 37500 | 100.00% | 16.9 / 17.1 / 17.4 | 0.1 | 0.1 | 0 | 0.00% | 0 |
| 10 | 19 | S2→S3 | 6 | 500 | 400.0 | 400.0 | 34.0 | 75000 | 75000 | 100.00% | 28.0 / 186.8 / 423.3 | 175.4 | 264.8 | 26749 | 35.67% | 0 |
| 11 | 20 | S1→S3 | 7 | 100 | 200.0 | 200.0 | 46.2 | 150000 | 150000 | 100.00% | 33.8 / 36.1 / 39.7 | 2.1 | 4.2 | 0 | 0.00% | 0 |
