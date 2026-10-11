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

| package | flows | before the fixes (round 1): delivered / lost / misses | after the fixes (final round): delivered / lost / misses | final max latency |
|---|---|---|---|---|
| SMT C9-off | 11 | 100.00% / 21 / 74,994 | 100.00% / 0 / **0** | 133.7 µs |
| SMT C9-on | 11 | 100.00% / 28 / 12,320 | 100.00% / 4 / **0** | 62.1 µs |
| heuristic C9-off | 11 | 100.00% / 46 / 74,983 | 100.00% / 9 / **0** | 134.0 µs |
| heuristic C9-on | 11 | 100.00% / 25 / 1 | 100.00% / 8 / **0** | 156.6 µs |
| RL C9-off | 11 | 100.00% / 49 / 0 | 100.00% / 0 / **0** | 133.7 µs |
| RL C9-on | 11 | 100.00% / 23 / 27,392 | 100.00% / 0 / **0** | 44.5 µs |
| Problem 3 heuristic C9-off | 24 | 99.99% / 117 / 74,994 | 100.00% / 8 / **0** | 420.7 µs |
| Problem 3 heuristic C9-on | 29 → 27 | 99.98% / 321 / 37,499 | 100.00% / 4 / **0** | 408.2 µs |
| Problem 3 RL C9-off | 28 | 99.25% / 15,124 / 74,364 | 100.00% / 0 / **0** | 235.5 µs |
| Problem 3 RL C9-on | 28 → 29 | 99.50% / 10,299 / 27,316 | 100.00% / 1 / **0** | 139.8 µs |

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
