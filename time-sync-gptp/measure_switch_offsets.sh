#!/bin/bash
# Sample every switch's offset-from-master for N seconds and print mean/rms/min/max per switch.
# Usage: measure_switch_offsets.sh [samples=60] [ips...]   (default ips: 192.168.0.1-8)
# PASS per switch if every |offset| < THRESH_NS (default 1000); exit 1 if any switch fails or is unreachable.
# One reused SSH connection per switch (ControlMaster) plus a pause between switches: the
# switches' sshd drops rapid back-to-back connections ("Connection closed by ... port 22").
N=${1:-60}; shift; THRESH_NS=${THRESH_NS:-1000}; rc=0
[ $# -gt 0 ] && IPS="$*" || IPS=$(echo 192.168.0.{1..8})
for ip in $IPS; do
  for try in 1 2 3; do
    out=$(ssh -o ConnectTimeout=8 -o ControlMaster=auto -o ControlPath=/tmp/ptp-meas-%h -o ControlPersist=30 root@$ip \
      "deptp_tool --get-current-dataset | awk '/steps-removed/{print \$2}';
       for i in \$(seq $N); do deptp_tool --get-current-dataset | awk '/offset-from-master-ns/{print \$2}'; sleep 1; done" 2>/dev/null) && break
    sleep 3
  done
  [ -z "$out" ] && { printf "%-12s unreachable -> FAIL\n" "$ip"; rc=1; continue; }
  echo "$out" | awk -v ip="$ip" -v t="$THRESH_NS" 'NR==1{hops=$1; next}
    {n++; s+=$1; ss+=$1*$1; if(n==1||$1>mx)mx=$1; if(n==1||$1<mn)mn=$1}
    END{w=(-mn>mx)?-mn:mx; ok=(n>0 && w<t)
        printf "%-12s hops %s  mean %6.0f  rms %6.0f  min %6d  max %6d  (n=%d)  -> %s\n", ip, hops, s/n, sqrt(ss/n), mn, mx, n, ok?"PASS":"FAIL"
        exit !ok}' || rc=1
  sleep 2
done
[ $rc = 0 ] && echo "RESULT: PASS, all switches within $THRESH_NS ns" || echo "RESULT: FAIL"
exit $rc
