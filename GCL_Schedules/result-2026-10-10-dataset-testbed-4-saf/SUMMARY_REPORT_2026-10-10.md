# Summary report: dataset-testbed 4 on the physical testbed (2026-10-10)

All 10 schedule packages of dataset-testbed 4 (SMT, heuristic, RL and Problem 3 heuristic/RL, each
with C9 off and C9 on) were deployed and measured on the 8-switch loop-free testbed
(`network-topology/network-topology-rtas-2027-tree.json`). The runs went in rounds: first as
generated, then after each fix of a cause of misses or loss (A–D below).

Where the packages are:
- **C9-off packages:** `../result-2026-10-09-dataset-testbed-4-avgwin/<group>/<package>`, unchanged from generation.
- **C9-on packages:** regenerated with fix B, in this folder. The original C9-on packages remain in the avgwin folder.

Per-package tables:
- [TESTBED_RESULTS_2026-10-10.md](TESTBED_RESULTS_2026-10-10.md): final C9-on runs.
- [../result-2026-10-09-dataset-testbed-4-avgwin/TESTBED_RESULTS_2026-10-10.md](../result-2026-10-09-dataset-testbed-4-avgwin/TESTBED_RESULTS_2026-10-10.md): the first round, plus the final C9-off runs.

Per-flow reports: `<package>/results/results-<date>[_n]/results.md`.

## Bottom line

- **All 10 packages: 100.00% delivered and 0 deadline misses** in the final round.
- **Totals:** 13,649,550 frames sent, 34 lost (at most 9 in any package), 0 switch queue drops.
- **Before the fixes:** 9 of 10 packages missed deadlines (up to 74,994 per 30 s run), and two lost 0.5–0.75% of their frames.
- **Four causes were found and fixed**, two in the testbed's end-station and test setup (A, C), one in schedule generation (B), and one in how the tests were run (D).
- **No known cause of deadline misses remains.**

## Results

Deadline = period, 30 s of traffic per package, deadline misses counted on received frames. "Lost"
= sent but not received. "Before the fixes" is round 1: each package as generated, run before any of
fixes A-D (its first run, `results-2026-10-10`, in `../result-2026-10-09-dataset-testbed-4-avgwin/`).
"After the fixes" is each package's latest run with all fixes in place: C9-off packages in the avgwin
folder, the regenerated C9-on packages in this folder.

### After the fixes (final round)

Rows in pipeline order, each approach C9 off then on. **Rank** orders the packages by deadline misses, then frames lost, then max latency (1 = best). **Flows** = admitted / offered: every flow of the dataset's base flow set for SMT, heuristic and RL; the base schedule's flows plus the arriving candidates for Problem 3. **Lost** = sent − received. **Deadline misses** = received frames whose latency exceeded their flow's deadline (deadline = period), with their share of received frames. **Latency** = receiver NIC's RX timestamp − sender NIC's launch time over all received frames (min / frame-weighted avg / max). **Jitter** = per-flow standard deviation of latency: best flow / average over the package's flows / worst flow.

| Rank | Package | Flows (admitted / offered) | Sent | Received | Lost | Deadline misses (%) | Latency min / avg / max (µs) | Jitter stddev best / avg / worst flow (µs) |
|---|---|---|---|---|---|---|---|---|
| 2 | SMT C9-off | 11 / 20 | 1,012,445 | 1,012,445 | 0 | 0 (0.00%) | 66.8 / 90.0 / 133.7 | 0.1 / 0.1 / 0.1 |
| 6 | SMT C9-on | 11 / 20 | 1,012,484 | 1,012,480 | 4 | 0 (0.00%) | 21.0 / 39.1 / 62.1 | 0.1 / 0.1 / 0.2 |
| 10 | heuristic C9-off | 11 / 20 | 1,012,482 | 1,012,473 | 9 | 0 (0.00%) | 19.0 / 73.7 / 134.0 | 0.1 / 0.6 / 5.7 |
| 8 | heuristic C9-on | 11 / 20 | 1,012,448 | 1,012,440 | 8 | 0 (0.00%) | 21.3 / 34.7 / 156.6 | 0.1 / 0.2 / 0.5 |
| 2 | RL C9-off | 11 / 20 | 1,012,488 | 1,012,488 | 0 | 0 (0.00%) | 19.1 / 72.0 / 133.7 | 0.1 / 1.8 / 18.7 |
| 1 | RL C9-on | 11 / 20 | 1,012,483 | 1,012,483 | 0 | 0 (0.00%) | 21.0 / 33.6 / 44.5 | 0.1 / 0.1 / 0.3 |
| 9 | Problem 3 heuristic C9-off | 24 / 50 | 1,612,431 | 1,612,423 | 8 | 0 (0.00%) | 12.8 / 82.4 / 420.7 | 0.1 / 2.5 / 49.9 |
| 7 | Problem 3 heuristic C9-on | 27 / 50 | 1,912,365 | 1,912,361 | 4 | 0 (0.00%) | 9.6 / 38.6 / 408.2 | 0.1 / 0.6 / 4.8 |
| 4 | Problem 3 RL C9-off | 28 / 50 | 2,024,967 | 2,024,967 | 0 | 0 (0.00%) | 9.7 / 67.4 / 235.5 | 0.1 / 2.6 / 25.0 |
| 5 | Problem 3 RL C9-on | 29 / 50 | 2,024,957 | 2,024,956 | 1 | 0 (0.00%) | 9.7 / 36.9 / 139.8 | 0.1 / 2.2 / 49.5 |
| | **Total** | | **13,649,550** | **13,649,516** | **34** | **0 (0.00%)** | | |

#### Details

**Received %** shows a lost frame even when it rounds to 100%. **No NIC ts** = received frames without a hardware timestamp (left out of latency). **Jitter RFC 3550** = mean |Δ latency| between consecutive frames, best flow / average / worst flow. **Worst latency, % of deadline** = the largest max latency / deadline over the package's flows. **Above e2e bound** = flows whose max latency exceeded the scheduler's own end-to-end bound.

| Package | Received % | No NIC ts | Jitter RFC 3550 best / avg / worst flow (µs) | Worst latency, % of deadline | Above e2e bound | Routes ping OK | Switch queue drops | Run (`results.md` inside) |
|---|---|---|---|---|---|---|---|---|
| SMT C9-off | 100.0000% | 0 | 0.0 / 0.0 / 0.1 | 67% | 1 | 11/11 | none | `../result-2026-10-09-dataset-testbed-4-avgwin/smt-c9-off/4-t3600-c9off-minlat/results/results-2026-10-10_5` |
| SMT C9-on | 99.9996% | 0 | 0.0 / 0.0 / 0.0 | 24% | 1 | 11/11 | none | `smt-c9-on/4-saf-retimed-c9on/results/results-2026-10-10_3` |
| heuristic C9-off | 99.9991% | 0 | 0.0 / 0.6 / 6.6 | 67% | 0 | 11/11 | none | `../result-2026-10-09-dataset-testbed-4-avgwin/heuristic-c9-off/4-matrix-c9off/results/results-2026-10-10_3` |
| heuristic C9-on | 99.9992% | 0 | 0.0 / 0.1 / 0.2 | 39% | 1 | 11/11 | none | `heuristic-c9-on/4-matrix-c9on/results/results-2026-10-10_2` |
| RL C9-off | 100.0000% | 0 | 0.0 / 3.5 / 37.4 | 67% | 0 | 11/11 | none | `../result-2026-10-09-dataset-testbed-4-avgwin/rl-c9-off/4-matrix-c9off/results/results-2026-10-10_3` |
| RL C9-on | 100.0000% | 0 | 0.0 / 0.1 / 0.2 | 21% | 0 | 11/11 | none | `rl-c9-on/4-matrix-c9on/results/results-2026-10-10_2` |
| Problem 3 heuristic C9-off | 99.9995% | 0 | 0.0 / 4.6 / 99.8 | 75% | 0 | 24/24 | none | `../result-2026-10-09-dataset-testbed-4-avgwin/prob3-heuristic-c9-off/4-heuristic-c9off-matrix/results/results-2026-10-10_3` |
| Problem 3 heuristic C9-on | 99.9998% | 0 | 0.0 / 0.8 / 7.3 | 51% | 0 | 27/27 | none | `prob3-heuristic-c9-on/4-heuristic-c9on-matrix/results/results-2026-10-10_2` |
| Problem 3 RL C9-off | 100.0000% | 0 | 0.0 / 4.8 / 50.0 | 67% | 0 | 28/28 | none | `../result-2026-10-09-dataset-testbed-4-avgwin/prob3-rl-c9-off/4-rl-c9off-matrix/results/results-2026-10-10_4` |
| Problem 3 RL C9-on | 99.99995% | 0 | 0.0 / 3.9 / 98.9 | 35% | 0 | 29/29 | none | `prob3-rl-c9-on/4-rl-c9on-matrix/results/results-2026-10-10_2` |

### Before the fixes (round 1)

| Rank | Package | Flows (admitted / offered) | Sent | Received | Lost | Deadline misses (%) | Latency min / avg / max (µs) | Jitter stddev best / avg / worst flow (µs) |
|---|---|---|---|---|---|---|---|---|
| 9 | SMT C9-off | 11 / 20 | 1,012,500 | 1,012,479 | 21 | 74,994 (7.41%) | 67.0 / 111.7 / 273.3 | 0.1 / 12.3 / 94.5 |
| 3 | SMT C9-on | 11 / 20 | 1,012,500 | 1,012,472 | 28 | 12,320 (1.22%) | 17.1 / 51.0 / 1198.1 | 0.1 / 15.1 / 138.6 |
| 8 | heuristic C9-off | 11 / 20 | 1,012,482 | 1,012,436 | 46 | 74,983 (7.41%) | 19.0 / 93.8 / 224.4 | 0.1 / 12.9 / 97.4 |
| 2 | heuristic C9-on | 11 / 20 | 1,012,500 | 1,012,475 | 25 | 1 (0.00%) | 15.8 / 32.4 / 428.0 | 0.1 / 2.9 / 18.0 |
| 1 | RL C9-off | 11 / 20 | 1,012,493 | 1,012,444 | 49 | 0 (0.00%) | 19.0 / 81.7 / 133.8 | 0.1 / 7.8 / 46.2 |
| 5 | RL C9-on | 11 / 20 | 1,012,500 | 1,012,477 | 23 | 27,392 (2.71%) | 16.9 / 56.2 / 422.1 | 0.1 / 17.3 / 176.1 |
| 10 | Problem 3 heuristic C9-off | 24 / 50 | 1,612,418 | 1,612,301 | 117 | 74,994 (4.65%) | 12.8 / 94.7 / 420.6 | 0.1 / 8.1 / 97.3 |
| 6 | Problem 3 heuristic C9-on | 29 / 50 | 2,137,495 | 2,137,174 | 321 | 37,499 (1.75%) | 9.7 / 49.7 / 568.3 | 0.1 / 9.9 / 197.7 |
| 7 | Problem 3 RL C9-off | 28 / 50 | 2,025,000 | 2,009,876 | 15,124 | 74,364 (3.70%) | 9.6 / 107.0 / 320964.9 | 0.2 / 1960.5 / 4668.9 |
| 4 | Problem 3 RL C9-on | 28 / 50 | 2,062,500 | 2,052,201 | 10,299 | 27,316 (1.33%) | 9.7 / 67.0 / 324839.5 | 0.1 / 2375.7 / 6468.4 |
| | **Total** | | **13,912,388** | **13,886,335** | **26,053** | **403,863 (2.91%)** | | |

The flow counts of the two Problem 3 C9-on packages changed (29 → 27 and 28 → 29) because they were
regenerated with fix B: Problem 3 admits a different set of extra flows when the C9-on spacing changes.

### How each fix changed the results

| round | fixes in place | C9-off packages | C9-on packages |
|---|---|---|---|
| 1. before the fixes (as generated) | none | 74,364–74,994 misses in 4 of 5 (RL: 0); Problem 3 RL lost 15,124 | 1–37,499 misses in all 5; Problem 3 RL lost 10,299 |
| 2. | A | 0 misses in 4 of 5; RL C9-off: 160 misses, 9,110 lost (D); 57–69 lost per Problem 3 package (C) | not run (round 3 regenerated them) |
| 3. | A + B (etf delta 300 µs) | – | 0 misses in 4 of 5, SMT C9-on 1; 22–64 lost (C) |
| 4. | A + B + C (etf delta 600 µs) | 0 misses, 0–9 lost in all 5 | 0 misses, 0–8 lost in 4 of 5; SMT C9-on: 314 misses, 10,600 lost (D) |
| 5. final | A + B + C + D | (= round 4) | SMT C9-on rerun: 0 misses, 4 lost |

## Causes found and fixed

| | cause | symptom | fix | where |
|---|---|---|---|---|
| **A** | The end stations' I210 NIC serves its two launch-time queues in strict priority. A pcp-6 frame (queue 1) waits behind a pcp-7 frame in queue 0 with a slightly later launch time. | Every frame of one pcp-6 flow left late and missed its window by one cycle: ~75,000 misses in each C9-off package (flow 14). | Socket priorities 5 and 7 both go to TX queue 0 (one etf qdisc), so frames leave in launch-time order. | `time-sync-gptp/gptp.sh` (`apply_launchtime`), README |
| **B** | C9-on windows were spaced by Γ = proc + prop per hop only, which assumes cut-through. The TTTech switches are store-and-forward, so each hop also needs the frame's own transmission time. | Delay built up along the path: 12,000–37,000 misses per C9-on package, typically every other frame of one flow. | New hardware flag `store_and_forward` (on in `hw/tttech-sw0p3.json` and the testbed datasets). With it, C9-on spaces hops by Γ + the frame's transmission time (500 B: 8,260 ns instead of 4,100). The SMT solver, heuristic, RL env, Problem 3 admit and verifier all use `HardwareConfig.c9_wait_ns()`. Simulation profiles are unchanged. The C9-on packages were regenerated. | RL-TSN `*/config.py`, `smt_sched`, `prob_2_*`, `prob_3_admit`, `tsn_sched`, `verifier/core.py` |
| **C** | Frames reached the sending host's etf qdisc less than its 300 µs delta before launch time and were dropped. | 20–70 lost frames per run, mostly on S3. | etf delta 600 µs (the value must match in both files). | `gptp.sh` and `Spawning-Flows/gen_traffic.py` (`ETF_DELTA_NS`) |
| **D** | Admitting flows changes MSTP on every switch, and mstpd then re-converges for up to ~25 s. Meanwhile sw08 put all its ports into blocking every ~4.5 s, for ~280 ms each time on its switch-to-switch ports, and the sw04↔sw06 link did the same. In two runs, traffic started before this ended: the last block came 1.7 s and 2 s into the run (switch kernel logs). | ~315 ms of every flow lost (~1%), the rest held up to 322 ms; queue drops on port 4 of sw05–sw08. Seen in RL C9-off (round 2) and SMT C9-on (round 4). | `wait_stp_quiet.py` waits until no switch has had a port state change or topology change for 15 s. `run_testbed.sh` runs it between admit and traffic. | `Network-Configure-Manager/wait_stp_quiet.py`, `GCL_Schedules/run_testbed.sh` |

Ruled out on the way:
- **Clock steps (for D):** S2's gPTP offset stayed below 80 ns through the stall. The grandmaster's clock runs free, and NTP is off on all hosts.
- **Ethernet PAUSE (for D):** the switches do not support it, and the hosts' pause counters are 0.

## Remaining loss and open points

- **34 lost frames in 13.6 million (final round).** These are etf launch-time drops on the sending hosts: the hosts' etf counters show 44 drops, which also include stray packets (F). The switches dropped nothing.
- **E. Frames skipped by the sender:** 450 in the final round (12–135 per package).
  - What happens: `gen_traffic.py` does not send a frame when it wakes up later than etf delta + 50 µs before the frame's launch time.
  - Why: Python wake-up jitter on the hosts.
  - These frames are not counted as sent or lost.
  - Likely fix: raise `--lead-us` from 1000 µs; it is now only 350 µs above the 650 µs cut-off.
- **F. Stray etf drops:** the etf qdiscs count 30–46 drops per host even with no test traffic. These are likely kernel control packets sent at priority 7 without a launch time (e.g. IPv6 neighbour discovery); this is not confirmed. They do not affect the flows but inflate the counter, so judge losses by the frame logs.

## Method and reproduction

For each package:
1. Push and activate the GCLs on all 17 gated switch ports.
2. Tear down the previous package, then admit the scheduled flows (VLANs, addresses, MSTP). All switches must share one MST region.
3. Remove stale VLAN interfaces on S1/S2/S3.
4. Wait for 15 s without any spanning-tree change (fix D, from round 5).
5. Ping every route.
6. Send 30 s of traffic from S1, S2 and S3 at once.

Each frame is sent at its scheduled time with NIC launch time (`SO_TXTIME` + etf offload). Latency = the receiver's hardware RX timestamp − the launch time, both on gPTP-synced NIC clocks.

Reproduce the final round:
```bash
cd Configure-TSN/GCL_Schedules
S3_PW=... S1_PW=... ./run_testbed.sh result-2026-10-09-dataset-testbed-4-avgwin \
    smt-c9-off heuristic-c9-off rl-c9-off prob3-heuristic-c9-off prob3-rl-c9-off
S3_PW=... S1_PW=... ./run_testbed.sh result-2026-10-10-dataset-testbed-4-saf
```
Before the first run, start gPTP with launch time on, on every end station (`time-sync-gptp/gptp.sh launchtime on`, etf delta 600 µs).

Hardware profile (measured):
- per-hop processing 4,020 ns, propagation 80 ns
- gate guard 12.4 µs
- 800 µs cycle, 320 ns tick
- store-and-forward
