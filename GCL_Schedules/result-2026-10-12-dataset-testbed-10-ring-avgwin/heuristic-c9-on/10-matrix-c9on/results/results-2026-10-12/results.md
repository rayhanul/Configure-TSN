# Traffic run: result-2026-10-12-dataset-testbed-10-ring-avgwin/heuristic-c9-on/10-matrix-c9on, 2026-10-12 16:31

11 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **1011704 / 1012449 packets (99.93%)**
- Deadline misses: **63 (0.01% of received)**; flows with zero misses: 8 / 11

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 4 | 99.83% | 56.7 | 0.01% |
| S2 | 3 | 99.89% | 62.9 | 0.01% |
| S3 | 4 | 100.00% | 22.9 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7276524.181] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7362506.528] rms   34 max   67 freq  -6365 +/-  41 delay    25 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[1054764.422] rms    7 max   13 freq  +2240 +/-   5 delay    50 +/-   0`
- Connectivity: 11 / 11 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 2 | 30 |
| S2 | 0 | 0 | 3 |
| S3 | 0 | 5 | 18 |

Switch queue drops (`ethtool -S` Q DROP) on the 19 gated ports: sw02/p4 +370, sw08/p4 +370.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S3→S1 | 6 | 400 | 400.0 | 400.0 | 27.9 | 74996 | 74994 | 100.00% | 9.7 / 10.2 / 36.1 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 2 | 3 | S1→S3 | 6 | 400 | 200.0 | 200.0 | 27.9 | 149992 | 149992 | 100.00% | 12.6 / 13.0 / 200.6 | 0.5 | 0.1 | 1 | 0.00% | 0 |
| 3 | 5 | S3→S1 | 7 | 400 | 800.0 | 800.0 | 31.1 | 37499 | 37499 | 100.00% | 18.8 / 19.0 / 19.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 4 | 7 | S2→S3 | 7 | 200 | 200.0 | 200.0 | 43.0 | 149999 | 149999 | 100.00% | 30.6 / 30.9 / 31.1 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 5 | 9 | S3→S2 | 7 | 400 | 200.0 | 200.0 | 51.0 | 149991 | 149989 | 100.00% | 38.6 / 38.8 / 39.0 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 6 | 10 | S2→S1 | 6 | 400 | 800.0 | 800.0 | 43.3 | 37499 | 37129 | 99.01% | 27.8 / 286.3 / 320777.1 | 8927.4 | 17.4 | 31 | 0.08% | 0 |
| 7 | 11 | S2→S3 | 7 | 200 | 400.0 | 400.0 | 43.0 | 74999 | 74999 | 100.00% | 30.6 / 30.9 / 31.1 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 8 | 12 | S1→S2 | 7 | 500 | 200.0 | 200.0 | 45.8 | 149985 | 149985 | 100.00% | 27.9 / 31.0 / 31.4 | 0.3 | 0.1 | 0 | 0.00% | 0 |
| 9 | 15 | S3→S1 | 6 | 300 | 400.0 | 400.0 | 26.0 | 74996 | 74995 | 100.00% | 8.1 / 8.6 / 27.5 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 10 | 17 | S1→S2 | 6 | 400 | 800.0 | 800.0 | 43.3 | 37498 | 37128 | 99.01% | 30.9 / 289.0 / 320739.9 | 8922.3 | 17.3 | 31 | 0.08% | 0 |
| 11 | 18 | S1→S3 | 6 | 200 | 400.0 | 400.0 | 30.8 | 74995 | 74995 | 100.00% | 18.5 / 18.7 / 22.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
