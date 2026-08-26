#!/bin/bash

# Author: <Chuanyu> (skewcy@gmail.com)
# recompile_and_deploy_nic.sh (c) 2024
# Desc: Recompile and deploy NIC driver on multiple hosts
# Created:  2024-10-27T21:30:17.885Z

hosts=(192.168.50.{13..16}) 
username="ubuntu"
tool_path="/home/ubuntu/tool"
igb_path="/lib/modules/\$(uname -r)/kernel/drivers/net/igb/"

for host in "${hosts[@]}"
do
    echo "Recompiling and deploying NIC driver on $host"

    ssh -t "$username@$host" << EOF
    set -e

    echo "Updating NIC driver on $host"
    cd $tool_path

    echo "Compiling NIC driver"
    make -C /lib/modules/\$(uname -r)/build M=\$PWD

    # echo "Installing NIC driver"
    # sudo make install

    echo "Removing old igb module"
    sudo rm -rf $igb_path
    sudo mkdir $igb_path

    echo "Copying new igb module"
    sudo cp ./igb.ko "${igb_path}igb.ko"

    echo "Updating module dependencies"
    sudo depmod -a

    echo "Loading i2c_algo_bit module"
    sudo modprobe i2c_algo_bit

    echo "Loading igb module"
    sudo modprobe igb

    echo "NIC driver update completed on $host"
EOF
done
