# Traffic run: result-2026-10-10-dataset-testbed-5-avgwin/heuristic-c9-off/5-matrix-c9off, 2026-10-11 00:02

10 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **824985 / 824985 packets (100.00%)**
- Deadline misses: **0 (0.00% of received)**; flows with zero misses: 10 / 10

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 1 | 100.00% | 34.0 | 0.00% |
| S2 | 6 | 100.00% | 60.7 | 0.00% |
| S3 | 3 | 100.00% | 48.0 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7192691.373] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7216789.553] rms   34 max   62 freq  -6208 +/-  47 delay    25 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[909046.707] rms   32 max   46 freq  +3038 +/-  43 delay    48 +/-   0`
- Connectivity: 10 / 10 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 0 |
| S2 | 0 | 0 | 0 |
| S3 | 0 | 0 | 15 |

Switch queue drops (`ethtool -S` Q DROP) on the 17 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 2 | S2→S3 | 6 | 300 | 200.0 | 200.0 | 95.8 | 150000 | 150000 | 100.00% | 19.7 / 20.7 / 22.0 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 2 | 3 | S1→S2 | 6 | 100 | 800.0 | 800.0 | 84.2 | 37500 | 37500 | 100.00% | 46.7 / 49.8 / 50.1 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 3 | 5 | S2→S3 | 7 | 100 | 800.0 | 800.0 | 95.8 | 37500 | 37500 | 100.00% | 83.4 / 83.6 / 83.8 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 4 | 9 | S2→S1 | 7 | 500 | 400.0 | 400.0 | 79.1 | 75000 | 75000 | 100.00% | 33.4 / 34.0 / 34.7 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 5 | 10 | S1→S2 | 7 | 500 | 200.0 | 200.0 | 79.1 | 150000 | 150000 | 100.00% | 66.7 / 67.0 / 67.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 6 | 12 | S3→S2 | 7 | 500 | 200.0 | 200.0 | 95.8 | 149992 | 149992 | 100.00% | 58.4 / 58.6 / 58.9 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 7 | 13 | S1→S3 | 6 | 400 | 800.0 | 800.0 | 145.7 | 37500 | 37500 | 100.00% | 121.3 / 121.7 / 122.5 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 8 | 16 | S3→S2 | 7 | 200 | 800.0 | 800.0 | 97.0 | 37498 | 37498 | 100.00% | 33.9 / 37.8 / 38.1 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 9 | 17 | S1→S2 | 6 | 400 | 400.0 | 400.0 | 83.6 | 75000 | 75000 | 100.00% | 71.2 / 71.4 / 71.7 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 10 | 19 | S3→S2 | 7 | 500 | 400.0 | 400.0 | 96.4 | 74995 | 74995 | 100.00% | 58.4 / 58.6 / 58.9 | 0.1 | 0.0 | 0 | 0.00% | 0 |
