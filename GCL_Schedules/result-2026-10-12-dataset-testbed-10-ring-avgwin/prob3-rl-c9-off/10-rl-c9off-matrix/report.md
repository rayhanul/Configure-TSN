# Reconfiguration-free admission (Problem 3)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Frozen schedule W loaded from: **result/result-2026-10-12-dataset-testbed-10-ring-avgwin/rl-c9-off/10-matrix-c9off**

## Admission: W (before) vs. after this run's arrivals

| | admitted | of total |
|---|---|---|
| W (base, unchanged) | 11 | 11 |
| + this run's arrivals | 21 | 39 |

Every arrival admitted here required **zero** window-boundary changes -- see the GCL-entry table below (unchanged from W by construction) and the window-boundary integrity check. No previously-admitted flow was rerouted.

## Arrivals

| id | src->dst | RS(s) size | admitted | route | queue | phi_s (ns) | e2e (ns) | rerouted to make room | reason if rejected |
|---|---|---|---|---|---|---|---|---|---|
| 20 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 4 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q7 | 12480 | 45760 | - | - |
| 13 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q6 | 12480 | 225920 | - | - |
| 16 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q6 | 37440 | 191680 | - | - |
| 14 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 37440 | 109760 | - | - |
| 2 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q6 | 88000 | 350400 | - | - |
| 8 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q7 | 37440 | 45760 | - | - |
| 6 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q7 | 62400 | 72640 | - | - |
| 19 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q6 | 123200 | 49600 | - | - |
| 34 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q6 | 139840 | 89280 | - | - |
| 47 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q6 | 212480 | 45760 | - | - |
| 21 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 87680 | 79040 | - | - |
| 22 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 100480 | 112000 | - | - |
| 40 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 62720 | 287680 | - | - |
| 23 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 75200 | 134720 | - | - |
| 24 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 | 62400 | 117120 | - | - |
| 28 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 30 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 | 462400 | 95680 | - | - |
| 38 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q6 | 250240 | 45760 | - | - |
| 39 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 42 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 46 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 88000 | 321920 | - | - |
| 50 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 109440 | 319680 | - | - |
| 27 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 128960 | 234240 | - | - |
| 29 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 31 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 32 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 35 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 212800 | 166400 | - | - |
| 36 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 41 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 45 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 48 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 25 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 33 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 43 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 44 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 49 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 26 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 37 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |

## Per-port GCL entries (should equal W exactly)

| port | W entries | after arrivals | GCL_size |
|---|---|---|---|
| sw01-p2 | 31 | 31 | 255 |
| sw01-p4 | 18 | 18 | 255 |
| sw01-p5 | 23 | 23 | 255 |
| sw02-p2 | 23 | 23 | 255 |
| sw02-p4 | 19 | 19 | 255 |
| sw02-p5 | 22 | 22 | 255 |
| sw03-p4 | 21 | 21 | 255 |
| sw03-p5 | 18 | 18 | 255 |
| sw04-p4 | 15 | 15 | 255 |
| sw04-p5 | 19 | 19 | 255 |
| sw05-p4 | 18 | 18 | 255 |
| sw05-p5 | 17 | 17 | 255 |
| sw06-p4 | 19 | 19 | 255 |
| sw06-p5 | 14 | 14 | 255 |
| sw07-p4 | 20 | 20 | 255 |
| sw07-p5 | 19 | 19 | 255 |
| sw08-p2 | 25 | 25 | 255 |
| sw08-p4 | 12 | 12 | 255 |
| sw08-p5 | 20 | 20 | 255 |

## Per-hop windows used by newly admitted flows

| flow | egress port | queue | psi (ns, unchanged) | delta (ns, unchanged) |
|---|---|---|---|---|
| s21(id=4 S1->S3) | S1-p0 | Q7 | 12480 | 12480 |
| s21(id=4 S1->S3) | sw02-p5 | Q7 | 29120 | 12480 |
| s21(id=4 S1->S3) | sw01-p2 | Q7 | 45760 | 12480 |
| s24(id=13 S3->S2) | S3-p0 | Q6 | 12480 | 12480 |
| s24(id=13 S3->S2) | sw01-p4 | Q6 | 91840 | 12480 |
| s24(id=13 S3->S2) | sw03-p5 | Q6 | 108480 | 12480 |
| s24(id=13 S3->S2) | sw05-p4 | Q6 | 125120 | 12480 |
| s24(id=13 S3->S2) | sw07-p5 | Q6 | 200000 | 12480 |
| s24(id=13 S3->S2) | sw08-p2 | Q6 | 225920 | 12480 |
| s26(id=16 S3->S1) | S3-p0 | Q6 | 37440 | 12480 |
| s26(id=16 S3->S1) | sw01-p5 | Q6 | 127040 | 12480 |
| s26(id=16 S3->S1) | sw02-p2 | Q6 | 147520 | 12480 |
| s25(id=14 S2->S1) | S2-p0 | Q7 | 37440 | 12480 |
| s25(id=14 S2->S1) | sw08-p4 | Q7 | 54080 | 12480 |
| s25(id=14 S2->S1) | sw06-p5 | Q7 | 70720 | 12480 |
| s25(id=14 S2->S1) | sw04-p4 | Q7 | 118080 | 12480 |
| s25(id=14 S2->S1) | sw02-p2 | Q7 | 134720 | 12480 |
| s20(id=2 S3->S2) | S3-p0 | Q6 | 88000 | 12480 |
| s20(id=2 S3->S2) | sw01-p4 | Q6 | 104640 | 12480 |
| s20(id=2 S3->S2) | sw03-p5 | Q6 | 121280 | 12480 |
| s20(id=2 S3->S2) | sw05-p4 | Q6 | 200000 | 12480 |
| s20(id=2 S3->S2) | sw07-p5 | Q6 | 400000 | 12480 |
| s20(id=2 S3->S2) | sw08-p2 | Q6 | 425920 | 12480 |
| s23(id=8 S1->S3) | S1-p0 | Q7 | 37440 | 12480 |
| s23(id=8 S1->S3) | sw02-p5 | Q7 | 54080 | 12480 |
| s23(id=8 S1->S3) | sw01-p2 | Q7 | 70720 | 12480 |
| s22(id=6 S1->S3) | S1-p0 | Q7 | 62400 | 12480 |
| s22(id=6 S1->S3) | sw02-p5 | Q7 | 102080 | 12480 |
| s22(id=6 S1->S3) | sw01-p2 | Q7 | 122560 | 12480 |
| s27(id=19 S3->S1) | S3-p0 | Q6 | 123200 | 12480 |
| s27(id=19 S3->S1) | sw01-p5 | Q6 | 143680 | 12480 |
| s27(id=19 S3->S1) | sw02-p2 | Q6 | 160320 | 12480 |
| s42(id=34 S3->S1) | S3-p0 | Q6 | 139840 | 12480 |
| s42(id=34 S3->S1) | sw01-p5 | Q6 | 200000 | 12480 |
| s42(id=34 S3->S1) | sw02-p2 | Q6 | 216640 | 12480 |
| s55(id=47 S3->S1) | S3-p0 | Q6 | 212480 | 12480 |
| s55(id=47 S3->S1) | sw01-p5 | Q6 | 229120 | 12480 |
| s55(id=47 S3->S1) | sw02-p2 | Q6 | 245760 | 12480 |
| s29(id=21 S1->S2) | S1-p0 | Q7 | 87680 | 12480 |
| s29(id=21 S1->S2) | sw02-p4 | Q7 | 104320 | 12480 |
| s29(id=21 S1->S2) | sw04-p5 | Q7 | 120960 | 12480 |
| s29(id=21 S1->S2) | sw06-p4 | Q7 | 137600 | 12480 |
| s29(id=21 S1->S2) | sw08-p2 | Q7 | 154240 | 12480 |
| s30(id=22 S1->S2) | S1-p0 | Q7 | 100480 | 12480 |
| s30(id=22 S1->S2) | sw02-p4 | Q7 | 150080 | 12480 |
| s30(id=22 S1->S2) | sw04-p5 | Q7 | 166720 | 12480 |
| s30(id=22 S1->S2) | sw06-p4 | Q7 | 183360 | 12480 |
| s30(id=22 S1->S2) | sw08-p2 | Q7 | 200000 | 12480 |
| s48(id=40 S2->S1) | S2-p0 | Q6 | 62720 | 12480 |
| s48(id=40 S2->S1) | sw08-p4 | Q6 | 79360 | 12480 |
| s48(id=40 S2->S1) | sw06-p5 | Q6 | 304640 | 12480 |
| s48(id=40 S2->S1) | sw04-p4 | Q6 | 321280 | 12480 |
| s48(id=40 S2->S1) | sw02-p2 | Q6 | 337920 | 12480 |
| s31(id=23 S2->S3) | S2-p0 | Q6 | 75200 | 12480 |
| s31(id=23 S2->S3) | sw08-p5 | Q6 | 91840 | 12480 |
| s31(id=23 S2->S3) | sw07-p4 | Q6 | 108480 | 12480 |
| s31(id=23 S2->S3) | sw05-p5 | Q6 | 125120 | 12480 |
| s31(id=23 S2->S3) | sw03-p4 | Q6 | 141760 | 12480 |
| s31(id=23 S2->S3) | sw01-p2 | Q6 | 197440 | 12480 |
| s32(id=24 S3->S2) | S3-p0 | Q7 | 62400 | 12480 |
| s32(id=24 S3->S2) | sw01-p4 | Q7 | 79040 | 12480 |
| s32(id=24 S3->S2) | sw03-p5 | Q7 | 95680 | 12480 |
| s32(id=24 S3->S2) | sw05-p4 | Q7 | 112320 | 12480 |
| s32(id=24 S3->S2) | sw07-p5 | Q7 | 150400 | 12480 |
| s32(id=24 S3->S2) | sw08-p2 | Q7 | 167040 | 12480 |
| s38(id=30 S3->S2) | S3-p0 | Q7 | 462400 | 12480 |
| s38(id=30 S3->S2) | sw01-p4 | Q7 | 479040 | 12480 |
| s38(id=30 S3->S2) | sw03-p5 | Q7 | 495680 | 12480 |
| s38(id=30 S3->S2) | sw05-p4 | Q7 | 512320 | 12480 |
| s38(id=30 S3->S2) | sw07-p5 | Q7 | 528960 | 12480 |
| s38(id=30 S3->S2) | sw08-p2 | Q7 | 545600 | 12480 |
| s46(id=38 S3->S1) | S3-p0 | Q6 | 250240 | 12480 |
| s46(id=38 S3->S1) | sw01-p5 | Q6 | 266880 | 12480 |
| s46(id=38 S3->S1) | sw02-p2 | Q6 | 283520 | 12480 |
| s54(id=46 S2->S3) | S2-p0 | Q6 | 88000 | 12480 |
| s54(id=46 S2->S3) | sw08-p5 | Q6 | 113280 | 12480 |
| s54(id=46 S2->S3) | sw07-p4 | Q6 | 136640 | 12480 |
| s54(id=46 S2->S3) | sw05-p5 | Q6 | 200000 | 12480 |
| s54(id=46 S2->S3) | sw03-p4 | Q6 | 229440 | 12480 |
| s54(id=46 S2->S3) | sw01-p2 | Q6 | 397440 | 12480 |
| s58(id=50 S2->S3) | S2-p0 | Q6 | 109440 | 12480 |
| s58(id=50 S2->S3) | sw08-p5 | Q6 | 132800 | 12480 |
| s58(id=50 S2->S3) | sw07-p4 | Q6 | 200000 | 12480 |
| s58(id=50 S2->S3) | sw05-p5 | Q6 | 225600 | 12480 |
| s58(id=50 S2->S3) | sw03-p4 | Q6 | 400000 | 12480 |
| s58(id=50 S2->S3) | sw01-p2 | Q6 | 416640 | 12480 |
| s35(id=27 S2->S1) | S2-p0 | Q6 | 128960 | 12480 |
| s35(id=27 S2->S1) | sw08-p4 | Q6 | 300800 | 12480 |
| s35(id=27 S2->S1) | sw06-p5 | Q6 | 317440 | 12480 |
| s35(id=27 S2->S1) | sw04-p4 | Q6 | 334080 | 12480 |
| s35(id=27 S2->S1) | sw02-p2 | Q6 | 350720 | 12480 |
| s43(id=35 S2->S3) | S2-p0 | Q7 | 212800 | 12480 |
| s43(id=35 S2->S3) | sw08-p5 | Q7 | 236160 | 12480 |
| s43(id=35 S2->S3) | sw07-p4 | Q7 | 252800 | 12480 |
| s43(id=35 S2->S3) | sw05-p5 | Q7 | 269440 | 12480 |
| s43(id=35 S2->S3) | sw03-p4 | Q7 | 292160 | 12480 |
| s43(id=35 S2->S3) | sw01-p2 | Q7 | 308800 | 12480 |

## Constraint check

- C1-C7, C9: OK
- window-boundary integrity (no window's psi/delta changed anywhere): OK

## GCL per egress port

### sw01-p2  (31 entries, util 37.4400 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 1280 0x3F # 00111111   BE
sgs 74880 0x80 # 10000000   Q7
sgs 35840 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0x80 # 10000000   Q7
sgs 35840 0xBF # 10111111   Q7
sgs 101440 0x80 # 10000000   Q7
sgs 35840 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 88640 0x40 # 01000000   Q6
sgs 35840 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0x80 # 10000000   Q7
sgs 35840 0xBF # 10111111   Q7
sgs 68160 0x80 # 10000000   Q7
sgs 35840 0xBF # 10111111   Q7
```

### sw01-p4  (18 entries, util 14.0400 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 75200 0x80 # 10000000   Q7
sgs 58240 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 75200 0x80 # 10000000   Q7
sgs 58240 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 75200 0x80 # 10000000   Q7
sgs 58240 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 58560 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p5  (23 entries, util 21.8400 %)

```
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 35200 0x40 # 01000000   Q6
sgs 37760 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 133120 0x40 # 01000000   Q6
sgs 37760 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 95680 0x80 # 10000000   Q7
sgs 37760 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 104000 0x40 # 01000000   Q6
sgs 16960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (23 entries, util 31.2000 %)

```
sgs 45760 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 1280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 42560 0x40 # 01000000   Q6
sgs 55680 0x7F # 01111111   Q6
sgs 144320 0x40 # 01000000   Q6
sgs 55680 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 106880 0x80 # 10000000   Q7
sgs 55680 0x7F # 01111111   Q6
sgs 98560 0x40 # 01000000   Q6
sgs 55680 0xBF # 10111111   Q7
```

### sw02-p4  (19 entries, util 10.9200 %)

```
sgs 42240 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 36800 0xBF # 10111111   Q7
sgs 27840 0x80 # 10000000   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 42240 0x7F # 01111111   Q6
sgs 77120 0x40 # 01000000   Q6
sgs 30720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 42240 0x7F # 01111111   Q6
sgs 77120 0x40 # 01000000   Q6
sgs 30720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 42240 0x7F # 01111111   Q6
sgs 34880 0x40 # 01000000   Q6
sgs 23040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p5  (22 entries, util 20.2800 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 23040 0xBF # 10111111   Q7
sgs 54400 0x80 # 10000000   Q7
sgs 43520 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 127360 0x80 # 10000000   Q7
sgs 43520 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 89920 0x40 # 01000000   Q6
sgs 43520 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 110720 0x80 # 10000000   Q7
sgs 60160 0xBF # 10111111   Q7
```

### sw03-p4  (21 entries, util 17.1600 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 23360 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 5760 0x3F # 00111111   BE
sgs 78400 0x40 # 01000000   Q6
sgs 30080 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 23360 0xBF # 10111111   Q7
sgs 96640 0x80 # 10000000   Q7
sgs 30080 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 23360 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 5760 0x3F # 00111111   BE
sgs 78400 0x40 # 01000000   Q6
sgs 30080 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 23360 0xBF # 10111111   Q7
sgs 23360 0x80 # 10000000   Q7
sgs 53440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p5  (18 entries, util 14.0400 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 75200 0x80 # 10000000   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 75200 0x80 # 10000000   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 75200 0x80 # 10000000   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 41920 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p4  (15 entries, util 9.3600 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 203200 0x80 # 10000000   Q7
sgs 28800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 17920 0x7F # 01111111   Q6
sgs 85120 0x80 # 10000000   Q7
sgs 46720 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (19 entries, util 10.9200 %)

```
sgs 58880 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 36800 0xBF # 10111111   Q7
sgs 27840 0x80 # 10000000   Q7
sgs 14080 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 58880 0x7F # 01111111   Q6
sgs 77120 0x40 # 01000000   Q6
sgs 14080 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 58880 0x7F # 01111111   Q6
sgs 77120 0x40 # 01000000   Q6
sgs 14080 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 58880 0x7F # 01111111   Q6
sgs 18240 0x40 # 01000000   Q6
sgs 23040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (18 entries, util 14.0400 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 75200 0x80 # 10000000   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 75200 0x80 # 10000000   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 75200 0x80 # 10000000   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 25280 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p5  (17 entries, util 17.1600 %)

```
sgs 56640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 5760 0x3F # 00111111   BE
sgs 78400 0x40 # 01000000   Q6
sgs 46720 0xBF # 10111111   Q7
sgs 56640 0x7F # 01111111   Q6
sgs 96640 0x80 # 10000000   Q7
sgs 46720 0xBF # 10111111   Q7
sgs 56640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 5760 0x3F # 00111111   BE
sgs 78400 0x40 # 01000000   Q6
sgs 46720 0xBF # 10111111   Q7
sgs 56640 0x7F # 01111111   Q6
sgs 40000 0x80 # 10000000   Q7
sgs 53440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p4  (19 entries, util 10.9200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 25600 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 36800 0x7F # 01111111   Q6
sgs 27840 0x80 # 10000000   Q7
sgs 47360 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 25600 0xBF # 10111111   Q7
sgs 77120 0x40 # 01000000   Q6
sgs 47360 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 25600 0xBF # 10111111   Q7
sgs 77120 0x40 # 01000000   Q6
sgs 47360 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 25600 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 62080 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (14 entries, util 9.3600 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 203200 0x80 # 10000000   Q7
sgs 45440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 51520 0xBF # 10111111   Q7
sgs 101760 0x80 # 10000000   Q7
sgs 46720 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (20 entries, util 17.1600 %)

```
sgs 40000 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 5760 0x3F # 00111111   BE
sgs 78400 0x40 # 01000000   Q6
sgs 13440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 40000 0x7F # 01111111   Q6
sgs 96640 0x80 # 10000000   Q7
sgs 13440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 40000 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 5760 0x3F # 00111111   BE
sgs 78400 0x40 # 01000000   Q6
sgs 13440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 40000 0x7F # 01111111   Q6
sgs 56640 0x80 # 10000000   Q7
sgs 53440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p5  (19 entries, util 14.0400 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 75200 0x80 # 10000000   Q7
sgs 58240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 75200 0x80 # 10000000   Q7
sgs 58240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 75200 0x80 # 10000000   Q7
sgs 58240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 21120 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p2  (25 entries, util 24.9600 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12160 0x3F # 00111111   BE
sgs 105280 0x80 # 10000000   Q7
sgs 24000 0x7F # 01111111   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 129920 0x40 # 01000000   Q6
sgs 24000 0x7F # 01111111   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12160 0x3F # 00111111   BE
sgs 105280 0x80 # 10000000   Q7
sgs 24000 0x7F # 01111111   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 46720 0x40 # 01000000   Q6
sgs 57280 0xBF # 10111111   Q7
```

### sw08-p4  (12 entries, util 9.3600 %)

```
sgs 54080 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 190720 0x40 # 01000000   Q6
sgs 42880 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 54080 0x7F # 01111111   Q6
sgs 149120 0x80 # 10000000   Q7
sgs 46720 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (20 entries, util 17.1600 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 71680 0x40 # 01000000   Q6
sgs 36800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 96640 0x80 # 10000000   Q7
sgs 36800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 71680 0x40 # 01000000   Q6
sgs 36800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 80000 0x80 # 10000000   Q7
sgs 53440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

