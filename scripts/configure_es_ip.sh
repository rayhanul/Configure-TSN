#!/bin/bash

host_indexs=($(seq 13 16))
username="ubuntu"

for host_index in "${host_indexs[@]}"
do
  host="192.168.50.${host_index}"
  ssh -t "$username@$host" << EOF
  sudo ip addr add 192.168.0.${host_index}/24 dev i210
EOF
done
