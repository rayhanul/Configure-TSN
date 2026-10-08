#!/usr/bin/env python3
"""
configure_gcl_netconf.py
------------------------
NETCONF counterpart of ../deploy-GCL/configure_gcl.py. Pushes the SAME
directory of "<switch>-<port>.cfg" GCL files to the switches, but over
NETCONF/YANG (ieee802-dot1q-sched via netopeer2) instead of SSH + tsntool.

What is identical to the tsntool path (reused from gcl_common.py):
  - filename -> switch/port mapping (sw01-p3.cfg -> switch sw01, iface sw0p3)
  - cycle time read from schedule.json's cycle_ns, as a numerator/denominator
  - rounding every GCL boundary to the switch's tick granularity
  - ONE common base time for every port on every switch, sampled from a
    reference switch + a lead, so all gates start the same absolute cycle
  - reading back the grid the switches actually run on and writing basetime.json

What differs (the whole point of the comparison):
  - no file upload, no tsntool: the gate list is the payload of an
    <edit-config> to the candidate datastore, activated with <commit>
  - per switch, ALL its ports go in ONE candidate + ONE commit (atomic)
  - errors come back as structured <rpc-error>, not scraped stderr

Usage (mirrors configure_gcl.py):
    python3 configure_gcl_netconf.py --gcl-dir <dir> --topology <topo.json>            # dry-run
    python3 configure_gcl_netconf.py --gcl-dir <dir> --topology <topo.json> --apply
    python3 configure_gcl_netconf.py --gcl-dir <dir> --topology <topo.json> --probe-schema --only sw01
Options --only / --exclude / --password / --lead-seconds / --port-prefix /
--tick-ns / --no-round-to-tick behave as in configure_gcl.py.
"""

import argparse
import getpass
import json
import os
import sys

import gcl_common as gc
import netconf_sched as ns

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


def load_entries(local_path, tick_ns, cycle_ns, no_round):
    with open(local_path) as f:
        entries = gc.parse_cfg_entries(gc.strip_trailing_comments(f.read()))
    if not no_round:
        before = len(entries)
        entries = gc.round_to_tick(entries, tick_ns, cycle_ns)
        return entries, before
    return entries, len(entries)


def main():
    ap = argparse.ArgumentParser(
        description="Push IEEE 802.1Qbv GCL schedules to switches via NETCONF")
    ap.add_argument("--gcl-dir", required=True,
                    help="directory of <switch>-<port>.cfg files (e.g. .../gcl)")
    ap.add_argument("--topology", required=True,
                    help="topology JSON with per-node ip/username/password")
    ap.add_argument("--cycle-ns", type=int, default=None,
                    help="cycle time in ns (default: cycle_ns from schedule.json "
                         "next to --gcl-dir)")
    ap.add_argument("--lead-seconds", type=float, default=60,
                    help="how far ahead of a reference switch's clock to set the "
                         "common base time (default 60)")
    ap.add_argument("--tick-ns", type=int, default=None,
                    help="tick granularity in ns to round to, instead of reading "
                         "it from the switch over NETCONF (the real DE-IP boards "
                         "report 320); useful offline or when state read is slow")
    ap.add_argument("--no-round-to-tick", action="store_true",
                    help="don't round intervals to the tick granularity")
    ap.add_argument("--port-prefix", default=gc.DEFAULT_PORT_PREFIX,
                    help="switch local port device prefix (default sw0)")
    ap.add_argument("--netconf-port", type=int, default=830)
    ap.add_argument("--apply", action="store_true",
                    help="actually edit-config + commit (default: dry-run, print "
                         "the plan and the edit-config XML for the first port)")
    ap.add_argument("--probe-schema", action="store_true",
                    help="connect and dump each selected switch's gate-parameters "
                         "state tree, then exit -- use this to CONFIRM the model's "
                         "augment point/leaf names before trusting --apply")
    ap.add_argument("--only", nargs="*", metavar="SWITCH")
    ap.add_argument("--exclude", nargs="*", metavar="SWITCH", default=[])
    ap.add_argument("--password", action="append", default=[], metavar="NODE=SECRET")
    args = ap.parse_args()

    preset = {}
    for item in args.password:
        if "=" not in item:
            ap.error(f"--password expects NODE=SECRET, got '{item}'")
        k, v = item.split("=", 1)
        preset[k.strip()] = v

    with open(args.topology) as f:
        topology = json.load(f)

    ports = gc.discover_ports(args.gcl_dir)
    if args.only:
        ports = {sw: p for sw, p in ports.items() if sw in args.only}
    if args.exclude:
        excluded = [sw for sw in ports if sw in args.exclude]
        ports = {sw: p for sw, p in ports.items() if sw not in args.exclude}
        if excluded:
            print(f"[info] excluding switch(es): {', '.join(sorted(excluded))}")
    if not ports:
        print(f"[FATAL] no <switch>-<port>.cfg files found in {args.gcl_dir}",
              file=sys.stderr)
        return 1

    missing = sorted(sw for sw in ports if sw not in topology)
    if missing:
        print(f"[FATAL] switch(es) not in {args.topology}: {', '.join(missing)}",
              file=sys.stderr)
        return 1

    # ---- schema probe: connect, dump state, exit (no config change) ----
    if args.probe_schema:
        for sw in sorted(ports):
            d = topology[sw]
            host, user = d["ip"], d["username"]
            pw = resolve_password(sw, host, user, d.get("password"), preset)
            iface = f"{args.port_prefix}{sorted(ports[sw])[0]}"
            print(f"\n== {sw} ({host}) gate-parameters state for {iface} ==")
            try:
                with ns.connect(host, user, pw, port=args.netconf_port) as m:
                    print("server capabilities (sched/bridge/interfaces):")
                    for c in m.server_capabilities:
                        if any(k in c for k in ("dot1q-sched", "dot1q-bridge",
                                                "ietf-interfaces")):
                            print("   ", c)
                    reply = m.get(filter=("subtree", ns.build_state_filter(iface)))
                    print(reply.data_xml)
            except Exception as e:
                print(f"   [ERROR] {type(e).__name__}: {e}")
        return 0

    cycle_ns = args.cycle_ns
    if cycle_ns is None:
        sched_json = os.path.join(os.path.dirname(os.path.normpath(args.gcl_dir)),
                                  "schedule.json")
        if os.path.exists(sched_json):
            with open(sched_json) as f:
                cycle_ns = json.load(f)["cycle_ns"]
            print(f"[info] cycle time read from {sched_json}: {cycle_ns} ns")
        else:
            ap.error("--cycle-ns not given and no schedule.json next to --gcl-dir")
    cycle_num, cycle_den = gc.reduce_cycle(cycle_ns)

    total_ports = sum(len(p) for p in ports.values())
    print(f"Plan: {len(ports)} switch(es), {total_ports} port(s), "
          f"cycle {cycle_ns} ns ({cycle_num}/{cycle_den} s), transport NETCONF")
    for sw in sorted(ports):
        ifaces = ", ".join(f"{args.port_prefix}{p}" for p in sorted(ports[sw]))
        print(f"  {sw} @ {topology[sw]['ip']}: {ifaces}")

    # ---- dry-run: render the first port's edit-config so it can be eyeballed ----
    if not args.apply:
        tick_ns = args.tick_ns or 320  # DE-IP boards report 320; only for preview
        sw0 = sorted(ports)[0]
        p0 = sorted(ports[sw0])[0]
        iface0 = f"{args.port_prefix}{p0}"
        entries, _ = load_entries(ports[sw0][p0], tick_ns, cycle_ns,
                                  args.no_round_to_tick)
        xml = ns.build_gate_parameters_config(
            iface0, entries, cycle_num, cycle_den, base_seconds=0, base_nanos=0)
        print(f"\nDry-run. Example <edit-config> payload for {sw0}/{iface0} "
              f"(base time 0 as placeholder, tick {tick_ns} ns):\n")
        print(xml)
        print("\nRe-run with --apply to edit-config + commit for real.")
        return 0

    # ---- apply ----
    sessions = {}
    try:
        # 1) open a session per switch and stage all its ports in candidate
        tick_cache = {}
        for sw in sorted(ports):
            d = topology[sw]
            host, user = d["ip"], d["username"]
            pw = resolve_password(sw, host, user, d.get("password"), preset)
            print(f"\n-- {sw} ({host}) --")
            m = ns.connect(host, user, pw, port=args.netconf_port)
            sessions[sw] = m

            tick_ns = args.tick_ns
            for port, local_path in sorted(ports[sw].items()):
                iface = f"{args.port_prefix}{port}"
                if not args.no_round_to_tick and tick_ns is None:
                    tick_ns = ns.read_tick_ns(m, iface)
                    if tick_ns is None:
                        raise RuntimeError(
                            f"{sw}/{iface}: switch did not report tick-granularity; "
                            f"pass --tick-ns (DE-IP boards use 320)")
                    tick_cache[sw] = tick_ns
                    print(f"   (tick-granularity for {sw}: {tick_ns} ns)")
                entries, before = load_entries(local_path, tick_ns, cycle_ns,
                                               args.no_round_to_tick)
                if len(entries) != before:
                    print(f"   {iface}: rounded to {tick_ns}ns tick, "
                          f"{before} -> {len(entries)} entries")
                # base time filled in step 3; stage list + cycle now with a
                # placeholder so validation runs against real data
                xml = ns.build_gate_parameters_config(
                    iface, entries, cycle_num, cycle_den,
                    base_seconds=0, base_nanos=0)
                m.edit_config(target="candidate", config=_wrap(xml),
                              default_operation="merge")
                print(f"   staged {iface}: {len(entries)} entries")

        # 2) one common base time from a reference switch's current-time + lead
        ref_sw = sorted(ports)[0]
        ref_iface = f"{args.port_prefix}{sorted(ports[ref_sw])[0]}"
        now_ns = ns.read_config_change_time_ns(sessions[ref_sw], ref_iface)
        # current-time and config-change-time share the ptp-time shape; if the
        # model exposes a distinct current-time leaf, prefer it. We read
        # whichever the state filter returned; fall back to wall clock if absent.
        if now_ns is None:
            import time
            now_ns = time.clock_gettime_ns(getattr(time, "CLOCK_TAI", time.CLOCK_REALTIME))
            print("   [warn] no current-time in state; using host CLOCK_TAI/REALTIME")
        base_total_ns = now_ns + int(args.lead_seconds * 1_000_000_000)
        base_sec, base_ns = divmod(base_total_ns, 1_000_000_000)
        print(f"\nCommon base time: {base_sec}.{base_ns:09d}  "
              f"(ref {ref_sw}/{ref_iface} + {args.lead_seconds}s lead)")

        # 3) re-stage base time on every port, then commit each switch atomically
        change_ns = {}
        for sw in sorted(ports):
            m = sessions[sw]
            tick_ns = args.tick_ns or tick_cache.get(sw, 320)
            for port in sorted(ports[sw]):
                iface = f"{args.port_prefix}{port}"
                entries, _ = load_entries(ports[sw][port], tick_ns, cycle_ns,
                                          args.no_round_to_tick)
                xml = ns.build_gate_parameters_config(
                    iface, entries, cycle_num, cycle_den,
                    base_seconds=base_sec, base_nanos=base_ns)
                m.edit_config(target="candidate", config=_wrap(xml),
                              default_operation="merge")
            m.commit()   # ALL of this switch's ports activate together
            print(f"   committed {sw}")

        # 4) read back the grid the switches actually run on -> basetime.json
        for sw in sorted(ports):
            for port in sorted(ports[sw]):
                iface = f"{args.port_prefix}{port}"
                v = ns.read_config_change_time_ns(sessions[sw], iface)
                if v is not None:
                    change_ns[f"{sw}/{iface}"] = v
        ref_key = f"{ref_sw}/{ref_iface}"
        grid_ns = change_ns.get(ref_key)
        if grid_ns is None:
            print(f"\nWARNING: no config-change-time from {ref_key}; "
                  "basetime.json not written")
        else:
            off = {k: (v - grid_ns + cycle_ns // 2) % cycle_ns - cycle_ns // 2
                   for k, v in change_ns.items()}
            off_grid = {k: v for k, v in off.items() if abs(v) > 1000}
            if off_grid:
                print(f"\nWARNING: ports not on {ref_key}'s grid (ns): {off_grid}")
            out = os.path.join(os.path.dirname(os.path.normpath(args.gcl_dir)),
                               "basetime.json")
            with open(out, "w") as f:
                json.dump({"basetime_ns": grid_ns, "cycle_ns": cycle_ns,
                           "clock": "TAI",
                           "source": f"config-change-time of {ref_key} (NETCONF)",
                           "requested_basetime_ns": base_total_ns,
                           "port_offsets_ns": off}, f, indent=2)
                f.write("\n")
            print(f"\nGate grid: {grid_ns} ns (TAI), phase {grid_ns % cycle_ns} ns. "
                  f"Saved to {out}")
    finally:
        for m in sessions.values():
            try:
                m.close_session()
            except Exception:
                pass
    return 0


def _wrap(inner_xml):
    """ncclient edit_config wants the payload under <config>."""
    return f"<config>{inner_xml}</config>"


if __name__ == "__main__":
    sys.exit(main())
