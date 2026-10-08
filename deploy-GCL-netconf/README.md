# Deploying GCL (802.1Qbv) schedules over NETCONF

This folder is a **self-contained NETCONF alternative** to `../deploy-GCL/`. It
pushes the *same* `<switch>-<port>.cfg` gate-control-list files to the same
switches, but over **NETCONF/YANG** (`ieee802-dot1q-sched` via netopeer2 +
sysrepo) instead of **SSH + `tsntool`**. Nothing here changes the tsntool path;
it exists so you can run both and decide which to keep.

The switches already run the stack this needs: `netopeer2-server 1.1.76` +
`sysrepo-plugind` are up on port **830** (confirmed on sw01–sw08 except sw03,
whose daemon isn't started), and `ieee802-dot1q-sched` rev **2018-09-11** is
installed and *implemented* (`sysrepoctl -l`), alongside `-psfp`, `-preempt`,
`-cb-frer`, `ietf-interfaces`, `ietf-ptp`.

## Files

| file | role | counterpart in `deploy-GCL/` |
|---|---|---|
| `configure_gcl_netconf.py` | push + activate a whole GCL package | `configure_gcl.py` |
| `bench_netconf.py` | time ONE port's update (for the latency comparison) | `../gcl-schedule-update/run-tsn-config-cnc.py` |
| `netconf_sched.py` | YANG layer: build the edit-config, read state | — |
| `gcl_common.py` | pure helpers copied from `configure_gcl.py` (tick rounding, port mapping, cycle fraction) | the same functions in `configure_gcl.py` |
| `requirements.txt` | `ncclient` | — |

## Setup

```bash
pip install -r requirements.txt     # ncclient is NOT currently installed on the CNC
```

Auth: NETCONF rides SSH, so it uses the same credentials as everything else.
The netopeer2 endpoint advertises `publickey`, `password`, and
`keyboard-interactive`. Pass a password with `--password sw01=SECRET` (repeatable),
put it in the topology JSON's `password` field, or rely on an authorized key.
`--password` with an empty value / key auth is tried when no password is given.

## Usage (mirrors `configure_gcl.py`)

```bash
# dry-run: print the plan AND the exact edit-config XML for the first port
python3 configure_gcl_netconf.py \
  --gcl-dir ../GCL_Schedules/heuristic-c9-off/1-matrix-c9off/gcl \
  --topology ../network-topology/network-topology-rtas-2027.json

# actually edit-config + commit (candidate datastore, one commit per switch)
python3 configure_gcl_netconf.py --gcl-dir <dir> --topology <topo.json> --apply

# subset / skip, same flags as the tsntool tool
python3 configure_gcl_netconf.py --gcl-dir <dir> --topology <topo.json> --apply --only sw01 sw02
python3 configure_gcl_netconf.py --gcl-dir <dir> --topology <topo.json> --apply --exclude sw01
```

### What is identical to the tsntool path
Reused byte-for-byte from `configure_gcl.py` (in `gcl_common.py`): the
`sw01-p3.cfg → switch sw01, iface sw0p3` mapping, the cycle time read from
`schedule.json`'s `cycle_ns` as a numerator/denominator, the rounding of every
GCL boundary to the switch's tick granularity, the **one common base time**
sampled from a reference switch + lead, and writing `basetime.json` from the
grid the switches actually report back.

### What differs (the point of the comparison)
- No file upload, no `tsntool`, no `cat > /home/root/...`: the gate list is the
  payload of an `<edit-config>` to the **candidate** datastore, activated with
  `<commit>`.
- **Per switch, all ports go in one candidate + one `commit`** → atomic: if any
  port's entry is rejected, none of that switch's ports change.
- Errors arrive as structured `<rpc-error>` (path + severity), not scraped
  stderr / dmesg.

## Benchmark: does NETCONF beat the 16–64 ms?

`run-tsn-config-cnc.py` reports 16–64 ms measured on an **already-open** SSH
session (connection setup excluded), around `tsntool st wrcl` + `st configure`.
`bench_netconf.py` uses the **same methodology** — session opened first and not
counted — around `edit-config` + `commit`, and splits the two:

```bash
python3 bench_netconf.py --host 192.168.0.1 --user root \
  --cfg ../GCL_Schedules/heuristic-c9-off/1-matrix-c9off/gcl/sw01-p3.cfg \
  --iface sw0p3 --cycle-ns 800000 --repeat 20
```

**Expectation (be skeptical):** NETCONF almost certainly will **not** be faster
per update. The dominant cost — the driver programming the gate list — is
identical, and NETCONF adds XML parse + sysrepo candidate→commit→plugin IPC on
top. The split (`edit-config` vs `commit`) tells you whether the commit is a
fixed floor. The one place NETCONF can win is **aggregate** whole-network time:
one commit per switch instead of N serial `tsntool` invocations per switch.

## Before you trust `--apply`: confirm the model shape

I could **not** complete NETCONF auth from here, so the exact *augment point*
and base-time leaf names in `netconf_sched.py` follow the published IEEE
802.1Q-2018 YANG but are **unverified against this switch's build**. Confirm
once, then adjust the handful of isolated constants at the top of
`netconf_sched.py` if the switch differs:

```bash
python3 configure_gcl_netconf.py \
  --gcl-dir <dir> --topology <topo.json> --probe-schema --only sw01
```

This connects, prints sw01's `gate-parameters` state tree and its
sched/bridge/interface capabilities, and **changes nothing**. Check:
1. does `gate-parameters` hang off `ietf-interfaces/interface` (as assumed), or
   off the `ieee802-dot1q-bridge` component? → fix `GATE_PARAMS_TEMPLATE` path.
2. are the base-time children `seconds`/`nanoseconds` (as assumed) or
   `seconds`/`fractional-seconds`? → fix `BASE_TIME_*_LEAF`.
3. is `tick-granularity` exposed in state (units of 1/10 ns)? If not, pass
   `--tick-ns 320`.

## Caveats NETCONF does NOT fix (same as the tsntool path)
- **Tick granularity** (`schedule.json` uses 8 ns, hardware enforces 320 ns):
  still a hardware constraint. `--no-round-to-tick` lets you reproduce the
  rejection; otherwise entries are rounded exactly as the tsntool tool rounds
  them. NETCONF just reports the rejection as a clean `<rpc-error>`.
- **`OperBaseTime` 0 / phase behavior** is driver-side; the readback reads
  `config-change-time`, same as the tsntool tool reads `ConfigChangeTime`.
- **PTP sync** is still a prerequisite — see `../time-sync-gptp/`.
- **sw03** has the netopeer2 init script but the daemon is down; start it there
  before `--apply` includes sw03.
