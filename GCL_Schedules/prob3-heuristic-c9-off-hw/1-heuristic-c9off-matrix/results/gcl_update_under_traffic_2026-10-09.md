# GCL update under traffic: prob3-heuristic-c9-off-hw/1-heuristic-c9off-matrix (2026-10-09)

Dataset 1 zero-miss package, 42 flows on S1, S2, S3 (30 s each run). At +10 s the package's own
GCL files were re-sent to all 27 ports of the 8 switches and activated one port at a time, as
`deploy-GCL/configure_gcl.py` does (`gcl-schedule-update/loss_during_update.py --scenario mesh-8
--strategy sequential --target-gcl <pkg>/gcl`). Every frame is logged at both ends; a frame is lost
if it was sent and never received, and misses its deadline if latency > deadline (= period).

Phases: **before** = traffic start to the first update command; **during** = first command sent to
the last port running the new GCL (its ConfigChangeTime); **after** = the rest of the run.

Baseline without any update (`results-2026-10-09_3`): 3,187,361 / 3,187,488 frames delivered
(127 lost, 0.004%), 2 deadline misses (flow 3, two frames one period late), no switch queue drops.

| run | update time | before: lost / sent (misses) | during: lost / sent (misses) | after: lost / sent (misses) |
|---|---|---|---|---|
| `update-loss-2026-10-09` | 2.53 s | 11 / 1,062,507 (1) | 4 / 268,350 (0) | 17,265 / 1,856,361 (192) |
| `update-loss-2026-10-09_2` | 2.63 s | 121 / 1,062,516 (0) | 0 / 279,582 (0) | 172 / 1,845,099 (0) |
| `update-loss-2026-10-09_3` | 2.74 s | 100 / 1,062,428 (0) | 0 / 291,472 (0) | 119 / 1,833,471 (1) |
| **all 3 runs** | | **232 / 3,187,451 (1)** — 0.0073% | **4 / 839,404 (0)** — 0.0005% | **17,556 / 5,534,931 (193)** — 0.3172% |

Run 1 also had a single ~320 ms outage at 18.23–18.55 s, 5.7 s after the update had completed:
22 of 42 flows lost every frame for that stretch (17,050 frames lost; 192 deadline misses, frames
held up to 321 ms in switch queues), with Q DROP on sw01/p4, sw02/p2, sw02/p3, sw05/p2, sw07/p3, sw08/p4. It did not
recur in runs 2 and 3 or in the baseline, and no switch logged a link or spanning-tree event, so it
is not attributed to the update. Without it, run 1's after-phase lost 215 frames with 0 misses.

Summary: during the update (2.5–2.7 s) the network lost 4 of 839,404 frames and no frame missed its
deadline; after the update, loss and misses were back to the before-update level (runs 2 and 3:
0.006–0.009% lost, 0–1 misses).

Per-run details: `update-loss-*/summary.md`, timelines `update-loss-*/loss_timeline.png`.
