#!/bin/bash

# Rename network interface on multiple hosts
hosts=(192.168.50.{13..16})
username="ubuntu"
old_interface="enp1s0" 
new_interface="i210"

for host in "${hosts[@]}"
do
  ssh -t "$username@$host" << EOF
    sudo ip link set $old_interface down
    sudo ip link set $old_interface name $new_interface
    sudo ip link set $new_interface up
EOF
done
