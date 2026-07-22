# TSN / VLAN Network Configuration Automation

`tsn_configure.py` automates the VLAN configuration of a Time-Sensitive
Networking (TSN) test network from two data files — a list of flows and a
network topology. For every flow it assigns a VLAN, computes the sender and
receiver IP addresses, and generates the exact `ip` / `bridge` commands for the
end stations and for every switch along that flow's route. It can print the
plan (dry-run) or push it to the devices over SSH.

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

# Also generate the MSTP command plan
python3 tsn_configure.py --mstp

# Actually connect over SSH and apply everything
python3 tsn_configure.py --apply --mstp
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
3. **Build end-station commands** for the source and destination (creating the
   VLAN sub-interface, assigning the IP, bringing it up, and setting the
   `egress-qos-map`). This step is skipped for an endpoint that is a switch.
4. **Walk the route** and, at each switch, look up the ingress port (facing the
   previous hop) and egress port (facing the next hop) from that switch's
   `links`, then emit `bridge vlan add` for both ports plus
   `vlan_filtering 1` on the bridge.
5. In `--apply` mode, **SSH into each node and run** its commands (using `sudo`
   for non-root users).

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

| Option              | Description                                                        |
|---------------------|-------------------------------------------------------------------|
| `--csv PATH`        | Flows file (default `stream.csv`)                                 |
| `--topology PATH`   | Topology file (default `network-topology.json`)                  |
| `--apply`           | SSH into the devices and run the commands (otherwise dry-run)     |
| `--mstp`            | Also build/print/apply the MSTP plan                              |
| `--password NODE=SECRET` | Pre-supply a password non-interactively (repeatable)         |

---

## Output and return value

- **Dry-run** prints, per flow: the VLAN, subnet, sender/receiver IPs, the route,
  and every command grouped by device — followed by a summary table.
- **`--apply`** prints an `OK` / `ERR(code)` line per command as it runs.
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