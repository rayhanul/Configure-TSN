#!/usr/bin/env python3
"""
gen_traffic.py
---------------
Generate and receive real traffic for the flows in a GCL schedule.json,
using the VLAN/IP addressing that Network-Configure-Manager/configureManager.py
already set up (read from its --endpoints output).

A flow is in scope for a given --node only if configureManager.py actually
admitted it for that node (i.e. it appears in endpoints.json's streams for
that node) -- flows whose other endpoint isn't physically present (no
endpoints.json entry was ever created for them) are silently out of scope,
no hardcoded flow-id list needed.

Each in-scope flow is:
  - a periodic UDP sender (role "sender"): SO_PRIORITY set to the flow's
    PCP, payload = 8-byte send timestamp + padding to the flow's size,
    sent every `period` ns at the flow's `offset_ns` within the cycle.
  - a UDP receiver (role "receiver") logging one-way latency (valid because
    sender and receiver are already PTP-synchronized -- see
    clock-syncrhonize-ptp/) against the flow's `deadline`.

Timing precision: Python userspace `time.sleep` realistically achieves
~tens-to-hundreds of microseconds of jitter on Linux, not the sub-microsecond
precision the schedule's GCL windows are computed for (periods here are
200-400us, smaller than typical sleep jitter). This gets the period and
rough offset right and exercises the right PCP/queue; it is not a hard
real-time per-packet guarantee. See README.md.

Run:
    python3 gen_traffic.py --schedule <schedule.json> --endpoints <endpoints.json> --node S1   # dry-run
    sudo python3 gen_traffic.py --schedule <schedule.json> --endpoints <endpoints.json> --node S2 --run --duration 30
"""

import argparse
import json
import math
import socket
import struct
import sys
import threading
import time

BASE_PORT = 50000
HEADER_FMT = "d"  # send timestamp, float64 seconds (time.time())
HEADER_SIZE = struct.calcsize(HEADER_FMT)


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


def print_plan(node, cycle_ns, in_scope):
    print(f"Node {node}: {len(in_scope)} in-scope flow(s), cycle {cycle_ns} ns\n")
    for flow, stream in in_scope:
        print(f"  id={flow['id']:<3} {stream['role']:<8} vlan={stream['vlan']:<3} "
              f"{stream['ip']} <-> {stream['peer_ip']}  "
              f"pcp={flow['pcp']} size={flow['size']}B period={flow['period']}ns "
              f"offset={flow['offset_ns']}ns deadline={flow['deadline']}ns "
              f"route={flow['route']}")


def make_payload(size, send_ts):
    header = struct.pack(HEADER_FMT, send_ts)
    if size < HEADER_SIZE:
        raise ValueError(f"flow size {size}B is smaller than the {HEADER_SIZE}B "
                          f"timestamp header")
    return header + b"\0" * (size - HEADER_SIZE)


def next_release(now, period_s, offset_s):
    n = math.floor((now - offset_s) / period_s)
    t = n * period_s + offset_s
    while t <= now:
        t += period_s
    return t


def sender_loop(flow, stream, stop_event, stats):
    period_s = flow["period"] / 1e9
    offset_s = flow["offset_ns"] / 1e9
    port = flow["_port"]

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_PRIORITY, flow["pcp"])
    except PermissionError:
        print(f"[id={flow['id']}] ERROR: setting SO_PRIORITY={flow['pcp']} needs "
              f"root (pcp>6 needs CAP_NET_ADMIN) -- run with sudo.", file=sys.stderr)
        stats["error"] = "permission"
        return
    sock.bind((stream["ip"], 0))

    sent = 0
    t = next_release(time.time(), period_s, offset_s)
    while not stop_event.is_set():
        now = time.time()
        wait = t - now
        if wait > 0:
            stop_event.wait(wait)
            if stop_event.is_set():
                break
        send_ts = time.time()
        payload = make_payload(flow["size"], send_ts)
        try:
            sock.sendto(payload, (stream["peer_ip"], port))
            sent += 1
        except OSError as e:
            print(f"[id={flow['id']}] send error: {e}", file=sys.stderr)
        t += period_s
    sock.close()
    stats["sent"] = sent


def receiver_loop(flow, stream, stop_event, stats):
    port = flow["_port"]
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((stream["ip"], port))
    sock.settimeout(0.5)

    latencies_ns = []
    misses = 0
    while not stop_event.is_set():
        try:
            data, _ = sock.recvfrom(65535)
        except socket.timeout:
            continue
        recv_ts = time.time()
        if len(data) < HEADER_SIZE:
            continue
        (send_ts,) = struct.unpack(HEADER_FMT, data[:HEADER_SIZE])
        latency_ns = (recv_ts - send_ts) * 1e9
        latencies_ns.append(latency_ns)
        if latency_ns > flow["deadline"]:
            misses += 1
    sock.close()
    stats["latencies_ns"] = latencies_ns
    stats["misses"] = misses


def summarize(flow, stream, stats):
    if stream["role"] == "sender":
        print(f"  id={flow['id']} sender: {stats.get('sent', 0)} packet(s) sent")
        if stats.get("error"):
            print(f"    ERROR: {stats['error']}")
        return
    lat = stats.get("latencies_ns", [])
    if not lat:
        print(f"  id={flow['id']} receiver: 0 packets received")
        return
    mean = sum(lat) / len(lat)
    # jitter, two common definitions:
    #  - stddev of latency: overall spread around the mean
    #  - RFC 3550 interarrival jitter: mean absolute difference between
    #    consecutive packets' latency (what RTP/VoIP calls "jitter")
    variance = sum((x - mean) ** 2 for x in lat) / len(lat)
    stddev = variance ** 0.5
    if len(lat) > 1:
        consecutive_abs_diffs = [abs(lat[i] - lat[i - 1]) for i in range(1, len(lat))]
        rfc3550_jitter = sum(consecutive_abs_diffs) / len(consecutive_abs_diffs)
    else:
        rfc3550_jitter = 0.0
    print(f"  id={flow['id']} receiver: {len(lat)} received, "
          f"latency ns min/avg/max = {min(lat):.0f}/{mean:.0f}/{max(lat):.0f}, "
          f"jitter ns stddev/rfc3550 = {stddev:.0f}/{rfc3550_jitter:.0f}, "
          f"deadline={flow['deadline']}ns, misses={stats.get('misses', 0)}")


def main():
    ap = argparse.ArgumentParser(description="Generate/receive traffic for a GCL schedule's flows")
    ap.add_argument("--schedule", required=True, help="schedule.json")
    ap.add_argument("--endpoints", required=True,
                     help="endpoints.json written by configureManager.py --endpoints")
    ap.add_argument("--node", required=True, help="which endpoints.json node this host is (e.g. S1)")
    ap.add_argument("--run", action="store_true",
                     help="actually open sockets and send/receive (default: dry-run, print the plan)")
    ap.add_argument("--duration", type=float, default=None,
                     help="stop after this many seconds (default: run until Ctrl-C)")
    args = ap.parse_args()

    cycle_ns, in_scope = load_in_scope_flows(args.schedule, args.endpoints, args.node)
    if not in_scope:
        print(f"[FATAL] no in-scope flows for node '{args.node}' in {args.endpoints}",
              file=sys.stderr)
        return 1

    print_plan(args.node, cycle_ns, in_scope)
    if not args.run:
        print("\nDry-run only. Re-run with --run to actually send/receive.")
        return 0

    stop_event = threading.Event()
    threads = []
    stats_by_id = {}
    for flow, stream in in_scope:
        stats = {}
        stats_by_id[flow["id"]] = stats
        target = sender_loop if stream["role"] == "sender" else receiver_loop
        th = threading.Thread(target=target, args=(flow, stream, stop_event, stats), daemon=True)
        threads.append(th)

    print(f"\nStarting {len(threads)} thread(s)"
          + (f" for {args.duration}s" if args.duration else " (Ctrl-C to stop") + " ...")
    for th in threads:
        th.start()

    try:
        if args.duration:
            time.sleep(args.duration)
        else:
            while True:
                time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        stop_event.set()
        for th in threads:
            th.join(timeout=2)

    print("\nSummary:")
    for flow, stream in in_scope:
        summarize(flow, stream, stats_by_id[flow["id"]])
    return 0


if __name__ == "__main__":
    sys.exit(main())
