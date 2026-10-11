# Testbed results: result-2026-10-09-dataset-testbed-4-avgwin (2026-10-10)

**Round 1, as generated** (the tables below up to "Final round"). These packages missed deadlines because of causes A, B, C and D, all since fixed; final results and causes: [../result-2026-10-10-dataset-testbed-4-saf/SUMMARY_REPORT_2026-10-10.md](../result-2026-10-10-dataset-testbed-4-saf/SUMMARY_REPORT_2026-10-10.md). The C9-on packages here are the originals (C9-on spaced for cut-through switches, cause B); their regenerated versions and final runs are in `../result-2026-10-10-dataset-testbed-4-saf/`.

Each package's GCLs were deployed on all of its switch ports (all live), its scheduled flows admitted (VLANs + MSTP, all 8 switches in one MST region), leftover VLAN interfaces removed on S1/S2/S3, every route pinged, then 30 s of traffic on S1, S2, S3 at once (NIC launch time, NIC RX timestamps). Full per-flow reports: `<package>/results/results-<date>/results.md`.

| package | approach | flows | routes ping OK | delivered | lost | deadline misses | flows with misses | switch queue drops |
|---|---|---|---|---|---|---|---|---|
| `smt-c9-off/4-t3600-c9off-minlat` | smt-c9-off | 11 | 11/11 | 100.00% | 21 | 74,994 (7.41%) | 1 | none |
| `smt-c9-on/4-fair-retimed-c9on` | smt-c9-on | 11 | 11/11 | 100.00% | 28 | 12,320 (1.22%) | 3 | none |
| `heuristic-c9-off/4-matrix-c9off` | heuristic-c9-off | 11 | 11/11 | 100.00% | 46 | 74,983 (7.41%) | 1 | none |
| `heuristic-c9-on/4-matrix-c9on` | heuristic-c9-on | 11 | 11/11 | 100.00% | 25 | 1 (0.00%) | 1 | none |
| `rl-c9-off/4-matrix-c9off` | rl-c9-off | 11 | 11/11 | 100.00% | 49 | 0 (0.00%) | 0 | none |
| `rl-c9-on/4-matrix-c9on` | rl-c9-on | 11 | 11/11 | 100.00% | 23 | 27,392 (2.71%) | 1 | none |
| `prob3-heuristic-c9-off/4-heuristic-c9off-matrix` | prob3-heuristic-c9-off | 24 | 24/24 | 99.99% | 117 | 74,994 (4.65%) | 2 | none |
| `prob3-heuristic-c9-on/4-heuristic-c9on-matrix` | prob3-heuristic-c9-on | 29 | 29/29 | 99.98% | 321 | 37,499 (1.75%) | 1 | none |
| `prob3-rl-c9-off/4-rl-c9off-matrix` | prob3-rl-c9-off | 28 | 28/28 | 99.25% | 15,124 | 74,364 (3.70%) | 17 | sw03/p4 +12, sw05/p4 +3578, sw06/p4 +5569, sw07/p4 +4349, sw08/p4 +1573 |
| `prob3-rl-c9-on/4-rl-c9on-matrix` | prob3-rl-c9-on | 28 | 28/28 | 99.50% | 10,299 | 27,316 (1.33%) | 16 | sw03/p4 +11, sw05/p4 +1950, sw06/p4 +1172, sw07/p4 +5138, sw08/p4 +1969 |

## Flows with misses or notable loss

- **smt-c9-off/4-t3600-c9off-minlat** (`smt-c9-off/4-t3600-c9off-minlat/results/results-2026-10-10/results.md`): flow 14 (S3→S2): 149990/150000 received, 74994 misses, latency 72.6 / 178.4 / 273.3 µs
- **smt-c9-on/4-fair-retimed-c9on** (`smt-c9-on/4-fair-retimed-c9on/results/results-2026-10-10/results.md`): flow 9 (S1→S3): 37500/37500 received, 16 misses, latency 39.2 / 398.2 / 1198.1 µs; flow 14 (S3→S2): 149991/150000 received, 2 misses, latency 31.2 / 31.6 / 231.8 µs; flow 19 (S2→S3): 74999/75000 received, 12302 misses, latency 28.0 / 111.3 / 423.5 µs
- **heuristic-c9-off/4-matrix-c9off** (`heuristic-c9-off/4-matrix-c9off/results/results-2026-10-10/results.md`): flow 14 (S3→S2): 149970/149991 received, 74983 misses, latency 28.0 / 126.1 / 224.4 µs
- **heuristic-c9-on/4-matrix-c9on** (`heuristic-c9-on/4-matrix-c9on/results/results-2026-10-10/results.md`): flow 19 (S2→S3): 74999/75000 received, 1 misses, latency 28.1 / 46.7 / 428.0 µs
- **rl-c9-off/4-matrix-c9off** (`rl-c9-off/4-matrix-c9off/results/results-2026-10-10/results.md`): no flow lost >100 frames or missed a deadline
- **rl-c9-on/4-matrix-c9on** (`rl-c9-on/4-matrix-c9on/results/results-2026-10-10/results.md`): flow 19 (S2→S3): 75000/75000 received, 27392 misses, latency 28.1 / 190.2 / 422.1 µs
- **prob3-heuristic-c9-off/4-heuristic-c9off-matrix** (`prob3-heuristic-c9-off/4-heuristic-c9off-matrix/results/results-2026-10-10/results.md`): flow 14 (S3→S2): 149989/150000 received, 74993 misses, latency 28.0 / 126.0 / 224.4 µs; flow 20 (S1→S3): 149961/149977 received, 1 misses, latency 133.3 / 133.5 / 258.7 µs
- **prob3-heuristic-c9-on/4-heuristic-c9on-matrix** (`prob3-heuristic-c9-on/4-heuristic-c9on-matrix/results/results-2026-10-10/results.md`): flow 19 (S2→S3): 75000/75000 received, 37499 misses, latency 29.0 / 230.2 / 428.7 µs
- **prob3-rl-c9-off/4-rl-c9off-matrix** (`prob3-rl-c9-off/4-rl-c9off-matrix/results/results-2026-10-10/results.md`): flow 3 (S2→S3): 74211/75000 received, 18 misses, latency 83.3 / 139.6 / 320883.6 µs; flow 6 (S1→S3): 37099/37500 received, 0 misses, latency 134.2 / 134.5 / 715.6 µs; flow 7 (S1→S3): 37106/37500 received, 9 misses, latency 235.0 / 287.0 / 320851.2 µs; flow 8 (S2→S3): 148418/150000 received, 26 misses, latency 83.6 / 175.8 / 320883.6 µs; flow 9 (S1→S3): 37099/37500 received, 1 misses, latency 111.8 / 112.1 / 808.7 µs; flow 11 (S2→S1): 37107/37500 received, 8 misses, latency 30.9 / 100.1 / 320727.7 µs; flow 12 (S2→S3): 74208/75000 received, 13 misses, latency 87.5 / 157.7 / 320850.3 µs; flow 13 (S1→S2): 148409/150000 received, 9 misses, latency 19.1 / 39.4 / 320005.2 µs; flow 14 (S3→S2): 148397/150000 received, 37110 misses, latency 28.1 / 131.2 / 320811.3 µs; flow 15 (S3→S2): 148399/150000 received, 13 misses, latency 33.2 / 128.2 / 320778.1 µs; flow 18 (S2→S1): 37107/37500 received, 8 misses, latency 41.2 / 110.3 / 320738.0 µs; flow 19 (S2→S3): 74211/75000 received, 18 misses, latency 83.3 / 135.3 / 320859.6 µs; flow 20 (S1→S3): 148398/150000 received, 37104 misses, latency 133.3 / 172.1 / 1067.9 µs; flow 21 (S2→S1): 37107/37500 received, 8 misses, latency 21.5 / 90.7 / 320719.0 µs; flow 23 (S2→S1): 37105/37500 received, 7 misses, latency 15.9 / 76.7 / 320709.5 µs; flow 29 (S1→S2): 74204/75000 received, 4 misses, latency 9.6 / 44.9 / 319781.0 µs; flow 30 (S1→S2): 74204/75000 received, 4 misses, latency 30.0 / 47.6 / 319771.0 µs; flow 45 (S3→S1): 37101/37500 received, 4 misses, latency 154.3 / 189.4 / 320964.9 µs
- **prob3-rl-c9-on/4-rl-c9on-matrix** (`prob3-rl-c9-on/4-rl-c9on-matrix/results/results-2026-10-10/results.md`): flow 1 (S3→S2): 74213/75000 received, 13 misses, latency 21.0 / 76.9 / 319983.7 µs; flow 3 (S2→S3): 74204/75000 received, 7 misses, latency 25.2 / 51.3 / 320801.8 µs; flow 4 (S3→S2): 37106/37500 received, 6 misses, latency 53.8 / 108.1 / 319987.2 µs; flow 6 (S1→S3): 37102/37500 received, 3 misses, latency 34.5 / 60.6 / 320778.8 µs; flow 8 (S2→S3): 148407/150000 received, 13 misses, latency 28.1 / 76.3 / 320822.6 µs; flow 9 (S1→S3): 37110/37500 received, 23 misses, latency 397.2 / 493.7 / 324839.5 µs; flow 10 (S3→S2): 74212/75000 received, 12 misses, latency 23.8 / 76.1 / 319996.3 µs; flow 11 (S2→S1): 37107/37500 received, 7 misses, latency 58.5 / 118.6 / 319997.7 µs; flow 19 (S2→S3): 74231/75000 received, 27175 misses, latency 28.0 / 323.5 / 320823.3 µs; flow 20 (S1→S3): 148407/150000 received, 13 misses, latency 26.2 / 56.0 / 320802.8 µs; flow 21 (S2→S1): 37106/37500 received, 6 misses, latency 35.3 / 86.9 / 319979.3 µs; flow 22 (S2→S1): 37106/37500 received, 6 misses, latency 68.7 / 120.3 / 319888.6 µs; flow 23 (S2→S1): 37105/37500 received, 6 misses, latency 68.7 / 120.3 / 319691.2 µs; flow 42 (S1→S2): 37109/37500 received, 10 misses, latency 26.8 / 112.4 / 320719.7 µs; flow 48 (S1→S2): 37109/37500 received, 10 misses, latency 16.1 / 102.2 / 320709.8 µs; flow 50 (S2→S1): 37106/37500 received, 6 misses, latency 58.5 / 110.0 / 319658.5 µs

## Final round: C9-off packages (2026-10-10, fixes A and C in place)

Same packages as above (C9-off schedules unchanged), rerun after fix A (one NIC launch-time queue) and fix C (etf delta 600 µs). Fix D (wait for the spanning tree to settle) came later, but none of these runs hit the spanning-tree stall. Latest run of each package.

| package | approach | flows | routes ping OK | delivered | lost | deadline misses | flows with misses | switch queue drops |
|---|---|---|---|---|---|---|---|---|
| `smt-c9-off/4-t3600-c9off-minlat` | smt-c9-off | 11 | 11/11 | 100.00% | 0 | 0 (0.00%) | 0 | none |
| `heuristic-c9-off/4-matrix-c9off` | heuristic-c9-off | 11 | 11/11 | 100.00% | 9 | 0 (0.00%) | 0 | none |
| `rl-c9-off/4-matrix-c9off` | rl-c9-off | 11 | 11/11 | 100.00% | 0 | 0 (0.00%) | 0 | none |
| `prob3-heuristic-c9-off/4-heuristic-c9off-matrix` | prob3-heuristic-c9-off | 24 | 24/24 | 100.00% | 8 | 0 (0.00%) | 0 | none |
| `prob3-rl-c9-off/4-rl-c9off-matrix` | prob3-rl-c9-off | 28 | 28/28 | 100.00% | 0 | 0 (0.00%) | 0 | none |

- **smt-c9-off/4-t3600-c9off-minlat** (`smt-c9-off/4-t3600-c9off-minlat/results/results-2026-10-10_5/results.md`): no flow lost >100 frames or missed a deadline
- **heuristic-c9-off/4-matrix-c9off** (`heuristic-c9-off/4-matrix-c9off/results/results-2026-10-10_3/results.md`): no flow lost >100 frames or missed a deadline
- **rl-c9-off/4-matrix-c9off** (`rl-c9-off/4-matrix-c9off/results/results-2026-10-10_3/results.md`): no flow lost >100 frames or missed a deadline
- **prob3-heuristic-c9-off/4-heuristic-c9off-matrix** (`prob3-heuristic-c9-off/4-heuristic-c9off-matrix/results/results-2026-10-10_3/results.md`): no flow lost >100 frames or missed a deadline
- **prob3-rl-c9-off/4-rl-c9off-matrix** (`prob3-rl-c9-off/4-rl-c9off-matrix/results/results-2026-10-10_4/results.md`): no flow lost >100 frames or missed a deadline
