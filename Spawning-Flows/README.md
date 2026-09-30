# Admitting flows and generating traffic for a GCL schedule

`gen_traffic.py` sends/receives real traffic for the flows in a `schedule.json` (see
`GCL_Schedules/`), using the VLAN/IP addressing `Network-Configure-Manager/configureManager.py`
already set up.

## Pipeline

1. **Filter the schedule's flows to what's physically realizable.** `schedule.json`'s `flows` list
   is already filtered to *admitted* flows (10 of this package's 20 candidates), but some of those
   still name end-stations that aren't physically on the testbed (e.g. S3). Cross-reference against
   what's actually present before configuring anything -- see
   `GCL_Schedules/heuristic-c9-off/1-matrix-c9off/stream-realizable.csv` for an example (filtered
   from `dataset/1/stream.csv`, which is already in `configureManager.py`'s native CSV format).

2. **Admit the realizable flows with `configureManager.py`** (reused as-is, not duplicated):
   ```bash
   cd Network-Configure-Manager
   python3 configureManager.py \
     --topology ../network-topology/network-topology-rtas-2027.json \
     --csv ../GCL_Schedules/heuristic-c9-off/1-matrix-c9off/stream-realizable.csv \
     --endpoints ../GCL_Schedules/heuristic-c9-off/1-matrix-c9off/endpoints.json \
     --mstp --apply
   ```
   Check for spanning-tree blocking on the flow's route first (`mstpctl showport br0` on each
   switch in the path) -- a multi-switch mesh like this one commonly has redundant links that plain
   STP blocks, same as any other VLAN deployed on it. `--endpoints` writes the file `gen_traffic.py`
   reads for local iface/IP/peer-IP per flow.

3. **Generate traffic**:
   ```bash
   # dry-run (default): just print which flows this node would send/receive
   python3 gen_traffic.py --schedule <schedule.json> --endpoints <endpoints.json> --node S1

   # actually send/receive (sudo needed for SO_PRIORITY on pcp > 6)
   sudo python3 gen_traffic.py --schedule <schedule.json> --endpoints <endpoints.json> \
     --node S2 --run --duration 30
   ```
   A flow is in scope for `--node X` only if `configureManager.py` actually admitted it for X (i.e.
   it has an entry in `endpoints.json`'s `streams` for X) -- no hardcoded flow-id list, and flows
   that need an absent node (no endpoints entry was ever created for them) are automatically out of
   scope.

## Design

- **Role per flow** comes straight from `endpoints.json`'s `"role": "sender"/"receiver"` --
  `configureManager.py` already determined this.
- **Sender**: UDP socket, `SO_PRIORITY` set to the flow's `pcp` (needs root for pcp 7; the manual
  requires `CAP_NET_ADMIN` above 6), bound to the flow's VLAN IP, sends every `period` ns at the
  flow's `offset_ns`, payload = 8-byte send timestamp + padding to `size` bytes, to
  `50000 + flow id` on the peer's VLAN IP.
- **Receiver**: binds the same deterministic port, computes one-way latency as
  `recv_time - embedded_send_time` -- valid because sender and receiver are already
  PTP-synchronized to sub-microsecond accuracy (see `clock-syncrhonize-ptp/`) -- and flags misses
  against the flow's `deadline`.

## Timing precision (read before trusting the numbers)

Python's `time.sleep` realistically achieves tens-to-hundreds of microseconds of jitter on Linux,
not the sub-microsecond precision `schedule.json`'s GCL windows are computed for. This matters
concretely here: these flows' periods are 200-400us, and their actual TAS-gated open window per
800us cycle is only a few microseconds. A test run (id 5: pcp 7, 200us period/deadline; id 12: pcp
6, 400us period/deadline) against the live schedule got:

| id | sent | received | deadline | misses |
|---|---|---|---|---|
| 5  | 99983 | 77858 (78%) | 200000ns | 7200 (9.2%) |
| 12 | 49991 | 38930 (78%) | 400000ns | 2 (0.005%) |

Both flows lost ~22% of packets in flight, and the tighter-deadline flow (id 5) missed its deadline
far more often than the looser one (id 12) -- the expected pattern if packets generated without
TAS-aware timing mostly land outside their queue's brief gated window each cycle, queue briefly at
the first hop, and either get dropped (shallow low-latency TSN egress buffers) or arrive late. This
is the generator doing what it's for -- demonstrating admission with real traffic and exposing where
timing precision matters -- not a bug to chase. Getting materially better numbers would need
TAS-aware release timing (aligning sends to the schedule's actual `hops[].psi_ns` windows, which
`schedule.json` already has per-flow) or kernel-bypass sending (`AF_XDP`/DPDK), both out of scope
unless asked for.

## A gotcha worth keeping in mind: backgrounding a command over SSH

`cd dir && nohup cmd > out.log 2>&1 < /dev/null &` does **not** reliably detach -- chaining `cd` into
the same `&&` list that gets backgrounded makes the shell background the *whole compound command* as
one subshell job, and in testing that subshell still held the SSH channel open for the full runtime
of `cmd` (a blocking `.read()` on the channel's stdout waited for the entire duration instead of
returning immediately). Separate `cd` from the backgrounded command with `;`, not `&&`:

```bash
cd dir; nohup cmd > out.log 2>&1 < /dev/null &
echo started
```
This actually returns immediately. Worth knowing before concluding a backgrounded remote process
isn't receiving anything -- it may just not have been running concurrently at all.
