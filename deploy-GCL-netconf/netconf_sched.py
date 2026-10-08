#!/usr/bin/env python3
"""
netconf_sched.py
----------------
The NETCONF/YANG layer: build an IEEE 802.1Qbv gate-control-list edit-config
for one switch port against the `ieee802-dot1q-sched` model, open a NETCONF
session via ncclient, and read back operational state.

The switches run netopeer2-server + sysrepo and have `ieee802-dot1q-sched`
(rev 2018-09-11, i.e. IEEE Std 802.1Q-2018) installed and *implemented*
(confirmed with `sysrepoctl -l`). This module targets that standard model.

   !!! ONE THING TO CONFIRM ON THE REAL SWITCH BEFORE TRUSTING A PUSH !!!
   The exact *augment point* and the base-time leaf names vary between
   vendor implementations of this model. The defaults below follow the
   published IEEE 802.1Q-2018 YANG (gate-parameters augmenting
   ietf-interfaces/interface, base-time as seconds + nanoseconds). Run
   `configure_gcl_netconf.py --probe-schema --only sw01` once to dump the
   real tree and adjust SCHED_NS / the GATE_PARAMS_TEMPLATE / base-time leaf
   names here if the switch differs. Everything implementation-specific is
   isolated in THIS file.
"""

from xml.sax.saxutils import escape

# --- implementation-specific constants (confirm against the switch schema) ---
IF_NS = "urn:ietf:params:xml:ns:yang:ietf-interfaces"
SCHED_NS = "urn:ieee:std:802.1Q:yang:ieee802-dot1q-sched"
# operation identity for a plain "set gate states" entry (the tsntool "sgs" op)
SET_GATE_STATES = "sched:set-gate-states"
# base-time child leaf names (IEEE 802.1Q-2018: seconds + nanoseconds)
BASE_TIME_SECONDS_LEAF = "seconds"
BASE_TIME_NANOS_LEAF = "nanoseconds"
# ---------------------------------------------------------------------------


def _gate_control_list_xml(entries):
    rows = []
    for index, (interval_ns, gate_byte) in enumerate(entries):
        rows.append(
            "          <gate-control-entry>\n"
            f"            <index>{index}</index>\n"
            f"            <operation-name>{SET_GATE_STATES}</operation-name>\n"
            f"            <time-interval-value>{int(interval_ns)}</time-interval-value>\n"
            f"            <gate-states-value>{int(gate_byte)}</gate-states-value>\n"
            "          </gate-control-entry>"
        )
    return "\n".join(rows)


def build_gate_parameters_config(iface, entries, cycle_num, cycle_den,
                                  base_seconds, base_nanos,
                                  cycle_time_extension=0, gate_enabled=True,
                                  admin_gate_states=255):
    """Return an <interfaces> edit-config payload that writes the admin gate
    control list + cycle + base time for one port and flips config-change to
    make the switch recalculate its gate grid (the NETCONF equivalent of
    `tsntool st wrcl` + `tsntool st configure`)."""
    gcl = _gate_control_list_xml(entries)
    return (
        f'<interfaces xmlns="{IF_NS}">\n'
        "  <interface>\n"
        f"    <name>{escape(iface)}</name>\n"
        f'    <gate-parameters xmlns="{SCHED_NS}" xmlns:sched="{SCHED_NS}">\n'
        f"      <gate-enabled>{'true' if gate_enabled else 'false'}</gate-enabled>\n"
        f"      <admin-gate-states>{int(admin_gate_states)}</admin-gate-states>\n"
        f"      <admin-control-list-length>{len(entries)}</admin-control-list-length>\n"
        "      <admin-control-list>\n"
        f"{gcl}\n"
        "      </admin-control-list>\n"
        "      <admin-cycle-time>\n"
        f"        <numerator>{cycle_num}</numerator>\n"
        f"        <denominator>{cycle_den}</denominator>\n"
        "      </admin-cycle-time>\n"
        f"      <admin-cycle-time-extension>{int(cycle_time_extension)}</admin-cycle-time-extension>\n"
        "      <admin-base-time>\n"
        f"        <{BASE_TIME_SECONDS_LEAF}>{int(base_seconds)}</{BASE_TIME_SECONDS_LEAF}>\n"
        f"        <{BASE_TIME_NANOS_LEAF}>{int(base_nanos)}</{BASE_TIME_NANOS_LEAF}>\n"
        "      </admin-base-time>\n"
        "      <config-change>true</config-change>\n"
        "    </gate-parameters>\n"
        "  </interface>\n"
        "</interfaces>"
    )


def build_state_filter(iface):
    """Subtree filter to read the operational gate-parameters state of one
    port (config-change-time, tick-granularity, oper-base-time, current-time)."""
    return (
        f'<interfaces xmlns="{IF_NS}">\n'
        "  <interface>\n"
        f"    <name>{escape(iface)}</name>\n"
        f'    <gate-parameters xmlns="{SCHED_NS}"/>\n'
        "  </interface>\n"
        "</interfaces>"
    )


def connect(host, user, password, port=830, timeout=15, hostkey_verify=False):
    """Open a NETCONF session with ncclient. Imported lazily so the module
    loads (and the XML builders can be unit-tested) without ncclient present."""
    from ncclient import manager
    return manager.connect(
        host=host, port=port, username=user,
        password=(password or None),
        hostkey_verify=hostkey_verify,
        allow_agent=True, look_for_keys=True,
        timeout=timeout,
    )


def read_tick_ns(session, iface):
    """Read tick-granularity (units of 1/10 ns in this model, matching
    tsntool's '3200 1/10 nsec') and return it in whole ns, or None if the
    switch doesn't expose it in state."""
    from ncclient.operations import RPCError  # noqa: F401
    reply = session.get(filter=("subtree", build_state_filter(iface)))
    xml = reply.data_xml
    import re
    m = re.search(r"<tick-granularity>\s*(\d+)\s*</tick-granularity>", xml)
    if not m:
        return None
    tenths = int(m.group(1))
    if tenths % 10 != 0:
        raise RuntimeError(f"{iface}: tick-granularity {tenths}/10 ns not a whole ns")
    return tenths // 10


def read_config_change_time_ns(session, iface):
    """Read config-change-time (the grid the gates actually run on) in ns, or
    None. Mirrors the tsntool path reading ConfigChangeTime from sysfs."""
    reply = session.get(filter=("subtree", build_state_filter(iface)))
    xml = reply.data_xml
    import re
    block = re.search(r"<config-change-time>(.*?)</config-change-time>", xml, re.S)
    if not block:
        return None
    body = block.group(1)
    sec = re.search(rf"<{BASE_TIME_SECONDS_LEAF}>\s*(\d+)", body)
    ns = re.search(rf"<{BASE_TIME_NANOS_LEAF}>\s*(\d+)", body)
    if not sec:
        return None
    return int(sec.group(1)) * 1_000_000_000 + (int(ns.group(1)) if ns else 0)
