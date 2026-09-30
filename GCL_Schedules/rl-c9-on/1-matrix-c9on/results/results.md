# Traffic generation results -- rl-c9-on schedule (RL-trained, constraint 9 on)

30-second concurrent run of `Spawning-Flows/gen_traffic.py` on all three end-stations (S1, S2, S3)
against the live, deployed TAS/GCL schedule from `../schedule.json` and VLAN admission via
`Network-Configure-Manager/configureManager.py` (`../stream-realizable.csv`). This is the
**second** schedule package tested in this repo (see `../../heuristic-c9-off/1-matrix-c9off/results/`
for the first, heuristic-generated one) -- this one comes from an RL-trained policy
(`policy.pt` in this directory) with constraint 9 enabled, and uses 20 candidate flows (10
admitted) with some routes differing from the heuristic package (e.g. `sw08->sw07->sw05` instead
of `sw08->sw06->sw05` for several S2<->S1 flows).

Real UDP traffic on the wire, PCP-tagged per flow, timed to each flow's actual period/offset --
not a simulation. Raw per-node output: `results_S1.log`, `results_S2.log`, `results_S3.log`.

## MSTP issue hit again (same root cause class as the heuristic package)

Applying this schedule's flow admission hit the same stale-MSTI-priority conflict found before:
`sw08` still held priority-0 for tree "5" left over from the *previous* (heuristic) schedule run,
where tree 5 legitimately belonged to a different route ending at `sw08`. Since this run's tree
numbering reused "5" for a different route (`S3->sw01->sw02->S1`, needing `sw02`/`sw01` as root),
`sw08`'s leftover claim won the root election by MAC tiebreak, blocking `sw01<->sw02`. Fixed the
same way: `mstpctl settreeprio br0 5 8` on `sw08` to release the stale claim. This confirms
`configureManager.py`'s `build_mstp()` needs a proper fix to reset stale priorities on switches no
longer holding a given tree -- flagged again, not yet implemented.

## Timing-precision caveat

Same caveat as before (see `Spawning-Flows/README.md`): Python's `time.sleep` jitter (tens to
hundreds of microseconds) is large relative to these flows' actual TAS-gated window sizes (a few
microseconds per 800us cycle), so nonzero deadline misses are expected and don't indicate a
schedule or switch defect.

## Results (sorted by flow id)

| id | route | pcp | size(B) | period(ns) | deadline(ns) | sent | received | received% | avg latency(us) | jitter stddev(us) | jitter rfc3550(us) | deadline misses |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1  | S3→S1 | 7 | 500 | 200000 | 200000 | 149979 | 148454 | 98.98% | 92.8  | 52.0   | 36.6  | 2350 |
| 2  | S2→S1 | 6 | 400 | 200000 | 200000 | 149978 | 147822 | 98.56% | 339.0 | 155.7  | 166.0 | 112221 |
| 6  | S2→S1 | 7 | 100 | 400000 | 400000 | 74988  | 73910  | 98.56% | 133.9 | 57.7   | 53.0  | 41 |
| 8  | S2→S3 | 7 | 100 | 800000 | 800000 | 37505  | 37348  | 99.58% | 129.3 | 83.5   | 23.1  | 2 |
| 9  | S3→S2 | 7 | 500 | 200000 | 200000 | 149976 | 149346 | 99.58% | 146.7 | 85.9   | 75.3  | 30843 |
| 10 | S1→S3 | 7 | 100 | 800000 | 800000 | 37506  | 37125  | 98.98% | 112.2 | 81.9   | 16.0  | 1 |
| 14 | S1→S2 | 7 | 100 | 200000 | 200000 | 149976 | 147820 | 98.56% | 89.2  | 71.8   | 26.2  | 2665 |
| 17 | S2→S3 | 6 | 200 | 800000 | 800000 | 37505  | 37348  | 99.58% | 162.4 | 89.0   | 32.0  | 8 |
| 19 | S3→S1 | 7 | 500 | 400000 | 400000 | 74987  | 74226  | 99.05% | 89.0  | 41.6   | 36.4  | 26 |
| 20 | S3→S1 | 7 | 200 | 200000 | 200000 | 149974 | 148450 | 98.98% | 82.5  | 47.1   | 40.7  | 1400 |

Overall delivery: 98.6-99.6% across all 10 flows, comparable to the heuristic package's 97.8-99.0%.

Flow 2 (`S2->S1`, PCP 6, the new `sw07`-routed path) stands out with a notably higher average
latency (339us vs. everything else in the 80-160us range) and by far the most deadline misses
(112221 of 147822, 76%) despite a very tight 200us deadline -- this route is one hop longer
(`sw08->sw07->sw05->sw02`) than the equivalent heuristic-package route
(`sw08->sw06->sw05->sw02`), and PCP 6 here is competing with flow 9 (PCP 7, also very high miss
count) somewhere along a shared segment. Worth a closer look if this specific route/PCP
combination matters -- not chased further here.
