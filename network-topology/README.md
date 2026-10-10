# Network topologies

| file | what it is |
|---|---|
| `network-topology-rtas-2027.json` | the testbed as cabled now: 8 switches in a mesh, 12 switch-to-switch links |
| `network-topology-line-8.json` | **proposed loop-free topology**: the same switches and cables, 5 of them unplugged |
| `network-topology-rtas-2027-line.json` | the same loop-free topology as `network-topology-line-8.json`, named after the RTAS 2027 testbed file |
| `network-topology-rtas-2027-tree.json` | **the testbed as actually recabled** (read off the switches 2026-10-09): loop-free, 7 switch links, `S3 - sw01 - sw03 - sw05 - sw07 - sw08 - sw06 - sw04 - sw02 - S1`, S2 on sw08 port 2, S3 now on sw01 port 2 |
| `network-topology.json` | older 4-switch topology, superseded |

## `network-topology-line-8.json`: no spanning-tree blocking

```
S3 - sw01 - sw02 - sw04 - sw03 - sw06 - sw05 - sw07 - sw08 - S2
             |
             S1
```

A loop-free network has exactly one path between any two switches, so the spanning tree has
nothing to block: every port forwards in every tree. On the mesh, MSTP had to block 5 of the 12
links, and on 2026-10-09 it kept blocking routes the schedules needed (every S2->S3 flow over
sw08-sw06-sw03-sw01, earlier every S2->S1 flow), see
`GCL_Schedules/result-2026-10-08-dataset-testbed-2/SUMMARY_REPORT_2026-10-09.md`.

This one is a single line through all 8 switches, built only from existing cables, with S1, S2,
S3 on the same switch ports as today. Both ends of the line carry an end station (sw01: S3,
sw08: S2), so every switch is on some end-station path:

| end stations | path | switches |
|---|---|---|
| S1 <-> S3 | sw02 - sw01 | 2 |
| S1 <-> S2 | sw02 - sw04 - sw03 - sw06 - sw05 - sw07 - sw08 | 7 |
| S2 <-> S3 | sw08 - sw07 - sw05 - sw06 - sw03 - sw04 - sw02 - sw01 | 8 |

**Recabling: unplug these 5 cables** (nothing new to plug in):

| cable | between |
|---|---|
| sw01 port 4 <-> sw03 port 3 | sw01-sw03 |
| sw02 port 5 <-> sw05 port 5 | sw02-sw05 |
| sw04 port 4 <-> sw05 port 3 | sw04-sw05 |
| sw06 port 2 <-> sw08 port 4 | sw06-sw08 |
| sw06 port 4 <-> sw07 port 5 | sw06-sw07 |

**Trade-offs.** No redundancy: a failed cable splits the network. Every S1<->S2 and S2<->S3
flow shares the middle links (sw04-sw03-sw06-sw05-sw07), so fewer flows fit than on the mesh,
and paths are longer (up to 8 switches = 9 links: 9 x 12.48 us frame slots + 8 x 4.1 us switch
delay = about 145 us best case, within the 200 us shortest period).

**Using it.** Point the tools at the new file (`--topology network-topology/network-topology-line-8.json`
for `configure_gcl.py`, `configureManager.py`, `run_experiment.py`). Schedules must be generated
for it: the current packages use routes over the unplugged links, so build a new testbed dataset
from this topology in RL-TSN (`data/dataset-testbed/generate.py --topology ...`) and run the
pipeline on it. `--mstp` can stay on (harmless); with no loops, the spanning tree blocks nothing.
