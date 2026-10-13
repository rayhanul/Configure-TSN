# Ring dataset 6: export validation

The original pipeline settings were retained. There are 50 offered flows: 20 initial and 30 additional. SMT schedules initial flows; admission totals include the fixed SMT flows plus admitted arrivals.

| Package | Scheduled flows | Independent verifier | Hardware replay |
|---|---:|---|---|
| heuristic-c9-off/6-matrix-c9off | 10 | PASS | PASS |
| heuristic-c9-on/6-matrix-c9on | 10 | PASS | PASS |
| prob3-heuristic-c9-off/6-heuristic-c9off-matrix | 25 | FAIL (see log) | PASS |
| prob3-heuristic-c9-on/6-heuristic-c9on-matrix | 25 | FAIL (see log) | PASS |
| prob3-rl-c9-off/6-rl-c9off-matrix | 27 | FAIL (see log) | PASS |
| prob3-rl-c9-on/6-rl-c9on-matrix | 27 | FAIL (see log) | PASS |
| rl-c9-off/6-matrix-c9off | 10 | PASS | PASS |
| rl-c9-on/6-matrix-c9on | 10 | PASS | PASS |
| smt-c9-off/6-t3600-c9off-minlat | 10 | PASS | PASS |
| smt-c9-on/6-fair-retimed-c9on | 10 | PASS | PASS |

Admission validation limitation: the existing Problem 3 implementation omits final-link propagation delay when computing dynamic-flow latency. The generic verifier also compares first-instance hop timing against the worst-instance latency reported by per-instance admission. For the C9-off RL admission export, it flags one recomputed latency 80 ns beyond its 400,000 ns deadline. These exports must not be described as passing all independent constraints. Raw diagnostics are beside each package.

Hardware replay uses the existing checker, 12,400 ns gate guard, four cycles, and hop delays 2,100 / 3,000 / 4,020 ns. Replay passing does not resolve inconsistent reported latency or verify live MSTP/VLAN routing.
