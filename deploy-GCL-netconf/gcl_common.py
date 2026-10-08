#!/usr/bin/env python3
"""
gcl_common.py
-------------
Transport-agnostic helpers shared by the NETCONF deploy/benchmark scripts in
this folder. These are copied verbatim (behaviour-for-behaviour) from
deploy-GCL/configure_gcl.py so that the NETCONF path produces the *same* gate
control list the tsntool path does -- same tick rounding, same filename->port
mapping, same cycle-fraction. Only the transport (how the list reaches the
switch) differs. Nothing here touches SSH or NETCONF.
"""

import os
import re
from fractions import Fraction

FILENAME_RE = re.compile(r"^(?P<switch>[A-Za-z0-9]+)-(?P<port>p\d+)\.cfg$")
DEFAULT_PORT_PREFIX = "sw0"


def strip_trailing_comments(text):
    """tsntool only accepts '#' as a comment when it's the first non-whitespace
    character of the line. The shipped .cfg files use trailing '# 01111111'
    annotations; drop them without touching any op/interval/gsv values. (The
    NETCONF payload has no comments at all, but we parse the same source files,
    so we strip the same way.)"""
    out_lines = []
    for line in text.splitlines():
        stripped = line.lstrip()
        if stripped.startswith("#") or not stripped:
            out_lines.append(line)
            continue
        head, sep, _ = line.partition("#")
        out_lines.append(head.rstrip() if sep else line)
    return "\n".join(out_lines) + "\n"


def parse_cfg_entries(text):
    """Parse already-comment-stripped 'sgs <interval> <gsv>' lines into
    [(interval_ns, gate_states_byte), ...]. Tolerates float-formatted
    intervals (a few shipped files have e.g. '7592.0'). Only the 'sgs'
    (set-gate-states) operation is handled, which is all the schedule
    generator emits."""
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


def round_to_tick(entries, tick_ns, cycle_ns):
    """Round every *cumulative* boundary to the nearest tick (not each interval
    independently) so rounding error doesn't accumulate across the list. Zero
    length results are dropped; adjacent entries with the same gate-state byte
    are re-merged. Identical to the tsntool path."""
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
    """Return {switch: {port: local_path}} from <switch>-<port>.cfg files."""
    ports = {}
    for name in sorted(os.listdir(gcl_dir)):
        m = FILENAME_RE.match(name)
        if not m:
            continue
        ports.setdefault(m["switch"], {})[m["port"]] = os.path.join(gcl_dir, name)
    return ports


def reduce_cycle(cycle_ns):
    """cycle time in ns -> (numerator, denominator) seconds, the admin-cycle-time
    rational that both tsntool and ieee802-dot1q-sched want."""
    f = Fraction(cycle_ns, 1_000_000_000)
    return f.numerator, f.denominator


def add_lead(basetime_str, lead_seconds):
    """basetime 'sec.nsec' string + lead seconds -> 'sec.nsec' string."""
    sec_str, _, nsec_str = basetime_str.partition(".")
    nsec_str = (nsec_str + "000000000")[:9]
    total_ns = int(sec_str) * 1_000_000_000 + int(nsec_str)
    total_ns += int(lead_seconds * 1_000_000_000)
    sec, ns = divmod(total_ns, 1_000_000_000)
    return f"{sec}.{ns:09d}"


def split_seconds_ns(basetime_str):
    """'sec.nsec' string -> (seconds:int, nanoseconds:int) for admin-base-time."""
    sec_str, _, nsec_str = basetime_str.partition(".")
    nsec_str = (nsec_str + "000000000")[:9]
    return int(sec_str), int(nsec_str)
