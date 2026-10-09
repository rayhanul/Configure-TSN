#!/usr/bin/env python3
"""
plot_update.py -- figures for measure_update.py and loss_during_update.py.

    python3 plot_update.py timing results/<date>/immediate-nagle results/<date>/immediate-nodelay
    python3 plot_update.py loss <pkg>/results/update-loss-<date>
    python3 plot_update.py switches results/<date>/immediate-nagle results/<date>/immediate-nodelay

timing: network update time per topology and strategy (median, p5-p95), and where one port's
update time goes (send / on-switch upload, wrcl, configure / return). Writes PNGs into the
first directory's parent.  loss: lost frames, deadline misses and max latency per bin over the
run, with the before / during / after phases of every update shaded. Writes loss_timeline.png.
switches: per switch, mean transmission time (CNC sends the command -> the switch starts running
it) plus update time with the list already on the switch (wrcl issued -> new GCL live). Writes
per_switch_activation.png next to the runs.
"""

import csv
import json
import os
import statistics
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

SERIES = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300", "#4a3aa7", "#e34948"]
INK, INK2, GRID = "#0b0b0b", "#52514e", "#e4e3df"
PHASE = {"before": "#ffffff", "during": "#f6dccd", "after": "#e7f0fb"}
plt.rcParams.update({"font.size": 9, "axes.edgecolor": INK2, "axes.labelcolor": INK, "xtick.color": INK2,
                     "ytick.color": INK2, "axes.spines.top": False, "axes.spines.right": False,
                     "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.6, "axes.axisbelow": True,
                     "legend.frameon": False, "figure.dpi": 150})
STRATEGIES = ["sequential", "parallel", "batched"]


def read_csv(path):
    with open(path) as f:
        return list(csv.DictReader(f))


def fnum(v):
    return float(v) if v not in ("", None) else float("nan")


def label_of(d):
    meta = json.load(open(os.path.join(d, "meta.json")))
    a = meta["args"]
    return (f"{'TCP_NODELAY on' if a['nodelay'] else 'TCP_NODELAY off (as configure_gcl.py)'}"
            + (f", {a['entries']}-entry list" if a.get("entries") else ""))


def plot_timing(dirs):
    out_dir = os.path.dirname(os.path.abspath(dirs[0]))
    data = [(label_of(d), read_csv(os.path.join(d, "runs.csv")), read_csv(os.path.join(d, "ports.csv")))
            for d in dirs]

    # 1) network update time per topology x strategy, one panel per setting, shared y
    fig, axes = plt.subplots(1, len(data), figsize=(6.4 * len(data), 4.0), sharey=True, squeeze=False)
    for ax, (label, runs, _) in zip(axes[0], data):
        topos = list(dict.fromkeys(r["scenario"] for r in runs))
        sizes = {r["scenario"]: f"{r['switches']} sw\n{r['ports']} ports" for r in runs}
        strats = [s for s in STRATEGIES if any(r["strategy"] == s for r in runs)]
        w = 0.8 / len(strats)
        for k, st in enumerate(strats):
            med, lo, hi = [], [], []
            for t in topos:
                v = sorted(fnum(r["update_ms"]) for r in runs if r["scenario"] == t and r["strategy"] == st)
                m = statistics.median(v)
                med.append(m)
                lo.append(m - v[int(.05 * (len(v) - 1))])
                hi.append(v[int(round(.95 * (len(v) - 1)))] - m)
            x = np.arange(len(topos)) + (k - (len(strats) - 1) / 2) * w
            ax.bar(x, med, w * 0.92, color=SERIES[k], label=st, yerr=[lo, hi],
                   error_kw=dict(ecolor=INK2, elinewidth=0.8, capsize=2))
            for xi, m, h in zip(x, med, hi):
                ax.text(xi, m + h + 25, f"{m:.0f}", ha="center", va="bottom", fontsize=6, color=INK2)
        ax.set_xticks(range(len(topos)), [f"{t}\n{sizes[t]}" for t in topos], fontsize=7.5)
        ax.set_title(label, fontsize=9, color=INK)
        ax.grid(axis="x", visible=False)
    axes[0][0].set_ylabel("network update time (ms)\nfirst command sent → last port live")
    axes[0][0].legend(title="strategy", fontsize=8, title_fontsize=8, loc="upper left")
    fig.suptitle("GCL update time on the real switches, by topology (median, bars p5–p95)", fontsize=10)
    fig.tight_layout()
    p1 = os.path.join(out_dir, "update_time_by_topology.png")
    fig.savefig(p1)
    plt.close(fig)

    # 2) per port: where the time goes (mean of each step), stacked horizontally
    parts = [("send_ms", "send (CNC → switch starts)", SERIES[0]),
             ("upload_ms", "upload list (on switch)", SERIES[3]),
             ("wrcl_ms", "tsntool st wrcl", SERIES[1]),
             ("configure_ms", "tsntool st configure", SERIES[2]),
             ("return_ms", "result back to CNC", SERIES[6])]
    rows_lbl, vals = [], []
    for label, _, ports in data:
        for st in STRATEGIES:
            rs = [r for r in ports if r["strategy"] == st and r.get("live") == "1"]
            if not rs:
                continue
            first = [r for r in rs if r["pos_in_exec"] == "0"]
            last = [r for r in rs if int(r["pos_in_exec"]) == int(r["exec_ports"]) - 1]
            src = {"send_ms": first, "return_ms": last}
            vals.append([statistics.fmean(fnum(r[c]) for r in src.get(c, rs)) for c, _, _ in parts])
            rows_lbl.append(f"{st}\n{label.split(' (')[0]}")
    fig, ax = plt.subplots(figsize=(8, 0.42 * len(rows_lbl) + 1.4))
    y = np.arange(len(rows_lbl))[::-1]
    left = np.zeros(len(rows_lbl))
    for j, (c, name, col) in enumerate(parts):
        v = np.array([r[j] for r in vals])
        ax.barh(y, v, left=left, color=col, height=0.62, label=name, edgecolor="white", linewidth=1.5)
        for yi, l, vi in zip(y, left, v):
            if vi >= 3:
                ax.text(l + vi / 2, yi, f"{vi:.1f}", ha="center", va="center", fontsize=7, color="white")
        left += v
    for yi, l in zip(y, left):
        ax.text(l + 0.6, yi, f"{l:.1f} ms", va="center", fontsize=7.5, color=INK)
    ax.set_yticks(y, rows_lbl, fontsize=7.5)
    ax.set_xlabel("ms per port (mean over all updates); send and return count once per SSH command,\n"
                  "so in batched they are shared by the switch's ports")
    ax.grid(axis="y", visible=False)
    ax.legend(ncol=3, fontsize=7.5, loc="upper center", bbox_to_anchor=(0.5, -0.32))
    ax.set_title("One port's GCL update: command send vs exact time on the switch", fontsize=10)
    fig.tight_layout()
    p2 = os.path.join(out_dir, "port_update_breakdown.png")
    fig.savefig(p2)
    plt.close(fig)
    print(f"wrote {p1}\nwrote {p2}")


def plot_loss(d):
    meta = json.load(open(os.path.join(d, "updates.json")))
    b = read_csv(os.path.join(d, "bins.csv"))
    t = np.array([fnum(r["t_ms"]) for r in b]) / 1e3
    sent = np.array([fnum(r["sent"]) for r in b])
    lost = np.array([fnum(r["lost"]) for r in b])
    miss = np.array([fnum(r["deadline_miss"]) for r in b])
    lat = np.array([fnum(r["max_latency_us"]) for r in b])
    start = meta["start_ns"]
    ups = [((u["t_first_send"] - start) / 1e9, (u["t_last_cct"] - start) / 1e9, u) for u in meta["updates"]]

    def shade(ax):
        for i, (a, z, u) in enumerate(ups):
            ax.axvspan(a, z, color=PHASE["during"], lw=0, zorder=0)
            ax.axvline(a, color=SERIES[1], lw=0.8, zorder=1)
            ax.axvline(z, color=SERIES[0], lw=0.8, zorder=1)

    fig, axes = plt.subplots(3, 2, figsize=(11, 6.4), sharex="col",
                             gridspec_kw=dict(width_ratios=[2.2, 1], hspace=0.18, wspace=0.12))
    a0, z0 = ups[0][0], ups[0][1]
    pad = max(0.3, 0.6 * (z0 - a0))
    for col, (lo, hi) in enumerate([(t[0], t[-1] + t[1] - t[0]), (a0 - pad, z0 + pad)]):
        m = (t >= lo) & (t <= hi)
        for row, (y, name, c) in enumerate([(lost, "lost frames / bin", SERIES[7]),
                                            (miss, "deadline misses / bin", SERIES[3]),
                                            (lat, "max latency (µs)", SERIES[0])]):
            ax = axes[row][col]
            shade(ax)
            if row < 2:
                ax.bar(t[m], y[m], width=(t[1] - t[0]), align="edge", color=c, lw=0)
                ax.set_ylim(bottom=0, top=max(1, y[m].max() * 1.1))
            else:
                ax.plot(t[m], y[m], color=c, lw=1.2)
            ax.set_xlim(lo, hi)
            if col == 0:
                ax.set_ylabel(name)
        axes[2][col].set_xlabel("time since traffic start (s)" if col == 0 else "zoom on update 1 (s)")

    phases = meta["phases"]
    txt = "   ".join(f"{p['phase']}: {p['lost']}/{p['sent']} lost ({p['loss_pct']:.3f}%)" for p in phases)
    upd = "; ".join(f"update {i}: {u['update_ms']:.0f} ms" for i, (_, _, u) in enumerate(ups, 1))
    fig.suptitle(f"Packet loss around a GCL update — {meta['scenario']}, {meta['strategy']}, {meta['mode']}, "
                 f"{len(meta['flows'])} flows, {meta['bin_ms']:g} ms bins ({upd})", fontsize=10)
    fig.text(0.5, 0.005, txt + "\nshaded = during the update (first command sent → last port live)",
             ha="center", fontsize=7.5, color=INK2)
    fig.subplots_adjust(left=0.07, right=0.98, top=0.93, bottom=0.12)
    p1 = os.path.join(d, "loss_timeline.png")
    fig.savefig(p1)
    plt.close(fig)

    # phase summary: loss rate per phase, per update
    fig, ax = plt.subplots(figsize=(6, 2.8))
    names = [p["phase"] for p in phases]
    rate = [p["loss_pct"] for p in phases]
    cols = [SERIES[0] if n == "before" else SERIES[1] if n.startswith("during") else SERIES[2] for n in names]
    ax.bar(range(len(names)), rate, color=cols, width=0.6)
    for i, p in enumerate(phases):
        ax.text(i, rate[i], f"{p['lost']}/{p['sent']}\n{p['length_ms'] / 1e3:.2f} s", ha="center",
                va="bottom", fontsize=7, color=INK2)
    ax.set_xticks(range(len(names)), names, fontsize=8)
    ax.set_ylabel("frames lost (%)")
    ax.grid(axis="x", visible=False)
    ax.set_title("Loss rate before / during / after the GCL update", fontsize=10)
    ax.margins(y=0.3)
    fig.tight_layout()
    p2 = os.path.join(d, "loss_by_phase.png")
    fig.savefig(p2)
    plt.close(fig)
    print(f"wrote {p1}\nwrote {p2}")


def plot_per_switch(dirs):
    """paper figure, no title: per switch, CNC transmission + on-switch update, per TCP setting."""
    out_dir = os.path.dirname(os.path.abspath(dirs[0]))
    data = []
    for d in dirs:
        rows = [r for r in read_csv(os.path.join(d, "ports.csv")) if r.get("live") == "1"]
        sws = sorted({r["switch"] for r in rows})
        tx = {sw: statistics.fmean((int(r["sw_a"]) - int(r["t_send"])) / 1e6 for r in rows
                                   if r["switch"] == sw and r["pos_in_exec"] == "0") for sw in sws}
        up = {sw: statistics.fmean((int(r["cct"]) - int(r["sw_b"])) / 1e6 for r in rows
                                   if r["switch"] == sw) for sw in sws}
        nodelay = json.load(open(os.path.join(d, "meta.json")))["args"]["nodelay"]
        data.append((nodelay, sws, tx, up))
    data.sort(key=lambda x: x[0])  # default TCP first
    sws = data[0][1]
    for _, _, tx, up in data:  # a final "Mean" group: average over the switches
        tx["mean"] = statistics.fmean(tx[s] for s in sws)
        up["mean"] = statistics.fmean(up[s] for s in sws)
    cats = sws + ["mean"]
    pos = np.append(np.arange(len(sws)), len(sws) + 0.4)
    style = {"font.family": "serif", "font.serif": ["Times New Roman", "Times", "STIXGeneral", "DejaVu Serif"],
             "mathtext.fontset": "stix", "font.size": 8, "axes.labelsize": 8.5, "xtick.labelsize": 8,
             "ytick.labelsize": 8, "legend.fontsize": 7.5, "axes.linewidth": 0.6, "grid.linewidth": 0.4,
             "xtick.major.width": 0.6, "ytick.major.width": 0.6}
    # muted slate purple / pale cream / dusty rose: OKLab distance >= 20 for every pair, also under
    # simulated protan, deutan and tritan vision; labels white on purple, dark on the lighter fills
    tx_col = {False: "#5d587a", True: "#e2ddb8"}  # transmission: default TCP / TCP_NODELAY
    up_col = "#c08d80"                             # GCL update on the switch
    with plt.rc_context(style):
        fig, ax = plt.subplots(figsize=(7.0, 2.4))
        w = 0.4
        for k, (nodelay, _, tx, up) in enumerate(data):
            x = pos + (k - (len(data) - 1) / 2) * (w + 0.02)
            t = np.array([tx[s] for s in cats])
            u = np.array([up[s] for s in cats])
            ax.bar(x, t, w, color=tx_col[nodelay], edgecolor="white", lw=0.6,
                   label="Transmission, TCP_NODELAY " + ("on" if nodelay else "off (default)"))
            ax.bar(x, u, w, bottom=t, color=up_col, edgecolor="white", lw=0.6,
                   label=None if k else "GCL update on switch")
            for xi, ti, ui in zip(x, t, u):
                ax.text(xi, ti + ui + 0.5, f"{ti + ui:.1f}", ha="center", va="bottom", fontsize=6.5, color=INK)
                ax.text(xi, ti / 2, f"{ti:.1f}", ha="center", va="center", fontsize=6,
                        color="white" if not nodelay else INK)
                ax.text(xi, ti + ui / 2, f"{ui:.1f}", ha="center", va="center", fontsize=6, color=INK)
        ax.axvline(len(sws) - 0.3, color=INK2, lw=0.6, ls=(0, (3, 2)))
        ax.set_xticks(pos, [s.replace("sw0", "SW") for s in sws] + ["Mean"])
        ax.get_xticklabels()[-1].set_fontweight("bold")
        ax.set_xlabel("Switch")
        ax.set_ylabel("Time (ms)")
        ax.set_ylim(0, max(tx[s] + up[s] for _, _, tx, up in data for s in cats) * 1.18)
        ax.set_xlim(pos[0] - 0.6, pos[-1] + 0.6)
        ax.grid(axis="x", visible=False)
        ax.tick_params(length=2.5)
        h, l = ax.get_legend_handles_labels()
        order = [0, 2, 1] if len(h) == 3 else range(len(h))
        ax.legend([h[i] for i in order], [l[i] for i in order], ncol=3, loc="upper center",
                  bbox_to_anchor=(0.5, 1.14), frameon=False, columnspacing=1.5, handlelength=1.6)
        fig.tight_layout(pad=0.3)
        paths = [os.path.join(out_dir, f"per_switch_activation.{ext}") for ext in ("pdf", "png")]
        fig.savefig(paths[0])
        fig.savefig(paths[1], dpi=300)
        plt.close(fig)
    print("wrote " + ", ".join(paths))


if __name__ == "__main__":
    if len(sys.argv) < 3 or sys.argv[1] not in ("timing", "loss", "switches"):
        sys.exit(__doc__)
    if sys.argv[1] == "timing":
        plot_timing(sys.argv[2:])
    elif sys.argv[1] == "switches":
        plot_per_switch(sys.argv[2:])
    else:
        for d in sys.argv[2:]:
            plot_loss(d)
