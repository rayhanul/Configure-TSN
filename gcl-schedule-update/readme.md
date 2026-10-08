# GCL schedule update timing

How long it takes to update the 802.1Qbv gate control lists (GCLs) on the real switches, and what
an update does to traffic that is already running.

| file | what it does |
|---|---|
| `measure_update.py` | times a GCL update of every port of a topology, split into command send vs exact on-switch time |
| `topologies.json` | the topologies (subgraphs of the 8-switch mesh) an update covers |
| `loss_during_update.py` | runs a package's traffic, updates the GCLs mid-run, counts lost frames before / during / after |
| `plot_update.py` | figures for both (needs a working matplotlib) |
| `run-tsn-config-cnc.py`, `run_config_wrcl.sh`, `result_manager.py` | the earlier single-port `wrcl` timing (June) |

## Update timing across topologies

```bash
python3 measure_update.py                       # dry-run: ports updated per topology
python3 measure_update.py --apply               # every topology x {sequential, parallel, batched}, 20 reps
python3 measure_update.py --apply --nodelay     # same with TCP_NODELAY on the SSH sockets
python3 measure_update.py --apply --scenario mesh-8 --mode coordinated
python3 measure_update.py --apply --scenario mesh-8 --strategy batched --entries 255   # GCL length
python3 plot_update.py timing results/<date>/<run> [results/<date>/<other run>]
```

Each port is updated like `deploy-GCL/configure_gcl.py` does it (upload the list, `tsntool st
wrcl`, `tsntool st configure`), with timestamps on two clocks that PTP keeps within ~100 ns of each
other: the CNC's `CLOCK_TAI` and the switch's own `CurrentTime` (read with the shell builtin `read`,
no fork). So for every port:

- **send**: CNC issues the command -> the switch starts running it (SSH channel open, exec request,
  shell start on the switch);
- **switch**: exact time on the switch: upload (`cat` the list to a file), `wrcl`, `configure`;
- **activation**: `configure` issued -> hardware runs the new list (`ConfigChangeTime`);
- **return**: result back at the CNC.

Network update time = first command sent -> last port's `ConfigChangeTime`. By default every port
gets its own current list back (read once at start; copies in `<out>/snapshot/`), so gates behave
the same before and after; `--entries N` writes all-open lists of N entries and restores the
originals at the end.

- Strategies: `sequential` (one port at a time, as `configure_gcl.py`), `parallel` (one thread per
  switch, one SSH command per port), `batched` (one thread and one SSH command per switch).
- Modes: `immediate` (basetime = the switch's own clock, so each port switches at its next cycle
  boundary; the driver logs `AdminBaseTime in the past!` and bumps `ConfigChangeError`, and applies
  the list) and `coordinated` (one basetime `--lead-seconds` ahead, meant to switch every port at
  once; see Notes: these switches ignore it).

Output: `results/results-<date>/` -> `ports.csv` (one row per port update, raw ns timestamps and
ms), `runs.csv` (one row per network update), `summary.md`, `meta.json`.

## Packet loss before / during / after an update

```bash
D=../GCL_Schedules/dataset-testbed-2_2026-10-08/2-rl-c9on-matrix-S2rx   # the package that is live
S3_PW='<S3 sudo password>' python3 loss_during_update.py --pkg $D --scenario mesh-8 \
    --strategy sequential --update-at 10 --duration 30
# to another package's lists and back:
python3 loss_during_update.py --pkg $D --target-gcl <other pkg>/gcl --update-at 10 --restore-at 20
```

Runs `Spawning-Flows/gen_traffic.py --packet-log` on every end station it can sudo on (without
`S3_PW`, S3 and its flows are left out), and updates the GCLs at `--update-at`. Each frame is
identified by (flow, launch time), so a frame is lost if it was sent and not received. Output in
`$D/results/update-loss-<date>/`: `summary.md` (per phase: sent, lost, deadline misses, latency),
`bins.csv`, `updates.json`, `ports.csv`, raw logs, `loss_timeline.png`, `loss_by_phase.png`.

## Notes

- **The switches ignore the basetime.** `tsntool st configure` with a basetime 3, 30 or 100 s ahead
  still switches the port at the next cycle boundary, ~7 ms after the call (`AdminBaseTime` reads
  back 0, also when written through sysfs). So a port runs its new list as soon as it is configured,
  the network runs old and new lists side by side for as long as the update takes, and
  `--mode coordinated` behaves like `immediate`. (This also holds for `deploy-GCL/configure_gcl.py`'s
  shared basetime.)
- `/tmp` on the switches is a 502 MB tmpfs shared with their logs. On sw04 it was full on 2026-10-08
  (`/var/volatile/log`), so a shell here-document could not create its temp file, an empty list was
  written, `wrcl` returned 0 and `configure` failed with 22. The update script puts the
  here-document's temp file in `/home/root`.
- paramiko leaves Nagle on. With the switches' delayed ACKs, opening an SSH channel then takes
  ~40 ms instead of ~1.3 ms; `--nodelay` sets `TCP_NODELAY`.
- The switches' sshd drops rapid reconnects, so both tools open one session per switch and reuse it.
- `/usr/bin/python3` has no paramiko and anaconda's matplotlib is built against NumPy 1.x; run the
  measurements with anaconda's `python3` and the plots from a venv with matplotlib
  (`python3 -m venv v && v/bin/pip install matplotlib numpy`).

## Earlier single-port wrcl timing (June)



```
python3 run-tsn-config-cnc.py   --ip 192.168.0.4   --user root   --cmd "tsntool st wrcl sw0p2 sw0p2.cfg"

```



To make the shell script executable:


```
chmod +x run_wrcl_100_times.sh

```





Now this the given amount of times using command :


```

./run_config_wrcl.sh 192.168.0.4 sw0p2 sw0p2.cfg

```


To plot result:

```
python result_manager.py wrcl_192.168.0.1_sw0p5_execution_times.csv wrcl_192.168.0.2_sw0p4_execution_times.csv wrcl_192.168.0.4_sw0p4_execution_times.csv
```






