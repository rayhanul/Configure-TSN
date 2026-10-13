# Traffic run: result-2026-10-12-dataset-testbed-10-ring-avgwin/smt-c9-on/10-fair-retimed-c9on, 2026-10-12 16:27

11 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **1006223 / 1012482 packets (99.38%)**
- Deadline misses: **245 (0.02% of received)**; flows with zero misses: 4 / 11

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 4 | 99.83% | 61.6 | 0.02% |
| S2 | 3 | 98.96% | 124.4 | 0.05% |
| S3 | 4 | 99.47% | 45.9 | 0.01% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7276524.181] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7362249.176] rms    7 max   11 freq  -6378 +/-   8 delay    23 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[1054505.943] rms    8 max   14 freq  +2166 +/-   9 delay    48 +/-   0`
- Connectivity: 11 / 11 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 0 |
| S2 | 0 | 0 | 0 |
| S3 | 0 | 2 | 18 |

Switch queue drops (`ethtool -S` Q DROP) on the 19 gated ports: sw01/p4 +1570, sw02/p4 +1940, sw03/p4 +6, sw07/p4 +2370, sw08/p4 +371.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S3→S1 | 6 | 400 | 400.0 | 400.0 | 27.9 | 74996 | 74995 | 100.00% | 15.6 / 15.8 / 16.0 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 2 | 3 | S1→S3 | 6 | 400 | 200.0 | 200.0 | 27.9 | 150000 | 150000 | 100.00% | 15.6 / 15.8 / 216.8 | 1.1 | 0.0 | 4 | 0.00% | 0 |
| 3 | 5 | S3→S1 | 7 | 400 | 800.0 | 800.0 | 31.1 | 37499 | 37499 | 100.00% | 18.8 / 19.0 / 19.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 4 | 7 | S2→S3 | 7 | 200 | 200.0 | 200.0 | 43.0 | 150000 | 148416 | 98.94% | 30.6 / 76.0 / 320830.8 | 3794.7 | 4.3 | 23 | 0.02% | 0 |
| 5 | 9 | S3→S2 | 7 | 400 | 200.0 | 200.0 | 51.0 | 149991 | 148421 | 98.95% | 38.6 / 105.6 / 320838.8 | 4606.1 | 4.3 | 50 | 0.03% | 0 |
| 6 | 10 | S2→S1 | 6 | 400 | 800.0 | 800.0 | 43.3 | 37500 | 37129 | 99.01% | 31.0 / 293.5 / 320831.2 | 9028.7 | 17.3 | 44 | 0.12% | 0 |
| 7 | 11 | S2→S3 | 7 | 200 | 400.0 | 400.0 | 43.0 | 75000 | 74208 | 98.94% | 30.6 / 73.9 / 320807.6 | 3705.1 | 8.7 | 11 | 0.01% | 0 |
| 8 | 12 | S1→S2 | 7 | 500 | 200.0 | 200.0 | 45.8 | 150000 | 148430 | 98.95% | 33.4 / 100.8 / 320833.7 | 4613.4 | 4.3 | 67 | 0.05% | 0 |
| 9 | 15 | S3→S1 | 6 | 300 | 400.0 | 400.0 | 26.0 | 74996 | 74995 | 100.00% | 13.7 / 13.9 / 14.0 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 10 | 17 | S1→S2 | 6 | 400 | 800.0 | 800.0 | 43.3 | 37500 | 37130 | 99.01% | 30.9 / 293.8 / 320831.1 | 9028.7 | 17.3 | 46 | 0.12% | 0 |
| 11 | 18 | S1→S3 | 6 | 200 | 400.0 | 400.0 | 30.8 | 75000 | 75000 | 100.00% | 18.5 / 18.7 / 22.1 | 0.1 | 0.0 | 0 | 0.00% | 0 |
