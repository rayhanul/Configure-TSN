# Traffic generation for a GCL schedule

`gen_traffic.py` sends and receives real UDP traffic for the flows in a `schedule.json`, on the
VLANs `Network-Configure-Manager/configureManager.py` set up.

## Prerequisites

1. Flows admitted with `configureManager.py ... --endpoints <dir>/endpoints.json --apply`
   (writes each node's VLAN IP, peer IP and sender/receiver role).
2. GCLs deployed with `deploy-GCL/configure_gcl.py --apply` (writes `<dir>/basetime.json`).
3. PTP running with the kernel TAI offset set (`time-sync-gptp/`, `sudo ./gptp.sh status`).

## Run

```bash
D=../GCL_Schedules/<package>/<run>
python3 gen_traffic.py --schedule $D/schedule.json --endpoints $D/endpoints.json --node S1   # dry-run: list flows
sudo python3 gen_traffic.py --schedule $D/schedule.json --endpoints $D/endpoints.json --node S1 --run --duration 30
```
Start receivers before senders. `sudo` is needed for pcp 7.

Whole experiment on S1/S2/S3 at once (preflight, ping check, common start, collect, report):
```bash
S3_PW='<S3 sudo password>' python3 run_experiment.py --pkg $D --duration 30 --ping
```
TX and RX times come only from the NICs: the sender's NIC launches each frame at its scheduled
time (needs `sudo ./gptp.sh launchtime on` on every node, see `time-sync-gptp/`) and the
receiver's NIC timestamps it. Sender and receiver run as pinned real-time processes with CPU
power-saving states off (`--no-rt` to disable). The report adds drop counters (UDP socket buffers,
etf, switch `Q DROP` per gated port) and each flow's schedule `e2e_ns`.
Writes `$D/results/results-<YYYY-MM-DD>/` (`_2`, `_3`, ... for more runs that day) with `results_<node>.log` and `results.md` (per flow: sent,
received, latency min/avg/max, jitter, deadline misses). `<NODE>_PW` overrides the topology file's
sudo password for that node. It stops if a node's kernel TAI offset is not 37 s.

## What it does

- **Sender** (one process, all flows): frame time = `basetime + n*period + psi_ns` of the flow's
  first hop (CLOCK_TAI, same grid as the switches' gates), port `50000 + rank of flow id`. `size`
  is the whole Ethernet frame, so the UDP payload is `size - 50` bytes (Ethernet 14 + VLAN 4 + FCS 4
  + IP 20 + UDP 8). Each frame is handed to the kernel 1 ms early with `SO_TXTIME` and the NIC
  sends it at exactly that time (pcp 7 → socket priority 7, pcp 6 → priority 5, mapped to PCP 6 by
  the VLAN's `egress-qos-map 5:6`); a frame that can no longer make its time is skipped and counted.
- **Receiver** (one epoll process, all flows): latency = NIC hardware RX timestamp − NIC launch
  time, so no software time is included (a frame without a NIC timestamp is counted, not measured); min/avg/max, jitter (stddev and
  RFC 3550), deadline misses. Loss = sender's count − receiver's count.

## Limits

No per-packet hardware TX timestamps: the I210 has one TX timestamp slot, shared with ptp4l, so the
TX time is the NIC launch time.
Before/after comparison: `results-2026-10-01/` (Python-timed, why it misses TSN's guarantees) and
`results-2026-10-01_3/` (launch time + hardware timestamps), under
`GCL_Schedules/prob3-rl-c9-on/1-rl-c9on-matrix/results/`.

Starting it remotely: use `cd dir; nohup cmd > out.log 2>&1 < /dev/null &` (`;`, not `&&`, or the
SSH session stays attached until `cmd` exits).
