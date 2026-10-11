# Testbed results: result-2026-10-10-dataset-testbed-4-saf (2026-10-10)

Final round of the C9-on packages (regenerated with the store-and-forward fix B) and the final round of the five C9-off packages (unchanged, so not regenerated: they live in `../result-2026-10-09-dataset-testbed-4-avgwin/`, where their runs are also listed), with fixes A, C (etf delta 600 µs) and, for SMT C9-on, D (wait for the spanning tree to settle) in place. Earlier rounds, the C9-off packages and the causes: [SUMMARY_REPORT_2026-10-10.md](SUMMARY_REPORT_2026-10-10.md).

Each package's GCLs were deployed on all of its switch ports (all live), its scheduled flows admitted (VLANs + MSTP, all 8 switches in one MST region), leftover VLAN interfaces removed on S1/S2/S3, every route pinged, then 30 s of traffic on S1, S2, S3 at once (NIC launch time, NIC RX timestamps). Full per-flow reports: `<package>/results/results-<date>/results.md`.

| package | approach | flows | routes ping OK | delivered | lost | deadline misses | flows with misses | switch queue drops |
|---|---|---|---|---|---|---|---|---|
| `../result-2026-10-09-dataset-testbed-4-avgwin/smt-c9-off/4-t3600-c9off-minlat` | smt-c9-off | 11 | 11/11 | 100.00% | 0 | 0 (0.00%) | 0 | none |
| `../result-2026-10-09-dataset-testbed-4-avgwin/heuristic-c9-off/4-matrix-c9off` | heuristic-c9-off | 11 | 11/11 | 100.00% | 9 | 0 (0.00%) | 0 | none |
| `../result-2026-10-09-dataset-testbed-4-avgwin/rl-c9-off/4-matrix-c9off` | rl-c9-off | 11 | 11/11 | 100.00% | 0 | 0 (0.00%) | 0 | none |
| `../result-2026-10-09-dataset-testbed-4-avgwin/prob3-heuristic-c9-off/4-heuristic-c9off-matrix` | prob3-heuristic-c9-off | 24 | 24/24 | 100.00% | 8 | 0 (0.00%) | 0 | none |
| `../result-2026-10-09-dataset-testbed-4-avgwin/prob3-rl-c9-off/4-rl-c9off-matrix` | prob3-rl-c9-off | 28 | 28/28 | 100.00% | 0 | 0 (0.00%) | 0 | none |
| `smt-c9-on/4-saf-retimed-c9on` | smt-c9-on | 11 | 11/11 | 100.00% | 4 | 0 (0.00%) | 0 | none |
| `heuristic-c9-on/4-matrix-c9on` | heuristic-c9-on | 11 | 11/11 | 100.00% | 8 | 0 (0.00%) | 0 | none |
| `rl-c9-on/4-matrix-c9on` | rl-c9-on | 11 | 11/11 | 100.00% | 0 | 0 (0.00%) | 0 | none |
| `prob3-heuristic-c9-on/4-heuristic-c9on-matrix` | prob3-heuristic-c9-on | 27 | 27/27 | 100.00% | 4 | 0 (0.00%) | 0 | none |
| `prob3-rl-c9-on/4-rl-c9on-matrix` | prob3-rl-c9-on | 29 | 29/29 | 100.00% | 1 | 0 (0.00%) | 0 | none |

## Flows with misses or notable loss

- **../result-2026-10-09-dataset-testbed-4-avgwin/smt-c9-off/4-t3600-c9off-minlat** (`../result-2026-10-09-dataset-testbed-4-avgwin/smt-c9-off/4-t3600-c9off-minlat/results/results-2026-10-10_5/results.md`): no flow lost >100 frames or missed a deadline
- **../result-2026-10-09-dataset-testbed-4-avgwin/heuristic-c9-off/4-matrix-c9off** (`../result-2026-10-09-dataset-testbed-4-avgwin/heuristic-c9-off/4-matrix-c9off/results/results-2026-10-10_3/results.md`): no flow lost >100 frames or missed a deadline
- **../result-2026-10-09-dataset-testbed-4-avgwin/rl-c9-off/4-matrix-c9off** (`../result-2026-10-09-dataset-testbed-4-avgwin/rl-c9-off/4-matrix-c9off/results/results-2026-10-10_3/results.md`): no flow lost >100 frames or missed a deadline
- **../result-2026-10-09-dataset-testbed-4-avgwin/prob3-heuristic-c9-off/4-heuristic-c9off-matrix** (`../result-2026-10-09-dataset-testbed-4-avgwin/prob3-heuristic-c9-off/4-heuristic-c9off-matrix/results/results-2026-10-10_3/results.md`): no flow lost >100 frames or missed a deadline
- **../result-2026-10-09-dataset-testbed-4-avgwin/prob3-rl-c9-off/4-rl-c9off-matrix** (`../result-2026-10-09-dataset-testbed-4-avgwin/prob3-rl-c9-off/4-rl-c9off-matrix/results/results-2026-10-10_4/results.md`): no flow lost >100 frames or missed a deadline
- **smt-c9-on/4-saf-retimed-c9on** (`smt-c9-on/4-saf-retimed-c9on/results/results-2026-10-10_3/results.md`): no flow lost >100 frames or missed a deadline
- **heuristic-c9-on/4-matrix-c9on** (`heuristic-c9-on/4-matrix-c9on/results/results-2026-10-10_2/results.md`): no flow lost >100 frames or missed a deadline
- **rl-c9-on/4-matrix-c9on** (`rl-c9-on/4-matrix-c9on/results/results-2026-10-10_2/results.md`): no flow lost >100 frames or missed a deadline
- **prob3-heuristic-c9-on/4-heuristic-c9on-matrix** (`prob3-heuristic-c9-on/4-heuristic-c9on-matrix/results/results-2026-10-10_2/results.md`): no flow lost >100 frames or missed a deadline
- **prob3-rl-c9-on/4-rl-c9on-matrix** (`prob3-rl-c9-on/4-rl-c9on-matrix/results/results-2026-10-10_2/results.md`): no flow lost >100 frames or missed a deadline
