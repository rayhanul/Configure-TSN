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
import sys
from dataclasses import dataclass, field

# ---------------------------------------------------------------------------
# Defaults (per-node values in the topology JSON override these)
# ---------------------------------------------------------------------------
DEFAULT_IFACE = "enp1s0"          # end-station physical NIC
DEFAULT_PORT_PREFIX = "sw0"       # topology port "p2" -> switch device "sw0p2"
DEFAULT_BRIDGE = "br0"            # switch bridge name

VLAN_BASE = 10                    # 1st flow -> VLAN 10
VLAN_STEP = 10                    # 2nd -> 20, 3rd -> 30 ...  (must keep vlan <= 4094)
SUBNET_PREFIX = "192.168"         # readable subnets: 192.168.<vlan>.0/24
SENDER_HOST = 10                  # sender   = <subnet>.10
RECEIVER_HOST = 11                # receiver = <subnet>.11
EGRESS_QOS_MAP = "0:0 1:1 2:2 3:3 4:4 5:5 6:6 7:7"

# Topology link values that should be treated as another node's name.
# (Your topology has sw03 "p5":"RS"; the routes use "S2".)
NODE_ALIASES = {"RS": "S2"}

# A password field equal to one of these keywords (or missing entirely) means
# "ask the user at run time" instead of failing. An explicit "" stays passwordless.
PROMPT_KEYWORDS = {"prompt", "ask", "<ask>", "<prompt>"}
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
    """'[S1,sw00,sw01,sw03,S2]' -> ['S1','sw00','sw01','sw03','S2']"""
    return [n.strip() for n in raw.strip().strip("[]").split(",") if n.strip()]


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
    for i, node in enumerate(route):
        if is_switch(topology, canon(node)):
            resolve_port(topology, canon(node), route[i - 1])
            resolve_port(topology, canon(node), route[i + 1])


# ---------------------------------------------------------------------------
# VLAN / subnet allocation (scales to thousands of flows)
# ---------------------------------------------------------------------------
def allocate(index):
    vlan = VLAN_BASE + VLAN_STEP * index
    if not (1 <= vlan <= 4094):
        raise ValueError(f"flow {index}: VLAN {vlan} out of range 1..4094; "
                         f"lower VLAN_BASE/VLAN_STEP.")
    if vlan <= 254:                                  # readable scheme
        net = f"{SUBNET_PREFIX}.{vlan}"
    else:                                            # scalable fallback
        net = f"10.{index // 256}.{index % 256}"
    return vlan, f"{net}.0/24", f"{net}.{SENDER_HOST}", f"{net}.{RECEIVER_HOST}"


# ---------------------------------------------------------------------------
# Command builders
# ---------------------------------------------------------------------------
def endstation_cmds(iface, vlan, ip):
    v = f"{iface}.{vlan}"
    return [
        f"ip link add link {iface} name {v} type vlan id {vlan}",
        f"ip addr add {ip}/24 dev {v}",
        f"ip link set dev {v} up",
        f"ip link set {v} type vlan egress-qos-map {EGRESS_QOS_MAP}",
        f"ip link set dev {iface} up",
    ]


def build_plan(topology, flow, index):
    validate_route(topology, flow)
    vlan, subnet, sender_ip, receiver_ip = allocate(index)
    route = [canon(n) for n in flow["route"]]

    plan = FlowPlan(index=index + 1, flow_id=flow["id"], src=canon(flow["src"]),
                    dst=canon(flow["dst"]), route=route, vlan=vlan, subnet=subnet,
                    sender_ip=sender_ip, receiver_ip=receiver_ip)

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
# MSTP (optional): one MSTI per flow; auto branch/root detection
# ---------------------------------------------------------------------------
def build_mstp(plans, topology, region="mstp_test", region_rev=1):
    all_switches = sorted({s for p in plans for s in p.switch_cmds})
    per_switch = {s: [] for s in all_switches}

    def bridge(s):
        return node_attr(topology, s, "bridge", DEFAULT_BRIDGE)

    def prefix(s):
        return node_attr(topology, s, "port_prefix", DEFAULT_PORT_PREFIX)

    for s in all_switches:
        b = bridge(s)
        cmds = [f"mstpctl setmstconfid {b} {region_rev} {region}",
                f"mstpctl showmstconfid {b}"]
        for i, _ in enumerate(plans, 1):
            cmds.append(f"mstpctl createtree {b} {i}")
        for i, p in enumerate(plans, 1):
            cmds.append(f"mstpctl setvid2fid {b} {i}:{p.vlan},{p.vlan + 1}")
        for i, _ in enumerate(plans, 1):
            cmds.append(f"mstpctl setfid2mstid {b} {i}:{i}")
        per_switch[s].extend(cmds)

    # force-route: at any switch where trees diverge, penalise foreign egress ports
    for s in all_switches:
        egress = {i: p.switch_hops[s][1]
                  for i, p in enumerate(plans, 1) if s in p.switch_hops}
        if len(set(egress.values())) > 1:
            for tree, my_out in egress.items():
                for other_out in set(egress.values()):
                    if other_out != my_out:
                        per_switch[s].append(
                            f"mstpctl settreeportcost {bridge(s)} "
                            f"{prefix(s)}{other_out} {tree} 5000000")

    # root bridge for every MSTI on the last switch of each route
    for s in {p.last_switch for p in plans if p.last_switch}:
        for i, _ in enumerate(plans, 1):
            per_switch[s].append(f"mstpctl settreeprio {bridge(s)} {i} 0")

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
def print_plan(plans, topology, mstp_plan=None):
    for p in plans:
        print("=" * 72)
        print(f"FLOW {p.index}  (id={p.flow_id})   {p.src} -> {p.dst}   "
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


def apply_plan(plans, topology, mstp_plan=None):
    def creds(n):
        d = topology[n]
        return d["ip"], d["username"], resolve_password(
            n, d["ip"], d["username"], d.get("password"))

    # Ask for every needed password up front, before opening any connection.
    asked = prompt_nodes(plans, topology, mstp_plan)
    if asked:
        print(f"Enter passwords for {len(asked)} node(s) "
              f"(input is hidden; shared host+user asked once):")
        for n in asked:
            creds(n)          # triggers the getpass prompt and caches it
        print()

    for p in plans:
        print(f"\n### FLOW {p.index}  VLAN {p.vlan} ###")
        if p.sender_cmds:
            print(f"-- sender {p.src}")
            ssh_run(*creds(p.src), p.sender_cmds)
        if p.receiver_cmds:
            print(f"-- receiver {p.dst}")
            ssh_run(*creds(p.dst), p.receiver_cmds)
        for sw, cmds in p.switch_cmds.items():
            print(f"-- switch {sw}")
            ssh_run(*creds(sw), cmds)

    if mstp_plan:
        print("\n### MSTP ###")
        for sw, cmds in mstp_plan.items():
            print(f"-- {sw}")
            ssh_run(*creds(sw), cmds)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(description="Topology-agnostic TSN/VLAN config")
    ap.add_argument("--csv", default="stream.csv")
    ap.add_argument("--topology", default="network-topology.json")
    ap.add_argument("--apply", action="store_true", help="SSH in and run (else dry-run)")
    ap.add_argument("--mstp", action="store_true", help="also build the MSTP plan")
    ap.add_argument("--password", action="append", default=[], metavar="NODE=SECRET",
                    help="pre-supply a password non-interactively (repeatable). "
                         "NODE may be a node name or an IP.")
    args = ap.parse_args()

    for item in args.password:
        if "=" not in item:
            ap.error(f"--password expects NODE=SECRET, got '{item}'")
        node, pw = item.split("=", 1)
        _pw_preset[node.strip()] = pw

    topology = load_topology(args.topology)
    flows = load_streams(args.csv)

    plans = []
    for i, flow in enumerate(flows):
        try:
            plans.append(build_plan(topology, flow, i))
        except ValueError as e:
            print(f"[SKIP] flow {i + 1} (id={flow.get('id')}) route "
                  f"{flow.get('route')}: {e}", file=sys.stderr)

    if not plans:
        print("No configurable flows.", file=sys.stderr)
        return []

    mstp_plan = build_mstp(plans, topology) if args.mstp else None
    (apply_plan if args.apply else print_plan)(plans, topology, mstp_plan)
    return [p.summary() for p in plans]


if __name__ == "__main__":
    result = main()
    print("\nreturn value:", json.dumps(result, indent=2))