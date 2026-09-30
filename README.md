# Configure-TSN

End-to-end pipeline for the 8-switch TTTech TSN testbed: clock sync, VLAN/flow admission,
IEEE 802.1Qbv (GCL/TAS) schedule deployment, and traffic generation against that schedule.

## Topology

- **S1** (`ubuntu@137.99.253.118`) — labeled "Sender" in the topology file, and is the **PTP
  grandmaster**. For the flows currently admitted (below), it is actually the traffic **receiver**
  -- the topology label is about its general role, not this specific flow set.
- **S2** (`jdg24001@137.99.253.167`) — labeled "Receiver", marked **CNC** (this is the orchestration
  node: it has SSH access to every switch and to S1, and is where all the commands below are run
  from unless noted otherwise). It is a **PTP slave**, and for the flows currently admitted, it is
  the traffic **sender**. This machine and the CNC are the same box.
- **sw01-sw08** (`192.168.0.1`-`.8`) — the switch fabric, all reachable by SSH as `root` (no
  password) from the CNC.
- **S3** — in the topology file but not physically present (confirmed via LLDP). Flows involving it
  can't be admitted or exercised until it's connected.

Topology file: `network-topology/network-topology-rtas-2027.json` (has real SSH credentials for
everything above). `network-topology/network-topology.json` is an older, smaller 4-switch topology
superseded by re-cabling -- use the `-rtas-2027` one.

## What to run from the CNC (S2)

Everything except the traffic receiver on S1 runs from here. Run in this order:

### 1. Verify clock sync (should already be running -- see `clock-syncrhonize-ptp/README.md`)
```bash
systemctl status tsn-ptp4l tsn-phc2sys
```
Both `active (running)`, `phc2sys` state `s2` (locked). If not running, see that README's
`install_autostart.sh` section -- don't re-run it blind, it's already installed on both S1 and S2.

### 2. Admit flows (VLAN + MSTP + addressing) with `Network-Configure-Manager/configureManager.py`
```bash
cd Network-Configure-Manager
python3 configureManager.py \
  --topology ../network-topology/network-topology-rtas-2027.json \
  --csv ../GCL_Schedules/heuristic-c9-off/1-matrix-c9off/stream-realizable.csv \
  --endpoints ../GCL_Schedules/heuristic-c9-off/1-matrix-c9off/endpoints.json \
  --mstp            # dry-run first: review the plan before adding --apply
python3 configureManager.py \
  --topology ../network-topology/network-topology-rtas-2027.json \
  --csv ../GCL_Schedules/heuristic-c9-off/1-matrix-c9off/stream-realizable.csv \
  --endpoints ../GCL_Schedules/heuristic-c9-off/1-matrix-c9off/endpoints.json \
  --mstp --apply
```
`--csv` here is a filtered copy of `dataset/1/stream.csv`, containing only the flows that are both
(a) admitted by the schedule and (b) physically realizable (both endpoints present) -- currently
flow ids 5 and 12, both `S2->S1`. See `Spawning-Flows/README.md` for how that filtering was done;
redo it if a different schedule package is used. Check for spanning-tree blocking on the route first
(`mstpctl showport br0` on each switch along the path) -- `--mstp` is needed whenever a flow's route
crosses a link the default CIST has blocked, which is common on this mesh's redundant links.

`--endpoints` writes the file the traffic generator (`Spawning-Flows/gen_traffic.py`) needs for
local iface/IP/peer-IP per flow -- always pass it when admitting flows you intend to exercise.

### 3. Deploy the GCL/TAS schedule to the switches with `deploy-GCL/configure_gcl.py`
```bash
cd ../deploy-GCL
python3 configure_gcl.py \
  --gcl-dir ../GCL_Schedules/heuristic-c9-off/1-matrix-c9off/gcl \
  --topology ../network-topology/network-topology-rtas-2027.json    # dry-run first
python3 configure_gcl.py \
  --gcl-dir ../GCL_Schedules/heuristic-c9-off/1-matrix-c9off/gcl \
  --topology ../network-topology/network-topology-rtas-2027.json --apply
```
This rounds every interval to the switches' real 320ns tick granularity (the schedule itself
assumes 8ns; see that folder's README) and activates every port with one shared PTP-synchronized
basetime. Verify with the same command's own output (`LIVE` on every port) before trusting it --
see that README for the full failure modes this had to work around.

### 4. Run the traffic sender (S2 is the sender for the currently admitted flows)
```bash
cd ../Spawning-Flows
python3 gen_traffic.py \
  --schedule ../GCL_Schedules/heuristic-c9-off/1-matrix-c9off/schedule.json \
  --endpoints ../GCL_Schedules/heuristic-c9-off/1-matrix-c9off/endpoints.json \
  --node S2                              # dry-run first: confirm it lists sender role for id 5, 12
sudo python3 gen_traffic.py \
  --schedule ../GCL_Schedules/heuristic-c9-off/1-matrix-c9off/schedule.json \
  --endpoints ../GCL_Schedules/heuristic-c9-off/1-matrix-c9off/endpoints.json \
  --node S2 --run --duration 30
```
`sudo` is required: one of the admitted flows uses PCP 7, which needs `CAP_NET_ADMIN` to set via
`SO_PRIORITY`. Start the **receiver on S1 first** (next section) -- the sender doesn't wait for it.

## What to run from the sender

For the flows currently admitted, **the sender is S2 -- the same machine as the CNC**, so this is
step 4 above, run locally. This is specific to this flow set (both admitted flows are `S2->S1`); if
a future schedule admits a flow the other direction, that node runs the sender command instead, with
`--node` set to itself. Don't assume "sender" == the node labeled "Sender" in the topology file --
check `endpoints.json`'s `role` field (or just run `gen_traffic.py --node <X>` without `--run` and
read what it prints) for whichever node you're on.

## What to run from the receiver (S1)

S1 doesn't have a checkout of this repo by default -- copy the three files it needs first:
```bash
scp Spawning-Flows/gen_traffic.py \
    GCL_Schedules/heuristic-c9-off/1-matrix-c9off/schedule.json \
    GCL_Schedules/heuristic-c9-off/1-matrix-c9off/endpoints.json \
    ubuntu@137.99.253.118:~/spawning-flows/
```
Then, on S1 itself (or via `ssh ubuntu@137.99.253.118 '...'` from the CNC):
```bash
cd ~/spawning-flows
python3 gen_traffic.py --schedule schedule.json --endpoints endpoints.json --node S1
                        # dry-run first: confirm it lists receiver role for id 5, 12
python3 gen_traffic.py --schedule schedule.json --endpoints endpoints.json \
  --node S1 --run --duration 35    # start this *before* the sender; give it a few extra seconds
```
No `sudo` needed here -- only senders set `SO_PRIORITY`.

**If launching the receiver over SSH from the CNC in the background**, see the gotcha documented in
`Spawning-Flows/README.md`: `cd dir && nohup cmd &` does not reliably detach and will silently block
your script for the command's entire runtime. Use `cd dir; nohup cmd < /dev/null > out.log 2>&1 &`
(`;` not `&&`, and redirect stdin) instead.

## Reading the results

After both sides finish, the receiver (S1) prints per-flow: packets received, min/avg/max one-way
latency, and deadline-miss count. Expect real misses and some loss under this generator -- Python's
scheduling precision (tens-to-hundreds of microseconds) is coarser than these flows' actual TAS-gated
window sizes (a few microseconds per 800us cycle); see `Spawning-Flows/README.md` for what a real
run looked like and what it would take to do better.

## Directory map

| Path | What |
|---|---|
| `network-topology/` | Topology JSON files (real SSH credentials) |
| `clock-syncrhonize-ptp/` | gPTP setup notes + configs; systemd services already installed |
| `Network-Configure-Manager/` | `configureManager.py` -- VLAN/MSTP/addressing per flow |
| `deploy-GCL/` | `configure_gcl.py` -- pushes GCL schedules to switches via `tsntool` |
| `GCL_Schedules/` | Schedule packages (`schedule.json`, `report.md`, `gcl/*.cfg`, per-package data) |
| `Spawning-Flows/` | `gen_traffic.py` -- sends/receives real traffic against an admitted schedule |
| `dataset/` | Original flow-set inputs (`stream.csv` etc.) that produced the schedule packages |
