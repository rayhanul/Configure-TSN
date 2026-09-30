# TSN / VLAN Network Configuration Automation

`configureManager.py` reads a flow list and a network topology, then
generates and (optionally) applies the VLAN/bridge/MSTP configuration for
every flow's route — any number of switches, end stations, links, or flows.

## Requirements

```bash
pip install paramiko   # only needed for --apply
```

## Quick start

```bash
python3 configureManager.py                          # dry-run: print the plan
python3 configureManager.py --config                 # + write config.txt
python3 configureManager.py --endpoints               # + write endpoints.json
python3 configureManager.py --mstp                    # + build MSTP plan
python3 configureManager.py --apply --mstp             # SSH in and apply
python3 configureManager.py --apply                    # re-apply (tears down previous run first)
python3 configureManager.py --reset --apply             # tear down last run's config
```

`--csv`/`--topology` default to `stream.csv` in the current directory /
`../network-topology/network-topology.json`.




## Configure 

To configure and write configuration:


```
python3 configureManager.py --apply --mstp --endpoints
```

## stream.csv

```
id,src,dst,route,size,period,deadline,jitter
1,S1,S2,[S1->sw00->sw01->sw03->S2],100,1000000,306400,306400
1,S1,S2,[S1->sw00->sw02->sw03->S2],100,1000000,314800,314800
```

- `id` — flow identifier; every row sharing an `id` is an alternate route
  (primary, then backup, ...) for the same `src`→`dst` flow.
- `route` — `[A->B->C]` or `[A,B,C]`, either works.
- `size`/`period`/`deadline`/`jitter` — metadata only, not used for VLAN/IP.

VLAN = `VLAN_STEP * (tier + 1) + flow_index` (tier = 0 for the primary route,
1 for the backup, ...; flow_index = 0-based order the `id` first appears).
Subnet = `192.168.<vlan>.0/24`, sender = `.10`, receiver = `.11`.

## network-topology/network-topology.json

Each link records both ends — the neighbor node and the port on the neighbor
it plugs into. Unconnected switch ports may be left as `{}`. An end station
has a single link object.

```json
{
  "sw01": {
    "type": "sw", "ip": "192.168.0.1", "username": "root", "password": "",
    "links": {
      "p2": { "node": "S1" },
      "p3": {},
      "p5": { "node": "sw02", "port": "p3" }
    }
  },
  "S1": {
    "type": "end-station", "ip": "192.168.0.101", "username": "ubuntu",
    "password": "1234567809", "links": { "node": "sw01", "port": "p2" }
  }
}
```

The older form `"links": { "p2": "S1", "p5": "sw02" }` is still accepted.

On load, every link is checked against the other end (the neighbor must link
back, and a recorded `port` must be the neighbor's port that points back).
Inconsistencies are printed as `[WARN]`; any flow whose route crosses an
inconsistent link is skipped, so a wiring typo can't put a VLAN on the wrong
port.

| Field         | Required | Meaning                                            |
|---------------|----------|-----------------------------------------------------|
| `type`        | yes      | `"sw"` for a switch, anything else = end station    |
| `ip`          | yes      | Management IP for SSH                                |
| `username`    | yes      | SSH username                                         |
| `password`    | yes      | `""` passwordless, a literal password, or `PROMPT`/`ASK`/`<ask>`/`<prompt>` (asked at run time; missing field = also prompted) |
| `links`       | yes      | Switch: `{ "<port>": {"node": "<neighbor>", "port": "<neighbor port>"} }` (`port` optional for end-station neighbors, `{}` = unconnected). End station: `{"node": "<switch>", "port": "<switch port>"}`. Must be reciprocal. |
| `iface`       | no       | End-station NIC (default `enp1s0`)                   |
| `port_prefix` | no       | Switch port prefix (default `sw0`)                   |
| `bridge`      | no       | Bridge name (default `br0`)                          |
| `label`       | no       | Human-readable name, shown in output only             |
| `cnc`         | no       | `true` on at most one node — marks it as the station this tool is run from. That node's commands run **locally** (subprocess) instead of over SSH, avoiding the self-connect timeout many networks hit when a machine SSHes to its own external IP; every other node is still reached over SSH as usual. Also printed in the dry-run header, `config.txt`, and `endpoints.json`. Two `true` nodes → the run fails fast. |

Pre-supply passwords non-interactively: `--password NODE=SECRET` (repeatable).

## Outputs

- **dry-run** (no `--apply`) — prints the plan, changes nothing.
- **`--config [PATH]`** — human-readable summary (default `config.txt`).
- **`--endpoints [PATH]`** — JSON per-node interface/IP map for a traffic-gen
  script (default `endpoints.json`): `{node: {label, management_ip, cnc,
  streams: {stream_name: {role, vlan, iface, ip, peer, peer_ip, route}}}}`.
  Stream names come from `TIER_LABELS` (`objects` = tier 0, `frame` = tier
  1); a node with multiple flows on the same tier gets `_<flow_id>` appended
  to stay unique.
- **`--apply`** — SSHes into each node and runs the commands; tears down the
  previous run first (via `.tsn_state.json`, see `--state`) and saves new
  state after.
- **`--reset [--apply]`** — tears down the last applied run (or the current
  plan if no state file exists). This only ever removes what the tool itself
  tracked or would have created — leftovers from manual or pre-fix config on
  a different port/VLAN won't be touched.
- **`--reset --hard [--apply]`** — ignores the plan/state file entirely and
  instead connects to every node live to discover what's actually there:
  switches via `bridge -j vlan show` (any non-default VLAN on the switch's
  known ports), end stations via `ip -j link show type vlan` (any VLAN
  sub-interface on the configured NIC — the NIC itself is never a candidate,
  since it isn't a VLAN-type link). Use this for a true clean slate when
  stray config exists that the plan-based reset can't see. Unlike every other
  dry-run, this **always connects over SSH** to check current state, even
  without `--apply` — it just won't change anything unless `--apply` is
  also given.
- `main()` returns/prints a JSON list of `{flow, route, vlan, sender_ip,
  receiver_ip}`.

## MSTP (`--mstp`)

One MSTI per path tier (all flows' primary routes → tree 1, all backups →
tree 2, ...): per switch, creates the region/trees, maps each tier's VLANs to
its FID/MSTI, raises `settreeportcost` on any switch where trees diverge, and
sets `settreeprio ... 0` on the last switch of each route. Not covered by
`--reset`, and not undone by anything in this script.

## Command-line options

| Option                   | Description                                                   |
|--------------------------|-----------------------------------------------------------------|
| `--csv PATH`             | Flows file (default `stream.csv`)                              |
| `--topology PATH`        | Topology file (default `../network-topology/network-topology.json`) |
| `--apply`                | SSH in and run (otherwise dry-run)                              |
| `--mstp`                 | Also build/print/apply the MSTP plan                            |
| `--config [PATH]`        | Write config.txt (default `config.txt`)                         |
| `--endpoints [PATH]`     | Write endpoints.json (default `endpoints.json`)                 |
| `--reset`                | Tear down the previous run (dry-run unless combined with `--apply`) |
| `--hard`                 | With `--reset`, discover and remove ALL live VLAN config via SSH instead of only what the plan tracked (always connects, even without `--apply`) |
| `--state PATH`           | State file (default `.tsn_state.json`; `none` disables it)      |
| `--password NODE=SECRET` | Pre-supply a password non-interactively (repeatable)             |

## Validation

- Bad route (unknown node, no port to next/prev hop, too short, or starts/ends
  at a switch) or out-of-range VLAN → that flow is skipped, others still run.
- Two rows sharing an `id` with different `src`/`dst` → whole run stops
  before configuring anything (the CSV itself is inconsistent).
- More than one node marked `"cnc": true` → whole run stops.
