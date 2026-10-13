# Traffic run: result-2026-10-12-dataset-testbed-9-ring-avgwin/smt-c9-off/9-t3600-c9off-minlat, 2026-10-12 16:04

20 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **862427 / 862439 packets (100.00%)**
- Deadline misses: **6 (0.00% of received)**; flows with zero misses: 10 / 20

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 6 | 100.00% | 46.0 | 0.00% |
| S2 | 2 | 100.00% | 75.3 | 0.00% |
| S3 | 3 | 100.00% | 61.4 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7276524.181] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7360852.182] rms   22 max   55 freq  -6401 +/-  31 delay    23 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[1053109.322] rms    9 max   17 freq  +2151 +/-  13 delay    49 +/-   0`
- Connectivity: 11 / 11 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 13 |
| S2 | 0 | 0 | 0 |
| S3 | 0 | 12 | 48 |

Switch queue drops (`ethtool -S` Q DROP) on the 19 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S3→S1 | 6 | 200 | 800.0 | 800.0 | 54.5 | 37493 | 37491 | 99.99% | 42.2 / 42.3 / 42.5 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 2 | 2 | S3→S2 | None | 100 | 800.0 | 800.0 | – | 0 | – | – | – | – | – | – | – | – |
| 3 | 3 | S3→S2 | None | 200 | 200.0 | 200.0 | – | 0 | – | – | – | – | – | – | – | – |
| 4 | 4 | S3→S1 | 7 | 100 | 400.0 | 400.0 | 45.8 | 74988 | 74985 | 100.00% | 33.5 / 33.7 / 33.9 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 5 | 5 | S1→S3 | None | 300 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 6 | 6 | S2→S3 | 7 | 100 | 200.0 | 200.0 | 95.8 | 150000 | 150000 | 100.00% | 83.4 / 83.6 / 83.8 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 7 | 7 | S2→S1 | 7 | 100 | 400.0 | 400.0 | 79.1 | 75000 | 75000 | 100.00% | 52.4 / 52.8 / 53.2 | 0.1 | 0.2 | 0 | 0.00% | 0 |
| 8 | 8 | S2→S3 | 6 | 400 | 800.0 | 800.0 | 95.8 | 37500 | 37500 | 100.00% | 83.4 / 83.6 / 83.8 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 9 | 9 | S3→S2 | 7 | 500 | 800.0 | 800.0 | 95.8 | 37493 | 37491 | 99.99% | 83.4 / 83.6 / 83.8 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 10 | 10 | S3→S1 | 7 | 400 | 200.0 | 200.0 | 45.8 | 149978 | 149973 | 100.00% | 33.5 / 33.7 / 33.9 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 11 | 11 | S2→S1 | None | 300 | 800.0 | 800.0 | – | 0 | – | – | – | – | – | – | – | – |
| 12 | 12 | S1→S2 | 7 | 200 | 800.0 | 800.0 | 79.1 | 37496 | 37496 | 100.00% | 66.8 / 67.0 / 67.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 13 | 13 | S2→S3 | None | 300 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 14 | 14 | S1→S3 | 6 | 400 | 200.0 | 200.0 | 45.8 | 149991 | 149991 | 100.00% | 33.4 / 33.7 / 233.7 | 1.3 | 0.0 | 6 | 0.00% | 0 |
| 15 | 15 | S2→S1 | None | 500 | 200.0 | 200.0 | – | 0 | – | – | – | – | – | – | – | – |
| 16 | 16 | S2→S1 | 7 | 500 | 400.0 | 400.0 | 79.8 | 75000 | 75000 | 100.00% | 67.4 / 67.6 / 67.8 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 17 | 17 | S2→S1 | None | 500 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 18 | 18 | S3→S1 | None | 500 | 200.0 | 200.0 | – | 0 | – | – | – | – | – | – | – | – |
| 19 | 19 | S3→S2 | None | 300 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 20 | 20 | S2→S1 | 6 | 200 | 800.0 | 800.0 | 79.1 | 37500 | 37500 | 100.00% | 66.8 / 67.0 / 67.1 | 0.1 | 0.0 | 0 | 0.00% | 0 |
