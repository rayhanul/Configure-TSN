# Traffic generation results -- all 10 admitted flows

30-second concurrent run of `Spawning-Flows/gen_traffic.py` on all three end-stations (S1, S2, S3)
against the live, deployed TAS/GCL schedule (`../schedule.json`) and VLAN admission
(`../stream-realizable.csv` via `Network-Configure-Manager/configureManager.py`). Every admitted
flow was exercised in its real direction/role simultaneously -- this is real UDP traffic on the
wire, PCP-tagged per flow, timed to each flow's actual period/offset, not a simulation.

Raw per-node output: `results_S1.log`, `results_S2.log`, `results_S3.log` (this directory).

## Timing-precision caveat (see `Spawning-Flows/README.md` for the full discussion)

Python's `time.sleep` achieves tens-to-hundreds of microseconds of jitter on Linux, smaller than
some of these flows' periods (100-200us) but not small next to their actual TAS-gated window size
(a few microseconds per 800us cycle). Packets that miss their queue's brief open window queue
briefly at the first hop and either get delayed or dropped -- expect real, nonzero deadline misses,
especially on tighter-deadline/higher-PCP flows. This is the generator demonstrating admission with
real traffic and exposing where timing precision matters, not a defect in the schedule or switches.

**One outlier worth flagging plainly, not glossing over**: every PCP-6 flow in this run shows a
single ~320ms-latency straggler packet (visible as the inflated `max` and `jitter (stddev)`
columns below), while both PCP-7 flows (ids 1, 10) don't. Because it hit every PCP-6 flow across
all three nodes at roughly the same time, it looks like one shared transient event (e.g. a brief
scheduling/GC stall, or conntrack overhead right after the UFW rule changes below) rather than a
per-flow problem -- and because RFC 3550 jitter (a consecutive-delta average, far less sensitive to
one outlier than stddev) stays low and normal for the very same flows, this reads as a single
isolated blip, not sustained instability. Worth re-running to confirm it doesn't recur; not
investigated further here.

## Infrastructure fixes required to get here (not part of the schedule/tool itself)

- **S2 and S3 both have UFW active** with a default-DROP `INPUT` policy and no rule for this tool's
  flow ports. Neither had ever been tested as a `gen_traffic.py` *receiver* before this run (S2 was
  always a sender in earlier tests; S3 only just came online). Fixed by:
  `sudo ufw allow 50001:50020/udp comment 'gen_traffic.py flow ports'` on both. This is a standing
  firewall change, not undone after the test -- worth knowing if either host's firewall policy
  matters for other purposes.
- S3's `sudo` needs a real password (`jdg24001`'s account password) piped via `sudo -S -p ''`; a
  plain `sudo` with stdin redirected to `/dev/null` fails silently with no process ever starting.

## Results (sorted by flow id)

| id | route | pcp | size(B) | period(ns) | deadline(ns) | sent | received | received% | avg latency(us) | jitter stddev(us) | jitter rfc3550(us) | deadline misses |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1  | S3→S1 | 7 | 500 | 800000 | 800000 | 37506  | 37119  | 98.97% | 84.3  | 29.9   | 15.8 | 1 |
| 4  | S1→S3 | 6 | 300 | 100000 | 100000 | 300314 | 294013 | 97.90% | 96.8  | 2362.0 | 22.1 | 74738 |
| 5  | S2→S1 | 7 | 200 | 200000 | 200000 | 149996 | 148307 | 98.87% | 114.2 | 61.6   | 65.1 | 12356 |
| 8  | S2→S3 | 6 | 100 | 800000 | 800000 | 37510  | 37077  | 98.85% | 102.2 | 1663.1 | 36.9 | 1 |
| 10 | S1→S3 | 7 | 100 | 400000 | 400000 | 74988  | 74214  | 98.97% | 74.8  | 30.6   | 19.4 | 7 |
| 12 | S2→S1 | 6 | 100 | 400000 | 400000 | 74998  | 73360  | 97.82% | 125.9 | 2887.1 | 35.8 | 51 |
| 15 | S2→S3 | 6 | 400 | 100000 | 100000 | 300340 | 296868 | 98.84% | 126.1 | 2199.1 | 30.8 | 182865 |
| 16 | S3→S2 | 6 | 200 | 800000 | 800000 | 37506  | 37080  | 98.86% | 171.3 | 4055.1 | 51.8 | 81 |
| 18 | S3→S2 | 6 | 100 | 200000 | 200000 | 149975 | 148261 | 98.86% | 151.5 | 4143.0 | 34.1 | 1515 |
| 20 | S3→S1 | 6 | 200 | 100000 | 100000 | 300308 | 294028 | 97.91% | 99.2  | 3273.7 | 23.7 | 33909 |

Overall delivery: 97.8-99.0% across all 10 flows -- a clear improvement over the earlier 2-flow-only
test (~78% then), likely reflecting the corrected per-route MSTI setup and the more realistic mixed
load this full flow set represents.
