# Deploying GCL (802.1Qbv) schedules to switches

`configure_gcl.py` pushes a directory of per-port GCL `.cfg` files (as produced under
`GCL_Schedules/<package>/<run>/gcl/`, e.g. `sw01-p3.cfg` = switch `sw01`, port `sw0p3`)
to the real switches over SSH, via each switch's own `tsntool`.

## Usage

```bash
# dry-run: just show which switch/port gets which file
python3 configure_gcl.py \
  --gcl-dir ../GCL_Schedules/heuristic-c9-off/1-matrix-c9off/gcl \
  --topology ../network-topology/network-topology-rtas-2027.json

# actually push + activate
python3 configure_gcl.py --gcl-dir <dir> --topology <topo.json> --apply

# skip a switch entirely (e.g. one whose GCL only serves routes to/from a
# node that isn't physically on the testbed)
python3 configure_gcl.py --gcl-dir <dir> --topology <topo.json> --apply --exclude sw01

# only a subset, e.g. to test before a full rollout
python3 configure_gcl.py --gcl-dir <dir> --topology <topo.json> --apply --only sw01 sw02
```

Cycle time is read from `schedule.json` next to `--gcl-dir` (its `cycle_ns` field) unless
`--cycle-ns` is given explicitly.

Every port on every switch is activated with **one shared basetime**, sampled from a
reference switch's own PTP-synchronized clock plus a lead time (`--lead-seconds`, default
30). A schedule only behaves correctly network-wide if every switch starts its gate cycle
at the same absolute instant -- see `time-sync-gptp/` for the sync setup this
depends on.

## Why it doesn't use SFTP

These boards' `sshd` has no `sftp-server` subsystem (plain `ssh`/exec works fine, SFTP
does not -- `EOF during negotiation`). Files are uploaded with `cat > remote_path` over a
normal exec channel instead. Default upload path is `/home/root/gcl_{port}.cfg`, **not**
`/tmp` -- on these boards `/tmp` is a small (502 MB) tmpfs (`/var/volatile`) shared by
everything on the switch, including its own logs; `/home/root` is on the real disk.

## tsntool's comment syntax

Per the DE-IP manual, a `#` is only a comment when it's the *first* non-whitespace
character of the line. The shipped `.cfg` files annotate each entry with a trailing
`# 01111111`-style comment, which `tsntool` rejects outright (`Excess record elements`).
`configure_gcl.py` strips trailing comments before upload -- it only removes the
annotation text, never touches the `sgs`/interval/gsv values.

## Known issue: tick granularity mismatch (unresolved)

`schedule.json`'s `hw.t_tick_ns` is **8**, but the real switches report
`TickGranularity: 3200 1/10 nsec` (**320ns**) via `tsntool st show <iface>`. Most interval
values in this schedule package are not multiples of 320ns (e.g. `9120`, `8`, `2128`,
and a few outright non-integer values like `7592.0`), so the driver rejects them:

```
dmesg: bridge-0: Control List Interval is not a multiple of TickGranularity!
tsntool: ERROR: Cannot set admin control list - driver reported 22 (Invalid argument)
```

This means the schedule as generated **cannot be loaded onto this hardware as-is**. Fixing
it means either regenerating the schedule with the real 320ns tick (best -- the generator
that produced `heuristic-c9-off` isn't in this repo, see `report.md`'s "Seeded from SMT
run" path), or rounding every interval to the nearest 320ns and re-balancing each port's
total back to the exact cycle time -- which changes real values, not just formatting, and
needs sign-off before anyone does it.

`AdminControlList` on these switches already has content matching this exact schedule
(from some earlier attempt, before this repo's history) but `OperControlList` -- what's
actually gating live traffic -- holds a different, older schedule that was never
successfully promoted, for the same tick-granularity reason. **No live switch is currently
running this schedule.**

## Known issue: basetime lead time

`--lead-seconds` (default 30) is consumed by the upload phase across *all* switches before
the shared basetime is sampled, but by the time the last switch's `configure` call runs,
enough of that margin can be gone that its basetime is already in the past
(`AdminBaseTime in the past!` in `dmesg`), silently keeping the old `OperControlList`
active instead. This hasn't yet been hit in isolation from the tick-granularity failure
above, but with `--only`/`--exclude` narrowing the switch count, or on a slower link,
watch for it -- `tsntool st show <iface>` after applying will show `OperControlList`
unchanged from before if this happens. Increase `--lead-seconds` if the switch count grows.
