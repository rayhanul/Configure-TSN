# dataset-testbed-2, run 2026-10-08: SMT + RL, C9 off, on the testbed

Deployed package: `2-rl-c9off-matrix/` (SMT base schedule, RL window enlargement, Problem 3
admission; store-and-forward timing). Testbed run: `2-rl-c9off-matrix/results/results-2026-10-08/`.
Schedules: `RL-TSN/result/result-2026-10-08-dataset-testbed-2/`. Dataset:
`RL-TSN/data/dataset-testbed/2` (seed 7).

## 1. Testbed and measurement

We evaluate on a physical testbed of eight TTTech TSN switches (IEEE 802.1Qbv) and three end
stations at 1 Gb/s. The GCL cycle (hyperperiod) is 800 µs with a 320 ns gate tick. All nodes are
synchronized with gPTP. Each sender's NIC transmits each frame at its scheduled offset in
hardware (SO_TXTIME with ETF offload), and receivers use NIC hardware RX timestamps. Latency is
therefore measured NIC to NIC, with no software time in the path. Each run lasts 30 s, and a
deadline miss is a frame whose latency exceeds its deadline (deadline = period).

## 2. Workload and pipeline

The workload has 20 base flows and 30 arriving flows between the three end stations, with
periods of 200/400/800 µs and frames of 100-500 B. The SMT solver first schedules the base flows
(11/20 admitted). The RL policy then enlarges windows (1M PPO steps), and Problem 3 admits
arriving flows into the existing windows without changing any window boundary (15/39 admitted;
the 39 candidates are the 9 base flows SMT rejected plus the 30 arriving flows). That gives 26
scheduled flows. Schedules are generated with store-and-forward timing and a hardware profile
measured on the switches: a 4 µs per-hop delay and a 12.4 µs gate guard band (every frame
reserves at least 12.48 µs; new windows for empty queues take the network-average size).

## 3. Main result

| Metric | Value |
|---|---|
| Flows deployed | 26 |
| Packets delivered | 1,912,467 / 1,912,500 (100.00%) |
| Flows with zero deadline misses | 25 / 26 |
| Switch queue drops | 0 |
| Measured latency vs. schedule bound | at or below the bound for 24 of 26 flows |

One flow (S2→S1, 200 µs period) missed its deadline on one of its four frames per cycle (25% of
its frames). That instance waits one period for the next window, which points to a model gap
rather than congestion.

### SMT c9-off base schedule

All 11 flows of the SMT c9-off base schedule met every deadline: 0 misses, 99.99-100%
delivered, latency below the schedule bound for 10 of 11 (flow 7: 79.6 µs average vs. a
45.8 µs bound, inside its 400 µs deadline). On paper the schedule also has no violation: every
bound is within its deadline, the solver reports all constraints satisfied, and the pre-deploy
check passes. These numbers come from the same run, where the 11 flows share the network with the
15 flows admitted later. A run of the SMT schedule on its own did not complete (see Notes).

| Flows by origin | Flows | Zero misses |
|---|---|---|
| SMT base schedule | 11 | 11 |
| Problem 3: base flows SMT rejected | 7 | 6 (flow 19: 25%) |
| Problem 3: arriving flows | 8 | 8 |

## 4. Why hardware-accurate timing matters

| Schedule timing model | Workload | Flows admitted | Testbed outcome |
|---|---|---|---|
| Cut-through (C9 on), 2 µs hop, no guard | dataset 1 (original `prob3-rl-c9-on`) | 48 | 75% and 50% misses on two flows; 10 pcp-6 flows lost ~99.6% of frames at one switch (observed, mechanism not identified) |
| Store-and-forward, 4 µs hop, 2.4 µs guard | dataset 2 | 43 | 42/43 flows clean; 1 flow missed 100% (windows of 2.9-4.2 µs too short for the switch) |
| Store-and-forward, 4 µs hop, 12.4 µs guard | dataset 2 | 26 | 25/26 flows clean, 0 drops |

Modeling the switches' real forwarding and gate-closing behavior removes nearly all deadline
misses, at a cost in admission capacity: about 40% fewer flows (43 → 26 on the same workload).
The first row uses a different workload; a cut-through run on dataset 2 is needed for a
same-workload comparison.

## 5. Admission across methods (same run)

| Method | C9 off (store-and-forward) | C9 on (cut-through) |
|---|---|---|
| SMT base | 11/20 | 11/20 |
| Heuristic + Problem 3 | 11/39 | 14/39 |
| RL + Problem 3 | **15/39 (deployed)** | 21/39 |

Pre-deploy check (`deploy-GCL/check_schedule.py`): all pass except heuristic C9-on. Only the
C9-off schedules are valid by construction on these store-and-forward switches.

## 6. Cut-through-planned schedule on the testbed (RL, C9 on)

The RL schedule planned with cut-through timing (C9 on), same dataset and hardware model (4 µs hop, 12.4 µs guard). It admits 21/39 arrivals (32 flows) and passes the pre-deploy check because the 12.48 µs reservations absorb the store-and-forward delay. Results: `2-rl-c9on-matrix/results/results-2026-10-08/`.

| Metric | RL, C9 off (section 3) | RL, C9 on |
|---|---|---|
| Flows deployed | 26 | 32 |
| Packets delivered | 1,912,467 / 1,912,500 (100.00%) | 2,549,636 / 2,549,998 (99.99%) |
| Flows with zero deadline misses | 25 / 26 | 29 / 32 |
| Deadline misses | 37,499 (1.96% of received) | 149,967 (5.88% of received) |
| Routes answering ping | 26 / 26 | 32 / 32 |
| Switch queue drops | 0 | 0 |

Flows with misses:

| id | route | pcp | period (µs) | schedule bound (µs) | latency min / avg / max (µs) | delivered | misses |
|---|---|---|---|---|---|---|---|
| 14 | S3→S2 | 6 | 200 | 29.1 | 69.4 / 145.7 / 222.2 | 99.99% | 50.00% (74,995) |
| 18 | S2→S1 | 6 | 200 | 29.1 | 19.5 / 143.7 / 219.8 | 99.98% | 49.99% (74,971) |
| 9 | S1→S2 | 6 | 200 | 29.8 | 19.0 / 19.8 / 217.8 | 100.00% | 1 frame |

Flows 14 and 18 miss on two of their four frames per cycle: those instances wait about one period
for a later window, while their schedule bound (29.1 µs) was computed for cut-through forwarding.
The pre-deploy check predicted both pass, so the 12.48 µs reservations did not absorb the
store-and-forward delay for these two flows. Flow 9's single late frame is a one-off.

The cut-through-planned schedule admits 6 more flows (32 vs. 26) at the cost of 2 flows missing
half their frames; the C9-off schedule is the one that holds on this store-and-forward hardware.
Every route answered ping here, including the S2→S1 flows that failed in the standalone SMT run.

## Per flow

Latency and bound in µs.

| id | route | pcp | size (B) | period | schedule bound | latency min / avg / max | delivered | misses | admitted by |
|---|---|---|---|---|---|---|---|---|---|
| 1 | S1→S2 | 7 | 500 | 200 | 79.0 | 66.8 / 67.0 / 67.2 | 100.00% | 0.00% | SMT base |
| 2 | S3→S2 | 6 | 100 | 800 | 93.4 | 56.5 / 56.7 / 56.9 | 99.99% | 0.00% | Problem 3 (base flow retried) |
| 3 | S1→S2 | 6 | 500 | 200 | 156.2 | 129.5 / 141.3 / 144.3 | 100.00% | 0.00% | Problem 3 (base flow retried) |
| 4 | S1→S3 | 6 | 400 | 800 | 45.8 | 33.5 / 33.7 / 33.9 | 100.00% | 0.00% | SMT base |
| 6 | S2→S1 | 6 | 100 | 800 | 150.1 | 44.2 / 44.4 / 44.6 | 100.00% | 0.00% | Problem 3 (base flow retried) |
| 7 | S3→S1 | 6 | 300 | 400 | 45.8 | 79.2 / 79.6 / 80.1 | 99.99% | 0.00% | SMT base |
| 8 | S1→S2 | 6 | 500 | 800 | 144.0 | 123.1 / 123.3 / 123.5 | 100.00% | 0.00% | Problem 3 (base flow retried) |
| 9 | S1→S2 | 7 | 400 | 200 | 79.7 | 46.0 / 46.2 / 46.4 | 100.00% | 0.00% | SMT base |
| 10 | S3→S2 | 6 | 300 | 800 | 79.0 | 66.8 / 67.0 / 67.2 | 99.99% | 0.00% | SMT base |
| 11 | S2→S3 | 7 | 300 | 400 | 83.5 | 43.8 / 44.4 / 45.0 | 100.00% | 0.00% | SMT base |
| 12 | S2→S1 | 6 | 200 | 800 | 79.0 | 55.2 / 55.5 / 55.7 | 100.00% | 0.00% | SMT base |
| 13 | S3→S1 | 7 | 100 | 400 | 137.9 | 33.8 / 34.0 / 34.2 | 99.99% | 0.00% | Problem 3 (base flow retried) |
| 14 | S3→S2 | 6 | 500 | 200 | 91.8 | 79.6 / 79.8 / 80.0 | 99.99% | 0.00% | SMT base |
| 15 | S2→S3 | 6 | 400 | 400 | 84.8 | 72.5 / 74.0 / 75.5 | 100.00% | 0.00% | Problem 3 (base flow retried) |
| 16 | S2→S1 | 7 | 100 | 400 | 79.0 | 66.8 / 67.0 / 67.2 | 100.00% | 0.00% | SMT base |
| 18 | S2→S1 | 7 | 400 | 200 | 83.5 | 59.2 / 66.0 / 72.6 | 100.00% | 0.00% | SMT base |
| 19 | S2→S1 | 6 | 100 | 200 | 84.2 | 13.1 / 95.7 / 213.4 | 100.00% | 25.00% | Problem 3 (base flow retried) |
| 20 | S3→S2 | 7 | 300 | 400 | 79.0 | 42.4 / 42.6 / 42.8 | 99.99% | 0.00% | SMT base |
| 21 | S1→S2 | 6 | 400 | 800 | 94.7 | 65.2 / 65.4 / 65.6 | 100.00% | 0.00% | Problem 3 (arrival) |
| 22 | S2→S3 | 6 | 100 | 800 | 79.0 | 13.2 / 13.4 / 13.6 | 100.00% | 0.00% | Problem 3 (arrival) |
| 28 | S1→S2 | 6 | 200 | 800 | 96.3 | 55.7 / 55.9 / 56.1 | 100.00% | 0.00% | Problem 3 (arrival) |
| 37 | S2→S3 | 7 | 100 | 800 | 400.0 | 306.8 / 307.0 / 307.2 | 100.00% | 0.00% | Problem 3 (arrival) |
| 40 | S2→S1 | 6 | 100 | 800 | 82.2 | 11.3 / 13.0 / 13.6 | 100.00% | 0.00% | Problem 3 (arrival) |
| 41 | S1→S2 | 7 | 500 | 800 | 163.5 | 30.3 / 32.7 / 32.9 | 100.00% | 0.00% | Problem 3 (arrival) |
| 49 | S2→S1 | 6 | 200 | 400 | 79.7 | 41.8 / 42.0 / 42.2 | 100.00% | 0.00% | Problem 3 (arrival) |
| 50 | S1→S3 | 6 | 300 | 800 | 85.1 | 60.1 / 60.3 / 60.5 | 100.00% | 0.00% | Problem 3 (arrival) |

## Notes

- **Flow 19:** two of its four frames per cycle have dedicated 12.48 µs windows, the other two
  share long windows with ample slack; the pre-deploy check predicts it passes. Which frame misses,
  and why, needs per-frame latencies.
- **SMT schedule on its own:** deploying `2-t3600-c9off-minlat/` alone stopped at flow 8 of 11
  during flow admission. The CNC (S2) runs a `tsn-tag` service (since 2026-09-14) that tags its
  ARP frames VLAN 1 / priority 6, so ARP travels in TT queue 6. The SMT base schedule has no
  queue-6 window on many ports (the enlarged schedules do), so the CNC lost ARP to seven
  switches. A standalone SMT run needs that ARP tagging removed first.
- Host drops in the run: S3 30 launch-time (ETF) drops, S1 1, S2 3.
