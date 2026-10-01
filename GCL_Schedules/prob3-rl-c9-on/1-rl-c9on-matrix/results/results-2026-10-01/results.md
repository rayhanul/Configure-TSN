# Traffic run: prob3-rl-c9-on/1-rl-c9on-matrix, 2026-10-01 14:10

48 flows, 30 s, S1/S2/S3 concurrently, all senders starting at the same TAI instant on the GCL grid (`basetime.json`). Raw output: `results_<node>.log`.

## Summary

- Delivered: **3351317 / 4009693 packets (83.58%)**
- Deadline misses: **2047936 (61.11% of received)**; flows with zero misses: 0 / 48

| receiving node | flows | delivered | avg latency (µs) | deadline misses |
|---|---|---|---|---|
| S1 | 16 | 99.91% | 444.9 | 51.58% |
| S2 | 21 | 69.78% | 15995.5 | 89.98% |
| S3 | 11 | 100.00% | 231.6 | 4.74% |

Setup at start:

- S1: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[6399248.915] port 1 (enp1s0): assuming the grand master role`
- S2: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[6403673.243] rms    7 max   15 freq  -5322 +/-  10 delay    20 +/-   0`
- S3: ptp4l/phc2sys active/active, CLOCK_TAI − UTC 37.0 s, ptp4l `[95972.431] rms   26 max   66 freq  +3688 +/-  36 delay    52 +/-   0`
- Connectivity: 48 / 48 sender routes answered ping

## Observations

- **S1 and S3 receive essentially everything** (99.91% / 100.00%). Their deadline misses grow as
  the period shrinks: 2–28% for 800 µs flows, 8–64% for 400 µs, 55–98% for 200 µs. Average latency
  is a few hundred µs, which is the Python send/receive overhead, not the network.
- **S2 is the bottleneck, and the cause is on the receiving side.** All ten 200 µs flows received on
  S2 deliver the same ~56% with ~27 ms average latency, whether they come from S1 or S3, over
  different routes, with sizes from 100 to 500 B. The other 400/800 µs flows on S2 arrive at
  99.7–100% but with ~1–3 ms latency. S2 runs 21 receiver threads (10 of them at 5,000 packets/s) on
  3 CPUs in one Python process. The threads can't drain their sockets fast enough, so packets
  queue (latency) and then overflow the socket buffers (loss). This matches the 2026-09-30 run,
  which had the same ~56% / ~27 ms on the same flows.
- Compared with 2026-09-30 (82.9% delivered), this run delivers 83.58%. Aligning sends to the GCL
  grid and sizing frames to the schedule did not change the overall picture, because Python's
  timing jitter (tens to hundreds of µs) still dominates the µs-wide gate windows.

## Why these results don't show TSN's guarantees yet

TSN bounds latency, jitter and loss from switch port to switch port, for frames that arrive inside
their scheduled gate window. This measurement also includes two parts TSN does not control:

1. **The sender** is a Python sleep loop. It releases frames tens to hundreds of µs off their
   window, while the windows are a few µs wide. A late frame waits for the next cycle (latency,
   deadline misses), and a burst can overflow a switch queue.
2. **The receiver** is Python threads. They timestamp late and lose packets when their socket
   buffers fill.

Evidence, read after this run:

| counter | value | meaning |
|---|---|---|
| S2 `UdpRcvbufErrors` (since boot) | 1,306,180 | ≈ S2's losses in the 2026-09-30 and 2026-10-01 runs combined: dropped in S2's own socket buffers, after the network delivered them |
| sw02 port p2 (to S1) `Q DROP` | 10,739 | a small real network loss, consistent with S1's 0.09% |

So most of the loss, latency and jitter in the table is the end hosts, not the network.

**What to change, in order:**

1. **Measure at the NIC**: hardware TX/RX timestamps (`SO_TIMESTAMPING`), so latency is
   NIC-to-NIC on PTP-synced clocks (±100 ns) and excludes Python.
2. **Stop receiver loss**: larger socket buffers (`net.core.rmem_max`, `SO_RCVBUF`; now 208 KiB),
   and one `epoll` loop or raw capture per node instead of a thread per flow. Check that
   `nstat UdpRcvbufErrors` does not grow during a run.
3. **Release frames on schedule**: `SO_TXTIME` + `etf` qdisc with `offload` on the I210 (launch
   time on queues 0/1: pcp 7 → queue 0, pcp 6 → queue 1). The NIC sends at `basetime + psi_ns`
   to within tens of ns.
4. **Then check the network**: switch `Q DROP` counters (`ethtool -S sw0pX`) before/after each
   run, the 249 ns grid offset on 11 of 27 switch ports, and the schedule's `proc_delay_ns` 2000 /
   `prop_delay_ns` 0 against measured per-hop delay.
5. **Host tuning** if still needed: dedicated CPU, `SCHED_FIFO`, CPU power-saving states off.

After 1–3, flows should show no loss and latency near the schedule's `e2e_ns` (e.g. flow 1:
8.6 µs) with sub-µs jitter; anything else points at a specific switch or schedule issue.

## Per flow

Latency = receive time − send timestamp, both taken in Python on PTP-synced system clocks. Jitter: standard deviation of latency, and RFC 3550 (mean |Δ latency| between consecutive packets). Deadline miss = latency > deadline.

| # | id | route | pcp | size (B) | period (µs) | deadline (µs) | sent | received | received % | latency min / avg / max (µs) | jitter stddev (µs) | jitter RFC 3550 (µs) | deadline misses | miss % |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S3→S1 | 7 | 500 | 200.0 | 200.0 | 150000 | 149872 | 99.91% | 41.5 / 400.0 / 34553.4 | 1163.7 | 115.4 | 91561 | 61.09% |
| 2 | 2 | S2→S1 | 6 | 400 | 200.0 | 200.0 | 111536 | 111215 | 99.71% | 57.0 / 695.7 / 10548.2 | 429.2 | 173.2 | 109051 | 98.05% |
| 3 | 3 | S3→S2 | 7 | 100 | 200.0 | 200.0 | 150000 | 85123 | 56.75% | 93.0 / 26600.5 / 88143.3 | 4540.1 | 405.9 | 85120 | 100.00% |
| 4 | 4 | S1→S3 | 6 | 300 | 800.0 | 800.0 | 37500 | 37500 | 100.00% | 51.8 / 307.8 / 2298.8 | 181.7 | 158.7 | 2556 | 6.82% |
| 5 | 5 | S2→S1 | 6 | 200 | 400.0 | 400.0 | 75000 | 74972 | 99.96% | 49.2 / 507.8 / 7416.0 | 286.8 | 189.0 | 47270 | 63.05% |
| 6 | 6 | S2→S1 | 7 | 100 | 400.0 | 400.0 | 75001 | 74982 | 99.97% | 44.4 / 463.6 / 7502.0 | 275.2 | 170.0 | 42973 | 57.31% |
| 7 | 7 | S2→S1 | 6 | 300 | 800.0 | 800.0 | 37499 | 37499 | 100.00% | 53.9 / 456.2 / 4274.2 | 228.6 | 226.2 | 2736 | 7.30% |
| 8 | 8 | S2→S3 | 7 | 100 | 800.0 | 800.0 | 37501 | 37501 | 100.00% | 35.5 / 153.0 / 1588.3 | 91.9 | 96.0 | 4 | 0.01% |
| 9 | 9 | S3→S2 | 7 | 500 | 200.0 | 200.0 | 150000 | 84519 | 56.35% | 204.0 / 26873.8 / 75297.0 | 4387.4 | 410.3 | 84519 | 100.00% |
| 10 | 10 | S1→S3 | 7 | 100 | 800.0 | 800.0 | 37501 | 37501 | 100.00% | 30.1 / 208.4 / 970.6 | 107.7 | 121.2 | 3 | 0.01% |
| 11 | 11 | S3→S2 | 6 | 500 | 800.0 | 800.0 | 37500 | 37500 | 100.00% | 72.7 / 859.1 / 37364.3 | 1595.4 | 413.6 | 12856 | 34.28% |
| 12 | 12 | S2→S1 | 7 | 100 | 800.0 | 800.0 | 37500 | 37500 | 100.00% | 43.6 / 403.4 / 3680.1 | 175.7 | 168.3 | 848 | 2.26% |
| 13 | 13 | S1→S2 | 7 | 300 | 400.0 | 400.0 | 75000 | 74808 | 99.74% | 50.6 / 2732.5 / 57775.1 | 4236.3 | 319.6 | 66562 | 88.98% |
| 14 | 14 | S1→S2 | 7 | 100 | 200.0 | 200.0 | 150001 | 84128 | 56.08% | 204.6 / 26919.1 / 90628.8 | 4460.1 | 433.0 | 84128 | 100.00% |
| 15 | 15 | S2→S3 | 7 | 400 | 400.0 | 400.0 | 75001 | 74991 | 99.99% | 51.2 / 177.1 / 2222.3 | 105.5 | 106.9 | 3050 | 4.07% |
| 16 | 16 | S3→S2 | 7 | 200 | 200.0 | 200.0 | 150000 | 84222 | 56.15% | 114.9 / 26938.0 / 63890.4 | 4298.4 | 414.0 | 84218 | 100.00% |
| 17 | 17 | S2→S3 | 6 | 200 | 800.0 | 800.0 | 37501 | 37501 | 100.00% | 43.6 / 142.1 / 1404.1 | 92.6 | 84.6 | 5 | 0.01% |
| 18 | 18 | S3→S2 | 6 | 100 | 400.0 | 400.0 | 75000 | 74781 | 99.71% | 53.4 / 3000.4 / 58683.1 | 4817.4 | 308.4 | 67356 | 90.07% |
| 19 | 19 | S3→S1 | 7 | 500 | 400.0 | 400.0 | 75000 | 75000 | 100.00% | 42.5 / 285.2 / 24537.8 | 847.0 | 137.0 | 8168 | 10.89% |
| 20 | 20 | S3→S1 | 7 | 200 | 200.0 | 200.0 | 150000 | 149885 | 99.92% | 29.6 / 353.0 / 37250.1 | 1079.1 | 113.0 | 82523 | 55.06% |
| 21 | 300000 | S3→S2 | 7 | 500 | 200.0 | 200.0 | 150000 | 84024 | 56.02% | 116.6 / 27003.8 / 77526.6 | 4502.1 | 409.7 | 84022 | 100.00% |
| 22 | 300001 | S2→S3 | 7 | 300 | 400.0 | 400.0 | 74997 | 74997 | 100.00% | 45.7 / 155.5 / 4440.8 | 95.2 | 96.0 | 858 | 1.14% |
| 23 | 300002 | S1→S2 | 7 | 500 | 200.0 | 200.0 | 150001 | 84791 | 56.53% | 117.8 / 26720.0 / 59322.1 | 4194.5 | 427.2 | 84786 | 99.99% |
| 24 | 300003 | S2→S1 | 7 | 100 | 200.0 | 200.0 | 110648 | 110403 | 99.78% | 42.9 / 542.0 / 9036.1 | 321.9 | 156.0 | 103942 | 94.15% |
| 25 | 300004 | S1→S2 | 6 | 200 | 800.0 | 800.0 | 37501 | 37501 | 100.00% | 119.4 / 920.8 / 30091.1 | 1360.6 | 413.1 | 14803 | 39.47% |
| 26 | 300005 | S3→S2 | 7 | 500 | 400.0 | 400.0 | 75000 | 74811 | 99.75% | 58.2 / 2794.2 / 65737.8 | 4435.5 | 309.9 | 66817 | 89.31% |
| 27 | 300006 | S1→S3 | 6 | 400 | 800.0 | 800.0 | 37501 | 37501 | 100.00% | 76.7 / 631.9 / 1555.5 | 111.4 | 120.6 | 865 | 2.31% |
| 28 | 300007 | S3→S2 | 7 | 500 | 200.0 | 200.0 | 150001 | 84410 | 56.27% | 186.1 / 26887.0 / 82417.5 | 4543.7 | 409.1 | 84409 | 100.00% |
| 29 | 300008 | S2→S1 | 6 | 100 | 400.0 | 400.0 | 75001 | 74905 | 99.87% | 46.0 / 514.1 / 12401.0 | 353.7 | 186.8 | 47798 | 63.81% |
| 30 | 300009 | S3→S2 | 7 | 300 | 400.0 | 400.0 | 75000 | 74794 | 99.73% | 46.9 / 2939.1 / 54235.5 | 4782.6 | 309.0 | 66301 | 88.64% |
| 31 | 300011 | S1→S3 | 7 | 100 | 400.0 | 400.0 | 75000 | 75000 | 100.00% | 28.6 / 147.7 / 1209.0 | 99.9 | 131.5 | 750 | 1.00% |
| 32 | 300012 | S3→S2 | 7 | 500 | 200.0 | 200.0 | 150000 | 84860 | 56.57% | 144.5 / 26714.5 / 68432.2 | 4396.8 | 407.7 | 84854 | 99.99% |
| 33 | 300013 | S1→S2 | 7 | 300 | 200.0 | 200.0 | 150001 | 84047 | 56.03% | 96.1 / 26974.2 / 72565.4 | 4496.9 | 433.2 | 84044 | 100.00% |
| 34 | 300014 | S3→S1 | 7 | 200 | 400.0 | 400.0 | 75000 | 75000 | 100.00% | 30.8 / 232.1 / 27673.2 | 1004.2 | 118.3 | 5676 | 7.57% |
| 35 | 300015 | S2→S1 | 7 | 500 | 800.0 | 800.0 | 37500 | 37500 | 100.00% | 64.1 / 404.7 / 3601.9 | 184.0 | 181.1 | 1068 | 2.85% |
| 36 | 300016 | S3→S1 | 6 | 500 | 800.0 | 800.0 | 37500 | 37499 | 100.00% | 44.5 / 384.5 / 5188.0 | 264.8 | 257.4 | 2895 | 7.72% |
| 37 | 300017 | S2→S3 | 7 | 100 | 800.0 | 800.0 | 37500 | 37500 | 100.00% | 37.6 / 172.2 / 980.2 | 86.7 | 93.5 | 2 | 0.01% |
| 38 | 300018 | S1→S3 | 6 | 300 | 800.0 | 800.0 | 37499 | 37499 | 100.00% | 47.3 / 554.5 / 1397.2 | 337.1 | 358.4 | 16740 | 44.64% |
| 39 | 300019 | S1→S2 | 6 | 200 | 800.0 | 800.0 | 37500 | 37500 | 100.00% | 98.7 / 903.5 / 37865.7 | 1601.6 | 413.6 | 14145 | 37.72% |
| 40 | 300020 | S3→S1 | 7 | 100 | 200.0 | 200.0 | 150000 | 149864 | 99.91% | 27.1 / 344.9 / 41190.6 | 1073.9 | 119.5 | 88749 | 59.22% |
| 41 | 300021 | S3→S2 | 7 | 100 | 400.0 | 400.0 | 75000 | 74767 | 99.69% | 36.8 / 2614.5 / 65128.6 | 4601.1 | 308.3 | 64717 | 86.56% |
| 42 | 300022 | S3→S1 | 6 | 200 | 800.0 | 800.0 | 37500 | 37496 | 99.99% | 101.4 / 684.5 / 7755.7 | 309.1 | 238.3 | 9981 | 26.62% |
| 43 | 300023 | S3→S2 | 7 | 500 | 200.0 | 200.0 | 150000 | 83992 | 55.99% | 96.4 / 27010.0 / 80052.3 | 4504.8 | 412.1 | 83990 | 100.00% |
| 44 | 300024 | S1→S3 | 7 | 500 | 400.0 | 400.0 | 75001 | 75001 | 100.00% | 42.2 / 171.7 / 1204.4 | 107.6 | 148.2 | 1803 | 2.40% |
| 45 | 300025 | S3→S2 | 6 | 200 | 800.0 | 800.0 | 37500 | 37500 | 100.00% | 47.0 / 885.4 / 39734.6 | 1842.4 | 410.1 | 12652 | 33.74% |
| 46 | 300026 | S3→S1 | 6 | 300 | 800.0 | 800.0 | 37500 | 37496 | 99.99% | 138.5 / 695.0 / 4576.9 | 222.5 | 226.5 | 10382 | 27.69% |
| 47 | 300028 | S3→S2 | 7 | 100 | 400.0 | 400.0 | 75000 | 74846 | 99.79% | 42.8 / 2634.2 / 69181.6 | 4328.6 | 307.2 | 65592 | 87.64% |
| 48 | 300029 | S1→S2 | 6 | 100 | 400.0 | 400.0 | 75001 | 74813 | 99.75% | 98.3 / 2899.8 / 52732.8 | 4553.2 | 319.9 | 69788 | 93.28% |
