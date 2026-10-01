# Traffic run: prob3-rl-c9-on/1-rl-c9on-matrix, 2026-10-01 14:37

48 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Mode: NIC launch time, real-time processes. Raw output: `results_<node>.log`.

## Summary

- Delivered: **4086992 / 4087500 packets (99.99%)**
- Deadline misses: **187439 (4.59% of received)**; flows with zero misses: 44 / 48

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 16 | 99.98% | 161.4 | 13.89% |
| S2 | 21 | 99.99% | 96.6 | 0.00% |
| S3 | 11 | 99.98% | 124.1 | 0.00% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[6405595.467] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[6405259.873] rms   15 max   24 freq  -6333 +/-  19 delay    16 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[97565.586] rms   33 max   55 freq  +2832 +/-  45 delay    48 +/-   0`
- Connectivity: 48 / 48 sender routes answered ping

## Observations

First run with every host-side improvement: frames launched by the sender's NIC at their scheduled
time (`SO_TXTIME` + etf offload), latency from NIC hardware RX timestamps, one epoll receiver and
one sender loop per node in separate real-time processes, 4 MiB socket buffers. Compared with the
Python-timed runs earlier today (82–84% delivered, 61% deadline misses):

- **Loss: 99.99% delivered.** No socket-buffer drops on any node, no queue drops on any of the 27
  gated switch ports. The remaining 0.01% are frames the senders' etf queues dropped (S2 329,
  S3 183, S1 1).
- **Jitter is sub-µs on most flows** (standard deviation 0.1–0.5 µs), i.e. the network delivers
  each flow with a fixed, repeatable latency.
- **Deadline misses: 4.59% of received, on 2 flows only**: flow 2 (S2→S1, 75.00%) and 300003
  (S2→S1, 49.99%), plus one packet each on flows 1 and 20. 75% and 50% are exactly 3 and 2 of the 4
  instances per 800 µs cycle, so specific instances are late every cycle.
- **Latency vs. the schedule:** 17 flows arrive within 10 µs of the schedule's `e2e_ns` (e.g. flow
  40: 6.1 µs measured vs 5.4 µs scheduled; flow 34: 7.0 vs 6.4). 31 flows arrive with a constant
  extra delay (e.g. flow 5: 367 µs vs 10.9 µs), which means they miss a gate window at some hop
  and wait for a later window of the same queue.

Checked and ruled out as the cause of the extra delay:
- Sender timing: every instance of every flow is launched inside its first-hop window
  (0 violations), since the NIC launches it at exactly `basetime + n*period + psi_ns`.
- GCL tick rounding in `configure_gcl.py`: all 448 scheduled switch windows are fully covered by
  the deployed (320 ns-rounded) gates.

Likely cause, in the schedule: in 145 of 164 hop pairs the scheduler opens the next hop's window
2,240 ns after the previous hop's, regardless of frame size. A store-and-forward switch can only
forward a frame after receiving all of it plus processing (`C_ns` + 2,000 ns = 5.5–6.2 µs for
these frames), and many windows have 0 ns slack, so such frames miss their window. Confirming
this needs a per-hop measurement (e.g. hardware-timestamped capture at an intermediate switch
port, or the switches' forwarding mode); the fix would be in the scheduler's hop-delay model.

## Drop counters (during the run)

| node | UDP receive-buffer drops | launch-time (etf) drops | frames skipped by sender (too late) |
|---|---|---|---|
| S1 | 0 | 1 | 0 |
| S2 | 0 | 329 | 0 |
| S3 | 0 | 183 | 0 |

Switch queue drops (`ethtool -S` Q DROP) on the 27 gated ports: none.

## Per flow

Latency = receiver NIC's hardware RX timestamp − launch time: the sender's NIC sent the frame at that time (SO_TXTIME, etf offload), so this is NIC to NIC on PTP-synced clocks. Schedule e2e = the scheduler's end-to-end bound for the flow. HW RX = share of packets with a NIC timestamp. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline. Release lag = send call − scheduled time on the sender (negative = queued ahead for launch time).

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | schedule e2e (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % | HW RX | release lag avg / max (µs) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S3→S1 | 7 | 500 | 200.0 | 200.0 | 8.6 | 150000 | 149990 | 99.99% | 12.6 / 14.5 / 367.6 | 1.8 | 3.2 | 1 | 0.00% | 100.0% | -993.0 / -386.6 |
| 2 | 2 | S2→S1 | 6 | 400 | 200.0 | 200.0 | 12.5 | 150000 | 149951 | 99.97% | 32.8 / 276.3 / 428.8 | 158.9 | 196.7 | 112468 | 75.00% | 100.0% | -996.1 / -472.6 |
| 3 | 3 | S3→S2 | 7 | 100 | 200.0 | 200.0 | 9.9 | 150000 | 149987 | 99.99% | 9.8 / 52.8 / 95.8 | 42.5 | 84.9 | 0 | 0.00% | 100.0% | -991.9 / -384.1 |
| 4 | 4 | S1→S3 | 6 | 300 | 800.0 | 800.0 | 171.2 | 37500 | 37500 | 100.00% | 269.9 / 273.3 / 274.1 | 0.1 | 0.0 | 0 | 0.00% | 100.0% | -996.0 / -987.9 |
| 5 | 5 | S2→S1 | 6 | 200 | 400.0 | 400.0 | 10.9 | 75000 | 74982 | 99.98% | 363.4 / 367.1 / 370.9 | 3.5 | 7.0 | 0 | 0.00% | 100.0% | -988.0 / -468.5 |
| 6 | 6 | S2→S1 | 7 | 100 | 400.0 | 400.0 | 9.9 | 75000 | 74969 | 99.96% | 54.4 / 112.0 / 348.7 | 56.1 | 112.0 | 0 | 0.00% | 100.0% | -982.2 / -533.1 |
| 7 | 7 | S2→S1 | 6 | 300 | 800.0 | 800.0 | 14.4 | 37500 | 37483 | 99.95% | 350.9 / 351.1 / 351.4 | 0.1 | 0.0 | 0 | 0.00% | 100.0% | -948.6 / -500.2 |
| 8 | 8 | S2→S3 | 7 | 100 | 800.0 | 800.0 | 9.9 | 37500 | 37480 | 99.95% | 62.5 / 63.2 / 63.9 | 0.2 | 0.2 | 0 | 0.00% | 100.0% | -965.4 / -520.2 |
| 9 | 9 | S3→S2 | 7 | 500 | 200.0 | 200.0 | 13.1 | 150000 | 149987 | 99.99% | 35.8 / 65.6 / 95.8 | 29.7 | 59.3 | 0 | 0.00% | 100.0% | -987.9 / -379.6 |
| 10 | 10 | S1→S3 | 7 | 100 | 800.0 | 800.0 | 5.4 | 37500 | 37500 | 100.00% | 48.9 / 49.1 / 49.7 | 0.1 | 0.0 | 0 | 0.00% | 100.0% | -969.9 / -939.3 |
| 11 | 11 | S3→S2 | 6 | 500 | 800.0 | 800.0 | 13.1 | 37500 | 37496 | 99.99% | 183.0 / 183.1 / 185.1 | 0.1 | 0.0 | 0 | 0.00% | 100.0% | -974.9 / -464.6 |
| 12 | 12 | S2→S1 | 7 | 100 | 800.0 | 800.0 | 9.9 | 37500 | 37481 | 99.95% | 164.8 / 169.1 / 349.6 | 1.6 | 0.1 | 0 | 0.00% | 100.0% | -989.0 / -538.0 |
| 13 | 13 | S1→S2 | 7 | 300 | 400.0 | 400.0 | 36.5 | 75000 | 75000 | 100.00% | 59.9 / 60.4 / 64.6 | 0.2 | 0.2 | 0 | 0.00% | 100.0% | -954.7 / -874.2 |
| 14 | 14 | S1→S2 | 7 | 100 | 200.0 | 200.0 | 9.9 | 150000 | 150000 | 100.00% | 59.6 / 60.1 / 60.9 | 0.2 | 0.1 | 0 | 0.00% | 100.0% | -993.1 / -959.0 |
| 15 | 15 | S2→S3 | 7 | 400 | 400.0 | 400.0 | 12.5 | 75000 | 74969 | 99.96% | 62.6 / 63.4 / 65.2 | 0.2 | 0.2 | 0 | 0.00% | 100.0% | -976.1 / -527.4 |
| 16 | 16 | S3→S2 | 7 | 200 | 200.0 | 200.0 | 145.0 | 150000 | 149985 | 99.99% | 35.8 / 65.6 / 95.8 | 29.7 | 59.3 | 0 | 0.00% | 100.0% | -986.8 / -378.5 |
| 17 | 17 | S2→S3 | 6 | 200 | 800.0 | 800.0 | 10.9 | 37500 | 37483 | 99.95% | 13.2 / 15.9 / 29.4 | 0.2 | 0.2 | 0 | 0.00% | 100.0% | -954.5 / -505.9 |
| 18 | 18 | S3→S2 | 6 | 100 | 400.0 | 400.0 | 9.9 | 75000 | 74994 | 99.99% | 187.1 / 187.3 / 187.7 | 0.1 | 0.0 | 0 | 0.00% | 100.0% | -984.5 / -455.6 |
| 19 | 19 | S3→S1 | 7 | 500 | 400.0 | 400.0 | 8.6 | 75000 | 74993 | 99.99% | 11.4 / 82.6 / 153.6 | 70.8 | 141.6 | 0 | 0.00% | 100.0% | -979.9 / -450.7 |
| 20 | 20 | S3→S1 | 7 | 200 | 200.0 | 200.0 | 6.4 | 150000 | 149985 | 99.99% | 6.6 / 8.0 / 272.1 | 1.3 | 2.1 | 1 | 0.00% | 100.0% | -983.5 / -374.9 |
| 21 | 300000 | S3→S2 | 7 | 500 | 200.0 | 200.0 | 13.1 | 150000 | 149988 | 99.99% | 22.5 / 69.4 / 116.3 | 46.3 | 92.7 | 0 | 0.00% | 100.0% | -997.7 / -458.7 |
| 22 | 300001 | S2→S3 | 7 | 300 | 400.0 | 400.0 | 11.5 | 75000 | 74968 | 99.96% | 62.5 / 63.2 / 65.0 | 0.2 | 0.2 | 0 | 0.00% | 100.0% | -973.0 / -524.3 |
| 23 | 300002 | S1→S2 | 7 | 500 | 200.0 | 200.0 | 37.8 | 150000 | 150000 | 100.00% | 59.9 / 60.4 / 61.0 | 0.2 | 0.1 | 0 | 0.00% | 100.0% | -979.7 / -890.4 |
| 24 | 300003 | S2→S1 | 7 | 100 | 200.0 | 200.0 | 18.2 | 150000 | 149957 | 99.97% | 9.7 / 134.9 / 217.6 | 84.0 | 103.6 | 74969 | 49.99% | 100.0% | -993.1 / -574.0 |
| 25 | 300004 | S1→S2 | 6 | 200 | 800.0 | 800.0 | 198.7 | 37500 | 37500 | 100.00% | 197.1 / 238.6 / 397.4 | 75.8 | 44.9 | 0 | 0.00% | 100.0% | -976.4 / -955.0 |
| 26 | 300005 | S3→S2 | 7 | 500 | 400.0 | 400.0 | 13.1 | 75000 | 74995 | 99.99% | 107.4 / 115.8 / 116.3 | 0.2 | 0.2 | 0 | 0.00% | 100.0% | -993.5 / -423.6 |
| 27 | 300006 | S1→S3 | 6 | 400 | 800.0 | 800.0 | 603.5 | 37500 | 37500 | 100.00% | 704.9 / 705.1 / 705.9 | 0.1 | 0.0 | 0 | 0.00% | 100.0% | -992.9 / -933.2 |
| 28 | 300007 | S3→S2 | 7 | 500 | 200.0 | 200.0 | 13.1 | 150000 | 149988 | 99.99% | 23.0 / 69.7 / 116.3 | 46.1 | 92.2 | 0 | 0.00% | 100.0% | -996.0 / -428.8 |
| 29 | 300008 | S2→S1 | 6 | 100 | 400.0 | 400.0 | 9.9 | 75000 | 74982 | 99.98% | 363.2 / 367.0 / 370.7 | 3.5 | 7.0 | 0 | 0.00% | 100.0% | -982.4 / -463.4 |
| 30 | 300009 | S3→S2 | 7 | 300 | 400.0 | 400.0 | 11.5 | 75000 | 74995 | 99.99% | 107.4 / 115.8 / 116.3 | 0.2 | 0.2 | 0 | 0.00% | 100.0% | -992.6 / -422.2 |
| 31 | 300011 | S1→S3 | 7 | 100 | 400.0 | 400.0 | 267.8 | 75000 | 75000 | 100.00% | 38.7 / 39.4 / 40.4 | 0.5 | 1.0 | 0 | 0.00% | 100.0% | -942.6 / -862.7 |
| 32 | 300012 | S3→S2 | 7 | 500 | 200.0 | 200.0 | 13.1 | 150000 | 149989 | 99.99% | 23.1 / 69.9 / 116.3 | 45.9 | 91.8 | 0 | 0.00% | 100.0% | -994.9 / -426.7 |
| 33 | 300013 | S1→S2 | 7 | 300 | 200.0 | 200.0 | 36.5 | 150000 | 150000 | 100.00% | 59.9 / 60.4 / 61.0 | 0.2 | 0.1 | 0 | 0.00% | 100.0% | -972.6 / -881.5 |
| 34 | 300014 | S3→S1 | 7 | 200 | 400.0 | 400.0 | 6.4 | 75000 | 74995 | 99.99% | 6.6 / 7.0 / 34.2 | 0.3 | 0.2 | 0 | 0.00% | 100.0% | -990.0 / -419.5 |
| 35 | 300015 | S2→S1 | 7 | 500 | 800.0 | 800.0 | 21.1 | 37500 | 37483 | 99.95% | 205.7 / 206.0 / 208.1 | 0.1 | 0.1 | 0 | 0.00% | 100.0% | -995.6 / -603.4 |
| 36 | 300016 | S3→S1 | 6 | 500 | 800.0 | 800.0 | 116.5 | 37500 | 37496 | 99.99% | 115.8 / 116.1 / 116.5 | 0.1 | 0.1 | 0 | 0.00% | 100.0% | -973.8 / -463.3 |
| 37 | 300017 | S2→S3 | 7 | 100 | 800.0 | 800.0 | 134.4 | 37500 | 37483 | 99.95% | 232.6 / 232.8 / 233.0 | 0.1 | 0.0 | 0 | 0.00% | 100.0% | -981.6 / -573.8 |
| 38 | 300018 | S1→S3 | 6 | 300 | 800.0 | 800.0 | 9.0 | 37500 | 37500 | 100.00% | 107.6 / 111.1 / 111.8 | 0.1 | 0.0 | 0 | 0.00% | 100.0% | -982.2 / -975.3 |
| 39 | 300019 | S1→S2 | 6 | 200 | 800.0 | 800.0 | 100.5 | 37500 | 37500 | 100.00% | 296.7 / 298.5 / 298.7 | 0.1 | 0.0 | 0 | 0.00% | 100.0% | -980.2 / -927.7 |
| 40 | 300020 | S3→S1 | 7 | 100 | 200.0 | 200.0 | 5.4 | 150000 | 149988 | 99.99% | 5.0 / 6.1 / 34.1 | 0.8 | 1.4 | 0 | 0.00% | 100.0% | -992.4 / -415.9 |
| 41 | 300021 | S3→S2 | 7 | 100 | 400.0 | 400.0 | 9.9 | 75000 | 74995 | 99.99% | 104.5 / 112.9 / 113.4 | 0.2 | 0.2 | 0 | 0.00% | 100.0% | -982.8 / -411.5 |
| 42 | 300022 | S3→S1 | 6 | 200 | 800.0 | 800.0 | 6.4 | 37500 | 37498 | 99.99% | 8.5 / 671.9 / 672.3 | 8.9 | 0.4 | 0 | 0.00% | 100.0% | -994.6 / -443.4 |
| 43 | 300023 | S3→S2 | 7 | 500 | 200.0 | 200.0 | 13.1 | 150000 | 149988 | 99.99% | 23.5 / 76.9 / 116.3 | 38.9 | 77.7 | 0 | 0.00% | 100.0% | -994.0 / -424.8 |
| 44 | 300024 | S1→S3 | 7 | 500 | 400.0 | 400.0 | 270.7 | 75000 | 75000 | 100.00% | 38.7 / 39.4 / 40.4 | 0.5 | 1.0 | 0 | 0.00% | 100.0% | -947.6 / -867.8 |
| 45 | 300025 | S3→S2 | 6 | 200 | 800.0 | 800.0 | 10.9 | 37500 | 37496 | 99.99% | 178.8 / 337.6 / 374.1 | 75.8 | 44.9 | 0 | 0.00% | 100.0% | -972.9 / -462.1 |
| 46 | 300026 | S3→S1 | 6 | 300 | 800.0 | 800.0 | 7.0 | 37500 | 37498 | 99.99% | 8.5 / 665.5 / 665.9 | 8.9 | 0.4 | 0 | 0.00% | 100.0% | -997.6 / -476.3 |
| 47 | 300028 | S3→S2 | 7 | 100 | 400.0 | 400.0 | 9.9 | 75000 | 74995 | 99.99% | 104.5 / 112.9 / 113.4 | 0.2 | 0.2 | 0 | 0.00% | 100.0% | -978.9 / -407.2 |
| 48 | 300029 | S1→S2 | 6 | 100 | 400.0 | 400.0 | 99.8 | 75000 | 75000 | 100.00% | 234.8 / 266.7 / 298.5 | 31.7 | 63.4 | 0 | 0.00% | 100.0% | -982.4 / -920.4 |
