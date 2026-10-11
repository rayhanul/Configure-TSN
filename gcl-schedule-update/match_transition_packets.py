#!/usr/bin/env python3
"""Compare baseline and activation using equal transmitted counts per flow/trial."""
import argparse
import csv
import json
from pathlib import Path

import numpy as np

import loss_during_update as loss


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("experiment", type=Path)
    root = parser.parse_args().experiment.resolve()
    config = json.loads((root / "experiment_config.json").read_text())
    schedule = json.loads((Path(loss.REPO) / config["source"] / "schedule.json").read_text())
    deadlines = {int(f["id"]): f["deadline"] for f in schedule["flows"] if f.get("scheduled")}
    records = []
    for trial, driver in enumerate(sorted(root.glob("driver_*.log")), 1):
        run = Path(next(line[9:] for line in driver.read_text().splitlines()
                        if line.startswith("Results: ")))
        meta = json.loads((run / "updates.json").read_text())
        update = meta["updates"][0]
        tx, rx = loss.load_logs(str(run), meta["nodes"])
        for fid, deadline in sorted(deadlines.items()):
            sent = np.sort(tx[tx[:, 0] == fid, 1])
            during = sent[(sent >= update["t_first_send"]) & (sent < update["t_last_cct"])]
            before = sent[(sent >= meta["start_ns"]) & (sent < update["t_first_send"])]
            assert len(during) > 0 and len(before) >= len(during)
            before = before[-len(during):]
            received = rx[rx[:, 0] == fid]
            late = received[(received[:, 2] > 0) &
                            (received[:, 2] - received[:, 1] > deadline), 1]
            for phase, selected in (("before", before), ("during", during)):
                records.append(dict(trial=trial, flow=fid, phase=phase, sent=len(selected),
                                    lost=int((~np.isin(selected, received[:, 1])).sum()),
                                    deadline_misses=int(np.isin(selected, late).sum()),
                                    first_launch_ns=int(selected[0]),
                                    last_launch_ns=int(selected[-1])))
    assert len(records) == config["repetitions"] * len(deadlines) * 2
    with (root / "equal_count_packets.csv").open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(records[0]))
        writer.writeheader()
        writer.writerows(records)
    lines = ["# Equal transmitted-packet comparison", "",
             "Reanalysis of the existing three trials; no additional testbed run. For each "
             "flow in each trial, retain all packets launched during activation and select "
             "the same number of its most recent transmitted packets before the first CNC "
             "command. This matches both the total packet count and the flow composition. "
             "Baseline selection boundaries differ slightly by flow. Original full-window "
             "results remain in SUMMARY.md.", "",
             "| Phase | Transmitted packets | Deadline misses | Deadline-miss rate | Lost |",
             "|---|---:|---:|---:|---:|"]
    totals = {}
    for phase in ("before", "during"):
        rows = [r for r in records if r["phase"] == phase]
        sent = sum(r["sent"] for r in rows)
        misses = sum(r["deadline_misses"] for r in rows)
        lost = sum(r["lost"] for r in rows)
        totals[phase] = sent
        lines.append(f"| {phase} activation | {sent:,} | {misses:,} | "
                     f"{100 * misses / sent:.2f}% | {lost:,} |")
    assert totals["before"] == totals["during"]
    lines += ["", "Suggested caption: Deadline compliance before and during GCL activation, "
              "using equal transmitted-packet counts per flow and trial. Results aggregate "
              "three transitions from the RL C9-on schedule to the Problem 3 heuristic C9-on "
              "schedule on 17 ports across eight switches.", "",
              "All observed deadline misses occurred on flows 7 and 8, which the replacement "
              "schedule does not admit. This comparison therefore includes a changed admission "
              "set and does not isolate activation transients. Skipped sender releases are "
              "excluded from transmitted-packet counts. The original analysis inferred 64 "
              "skipped releases during activation.", "",
              "Per-flow counts and selected launch-time ranges: equal_count_packets.csv.", ""]
    (root / "EQUAL_COUNT_COMPARISON.md").write_text("\n".join(lines))
    print("\n".join(lines))


if __name__ == "__main__":
    main()
