# Traffic run: result-2026-10-10-dataset-testbed-5-avgwin/prob3-rl-c9-off/5-rl-c9off-matrix, 2026-10-11 00:48

25 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **1874935 / 1874949 packets (100.00%)**
- Deadline misses: **2 (0.00% of received)**; flows with zero misses: 23 / 25

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 7 | 100.00% | 121.5 | 0.00% |
| S2 | 7 | 100.00% | 78.3 | 0.00% |
| S3 | 11 | 100.00% | 96.8 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7192691.373] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7219547.146] rms    6 max   12 freq  -6198 +/-   8 delay    23 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[911803.550] rms   39 max   48 freq  +3015 +/-  53 delay    48 +/-   0`
- Connectivity: 25 / 25 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 0 |
| S2 | 0 | 0 | 0 |
| S3 | 0 | 14 | 51 |

Switch queue drops (`ethtool -S` Q DROP) on the 17 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S3→S1 | 6 | 200 | 800.0 | 800.0 | 237.8 | 37497 | 37496 | 100.00% | 159.6 / 160.3 / 161.0 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 2 | 2 | S2→S3 | 6 | 300 | 200.0 | 200.0 | 95.8 | 150000 | 150000 | 100.00% | 19.8 / 52.2 / 83.8 | 31.5 | 62.9 | 0 | 0.00% | 0 |
| 3 | 3 | S1→S2 | 6 | 100 | 800.0 | 800.0 | 84.2 | 37500 | 37500 | 100.00% | 46.5 / 49.9 / 54.0 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 4 | 4 | S1→S3 | 7 | 300 | 800.0 | 800.0 | 176.3 | 37500 | 37500 | 100.00% | 164.1 / 164.3 / 164.5 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 5 | 5 | S2→S3 | 7 | 100 | 800.0 | 800.0 | 95.8 | 37500 | 37500 | 100.00% | 83.4 / 83.6 / 83.8 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 6 | 6 | S2→S3 | 6 | 200 | 400.0 | 400.0 | 100.5 | 75000 | 75000 | 100.00% | 88.2 / 88.4 / 88.6 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 7 | 7 | S3→S2 | 6 | 500 | 400.0 | 400.0 | 157.1 | 74995 | 74994 | 100.00% | 144.8 / 145.1 / 884.0 | 2.7 | 0.0 | 1 | 0.00% | 0 |
| 8 | 8 | S3→S1 | 6 | 500 | 200.0 | 200.0 | 145.6 | 149989 | 149986 | 100.00% | 75.4 / 102.5 / 117.1 | 16.9 | 28.8 | 0 | 0.00% | 0 |
| 9 | 9 | S2→S1 | 7 | 500 | 400.0 | 400.0 | 79.1 | 75000 | 75000 | 100.00% | 33.3 / 34.0 / 34.7 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 10 | 10 | S1→S2 | 7 | 500 | 200.0 | 200.0 | 79.1 | 150000 | 150000 | 100.00% | 66.7 / 67.0 / 67.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 11 | 11 | S2→S3 | 7 | 500 | 400.0 | 400.0 | 95.7 | 75000 | 75000 | 100.00% | 74.8 / 75.0 / 75.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 12 | 12 | S3→S2 | 7 | 500 | 200.0 | 200.0 | 95.8 | 149989 | 149986 | 100.00% | 83.4 / 83.6 / 683.6 | 1.6 | 0.0 | 1 | 0.00% | 0 |
| 13 | 13 | S1→S3 | 6 | 400 | 800.0 | 800.0 | 145.7 | 37500 | 37500 | 100.00% | 121.3 / 121.7 / 122.2 | 0.2 | 0.2 | 0 | 0.00% | 0 |
| 14 | 14 | S1→S3 | 6 | 100 | 200.0 | 200.0 | 162.9 | 150000 | 150000 | 100.00% | 106.7 / 121.9 / 151.0 | 17.0 | 21.7 | 0 | 0.00% | 0 |
| 15 | 15 | S2→S3 | 7 | 500 | 200.0 | 200.0 | 95.7 | 150000 | 150000 | 100.00% | 83.4 / 83.6 / 83.8 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 16 | 16 | S3→S2 | 7 | 200 | 800.0 | 800.0 | 97.0 | 37497 | 37496 | 100.00% | 33.7 / 42.0 / 42.2 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 17 | 17 | S1→S2 | 6 | 400 | 400.0 | 400.0 | 83.6 | 75000 | 75000 | 100.00% | 71.2 / 71.5 / 75.6 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 18 | 18 | S1→S3 | 7 | 400 | 400.0 | 400.0 | 148.5 | 75000 | 75000 | 100.00% | 136.2 / 136.4 / 136.6 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 19 | 19 | S3→S2 | 7 | 500 | 400.0 | 400.0 | 96.4 | 74994 | 74992 | 100.00% | 62.6 / 62.8 / 63.0 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 20 | 22 | S3→S1 | 7 | 100 | 800.0 | 800.0 | 253.8 | 37496 | 37495 | 100.00% | 227.1 / 227.5 / 227.9 | 0.1 | 0.1 | 0 | 0.00% | 0 |
| 21 | 28 | S1→S3 | 7 | 500 | 800.0 | 800.0 | 145.6 | 37500 | 37500 | 100.00% | 123.9 / 124.1 / 124.3 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 22 | 31 | S3→S1 | 7 | 500 | 800.0 | 800.0 | 257.6 | 37496 | 37495 | 100.00% | 218.5 / 218.9 / 219.3 | 0.1 | 0.1 | 0 | 0.00% | 0 |
| 23 | 43 | S3→S1 | 7 | 300 | 800.0 | 800.0 | 428.2 | 37496 | 37495 | 100.00% | 209.8 / 210.2 / 210.6 | 0.1 | 0.1 | 0 | 0.00% | 0 |
| 24 | 45 | S1→S3 | 6 | 200 | 800.0 | 800.0 | 162.9 | 37500 | 37500 | 100.00% | 102.6 / 102.8 / 103.0 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 25 | 50 | S2→S1 | 6 | 500 | 800.0 | 800.0 | 79.0 | 37500 | 37500 | 100.00% | 37.4 / 41.7 / 41.9 | 0.1 | 0.0 | 0 | 0.00% | 0 |
