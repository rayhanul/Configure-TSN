# Traffic run: rerun-dataset-11-tree-quiet60/rl-c9-off/11-matrix-c9off, 2026-10-13 14:53

20 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **937475 / 937475 packets (100.00%)**
- Deadline misses: **0 (0.00% of received)**; flows with zero misses: 10 / 20

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 3 | 100.00% | 66.0 | 0.00% |
| S2 | 6 | 100.00% | 71.9 | 0.00% |
| S3 | 1 | 100.00% | 83.9 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7276524.181] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7443036.891] rms   24 max   63 freq  -6318 +/-  31 delay    24 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[1135294.174] rms   27 max   39 freq  +2282 +/-  36 delay    48 +/-   0`
- Connectivity: 10 / 10 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 0 |
| S2 | 0 | 0 | 3 |
| S3 | 0 | 0 | 22 |

Switch queue drops (`ethtool -S` Q DROP) on the 17 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S1→S2 | 6 | 500 | 200.0 | 200.0 | 79.1 | 150000 | 150000 | 100.00% | 67.0 / 67.2 / 70.8 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 2 | 2 | S3→S2 | 6 | 400 | 200.0 | 200.0 | 95.8 | 149991 | 149991 | 100.00% | 67.1 / 71.4 / 71.6 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 3 | 3 | S1→S2 | 7 | 500 | 400.0 | 400.0 | 83.6 | 75000 | 75000 | 100.00% | 71.5 / 71.7 / 72.0 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 4 | 4 | S2→S3 | None | 500 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 5 | 5 | S2→S1 | 7 | 200 | 200.0 | 200.0 | 79.1 | 149999 | 149999 | 100.00% | 53.5 / 53.8 / 54.3 | 0.1 | 0.1 | 0 | 0.00% | 0 |
| 6 | 6 | S3→S1 | None | 200 | 200.0 | 200.0 | – | 0 | – | – | – | – | – | – | – | – |
| 7 | 7 | S2→S1 | 7 | 300 | 800.0 | 800.0 | 79.1 | 37499 | 37499 | 100.00% | 28.7 / 29.4 / 30.2 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 8 | 8 | S3→S2 | 6 | 500 | 200.0 | 200.0 | 96.4 | 149992 | 149992 | 100.00% | 84.3 / 84.5 / 84.8 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 9 | 9 | S3→S2 | 7 | 100 | 800.0 | 800.0 | 95.8 | 37498 | 37498 | 100.00% | 83.7 / 83.9 / 84.1 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 10 | 10 | S3→S1 | 7 | 300 | 400.0 | 400.0 | 145.7 | 74997 | 74997 | 100.00% | 108.0 / 108.6 / 109.5 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 11 | 11 | S1→S3 | None | 100 | 200.0 | 200.0 | – | 0 | – | – | – | – | – | – | – | – |
| 12 | 12 | S2→S3 | None | 300 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 13 | 13 | S1→S3 | None | 300 | 800.0 | 800.0 | – | 0 | – | – | – | – | – | – | – | – |
| 14 | 14 | S3→S1 | None | 400 | 200.0 | 200.0 | – | 0 | – | – | – | – | – | – | – | – |
| 15 | 15 | S2→S3 | None | 300 | 800.0 | 800.0 | – | 0 | – | – | – | – | – | – | – | – |
| 16 | 16 | S3→S1 | None | 500 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 17 | 17 | S1→S2 | None | 400 | 400.0 | 400.0 | – | 0 | – | – | – | – | – | – | – | – |
| 18 | 18 | S2→S3 | 7 | 500 | 800.0 | 800.0 | 95.8 | 37499 | 37499 | 100.00% | 83.7 / 83.9 / 84.1 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 19 | 19 | S3→S1 | None | 400 | 800.0 | 800.0 | – | 0 | – | – | – | – | – | – | – | – |
| 20 | 20 | S1→S2 | 7 | 500 | 400.0 | 400.0 | 84.2 | 75000 | 75000 | 100.00% | 50.7 / 50.9 / 51.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
