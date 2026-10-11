#!/usr/bin/env python3
"""Export the equal-count deadline-miss comparison as a paper figure."""
import argparse
import csv
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("experiment", type=Path)
    root = parser.parse_args().experiment.resolve()
    with (root / "equal_count_packets.csv").open() as fh:
        rows = list(csv.DictReader(fh))
    phases = ("before", "during")
    sent = [sum(int(r["sent"]) for r in rows if r["phase"] == p) for p in phases]
    misses = [sum(int(r["deadline_misses"]) for r in rows if r["phase"] == p)
              for p in phases]
    assert sent[0] == sent[1] and sent[0] > 0
    trials = len({r["trial"] for r in rows})
    rates = [100 * m / n for m, n in zip(misses, sent)]
    plt.rcParams.update({"font.family": "serif", "font.size": 9,
                         "axes.labelsize": 10, "pdf.fonttype": 42,
                         "ps.fonttype": 42, "svg.fonttype": "none"})
    fig, ax = plt.subplots(figsize=(3.45, 2.8))
    fig.subplots_adjust(left=.18, right=.97, top=.95, bottom=.29)
    bars = ax.bar([0, 1], rates, width=.52, color=["#C9D2DA", "#A8BDCE"],
                  edgecolor="#465565", linewidth=.7, zorder=3)
    bars[1].set_hatch("///")
    for x, value in enumerate(rates):
        ax.text(x, value + .22, f"{value:.2f}%\n{misses[x]:,} misses",
                ha="center", va="bottom", fontsize=10, color="#303840")
    ax.set_xticks([0, 1], ["Before activation", "During activation"])
    ax.set_ylabel("Deadline-miss rate (%)")
    ax.set_ylim(0, 10)
    ax.set_yticks([0, 2, 4, 6, 8])
    ax.set_xlim(-.65, 1.65)
    ax.set_axisbelow(True)
    ax.grid(axis="y", color=".87", linewidth=.5)
    ax.spines[["top", "right"]].set_visible(False)
    ax.tick_params(axis="x", length=0, pad=8)
    fig.text(.5, .095, f"{sent[0]:,} transmitted packets per phase\n"
             f"Counts matched per flow and trial; {trials} trials",
             ha="center", va="center", fontsize=8)
    stem = root / "deadline_misses_equal_count"
    for ext in ("pdf", "svg", "png"):
        fig.savefig(stem.with_suffix("." + ext), dpi=600, facecolor="white")
    svg = stem.with_suffix(".svg")
    svg.write_text("\n".join(line.rstrip() for line in svg.read_text().splitlines()) + "\n")
    plt.close(fig)
    caption = ("Deadline compliance before and during online GCL replacement on a physical "
               "TSN testbed. Results aggregate three transitions from RL C9-on to Problem 3 "
               "heuristic C9-on across 17 ports on eight switches. Baseline transmitted-packet "
               "counts are matched to the activation counts per flow and trial (353,280 per "
               "phase). Deadline misses increase from 0 to 25,959 (7.35%); all misses occur on "
               "flows 7 and 8, which the replacement schedule does not admit. Skipped sender "
               "releases are excluded. This comparison includes an admission-set change "
               "and does not isolate activation transients.\n")
    (root / "deadline_misses_equal_count_caption.txt").write_text(caption)
    print(f"Exported PDF, SVG and PNG: {stem}")


if __name__ == "__main__":
    main()
