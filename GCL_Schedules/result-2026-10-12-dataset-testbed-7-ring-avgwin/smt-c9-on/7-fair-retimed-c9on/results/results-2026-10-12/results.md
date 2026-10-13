# Traffic run: result-2026-10-12-dataset-testbed-7-ring-avgwin/smt-c9-on/7-fair-retimed-c9on, 2026-10-12 15:19

11 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time (1000 µs sender lead), NIC RX timestamps, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **1005015 / 1012469 packets (99.26%)**
- Deadline misses: **224 (0.02% of received)**; flows with zero misses: 3 / 11

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 4 | 99.89% | 45.7 | 0.02% |
| S2 | 6 | 98.95% | 75.8 | 0.02% |
| S3 | 1 | 98.97% | 176.2 | 0.08% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7276524.181] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[7358171.303] rms    9 max   18 freq  -6849 +/-  12 delay    24 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[1050428.321] rms   17 max   28 freq  +2844 +/-  10 delay    48 +/-   0`
- Connectivity: 11 / 11 sender routes answered ping

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 5 |
| S2 | 0 | 0 | 0 |
| S3 | 0 | 0 | 26 |

Switch queue drops (`ethtool -S` Q DROP) on the 19 gated ports: sw01/p4 +1574, sw02/p4 +4740, sw02/p5 +52, sw07/p4 +770, sw08/p4 +370.

## Per flow

Latency = receiver NIC's hardware RX timestamp − sender NIC's launch time (the sender's NIC sends each frame at its scheduled time via SO_TXTIME + etf offload), both on PTP-synced NIC clocks: NIC to NIC, no software time involved. Schedule e2e = the scheduler's end-to-end bound. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. No NIC ts = frames received without a hardware timestamp (counted as received, left out of latency).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | no NIC ts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S1→S2 | 7 | 200 | 200.0 | 200.0 | 36.9 | 149998 | 148422 | 98.95% | 24.5 / 78.3 / 320024.7 | 4125.4 | 4.3 | 28 | 0.02% | 0 |
| 2 | 3 | S2→S3 | 7 | 500 | 400.0 | 400.0 | 54.2 | 75000 | 74230 | 98.97% | 41.8 / 176.2 / 320842.1 | 6491.8 | 8.7 | 63 | 0.08% | 0 |
| 3 | 5 | S1→S2 | 7 | 200 | 800.0 | 800.0 | 36.9 | 37500 | 37106 | 98.95% | 24.5 / 76.2 / 319951.6 | 4045.4 | 17.3 | 6 | 0.02% | 0 |
| 4 | 7 | S2→S1 | 6 | 500 | 800.0 | 800.0 | 45.8 | 37500 | 37130 | 99.01% | 33.5 / 300.2 / 320033.7 | 9066.0 | 17.3 | 59 | 0.16% | 0 |
| 5 | 8 | S3→S1 | 7 | 500 | 400.0 | 400.0 | 33.7 | 74996 | 74996 | 100.00% | 21.4 / 21.5 / 21.7 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 6 | 9 | S3→S1 | 7 | 100 | 200.0 | 200.0 | 22.8 | 149991 | 149991 | 100.00% | 10.5 / 10.7 / 10.8 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 7 | 12 | S1→S2 | 6 | 300 | 200.0 | 200.0 | 51.0 | 149998 | 148414 | 98.94% | 26.4 / 63.5 / 320026.5 | 3410.6 | 4.3 | 20 | 0.01% | 0 |
| 8 | 15 | S1→S2 | 6 | 300 | 400.0 | 400.0 | 39.4 | 74999 | 74208 | 98.95% | 27.1 / 66.0 / 320004.6 | 3509.4 | 8.6 | 11 | 0.01% | 0 |
| 9 | 18 | S3→S1 | 6 | 300 | 400.0 | 400.0 | 26.0 | 74996 | 74996 | 100.00% | 13.7 / 13.9 / 14.0 | 0.1 | 0.0 | 0 | 0.00% | 0 |
| 10 | 19 | S1→S2 | 6 | 200 | 800.0 | 800.0 | 36.9 | 37500 | 37105 | 98.95% | 24.5 / 67.7 / 319957.2 | 3699.0 | 17.3 | 5 | 0.01% | 0 |
| 11 | 20 | S3→S2 | 6 | 100 | 200.0 | 200.0 | 38.2 | 149991 | 148417 | 98.95% | 25.8 / 92.4 / 320826.0 | 4595.4 | 4.3 | 32 | 0.02% | 0 |
