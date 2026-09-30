#!/bin/bash
# Install gPTP as systemd services (boot-time autostart). Run as root: install_autostart.sh gm|slave <cfg_file> [nic]
# gm    : ptp4l (grandmaster) + phc2sys REALTIME -> PHC (-w: takes the TAI-UTC offset from ptp4l)
# slave : ptp4l (priority1 255) + phc2sys PHC -> REALTIME with the fixed TAI-UTC offset (-O -37); chrony/timesyncd disabled
set -e
ROLE=$1; CFG=$2; NIC=${3:-enp1s0}
[ -f "$CFG" ] || { echo "cfg $CFG missing"; exit 1; }
install -m 644 "$CFG" /etc/linuxptp/gptp_${ROLE}.cfg          # AppArmor-confined linuxptp (Ubuntu 25+) only reads /etc/linuxptp
cat > /etc/systemd/system/tsn-ptp4l.service <<UNIT
[Unit]
Description=gPTP ptp4l ($ROLE) on $NIC
After=network-online.target
Wants=network-online.target
[Service]
ExecStart=/usr/sbin/ptp4l -i $NIC -f /etc/linuxptp/gptp_${ROLE}.cfg
Restart=always
RestartSec=2
[Install]
WantedBy=multi-user.target
UNIT
if [ "$ROLE" = gm ]; then
  PHC2SYS="/usr/sbin/phc2sys -s CLOCK_REALTIME -c $NIC -w -f /etc/linuxptp/gptp_gm.cfg"
else
  PHC2SYS="/usr/sbin/phc2sys -s $NIC -c CLOCK_REALTIME -O -37"
fi
cat > /etc/systemd/system/tsn-phc2sys.service <<UNIT
[Unit]
Description=gPTP phc2sys ($ROLE) on $NIC
After=tsn-ptp4l.service
Requires=tsn-ptp4l.service
[Service]
ExecStartPre=/bin/sleep 6
ExecStart=$PHC2SYS
Restart=always
RestartSec=2
[Install]
WantedBy=multi-user.target
UNIT
if [ "$ROLE" = slave ]; then
  systemctl disable --now chrony 2>/dev/null || true
  systemctl disable --now systemd-timesyncd 2>/dev/null || true
fi
pkill -x ptp4l 2>/dev/null || true; pkill -x phc2sys 2>/dev/null || true
systemctl daemon-reload
systemctl enable --now tsn-ptp4l.service tsn-phc2sys.service
sleep 14
echo "== $(hostname): $(systemctl is-active tsn-ptp4l) / $(systemctl is-active tsn-phc2sys)  chrony=$(systemctl is-enabled chrony 2>/dev/null || echo n/a)"
journalctl -u tsn-ptp4l -n 1 --no-pager -o cat; journalctl -u tsn-phc2sys -n 1 --no-pager -o cat
