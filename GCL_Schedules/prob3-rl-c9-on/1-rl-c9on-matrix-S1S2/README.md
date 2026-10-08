# prob3-rl-c9-on, S1/S2 flows only

A copy of `../1-rl-c9on-matrix` whose `endpoints.json` keeps only the 15 S1<->S2 flows: S3 is not
contacted and sends or receives nothing. `schedule.json`, `basetime.json` and `gcl/` are the full
package's, and the switches ran the full package's gate lists (deployed 2026-10-07). The results
table still lists all 48 schedule flows; the S3 ones show "–".

| run | sw08 gate lists | pcp-6 delivered | sw08 queue drops |
|---|---|---|---|
| `results-2026-10-07` | the package's | 0.3-0.7% | 485k (p2, p5) |
| `results-2026-10-07_2` | all gates open (`sgs 800000 0xFF`), every other switch unchanged | 99.99-100% | none |

So sw08's gate lists in this package are what drop the pcp-6 traffic leaving sw08 toward S1 and
S2; which part of them does it is not yet known (`check_schedule.py` doesn't predict it). With
sw08 open, flow 2 measures 31.9 / 277.0 / 428.8 µs and 75% misses, nearly the 2026-10-01 result,
so that run probably didn't have this package's gate lists on sw08. sw08's original lists were
restored after the second run.
