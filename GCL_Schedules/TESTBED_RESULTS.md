# Testbed results: which schedules had no deadline misses

**Only one schedule ran on the physical testbed with zero deadline misses and full delivery:
dataset 1, `prob3-heuristic-c9-off-hw/1-heuristic-c9off-matrix`, run `results-2026-10-07_4`**
(42 flows, 3,187,354 / 3,187,500 packets delivered, 0 misses). No dataset-2 schedule has had a
zero-miss run yet.

Every run: 8 TTTech switches, 3 end stations (S1, S2, S3), 1 Gb/s, 800 µs GCL cycle, 30 s of
traffic. Senders transmit each frame at its scheduled offset with NIC launch time (SO_TXTIME +
etf offload) and receivers use NIC hardware RX timestamps. A deadline miss is a frame whose
latency exceeds its deadline (deadline = period). Each run's full per-flow report is
`<package>/results/<run>/results.md`.

## Dataset 1 (`RL-TSN/data/dataset-testbed/1`, seed 42)

| Package | Timing model | Run | Flows | Delivered | Deadline misses |
|---|---|---|---|---|---|
| **`prob3-heuristic-c9-off-hw/1-heuristic-c9off-matrix`** | C9 off, 4 µs hop, 2.4 µs guard | **`results-2026-10-07_4`** | **42** | **100.00%** | **0** ✅ |
| same | same | `results-2026-10-07_2`, `_3` | 42 | 77-79% | 161 / 1 (routes blocked by stale MSTP state, since fixed) |
| `prob3-rl-c9-on/1-rl-c9on-matrix` | C9 on (cut-through), 2 µs hop | `results-2026-10-01_3` ... `_5` | 48 | 99.99% | ~187k (flows 2 and 300003) |
| same | same | `results-2026-10-07`, `_2`, `_3` | 48 | 84.4% | ~2.5k (sw08 drops pcp-6 traffic) |
| `prob3-rl-c9-on/1-rl-c9on-matrix-S1S2` | same, S1<->S2 flows only | `results-2026-10-07`, `_2` | 15 | 63-100% | 2,250 / 187,492 |
| `heuristic-c9-off/1-matrix-c9off` | stages after SMT still cut-through | `results-2026-10-01_3` | 10 | 100.00% | 75,003 (flow 15) |

## Dataset 2 (`RL-TSN/data/dataset-testbed/2`, seed 7)

| Package | Timing model | Run | Flows | Delivered | Deadline misses |
|---|---|---|---|---|---|
| `dataset-testbed-2_2026-10-08/2-rl-c9off-matrix` | C9 off, 4 µs hop, 12.4 µs guard | `results-2026-10-08` | 26 | 100.00% | 37,499: flow 19 (S2->S1, 200 µs), 25% of its frames |
| `dataset-testbed-2_2026-10-07/2-heuristic-c9off-matrix` | C9 off, 4 µs hop, 2.4 µs guard | `results-2026-10-08` | 43 | 100.00% | 150,000: flow 1 (S1->S2, 200 µs), 100% of its frames |
| `dataset-testbed-2_2026-10-08/2-rl-c9on-matrix` | C9 on (cut-through), 4 µs hop, 12.4 µs guard | `results-2026-10-08` | 32 | 99.99% | 149,967: flows 14 and 18, 50% each |
| same | same | `results-2026-10-08_2` | 32 | 77.94% | 74,993: flow 14; S2->S1 route blocked at sw07 (CIST port state) |
| `dataset-testbed-2_2026-10-08/2-rl-c9on-matrix-S2rx` | same, S2 only receives | `results-2026-10-08` | 18 | 100.00% | 74,994: flow 14 (S3->S2, 200 µs), 50% |

In every dataset-2 run all missed frames come from one or two 200 µs flows, each missing a fixed
share of its instances (25/50/100%): those instances wait one period for the next window, a
schedule/model gap rather than congestion.

## Not yet run on the testbed

`heuristic-c9-off-hw`, `heuristic-c9-on-hw`, `rl-c9-off-hw`, `smt-c9-off-hw`, `smt-c9-on-hw`
(dataset-1 base and enlarged schedules) and `prob3-rl-c9-off-hw` (dataset 1, RL + Problem 3,
C9 off; passes `deploy-GCL/check_schedule.py`).

## What separates the zero-miss run

Schedules generated with store-and-forward timing in every stage (C9 off), the switches'
measured per-hop delay, and a gate guard, then checked with `deploy-GCL/check_schedule.py`
before deploying. C9-on schedules assume cut-through forwarding and miss deadlines on these
store-and-forward switches. See "Why schedules missed deadlines on the testbed" in `../README.md`.
