# Tree topology: datasets 4, 5, 11, 12, 13 on the physical testbed

All five datasets use the same eight-switch tree topology
(`RL-TSN/data/dataset-testbed/network-topology-rtas-2027-tree.json`; each dataset's
`network-topology.json` is identical), the measured TTTech hardware profile (`hw/tttech-sw0p3.json`),
20 initial flows and 30 additional (Problem 3) flows, periods 200 / 400 / 800 µs. They differ only in
the traffic draw.

| Dataset | Seed | Testbed run | Full report |
|---|---|---|---|
| 4 | – | 2026-10-10 | [result-2026-10-10-dataset-testbed-4-saf](../result-2026-10-10-dataset-testbed-4-saf/TESTBED_RESULTS_2026-10-10.md) (C9-off rows from `result-2026-10-09-dataset-testbed-4-avgwin`) |
| 5 | 20261010 | 2026-10-11 | [result-2026-10-10-dataset-testbed-5-avgwin](../result-2026-10-10-dataset-testbed-5-avgwin/TESTBED_RESULTS_2026-10-11.md) |
| 11 | 47 | 2026-10-13 | [result-2026-10-13-dataset-testbed-11-tree-avgwin](../result-2026-10-13-dataset-testbed-11-tree-avgwin/TESTBED_RESULTS_2026-10-13.md) |
| 12 | 48 | 2026-10-13 | [result-2026-10-13-dataset-testbed-12-tree-avgwin](../result-2026-10-13-dataset-testbed-12-tree-avgwin/TESTBED_RESULTS_2026-10-13.md) |
| 13 | 49 | 2026-10-13 | [result-2026-10-13-dataset-testbed-13-tree-avgwin](../result-2026-10-13-dataset-testbed-13-tree-avgwin/TESTBED_RESULTS_2026-10-13.md) |

Every package: GCLs live on all ports, flows admitted (VLANs + MSTP, one MST region), routes pinged,
then 30 s of traffic on S1, S2, S3 at once (NIC launch time, NIC RX timestamps; deadline = period).
Single trials per package. Per-package detail for 11–13: [BENCHMARK_RESULTS.md](BENCHMARK_RESULTS.md).

## Totals

| Dataset | Packages | Sent | Lost | Deadline misses | Zero-miss packages |
|---|---|---|---|---|---|
| 4 | 10 | 13,649,550 | 34 | 0 | 10 / 10 |
| 5 | 10 | 12,374,568 | 22 | 19 | 7 / 10 |
| 11 | 10 | 12,862,045 | 187,525 | 17 | 8 / 10 |
| 12 | 10 | 14,999,654 | 42,493 | 423 | 4 / 10 |
| 13 | 10 | 13,424,578 | 65 | 4 | 9 / 10 |
| **All** | **50** | **67,310,395** | **230,139** | **463** | **38 / 50** |

## Deadline misses per approach

| Approach | D4 | D5 | D11 | D12 | D13 |
|---|---|---|---|---|---|
| SMT C9-off | 0 | 2 | 12 | 7 | 4 |
| SMT C9-on | 0 | 15 | 5 | 5 | 0 |
| heuristic C9-off | 0 | 0 | 0 | 0 | 0 |
| heuristic C9-on | 0 | 0 | 0 | 94 | 0 |
| RL C9-off | 0 | 0 | 0 | 0 | 0 |
| RL C9-on | 0 | 0 | 0 | 78 | 0 |
| Problem 3 heuristic C9-off | 0 | 0 | 0 | 0 | 0 |
| Problem 3 heuristic C9-on | 0 | 0 | 0 | 111 | 0 |
| Problem 3 RL C9-off | 0 | 2 | 0 | 0 | 0 |
| Problem 3 RL C9-on | 0 | 0 | 0 | 128 | 0 |

## Problem 3 admitted flows (of 50 offered)

| Approach | D4 | D5 | D11 | D12 | D13 |
|---|---|---|---|---|---|
| heuristic C9-off | 24 | 24 | 29 | 34 | 23 |
| heuristic C9-on | 27 | 28 | 27 | 36 | 25 |
| RL C9-off | 28 | 25 | 25 | 33 | 27 |
| RL C9-on | 29 | 29 | 27 | 37 | 28 |

Base schedules (SMT, heuristic, RL) admit 10–11 of 20 flows on every dataset.

## Findings

- **heuristic C9-off, RL C9-off and Problem 3 heuristic C9-off had zero deadline misses on all five
  datasets.** Apart from the two dataset-12 issues below, the other packages lost at most a few dozen
  frames out of 0.8–2.6 million.
- **C9-on halves latency**: average latency of about 30–40 µs, against 55–90 µs with C9 off for the
  same approach.
- **Problem 3 RL C9-on admits the most flows** on four of the five datasets (27–37 of 50). RL admits
  at least as many flows as the heuristic in each C9 setting, except C9-off on datasets 11 and 12.
- **SMT's misses are isolated outliers**: a few frames per 30 s held for one extra cycle (max latency
  234–934 µs), not a systematic schedule gap.
- **Dataset 11 SMT C9-off lost 187,500 frames**: flows 5 and 7 (S2→S1) received nothing, an
  unreachable route rather than congestion. The other nine dataset-11 packages delivered S2→S1
  traffic.
- **Dataset 12 C9-on, four packages**: almost every flow lost about 1.06% of its frames, and a few
  frames per flow arrived about 320 ms late. That matches one network-wide stall of about 320 ms
  during each run, not a schedule problem; the C9-off runs of the same dataset were clean. The
  cause is not yet identified; rerun these four packages to tell whether it is transient.
- Hardware replay passed for all 30 packages of datasets 11–13; independent export validation passed
  for 18 of 30 (see each result directory's `validation.json`).
