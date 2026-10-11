# Traffic run: result-2026-10-10-dataset-testbed-5-avgwin/heuristic-c9-on/5-matrix-c9on, 2026-10-11 00:09

10 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **824981 / 824981 packets (100.00%)**
- Deadline misses: **0 (0.00% of received)**; flows with zero misses: 10 / 10

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 1 | 100.00% | 33.9 | 0.00% |
| S2 | 6 | 100.00% | 31.3 | 0.00% |
| S3 | 3 | 100.00% | 35.3 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7192691.373] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7217184.890] rms   20 max   47 freq  -6226 +/-  28 delay    23 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[909442.802] rms   49 max  107 freq  +3006 +/-  65 delay    49 +/-   0`
- Connectivity: 10 / 10 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 2 | 0 |
| S2 | 0 | 0 | 1 |
| S3 | 0 | 0 | 18 |

Switch queue drops (`ethtool -S` Q DROP) on the 17 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 2 | S2→S3 | 7 | 300 | 200.0 | 200.0 | 46.2 | 149999 | 149999 | 100.00% | 34.1 / 34.3 / 34.5 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 2 | 3 | S1→S2 | 7 | 100 | 800.0 | 800.0 | 56.7 | 37500 | 37500 | 100.00% | 9.8 / 10.4 / 11.1 | 0.2 | 0.1 | 0 | 0.00% | 0 |
| 3 | 5 | S2→S3 | 7 | 100 | 800.0 | 800.0 | 38.2 | 37500 | 37500 | 100.00% | 12.1 / 12.8 / 13.6 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 4 | 9 | S2→S1 | 6 | 500 | 400.0 | 400.0 | 45.8 | 75000 | 75000 | 100.00% | 33.7 / 33.9 / 34.1 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 5 | 10 | S1→S2 | 6 | 500 | 200.0 | 200.0 | 45.8 | 150000 | 150000 | 100.00% | 33.7 / 33.9 / 40.7 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 6 | 12 | S3→S2 | 6 | 500 | 200.0 | 200.0 | 54.2 | 149990 | 149990 | 100.00% | 28.0 / 29.4 / 32.4 | 1.2 | 1.5 | 0 | 0.00% | 0 |
| 7 | 13 | S1→S3 | 7 | 400 | 800.0 | 800.0 | 74.0 | 37500 | 37500 | 100.00% | 61.9 / 62.1 / 62.3 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 8 | 16 | S3→S2 | 6 | 200 | 800.0 | 800.0 | 43.9 | 37497 | 37497 | 100.00% | 23.2 / 23.4 / 23.6 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 9 | 17 | S1→S2 | 7 | 400 | 400.0 | 400.0 | 43.3 | 75000 | 75000 | 100.00% | 31.2 / 31.4 / 31.6 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 10 | 19 | S3→S2 | 6 | 500 | 400.0 | 400.0 | 56.1 | 74995 | 74995 | 100.00% | 44.0 / 44.2 / 44.4 | 0.1 | 0.0 | 0 | 0.00% | 0 |
