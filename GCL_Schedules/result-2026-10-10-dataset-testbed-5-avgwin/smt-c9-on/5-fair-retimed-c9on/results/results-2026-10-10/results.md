# Traffic run: result-2026-10-10-dataset-testbed-5-avgwin/smt-c9-on/5-fair-retimed-c9on, 2026-10-10 23:56

10 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **824979 / 824984 packets (100.00%)**
- Deadline misses: **15 (0.00% of received)**; flows with zero misses: 8 / 10

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 1 | 100.00% | 33.9 | 0.00% |
| S2 | 6 | 100.00% | 38.0 | 0.00% |
| S3 | 3 | 100.00% | 37.6 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7192691.373] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7216398.539] rms    7 max   19 freq  -6211 +/-   9 delay    25 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[908655.834] rms   37 max   66 freq  +3107 +/-  49 delay    47 +/-   0`
- Connectivity: 10 / 10 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 0 |
| S2 | 0 | 0 | 0 |
| S3 | 0 | 5 | 16 |

Switch queue drops (`ethtool -S` Q DROP) on the 17 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 2 | S2→S3 | 7 | 300 | 200.0 | 200.0 | 46.2 | 150000 | 150000 | 100.00% | 34.1 / 34.3 / 34.5 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 2 | 3 | S1→S2 | 7 | 100 | 800.0 | 800.0 | 56.7 | 37500 | 37500 | 100.00% | 44.5 / 44.8 / 45.1 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 3 | 5 | S2→S3 | 7 | 100 | 800.0 | 800.0 | 38.2 | 37500 | 37500 | 100.00% | 26.1 / 26.3 / 26.5 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 4 | 9 | S2→S1 | 6 | 500 | 400.0 | 400.0 | 45.8 | 75000 | 75000 | 100.00% | 33.7 / 33.9 / 34.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 5 | 10 | S1→S2 | 6 | 500 | 200.0 | 200.0 | 45.8 | 150000 | 150000 | 100.00% | 33.7 / 33.9 / 234.2 | 1.9 | 0.0 | 14 | 0.01% | 0 |
| 6 | 12 | S3→S2 | 6 | 500 | 200.0 | 200.0 | 54.2 | 149992 | 149990 | 100.00% | 42.0 / 42.2 / 242.2 | 0.5 | 0.0 | 1 | 0.00% | 0 |
| 7 | 13 | S1→S3 | 7 | 400 | 800.0 | 800.0 | 74.0 | 37500 | 37500 | 100.00% | 61.9 / 62.1 / 62.3 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 8 | 16 | S3→S2 | 6 | 200 | 800.0 | 800.0 | 43.9 | 37497 | 37496 | 100.00% | 31.7 / 32.0 / 32.3 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 9 | 17 | S1→S2 | 7 | 400 | 400.0 | 400.0 | 43.3 | 75000 | 75000 | 100.00% | 31.1 / 31.4 / 31.6 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 10 | 19 | S3→S2 | 6 | 500 | 400.0 | 400.0 | 56.1 | 74995 | 74993 | 100.00% | 43.9 / 44.2 / 44.4 | 0.1 | 0.0 | 0 | 0.00% | 0 |
