#!/bin/bash
# Sample every switch's offset-from-master for N seconds and print mean/rms/min/max per switch.
# Usage: measure_switch_offsets.sh [samples=60] [ips...]   (default ips: 192.168.0.1-8)
# One reused SSH connection per switch (ControlMaster) plus a pause between switches: the
# switches' sshd drops rapid back-to-back connections ("Connection closed by ... port 22").
N=${1:-60}; shift
[ $# -gt 0 ] && IPS="$*" || IPS=$(echo 192.168.0.{1..8})
for ip in $IPS; do
  for try in 1 2 3; do
    out=$(ssh -o ConnectTimeout=8 -o ControlMaster=auto -o ControlPath=/tmp/ptp-meas-%h -o ControlPersist=30 root@$ip \
      "deptp_tool --get-current-dataset | awk '/steps-removed/{print \$2}';
       for i in \$(seq $N); do deptp_tool --get-current-dataset | awk '/offset-from-master-ns/{print \$2}'; sleep 1; done" 2>/dev/null) && break
    sleep 3
  done
  [ -z "$out" ] && { printf "%-12s unreachable\n" "$ip"; continue; }
  echo "$out" | awk -v ip="$ip" 'NR==1{hops=$1; next}
    {n++; s+=$1; ss+=$1*$1; if(n==1||$1>mx)mx=$1; if(n==1||$1<mn)mn=$1}
    END{printf "%-12s hops %s  mean %6.0f  rms %6.0f  min %6d  max %6d  (n=%d)\n", ip, hops, s/n, sqrt(ss/n), mn, mx, n}'
  sleep 2
done
