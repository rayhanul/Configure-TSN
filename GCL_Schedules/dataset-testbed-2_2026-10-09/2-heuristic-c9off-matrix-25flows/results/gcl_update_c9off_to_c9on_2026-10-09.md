# GCL update c9off → c9on under traffic (dataset 2, 2026-10-09)

**Before:** `2-heuristic-c9off-matrix-25flows` (dataset-testbed-2_2026-10-07/2-heuristic-c9off-matrix
restricted to the 25 flows the target schedules) deployed on all 27 ports, its 25 flows admitted
(VLANs, MSTP) and running on S1, S2, S3. **Update:** at +10 s every port's GCL is replaced by
`2-heuristic-c9on-matrix` (copied from RL-TSN `result-2026-10-08-dataset-testbed-2/prob3-heuristic-c9-on`),
one port at a time as `deploy-GCL/configure_gcl.py` does. Only the GCLs change: same flows, routes,
VLANs and MSTP; senders keep the c9off transmit offsets for the whole run. 30 s per run, 3 runs.

Phases: before = start to the first update command; during = first command to the last port running
the new GCL; after = the rest. Lost = sent and never received; deadline miss = latency > deadline (= period).

## Results

| run | update | before: lost (misses) | during: lost (misses) | after: lost (misses) |
|---|---|---|---|---|
| `update-loss-2026-10-09` | 2.62 s | 7,526 / 650,016 (1.158%) (48,532) | 0 / 170,181 (0.000%) (11,633) | 44 / 1,129,803 (0.004%) (173,804) |
| `update-loss-2026-10-09_2` | 2.96 s | 41 / 650,005 (0.006%) (50,000) | 0 / 192,510 (0.000%) (12,381) | 63 / 1,107,414 (0.006%) (170,344) |
| `update-loss-2026-10-09_3` | 2.61 s | 0 / 650,005 (0.000%) (50,000) | 6 / 169,812 (0.004%) (11,433) | 36 / 1,130,183 (0.003%) (173,864) |

Deadline misses by flow (all three runs alike):

| phase | flow 1 (S1→S2, pcp 6) | flow 9 (S1→S2, pcp 7) | flow 14 (S3→S2, pcp 7) | other 22 flows |
|---|---|---|---|---|
| before (c9off) | 100% of frames (200–204 µs) | 0 | 0 | 0 |
| during (ports switching) | 73–75% | 5–7% (764–916 frames) | 5–7% (764–916 frames) | 0 |
| after (c9on) | **0** | **100%** (≤228 µs) | **100%** (≤233 µs, 433 µs once) | 0 |

- **Loss:** the update itself lost 0–6 frames per run (≤0.004%); after it, loss was at the
  background level of the before-phase (0.003–0.006%). No switch queue drops in runs 2 and 3.
- **Deadline misses** move from one flow to two: c9on fixes flow 1 (which misses every deadline under
  c9off on this testbed) but makes flows 9 and 14 miss every deadline. Both have windows spaced ~4.2 µs
  per hop in c9on, which assumes cut-through forwarding; on these store-and-forward switches their
  frames wait one full 200 µs cycle (latency 228–233 µs). Flow 9 also keeps its c9off send offset
  (8.3 µs vs c9on's 25.0 µs). During the update the network is mixed, so both effects appear partially.
- Max latency rises from 297 µs to 397 µs during the update and stays there.

Run 1's before-phase includes a ~321 ms outage (7,526 lost in that phase vs 0–41 in runs 2–3; 12 flows delayed up to
321 ms, Q DROP on 9 ports) on the old schedule, before any update command: the same glitch seen once in
the dataset-1 experiment, so it is a testbed event, not an update effect.

Baseline without update (`results-2026-10-09`): 39 / 1,950,000 lost, 150,000 misses (flow 1 only).
Per-run details: `update-loss-*/summary.md`, timelines `update-loss-*/loss_timeline.png`.
