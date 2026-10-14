# Traffic run: rerun-dataset-11-tree-quiet60/smt-c9-on/11-fair-retimed-c9on, 2026-10-13 14:48

10 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **937448 / 937448 packets (100.00%)**
- Deadline misses: **5 (0.00% of received)**; flows with zero misses: 9 / 10

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 3 | 100.00% | 33.5 | 0.00% |
| S2 | 6 | 100.00% | 39.6 | 0.00% |
| S3 | 1 | 100.00% | 42.0 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7276524.181] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7442724.518] rms   26 max   64 freq  -6292 +/-  35 delay    24 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[1134982.171] rms   25 max   52 freq  +2769 +/-  34 delay    48 +/-   0`
- Connectivity: 10 / 10 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 23 |
| S2 | 0 | 0 | 0 |
| S3 | 0 | 0 | 29 |

Switch queue drops (`ethtool -S` Q DROP) on the 17 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S1→S2 | 7 | 500 | 200.0 | 200.0 | 45.8 | 149988 | 149988 | 100.00% | 33.5 / 33.7 / 33.9 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 2 | 2 | S3→S2 | 7 | 400 | 200.0 | 200.0 | 58.6 | 149989 | 149989 | 100.00% | 46.3 / 46.5 / 46.7 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 3 | 3 | S1→S2 | 6 | 500 | 400.0 | 400.0 | 46.5 | 74992 | 74992 | 100.00% | 34.1 / 34.3 / 60.1 | 0.3 | 0.0 | 0 | 0.00% | 0 |
| 4 | 5 | S2→S1 | 6 | 200 | 200.0 | 200.0 | 36.9 | 150000 | 150000 | 100.00% | 24.6 / 24.7 / 24.9 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 5 | 7 | S2→S1 | 6 | 300 | 800.0 | 800.0 | 39.4 | 37500 | 37500 | 100.00% | 27.1 / 27.3 / 27.5 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 6 | 8 | S3→S2 | 7 | 500 | 200.0 | 200.0 | 59.3 | 149989 | 149989 | 100.00% | 46.9 / 47.1 / 47.3 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 7 | 9 | S3→S2 | 6 | 100 | 800.0 | 800.0 | 38.2 | 37497 | 37497 | 100.00% | 25.8 / 26.0 / 26.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 8 | 10 | S3→S1 | 7 | 300 | 400.0 | 400.0 | 66.3 | 74996 | 74996 | 100.00% | 54.0 / 54.2 / 54.3 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 9 | 18 | S2→S3 | 7 | 500 | 800.0 | 800.0 | 54.2 | 37500 | 37500 | 100.00% | 41.8 / 42.0 / 42.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 10 | 20 | S1→S2 | 6 | 500 | 400.0 | 400.0 | 47.1 | 74997 | 74997 | 100.00% | 34.8 / 35.0 / 409.5 | 3.1 | 0.1 | 5 | 0.01% | 0 |
