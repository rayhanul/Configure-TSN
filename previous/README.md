# Time-Sensitive Network Project


## 1. Introduction

## 2. Current Progress

## 3. Future Plan

## 4. Command List

### 4.1 Change interface name

    sudo ip link set dev <current-name> down
    sudo ip link set dev <current-name> name <new-name>
    sudo ip link set dev <new-name> up

### 4.1 Address setting

    sudo ip addr add 192.168.10.21/24 dev eth0
    sudo ip addr del 0.0.0.0/24 dev eth0
    sudo ip addr show

### 4.2 Link setting

    sudo ip link add link eth0 name vlan10 type vlan id 10
    sudo ip addr add 192.168.10.21/24 dev vlan10


    sudo ip link set vlan10 type vlan egress 0:3
    sudo ip link set vlan10 type vlan egress 1:3
    sudo ip link set vlan10 type vlan egress 2:3
    sudo ip link set vlan10 type vlan egress 3:3
    sudo ip link set vlan10 type vlan egress 4:3
    sudo ip link set vlan10 type vlan egress 5:3
    sudo ip link set vlan10 type vlan egress 6:3
    sudo ip link set vlan10 type vlan egress 7:3
    sudo ip link set vlan10 type vlan egress 8:3
    sudo ip link set vlan10 up


    sudo ip link del vlan10

### 4.3 Check board VLAN setting
    
    bridge vlan
    bridge vlan add dev sw0p3 vid 7

### 4.4 check schedule

    tsntool st rdacl

### Check priority

    tsntool brport rdtctbl sw0p2
    tsntool brport wrtctbl 0 1 sw0p2

### 4.5 set schedule
    
    date +%s.%N         #Check current timestamp on host
    
    tsntool st wrcl sw0p3 ./gcl/4_0.cfg

    tsntool st configure +0.0 1/100 10000 sw0p3
    
#### 4.5.1 Open one queue:

    00000000 -> 0x00
    00000001 -> 0x01
    00000010 -> 0x02
    00000100 -> 0x04
    00001000 -> 0x08
    00010000 -> 0x10
    00100000 -> 0x20
    01000000 -> 0x40
    10000000 -> 0x80
    
    
#### 4.5.2 Close one queue:

    11111110 -> 0xFE
    11111101 -> 0xFD
    11111011 -> 0xFB
    11110111 -> 0xF7
    11101111 -> 0xEF
    11011111 -> 0xDF
    10111111 -> 0xBF
    01111111 -> 0x7F

### 4.6 check port occupy

    ps -ef | grep python

### 4.7 set link speed

    ethtool -s sw0p2 speed 100 duplex full autoneg on

### 4.8 restart NIC 

    ethtool -r eth0

### 4.9 check PTP status

    deptp_tool --get-current-dataset
    deptp_tool -t 4 --get-port-dataset

## 5. Resources






### 5.1 OMINET vs GoSimu vs TTTech

| Standard                | Component           | Functionality                          | NeSTiNg | Go Simulator | TTTech Evaluation board |
| ----------------------- | ------------------- | -------------------------------------- | ------- | ------------ | ----------------------- |
| **802.1AS**             | Synchronization     | Time Synchronization                   | ✅       | ✅            | ✅                       |
| **802.1Qav**            | Latency             | Credit Based Shaper                    | ✅       | ✅            | ✅                       |
| **802.1Qbu & 802.3 Br** | Latency             | Frame Preemption                       | ✅       |              | ✅                       |
| **802.1Qbv**            | Latency             | Scheduled Traffic                      | ✅       |              | ✅                       |
| **802.1Qch**            | Latency             | Cyclic Queuing and Forwarding          |         |              |                         |
| **802.1Qcr**            | Latency             | Asynchronous Traffic Shaping           |         |              |                         |
| **802.1CB**             | Reliability         | Frame Replication and Elimination      |         | ✅            | ✅                       |
| **802.1Qca**            | Reliability         | Path Control and Reservation           |         |              |                         |
| **802.1Qci**            | Reliability         | Per-Stream Filtering and Policing      |         |              | ✅                       |
| **802.1As**             | Reliability         | Reliability for Time Sync              |         |              | ✅                       |
| **802.1Qat**            | Resource Management | Stream Reservation Protocol            |         |              |                         |
| **802.1CS**             | Resource Management | Link-local Registration Protocol       |         |              |                         |
| **802.1Qcc**            | Resource Management | TSN Configuration                      |         |              | ✅                       |
| **802.1Qcp**            | Resource Management | Foundational Bridge YANG               |         |              | ✅                       |
| **802.1Qcx**            | Resource Management | YANG for CFM                           |         |              |                         |
| P802.1ASdm              | Synchronization     | Hot Standby                            |         |              |                         |
| P802.1ASdn              | Synchronization     | YANG                                   |         |              |                         |
| P802.1ASdr              | Synchronization     | Inclusive Terminology                  |         |              |                         |
| P802.1Qdq               | Latency             | Shaper Parameter Settings              |         |              |                         |
| P802.1DC                | Latency             | QoS Provisions                         |         |              |                         |
| P802.1ABcu              | Resource Management | YANG for LLDP                          |         |              |                         |
| P802.1Qcw               | Resource Management | YANG for 802.1Qbv/Qbu/Qci              |         |              | ✅                       |
| P802.1CBcv              | Resource Management | YANG & MIB for FRER                    |         |              |                         |
| P802.1CBdb              | Resource Management | Extended Stream Identification         |         |              |                         |
| P802.1Qdd               | Resource Management | Resource Allocation Protocol           |         |              |                         |
| P802.1Qdj               | Resource Management | TSN Configuration Enhancements         |         |              |                         |
| P802.1ABdh              | Resource Management | LLDPv2 for Multiframe Data Units       |         |              |                         |
| P802.1CQ                | Resource Management | Multicast and Local Address Assignment |         |              |                         |
|                         |                     |                                        |         |              |                         |
