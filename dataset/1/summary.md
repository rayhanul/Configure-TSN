# Dataset 1 — flow admission and traffic generation summary

## What this dataset is

`stream.csv` (20 candidate flows, ids 1-20) and `additional-flows.csv` (30 more, unused so far) are
the flow-set inputs fed to an external SMT/heuristic GCL scheduler (not in this repo -- see
`GCL_Schedules/heuristic-c9-off/1-matrix-c9off/report.md`'s "Seeded from SMT run" line) against the
8-switch topology in `network-topology.json` here. That run admitted **10 of the 20** flows and
produced the schedule package at `GCL_Schedules/heuristic-c9-off/1-matrix-c9off/` (`schedule.json`,
per-port `gcl/*.cfg`, `report.md`, `offsets.csv`).

`network-topology.json` in this folder uses placeholder end-station IPs (`192.168.0.101-103`) for
scheduling purposes only -- it is not used for SSH/deployment. The real, SSH-reachable topology is
`network-topology/network-topology-rtas-2027.json` at the repo root.

## Physical realizability, over time

The scheduler admitted 10 flows among three end-stations (S1, S2, S3), but S3 was not physically
connected to the testbed when this was first deployed:

| When | End-stations present | Realizable flows |
|---|---|---|
| Initial deployment | S1, S2 | 2 of 10 (ids 5, 12 -- both `S2->S1`) |
| After S3's cable was connected and its SSH access set up | S1, S2, S3 | 10 of 10 (all admitted flows) |

"Realizable" means both the flow's source and destination are physically present and reachable --
the switch-side GCL schedule was deployed in full from the start regardless (unused TAS windows for
an absent node's traffic are just idle permissions, not a problem), but no sender/receiver traffic
can exist for a flow whose endpoint isn't there to run one.

## Pipeline

1. `Network-Configure-Manager/configureManager.py` -- VLAN + MSTP + addressing per flow, from a
   CSV filtered to the realizable subset (`GCL_Schedules/.../stream-realizable.csv`).
2. `deploy-GCL/configure_gcl.py` -- pushes `schedule.json`'s per-port GCL to all 8 switches via
   `tsntool` (see that folder's README for the tick-granularity rounding this needed).
3. `Spawning-Flows/gen_traffic.py` -- generates/receives real PCP-tagged UDP traffic per flow's
   actual period/offset/size, timestamped against the existing PTP sync
   (`clock-syncrhonize-ptp/`) to measure real one-way latency and jitter.

See the root `README.md` for the exact commands, organized by which node (CNC/sender/receiver) runs
what.

## Real traffic test results (2-flow phase: ids 5, 12, both S2->S1)

20s send window, over the live deployed GCL schedule:

| id | pcp | period | deadline | sent | received | avg latency | jitter (stddev) | jitter (RFC 3550) | deadline misses |
|---|---|---|---|---|---|---|---|---|---|
| 5  | 7 | 200us | 200us | 99,983 | 81,196 (81%) | 114.4us | 50.5us | 60.2us | 7,314 (9.0%) |
| 12 | 6 | 400us | 400us | 49,991 | 40,599 (81%) | 95.3us | 33.1us | 23.6us | 9 (0.02%) |

The tighter-deadline flow (id 5) shows both higher jitter and far more deadline misses than the
looser one (id 12) -- the expected signature of the generator's own timing-precision limit (Python
`time.sleep` jitter is tens-to-hundreds of microseconds, comparable to or larger than these flows'
few-microsecond TAS windows per 800us cycle), not a defect in the schedule or switches. Full
discussion: `Spawning-Flows/README.md`.

## Status as of this note

The 10-flow (all-realizable) admission is in progress. One real issue surfaced while bringing S3
online: `configureManager.py`'s remote command runner pipes the topology's `password` field into
`sudo -S` on non-root nodes -- S3 needed SSH *key* auth (its `password` field can't carry a real
secret safely) but *also* needs a real sudo password for privileged commands, which is a different
secret than the SSH key. Fixed by making SSH login always try known private keys first,
independently of `password`, which stays dedicated to sudo. Re-running the 10-flow `--apply` with
S3's actual sudo password supplied is the next step.
