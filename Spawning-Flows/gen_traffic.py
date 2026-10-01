#!/usr/bin/env python3
"""
gen_traffic.py -- send/receive real UDP traffic for the flows of a GCL schedule.json.

Flows in scope for --node are those configureManager.py admitted for it (endpoints.json).
Sender (one process, all flows): SO_PRIORITY = pcp, frame time = basetime + n*period + first-hop
psi_ns (CLOCK_TAI); UDP payload = size - 50 so the frame is `size` bytes. The frame is
queued early with SO_TXTIME and the NIC launches it at exactly that time (etf offload, see
time-sync-gptp/gptp.sh launchtime). Receiver (one epoll process, all flows): latency = NIC hardware
RX timestamp - NIC launch time, jitter, deadline misses. No timestamp comes from Python. See README.md.
"""

import argparse
import heapq
import json
import multiprocessing as mp
import os
import selectors
import socket
import struct
import sys
import time

BASE_PORT = 50000
HEADER_FMT = "q"  # TX time: the NIC launch time, CLOCK_TAI ns
HEADER_SIZE = struct.calcsize(HEADER_FMT)
# bytes of a VLAN-tagged UDP/IPv4 frame that are not UDP payload: Ethernet 14 + VLAN 4 + FCS 4 + IP 20 + UDP 8
FRAME_OVERHEAD = 50
MIN_FRAME = 68  # 64-byte Ethernet minimum + 4-byte VLAN tag; smaller frames get padded by the NIC
TAI_UTC_S = 37
# RX time: the NIC's hardware timestamp (PHC = TAI). The I210/I225 rx_filter is ALL while ptp4l
# runs, so every received frame carries one. TX time: the NIC launch time (SO_TXTIME + etf offload);
# no per-packet TX hardware timestamps, since the I210 has one TX timestamp slot, shared with ptp4l.
SO_TIMESTAMPING = SCM_TIMESTAMPING = 37
TS_FLAGS = (1 << 2) | (1 << 6)  # SOF_TIMESTAMPING_RX_HARDWARE | SOF_TIMESTAMPING_RAW_HARDWARE
SO_TXTIME = SCM_TXTIME = 61
ETF_DELTA_NS = 300_000   # must match gptp.sh launchtime: etf hands a frame to the NIC this long before its launch time
LATE_MARGIN_NS = 50_000  # a frame not queued by launch - delta - margin would be dropped by etf: skip it instead


def load_basetime(path):
    """basetime in ns (TAI) from configure_gcl.py's basetime.json, or None if there is none."""
    try:
        with open(path) as f:
            return int(json.load(f)["basetime_ns"])
    except FileNotFoundError:
        return None


def check_tai_offset():
    # the switches' basetime is TAI; CLOCK_TAI is only TAI if the kernel's TAI offset is set (37 s)
    off = time.clock_gettime(time.CLOCK_TAI) - time.time()
    if abs(off - TAI_UTC_S) > 0.5:
        print(f"[WARN] CLOCK_TAI - CLOCK_REALTIME = {off:.1f} s, expected {TAI_UTC_S} s: sends "
              f"will not line up with the switches' basetime. Set the kernel TAI offset first.",
              file=sys.stderr)


def load_in_scope_flows(schedule_path, endpoints_path, node):
    with open(schedule_path) as f:
        schedule = json.load(f)
    with open(endpoints_path) as f:
        endpoints = json.load(f)

    flows_by_id = {f["id"]: f for f in schedule["flows"]}
    # Flow ids aren't always small (some schedule packages use ids like
    # 300000+ for dynamically-added flows) -- BASE_PORT + id can exceed the
    # 65535 UDP port limit. Map each id to a rank over the *sorted* id list
    # instead, so the port stays in range and is still identical across every
    # node (all nodes load the same schedule.json and sort the same ids).
    port_by_id = {fid: BASE_PORT + rank for rank, fid in enumerate(sorted(flows_by_id))}
    for fid, flow in flows_by_id.items():
        flow["_port"] = port_by_id[fid]
    local_streams = endpoints.get(node, {}).get("streams", {})

    in_scope = []
    for name, stream in local_streams.items():
        flow_id = int(stream["flow_id"])
        flow = flows_by_id.get(flow_id)
        if flow is None:
            continue  # stream configured but not part of this schedule package
        in_scope.append((flow, stream))
    return schedule["cycle_ns"], in_scope


def first_hop_phase(flow):
    """ns after basetime (mod period) at which the flow's first-hop gate window opens."""
    hops = flow.get("hops")
    return hops[0]["psi_ns"] if hops else flow["offset_ns"]


def print_plan(node, cycle_ns, in_scope, basetime_ns):
    print(f"Node {node}: {len(in_scope)} in-scope flow(s), cycle {cycle_ns} ns, "
          + (f"basetime {basetime_ns} ns (TAI)" if basetime_ns is not None
             else "NO basetime.json: sends aligned to the TAI epoch, not to the GCLs") + "\n")
    for flow, stream in in_scope:
        print(f"  id={flow['id']:<3} {stream['role']:<8} vlan={stream['vlan']:<3} "
              f"{stream['ip']} <-> {stream['peer_ip']}  "
              f"pcp={flow['pcp']} frame={flow['size']}B (payload {payload_size(flow['size'])}B) "
              f"period={flow['period']}ns phase={first_hop_phase(flow)}ns deadline={flow['deadline']}ns "
              f"route={flow['route']}")


def payload_size(frame_size):
    """UDP payload that makes the frame on the wire exactly frame_size bytes."""
    if frame_size < MIN_FRAME:
        print(f"[WARN] frame size {frame_size}B is below the {MIN_FRAME}B minimum; "
              f"the NIC pads it to {MIN_FRAME}B", file=sys.stderr)
    return max(HEADER_SIZE, frame_size - FRAME_OVERHEAD)


def make_payload(size, tx_ns):
    return struct.pack(HEADER_FMT, tx_ns) + b"\0" * (size - HEADER_SIZE)


def next_release(now_ns, period_ns, anchor_ns):
    """first anchor + n*period strictly after now (all ints, ns)."""
    return anchor_ns + ((now_ns - anchor_ns) // period_ns + 1) * period_ns


def tai_ns():
    return time.clock_gettime_ns(time.CLOCK_TAI)


def sleep_until(t_ns):
    d = t_ns - tai_ns()
    if d > 0:
        time.sleep(d / 1e9)


def realtime(cpu):
    """pin this process to one CPU and give it SCHED_FIFO priority (needs root; skipped otherwise)."""
    try:
        if cpu is not None:
            os.sched_setaffinity(0, {cpu})
        os.sched_setscheduler(0, os.SCHED_FIFO, os.sched_param(50))
    except (PermissionError, OSError) as e:
        print(f"[WARN] real-time setup failed: {e}", file=sys.stderr)


def sender_proc(flows, basetime_ns, start_ns, end_ns, lead_ns, cpu, out):
    """all sender flows of this node in one loop, ordered by launch time. Each frame is handed to
    the kernel lead_ns early with its launch time; the NIC sends it at exactly that time."""
    if cpu is not False:
        realtime(cpu)
    socks, heap, stats = {}, [], {}
    for flow, stream in flows:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            # pcp 6 uses socket priority 5 (VLAN egress-qos-map 5:6): priority 6 is shared with
            # interactive-TOS traffic such as ssh, which must not enter the launch-time queue
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_PRIORITY, 5 if flow["pcp"] == 6 else flow["pcp"])
            sock.setsockopt(socket.SOL_SOCKET, SO_TXTIME, struct.pack("iI", time.CLOCK_TAI, 0))
        except PermissionError:
            stats[flow["id"]] = {"error": "permission (run with sudo)"}
            continue
        sock.bind((stream["ip"], 0))
        fid = flow["id"]
        socks[fid] = (sock, (stream["peer_ip"], flow["_port"]), payload_size(flow["size"]), flow["period"])
        stats[fid] = {"sent": 0, "skipped": 0}
        anchor = (basetime_ns or 0) + first_hop_phase(flow)
        heapq.heappush(heap, (next_release(max(tai_ns() + lead_ns, start_ns), flow["period"], anchor), fid))

    while heap:
        t, fid = heapq.heappop(heap)
        if t >= end_ns:
            continue
        sock, addr, size, period = socks[fid]
        sleep_until(t - lead_ns)
        if tai_ns() > t - ETF_DELTA_NS - LATE_MARGIN_NS:
            stats[fid]["skipped"] += 1  # handed over too late for its launch time: etf would drop it
        else:
            sock.sendmsg([make_payload(size, t)],
                         [(socket.SOL_SOCKET, SCM_TXTIME, struct.pack("Q", t))], 0, addr)
            stats[fid]["sent"] += 1
        heapq.heappush(heap, (t + period, fid))
    out.put(("sender", stats))


def receiver_proc(flows, end_ns, rcvbuf, cpu, out):
    """all receiver flows of this node in one epoll loop; latency = NIC RX timestamp - launch time,
    kept as running sums. A frame without a NIC timestamp is counted, not measured."""
    if cpu is not False:
        realtime(cpu)
    sel = selectors.DefaultSelector()
    anc_size = socket.CMSG_SPACE(48)
    stats = {}
    for flow, stream in flows:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, rcvbuf)
        sock.setsockopt(socket.SOL_SOCKET, SO_TIMESTAMPING, TS_FLAGS)
        sock.bind((stream["ip"], flow["_port"]))
        sock.setblocking(False)
        st = stats[flow["id"]] = dict(n=0, no_ts=0, sum=0, sumsq=0, min=None, max=None, last=None,
                                      absdiff=0, misses=0, deadline=flow["deadline"])
        sel.register(sock, selectors.EVENT_READ, st)

    while tai_ns() < end_ns:
        for key, _ in sel.select(timeout=0.2):
            sock, st = key.fileobj, key.data
            while True:
                try:
                    data, anc, _, _ = sock.recvmsg(2048, anc_size)
                except BlockingIOError:
                    break
                if len(data) < HEADER_SIZE:
                    continue
                rx = 0
                for level, ctype, cdata in anc:
                    if level == socket.SOL_SOCKET and ctype == SCM_TIMESTAMPING and len(cdata) >= 48:
                        hw_s, hw_n = struct.unpack("2q", cdata[32:48])  # third timespec: raw hardware
                        rx = hw_s * 1_000_000_000 + hw_n
                if not rx:
                    st["no_ts"] += 1
                    continue
                (tx,) = struct.unpack(HEADER_FMT, data[:HEADER_SIZE])
                lat = rx - tx
                st["n"] += 1
                st["sum"] += lat
                st["sumsq"] += lat * lat
                st["min"] = lat if st["min"] is None else min(st["min"], lat)
                st["max"] = lat if st["max"] is None else max(st["max"], lat)
                if st["last"] is not None:
                    st["absdiff"] += abs(lat - st["last"])
                st["last"] = lat
                st["misses"] += lat > st["deadline"]
    out.put(("receiver", stats))


def summarize(flow, role, st):
    if role == "sender":
        if st.get("error"):
            print(f"  id={flow['id']} sender: 0 packet(s) sent, ERROR: {st['error']}")
        else:
            print(f"  id={flow['id']} sender: {st['sent']} packet(s) sent, {st['skipped']} skipped")
        return
    n = st["n"]
    if not n:
        print(f"  id={flow['id']} receiver: 0 packets received" + (f", no_nic_ts={st['no_ts']}" if st.get("no_ts") else ""))
        return
    mean = st["sum"] / n
    # jitter: stddev of latency, and RFC 3550 (mean |difference| of consecutive packets' latency)
    stddev = max(st["sumsq"] / n - mean * mean, 0) ** 0.5
    rfc3550 = st["absdiff"] / (n - 1) if n > 1 else 0.0
    print(f"  id={flow['id']} receiver: {n} received, "
          f"latency ns min/avg/max = {st['min']}/{mean:.0f}/{st['max']}, "
          f"jitter ns stddev/rfc3550 = {stddev:.0f}/{rfc3550:.0f}, "
          f"deadline={flow['deadline']}ns, misses={st['misses']}, no_nic_ts={st['no_ts']}")


def main():
    ap = argparse.ArgumentParser(description="Generate/receive traffic for a GCL schedule's flows")
    ap.add_argument("--schedule", required=True, help="schedule.json")
    ap.add_argument("--endpoints", required=True,
                     help="endpoints.json written by configureManager.py --endpoints")
    ap.add_argument("--node", required=True, help="which endpoints.json node this host is (e.g. S1)")
    ap.add_argument("--basetime", default=None,
                     help="basetime.json from configure_gcl.py (default: next to --schedule)")
    ap.add_argument("--run", action="store_true",
                     help="actually open sockets and send/receive (default: dry-run, print the plan)")
    ap.add_argument("--duration", type=float, default=30, help="seconds of sending (default 30)")
    ap.add_argument("--start-at", type=float, default=None,
                     help="CLOCK_TAI time (s) at which senders start, so all nodes send the same "
                          "window (default: 2 s from now). Receivers listen from launch.")
    ap.add_argument("--lead-us", type=float, default=1000,
                     help="hand each frame to the kernel this long before its launch time (default 1000)")
    ap.add_argument("--rcvbuf", type=int, default=4 << 20, help="SO_RCVBUF per receiver socket (default 4 MiB)")
    ap.add_argument("--rt", action=argparse.BooleanOptionalAction, default=True,
                     help="pin sender/receiver to their own CPUs, SCHED_FIFO, CPU power-saving states off "
                          "(default; needs root)")
    args = ap.parse_args()

    cycle_ns, in_scope = load_in_scope_flows(args.schedule, args.endpoints, args.node)
    if not in_scope:
        print(f"[FATAL] no in-scope flows for node '{args.node}' in {args.endpoints}",
              file=sys.stderr)
        return 1

    basetime_path = args.basetime or os.path.join(
        os.path.dirname(os.path.abspath(args.schedule)), "basetime.json")
    basetime_ns = load_basetime(basetime_path)
    check_tai_offset()
    print_plan(args.node, cycle_ns, in_scope, basetime_ns)
    if not args.run:
        print("\nDry-run only. Re-run with --run to actually send/receive.")
        return 0

    nic = in_scope[0][1]["iface"].split(".")[0]
    qd = os.popen(f"tc qdisc show dev {nic} 2>/dev/null").read()
    if qd.count("offload on") < 2 or "etf" not in qd:
        print(f"[FATAL] no launch-time queues on {nic}: run 'sudo ./gptp.sh launchtime on' "
              f"(time-sync-gptp/) first", file=sys.stderr)
        return 1
    start_ns = int(args.start_at * 1e9) if args.start_at else tai_ns() + 2_000_000_000
    end_ns = start_ns + int(args.duration * 1e9)
    lead_ns = int(args.lead_us * 1000)
    senders = [(f, s) for f, s in in_scope if s["role"] == "sender"]
    receivers = [(f, s) for f, s in in_scope if s["role"] == "receiver"]
    cpus = sorted(os.sched_getaffinity(0))
    tx_cpu = rx_cpu = False  # False: no real-time setup
    dma = None
    if args.rt:
        tx_cpu, rx_cpu = cpus[-1], (cpus[-2] if len(cpus) > 1 else cpus[-1])
        try:  # keep CPUs out of deep idle states while this file is open
            dma = open("/dev/cpu_dma_latency", "wb", buffering=0)
            dma.write(struct.pack("i", 0))
        except OSError as e:
            print(f"[WARN] /dev/cpu_dma_latency: {e}", file=sys.stderr)

    out = mp.Queue()
    procs = [mp.Process(target=receiver_proc, args=(receivers, end_ns + 300_000_000, args.rcvbuf, rx_cpu, out))]
    if senders:
        procs.append(mp.Process(target=sender_proc,
                                args=(senders, basetime_ns, start_ns, end_ns, lead_ns, tx_cpu, out)))
    print(f"\n{len(senders)} sender / {len(receivers)} receiver flow(s); sending "
          f"{args.duration:g} s from TAI {start_ns / 1e9:.3f}, NIC launch time"
          + (f", real-time on CPU {tx_cpu} (tx) / {rx_cpu} (rx)" if args.rt else "") + " ...")
    for p in procs:
        p.start()
    results = {}
    for _ in procs:
        role, stats = out.get()
        results[role] = stats
    for p in procs:
        p.join()
    if dma:
        dma.close()

    print("\nSummary:")
    for flow, stream in in_scope:
        role = stream["role"]
        summarize(flow, role, results.get(role, {}).get(flow["id"], {"n": 0, "sent": 0, "skipped": 0}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
