# gPTP (IEEE 802.1AS) time sync, sub-microsecond

linuxptp with hardware timestamping on Intel I210 (`igb`) / I225-I226 (`igc`), Ubuntu.
`ptp4l` synchronizes the NIC's PTP hardware clock (PHC, `/dev/ptpN`) over the network (802.1AS:
L2, peer-to-peer delay, transportSpecific 1), `phc2sys` makes the Linux system clock follow the PHC.
NTP/chrony are turned off; they would fight `phc2sys`.

| file | |
|---|---|
| `gptp.sh` | everything below: detect, check, run, install, status, verify |
| `gptp_gm.cfg` | ptp4l config for the grandmaster (`priority1 128`) |
| `gptp_slave.cfg` | ptp4l config for all other end stations (`priority1 255`, never grandmaster) |

The two configs differ only in priority. Sync interval is 8/s (`logSyncInterval -3`), which must
match the switches' gPTP ports.

## 1. Install and find the interface / PHC

```bash
sudo apt install -y linuxptp ethtool
./gptp.sh detect
```
```
IFACE          DRIVER   PHC         LINK  SPEED     PCI
eno1           e1000e   /dev/ptp1   up    1000Mb/s  0000:00:1f.6
enp1s0         igb      /dev/ptp0   up    1000Mb/s  0000:01:00.0
```
Use the `igb`/`igc` row cabled into the TSN network. The PHC comes from
`/sys/class/net/<if>/device/ptp/` (same number as `PTP Hardware Clock:` in `ethtool -T`).
All commands take the interface as last argument; without it they pick the first `igb`/`igc`
interface with a PHC and link up.

## 2. Check hardware timestamping

```bash
./gptp.sh check enp1s0          # prints ethtool -T, then:
```
```
ok    hardware-transmit
ok    hardware-receive
ok    hardware-raw-clock
ok    PTP hardware clock /dev/ptp0
ok    driver igb
ok    EEE off
ok    NTP/chrony off
=> enp1s0 supports hardware timestamping
```
It also warns about an active Energy-Efficient Ethernet link (latency jitter; `run`/`install` turn
it off) and pre-B3 I225 steppings (timestamp errors at 2.5 Gb/s).

## 3. Start: grandmaster first, then slaves

Permanent (systemd units `tsn-ptp4l` + `tsn-phc2sys`, start at boot, restart on failure; config
copied to `/etc/linuxptp/`):
```bash
sudo ./gptp.sh install gm    enp1s0     # exactly one node
sudo ./gptp.sh install slave enp1s0     # every other end station
```
Foreground, for testing (Ctrl-C stops both; logs in `./logs/`):
```bash
sudo ./gptp.sh run gm    enp1s0
sudo ./gptp.sh run slave enp1s0
```
What runs, so you can also type it by hand:

| role | ptp4l | phc2sys |
|---|---|---|
| gm | `ptp4l -i enp1s0 -f gptp_gm.cfg -m` | `phc2sys -s enp1s0 -c CLOCK_REALTIME -w -f gptp_gm.cfg -N 5 -m` |
| slave | `ptp4l -i enp1s0 -f gptp_slave.cfg -m` | `phc2sys -s enp1s0 -c CLOCK_REALTIME -w -f gptp_slave.cfg -N 5 -m` |

- `-w` takes the TAI−UTC offset (37 s) from ptp4l; `-f cfg` is required with it, otherwise
  phc2sys asks with transportSpecific 0 and the gPTP ptp4l never answers.
- Ubuntu ≥ 25 (linuxptp ≥ 4.4) confines linuxptp with AppArmor, which blocks `-w`; there the
  script uses `-O -37` instead (detected from `/etc/apparmor.d`, override with `UTC_MODE=w|fixed`),
  and configs must live in `/etc/linuxptp`.
- `-N 5`: phc2sys reads the PHC 5 times per update and uses the fastest read. Reading the PHC over
  PCIe takes ~3.7 µs on the I210 and jitters; on S2 this cut the system clock's worst offset from
  843 to ~510 ns. Override with `PHC2SYS_OPTS=...`.
- **Grandmaster:** its PHC runs free and the system clock follows it. Before ptp4l starts the PHC is
  set to system time + 37 s (TAI), but only when it is more than 1 s off (e.g. after a power cycle),
  so a restart never steps the network. Do not let NTP steer the grandmaster's PHC: every NTP
  correction would ripple through all nodes. Network time drifts slowly from true UTC; for TAS
  only agreement between nodes matters.
- If a slave was started before the grandmaster's PHC was set, restart it (`systemctl restart
  tsn-ptp4l tsn-phc2sys`) so it steps instead of slewing tens of seconds.

## 4. Monitor and verify < 1 µs

```bash
sudo ./gptp.sh status          # services, last log lines, portState / master_offset / gmIdentity
sudo ./gptp.sh verify          # last 120 s
sudo ./gptp.sh verify 600      # last 10 min
./gptp.sh verify-log logs/ptp4l_slave.log logs/phc2sys_slave.log   # after 'run'
```
```
slave on enp1s0, last 100 s, threshold 1000 ns
tsn-ptp4l    samples=100  rms=... ns  worst=... ns  <1000 ns: 100.0%  unlocked=0  -> PASS
tsn-phc2sys  samples=100  rms=... ns  worst=... ns  <1000 ns: 100.0%  unlocked=0  -> PASS
RESULT: PASS (sub-microsecond)
```
PASS means every sample in the window was locked (`s2`) and below 1 µs (`THRESH_NS=500 ./gptp.sh
verify` for a tighter bound).
- **tsn-ptp4l**: PHC vs. grandmaster. At 8 Sync/s ptp4l logs one `rms <ns> max <ns>` line per
  second; `max` is checked.
- **tsn-phc2sys**: system clock vs. PHC (`phc offset <ns> s2`). `s0` = unlocked, `s1` = stepped,
  `s2` = locked.

Manual equivalents:
```bash
sudo journalctl -u tsn-ptp4l -f
sudo pmc -u -b 0 -f /etc/linuxptp/gptp_slave.cfg 'GET TIME_STATUS_NP'   # master_offset, gmPresent
sudo pmc -u -b 0 -f /etc/linuxptp/gptp_slave.cfg 'GET PORT_DATA_SET'    # portState, peerMeanPathDelay
```
These are each node's own estimate of its offset. A constant error (e.g. asymmetric link delay)
is invisible to them; the only end-to-end proof is a 1 PPS output from two NICs on an
oscilloscope (`testptp -d /dev/ptp0 -L 0,2 -p 1000000000`, SDP0 pin on the I210/I225).

## Troubleshooting

| symptom | cause / fix |
|---|---|
| `check`: FAIL hardware-* | wrong interface, or NIC without PTP; use the `igb`/`igc` one |
| ptp4l never leaves LISTENING / no `new foreign master` | switch port not in gPTP profile, or `transportSpecific`/`ptp_dst_mac` mismatch |
| `SYNC_RECEIPT_TIMEOUT`, port FAULTY | `logSyncInterval` differs from the switch |
| `timed out while polling for tx timestamp` | raise `tx_timestamp_timeout` |
| `peerMeanPathDelay` > 800 or port not asCapable | cable/PHY problem, or raise `neighborPropDelayThresh` |
| offsets positive and growing with hop count | grandmaster steered by NTP (see above), or fixed latency to correct with `ingressLatency`/`egressLatency` |
| phc2sys hangs at start | AppArmor blocks `-w`: `UTC_MODE=fixed sudo ./gptp.sh install ...` |

Remove: `sudo ./gptp.sh uninstall` (NTP stays off: `sudo timedatectl set-ntp true`).

## Deployed on the testbed (2026-10-01)

S1 (`ubuntu@137.99.253.118`) = `install gm`, S2 (`jdg24001@137.99.253.167`) and S3
(`jdg24001@137.99.252.240`) = `install slave`, all on `enp1s0` (I210, `/dev/ptp0`). This replaced the
units from `clock-syncrhonize-ptp/install_autostart.sh` (same unit names; S1's old units backed up in
`~/time-sync-gptp-old/`). S3 runs linuxptp 4.4 under AppArmor, so its phc2sys uses `-O -37` and `pmc`
gets no answer there.

Measured ~3 min after S1 became a free-running grandmaster (ns; ptp4l = PHC vs. GM, phc2sys = system
clock vs. PHC, switches = `measure_switch_offsets.sh 20`):

| node | hops | rms | worst |
|---|---|---|---|
| S1 phc2sys | GM | 193 | 696 |
| S2 ptp4l / phc2sys | 5 | 41 / 111 | 81 / 553 |
| S3 ptp4l (install output) | | 26–42 | 57 |
| sw02 (192.168.0.2) | 1 | 20 | 31 |
| sw01, sw05 (.3), sw04 | 2 | 25–33 | 65 |
| sw03 (.5), sw06, sw07 | 3 | 22–49 | 93 |
| sw08 | 4 | 14 | 38 |

Before (S1's PHC steered by NTP through phc2sys, 2026-09-30): switch offsets 151–463 ns, always
positive and growing with hop count; S2 ptp4l rms 147 / worst 398 ns. The per-hop bias is gone
(all switch means within ±25 ns).
