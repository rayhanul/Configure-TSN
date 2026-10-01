# Time sync: gPTP (IEEE 802.1AS)

linuxptp with hardware timestamping on the end stations' Intel I210/I225 NICs. `ptp4l` syncs the
NIC clock (PHC) over the network, `phc2sys` makes the Linux system clock follow the PHC. NTP is off.

| file | |
|---|---|
| `gptp.sh` | detect NIC, check hardware timestamping, install, status, verify |
| `gptp_gm.cfg` / `gptp_slave.cfg` | ptp4l configs (identical except priority) |
| `measure_switch_offsets.sh` | switch offsets from the grandmaster, PASS/FAIL |

Testbed: S1 = grandmaster, S2/S3 = slaves, all on `enp1s0` (I210, `/dev/ptp0`). Installed as systemd
units `tsn-ptp4l` and `tsn-phc2sys` (start at boot). Switches sw01–sw08 run `profile gptp`.

## Install

```bash
sudo apt install -y linuxptp ethtool
./gptp.sh detect                          # find the igb/igc interface and its /dev/ptpX
./gptp.sh check enp1s0                    # must end with "supports hardware timestamping"
sudo ./gptp.sh install gm    enp1s0       # S1 only, first
sudo ./gptp.sh install slave enp1s0       # S2, S3
```
`install` also sets the kernel TAI offset (`CLOCK_TAI` = UTC + 37 s, needed by `gen_traffic.py` and
taprio/etf) at every boot; on its own: `sudo ./gptp.sh tai`.
`sudo ./gptp.sh launchtime on|off` sets up the NIC launch-time queues `gen_traffic.py` needs
(socket priority 7 → TX queue 0, 5 → queue 1, etf with hardware offload), now and at boot. It
resets the NIC and its PHC, so it stops and restarts PTP around the change; on the grandmaster
that pauses sync for the whole network (~20 s). Don't remove the queues with plain `tc`.
`sudo ./gptp.sh run gm|slave` runs the same in the foreground for testing.
Installing on the grandmaster restarts sync for the whole network (~20 s); not during experiments.

## Verify (< 1 µs)

```bash
sudo ./gptp.sh verify                     # end station: PASS/FAIL over the last 120 s
sudo ./gptp.sh status                     # services, port state, last offsets
./measure_switch_offsets.sh 20            # all switches, 20 samples each: PASS/FAIL
```
Quick single reading of every switch:
```bash
for ip in 192.168.0.{1..8}; do ssh root@$ip deptp_tool --get-current-dataset | awk -v ip=$ip '/offset-from-master-ns/{o=$2} /steps-removed/{h=$2} END{a=(o<0)?-o:o; printf "%-12s hops %s  offset %5d ns  -> %s\n", ip, h, o, (o!="" && h>0 && a<1000)?"PASS":"FAIL"}'; sleep 1; done
```
Measured 2026-10-01: switches and S2's PHC within ±115 ns of the grandmaster (rms 20–54 ns);
system clocks within ~750 ns of their PHC.

## Notes

- The grandmaster's PHC runs free (set once to system time + 37 s = TAI); letting NTP steer it
  made offsets grow per hop (150–460 ns before).
- `logSyncInterval -3` must match the switches' gPTP ports.
- S3 (linuxptp 4.4, AppArmor): phc2sys uses `-O -37` instead of `-w`; `pmc` gets no answer.
- Switch IPs vs. names: sw03 = `192.168.0.5`, sw05 = `192.168.0.3`. `steps-removed 0` on a switch
  means it thinks it is the grandmaster.
