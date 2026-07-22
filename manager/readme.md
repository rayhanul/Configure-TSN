# TSN / VLAN Network Configuration Automation

`tsn_configure.py` automates the VLAN configuration of a Time-Sensitive
Networking (TSN) test network from two data files — a list of flows and a
network topology. For every flow it assigns a VLAN, computes the sender and
receiver IP addresses, and generates the exact `ip` / `bridge` commands for the
end stations and for every switch along that flow's route. It can print the
plan (dry-run), write a `config.txt` summary, or push the config to the devices
over SSH — and it tracks what it applied so re-runs are safe.

It is **topology-agnostic**: it works for any set of switches, end stations and
links, and for any number of flows. Each flow is configured strictly along the
route given for it in the CSV.

---

## Contents

- [Requirements](#requirements)
- [Quick start](#quick-start)
- [Input files](#input-files)
  - [stream.csv](#streamcsv)
  - [network-topology.json](#network-topologyjson)
- [What the script does](#what-the-script-does)
- [VLAN and IP scheme](#vlan-and-ip-scheme)
- [Passwords](#passwords)
- [Re-running, idempotency and cleanup](#re-running-idempotency-and-cleanup)
- [config.txt output](#configtxt-output)
- [MSTP option](#mstp-option)
- [Command-line options](#command-line-options)
- [Output and return value](#output-and-return-value)
- [Validation and error handling](#validation-and-error-handling)
- [Configurable defaults](#configurable-defaults)
- [Known caveats for this network](#known-caveats-for-this-network)

---

## Requirements

- Python 3.8+
- [`paramiko`](https://pypi.org/project/paramiko/) — **only** needed for the
  `--apply` (real SSH) mode. Dry-run needs nothing beyond the standard library.

```bash
pip install paramiko
```

---

## Quick start

```bash
# Dry-run: print the full configuration plan, change nothing
python3 tsn_configure.py --csv stream.csv --topology network-topology.json

# Write a config.txt summary (flow / vlan / sender / receiver / switch path)
python3 tsn_configure.py --config

# Also generate the MSTP command plan
python3 tsn_configure.py --mstp

# Actually connect over SSH and apply everything (records state for next time)
python3 tsn_configure.py --apply --mstp

# Re-apply safely (removes the previous run's config, then applies)
python3 tsn_configure.py --apply

# Tear down everything the last run configured
python3 tsn_configure.py --reset --apply
```

If `--csv` / `--topology` are omitted they default to `stream.csv` and
`network-topology.json` in the current directory.

---

## Input files

### stream.csv

One row per flow. Columns:

| Column     | Meaning                                                    |
|------------|------------------------------------------------------------|
| `id`       | Flow identifier (may repeat across rows)                   |
| `src`      | Source node name (must exist in the topology)              |
| `dst`      | Destination node name (must exist in the topology)         |
| `route`    | Ordered node list for the path, e.g. `[S1,sw00,sw01,sw03,S2]` |
| `size`     | Frame size (bytes) — carried through, not used for VLANs   |
| `period`   | Period (ns) — metadata                                     |
| `deadline` | Deadline (ns) — metadata                                   |
| `jitter`   | Jitter (ns) — metadata                                     |

Example:

```csv
id,src,dst,route,size,period,deadline,jitter
1,S1, S2,[S1,sw00,sw01,sw03,S2],100,1000000,306400,306400
1,S1, S2,[S1,sw00,sw02,sw03,S2],100,1000000,314800,314800
```

**Note on the `route` field:** it contains commas but is not quoted, so a normal
CSV parser would split it into extra columns. The script reads the route from
between the `[` and `]` brackets, so both quoted and unquoted forms work. The
`size`/`period`/`deadline`/`jitter` fields are read as metadata only; VLAN and IP
assignment does not depend on them.

### network-topology.json

A dictionary keyed by node name. Each node has:

| Field      | Required | Meaning                                                        |
|------------|----------|----------------------------------------------------------------|
| `type`     | yes      | `"sw"` for a switch, anything else (e.g. `"end-station"`) otherwise |
| `ip`       | yes      | Management IP for SSH                                           |
| `username` | yes      | SSH username                                                   |
| `password` | see below| SSH password (or a prompt keyword — see [Passwords](#passwords)) |
| `links`    | yes      | `{ "<port>": "<neighbor node>" }` map                          |

Optional per-node overrides (each falls back to a global default):

| Field         | Applies to    | Default    | Meaning                                      |
|---------------|---------------|------------|----------------------------------------------|
| `iface`       | end stations  | `enp1s0`   | Physical NIC name the VLAN interface rides on |
| `port_prefix` | switches      | `sw0`      | Prefix for local port devices: port `p2` → `sw0p2` |
| `bridge`      | switches      | `br0`      | Bridge name used in `bridge` / `mstpctl` commands |

Example switch and end-station entries:

```json
{
  "sw00": {
    "type": "sw", "ip": "192.168.0.1", "username": "root", "password": "",
    "links": { "p2": "S1", "p3": "S3", "p4": "sw02", "p5": "sw01" }
  },
  "S1": {
    "type": "end-station", "ip": "137.99.253.188", "username": "ubuntu",
    "password": "1234567809", "links": { "p2": "sw00" }
  }
}
```

**Links should be reciprocal.** If `S2` lists `p4: sw03`, then `sw03` must also
list the port that faces `S2` — the script derives a switch's egress port from
that switch's own `links`, so a missing back-link cannot be inferred (see
[Known caveats](#known-caveats-for-this-network)).

---

## What the script does

For each flow, in order:

1. **Validate the route** against the topology (every node exists; every switch
   hop's neighbours resolve to a real port).
2. **Allocate** a VLAN, a `/24` subnet, and the sender/receiver IPs.
3. **Build end-station commands** for the source and destination (removing any
   old VLAN sub-interface, then creating it, assigning the IP, bringing it up,
   and setting the `egress-qos-map`). This step is skipped for an endpoint that
   is a switch.
4. **Walk the route** and, at each switch, look up the ingress port (facing the
   previous hop) and egress port (facing the next hop) from that switch's
   `links`, then emit `bridge vlan add` for both ports plus
   `vlan_filtering 1` on the bridge.
5. In `--apply` mode, **tear down the previous run** (from the saved state),
   **SSH into each node and run** its commands, then **save the new state**.

---

## VLAN and IP scheme

For flow index `n` (0-based):

- **VLAN** = `VLAN_BASE + VLAN_STEP * n` → `10, 20, 30, …` by default. Validated
  against the 1–4094 range.
- **Subnet**:
  - `192.168.<vlan>.0/24` while the VLAN id is ≤ 254 (readable scheme), otherwise
  - `10.<n//256>.<n%256>.0/24` (scalable fallback, so large flow counts never
    collide).
- **Sender IP** = `<subnet>.10`, **Receiver IP** = `<subnet>.11`.

So the first two flows come out as:

| Flow | VLAN | Subnet             | Sender IP       | Receiver IP     |
|------|------|--------------------|-----------------|-----------------|
| 1    | 10   | 192.168.10.0/24    | 192.168.10.10   | 192.168.10.11   |
| 2    | 20   | 192.168.20.0/24    | 192.168.20.10   | 192.168.20.11   |

These values (base, step, host octets, subnet prefix) are all editable at the
top of the script.

---

## Passwords

The `password` field of each node is interpreted as follows:

| Value in JSON                     | Behaviour                                   |
|-----------------------------------|---------------------------------------------|
| `""` (empty string)               | Passwordless login (e.g. root on switches)  |
| a real string, e.g. `"hunter2"`   | Used as-is                                   |
| `"PROMPT"` / `"ASK"` / `"<ask>"` / `"<prompt>"` | Asked for **securely at run time** (hidden input) |
| field omitted entirely            | Also treated as a prompt                     |

Details:

- Prompting uses `getpass`, so nothing is echoed to the terminal.
- Each **host + username** pair is asked only **once**, even if it appears in
  several flows (e.g. two end stations that share an IP and user).
- In `--apply` mode all needed passwords are collected **up front**, before any
  connection opens.
- Dry-run never prompts; it lists which nodes *would* be asked, e.g.
  `Password will be requested at --apply for: S1, sw01`.

For non-interactive / scripted runs, pre-supply passwords with `--password`
(repeatable; `NODE` can be a node name or an IP):

```bash
python3 tsn_configure.py --apply --password S1=mypw --password sw03=rootpw
```

> Security note: passwords passed on the command line are visible to other users
> via the process list. Prefer the interactive prompt where possible and reserve
> `--password` for automation contexts where that is acceptable.

---

## Re-running, idempotency and cleanup

The script is designed to be run repeatedly without leaving stale configuration
behind.

**Idempotent creation.** Each end-station sequence starts with
`ip link del <iface>.<vlan> 2>/dev/null || true`, so re-applying the same config
recreates the interface cleanly instead of failing with *"File exists"*. Switch
`bridge vlan add` is already idempotent.

**State tracking.** After a successful `--apply`, the script writes a state file
(`.tsn_state.json` by default) recording exactly what it configured — which VLAN
sub-interfaces and which `port/vid` memberships. On the **next** `--apply`, it:

1. reads the previous state,
2. tears it down (removing those VLAN interfaces and bridge memberships),
3. applies the new plan,
4. rewrites the state.

This means that if you change routes, VLANs, or flows between runs, the entries
that no longer apply are **removed** rather than left dangling.

**Reset.** `--reset` tears down what a previous run configured. It prefers the
saved state file and falls back to the current plan's teardown if there is none.

```bash
python3 tsn_configure.py --reset            # dry-run: print the teardown plan
python3 tsn_configure.py --reset --apply    # run the teardown and clear the state
```

Teardown commands are tolerant (`2>/dev/null || true`), so removing an entry that
is already gone is harmless.

**Notes / limits:**

- The state file is how the tool knows what to clean up. If you delete
  `.tsn_state.json`, it can no longer remove a prior run's entries automatically
  — run `--reset` first, or simply re-`--apply` your current config (which
  overwrites the relevant ports).
- Use `--state PATH` to choose a different state file, or `--state none` to
  disable state tracking entirely.
- Teardown covers VLAN interfaces and `bridge vlan` memberships. It does **not**
  reset MSTP trees/region or the `vlan_filtering` flag; those persist by design.

---

## config.txt output

`--config` writes a human-readable summary file. With no argument it writes
`config.txt`; pass a path to choose another name.

```bash
python3 tsn_configure.py --config              # -> config.txt
python3 tsn_configure.py --config mynet.txt    # -> mynet.txt
```

Each flow block lists the flow id, source/destination (with management IPs), the
route, the VLAN and subnet, the sender/receiver IPs with their VLAN interface
names, and the per-switch ingress/egress ports carrying that VLAN, followed by a
summary table. Example block:

```
[FLOW 1]
flow_id      = 1
source       = S1  (137.99.253.188)
destination  = S2  (137.99.253.167)
route        = S1 -> sw00 -> sw01 -> sw03 -> S2
vlan         = 10
subnet       = 192.168.10.0/24
sender_ip    = 192.168.10.10   (S1, enp1s0.10)
receiver_ip  = 192.168.10.11   (S2, enp1s0.10)
switch_path  =
    sw00 @ 192.168.0.1 : in=sw0p2  out=sw0p5  vid 10
    sw01 @ 192.168.0.2 : in=sw0p2  out=sw0p4  vid 10
    sw03 @ 192.168.0.4 : in=sw0p3  out=sw0p5  vid 10
```

`--config` can be combined with any other mode (`--config --mstp`,
`--apply --config`, etc.) and is regenerated whenever the CSV or topology changes.

---

## MSTP option

With `--mstp`, the script also emits a Multiple Spanning Tree Protocol plan that
mirrors a one-tree-per-flow scheme:

- On **every switch** on any route: create the MST region, create one tree per
  flow, map each VLAN and its return VLAN (`vlan`, `vlan+1`) to a FID, and bind
  each FID to its MSTI.
- At any switch where the trees **diverge** (different egress ports), apply a high
  `settreeportcost` to the ports used by the *other* trees, forcing each tree onto
  its intended path.
- On the **last switch** of each route, set `settreeprio … 0` to make it the root
  bridge for every MSTI.

Review the return-VLAN mapping (`vlan+1`) against how you actually handle reverse
(destination → source) traffic before applying, and treat the MSTP output as a
starting point for topologies with multiple branch points.

---

## Command-line options

| Option                   | Description                                                        |
|--------------------------|-------------------------------------------------------------------|
| `--csv PATH`             | Flows file (default `stream.csv`)                                 |
| `--topology PATH`        | Topology file (default `network-topology.json`)                  |
| `--apply`                | SSH into the devices and run the commands (otherwise dry-run)     |
| `--mstp`                 | Also build/print/apply the MSTP plan                              |
| `--config [PATH]`        | Write a config.txt summary (default filename `config.txt`)        |
| `--reset`                | Tear down the previous run (dry-run unless combined with `--apply`) |
| `--state PATH`           | State file path (default `.tsn_state.json`; `none` disables it)   |
| `--password NODE=SECRET` | Pre-supply a password non-interactively (repeatable)             |

---

## Output and return value

- **Dry-run** prints, per flow: the VLAN, subnet, sender/receiver IPs, the route,
  and every command grouped by device — followed by a summary table.
- **`--apply`** prints an `OK` / `ERR(code)` line per command as it runs, plus the
  teardown of the previous state and a note that new state was saved.
- The `main()` function returns a machine-readable list, one entry per configured
  flow:

```json
[
  {
    "flow": "1 (id=1)",
    "route": "S1 -> sw00 -> sw01 -> sw03 -> S2",
    "vlan": 10,
    "sender_ip": "192.168.10.10",
    "receiver_ip": "192.168.10.11"
  }
]
```

This is also printed at the end of every run as `return value: …`.

---

## Validation and error handling

- If a flow's route references an unknown node, or a switch has no link to the
  next/previous hop, that **single flow is skipped** with a specific message
  (e.g. `route node 'badnode' is not defined in the topology`) and the remaining
  flows are still configured.
- A route shorter than two nodes, or a VLAN that would fall outside 1–4094, is
  also reported and skipped.

This means one malformed CSV row cannot corrupt the configuration of the others.

---

## Configurable defaults

Set at the top of `tsn_configure.py`:

| Constant              | Default              | Purpose                                  |
|-----------------------|----------------------|------------------------------------------|
| `DEFAULT_IFACE`       | `enp1s0`             | End-station NIC when no `iface` override |
| `DEFAULT_PORT_PREFIX` | `sw0`                | Switch port prefix when no override      |
| `DEFAULT_BRIDGE`      | `br0`                | Bridge name when no override             |
| `DEFAULT_STATE_FILE`  | `.tsn_state.json`    | Where applied config is recorded         |
| `VLAN_BASE`           | `10`                 | VLAN of the first flow                   |
| `VLAN_STEP`           | `10`                 | VLAN increment between flows             |
| `SUBNET_PREFIX`       | `192.168`            | Readable-subnet prefix                   |
| `SENDER_HOST`         | `10`                 | Last octet of the sender IP              |
| `RECEIVER_HOST`       | `11`                 | Last octet of the receiver IP            |
| `EGRESS_QOS_MAP`      | `0:0 1:1 … 7:7`      | VLAN egress QoS (priority) map           |
| `NODE_ALIASES`        | `{"RS": "S2"}`       | Treat a link value as another node name  |

---

## Known caveats for this network

These stem from the sample data and are worth fixing at the source:

1. **`sw03` port to the receiver is ambiguous.** The topology gives `sw03` a
   port `"p5": "RS"` and `RS` is not defined as a node, so an alias `RS → S2` is
   used and the script emits sw03's egress on `sw0p5`. Earlier manual configs
   used `sw0p4`. Confirm the physical port and set `sw03`'s link accordingly
   (e.g. `"p5": "S2"` or `"p4": "S2"`); the script trusts the topology.

2. **Non-reciprocal link.** `S2` lists `p4 → sw03`, but `sw03` has no matching
   back-link to `S2` (only `p5 → RS`). Make links symmetric to avoid relying on
   the alias.

3. **`S1` and `S3` share an IP** (`137.99.253.188`, user `ubuntu`). The current
   flows only use `S1`, so this is harmless now, but a future flow sourced from
   `S3` could not be addressed distinctly over SSH. Give them separate
   management IPs.