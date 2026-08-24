#!/usr/bin/env python3
"""
tsn_configure.py
----------------
Topology-agnostic TSN / VLAN configuration for the secure-camera project.

Works for:
  * ANY network topology (arbitrary switches / end-stations / links), and
  * ANY number of flows,
each flow being configured strictly along the route given in the CSV.

Inputs
  stream.csv              id,src,dst,route,size,period,deadline,jitter
                          route = ordered node list, e.g. [S1,sw00,sw01,sw03,S2]
  network-topology.json   per node: type, ip, username, password, links{port:neighbor}
                          optional per-node overrides:
                              "iface"       (end-station NIC name,   default enp1s0)
                              "port_prefix" (switch local port name,  default sw0)
                              "bridge"      (switch bridge name,      default br0)

Passwords
  * "password": ""              -> passwordless login (e.g. root switches)
  * "password": "hunter2"       -> used as-is
  * "password": "PROMPT"        -> ask me securely at run time (hidden input).
    field missing entirely       -> also treated as PROMPT.
  Accepted prompt keywords: PROMPT, ASK, <ask>, <prompt> (case-insensitive).
  Each host+user is asked once, even if it appears in several flows.
  For non-interactive runs you can pre-supply them:  --password NODE=secret
  (repeatable). Dry-run never prompts.

For every flow the tool:
  1. validates the route against the topology,
  2. allocates a VLAN + /24 subnet + sender/receiver IPs,
  3. builds sender & receiver end-station commands (skipped if an endpoint is a switch),
  4. walks the route and builds each switch's ingress+egress `bridge vlan add` commands,
  5. optionally pushes it all over SSH,
  6. returns/prints  flow -> {vlan, sender_ip, receiver_ip}.

Run:
    python3 tsn_configure.py                 # dry-run: print the plan
    python3 tsn_configure.py --mstp          # also build the MSTP plan
    python3 tsn_configure.py --apply         # SSH in and run it (pip install paramiko)
"""

import argparse
import getpass
import json
import os
import sys
from dataclasses import dataclass, field

# ---------------------------------------------------------------------------
# Defaults (per-node values in the topology JSON override these)
# ---------------------------------------------------------------------------
DEFAULT_IFACE = "enp1s0"          # end-station physical NIC
DEFAULT_PORT_PREFIX = "sw0"       # topology port "p2" -> switch device "sw0p2"
DEFAULT_BRIDGE = "br0"            # switch bridge name
DEFAULT_STATE_FILE = ".tsn_state.json"   # records what --apply configured

VLAN_STEP = 10                    # spacing between path tiers: 10, 20, 30 ...
SUBNET_PREFIX = "192.168"         # readable subnets: 192.168.<vlan>.0/24
SENDER_HOST = 10                  # sender   = <subnet>.10
RECEIVER_HOST = 11                # receiver = <subnet>.11
EGRESS_QOS_MAP = "0:0 1:1 2:2 3:3 4:4 5:5 6:6 7:7"

# Stream name per path tier, used only in --endpoints output; a tier beyond
# this map (a 3rd+ route for the same flow id) falls back to "path_N".
TIER_LABELS = {0: "objects", 1: "frame"}

# Topology link values that should be treated as another node's name, for
# topologies where a link target isn't spelled the same as the node itself.
NODE_ALIASES = {}

# A password field equal to one of these keywords (or missing entirely) means
# "ask the user at run time" instead of failing. An explicit "" stays passwordless.
PROMPT_KEYWORDS = {"prompt", "ask", "<ask>", "<prompt>", "promt", "<promt>"}
_pw_cache = {}                     # (host, user) -> resolved password
_pw_preset = {}                    # node/host -> password supplied via --password


def needs_prompt(raw):
    """True when the password should be asked for (missing or a keyword)."""
    return raw is None or str(raw).strip().lower() in PROMPT_KEYWORDS


def resolve_password(node, host, user, raw):
    """Return the usable password, prompting once per (host,user) if needed."""
    if node in _pw_preset:
        return _pw_preset[node]
    if host in _pw_preset:
        return _pw_preset[host]
    if not needs_prompt(raw):
        return raw                                   # "" or a real password
    key = (host, user)
    if key not in _pw_cache:
        _pw_cache[key] = getpass.getpass(f"  password for {node} ({user}@{host}): ")
    return _pw_cache[key]


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------
@dataclass
class FlowPlan:
    index: int
    flow_id: str
    src: str
    dst: str
    route: list
    vlan: int
    tier: int
    subnet: str
    sender_ip: str
    receiver_ip: str
    sender_cmds: list = field(default_factory=list)
    receiver_cmds: list = field(default_factory=list)
    switch_cmds: dict = field(default_factory=dict)   # switch -> [cmds]
    switch_hops: dict = field(default_factory=dict)   # switch -> (in_port, out_port)
    last_switch: str = ""

    def summary(self):
        return {
            "flow": f"{self.index} (id={self.flow_id})",
            "route": " -> ".join(self.route),
            "vlan": self.vlan,
            "sender_ip": self.sender_ip,
            "receiver_ip": self.receiver_ip,
        }


# ---------------------------------------------------------------------------
# Loading / parsing
# ---------------------------------------------------------------------------
def load_topology(path):
    with open(path) as f:
        return json.load(f)


def parse_route(raw):
    """Support both '[S1,sw00,sw01,sw03,S2]' and '[S1->sw00->sw01->sw03->S2]'"""
    text = raw.strip().strip("[]")
    if "->" in text:
        parts = [n.strip() for n in text.split("->") if n.strip()]
    else:
        parts = [n.strip() for n in text.split(",") if n.strip()]
    return parts


def load_streams(path):
    """
    The route column is an unquoted, comma-containing list, which a normal CSV
    parser would shred. We split each data line on the [ ] brackets instead:
        <id,src,dst,>[<route>]<,size,period,deadline,jitter>
    (Quoting the route field in the CSV would also work; this is robust to both.)
    """
    flows = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.lower().startswith("id,"):
                continue
            if "[" not in line or "]" not in line:
                continue
            before, rest = line.split("[", 1)
            inside, _after = rest.split("]", 1)
            head = [c.strip() for c in before.split(",") if c.strip()]
            if len(head) < 3:
                continue
            flows.append({"id": head[0], "src": head[1], "dst": head[2],
                          "route": parse_route(inside)})
    return flows


# ---------------------------------------------------------------------------
# Topology helpers (all per-node, no globals baked in)
# ---------------------------------------------------------------------------
def canon(node):
    """Resolve an alias to its canonical node name."""
    return NODE_ALIASES.get(node, node)


def node_attr(topology, node, key, default):
    return topology.get(node, {}).get(key, default)


def is_switch(topology, node):
    return topology.get(node, {}).get("type") == "sw"


def find_cnc(topology):
    """
    Return the name of the node marked "cnc": true (the station this tool is
    meant to be run from), or None if none is marked. At most one node may
    be marked cnc — the topology can't name two orchestration stations.
    """
    candidates = [n for n, d in topology.items() if d.get("cnc")]
    if len(candidates) > 1:
        raise ValueError(
            f"more than one node is marked \"cnc\": true ({', '.join(candidates)}) "
            f"— only one node can be the CNC."
        )
    return candidates[0] if candidates else None


def resolve_port(topology, switch, neighbor):
    """Port key on `switch` whose link points at `neighbor` (alias-aware)."""
    neighbor = canon(neighbor)
    for port, node in topology[switch]["links"].items():
        if canon(node) == neighbor:
            return port
    raise ValueError(
        f"'{switch}' has no port linking to '{neighbor}'. "
        f"Links present: {topology[switch]['links']}. "
        f"Add the missing link to network-topology.json (or a NODE_ALIASES entry)."
    )


def validate_route(topology, flow):
    """Every node must exist; every switch hop's neighbours must be resolvable."""
    route = flow["route"]
    if len(route) < 2:
        raise ValueError(f"route too short: {route}")
    for n in route:
        if canon(n) not in topology:
            raise ValueError(f"route node '{n}' is not defined in the topology.")
    if is_switch(topology, canon(route[0])) or is_switch(topology, canon(route[-1])):
        raise ValueError(
            f"route {route}: the first and last node must be end-stations, not "
            f"switches (a switch has no single 'ingress+egress' pair when it's "
            f"the flow's own endpoint)."
        )
    for i, node in enumerate(route):
        if is_switch(topology, canon(node)):
            resolve_port(topology, canon(node), route[i - 1])
            resolve_port(topology, canon(node), route[i + 1])


# ---------------------------------------------------------------------------
# VLAN / subnet allocation (scales to thousands of flows)
# ---------------------------------------------------------------------------
def assign_vlans(flows):
    """
    Pair each CSV row with a VLAN and a "tier" (0 = primary route, 1 = backup
    route, 2 = 2nd backup, ...), grouping rows by their shared 'id' column —
    each id is one logical flow with an ordered list of candidate routes.

    VLAN = VLAN_STEP * (tier + 1) + flow_index, so with two logical flows and
    the default VLAN_STEP=10, flow 0's routes land on VLAN 10 (tier 0) and 20
    (tier 1), and flow 1's routes land on 11 (tier 0) and 21 (tier 1). Every
    route sharing a tier shares one VLAN pool decade, so a fixed MSTP tree per
    tier (see build_mstp) can carry every flow's primary paths on one tree and
    every flow's backup paths on another, regardless of flow count.
    """
    flow_index, tier_counter, src_dst, out = {}, {}, {}, []
    for f in flows:
        fid = f["id"]
        if fid not in flow_index:
            flow_index[fid] = len(flow_index)
            tier_counter[fid] = 0
            src_dst[fid] = (f["src"], f["dst"])
        elif src_dst[fid] != (f["src"], f["dst"]):
            raise ValueError(
                f"stream id '{fid}' is used by both {src_dst[fid]} and "
                f"({f['src']}, {f['dst']}) — every row sharing an id must be "
                f"an alternate route for the SAME (src, dst) logical flow."
            )
        tier = tier_counter[fid]
        tier_counter[fid] += 1
        vlan = VLAN_STEP * (tier + 1) + flow_index[fid]
        out.append((f, vlan, tier))
    return out


def allocate(vlan):
    if not (1 <= vlan <= 4094):
        raise ValueError(f"VLAN {vlan} out of range 1..4094; lower VLAN_STEP "
                         f"or reduce the number of flows/tiers.")
    if vlan <= 254:                                  # readable scheme
        net = f"{SUBNET_PREFIX}.{vlan}"
    else:                                            # scalable fallback
        net = f"10.{vlan // 256}.{vlan % 256}"
    return f"{net}.0/24", f"{net}.{SENDER_HOST}", f"{net}.{RECEIVER_HOST}"


# ---------------------------------------------------------------------------
# Command builders
# ---------------------------------------------------------------------------
def endstation_cmds(iface, vlan, ip):
    v = f"{iface}.{vlan}"
    return [
        f"ip link del {v} 2>/dev/null || true",   # idempotent: drop it if it exists
        f"ip link add link {iface} name {v} type vlan id {vlan}",
        f"ip addr add {ip}/24 dev {v}",
        f"ip link set dev {v} up",
        f"ip link set {v} type vlan egress-qos-map {EGRESS_QOS_MAP}",
        f"ip link set dev {iface} up",
    ]


def build_plan(topology, flow, vlan, tier, index):
    validate_route(topology, flow)
    subnet, sender_ip, receiver_ip = allocate(vlan)
    route = [canon(n) for n in flow["route"]]

    plan = FlowPlan(index=index + 1, flow_id=flow["id"], src=canon(flow["src"]),
                    dst=canon(flow["dst"]), route=route, vlan=vlan, tier=tier,
                    subnet=subnet, sender_ip=sender_ip, receiver_ip=receiver_ip)

    # end-station config only when the endpoint is actually an end station
    if not is_switch(topology, plan.src):
        plan.sender_cmds = endstation_cmds(
            node_attr(topology, plan.src, "iface", DEFAULT_IFACE), vlan, sender_ip)
    if not is_switch(topology, plan.dst):
        plan.receiver_cmds = endstation_cmds(
            node_attr(topology, plan.dst, "iface", DEFAULT_IFACE), vlan, receiver_ip)

    switches = [n for n in route if is_switch(topology, n)]
    plan.last_switch = switches[-1] if switches else ""

    for i, node in enumerate(route):
        if not is_switch(topology, node):
            continue
        in_port = resolve_port(topology, node, route[i - 1])
        out_port = resolve_port(topology, node, route[i + 1])
        plan.switch_hops[node] = (in_port, out_port)

        prefix = node_attr(topology, node, "port_prefix", DEFAULT_PORT_PREFIX)
        bridge = node_attr(topology, node, "bridge", DEFAULT_BRIDGE)
        plan.switch_cmds[node] = [
            f"bridge vlan add dev {prefix}{in_port} vid {vlan}",
            f"bridge vlan add dev {prefix}{out_port} vid {vlan}",
            f"ip link set dev {bridge} type bridge vlan_filtering 1",
        ]
    return plan


# ---------------------------------------------------------------------------
# MSTP (optional): one MSTI per path tier (all flows' primary routes share
# tree 1, all their backup routes share tree 2, etc); auto branch/root
# detection
# ---------------------------------------------------------------------------
def build_mstp(plans, topology, region="mstp_test", region_rev=1):
    all_switches = sorted({s for p in plans for s in p.switch_cmds})
    per_switch = {s: [] for s in all_switches}

    def bridge(s):
        return node_attr(topology, s, "bridge", DEFAULT_BRIDGE)

    def prefix(s):
        return node_attr(topology, s, "port_prefix", DEFAULT_PORT_PREFIX)

    tiers = sorted({p.tier for p in plans})
    tree_of_tier = {t: i + 1 for i, t in enumerate(tiers)}   # tier -> MSTI (1-based)
    vlans_by_tree = {tree_of_tier[t]: sorted({p.vlan for p in plans if p.tier == t})
                     for t in tiers}

    for s in all_switches:
        b = bridge(s)
        cmds = [f"mstpctl setmstconfid {b} {region_rev} {region}",
                f"mstpctl showmstconfid {b}"]
        for tree in vlans_by_tree:
            cmds.append(f"mstpctl createtree {b} {tree}")
        for tree, vlans in vlans_by_tree.items():
            cmds.append(f"mstpctl setvid2fid {b} {tree}:{','.join(str(v) for v in vlans)}")
        for tree in vlans_by_tree:
            cmds.append(f"mstpctl setfid2mstid {b} {tree}:{tree}")
        per_switch[s].extend(cmds)

    # force-route: at any switch where trees diverge, penalise the egress
    # ports used by *other* trees so each tree takes its intended path.
    for s in all_switches:
        egress_by_tree = {}
        for p in plans:
            if s not in p.switch_hops:
                continue
            egress_by_tree.setdefault(tree_of_tier[p.tier], set()).add(p.switch_hops[s][1])
        if len(egress_by_tree) > 1:
            all_out_ports = {port for ports in egress_by_tree.values() for port in ports}
            for tree, my_ports in egress_by_tree.items():
                for other_port in all_out_ports - my_ports:
                    per_switch[s].append(
                        f"mstpctl settreeportcost {bridge(s)} "
                        f"{prefix(s)}{other_port} {tree} 5000000")

    # root bridge for every MSTI on the last switch of each route
    for s in {p.last_switch for p in plans if p.last_switch}:
        for tree in vlans_by_tree:
            per_switch[s].append(f"mstpctl settreeprio {bridge(s)} {tree} 0")

    return per_switch


# ---------------------------------------------------------------------------
# Node enumeration / passwords
# ---------------------------------------------------------------------------
def involved_nodes(plans, mstp_plan=None):
    """Every node the tool would SSH into for this run."""
    nodes = set()
    for p in plans:
        if p.sender_cmds:
            nodes.add(p.src)
        if p.receiver_cmds:
            nodes.add(p.dst)
        nodes.update(p.switch_cmds)
    if mstp_plan:
        nodes.update(mstp_plan)
    return nodes


def prompt_nodes(plans, topology, mstp_plan=None):
    """Nodes whose password will be requested interactively."""
    return sorted(n for n in involved_nodes(plans, mstp_plan)
                  if n not in _pw_preset
                  and topology[n]["ip"] not in _pw_preset
                  and needs_prompt(topology[n].get("password")))


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------
def print_plan(plans, topology, mstp_plan=None, cnc=None):
    if cnc:
        print(f"CNC (run this tool from here): {cnc} @ {topology[cnc]['ip']}\n")
    for p in plans:
        print("=" * 72)
        tier_label = "primary" if p.tier == 0 else f"backup #{p.tier}"
        print(f"FLOW {p.index}  (id={p.flow_id}, {tier_label})   {p.src} -> {p.dst}   "
              f"VLAN {p.vlan}   subnet {p.subnet}")
        print(f"  route      : {' -> '.join(p.route)}")
        print(f"  sender  IP : {p.sender_ip}   ({p.src})")
        print(f"  receiver IP: {p.receiver_ip}   ({p.dst})")
        if p.sender_cmds:
            print(f"\n  [{p.src}] sender:")
            for c in p.sender_cmds:
                print(f"      sudo {c}")
        if p.receiver_cmds:
            print(f"\n  [{p.dst}] receiver:")
            for c in p.receiver_cmds:
                print(f"      sudo {c}")
        for sw, cmds in p.switch_cmds.items():
            in_p, out_p = p.switch_hops[sw]
            pre = node_attr(topology, sw, "port_prefix", DEFAULT_PORT_PREFIX)
            print(f"\n  [{sw} @ {topology[sw]['ip']}]  "
                  f"in={pre}{in_p} out={pre}{out_p}:")
            for c in cmds:
                print(f"      {c}")
        print()

    if mstp_plan:
        print("#" * 72 + "\n# MSTP plan (per switch)\n" + "#" * 72)
        for sw, cmds in mstp_plan.items():
            print(f"\n  [{sw} @ {topology[sw]['ip']}]")
            for c in cmds:
                print(f"      {c}")

    print("=" * 72 + "\nSUMMARY  (flow -> vlan / sender / receiver)\n" + "=" * 72)
    print(f"{'flow':<12}{'vlan':<6}{'sender_ip':<18}{'receiver_ip':<18}route")
    for p in plans:
        s = p.summary()
        print(f"{s['flow']:<12}{s['vlan']:<6}{s['sender_ip']:<18}"
              f"{s['receiver_ip']:<18}{s['route']}")

    asked = prompt_nodes(plans, topology, mstp_plan)
    if asked:
        print("\nPassword will be requested at --apply for: " + ", ".join(asked))


def write_config(plans, topology, path, cnc=None):
    """Write a human-readable config.txt with flow / vlan / sender / receiver info."""
    def ip(n):
        return topology[n]["ip"]

    def iface_of(node, cmds, vlan):
        if not cmds:                       # endpoint is a switch, no VLAN sub-iface
            return "(switch, no end-station interface)"
        base = node_attr(topology, node, "iface", DEFAULT_IFACE)
        return f"{base}.{vlan}"

    lines = [
        "# TSN / VLAN Network Configuration",
        "# Generated by configureManager.py",
        f"# Flows configured: {len(plans)}",
    ]
    if cnc:
        lines.append(f"# CNC (run this tool from here): {cnc} @ {ip(cnc)}")
    lines += ["=" * 72, ""]
    for p in plans:
        lines += [
            f"[FLOW {p.index}]",
            f"flow_id      = {p.flow_id}",
            f"source       = {p.src}  ({ip(p.src)})",
            f"destination  = {p.dst}  ({ip(p.dst)})",
            f"route        = {' -> '.join(p.route)}",
            f"vlan         = {p.vlan}",
            f"subnet       = {p.subnet}",
            f"sender_ip    = {p.sender_ip}   "
            f"({p.src}, {iface_of(p.src, p.sender_cmds, p.vlan)})",
            f"receiver_ip  = {p.receiver_ip}   "
            f"({p.dst}, {iface_of(p.dst, p.receiver_cmds, p.vlan)})",
            "switch_path  =",
        ]
        for sw in p.switch_cmds:
            in_p, out_p = p.switch_hops[sw]
            pre = node_attr(topology, sw, "port_prefix", DEFAULT_PORT_PREFIX)
            lines.append(
                f"    {sw} @ {ip(sw)} : in={pre}{in_p}  out={pre}{out_p}  vid {p.vlan}")
        lines.append("")

    lines += ["=" * 72, "SUMMARY",
              f"{'flow':<8}{'vlan':<6}{'sender_ip':<18}{'receiver_ip':<18}route"]
    for p in plans:
        lines.append(f"{p.index:<8}{p.vlan:<6}{p.sender_ip:<18}"
                     f"{p.receiver_ip:<18}{' -> '.join(p.route)}")
    lines.append("")

    with open(path, "w") as f:
        f.write("\n".join(lines))
    print(f"Wrote config to {path}")


def tier_label(tier):
    return TIER_LABELS.get(tier, f"path_{tier + 1}")


def build_endpoints(plans, topology):
    """
    Per-node VLAN interface/IP info, keyed by stream name, for a traffic-gen
    script to load directly: which local interface+IP to bind for a given
    stream, and the peer IP to send to. A node that only receives (e.g. a
    single receiver fed by several senders) gets one entry per (sender,
    stream) pair since it holds several VLAN interfaces at once.

    Keys default to the short form ("objects", "S1_objects", ...); if the
    same node sources or receives more than one flow id on the same tier
    (e.g. two separate logical flows both originating at S1), the flow id is
    appended to keep every key unique instead of silently overwriting.
    """
    nodes = {}
    sender_ids, receiver_ids = {}, {}
    for p in plans:
        stream = tier_label(p.tier)
        if p.sender_cmds:
            sender_ids.setdefault((p.src, stream), set()).add(p.flow_id)
        if p.receiver_cmds:
            receiver_ids.setdefault((p.dst, p.src, stream), set()).add(p.flow_id)

    def entry(node):
        d = topology[node]
        return nodes.setdefault(node, {
            "label": d.get("label", node),
            "management_ip": d["ip"],
            "cnc": bool(d.get("cnc", False)),
            "streams": {},
        })

    for p in plans:
        stream = tier_label(p.tier)
        if p.sender_cmds:
            iface = node_attr(topology, p.src, "iface", DEFAULT_IFACE)
            key = stream if len(sender_ids[(p.src, stream)]) == 1 else f"{stream}_{p.flow_id}"
            entry(p.src)["streams"][key] = {
                "role": "sender",
                "vlan": p.vlan,
                "iface": f"{iface}.{p.vlan}",
                "ip": p.sender_ip,
                "peer": p.dst,
                "peer_ip": p.receiver_ip,
                "route": " -> ".join(p.route),
            }
        if p.receiver_cmds:
            iface = node_attr(topology, p.dst, "iface", DEFAULT_IFACE)
            base = f"{p.src}_{stream}"
            key = base if len(receiver_ids[(p.dst, p.src, stream)]) == 1 else f"{base}_{p.flow_id}"
            entry(p.dst)["streams"][key] = {
                "role": "receiver",
                "vlan": p.vlan,
                "iface": f"{iface}.{p.vlan}",
                "ip": p.receiver_ip,
                "peer": p.src,
                "peer_ip": p.sender_ip,
                "route": " -> ".join(p.route),
            }
    return nodes


def write_endpoints_json(plans, topology, path):
    with open(path, "w") as f:
        json.dump(build_endpoints(plans, topology), f, indent=2)
    print(f"Wrote endpoint config to {path}")


# ---------------------------------------------------------------------------
# Teardown / state tracking (idempotent re-runs + stale cleanup)
# ---------------------------------------------------------------------------
def build_teardown(plans, topology):
    """
    Return {node: {"host","user","cmds":[...]}} that removes exactly what this
    plan creates: the VLAN sub-interfaces and the bridge VLAN memberships.
    Commands are tolerant (won't fail if the entry is already gone).
    """
    nodes = {}

    def add(node, cmd):
        d = topology[node]
        e = nodes.setdefault(node, {"host": d["ip"], "user": d["username"], "cmds": []})
        if cmd not in e["cmds"]:
            e["cmds"].append(cmd)

    for p in plans:
        if p.sender_cmds:
            iface = node_attr(topology, p.src, "iface", DEFAULT_IFACE)
            add(p.src, f"ip link del {iface}.{p.vlan} 2>/dev/null || true")
        if p.receiver_cmds:
            iface = node_attr(topology, p.dst, "iface", DEFAULT_IFACE)
            add(p.dst, f"ip link del {iface}.{p.vlan} 2>/dev/null || true")
        for sw in p.switch_cmds:
            in_p, out_p = p.switch_hops[sw]
            pre = node_attr(topology, sw, "port_prefix", DEFAULT_PORT_PREFIX)
            for port in (in_p, out_p):
                add(sw, f"bridge vlan del dev {pre}{port} vid {p.vlan} 2>/dev/null || true")
    return nodes


def discover_stray_switch_vlans(query, ports):
    """
    Query the switch's live `bridge -j vlan show` (via `query(cmd) -> stdout`,
    local or SSH) and return {port: [vids]} (the default VLAN 1 excluded)
    restricted to `ports` — the switch's known port devices, e.g.
    {"sw0p2", "sw0p3", ...}.
    """
    out = query("bridge -j vlan show")
    try:
        data = json.loads(out)
    except ValueError:
        return {}
    found = {}
    for entry in data:
        port = entry.get("ifname")
        if port not in ports:
            continue
        vids = [v["vlan"] for v in entry.get("vlans", [])
                if isinstance(v, dict) and v.get("vlan", 1) != 1]
        if vids:
            found[port] = vids
    return found


def discover_stray_endstation_vlans(query, iface):
    """
    Query the node's live `ip -j link show type vlan` (via `query(cmd) ->
    stdout`, local or SSH) and return the names of any VLAN sub-interfaces
    riding on `iface`. Filtering on `type vlan` means this can only ever
    match 802.1Q sub-interfaces (e.g. enp1s0.10) — the physical NIC itself
    is a different link type and is never a candidate.
    """
    out = query("ip -j link show type vlan")
    try:
        data = json.loads(out)
    except ValueError:
        return []
    return [e["ifname"] for e in data
            if e.get("link") == iface and e.get("ifname", "").startswith(f"{iface}.")]


def build_hard_teardown(topology, nodes, cnc=None):
    """
    For each of `nodes`, discover ALL VLAN configuration actually present
    right now — not just what the current CSV/topology plan would have
    created — then build teardown commands for everything found. Use this to
    clean up leftovers from manual or pre-fix configuration this tool never
    tracked in its state file. `cnc` (if any) is queried locally instead of
    over SSH, same as everywhere else.
    """
    teardown = {}
    for node in nodes:
        d = topology[node]
        host, user = d["ip"], d["username"]
        pw = resolve_password(node, host, user, d.get("password"))
        if node == cnc:
            query = lambda cmd, u=user, p=pw: local_query(cmd, u, p)
        else:
            query = lambda cmd, h=host, u=user, p=pw: ssh_query(h, u, p, cmd)
        cmds = []
        if is_switch(topology, node):
            prefix = node_attr(topology, node, "port_prefix", DEFAULT_PORT_PREFIX)
            ports = {f"{prefix}{p}" for p in d.get("links", {})}
            for port, vids in discover_stray_switch_vlans(query, ports).items():
                for vid in vids:
                    cmds.append(f"bridge vlan del dev {port} vid {vid} 2>/dev/null || true")
        else:
            iface = node_attr(topology, node, "iface", DEFAULT_IFACE)
            for sub in discover_stray_endstation_vlans(query, iface):
                cmds.append(f"ip link del {sub} 2>/dev/null || true")
        if cmds:
            teardown[node] = {"host": host, "user": user, "cmds": cmds}
    return teardown


def save_state(path, teardown):
    with open(path, "w") as f:
        json.dump(teardown, f, indent=2)


def load_state(path):
    if path and os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return {}


def run_teardown(teardown, topology, label="teardown", cnc=None):
    """Execute a teardown dict, locally for `cnc` and over SSH for everyone else."""
    for node, e in teardown.items():
        host, user = e["host"], e["user"]
        raw = topology.get(node, {}).get("password")  # None -> prompt
        pw = resolve_password(node, host, user, raw)
        print(f"-- {label}: {node} ({'local' if node == cnc else host})")
        if node == cnc:
            run_local(e["cmds"], user, pw)
        else:
            ssh_run(host, user, pw, e["cmds"])


def print_teardown(teardown, header):
    print("#" * 72 + f"\n# {header}\n" + "#" * 72)
    for node, e in teardown.items():
        print(f"\n  [{node} @ {e['host']}]")
        for c in e["cmds"]:
            print(f"      {c}")


# ---------------------------------------------------------------------------
# SSH execution
# ---------------------------------------------------------------------------
def ssh_run(host, user, password, commands):
    import paramiko
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=user, password=password or None,
                   look_for_keys=False, allow_agent=False, timeout=15)
    try:
        for cmd in commands:
            full = cmd if user == "root" else f"sudo -S -p '' {cmd}"
            stdin, stdout, stderr = client.exec_command(full)
            if user != "root" and password:
                stdin.write(password + "\n"); stdin.flush()
            rc = stdout.channel.recv_exit_status()
            out, err = stdout.read().decode().strip(), stderr.read().decode().strip()
            print(f"    [{host}] {'OK ' if rc == 0 else f'ERR({rc})'} {cmd}")
            if out:
                print(f"        stdout: {out}")
            if err and rc != 0:
                print(f"        stderr: {err}")
    finally:
        client.close()


def ssh_query(host, user, password, cmd):
    """Run a single read-only command over SSH and return its stdout text."""
    import paramiko
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=user, password=password or None,
                   look_for_keys=False, allow_agent=False, timeout=15)
    try:
        full = cmd if user == "root" else f"sudo -S -p '' {cmd}"
        stdin, stdout, stderr = client.exec_command(full)
        if user != "root" and password:
            stdin.write(password + "\n"); stdin.flush()
        stdout.channel.recv_exit_status()
        return stdout.read().decode()
    finally:
        client.close()


# ---------------------------------------------------------------------------
# Local execution — for a node marked "cnc": true, meaning this script is
# itself running on that machine. SSHing to your own external IP often fails
# (NAT hairpin isn't supported on many networks), so the CNC's own commands
# run as a local subprocess instead of over the network.
# ---------------------------------------------------------------------------
def run_local(commands, user, password):
    import subprocess
    needs_sudo = user != "root"
    for cmd in commands:
        full = f"sudo -S -p '' {cmd}" if needs_sudo else cmd
        proc = subprocess.run(full, shell=True, capture_output=True, text=True,
                              input=f"{password}\n" if needs_sudo and password else None)
        print(f"    [local] {'OK ' if proc.returncode == 0 else f'ERR({proc.returncode})'} {cmd}")
        if proc.stdout.strip():
            print(f"        stdout: {proc.stdout.strip()}")
        if proc.stderr.strip() and proc.returncode != 0:
            print(f"        stderr: {proc.stderr.strip()}")


def local_query(cmd, user, password):
    """Run a single read-only command locally and return its stdout text."""
    import subprocess
    needs_sudo = user != "root"
    full = f"sudo -S -p '' {cmd}" if needs_sudo else cmd
    proc = subprocess.run(full, shell=True, capture_output=True, text=True,
                          input=f"{password}\n" if needs_sudo and password else None)
    return proc.stdout


def apply_plan(plans, topology, mstp_plan=None, state_path=DEFAULT_STATE_FILE, cnc=None):
    def creds(n):
        d = topology[n]
        return d["ip"], d["username"], resolve_password(
            n, d["ip"], d["username"], d.get("password"))

    def exec_node(n, cmds):
        host, user, pw = creds(n)
        if n == cnc:
            run_local(cmds, user, pw)
        else:
            ssh_run(host, user, pw, cmds)

    # Ask for every needed password up front, before opening any connection.
    asked = prompt_nodes(plans, topology, mstp_plan)
    if asked:
        print(f"Enter passwords for {len(asked)} node(s) "
              f"(input is hidden; shared host+user asked once):")
        for n in asked:
            creds(n)          # triggers the getpass prompt and caches it
        print()

    # Remove whatever a previous --apply configured (idempotent + clears stale).
    prior = load_state(state_path)
    if prior:
        print("### Tearing down previous configuration (from "
              f"{state_path}) ###")
        run_teardown(prior, topology, label="remove old", cnc=cnc)
        print()

    for p in plans:
        print(f"\n### FLOW {p.index}  VLAN {p.vlan} ###")
        if p.sender_cmds:
            print(f"-- sender {p.src}" + ("  (local)" if p.src == cnc else ""))
            exec_node(p.src, p.sender_cmds)
        if p.receiver_cmds:
            print(f"-- receiver {p.dst}" + ("  (local)" if p.dst == cnc else ""))
            exec_node(p.dst, p.receiver_cmds)
        for sw, cmds in p.switch_cmds.items():
            print(f"-- switch {sw}" + ("  (local)" if sw == cnc else ""))
            exec_node(sw, cmds)

    if mstp_plan:
        print("\n### MSTP ###")
        for sw, cmds in mstp_plan.items():
            print(f"-- {sw}" + ("  (local)" if sw == cnc else ""))
            exec_node(sw, cmds)

    # Record what we just configured so the next run can clean it up.
    if state_path:
        save_state(state_path, build_teardown(plans, topology))
        print(f"\nState saved to {state_path} "
              f"(used to tear down on the next run).")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(description="Topology-agnostic TSN/VLAN config")
    ap.add_argument("--csv", default="stream.csv")
    ap.add_argument("--topology", default="network-topology.json")
    ap.add_argument("--apply", action="store_true", help="SSH in and run (else dry-run)")
    ap.add_argument("--mstp", action="store_true", help="also build the MSTP plan")
    ap.add_argument("--config", nargs="?", const="config.txt", default=None,
                    metavar="PATH",
                    help="write a config.txt summary (flow/vlan/sender/receiver). "
                         "PATH optional, defaults to config.txt")
    ap.add_argument("--endpoints", nargs="?", const="endpoints.json", default=None,
                    metavar="PATH",
                    help="write a JSON file mapping each node's VLAN interface/IP "
                         "per stream (objects/frame/...), for a traffic-gen script "
                         "to load directly. PATH optional, defaults to endpoints.json")
    ap.add_argument("--password", action="append", default=[], metavar="NODE=SECRET",
                    help="pre-supply a password non-interactively (repeatable). "
                         "NODE may be a node name or an IP.")
    ap.add_argument("--reset", action="store_true",
                    help="tear down what a previous run configured. With --apply it "
                         "runs the teardown; without, it just prints it.")
    ap.add_argument("--hard", action="store_true",
                    help="with --reset, discover and remove ALL VLAN config found "
                         "live over SSH instead of only what the current CSV/topology "
                         "plan would have created: on switches, any non-default VLAN "
                         "on the switch's known ports; on end stations, any VLAN "
                         "sub-interface riding on the configured NIC (never the NIC "
                         "itself). Always connects over SSH to check, even without "
                         "--apply; nothing changes unless --apply is also given.")
    ap.add_argument("--state", default=DEFAULT_STATE_FILE, metavar="PATH",
                    help=f"state file recording applied config (default "
                         f"{DEFAULT_STATE_FILE}); use 'none' to disable")
    args = ap.parse_args()
    if args.hard and not args.reset:
        ap.error("--hard only applies together with --reset")
    state_path = None if args.state.lower() == "none" else args.state

    for item in args.password:
        if "=" not in item:
            ap.error(f"--password expects NODE=SECRET, got '{item}'")
        node, pw = item.split("=", 1)
        _pw_preset[node.strip()] = pw

    topology = load_topology(args.topology)
    flows = load_streams(args.csv)

    try:
        cnc = find_cnc(topology)
        vlan_plan = assign_vlans(flows)
    except ValueError as e:
        print(f"[FATAL] {e}", file=sys.stderr)
        return []

    plans = []
    for i, (flow, vlan, tier) in enumerate(vlan_plan):
        try:
            plans.append(build_plan(topology, flow, vlan, tier, i))
        except ValueError as e:
            print(f"[SKIP] flow {i + 1} (id={flow.get('id')}) route "
                  f"{flow.get('route')}: {e}", file=sys.stderr)

    if not plans and not args.reset:
        print("No configurable flows.", file=sys.stderr)
        return []

    # --reset: tear down the previous run's config (prefer saved state, else
    # fall back to the teardown for the current plan) and stop.
    if args.reset:
        if args.hard:
            nodes = sorted(topology)
            asked = sorted(n for n in nodes
                           if n not in _pw_preset
                           and topology[n]["ip"] not in _pw_preset
                           and needs_prompt(topology[n].get("password")))
            if asked:
                print(f"Enter passwords for {len(asked)} node(s) to query live "
                      f"state (input is hidden; shared host+user asked once):")
                for n in asked:
                    d = topology[n]
                    resolve_password(n, d["ip"], d["username"], d.get("password"))
                print()
            print(f"Querying {len(nodes)} node(s) live for --hard reset "
                  f"({cnc + ' locally, ' if cnc else ''}the rest over SSH; "
                  f"this connects even without --apply)...")
            teardown = build_hard_teardown(topology, nodes, cnc)
        else:
            teardown = load_state(state_path) or build_teardown(plans, topology)
        if not teardown:
            print("Nothing to reset.")
            return []
        if args.apply:
            run_teardown(teardown, topology, label="reset", cnc=cnc)
            if state_path and os.path.exists(state_path):
                os.remove(state_path)
                print(f"\nCleared {state_path}.")
        else:
            print_teardown(teardown, "RESET plan (dry-run) — use --apply to run it")
        return []

    mstp_plan = build_mstp(plans, topology) if args.mstp else None
    if args.apply:
        apply_plan(plans, topology, mstp_plan, state_path, cnc)
    else:
        print_plan(plans, topology, mstp_plan, cnc)
    if args.config:
        write_config(plans, topology, args.config, cnc)
    if args.endpoints:
        write_endpoints_json(plans, topology, args.endpoints)
    return [p.summary() for p in plans]


if __name__ == "__main__":
    result = main()
    print("\nreturn value:", json.dumps(result, indent=2))