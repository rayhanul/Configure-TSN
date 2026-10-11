# Equal transmitted-packet comparison

Reanalysis of the existing three trials; no additional testbed run. For each flow in each trial, retain all packets launched during activation and select the same number of its most recent transmitted packets before the first CNC command. This matches both the total packet count and the flow composition. Baseline selection boundaries differ slightly by flow. Original full-window results remain in SUMMARY.md.

| Phase | Transmitted packets | Deadline misses | Deadline-miss rate | Lost |
|---|---:|---:|---:|---:|
| before activation | 353,280 | 0 | 0.00% | 0 |
| during activation | 353,280 | 25,959 | 7.35% | 0 |

Suggested caption: Deadline compliance before and during GCL activation, using equal transmitted-packet counts per flow and trial. Results aggregate three transitions from the RL C9-on schedule to the Problem 3 heuristic C9-on schedule on 17 ports across eight switches.

All observed deadline misses occurred on flows 7 and 8, which the replacement schedule does not admit. This comparison therefore includes a changed admission set and does not isolate activation transients. Skipped sender releases are excluded from transmitted-packet counts. The original analysis inferred 64 skipped releases during activation.

Per-flow counts and selected launch-time ranges: equal_count_packets.csv.
