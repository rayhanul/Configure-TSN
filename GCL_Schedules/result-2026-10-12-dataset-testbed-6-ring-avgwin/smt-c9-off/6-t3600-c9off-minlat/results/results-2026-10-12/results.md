# Traffic run: result-2026-10-12-dataset-testbed-6-ring-avgwin/smt-c9-off/6-t3600-c9off-minlat, 2026-10-12 13:14

20 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **1012447 / 1012447 packets (100.00%)**
- Deadline misses: **5 (0.00% of received)**; flows with zero misses: 9 / 20

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 7 | 100.00% | 44.9 | 0.00% |
| S2 | 2 | 100.00% | 75.6 | 0.00% |
| S3 | 1 | 100.00% | 34.1 | 0.01% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7276524.181] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7350704.675] rms   29 max   77 freq  -6362 +/-  38 delay    24 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[1042962.069] rms    9 max   17 freq  +3086 +/-  12 delay    47 +/-   0`
- Connectivity: 10 / 10 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 21 |
| S2 | 0 | 0 | 0 |
| S3 | 0 | 0 | 32 |

Switch queue drops (`ethtool -S` Q DROP) on the 19 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S3→S1 | 6 | 500 | 200.0 | 200.0 | 45.8 | 149991 | 149991 | 100.00% | 33.8 / 33.9 / 34.1 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 2 | 2 | S2→S1 | 7 | 400 | 200.0 | 200.0 | 79.1 | 150000 | 150000 | 100.00% | 67.0 / 67.2 / 67.4 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 3 | 3 | S3→S2 | None | 100 | 200.0 | 200.0 | – | 0 | – | – | – | – | – | – | – | – |
| 4 | 4 | S1→S3 | 6 | 300 | 800.0 | 800.0 | 45.8 | 37495 | 37495 | 100.00% | 33.8 / 34.1 / 834.1 | 9.2 | 0.2 | 5 | 0.01% | 0 |
| 5 | 5 | S2→S1 | None | 200 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 6 | 6 | S2→S1 | 6 | 100 | 400.0 | 400.0 | 83.6 | 75000 | 75000 | 100.00% | 71.5 / 71.7 / 71.9 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 7 | 7 | S2→S1 | 6 | 300 | 800.0 | 800.0 | 84.2 | 37500 | 37500 | 100.00% | 54.2 / 54.7 / 72.3 | 1.3 | 0.3 | 0 | 0.00% | 0 |
| 8 | 8 | S2→S3 | None | 100 | 800.0 | 800.0 | – | 0 | – | – | – | – | – | – | – | – |
| 9 | 9 | S3→S2 | 6 | 500 | 200.0 | 200.0 | 95.8 | 149991 | 149991 | 100.00% | 83.7 / 83.9 / 84.1 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 10 | 10 | S1→S3 | None | 100 | 800.0 | 800.0 | – | 0 | – | – | – | – | – | – | – | – |
| 11 | 11 | S3→S2 | None | 500 | 800.0 | 800.0 | – | 0 | – | – | – | – | – | – | – | – |
| 12 | 12 | S2→S1 | 6 | 100 | 800.0 | 800.0 | 79.1 | 37500 | 37500 | 100.00% | 52.6 / 53.0 / 53.5 | 0.1 | 0.1 | 0 | 0.00% | 0 |
| 13 | 13 | S1→S2 | None | 300 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 14 | 14 | S1→S2 | 7 | 100 | 200.0 | 200.0 | 79.1 | 149984 | 149984 | 100.00% | 67.0 / 67.2 / 67.5 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 15 | 15 | S2→S3 | None | 400 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 16 | 16 | S3→S2 | None | 200 | 200.0 | 200.0 | – | 0 | – | – | – | – | – | – | – | – |
| 17 | 17 | S2→S3 | None | 200 | 800.0 | 800.0 | – | 0 | – | – | – | – | – | – | – | – |
| 18 | 18 | S3→S2 | None | 100 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 19 | 19 | S3→S1 | 7 | 500 | 400.0 | 400.0 | 46.5 | 74995 | 74995 | 100.00% | 34.4 / 34.6 / 34.8 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 20 | 20 | S3→S1 | 7 | 200 | 200.0 | 200.0 | 45.8 | 149991 | 149991 | 100.00% | 20.5 / 20.8 / 25.3 | 0.2 | 0.1 | 0 | 0.00% | 0 |
