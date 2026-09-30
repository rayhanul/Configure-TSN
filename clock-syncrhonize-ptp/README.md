# gPTP time sync on the testbed (set up 2026-09-14)

Profile: IEEE 802.1AS (gPTP), L2, peer-to-peer delay, domain 0. All TTTech switch ports run
`profile gptp` (sw00 p2/p3 were `default_l3` and were changed on 2026-09-14; backup
`/etc/deptp/ptp_config.xml.bak-2026-09-14` on sw00; `/etc/init.d/deptp restart` applied it).

| host | role | ptp4l | phc2sys | notes |
|---|---|---|---|---|
| ES1 CNC | grandmaster | `ptp4l -i enp1s0 -f gptp_gm.cfg -m` (priority1 128 beats the switches' 247) | `phc2sys -s CLOCK_REALTIME -c enp1s0 -w -f gptp_gm.cfg -m` (PHC = system time + 37 s TAI) | system clock stays NTP-disciplined (timesyncd) = the time base of the whole network |
| ES2 | end station | `ptp4l -i enp1s0 -f /etc/linuxptp/gptp_slave.cfg -m` | `phc2sys -s enp1s0 -c CLOCK_REALTIME -O -37 -m` | linuxptp 4.4 is AppArmor-confined: config must live in /etc/linuxptp, phc2sys cannot query ptp4l (-w), so the UTC offset is given as -O -37. chrony stopped. |
| ES3 RS | end station | `ptp4l -i enp1s0 -f /home/pwh24004/ptp/gptp_slave.cfg -m` | `phc2sys -s enp1s0 -c CLOCK_REALTIME -w -f <cfg> -m` | linuxptp 4.0, no AppArmor issue. chrony stopped. |

gPTP needs `gmCapable 1` on every node; a node is kept from becoming grandmaster with
`priority1 255` (not `slaveOnly`, which linuxptp rejects with 802.1AS). `phc2sys`/`pmc` must
carry `transportSpecific 0x1` (via `-f cfg`) to talk to a gPTP ptp4l.

Start order: GM first (`ptp_start.sh gm` on the CNC), then slaves. If a slave was running
before the GM's PHC was set, restart its ptp4l and phc2sys so they step instead of slewing
tens of seconds at the maximum rate.

Observed over a 60 s window after convergence (2026-09-14, logs/stats_*.txt): ptp4l PHC-to-master
rms 155 ns (ES2) / 158 ns (RS), worst 1.4 us; phc2sys system-to-PHC mean ~0, worst 1.3 us;
CNC PHC-to-system a few hundred ns; all four switch TAI clocks jumped from 2018 to now (TAI = UTC + 37 s).

Autostart (installed 2026-09-14 with `install_autostart.sh gm|slave <cfg>`): systemd units
`tsn-ptp4l.service` and `tsn-phc2sys.service` on all three hosts, enabled at boot, `Restart=always`;
config copied to `/etc/linuxptp/gptp_<role>.cfg`. Slaves use `phc2sys -O -37` (no dependency on
ptp4l's management socket); chrony (ES2) / systemd-timesyncd (RS) are disabled so they do not
fight phc2sys. The CNC keeps systemd-timesyncd: its system clock is the NTP-disciplined source.
Check: `systemctl status tsn-ptp4l tsn-phc2sys`, `journalctl -u tsn-ptp4l -f`.
Manual fallback: `ptp_start.sh`. Old hand-started logs: `logs/` (CNC), `/home/pwh24004/ptp/` (ES2, RS).
