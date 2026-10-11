#!/usr/bin/env python3
"""Summarize a continuous-traffic GCL transition, including affected switches.

Usage: python3 summarize_transition.py <experiment-dir>
Run directories are read from driver_*.log; raw packet logs remain in those runs.
"""
import argparse
import csv
import json
import os
from pathlib import Path

import numpy as np

import loss_during_update as loss


def write_csv(path, rows):
    with path.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("experiment", type=Path)
    args = parser.parse_args()
    root = args.experiment.resolve()
    config = json.loads((root / "experiment_config.json").read_text())
    source = Path(loss.REPO) / config["source"]
    target = Path(loss.REPO) / config["target"]
    schedule = json.loads((source / "schedule.json").read_text())
    target_doc = json.loads((target / "schedule.json").read_text())
    flows = {int(f["id"]): f for f in schedule["flows"] if f.get("scheduled")}
    target_ids = {int(f["id"]) for f in target_doc["flows"] if f.get("scheduled")}
    rows, switches, flow_rows, runs, skip_rows = [], [], [], [], []
    for trial, driver in enumerate(sorted(root.glob("driver_*.log")), 1):
        run = next(Path(line.removeprefix("Results: ")) for line in driver.read_text().splitlines()
                   if line.startswith("Results: "))
        meta = json.loads((run / "updates.json").read_text())
        assert meta["nodes"] == ["S1", "S2", "S3"] and not meta["skipped_nodes"]
        assert set(meta["flows"]) == set(flows) and len(flows) == 29
        assert len(meta["updates"]) == 1
        update = meta["updates"][0]
        assert update["live_ports"] == update["ports"] == 17
        tx, rx = loss.load_logs(str(run), meta["nodes"])
        tx = tx[np.isin(tx[:, 0], list(flows))]
        rx = rx[np.isin(rx[:, 0], list(flows))]
        assert set(map(int, np.unique(tx[:, 0]))) == set(flows)
        key = lambda data: data[:, 0] * (1 << 40) + data[:, 1] - meta["start_ns"] + (1 << 38)
        got = np.isin(key(tx), key(rx))
        misses = (rx[:, 2] > 0) & (rx[:, 2] - rx[:, 1] >
                                  np.array([flows[int(fid)]["deadline"] for fid in rx[:, 0]]))
        ports = list(csv.DictReader((run / "ports.csv").open()))
        assert len(ports) == 17 and all(p["live"] == "1" for p in ports)
        samples = {s["label"]: s["counters"] for s in meta["switch_queue_samples"]}
        phase_samples = [("before_traffic", "before_update"),
                         ("before_update", "after_update"),
                         ("after_update", "after_traffic")]
        for phase, (before, after) in zip(meta["phases"], phase_samples):
            deltas = [samples[after][p]["count"] - samples[before][p]["count"]
                      for p in samples[before]]
            assert len(deltas) == 17 and min(deltas) >= 0, "missing/reset queue counter"
            rows.append(dict(trial=trial, phase=phase["phase"], sent=phase["sent"],
                             lost=phase["lost"], loss_pct=phase["loss_pct"],
                             deadline_misses=phase["deadline_miss"],
                             duration_ms=phase["length_ms"], queue_drops=sum(deltas),
                             activation_ms=update["update_ms"], run=str(run)))
        bounds = [("before", meta["start_ns"], update["t_first_send"]),
                  ("during", update["t_first_send"], update["t_last_cct"]),
                  ("after", update["t_last_cct"], meta["end_ns"])]
        for fid in sorted(flows):
            launches = np.sort(tx[tx[:, 0] == fid, 1])
            period = flows[fid]["period"]
            missing = np.array([int(a) + k * period
                                for a, gap in zip(launches[:-1], np.diff(launches))
                                if gap > period for k in range(1, int(gap) // period)],
                               dtype=np.int64)
            for phase, a, b in bounds:
                skip_rows.append(dict(trial=trial, flow=fid, phase=phase,
                                      inferred_skipped_launches=int(((missing >= a) &
                                                                     (missing < b)).sum())))
                sent = (tx[:, 0] == fid) & (tx[:, 1] >= a) & (tx[:, 1] < b)
                received = (rx[:, 0] == fid) & (rx[:, 1] >= a) & (rx[:, 1] < b)
                flow_rows.append(dict(trial=trial, flow=fid, phase=phase,
                                      in_target=int(fid in target_ids), sent=int(sent.sum()),
                                      lost=int((sent & ~got).sum()),
                                      deadline_misses=int((received & misses).sum())))
        for sw in sorted({p["switch"] for p in ports}):
            own = [p for p in ports if p["switch"] == sw]
            first = min(int(p["t_send"]) for p in own)
            last = max(int(p["cct"]) for p in own)
            routed = [fid for fid, f in flows.items() if sw in f["route"]]
            mask = np.isin(tx[:, 0], routed)
            record = dict(trial=trial, switch=sw, ports=len(own), routed_flows=len(routed),
                          first_command_ms=(first - meta["start_ns"]) / 1e6,
                          last_activation_ms=(last - meta["start_ns"]) / 1e6,
                          activation_window_ms=(last - first) / 1e6)
            for phase, a, b in bounds + [("own_activation", first, last)]:
                sent = mask & (tx[:, 1] >= a) & (tx[:, 1] < b)
                record[phase + "_sent"] = int(sent.sum())
                record[phase + "_lost"] = int((sent & ~got).sum())
            for phase, (before, after) in zip(("before", "during", "after"), phase_samples):
                record[phase + "_queue_drops"] = sum(
                    samples[after][p]["count"] - samples[before][p]["count"]
                    for p in samples[before] if p.startswith(sw + "/"))
            switches.append(record)
        runs.append(dict(trial=trial, run=str(run), update=update,
                         host_counter_delta=meta.get("host_counter_delta", {})))
    assert len(runs) == config["repetitions"], "not all trials completed"
    write_csv(root / "phases.csv", rows)
    write_csv(root / "switches.csv", switches)
    write_csv(root / "flows.csv", flow_rows)
    write_csv(root / "sender_skips.csv", skip_rows)
    (root / "combined.json").write_text(json.dumps(dict(config=config, runs=runs,
                                                       phases=rows, switches=switches), indent=2) + "\n")
    lines = ["# RL29 → heuristic28: GCL transition under continuous traffic", "",
             "Three 30-second trials on S1, S2 and S3. All 29 current TT flows kept their RL "
             "send offsets, queue priorities, VLANs, endpoints and MSTP routes throughout each trial. "
             "At about +10 seconds, the CNC sent the Problem 3 heuristic C9-on GCL to all 17 affected "
             "ports of sw01–sw08, sequentially. All 17 ports activated in every trial. Original RL "
             "GCLs were restored after traffic stopped in each trial.", "",
             "Before = traffic start to first GCL command; during = first command to last hardware "
             "ConfigChangeTime; after = the remainder. A lost packet is a sender-log entry with no "
             "matching receiver entry (flow ID + launch time). Received late packets are deadline "
             "misses, separately from loss.", "",
             "| Trial | Update (ms) | Before lost / sent | During lost / sent | After lost / sent | "
             "Deadline misses before / during / after |", "|---|---:|---:|---:|---:|---:|"]
    for trial in range(1, len(runs) + 1):
        r = [p for p in rows if p["trial"] == trial]
        counts = " | ".join(f"{p['lost']:,} / {p['sent']:,}" for p in r)
        miss = " / ".join(f"{p['deadline_misses']:,}" for p in r)
        lines.append(f"| {trial} | {r[0]['activation_ms']:.2f} | {counts} | {miss} |")
    lines += ["", "| Phase (all trials) | Sent | Lost | Loss % | Deadline misses | Switch queue drops |",
              "|---|---:|---:|---:|---:|---:|"]
    for phase in ("before", "during update 1", "after update 1"):
        r = [p for p in rows if p["phase"] == phase]
        sent, lost = sum(p["sent"] for p in r), sum(p["lost"] for p in r)
        lines.append(f"| {phase} | {sent:,} | {lost:,} | {100 * lost / sent:.6f} | "
                     f"{sum(p['deadline_misses'] for p in r):,} | {sum(p['queue_drops'] for p in r):,} |")
    lines += ["", "## Affected switches", "",
              "Packet columns below are end-to-end losses for flows whose route crosses that switch, "
              "classified by packet launch time. They overlap across switches and must not be summed "
              "or interpreted as identifying the switch that dropped a packet. Queue-drop columns "
              "are actual per-port hardware counter increases, summed within each switch.", "",
              "| Switch | Ports | Routed flows | Activation window ms, median (min–max) | "
              "Before lost / sent | Network-transition lost / sent | Own-activation lost / sent | "
              "Queue drops before / during / after |", "|---|---:|---:|---:|---:|---:|---:|---:|"]
    for sw in sorted({p["switch"] for p in switches}):
        r = [p for p in switches if p["switch"] == sw]
        durations = [p["activation_window_ms"] for p in r]
        counts = " | ".join(f"{sum(p[k + '_lost'] for p in r):,} / "
                            f"{sum(p[k + '_sent'] for p in r):,}"
                            for k in ("before", "during", "own_activation"))
        qdrops = " / ".join(str(sum(p[k + "_queue_drops"] for p in r))
                             for k in ("before", "during", "after"))
        lines.append(f"| {sw} | {r[0]['ports']} | {r[0]['routed_flows']} | "
                     f"{np.median(durations):.2f} ({min(durations):.2f}–{max(durations):.2f}) | "
                     f"{counts} | {qdrops} |")
    lines += ["", "Queue counters are sampled near phase boundaries, with each read bracketed by "
              "switch-clock timestamps saved in updates.json. Sampling adds overhead to the measured "
              "network transition. Queue counters include all traffic on the affected ports.", "",
              f"The target package does not admit these current RL flow IDs: {sorted(set(flows) - target_ids)}. "
              "They continued transmitting as requested. Target GCLs and unchanged RL sender timing "
              "are a different steady state from deploying the heuristic package with its own "
              "flow selection and transmit offsets; after-phase deadline misses must be assessed "
              "separately from packet loss during activation.", "",
              "## Sender continuity", "",
              "Generators remained running through each update. Late host wakeups caused some "
              "scheduled releases to be skipped before socket submission. These are not included "
              "in sent-packet loss. Counts below are inferred from gaps between recorded launch "
              "times and exclude any skips before a flow's first or after its last logged send.", "",
              "| Trial | Skipped releases before | During | After |",
              "|---|---:|---:|---:|"]
    for trial in range(1, len(runs) + 1):
        counts = [sum(r["inferred_skipped_launches"] for r in skip_rows
                      if r["trial"] == trial and r["phase"] == phase)
                  for phase in ("before", "during", "after")]
        lines.append(f"| {trial} | " + " | ".join(map(str, counts)) + " |")
    verification_file = root / "final_verification.json"
    if verification_file.exists():
        verification = json.loads(verification_file.read_text())
        assert verification["all_gcls_match_initial"] and verification["restored_ports"] == 17
        lines += ["", "Final live readback verified that all 17 ports match the initial RL GCLs "
                  "and cycle times. No generator remains running on S1, S2 or S3. Evidence: "
                  "final_gcl_snapshot.json and final_verification.json."]
    lines += ["",
              "## Flows with loss or missed deadlines", "",
              "| Flow | Admitted by target | Before lost / misses | During lost / misses | "
              "After lost / misses |", "|---|---|---:|---:|---:|"]
    for fid in sorted(flows):
        records = [p for p in flow_rows if p["flow"] == fid]
        if not any(p["lost"] or p["deadline_misses"] for p in records):
            continue
        counts = []
        for phase in ("before", "during", "after"):
            r = [p for p in records if p["phase"] == phase]
            counts.append(f"{sum(p['lost'] for p in r):,} / {sum(p['deadline_misses'] for p in r):,}")
        lines.append(f"| {fid} | {'yes' if fid in target_ids else 'no'} | " + " | ".join(counts) + " |")
    lines += ["", "Host counter changes per run (receive-buffer errors and ETF drops; ETF may also "
              "count non-test control packets):", "", "```json", json.dumps(
                  [r["host_counter_delta"] for r in runs], indent=2), "```", "",
              "Raw run summaries and packet logs:", ""]
    for r in runs:
        rel = os.path.relpath(r["run"], root)
        lines.append(f"- Trial {r['trial']}: [{Path(r['run']).name}]({rel}/summary.md).")
    lines += ["", "Machine-readable phase, switch and flow tables: phases.csv, switches.csv, flows.csv. "
              "Exact per-port activation timestamps: each run's ports.csv.", ""]
    (root / "SUMMARY.md").write_text("\n".join(lines))
    print("\n".join(lines[:24]))
    print(f"Full report: {root / 'SUMMARY.md'}")


if __name__ == "__main__":
    main()
