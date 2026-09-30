#!/usr/bin/env python3
"""
configure_gcl.py
-----------------
Push a directory of IEEE 802.1Qbv (Qbv/TAS) GCL schedules to a set of TTTech
switches over SSH, via each switch's own `tsntool`.

Input: a directory of "<switch>-<port>.cfg" files, e.g. sw01-p3.cfg means
switch "sw01", local port "p3" (device sw0p3). Each file is already in
tsntool's record format ("sgs <interval-ns> <gate-state-value>", comments
allowed) -- this is exactly what a schedule generator under GCL_Schedules/
writes to its gcl/ subfolder.

For every port found it:
  1. uploads the .cfg to the switch (SFTP) and writes it to the
     AdminControlList (`tsntool st wrcl`),
  2. activates it (`tsntool st configure`) using ONE common basetime for
     every port on every switch, so all switches start their gate cycle at
     the same absolute instant -- this only produces a correct schedule if
     the switches' clocks are already synchronized (see
     clock-syncrhonize-ptp/), since the basetime is an absolute PTP/TAI
     timestamp, not a per-switch relative offset.

Run:
    python3 configure_gcl.py --gcl-dir <dir> --topology <topology.json>            # dry-run
    python3 configure_gcl.py --gcl-dir <dir> --topology <topology.json> --apply
"""

import argparse
import getpass
import json
import os
import re
import sys
from fractions import Fraction

FILENAME_RE = re.compile(r"^(?P<switch>[A-Za-z0-9]+)-(?P<port>p\d+)\.cfg$")
DEFAULT_PORT_PREFIX = "sw0"
CYCLE_TIME_EXTENSION = 0  # legacy tsntool parameter, ignored by the driver

PROMPT_KEYWORDS = {"prompt", "ask", "<ask>", "<prompt>", "promt", "<promt>"}
_pw_cache = {}


def needs_prompt(raw):
    return raw is None or str(raw).strip().lower() in PROMPT_KEYWORDS


def resolve_password(node, host, user, raw, preset):
    if node in preset:
        return preset[node]
    if host in preset:
        return preset[host]
    if not needs_prompt(raw):
        return raw
    key = (host, user)
    if key not in _pw_cache:
        _pw_cache[key] = getpass.getpass(f"  password for {node} ({user}@{host}): ")
    return _pw_cache[key]


def ssh_connect(host, user, password, timeout=15):
    """Open an authenticated SSHClient. An empty password means passwordless
    (SSH 'none' auth), which paramiko's high-level connect() never tries."""
    import socket
    import paramiko

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    if password:
        client.connect(host, username=user, password=password,
                        look_for_keys=False, allow_agent=False, timeout=timeout)
        return client
    sock = socket.create_connection((host, 22), timeout=timeout)
    transport = paramiko.Transport(sock)
    transport.start_client(timeout=timeout)
    try:
        transport.auth_none(user)
    except paramiko.BadAuthenticationType as e:
        transport.close()
        raise RuntimeError(f"{user}@{host} rejected passwordless (none) auth; "
                            f"allowed types: {e.allowed_types}")
    if not transport.is_authenticated():
        transport.close()
        raise RuntimeError(f"{user}@{host}: SSH none auth did not authenticate")
    client._transport = transport
    return client


def run(client, cmd):
    stdin, stdout, stderr = client.exec_command(cmd)
    rc = stdout.channel.recv_exit_status()
    return rc, stdout.read().decode().strip(), stderr.read().decode().strip()


def strip_trailing_comments(text):
    """tsntool only accepts '#' as a comment when it's the first non-whitespace
    character of the line (whole-line comments) -- a trailing '# ...' after
    real sgs/shm/srm data is an unrecognized 4th field ("Excess record
    elements") and tsntool rejects the whole file. The shipped .cfg files
    use trailing comments for human-readable annotation only; this drops
    them without touching any op/interval/gsv values."""
    out_lines = []
    for line in text.splitlines():
        stripped = line.lstrip()
        if stripped.startswith("#") or not stripped:
            out_lines.append(line)
            continue
        head, sep, _ = line.partition("#")
        out_lines.append(head.rstrip() if sep else line)
    return "\n".join(out_lines) + "\n"


def upload_via_cat(client, remote_path, content_bytes):
    """Write bytes to the remote host over a plain exec channel (`cat >
    remote_path`), for switches whose sshd has no sftp subsystem."""
    stdin, stdout, stderr = client.exec_command(f"cat > {remote_path}")
    stdin.write(content_bytes)
    stdin.channel.shutdown_write()
    rc = stdout.channel.recv_exit_status()
    if rc != 0:
        raise RuntimeError(f"upload to {remote_path} failed: {stderr.read().decode().strip()}")


def parse_cfg_entries(text):
    """Parse already-comment-stripped 'sgs <interval> <gsv>' lines into
    [(interval_ns, byte), ...]. Tolerates float-formatted intervals (the
    shipped files have a few, e.g. '7592.0')."""
    entries = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        op, interval, gsv = line.split()
        if op != "sgs":
            raise ValueError(f"unsupported GCL operation '{op}' (only sgs is handled)")
        entries.append((int(float(interval)), int(gsv, 0)))
    return entries


def render_cfg_entries(entries):
    return "".join(f"sgs {interval} {byte:#04x}\n" for interval, byte in entries)


def query_tick_ns(client, iface):
    rc, out, err = run(client, f"tsntool st show {iface}")
    if rc != 0:
        raise RuntimeError(f"tsntool st show {iface} failed: {err or out}")
    for line in out.splitlines():
        if "TickGranularity" in line:
            # e.g. "TickGranularity:         3200 1/10 nsec" -> value is in units of 0.1ns
            value = line.split(":", 1)[1].strip().split()[0]
            tenths_ns = int(value)
            if tenths_ns % 10 != 0:
                raise RuntimeError(f"{iface}: TickGranularity {tenths_ns}/10 ns "
                                    f"isn't a whole number of ns, can't round to it")
            return tenths_ns // 10
    raise RuntimeError(f"could not find TickGranularity in `tsntool st show {iface}`")


def round_to_tick(entries, tick_ns, cycle_ns):
    """Round every cumulative boundary to the nearest tick (not each interval
    independently) so rounding error doesn't accumulate across the list --
    the total still lands on the nearest tick to cycle_ns, which is exact
    when cycle_ns is itself a multiple of tick_ns. Zero-length results from
    rounding (two boundaries collapsing onto the same tick) are dropped;
    adjacent entries with the same gate-state byte are re-merged."""
    total = sum(i for i, _ in entries)
    if total != cycle_ns:
        raise ValueError(f"entries sum to {total} ns, expected cycle {cycle_ns} ns")

    rounded = []
    cum_orig = 0
    cum_rounded = 0
    for interval, byte in entries:
        cum_orig += interval
        target = round(cum_orig / tick_ns) * tick_ns
        length = target - cum_rounded
        cum_rounded = target
        if length > 0:
            rounded.append([length, byte])

    merged = []
    for length, byte in rounded:
        if merged and merged[-1][1] == byte:
            merged[-1][0] += length
        else:
            merged.append([length, byte])

    new_total = sum(i for i, _ in merged)
    if new_total != cycle_ns:
        raise RuntimeError(f"rounding bug: rebuilt total {new_total} != cycle {cycle_ns}")
    return [(i, b) for i, b in merged]


def discover_ports(gcl_dir):
    """Return {switch: {port: local_path}}."""
    ports = {}
    for name in sorted(os.listdir(gcl_dir)):
        m = FILENAME_RE.match(name)
        if not m:
            continue
        ports.setdefault(m["switch"], {})[m["port"]] = os.path.join(gcl_dir, name)
    return ports


def reduce_cycle(cycle_ns):
    """cycle time in ns -> (numerator, denominator) seconds, as tsntool wants."""
    f = Fraction(cycle_ns, 1_000_000_000)
    return f.numerator, f.denominator


def query_currenttime(client, iface):
    rc, out, err = run(client, f"cat /sys/class/net/{iface}/ieee8021ST/CurrentTime")
    if rc != 0 or not out.strip():
        raise RuntimeError(f"could not read CurrentTime for {iface}: {err or out}")
    return out.strip()


def add_lead(basetime_str, lead_seconds):
    sec_str, _, nsec_str = basetime_str.partition(".")
    nsec_str = (nsec_str + "000000000")[:9]
    total_ns = int(sec_str) * 1_000_000_000 + int(nsec_str)
    total_ns += int(lead_seconds * 1_000_000_000)
    sec, ns = divmod(total_ns, 1_000_000_000)
    return f"{sec}.{ns:09d}"


def main():
    ap = argparse.ArgumentParser(
        description="Push IEEE 802.1Qbv GCL schedules to switches via tsntool")
    ap.add_argument("--gcl-dir", required=True,
                     help="directory of <switch>-<port>.cfg files (e.g. .../gcl)")
    ap.add_argument("--topology", required=True,
                     help="topology JSON with per-node ip/username/password")
    ap.add_argument("--cycle-ns", type=int, default=None,
                     help="cycle time in ns (default: read cycle_ns from "
                          "schedule.json next to --gcl-dir)")
    ap.add_argument("--lead-seconds", type=float, default=60,
                     help="how far in the future (from a reference switch's own "
                          "clock) to set the common activation basetime -- must "
                          "cover the whole activation loop below, or later "
                          "switches' basetime arrives before they're configured "
                          "(default 60)")
    ap.add_argument("--no-round-to-tick", action="store_true",
                     help="don't round intervals to the switch's TickGranularity "
                          "before upload -- will fail on hardware whose tick "
                          "doesn't evenly divide the schedule's intervals")
    ap.add_argument("--port-prefix", default=DEFAULT_PORT_PREFIX,
                     help="switch local port device prefix (default sw0)")
    ap.add_argument("--remote-path", default="/home/root/gcl_{port}.cfg",
                     help="path to upload each cfg to on its switch (default "
                          "avoids /tmp: on these boards it's tmpfs-backed and "
                          "small, and shared across all tenants of the switch)")
    ap.add_argument("--apply", action="store_true",
                     help="actually push and activate (default: dry-run, print plan)")
    ap.add_argument("--only", nargs="*", metavar="SWITCH",
                     help="restrict to these switch names (e.g. sw01 sw03)")
    ap.add_argument("--exclude", nargs="*", metavar="SWITCH", default=[],
                     help="skip these switch names entirely -- e.g. a switch "
                          "whose GCL only serves routes to/from a node that "
                          "isn't physically on the testbed right now, so it "
                          "should not be admitted (--exclude sw01)")
    ap.add_argument("--password", action="append", default=[], metavar="NODE=SECRET",
                     help="pre-supply a password non-interactively (repeatable)")
    args = ap.parse_args()

    preset = {}
    for item in args.password:
        if "=" not in item:
            ap.error(f"--password expects NODE=SECRET, got '{item}'")
        k, v = item.split("=", 1)
        preset[k.strip()] = v

    with open(args.topology) as f:
        topology = json.load(f)

    ports = discover_ports(args.gcl_dir)
    if args.only:
        ports = {sw: p for sw, p in ports.items() if sw in args.only}
    if args.exclude:
        excluded = [sw for sw in ports if sw in args.exclude]
        ports = {sw: p for sw, p in ports.items() if sw not in args.exclude}
        if excluded:
            print(f"[info] excluding switch(es): {', '.join(sorted(excluded))}")
    if not ports:
        print("[FATAL] no <switch>-<port>.cfg files found in "
              f"{args.gcl_dir}", file=sys.stderr)
        return 1

    missing = sorted(sw for sw in ports if sw not in topology)
    if missing:
        print(f"[FATAL] switch(es) not found in {args.topology}: "
              f"{', '.join(missing)}", file=sys.stderr)
        return 1

    cycle_ns = args.cycle_ns
    if cycle_ns is None:
        sched_json = os.path.join(os.path.dirname(os.path.normpath(args.gcl_dir)),
                                   "schedule.json")
        if os.path.exists(sched_json):
            with open(sched_json) as f:
                cycle_ns = json.load(f)["cycle_ns"]
            print(f"[info] cycle time read from {sched_json}: {cycle_ns} ns")
        else:
            ap.error("--cycle-ns not given and no schedule.json found next to --gcl-dir")
    num, den = reduce_cycle(cycle_ns)
    cycle_frac = f"{num}/{den}"

    total_ports = sum(len(p) for p in ports.values())
    print(f"Plan: {len(ports)} switch(es), {total_ports} port(s), "
          f"cycle time {cycle_ns} ns ({cycle_frac} s)")
    for sw in sorted(ports):
        d = topology[sw]
        ifaces = ", ".join(f"{args.port_prefix}{p}" for p in sorted(ports[sw]))
        print(f"  {sw} @ {d['ip']}: {ifaces}")

    if not args.apply:
        print("\nDry-run only. Re-run with --apply to push and activate.")
        return 0

    import paramiko

    clients = {}
    try:
        # 1) upload + write AdminControlList on every port
        for sw in sorted(ports):
            d = topology[sw]
            host, user = d["ip"], d["username"]
            pw = resolve_password(sw, host, user, d.get("password"), preset)
            print(f"\n-- {sw} ({host}) --")
            client = ssh_connect(host, user, pw)
            clients[sw] = client
            tick_ns = None
            for port, local_path in sorted(ports[sw].items()):
                iface = f"{args.port_prefix}{port}"
                remote_path = args.remote_path.format(port=port)
                with open(local_path) as f:
                    entries = parse_cfg_entries(strip_trailing_comments(f.read()))
                if not args.no_round_to_tick:
                    if tick_ns is None:
                        tick_ns = query_tick_ns(client, iface)
                        print(f"   (TickGranularity for {sw}: {tick_ns} ns)")
                    before = len(entries)
                    entries = round_to_tick(entries, tick_ns, cycle_ns)
                    if len(entries) != before:
                        print(f"   {iface}: rounded to {tick_ns}ns tick, "
                              f"{before} -> {len(entries)} entries")
                content = render_cfg_entries(entries).encode()
                upload_via_cat(client, remote_path, content)
                rc, out, err = run(client, f"tsntool st wrcl {iface} {remote_path}")
                status = "OK" if rc == 0 else f"ERR({rc})"
                print(f"   wrcl {iface}: {status}" + (f"  {err or out}" if rc else ""))

        # 2) one common basetime, sampled from a reference switch's own clock --
        #    valid for every switch only because they're already PTP-synced.
        ref_sw = sorted(ports)[0]
        ref_client = clients[ref_sw]
        ref_iface = f"{args.port_prefix}{sorted(ports[ref_sw])[0]}"
        now = query_currenttime(ref_client, ref_iface)
        basetime = add_lead(now, args.lead_seconds)
        print(f"\nCommon basetime: {basetime}  "
              f"(reference {ref_sw}/{ref_iface} CurrentTime {now} + "
              f"{args.lead_seconds}s lead)")

        # 3) activate every port with the same basetime
        for sw in sorted(ports):
            client = clients[sw]
            for port in sorted(ports[sw]):
                iface = f"{args.port_prefix}{port}"
                rc, out, err = run(
                    client,
                    f"tsntool st configure {basetime} {cycle_frac} "
                    f"{CYCLE_TIME_EXTENSION} {iface}")
                status = "OK" if rc == 0 else f"ERR({rc})"
                print(f"   configure {sw}/{iface}: {status}" +
                      (f"  {err or out}" if rc else ""))

        # 4) verify -- GatesEnabled/ConfigPending can look fine even when the
        #    activation silently didn't take (e.g. basetime already in the
        #    past by the time it ran), so compare AdminControlList against
        #    OperControlList directly: that's the real proof it promoted.
        print("\nVerifying (comparing AdminControlList to OperControlList -- "
              "they must match for the new schedule to actually be live):")
        not_live = []
        for sw in sorted(ports):
            client = clients[sw]
            for port in sorted(ports[sw]):
                iface = f"{args.port_prefix}{port}"
                _, acl, _ = run(client, f"tsntool st rdacl {iface}")
                _, ocl, _ = run(client, f"tsntool st rdocl {iface}")
                live = acl == ocl
                if not live:
                    not_live.append(f"{sw}/{iface}")
                print(f"   {sw}/{iface}: {'LIVE' if live else 'NOT LIVE YET'}")
        if not_live:
            print(f"\n{len(not_live)} port(s) did NOT promote to OperControlList: "
                  f"{', '.join(not_live)}")
            print("AdminControlList holds the new schedule but the switch is still "
                  "gating on the old one. Likely cause: the shared basetime was "
                  "already in the past by the time that port's `configure` ran -- "
                  "re-run (possibly with a larger --lead-seconds), then check again.")
    finally:
        for client in clients.values():
            client.close()

    return 0


if __name__ == "__main__":
    sys.exit(main())
