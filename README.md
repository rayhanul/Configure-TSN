# Configure-TSN

End-to-end pipeline for the 8-switch TTTech TSN testbed: clock sync, IEEE 802.1Qbv (GCL/TAS)
schedule deployment, VLAN/flow admission, and real traffic generation against that schedule.

## Topology

- **S1** (`ubuntu@137.99.253.118`) -- end-station, PTP grandmaster.
- **S2** (`jdg24001@137.99.253.167`) -- end-station, marked **CNC** in the topology file: it has
  SSH access to every switch and to S1/S3, and is where every command below is run from unless
  noted otherwise. PTP slave.
- **S3** (`jdg24001@137.99.252.240`, "Kefan PC") -- end-station, PTP slave, onboarded later than
  S1/S2 (SSH key `~/.ssh/id_ed25519_s3`).
- **sw01-sw08** (`192.168.0.1`-`.8`) -- the switch fabric, all reachable by SSH as `root` (no
  password) from the CNC.

Which node sends and which receives is **per-flow**, decided by each schedule package's own data
(a node can be a sender for one flow and a receiver for another in the same run) -- never assume
a node's role; read it off `endpoints.json` (below) or `gen_traffic.py`'s dry-run output.

Topology file: `network-topology/network-topology-rtas-2027.json` (real SSH credentials for
everything above). `network-topology/network-topology.json` is an older, smaller 4-switch topology
superseded by re-cabling -- don't use it for anything live.

## Pipeline overview

Each schedule package under `GCL_Schedules/<package>/<variant>/` carries its own
`offsets.csv`/`schedule.json`/`gcl/*.cfg`, produced by an external scheduler (not in this repo).
Everything below operates on **one package at a time** -- set a shell variable once and reuse it:

```bash
PKG=GCL_Schedules/prob3-rl-c9-on/1-rl-c9on-matrix   # swap for whichever package you're running
```

| # | Step | Command (below) | Reads | Writes |
|---|---|---|---|---|
| 0 | Verify clock sync | `systemctl status` | -- | -- |
| 1 | Filter admitted flows | `awk` one-liner | `$PKG/offsets.csv` | `$PKG/stream-realizable.csv` |
| 2 | Deploy GCL/TAS schedule (do this **before** step 3) | `deploy-GCL/configure_gcl.py` | `$PKG/gcl/*.cfg` | live switch gate config (no file) |
| 3 | Admit flows (VLAN + MSTP + addressing) | `Network-Configure-Manager/configureManager.py` | `$PKG/stream-realizable.csv` | `$PKG/endpoints.json`, `Network-Configure-Manager/.tsn_state.json` |
| 4 | Verify connectivity (optional but recommended) | ad-hoc ping sweep | `$PKG/endpoints.json` | -- |
| 5 | Push generator + schedule to each remote end-station | SFTP | `Spawning-Flows/gen_traffic.py`, `$PKG/schedule.json`, `$PKG/endpoints.json` | copies under `/tmp/spawning-flows-test/` on S1/S3 |
| 6 | Run traffic concurrently on S1, S2, S3 | `gen_traffic.py --run` | files from step 5 | per-node log (`run_<NODE>.log`) |
| 7 | Collect + write results | pull logs, parse | `run_<NODE>.log` from each node | `$PKG/results/results-<date>/results_<NODE>.log`, `.../results.md` (`Spawning-Flows/run_experiment.py` does steps 4-7) |

Step 2 must run **before** step 3: the switches' GCL/TAS gates should already be live before you
open up VLAN paths onto them, so admitted traffic is gated correctly from the moment it can flow.

## Step 0 -- verify clock sync

```bash
systemctl status tsn-ptp4l tsn-phc2sys
```
Both `active (running)` on every node, `phc2sys` state `s2` (locked). Already installed on
S1/S2/S3 -- see `time-sync-gptp/README.md` if it isn't running; `sudo ./gptp.sh verify` checks
sub-microsecond sync.

## Step 1 -- filter the package's admitted flows

`offsets.csv` lists every candidate flow the scheduler considered, admitted or not (`scheduled`
column). Build the filtered CSV `configureManager.py` actually consumes:

```bash
tr -d '\r' < $PKG/offsets.csv | \
  awk -F, 'NR==1{print "id,src,dst,route,size,period,deadline,jitter"; next}
           $10=="yes" {print $1","$2","$3",["$4"],"$5","$6","$7","$8}' \
  > $PKG/stream-realizable.csv
```
Strip `\r` first -- CRLF line endings in some packages' CSVs silently break the `$10=="yes"`
field match otherwise. **Output:** `$PKG/stream-realizable.csv`, consumed directly by step 3.

## Step 2 -- deploy the GCL/TAS schedule to the switches

```bash
cd deploy-GCL
python3 configure_gcl.py --gcl-dir ../$PKG/gcl \
  --topology ../network-topology/network-topology-rtas-2027.json            # dry-run first
python3 configure_gcl.py --gcl-dir ../$PKG/gcl \
  --topology ../network-topology/network-topology-rtas-2027.json --apply
cd ..
```
Rounds every interval to the switches' real 320ns tick granularity (some packages' `hw.t_tick_ns`
is wrong), and activates every port under one shared PTP-synchronized basetime. **Output:** no
file -- the command's own final check (compares `tsntool st rdacl` against `rdocl`, prints `LIVE`
per port) is the artifact; don't trust a run you didn't see finish with `LIVE` on every port. See
`deploy-GCL/README.md` for the failure modes this had to work around. This step is independent of
which end-stations are physically present -- deploy the full schedule regardless; idle TAS windows
for an absent node's flows are harmless.

## Step 3 -- admit flows (VLAN + MSTP + addressing)

```bash
cd Network-Configure-Manager
python3 configureManager.py \
  --topology ../network-topology/network-topology-rtas-2027.json \
  --csv ../$PKG/stream-realizable.csv \
  --endpoints ../$PKG/endpoints.json \
  --mstp                          # dry-run first: review the plan before adding --apply
python3 configureManager.py \
  --topology ../network-topology/network-topology-rtas-2027.json \
  --csv ../$PKG/stream-realizable.csv \
  --endpoints ../$PKG/endpoints.json \
  --mstp --apply
cd ..
```
`--mstp` is needed whenever any flow's route crosses a link the default CIST has blocked -- common
on this mesh's redundant links; always pass it unless you've specifically checked otherwise.
Non-CNC nodes prompt for a password on first use of a host; pass `--password NODE=secret`
(e.g. `--password S3=...`) to supply it non-interactively -- **never commit a real password to a
file**, pass it inline on the command line only. At this scale (dozens of flows) expect many
"Error reading SSH protocol banner" retries in the output -- that's sshd throttling rapid
reconnects, not a real failure; `ssh_connect()` retries with backoff automatically. The run isn't
done until you see `State saved to .tsn_state.json` in the output.

**Outputs:**
- `$PKG/endpoints.json` -- per-node, per-flow role/iface/IP/peer-IP/route. Step 5/6 need this.
- `Network-Configure-Manager/.tsn_state.json` -- records what was configured, for teardown
  (`python3 configureManager.py --reset`, or `--reset --hard` to also sweep any VLAN config not in
  the saved state).

After admitting a **new** package, sanity-check connectivity (step 4) before assuming step 3
succeeded everywhere -- MSTP root-election edge cases can leave one specific route blocked even
when the command reports no errors.

## Step 4 -- verify connectivity (recommended)

One ping per flow's sender role is enough to catch a blocked route before burning time on traffic
generation. From the CNC, using `configureManager.py`'s own `ssh_connect` (it already knows how to
reach every node -- keys first, then password, then SSH "none" auth):

```python
import sys, json, subprocess
sys.path.insert(0, "Network-Configure-Manager")
import configureManager as cm

topo = json.load(open("network-topology/network-topology-rtas-2027.json"))
ep = json.load(open("$PKG/endpoints.json"))
PW = {"S1": "<S1 sudo password>", "S3": "<S3 sudo password>"}  # S2 is the local CNC, no SSH needed

for node in ["S1", "S2", "S3"]:
    client = None if node == "S2" else cm.ssh_connect(topo[node]["ip"], topo[node]["username"], PW.get(node, ""))
    for name, s in ep[node]["streams"].items():
        if s["role"] != "sender":
            continue
        cmd = f"ping -I {s['iface']} -c 2 -W 2 {s['peer_ip']}"
        if client is None:
            rc = subprocess.run(cmd, shell=True, capture_output=True).returncode
        else:
            _, stdout, _ = client.exec_command(cmd)
            rc = stdout.channel.recv_exit_status()
        print(node, s["flow_id"], "OK" if rc == 0 else "FAIL")
    if client:
        client.close()
```
If any flow shows `FAIL`, check spanning-tree state on its route
(`mstpctl showtreeport br0 <tree>` on each switch along the way) -- see `Network-Configure-Manager`'s
known-issue note on stale MSTI root priority below. **Output:** none persisted -- this is a live
check; fix and re-run rather than trusting a stale result.

## Step 5 -- push the generator to each remote end-station

The CNC (S2) runs `gen_traffic.py` locally from the repo directly. S1 and S3 need their own copy
(they don't have a checkout of this repo) -- push it once per package via SFTP (works fine on
end-stations; switches don't support SFTP, irrelevant here):

```python
import sys
sys.path.insert(0, "Network-Configure-Manager")
import configureManager as cm

files = [("Spawning-Flows/gen_traffic.py", "gen_traffic.py"),
         ("$PKG/schedule.json", "schedule.json"),
         ("$PKG/endpoints.json", "endpoints.json")]
for node, host, user, pw in [("S1", "137.99.253.118", "ubuntu", "<S1 password>"),
                              ("S3", "137.99.252.240", "jdg24001", "<S3 password>")]:
    client = cm.ssh_connect(host, user, pw)
    sftp = client.open_sftp()
    for local, remote_name in files:
        sftp.put(local, f"/tmp/spawning-flows-test/{remote_name}")
    sftp.close()
    client.close()
```
Re-run this every time `schedule.json`/`endpoints.json` change (new package, or re-admitted
flows) -- a stale copy on S1/S3 silently tests the wrong schedule. **Output:** identical copies of
the three files under `/tmp/spawning-flows-test/` on S1 and S3 (create the directory once with
`mkdir -p` if it doesn't exist yet).

One-time per node, if its UFW firewall is active (`sudo ufw status`): open the UDP port range
`gen_traffic.py` uses (`50000` + up to the flow count, e.g. `50000:50100` comfortably covers up to
100 flows) --
```bash
sudo ufw allow 50000:50100/udp comment 'gen_traffic.py flow ports'
```
S1's firewall has been inactive throughout this project; S2 and S3 both needed this the first time
each acted as a receiver.

## Step 6 -- run traffic generation concurrently

Always dry-run first on every node (no `--run`) and check the printed sender/receiver role list
matches what you expect before spending a real run:
```bash
python3 Spawning-Flows/gen_traffic.py --schedule $PKG/schedule.json --endpoints $PKG/endpoints.json --node S2
```
Then launch all three **together** (order doesn't matter -- each node runs both sender and
receiver threads for its own in-scope flows). `sudo` is required wherever any in-scope flow uses
PCP 7 (needs `CAP_NET_ADMIN` for `SO_PRIORITY`); harmless to always use it.

From the CNC, local (S2):
```bash
nohup sudo python3 Spawning-Flows/gen_traffic.py \
  --schedule $PKG/schedule.json --endpoints $PKG/endpoints.json \
  --node S2 --run --duration 30 < /dev/null > /tmp/run_S2.log 2>&1 &
```
Remote (S1, S3) -- **use `;` between `cd` and the backgrounded command, never `&&`** (see gotcha
below), and pipe the sudo password for nodes that need one:
```python
# via cm.ssh_connect(...) as in step 5, per node:
cmd = ("cd /tmp/spawning-flows-test; echo '<password>' | nohup sudo -S -p '' python3 gen_traffic.py "
       "--schedule schedule.json --endpoints endpoints.json --node S1 --run --duration 30 "
       "> run_S1.log 2>&1 &")
client.exec_command(cmd)
```
Wait for the duration to elapse, then confirm every node actually exited (`pgrep -af gen_traffic`
on each -- empty means done) before trusting the logs. **Check for a double-launch first**
(`pgrep -af gen_traffic` before you start) -- a leftover process from a previous run causes a
`bind(): Address already in use` on the new one's receiver threads. **Output:** `/tmp/run_S2.log`
on S2 (CNC, local path); `/tmp/spawning-flows-test/run_S1.log` / `run_S3.log` on those nodes.

## Step 7 -- collect and write results

Pull the two remote logs back via SFTP, then parse all three into the results table:
```python
import sys
sys.path.insert(0, "Network-Configure-Manager")
import configureManager as cm

for node, host, user, pw in [("S1", "137.99.253.118", "ubuntu", "<pw>"), ("S3", "137.99.252.240", "jdg24001", "<pw>")]:
    client = cm.ssh_connect(host, user, pw)
    sftp = client.open_sftp()
    sftp.get(f"/tmp/spawning-flows-test/run_{node}.log", f"$PKG/results/results_{node}.log")
    sftp.close(); client.close()
# cp /tmp/run_S2.log $PKG/results/results_S2.log
```
Each log's `Summary:` section has one line per in-scope flow: `id=<id> sender: N sent` or
`id=<id> receiver: N received, latency ns min/avg/max=..., jitter ns stddev/rfc3550=...,
deadline=...ns, misses=...`. Cross-reference a flow's sender-side `sent` count (from whichever
node sent it) against its receiver-side stats (from whichever node received it) using
`schedule.json`'s flow list (`pcp`/`size`/`period`/`deadline`/`route`) -- there's no ready-made
script for this merge in the repo yet; see `GCL_Schedules/prob3-rl-c9-on/1-rl-c9on-matrix/results/results-2026-09-30/results.md`
for the exact table format and regex approach used there (`sender_re`/`recv_re` over the three log
files, joined by flow id). **Output:** `$PKG/results/results_S1.log` / `results_S2.log` /
`results_S3.log` (raw copies) and `$PKG/results/results-<date>/results.md` (the merged table + narrative).

## Known gotchas

- **SSH backgrounding**: `cd dir && nohup cmd &` backgrounds the *whole* `cd && cmd` as one
  subshell job that does **not** detach -- it keeps the SSH channel open and blocks for the
  command's entire runtime. Use `cd dir; nohup cmd < /dev/null > log 2>&1 &` (`;`, and redirect
  stdin) instead. Full discussion: `Spawning-Flows/README.md`.
- **Stale MSTI root priority**: `configureManager.py`'s `build_mstp()` assigns each distinct
  `(tier, route)` pair its own MSTI and sets `settreeprio(tree, 0)` on the intended root switch --
  but doesn't reset priority on a switch that held priority-0 for that same *numeric* tree ID from
  an earlier, different schedule package (where that number meant a different route). If a newly
  admitted flow's route is unexpectedly blocked, check `mstpctl showtreeport br0 <tree>` on
  switches along it; fix live with `mstpctl settreeprio br0 <tree> 8` on whichever switch wrongly
  holds priority 0 (8 is `mstpctl`'s priority *step*, not the raw value). This is a known,
  unpatched gap -- flagged here, not fixed in code.
- **UDP port range**: `gen_traffic.py` maps each flow id to a port by its *rank* in the sorted id
  list (`BASE_PORT + rank`), not `BASE_PORT + id` -- some packages use large synthetic ids
  (e.g. `300000`+) that would overflow the 65535 port ceiling otherwise. This is already handled;
  no action needed unless you're modifying the generator itself.
- **Timing precision**: Python `time.sleep`/thread scheduling achieves tens-to-hundreds of
  microseconds of jitter, coarser than these flows' actual TAS-gated window sizes (a few
  microseconds per 800us cycle) -- expect real, nonzero deadline misses; this is the generator's
  own limit, not a schedule or switch defect. At larger flow counts, a *further* effect shows up:
  many high-rate (short-period) receiver threads sharing one Python process's GIL on the same node
  can starve each other by milliseconds -- see the "GIL/thread-scheduling contention" section in
  `GCL_Schedules/prob3-rl-c9-on/1-rl-c9on-matrix/results/results-2026-09-30/results.md` for a worked example and how
  to recognize it (delivery% collapses specifically for the node with the most concurrent
  high-rate receivers, while other nodes stay normal).
- **Git push**: this environment has no credential helper configured for
  `https://github.com/...` -- pushing needs to be done manually, or the remote switched to SSH.

## Directory map

| Path | What |
|---|---|
| `network-topology/` | Topology JSON files (real SSH credentials) |
| `time-sync-gptp/` | gPTP (802.1AS) setup, install and sync verification for end stations and switches |
| `Network-Configure-Manager/` | `configureManager.py` -- VLAN/MSTP/addressing per flow; `.tsn_state.json` (teardown state) |
| `deploy-GCL/` | `configure_gcl.py` -- pushes GCL schedules to switches via `tsntool` |
| `GCL_Schedules/` | Schedule packages (`offsets.csv`, `schedule.json`, `report.md`, `gcl/*.cfg`, per-package `stream-realizable.csv`/`endpoints.json`/`results/`) |
| `Spawning-Flows/` | `gen_traffic.py` -- sends/receives real traffic against an admitted schedule |
| `dataset/` | Original flow-set inputs (`stream.csv` etc.) that produced some schedule packages |
