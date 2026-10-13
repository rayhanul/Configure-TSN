# Traffic run: result-2026-10-12-dataset-testbed-8-ring-avgwin/smt-c9-on/8-fair-retimed-c9on, 2026-10-12 15:45

10 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **862498 / 862498 packets (100.00%)**
- Deadline misses: **4 (0.00% of received)**; flows with zero misses: 9 / 10

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 4 | 100.00% | 17.1 | 0.00% |
| S2 | 1 | 100.00% | 33.7 | 0.00% |
| S3 | 5 | 100.00% | 22.0 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7276524.181] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7359748.744] rms   23 max   60 freq  -6397 +/-  32 delay    23 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[1052005.261] rms    7 max   12 freq  +2325 +/-   9 delay    48 +/-   0`
- Connectivity: 10 / 10 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 0 |
| S2 | 0 | 0 | 0 |
| S3 | 0 | 0 | 2 |

Switch queue drops (`ethtool -S` Q DROP) on the 19 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 2 | S2→S1 | 7 | 100 | 400.0 | 400.0 | 40.7 | 75000 | 75000 | 100.00% | 28.4 / 28.6 / 28.8 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 2 | 5 | S1→S3 | 6 | 100 | 800.0 | 800.0 | 22.8 | 37500 | 37500 | 100.00% | 10.4 / 10.7 / 12.7 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 3 | 6 | S2→S3 | 7 | 100 | 200.0 | 200.0 | 48.1 | 150000 | 150000 | 100.00% | 35.7 / 36.0 / 36.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 4 | 9 | S3→S1 | 6 | 100 | 400.0 | 400.0 | 22.8 | 75000 | 75000 | 100.00% | 10.5 / 10.7 / 14.0 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 5 | 10 | S1→S3 | 6 | 100 | 200.0 | 200.0 | 22.8 | 150000 | 150000 | 100.00% | 10.4 / 10.7 / 212.0 | 1.1 | 0.0 | 4 | 0.00% | 0 |
| 6 | 12 | S2→S3 | 6 | 500 | 800.0 | 800.0 | 60.6 | 37500 | 37500 | 100.00% | 39.0 / 39.4 / 39.8 | 0.1 | 0.1 | 0 | 0.00% | 0 |
| 7 | 13 | S3→S1 | 7 | 200 | 800.0 | 800.0 | 28.6 | 37499 | 37499 | 100.00% | 9.3 / 9.7 / 10.1 | 0.1 | 0.1 | 0 | 0.00% | 0 |
| 8 | 18 | S3→S1 | 6 | 400 | 400.0 | 400.0 | 27.9 | 74999 | 74999 | 100.00% | 15.6 / 15.8 / 385.6 | 1.4 | 0.0 | 0 | 0.00% | 0 |
| 9 | 19 | S1→S3 | 7 | 300 | 400.0 | 400.0 | 26.0 | 75000 | 75000 | 100.00% | 13.6 / 13.9 / 14.1 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 10 | 20 | S1→S2 | 7 | 500 | 200.0 | 200.0 | 45.8 | 150000 | 150000 | 100.00% | 33.5 / 33.7 / 33.9 | 0.1 | 0.0 | 0 | 0.00% | 0 |
