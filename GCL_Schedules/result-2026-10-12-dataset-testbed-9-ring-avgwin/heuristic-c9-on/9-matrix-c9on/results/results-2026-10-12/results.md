# Traffic run: result-2026-10-12-dataset-testbed-9-ring-avgwin/heuristic-c9-on/9-matrix-c9on, 2026-10-12 16:10

11 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **862472 / 862478 packets (100.00%)**
- Deadline misses: **0 (0.00% of received)**; flows with zero misses: 11 / 11

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 6 | 100.00% | 17.2 | 0.00% |
| S2 | 2 | 100.00% | 27.8 | 0.00% |
| S3 | 3 | 100.00% | 18.7 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7276524.181] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7361217.162] rms    9 max   12 freq  -6389 +/-  10 delay    26 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[1053474.932] rms   27 max   75 freq  +2118 +/-  36 delay    48 +/-   0`
- Connectivity: 11 / 11 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 2 | 0 |
| S2 | 0 | 6 | 11 |
| S3 | 0 | 0 | 11 |

Switch queue drops (`ethtool -S` Q DROP) on the 19 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S3→S1 | 6 | 200 | 800.0 | 800.0 | 24.7 | 37500 | 37500 | 100.00% | 12.4 / 12.6 / 12.7 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 2 | 4 | S3→S1 | 7 | 100 | 400.0 | 400.0 | 33.4 | 74999 | 74999 | 100.00% | 21.0 / 21.2 / 21.4 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 3 | 6 | S2→S3 | 6 | 100 | 200.0 | 200.0 | 40.7 | 149995 | 149993 | 100.00% | 17.4 / 19.4 / 23.8 | 2.3 | 2.7 | 0 | 0.00% | 0 |
| 4 | 7 | S2→S1 | 6 | 100 | 400.0 | 400.0 | 33.0 | 74998 | 74997 | 100.00% | 9.7 / 10.3 / 11.0 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 5 | 8 | S2→S3 | 6 | 400 | 800.0 | 800.0 | 51.0 | 37499 | 37498 | 100.00% | 35.6 / 36.0 / 36.6 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 6 | 9 | S3→S2 | 7 | 500 | 800.0 | 800.0 | 54.2 | 37500 | 37500 | 100.00% | 41.8 / 42.0 / 42.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 7 | 10 | S3→S1 | 6 | 400 | 200.0 | 200.0 | 27.9 | 149990 | 149990 | 100.00% | 9.7 / 10.2 / 11.2 | 0.2 | 0.1 | 0 | 0.00% | 0 |
| 8 | 12 | S1→S2 | 6 | 200 | 800.0 | 800.0 | 36.9 | 37500 | 37500 | 100.00% | 12.8 / 13.5 / 14.2 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 9 | 14 | S1→S3 | 6 | 400 | 200.0 | 200.0 | 27.9 | 150000 | 150000 | 100.00% | 12.6 / 13.7 / 27.5 | 1.2 | 1.5 | 0 | 0.00% | 0 |
| 10 | 16 | S2→S1 | 6 | 500 | 400.0 | 400.0 | 50.0 | 74998 | 74997 | 100.00% | 33.2 / 35.7 / 38.0 | 2.1 | 4.3 | 0 | 0.00% | 0 |
| 11 | 20 | S2→S1 | 6 | 200 | 800.0 | 800.0 | 36.9 | 37499 | 37498 | 100.00% | 18.5 / 19.1 / 19.7 | 0.2 | 0.2 | 0 | 0.00% | 0 |
