<!--
Author: <Chuanyu> (skewcy@gmail.com)
readme.md (c) 2024
Desc: description
Created:  2024-10-28T17:25:37.319Z
-->

# Prerequisites

- sshpass: use `ssh-copy-id` to copy ssh key to remote hosts
- sudo: set nopassword for sudo

```bash
sudo vim /etc/sudoers

## Add
ubuntu ALL=(ALL) NOPASSWD: ALL
```

# Usage


Recompile and deploy NIC driver on multiple hosts
```bash
./recompile_and_deploy_nic.sh
```

Rename network interface on multiple hosts
```bash
./rename_interface.sh
```

Configure ES IP on multiple hosts
```bash
./configure_es_ip.sh
```


