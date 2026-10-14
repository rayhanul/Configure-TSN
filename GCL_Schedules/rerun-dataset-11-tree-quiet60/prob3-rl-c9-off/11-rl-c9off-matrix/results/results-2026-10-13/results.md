# Traffic run: rerun-dataset-11-tree-quiet60/prob3-rl-c9-off/11-rl-c9off-matrix, 2026-10-13 15:04

25 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **1679575 / 1687427 packets (99.53%)**
- Deadline misses: **120 (0.01% of received)**; flows with zero misses: 12 / 25

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 12 | 99.73% | 121.4 | 0.01% |
| S2 | 7 | 99.40% | 94.4 | 0.01% |
| S3 | 6 | 99.40% | 146.3 | 0.01% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7276524.181] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7443654.989] rms   12 max   26 freq  -6403 +/-  15 delay    26 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[1135911.393] rms   38 max   62 freq  +2313 +/-  51 delay    49 +/-   0`
- Connectivity: 25 / 25 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 37 |
| S2 | 0 | 0 | 1 |
| S3 | 0 | 28 | 35 |

Switch queue drops (`ethtool -S` Q DROP) on the 17 gated ports: sw01/p4 +3341, sw02/p4 +2115, sw07/p4 +1502, sw08/p2 +4, sw08/p4 +888.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S1→S2 | 6 | 500 | 200.0 | 200.0 | 79.1 | 149989 | 148779 | 99.19% | 67.0 / 101.6 / 320867.1 | 3314.3 | 2.2 | 16 | 0.01% | 0 |
| 2 | 2 | S3→S2 | 6 | 400 | 200.0 | 200.0 | 95.8 | 149990 | 148774 | 99.19% | 67.0 / 92.9 / 320871.2 | 2625.7 | 2.2 | 10 | 0.01% | 0 |
| 3 | 3 | S1→S2 | 7 | 500 | 400.0 | 400.0 | 83.6 | 74992 | 74992 | 100.00% | 71.5 / 71.7 / 71.9 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 4 | 4 | S2→S3 | 6 | 500 | 400.0 | 400.0 | 108.2 | 75000 | 74400 | 99.20% | 28.0 / 84.4 / 320805.1 | 4209.9 | 4.6 | 13 | 0.02% | 0 |
| 5 | 5 | S2→S1 | 7 | 200 | 200.0 | 200.0 | 79.1 | 150000 | 150000 | 100.00% | 50.5 / 53.8 / 54.3 | 0.3 | 0.1 | 0 | 0.00% | 0 |
| 6 | 7 | S2→S1 | 7 | 300 | 800.0 | 800.0 | 79.1 | 37500 | 37500 | 100.00% | 16.0 / 29.3 / 30.1 | 1.2 | 0.2 | 0 | 0.00% | 0 |
| 7 | 8 | S3→S2 | 6 | 500 | 200.0 | 200.0 | 96.4 | 149991 | 148775 | 99.19% | 84.3 / 106.0 / 320853.0 | 2625.8 | 2.2 | 10 | 0.01% | 0 |
| 8 | 9 | S3→S2 | 7 | 100 | 800.0 | 800.0 | 95.8 | 37499 | 37498 | 100.00% | 29.9 / 83.4 / 84.1 | 4.8 | 0.0 | 0 | 0.00% | 0 |
| 9 | 10 | S3→S1 | 7 | 300 | 400.0 | 400.0 | 145.7 | 74996 | 74996 | 100.00% | 45.2 / 108.2 / 109.5 | 4.1 | 0.6 | 0 | 0.00% | 0 |
| 10 | 12 | S2→S3 | 6 | 300 | 400.0 | 400.0 | 126.4 | 74999 | 74398 | 99.20% | 58.7 / 138.2 / 320771.8 | 4046.2 | 60.0 | 12 | 0.02% | 0 |
| 11 | 13 | S1→S3 | 7 | 300 | 800.0 | 800.0 | 366.4 | 37499 | 37499 | 100.00% | 308.6 / 308.9 / 309.1 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 12 | 15 | S2→S3 | 6 | 300 | 800.0 | 800.0 | 134.1 | 37500 | 37199 | 99.20% | 80.7 / 139.9 / 320696.6 | 4047.5 | 8.9 | 6 | 0.02% | 0 |
| 13 | 16 | S3→S1 | 7 | 500 | 400.0 | 400.0 | 193.0 | 74996 | 74996 | 100.00% | 114.7 / 180.6 / 181.3 | 5.9 | 0.0 | 0 | 0.00% | 0 |
| 14 | 17 | S1→S2 | 6 | 400 | 400.0 | 400.0 | 109.8 | 74992 | 74387 | 99.19% | 97.7 / 132.3 / 320837.1 | 3314.5 | 4.3 | 8 | 0.01% | 0 |
| 15 | 18 | S2→S3 | 7 | 500 | 800.0 | 800.0 | 95.8 | 37500 | 37500 | 100.00% | 36.5 / 83.5 / 84.1 | 4.2 | 0.0 | 0 | 0.00% | 0 |
| 16 | 19 | S3→S1 | 7 | 400 | 800.0 | 800.0 | 380.2 | 37498 | 37498 | 100.00% | 106.1 / 172.0 / 172.7 | 5.9 | 0.0 | 0 | 0.00% | 0 |
| 17 | 20 | S1→S2 | 7 | 500 | 400.0 | 400.0 | 84.2 | 74992 | 74992 | 100.00% | 46.7 / 50.9 / 51.1 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 18 | 23 | S2→S1 | 6 | 300 | 800.0 | 800.0 | 115.8 | 37500 | 37204 | 99.21% | 103.8 / 197.7 / 320787.6 | 5447.8 | 8.8 | 11 | 0.03% | 0 |
| 19 | 25 | S2→S1 | 6 | 300 | 800.0 | 800.0 | 175.7 | 37500 | 37204 | 99.21% | 84.7 / 170.3 / 320488.0 | 5195.9 | 9.0 | 10 | 0.03% | 0 |
| 20 | 28 | S2→S1 | 7 | 400 | 800.0 | 800.0 | 79.0 | 37500 | 37500 | 100.00% | 54.3 / 61.9 / 62.1 | 0.7 | 0.0 | 0 | 0.00% | 0 |
| 21 | 36 | S2→S1 | 6 | 500 | 800.0 | 800.0 | 183.0 | 37500 | 37204 | 99.21% | 171.1 / 256.4 / 320397.4 | 5193.2 | 8.8 | 10 | 0.03% | 0 |
| 22 | 37 | S3→S1 | 6 | 500 | 800.0 | 800.0 | 145.6 | 37499 | 37195 | 99.19% | 133.6 / 159.6 / 321157.7 | 2876.9 | 8.7 | 3 | 0.01% | 0 |
| 23 | 39 | S3→S1 | 6 | 500 | 400.0 | 400.0 | 216.0 | 74996 | 74388 | 99.19% | 112.8 / 147.4 / 321137.4 | 2875.3 | 21.6 | 6 | 0.01% | 0 |
| 24 | 46 | S1→S3 | 6 | 500 | 800.0 | 800.0 | 233.3 | 37499 | 37197 | 99.19% | 149.1 / 192.5 / 320992.8 | 3701.2 | 8.9 | 5 | 0.01% | 0 |
| 25 | 50 | S2→S1 | 7 | 400 | 800.0 | 800.0 | 79.0 | 37500 | 37500 | 100.00% | 44.9 / 52.4 / 52.7 | 0.7 | 0.0 | 0 | 0.00% | 0 |
