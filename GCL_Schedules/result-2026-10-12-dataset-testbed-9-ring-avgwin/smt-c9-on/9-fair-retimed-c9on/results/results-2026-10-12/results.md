# Traffic run: result-2026-10-12-dataset-testbed-9-ring-avgwin/smt-c9-on/9-fair-retimed-c9on, 2026-10-12 16:06

11 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **857793 / 862484 packets (99.46%)**
- Deadline misses: **175 (0.02% of received)**; flows with zero misses: 3 / 11

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 6 | 99.56% | 43.8 | 0.01% |
| S2 | 2 | 99.01% | 296.7 | 0.13% |
| S3 | 3 | 99.41% | 51.1 | 0.01% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7276524.181] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7360974.339] rms    9 max   17 freq  -6393 +/-   8 delay    24 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[1053231.482] rms   22 max   51 freq  +2158 +/-  30 delay    47 +/-   0`
- Connectivity: 11 / 11 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 0 |
| S2 | 0 | 0 | 0 |
| S3 | 0 | 0 | 16 |

Switch queue drops (`ethtool -S` Q DROP) on the 19 gated ports: sw01/p4 +371, sw02/p4 +370, sw07/p4 +1975, sw08/p4 +1975.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S3→S1 | 6 | 200 | 800.0 | 800.0 | 24.7 | 37498 | 37498 | 100.00% | 12.4 / 12.6 / 12.7 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 2 | 4 | S3→S1 | 7 | 100 | 400.0 | 400.0 | 33.4 | 74995 | 74995 | 100.00% | 21.0 / 21.2 / 21.4 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 3 | 6 | S2→S3 | 6 | 100 | 200.0 | 200.0 | 40.7 | 150000 | 148420 | 98.95% | 22.9 / 77.0 / 320823.1 | 4135.3 | 4.4 | 28 | 0.02% | 0 |
| 4 | 7 | S2→S1 | 6 | 100 | 400.0 | 400.0 | 33.0 | 75000 | 74210 | 98.95% | 20.7 / 76.8 / 320820.9 | 4220.8 | 8.7 | 16 | 0.02% | 0 |
| 5 | 8 | S2→S3 | 6 | 400 | 800.0 | 800.0 | 51.0 | 37500 | 37105 | 98.95% | 38.6 / 90.4 / 320753.7 | 4055.5 | 17.3 | 6 | 0.02% | 0 |
| 6 | 9 | S3→S2 | 7 | 500 | 800.0 | 800.0 | 54.2 | 37499 | 37128 | 99.01% | 41.8 / 309.2 / 320841.9 | 9089.4 | 17.3 | 59 | 0.16% | 0 |
| 7 | 10 | S3→S1 | 6 | 400 | 200.0 | 200.0 | 27.9 | 149992 | 149992 | 100.00% | 15.6 / 15.8 / 16.0 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 8 | 12 | S1→S2 | 6 | 200 | 800.0 | 800.0 | 36.9 | 37500 | 37130 | 99.01% | 24.5 / 284.3 / 320824.6 | 8969.2 | 17.3 | 37 | 0.10% | 0 |
| 9 | 14 | S1→S3 | 6 | 400 | 200.0 | 200.0 | 27.9 | 150000 | 150000 | 100.00% | 15.6 / 15.8 / 216.8 | 1.3 | 0.0 | 6 | 0.00% | 0 |
| 10 | 16 | S2→S1 | 6 | 500 | 400.0 | 400.0 | 50.0 | 75000 | 74210 | 98.95% | 37.7 / 89.5 / 320798.4 | 4057.0 | 8.7 | 16 | 0.02% | 0 |
| 11 | 20 | S2→S1 | 6 | 200 | 800.0 | 800.0 | 36.9 | 37500 | 37105 | 98.95% | 24.5 / 76.4 / 320752.7 | 4059.7 | 17.3 | 7 | 0.02% | 0 |
