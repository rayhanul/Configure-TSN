#!/bin/bash
# gPTP (802.1AS) for the testbed. Run as root on each host. Usage: ptp_start.sh gm|slave [cfg_path]
#   gm    : CNC (ES1). PHC follows the NTP-disciplined system clock (+37 s TAI), ptp4l serves it as grandmaster.
#   slave : ES2 / RS. ptp4l disciplines the PHC from the network; phc2sys disciplines the system clock from the PHC.
# Logs go next to the config on the slaves (/home/pwh24004/ptp) and to ./logs on the CNC.
ROLE=$1; CFG=${2:-$(dirname "$0")/gptp_${1}.cfg}; LOG=${LOG:-$(dirname "$0")/logs}; mkdir -p "$LOG"
pkill -x ptp4l; pkill -x phc2sys; sleep 1
case $ROLE in
  gm)
    phc_ctl enp1s0 set >/dev/null 2>&1                      # PHC starts near system time (phc2sys adds the 37 s TAI offset)
    setsid nohup ptp4l -i enp1s0 -f "$CFG" -m > "$LOG/ptp4l.log" 2>&1 < /dev/null &
    sleep 3
    setsid nohup phc2sys -s CLOCK_REALTIME -c enp1s0 -w -f "$CFG" -m > "$LOG/phc2sys.log" 2>&1 < /dev/null & ;;
  slave)
    systemctl stop chrony systemd-timesyncd 2>/dev/null       # NTP would fight phc2sys for the system clock
    setsid nohup ptp4l -i enp1s0 -f "$CFG" -m > "$LOG/ptp4l.log" 2>&1 < /dev/null &
    sleep 6                                                  # let ptp4l lock (it steps the PHC once at start)
    # -w asks ptp4l for the UTC offset. Where AppArmor confines phc2sys (ES2, linuxptp 4.4) it cannot reach ptp4l:
    # run with PHC2SYS_NO_W=1 to use the fixed TAI-UTC offset (-O -37) instead.
    if [ "${PHC2SYS_NO_W:-0}" = 1 ]; then
      setsid nohup phc2sys -s enp1s0 -c CLOCK_REALTIME -O -37 -m > "$LOG/phc2sys.log" 2>&1 < /dev/null &
    else
      setsid nohup phc2sys -s enp1s0 -c CLOCK_REALTIME -w -f "$CFG" -m > "$LOG/phc2sys.log" 2>&1 < /dev/null &
    fi ;;
  *) echo "usage: $0 gm|slave [cfg]"; exit 1 ;;
esac
sleep 8; echo "== ptp4l"; tail -2 "$LOG/ptp4l.log"; echo "== phc2sys"; tail -2 "$LOG/phc2sys.log"
