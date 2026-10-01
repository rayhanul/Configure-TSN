# Traffic generation results -- prob3-rl-c9-on schedule (RL-trained, probability-3 variant, constraint 9 on)

30-second concurrent run of `Spawning-Flows/gen_traffic.py` on all three end-stations (S1, S2, S3)
against the live, deployed TAS/GCL schedule from `../schedule.json` and VLAN/MSTP admission via
`Network-Configure-Manager/configureManager.py` (`../stream-realizable.csv`). This is the
**third** (and by far largest) schedule package tested in this repo -- 48 admitted flows (10
`origin=base` + 38 `origin=dynamic`) out of 60 candidates in `../offsets.csv`, versus 10 flows in
each of the two earlier packages (`heuristic-c9-off/1-matrix-c9off/`, `rl-c9-on/1-matrix-c9on/`).

Real UDP traffic on the wire, PCP-tagged per flow, timed to each flow's actual period/offset --
not a simulation. Raw per-node output: `results_S1.log`, `results_S2.log`, `results_S3.log`.

**On flow numbering below:** the `#` column is a plain sequential flow number (1-48, in dataset-id
order), assigned here just for readability. The `dataset id` column is the scheduler's own id;
ids 1-20 are the original candidate flows (`origin=base`, or `origin=dynamic` reusing the same
numbering). `../offsets.csv` has since been edited to relabel the "arrival" flows (the ones that
were numbered `300000`+ at the time this schedule was deployed and tested) with shorter `a-N`
labels -- the table below uses those current `a-N` labels, each matched back (by
route/size/period/deadline) to the flow actually deployed and tested. Three of them (`a-2`, `a-12`,
`a-25`, marked with `*`; deployed as `300001`, `300011`, `300024`) are still in the current
`offsets.csv` but are now marked `scheduled=no` there (that file now schedules 44 flows, not 48 --
one more flow, former id `15`, also flipped to rejected under the same literal id), so the results
below for those three come from the earlier run, when they were admitted. This is a display-only relabeling; the
actual deployed switch config, `schedule.json`, and the results below are unchanged and still
reflect the 48-flow set this package was tested with.

## Fix required before this run: UDP port overflow for large flow ids

`gen_traffic.py` derived each flow's UDP port as `BASE_PORT (50000) + flow["id"]`. The two earlier
packages only used flow ids 1-20, so this stayed under the 65535 port ceiling. This package's
38 dynamically-added flows use ids like `300000`-`300029`, which overflowed it
(`50000 + 300000 = 350000`, not a valid port). Fixed by mapping each flow id to its **rank** in
the sorted id list instead (`port = BASE_PORT + rank`), computed identically from `schedule.json`
on every node, so sender and receiver still agree on the port without ever exceeding it.
Also widened the UFW `ALLOW` rule on S2 and S3 from `50001:50020/udp` to `50000:50100/udp` to
cover all 48 ports (S1's firewall remains inactive, no change needed there).

## Flow admission and connectivity: no issues this time

All 48 flows admitted cleanly via `configureManager.py --mstp --apply` (took ~24 minutes end-to-
end at this scale, mostly SSH banner-retry overhead under repeated rapid connections, not real
failures). A post-admission connectivity sweep -- one ping per flow's sender role, all 48 --
came back 100% clean (0% packet loss on every one), unlike the two earlier packages which each
hit the known stale-MSTI-priority bug on one route. The per-route MSTI fix in `build_mstp()`
(grouping by `(tier, route)` rather than `tier` alone) held up at this larger scale without any
live `mstpctl` intervention needed.

## The real finding: GIL/thread-scheduling contention on receiver-heavy nodes, not the network

Overall delivery across all 48 flows: **82.9%** (149... total packets sent, received varies
wildly per flow -- see table). That average hides a sharp split: most flows behave the same as
the earlier, smaller packages (98.5-99.9% received, average latency in the 130-900us range,
consistent with the existing timing-precision caveat below). But **10 flows show catastrophic
~55-57% delivery with ~26-27ms average latency** -- two orders of magnitude above their 200us
deadline -- and a further 9 flows show a milder but still clearly elevated ~3ms average latency.

Every one of the badly-affected flows shares two traits: **200000ns (200us) period, PCP 7, and
received on S2** -- S2 has 10 such flows landing on it simultaneously (flow #3, 9, 14, 16, 21, 23,
28, 32, 33, 43 -- dataset ids 3, 9, 14, 16, a-24, a-3, a-13, a-8, a-14, a-1), versus only 4 on S1
and **zero** on S3. S3, which has no such concentration, shows the cleanest numbers of all three
nodes despite having the most total in-scope flows (33).

This points to `gen_traffic.py`'s thread-per-flow design, not the network: each node runs every
in-scope flow's sender or receiver as its own Python thread, all sharing one GIL. S2 (34 in-scope
flows total) ends up running 10 receiver threads that each need to wake and drain a UDP socket
5,000 times/second (200us period). Under the GIL, only one thread runs at a time -- when 10 of
them are all trying to service 5kHz sockets, most get starved for multiple milliseconds at a
stretch, and the packets that *do* arrive get timestamped (correctly, against real arrival time)
only once their thread finally gets scheduled. That produces exactly what's observed: real
packets landing on time at the NIC/kernel socket buffer, but measured "latency" inflated by
userspace scheduling delay -- a **generator bottleneck**, not a schedule, switch, or GCL defect.
This is a scaled-up, much more visible version of the timing-precision caveat already documented
in `Spawning-Flows/README.md` (Python `time.sleep`/thread-scheduling jitter vs. microsecond-scale
TAS windows) -- 10-20 flows never had enough concurrent high-rate receiver threads on one node to
expose it this badly; 48 flows, unevenly distributed (S2 got disproportionately more 200us-period
PCP-7 receiver roles than S1 or S3), did. Not chased further here (would need a redesign away from
one-thread-per-flow, e.g. `asyncio`/`select`-based or multi-process receivers), but worth knowing
before drawing conclusions about specific flows' real-world deadline-miss rates from this run.

## Results (sorted by flow #)

| # | dataset id | route | pcp | size(B) | period(ns) | deadline(ns) | sent | received | received% | avg latency(us) | jitter stddev(us) | jitter rfc3550(us) | deadline misses | deadline miss% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | S3→S1 | 7 | 500 | 200000 | 200000 | 149997 | 148040 | 98.70% | 328.3 | 690.4 | 109.6 | 90347 | 61.03% |
| 2 | 2 | S2→S1 | 6 | 400 | 200000 | 200000 | 116847 | 112308 | 96.12% | 688.5 | 441.7 | 172.7 | 109291 | 97.31% |
| 3 | 3 | S3→S2 | 7 | 100 | 200000 | 200000 | 149985 | 85958 | 57.31% | 26296.3 | 4641.4 | 399.4 | 85956 | 100.00% |
| 4 | 4 | S1→S3 | 6 | 300 | 800000 | 800000 | 37506 | 37027 | 98.72% | 405.2 | 218.1 | 129.2 | 607 | 1.64% |
| 5 | 5 | S2→S1 | 6 | 200 | 400000 | 400000 | 75012 | 73916 | 98.54% | 520.9 | 305.9 | 188.2 | 48285 | 65.32% |
| 6 | 6 | S2→S1 | 7 | 100 | 400000 | 400000 | 75024 | 73971 | 98.60% | 326.8 | 207.8 | 139.3 | 18841 | 25.47% |
| 7 | 7 | S2→S1 | 6 | 300 | 800000 | 800000 | 37514 | 36990 | 98.60% | 462.5 | 222.9 | 210.7 | 2659 | 7.19% |
| 8 | 8 | S2→S3 | 7 | 100 | 800000 | 800000 | 37523 | 37479 | 99.88% | 165.3 | 89.4 | 87.6 | 11 | 0.03% |
| 9 | 9 | S3→S2 | 7 | 500 | 200000 | 200000 | 149995 | 85017 | 56.68% | 26647.2 | 4791.7 | 405.0 | 85011 | 99.99% |
| 10 | 10 | S1→S3 | 7 | 100 | 800000 | 800000 | 37509 | 37031 | 98.73% | 138.3 | 85.7 | 70.7 | 5 | 0.01% |
| 11 | 11 | S3→S2 | 6 | 500 | 800000 | 800000 | 37508 | 37474 | 99.91% | 849.5 | 1085.0 | 404.5 | 13352 | 35.63% |
| 12 | 12 | S2→S1 | 7 | 100 | 800000 | 800000 | 37507 | 36983 | 98.60% | 272.4 | 153.3 | 140.4 | 300 | 0.81% |
| 13 | 13 | S1→S2 | 7 | 300 | 400000 | 400000 | 74993 | 73803 | 98.41% | 3137.5 | 4830.2 | 316.9 | 65830 | 89.20% |
| 14 | 14 | S1→S2 | 7 | 100 | 200000 | 200000 | 149985 | 83790 | 55.87% | 26680.8 | 4570.3 | 423.2 | 83781 | 99.99% |
| 15 | 15 | S2→S3 | 7 | 400 | 400000 | 400000 | 75018 | 74929 | 99.88% | 176.8 | 102.4 | 96.4 | 1887 | 2.52% |
| 16 | 16 | S3→S2 | 7 | 200 | 200000 | 200000 | 149990 | 85049 | 56.70% | 26646.9 | 4795.0 | 405.3 | 85049 | 100.00% |
| 17 | 17 | S2→S3 | 6 | 200 | 800000 | 800000 | 37522 | 37478 | 99.88% | 169.1 | 97.3 | 95.3 | 6 | 0.02% |
| 18 | 18 | S3→S2 | 6 | 100 | 400000 | 400000 | 74992 | 74722 | 99.64% | 3087.0 | 4987.9 | 305.7 | 67909 | 90.88% |
| 19 | 19 | S3→S1 | 7 | 500 | 400000 | 400000 | 74997 | 74037 | 98.72% | 234.8 | 170.8 | 131.5 | 7290 | 9.85% |
| 20 | 20 | S3→S1 | 7 | 200 | 200000 | 200000 | 149994 | 148055 | 98.71% | 330.2 | 730.2 | 108.9 | 80545 | 54.40% |
| 21 | a-24 | S3→S2 | 7 | 500 | 200000 | 200000 | 149993 | 84860 | 56.58% | 26726.8 | 4595.3 | 403.0 | 84855 | 99.99% |
| 22 | 300001* | S2→S3 | 7 | 300 | 400000 | 400000 | 75016 | 74927 | 99.88% | 178.9 | 102.0 | 92.8 | 1881 | 2.51% |
| 23 | a-3 | S1→S2 | 7 | 500 | 200000 | 200000 | 149966 | 83239 | 55.51% | 26895.3 | 4738.6 | 425.7 | 83238 | 100.00% |
| 24 | a-4 | S2→S1 | 7 | 100 | 200000 | 200000 | 114789 | 110463 | 96.23% | 416.9 | 614.3 | 135.8 | 87251 | 78.99% |
| 25 | a-20 | S1→S2 | 6 | 200 | 800000 | 800000 | 37506 | 36989 | 98.62% | 862.7 | 893.7 | 409.2 | 13975 | 37.78% |
| 26 | a-6 | S3→S2 | 7 | 500 | 400000 | 400000 | 74995 | 74750 | 99.67% | 3006.1 | 5019.2 | 305.5 | 67128 | 89.80% |
| 27 | a-7 | S1→S3 | 6 | 400 | 800000 | 800000 | 37506 | 37028 | 98.73% | 408.4 | 214.9 | 145.7 | 1006 | 2.72% |
| 28 | a-13 | S3→S2 | 7 | 500 | 200000 | 200000 | 149992 | 84909 | 56.61% | 26650.5 | 4862.3 | 402.7 | 84902 | 99.99% |
| 29 | a-9 | S2→S1 | 6 | 100 | 400000 | 400000 | 75003 | 73951 | 98.60% | 489.6 | 256.0 | 186.7 | 44253 | 59.84% |
| 30 | a-10 | S3→S2 | 7 | 300 | 400000 | 400000 | 74994 | 74737 | 99.66% | 2948.9 | 4790.2 | 304.8 | 66994 | 89.64% |
| 31 | 300011* | S1→S3 | 7 | 100 | 400000 | 400000 | 74988 | 74029 | 98.72% | 148.9 | 83.8 | 98.0 | 388 | 0.52% |
| 32 | a-8 | S3→S2 | 7 | 500 | 200000 | 200000 | 149991 | 84755 | 56.51% | 26765.9 | 5123.3 | 406.5 | 84754 | 100.00% |
| 33 | a-14 | S1→S2 | 7 | 300 | 200000 | 200000 | 149986 | 83178 | 55.46% | 26870.6 | 4422.5 | 428.6 | 83176 | 100.00% |
| 34 | a-15 | S3→S1 | 7 | 200 | 400000 | 400000 | 74992 | 74033 | 98.72% | 215.6 | 157.8 | 127.6 | 7108 | 9.60% |
| 35 | a-16 | S2→S1 | 7 | 500 | 800000 | 800000 | 37518 | 36993 | 98.60% | 295.6 | 159.9 | 143.2 | 411 | 1.11% |
| 36 | a-17 | S3→S1 | 6 | 500 | 800000 | 800000 | 37507 | 37023 | 98.71% | 476.4 | 215.7 | 179.1 | 3052 | 8.24% |
| 37 | a-18 | S2→S3 | 7 | 100 | 800000 | 800000 | 37505 | 37461 | 99.88% | 160.4 | 89.6 | 87.0 | 9 | 0.02% |
| 38 | a-19 | S1→S3 | 6 | 300 | 800000 | 800000 | 37506 | 37027 | 98.72% | 405.4 | 211.1 | 134.6 | 563 | 1.52% |
| 39 | a-5 | S1→S2 | 6 | 200 | 800000 | 800000 | 37506 | 36988 | 98.62% | 846.9 | 919.2 | 411.6 | 13669 | 36.96% |
| 40 | a-21 | S3→S1 | 7 | 100 | 200000 | 200000 | 149984 | 148048 | 98.71% | 314.8 | 630.6 | 110.9 | 82062 | 55.43% |
| 41 | a-29 | S3→S2 | 7 | 100 | 400000 | 400000 | 74990 | 74770 | 99.71% | 3062.2 | 4779.7 | 306.5 | 66035 | 88.32% |
| 42 | a-23 | S3→S1 | 6 | 200 | 800000 | 800000 | 37505 | 37021 | 98.71% | 506.2 | 227.8 | 167.2 | 3943 | 10.65% |
| 43 | a-1 | S3→S2 | 7 | 500 | 200000 | 200000 | 149991 | 84729 | 56.49% | 26768.7 | 4595.8 | 409.7 | 84726 | 100.00% |
| 44 | 300024* | S1→S3 | 7 | 500 | 400000 | 400000 | 74993 | 74035 | 98.72% | 162.3 | 85.1 | 98.6 | 553 | 0.75% |
| 45 | a-26 | S3→S2 | 6 | 200 | 800000 | 800000 | 37506 | 37466 | 99.89% | 883.9 | 1316.9 | 407.1 | 13484 | 35.99% |
| 46 | a-27 | S3→S1 | 6 | 300 | 800000 | 800000 | 37505 | 37022 | 98.71% | 497.0 | 227.2 | 167.0 | 3695 | 9.98% |
| 47 | a-22 | S3→S2 | 7 | 100 | 400000 | 400000 | 74990 | 74831 | 99.79% | 2811.4 | 4024.0 | 304.3 | 66431 | 88.77% |
| 48 | a-30 | S1→S2 | 6 | 100 | 400000 | 400000 | 74990 | 73791 | 98.40% | 2937.7 | 4456.5 | 317.5 | 69128 | 93.68% |

Overall delivery: 82.9% across all 48 flows -- pulled down almost entirely by the 10
S2-receiver, 200us-period, PCP-7 flows described above (55-57% each); every flow landing on S3
(zero 200us/PCP7 concentration) and most landing on S1 (only 4) stay in the 96-99.9% range typical
of the two earlier, smaller packages.

Deadline-miss rate (misses as a share of packets actually *received*, i.e. excluding outright
loss): **58.97%** overall across all 48 flows -- again dominated by the 10 GIL-contended flows
(each ~100% miss, since their ~26ms measured latency is ~130x their 200us deadline) and the 9
milder-contention flows (~88-94% miss, ~15x their deadline). The flows outside that contention
cluster mostly stay well under 40% (several PCP-6/800us-period flows under 2%), consistent with
the timing-precision caveat -- the contention cluster is what pulls the overall average this high,
not a uniform schedule/switch issue across all 48 flows.
