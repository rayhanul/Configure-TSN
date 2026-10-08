#!/usr/bin/env python3
"""
bench_netconf.py
----------------
NETCONF counterpart of ../gcl-schedule-update/run-tsn-config-cnc.py, so you can
put a number next to the "16-64 ms" the tsntool path reports and decide whether
NETCONF is worth it.

It uses the SAME methodology as run-tsn-config-cnc.py: the session is opened
FIRST (connection setup is NOT counted), then a timer wraps only the act of
pushing + activating one port's gate control list. For NETCONF that act is
<edit-config> to candidate + <commit>, which is the true apples-to-apples
analog of one `tsntool st wrcl` + `tsntool st configure`.

It additionally splits the window into edit-config vs commit, because on these
boards the sysrepo commit (candidate->running->plugin->driver) is expected to
dominate -- that breakdown is exactly what tells you whether NETCONF can ever
beat tsntool here, or whether the datastore commit is a fixed floor.

Run:
    python3 bench_netconf.py --host 192.168.0.1 --user root --cfg <one>.cfg \
        --iface sw0p3 --cycle-ns 800000 [--repeat 20] [--tick-ns 320]
"""

import argparse
import statistics
import sys
import time

import gcl_common as gc
import netconf_sched as ns


def main():
    ap = argparse.ArgumentParser(
        description="Time one NETCONF GCL update (edit-config + commit), "
                    "connection setup excluded -- comparable to run-tsn-config-cnc.py")
    ap.add_argument("--host", required=True)
    ap.add_argument("--user", required=True)
    ap.add_argument("--password", default="",
                    help="switch password (empty tries key/agent auth)")
    ap.add_argument("--cfg", required=True, help="one <switch>-<port>.cfg file")
    ap.add_argument("--iface", required=True, help="e.g. sw0p3")
    ap.add_argument("--cycle-ns", type=int, required=True)
    ap.add_argument("--tick-ns", type=int, default=None,
                    help="round to this tick (default: read from switch; "
                         "DE-IP boards report 320)")
    ap.add_argument("--no-round-to-tick", action="store_true")
    ap.add_argument("--netconf-port", type=int, default=830)
    ap.add_argument("--repeat", type=int, default=1,
                    help="repeat the timed update N times (reuse one session)")
    ap.add_argument("--lead-seconds", type=float, default=2.0)
    args = ap.parse_args()

    with open(args.cfg) as f:
        entries = gc.parse_cfg_entries(gc.strip_trailing_comments(f.read()))
    cycle_num, cycle_den = gc.reduce_cycle(args.cycle_ns)

    print(f"Connecting to {args.user}@{args.host}:{args.netconf_port} "
          f"(not timed)...")
    conn_start = time.perf_counter()
    m = ns.connect(args.host, args.user, args.password, port=args.netconf_port)
    conn_ms = (time.perf_counter() - conn_start) * 1e3
    print(f"  session up in {conn_ms:.1f} ms (setup cost, excluded from the "
          f"comparison below)")

    try:
        tick_ns = args.tick_ns
        if not args.no_round_to_tick and tick_ns is None:
            tick_ns = ns.read_tick_ns(m, args.iface)
            if tick_ns is None:
                print("[WARN] switch did not report tick-granularity; "
                      "assuming 320 ns", file=sys.stderr)
                tick_ns = 320
        if not args.no_round_to_tick:
            entries = gc.round_to_tick(entries, tick_ns, args.cycle_ns)
        print(f"  {len(entries)} gate-control entries, tick "
              f"{tick_ns if not args.no_round_to_tick else 'n/a'} ns\n")

        edit_samples, commit_samples, total_samples = [], [], []
        for i in range(args.repeat):
            base_total = (time.clock_gettime_ns(
                getattr(time, "CLOCK_TAI", time.CLOCK_REALTIME))
                + int(args.lead_seconds * 1e9))
            base_sec, base_ns = divmod(base_total, 1_000_000_000)
            xml = ns.build_gate_parameters_config(
                args.iface, entries, cycle_num, cycle_den,
                base_seconds=base_sec, base_nanos=base_ns)
            config = f"<config>{xml}</config>"

            # ---- timed window: edit-config to candidate, then commit ----
            t0 = time.perf_counter()
            m.edit_config(target="candidate", config=config,
                          default_operation="merge")
            t1 = time.perf_counter()
            m.commit()
            t2 = time.perf_counter()

            edit_ms = (t1 - t0) * 1e3
            commit_ms = (t2 - t1) * 1e3
            total_ms = (t2 - t0) * 1e3
            edit_samples.append(edit_ms)
            commit_samples.append(commit_ms)
            total_samples.append(total_ms)
            print(f"  run {i+1:2d}: edit-config {edit_ms:7.2f} ms | "
                  f"commit {commit_ms:7.2f} ms | TOTAL {total_ms:7.2f} ms")

        print("\n" + "=" * 60)
        print("NETCONF GCL UPDATE TIME  (connection setup excluded)")
        print("=" * 60)

        def summarize(label, s):
            if len(s) == 1:
                print(f"{label:12s}: {s[0]:.2f} ms")
            else:
                print(f"{label:12s}: min {min(s):.2f}  median "
                      f"{statistics.median(s):.2f}  max {max(s):.2f} ms")

        summarize("edit-config", edit_samples)
        summarize("commit", commit_samples)
        summarize("TOTAL", total_samples)
        print("=" * 60)
        print("Compare TOTAL against run-tsn-config-cnc.py's 'CNC time' (16-64 ms).")
    finally:
        try:
            m.close_session()
        except Exception:
            pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
