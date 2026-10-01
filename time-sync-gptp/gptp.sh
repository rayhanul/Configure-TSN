#!/bin/bash
# IEEE 802.1AS (gPTP) time sync with linuxptp on Intel I210 (igb) / I225-I226 (igc), hardware timestamping.
#
#   gptp.sh detect                  list NICs with driver, PHC (/dev/ptpN), link and speed
#   gptp.sh check   [IF]            verify hardware timestamping; report EEE and NTP state
#   gptp.sh run     gm|slave [IF]   run ptp4l + phc2sys in the foreground (-m), Ctrl-C stops both (root)
#   gptp.sh install gm|slave [IF]   install config + systemd units and start them (root)
#   gptp.sh status                  service state, ptp4l port state, last log lines (root)
#   gptp.sh verify  [SECONDS]       PASS if every locked offset in the window is < 1 us (default 120 s) (root)
#   gptp.sh uninstall               stop and remove the units (root)
#
# Grandmaster: the PHC runs free (set once to system time + 37 s = TAI), ptp4l serves it to the network,
# phc2sys makes the system clock follow the PHC. Slave: ptp4l disciplines the PHC from the network,
# phc2sys makes the system clock follow the PHC. NTP/chrony are disabled on both, so nothing else
# steers either clock. IF defaults to the first igb/igc interface with a PHC and link up.
set -u
HERE=$(cd "$(dirname "$0")" && pwd)
ENV=/etc/linuxptp/tsn-gptp.env      # ROLE, IF, CFG of the installed setup
TAI_UTC=37                          # TAI - UTC in seconds (unchanged since 2017)
THRESH_NS=${THRESH_NS:-1000}
# -N 5: read the PHC 5 times per update and use the fastest read. On I210 the PCIe read takes ~3.7 us and
# jitters; this cut the system clock's worst offset from 843 to ~510 ns (rms 228 -> 165 ns).
PHC2SYS_OPTS=${PHC2SYS_OPTS:--N 5}

die() { echo "error: $*" >&2; exit 1; }
need_root() { [ "$(id -u)" = 0 ] || die "run as root: sudo $0 $*"; }
load_env() { [ -r "$ENV" ] || die "$ENV missing: run '$0 install gm|slave' first"; . "$ENV"; }

driver_of() { basename "$(readlink -f "/sys/class/net/$1/device/driver" 2>/dev/null)" 2>/dev/null; }

phc_of() {  # ptpN of the interface, empty if none
  local p; p=$(ls "/sys/class/net/$1/device/ptp" 2>/dev/null | head -1)
  [ -n "$p" ] || p=$(ethtool -T "$1" 2>/dev/null |
    awk -F': *' '/PTP Hardware Clock|provider index/ && $2 ~ /^[0-9]+$/ {print "ptp" $2; exit}')
  echo "$p"
}

default_if() {  # first igb/igc interface with a PHC, preferring one with link up
  local n first=
  for n in $(ls /sys/class/net); do
    case $(driver_of "$n") in igb|igc) ;; *) continue ;; esac
    [ -n "$(phc_of "$n")" ] || continue
    [ "$(cat "/sys/class/net/$n/carrier" 2>/dev/null)" = 1 ] && { echo "$n"; return; }
    [ -n "$first" ] || first=$n
  done
  echo "$first"
}

pick_if() {
  local i=${1:-${IF:-}}
  [ -n "$i" ] || i=$(default_if)
  [ -n "$i" ] || die "no igb/igc interface with a PHC found; pass the interface name"
  [ -e "/sys/class/net/$i" ] || die "no interface $i"
  echo "$i"
}

phc2sys_utc_args() {  # how phc2sys learns TAI-UTC: from ptp4l (-w) or fixed (-O -37)
  # Ubuntu's AppArmor profile for linuxptp >= 4.4 blocks phc2sys from ptp4l's UNIX socket, so -w
  # would hang there. UTC_MODE=w|fixed overrides the detection.
  local mode=${UTC_MODE:-auto}
  if [ "$mode" = auto ]; then
    ls /etc/apparmor.d 2>/dev/null | grep -q phc2sys && mode=fixed || mode=w
  fi
  # -f is needed with -w so phc2sys queries ptp4l with transportSpecific 0x1
  [ "$mode" = w ] && echo "-w -f $1" || echo "-O -$TAI_UTC"
}

cmd_detect() {
  local n drv phc pci speed link
  printf '%-14s %-8s %-11s %-5s %-9s %s\n' IFACE DRIVER PHC LINK SPEED PCI
  for n in $(ls /sys/class/net); do
    [ -e "/sys/class/net/$n/device" ] || continue
    drv=$(driver_of "$n"); phc=$(phc_of "$n")
    pci=$(basename "$(readlink -f "/sys/class/net/$n/device")")
    speed=$(cat "/sys/class/net/$n/speed" 2>/dev/null)
    [ "${speed:--1}" -gt 0 ] 2>/dev/null && speed=${speed}Mb/s || speed=-
    [ "$(cat "/sys/class/net/$n/carrier" 2>/dev/null)" = 1 ] && link=up || link=down
    phc=${phc:+/dev/$phc}
    printf '%-14s %-8s %-11s %-5s %-9s %s\n' "$n" "${drv:--}" "${phc:--}" "$link" "$speed" "$pci"
  done
  echo
  echo "default: $(default_if)   (igb = I210, igc = I225/I226; override with an argument or IF=<name>)"
}

cmd_check() {
  local IF ts c ok=1 phc drv pci id rev
  IF=$(pick_if "${1:-}") || exit 1
  command -v ptp4l >/dev/null || die "linuxptp missing: sudo apt install -y linuxptp ethtool"
  command -v ethtool >/dev/null || die "ethtool missing: sudo apt install -y ethtool"
  ts=$(ethtool -T "$IF" 2>&1) || die "ethtool -T $IF failed: $ts"
  echo "$ts"; echo
  for c in hardware-transmit hardware-receive hardware-raw-clock; do
    if grep -qw -- "$c" <<<"$ts"; then echo "ok    $c"; else echo "FAIL  $c missing"; ok=0; fi
  done
  phc=$(phc_of "$IF")
  if [ -n "$phc" ] && [ -c "/dev/$phc" ]; then echo "ok    PTP hardware clock /dev/$phc"
  else echo "FAIL  no PTP hardware clock on $IF"; ok=0; fi
  drv=$(driver_of "$IF")
  case $drv in igb|igc) echo "ok    driver $drv" ;; *) echo "warn  driver ${drv:-?} (not igb/igc)" ;; esac
  # I225 steppings before B3 (rev 03) have known timestamping errors, especially at 2.5 Gb/s
  pci=$(basename "$(readlink -f "/sys/class/net/$IF/device")")
  read -r id rev < <(lspci -n -s "$pci" 2>/dev/null | sed -n 's/.* \(8086:[0-9a-f]*\) *(rev \(..\)).*/\1 \2/p')
  case "${id:-}:${rev:-}" in 8086:15f[23]:0[12]) echo "warn  I225 rev $rev: pre-B3 stepping, fix the link at 1 Gb/s or use B3/I226" ;; esac
  if ethtool --show-eee "$IF" 2>/dev/null | grep -q 'EEE status: enabled - active'; then
    echo "warn  Energy-Efficient Ethernet is on (adds latency jitter); run/install turn it off"
  else echo "ok    EEE off"; fi
  if [ "$(timedatectl show -p NTP --value 2>/dev/null)" = yes ] || systemctl is-active -q chrony 2>/dev/null; then
    echo "warn  NTP/chrony is active and would fight phc2sys; run/install turn it off"
  else echo "ok    NTP/chrony off"; fi
  [ $ok = 1 ] && echo "=> $IF supports hardware timestamping" || echo "=> $IF can NOT do hardware PTP"
  [ $ok = 1 ]
}

disable_eee() {  # only when active: changing EEE renegotiates the link
  if ethtool --show-eee "$1" 2>/dev/null | grep -q 'EEE status: enabled - active'; then
    ethtool --set-eee "$1" eee off && sleep 4
  fi
}

disable_ntp() {
  local u
  timedatectl set-ntp false 2>/dev/null
  for u in chrony systemd-timesyncd ntp ntpsec; do systemctl disable --now "$u" 2>/dev/null; done
  return 0
}

cmd_init_phc() {  # GM: set the PHC to TAI only if it is more than 1 s off (never steps a running network)
  local phc now
  [ -n "${IF:-}" ] || load_env
  phc=$(phc_ctl "$IF" get 2>&1 | awk '{for (i = 1; i < NF; i++) if ($i == "is") {print $(i+1); exit}}')
  now=$(date +%s.%N)
  if [ -n "$phc" ] && awk -v p="$phc" -v n="$now" -v t=$TAI_UTC 'BEGIN {d = p - n - t; exit !(d < 1 && d > -1)}'; then
    echo "PHC of $IF is within 1 s of TAI, left as is"
  else
    echo "PHC of $IF is off (PHC=$phc system=$now): setting it to system time + $TAI_UTC s"
    phc_ctl "$IF" set adj $TAI_UTC >/dev/null
  fi
}

role_args() {  # sets ROLE, IF, CFG from "gm|slave [IF]"
  ROLE=${1:-}
  case $ROLE in gm|slave) ;; *) die "usage: $0 ${CMD} gm|slave [IF]" ;; esac
  IF=$(pick_if "${2:-}") || exit 1
  local out; out=$(cmd_check "$IF") || { echo "$out"; die "hardware timestamping not available on $IF"; }
}

cmd_run() {
  need_root run "$@"; role_args "$@"
  CFG=$HERE/gptp_$ROLE.cfg
  local log=$HERE/logs; mkdir -p "$log"
  systemctl stop tsn-phc2sys tsn-ptp4l 2>/dev/null; pkill -x phc2sys; pkill -x ptp4l; sleep 1
  disable_ntp; disable_eee "$IF"
  [ "$ROLE" = gm ] && cmd_init_phc
  trap 'kill $(jobs -p) 2>/dev/null; wait; exit' INT TERM
  ptp4l -i "$IF" -f "$CFG" -m 2>&1 | tee "$log/ptp4l_$ROLE.log" | sed -u 's/^/[ptp4l]   /' &
  sleep 6
  # shellcheck disable=SC2046
  phc2sys -s "$IF" -c CLOCK_REALTIME $(phc2sys_utc_args "$CFG") $PHC2SYS_OPTS -m 2>&1 |
    tee "$log/phc2sys_$ROLE.log" | sed -u 's/^/[phc2sys] /' &
  echo "logs: $log  (check them with: $0 verify-log $log/*_$ROLE.log)"
  wait
}

cmd_install() {
  need_root install "$@"; role_args "$@"
  local ptp4l phc2sys ethtool pre=
  ptp4l=$(command -v ptp4l); phc2sys=$(command -v phc2sys); ethtool=$(command -v ethtool)
  CFG=/etc/linuxptp/gptp_$ROLE.cfg     # AppArmor-confined linuxptp only reads configs from /etc/linuxptp
  install -d /etc/linuxptp
  install -m 644 "$HERE/gptp_$ROLE.cfg" "$CFG"
  install -m 755 "$HERE/gptp.sh" /usr/local/sbin/tsn-gptp
  printf 'ROLE=%s\nIF=%s\nCFG=%s\n' "$ROLE" "$IF" "$CFG" > "$ENV"
  [ "$ROLE" = gm ] && pre="ExecStartPre=/usr/local/sbin/tsn-gptp init-phc"

  cat > /etc/systemd/system/tsn-ptp4l.service <<UNIT
[Unit]
Description=gPTP (802.1AS) ptp4l, $ROLE, on $IF
After=network-online.target
Wants=network-online.target
Conflicts=ptp4l@$IF.service

[Service]
ExecStartPre=-/bin/sh -c '$ethtool --show-eee $IF | grep -q \"EEE status: enabled - active\" && $ethtool --set-eee $IF eee off && sleep 4'
$pre
ExecStart=$ptp4l -i $IF -f $CFG
Restart=always
RestartSec=2

[Install]
WantedBy=multi-user.target
UNIT

  cat > /etc/systemd/system/tsn-phc2sys.service <<UNIT
[Unit]
Description=gPTP phc2sys ($ROLE): CLOCK_REALTIME follows the PHC of $IF
After=tsn-ptp4l.service
Requires=tsn-ptp4l.service
Conflicts=phc2sys@$IF.service

[Service]
ExecStartPre=/bin/sleep 6
ExecStart=$phc2sys -s $IF -c CLOCK_REALTIME $(phc2sys_utc_args "$CFG") $PHC2SYS_OPTS
Restart=always
RestartSec=2

[Install]
WantedBy=multi-user.target
UNIT

  disable_ntp
  systemctl stop tsn-phc2sys tsn-ptp4l 2>/dev/null; pkill -x phc2sys; pkill -x ptp4l
  systemctl daemon-reload
  systemctl enable --now tsn-ptp4l.service tsn-phc2sys.service
  echo "installed $ROLE on $IF; waiting 20 s for lock..."
  sleep 20
  cmd_status
}

cmd_status() {
  need_root status; load_env
  local u
  echo "role=$ROLE  if=$IF  phc=/dev/$(phc_of "$IF")  cfg=$CFG"
  for u in tsn-ptp4l tsn-phc2sys; do
    printf '%-12s %s\n' "$u" "$(systemctl is-active $u)"
    journalctl -u $u -n 3 -o cat --no-pager | sed 's/^/    /'
  done
  echo "ptp4l data sets:"
  local ds; ds=$(timeout 3 pmc -u -b 0 -f "$CFG" 'GET PORT_DATA_SET' 'GET TIME_STATUS_NP' 2>/dev/null |
    grep -E 'portState|peerMeanPathDelay|master_offset|gmPresent|gmIdentity')
  [ -n "$ds" ] && echo "$ds" | sed 's/^ */    /' || echo "    (pmc got no answer; AppArmor may block it)"
}

offset_stats() {  # stdin: ptp4l/phc2sys log lines; $1 label. Prints stats, exit 0 = PASS
  awk -v u="$1" -v t="$THRESH_NS" '
    { v = ""; st = "s2"
      for (i = 1; i < NF; i++) {
        if ($i == "max") v = $(i+1)                              # ptp4l summary: rms <ns> max <ns> ...
        else if ($i == "offset") { v = $(i+1); st = $(i+2) }     # per sample: ... offset <ns> s0|s1|s2 ...
      }
      if (st !~ /^s[0-9]$/) st = "s2"                            # no state column: count it as locked
      if (v !~ /^[-+]?[0-9]+$/) next
      if (st != "s2") { unlocked++; next }
      v += 0; if (v < 0) v = -v
      n++; s += v * v; if (v > m) m = v; if (v < t) ok++
    }
    END {
      if (!n) { printf "%-12s no locked (s2) samples, %d unlocked\n", u, unlocked; exit 1 }
      pass = (m < t && !unlocked)
      printf "%-12s samples=%d  rms=%.0f ns  worst=%d ns  <%d ns: %.1f%%  unlocked=%d  -> %s\n",
             u, n, sqrt(s / n), m, t, 100 * ok / n, unlocked, pass ? "PASS" : "FAIL"
      exit !pass
    }'
}

cmd_verify() {
  need_root verify; load_env
  local win=${1:-120} rc=0 u
  echo "$ROLE on $IF, last ${win} s, threshold ${THRESH_NS} ns"
  for u in tsn-ptp4l tsn-phc2sys; do
    if [ "$ROLE" = gm ] && [ $u = tsn-ptp4l ]; then
      echo "tsn-ptp4l    grandmaster: it is the time source, nothing to measure"; continue
    fi
    journalctl -u $u --since "-${win}s" -o cat --no-pager | offset_stats $u || rc=1
  done
  [ $rc = 0 ] && echo "RESULT: PASS (sub-microsecond)" || echo "RESULT: FAIL"
  return $rc
}

cmd_verify_log() {  # same check on log files written by 'run' (or any ptp4l/phc2sys -m output)
  local f rc=0
  [ $# -gt 0 ] || die "usage: $0 verify-log FILE..."
  for f in "$@"; do offset_stats "$(basename "$f" .log)" < "$f" || rc=1; done
  return $rc
}

cmd_uninstall() {
  need_root uninstall
  systemctl disable --now tsn-phc2sys tsn-ptp4l 2>/dev/null
  rm -f /etc/systemd/system/tsn-ptp4l.service /etc/systemd/system/tsn-phc2sys.service \
        /usr/local/sbin/tsn-gptp "$ENV"
  systemctl daemon-reload
  echo "removed. NTP stays off; turn it back on with: sudo timedatectl set-ntp true"
}

CMD=${1:-}; shift || true
case $CMD in
  detect)     cmd_detect ;;
  check)      cmd_check "$@" ;;
  run)        cmd_run "$@" ;;
  install)    cmd_install "$@" ;;
  init-phc)   cmd_init_phc ;;
  status)     cmd_status ;;
  verify)     cmd_verify "$@" ;;
  verify-log) cmd_verify_log "$@" ;;
  uninstall)  cmd_uninstall ;;
  *) sed -n '2,11p' "$0" | sed 's/^# \{0,1\}//'; exit 1 ;;
esac
