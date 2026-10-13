# Reconfiguration-free admission (Problem 3)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Frozen schedule W loaded from: **result/result-2026-10-12-dataset-testbed-10-ring-avgwin/rl-c9-on/10-matrix-c9on**

## Admission: W (before) vs. after this run's arrivals

| | admitted | of total |
|---|---|---|
| W (base, unchanged) | 11 | 11 |
| + this run's arrivals | 27 | 39 |

Every arrival admitted here required **zero** window-boundary changes -- see the GCL-entry table below (unchanged from W by construction) and the window-boundary integrity check. No previously-admitted flow was rerouted.

## Arrivals

| id | src->dst | RS(s) size | admitted | route | queue | phi_s (ns) | e2e (ns) | rerouted to make room | reason if rejected |
|---|---|---|---|---|---|---|---|---|---|
| 20 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 12480 | 105280 | - | - |
| 4 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q7 | 12480 | 90560 | - | - |
| 13 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q6 | 12480 | 70720 | - | - |
| 16 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 14 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 140800 | 39360 | - | - |
| 2 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 | 62400 | 69120 | - | - |
| 8 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q7 | 158720 | 35200 | - | - |
| 6 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q7 | 254400 | 29440 | - | - |
| 19 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q6 | 137600 | 274880 | - | - |
| 34 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q7 | 87360 | 31040 | - | - |
| 47 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q6 | 337600 | 87360 | - | - |
| 21 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q6 | 87360 | 125120 | - | - |
| 22 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q6 | 99840 | 125440 | - | - |
| 40 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 62400 | 375360 | - | - |
| 23 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 74880 | 55360 | - | - |
| 24 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 | 99840 | 83200 | - | - |
| 28 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q7 | 266880 | 35520 | - | - |
| 30 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q6 | 37440 | 375040 | - | - |
| 38 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q7 | 163840 | 134080 | - | - |
| 39 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q7 | 279360 | 114560 | - | - |
| 42 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 46 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 87360 | 55360 | - | - |
| 50 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 99840 | 55360 | - | - |
| 27 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 153280 | 52480 | - | - |
| 29 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 165760 | 54720 | - | - |
| 31 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 | 213760 | 69760 | - | - |
| 32 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 | 226240 | 71360 | - | - |
| 35 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 224960 | 105600 | - | - |
| 36 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 41 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 45 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 48 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 | 238720 | 71360 | - | - |
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
| sw01-p2 | 40 | 40 | 255 |
| sw01-p4 | 19 | 19 | 255 |
| sw01-p5 | 11 | 11 | 255 |
| sw02-p2 | 11 | 11 | 255 |
| sw02-p4 | 19 | 19 | 255 |
| sw02-p5 | 24 | 24 | 255 |
| sw03-p4 | 27 | 27 | 255 |
| sw03-p5 | 22 | 22 | 255 |
| sw04-p4 | 14 | 14 | 255 |
| sw04-p5 | 19 | 19 | 255 |
| sw05-p4 | 22 | 22 | 255 |
| sw05-p5 | 27 | 27 | 255 |
| sw06-p4 | 19 | 19 | 255 |
| sw06-p5 | 14 | 14 | 255 |
| sw07-p4 | 22 | 22 | 255 |
| sw07-p5 | 22 | 22 | 255 |
| sw08-p2 | 18 | 18 | 255 |
| sw08-p4 | 14 | 14 | 255 |
| sw08-p5 | 22 | 22 | 255 |

## Per-hop windows used by newly admitted flows

| flow | egress port | queue | psi (ns, unchanged) | delta (ns, unchanged) |
|---|---|---|---|---|
| s28(id=20 S2->S3) | S2-p0 | Q6 | 12480 | 12480 |
| s28(id=20 S2->S3) | sw08-p5 | Q6 | 51520 | 12480 |
| s28(id=20 S2->S3) | sw07-p4 | Q6 | 59840 | 12480 |
| s28(id=20 S2->S3) | sw05-p5 | Q6 | 68160 | 12480 |
| s28(id=20 S2->S3) | sw03-p4 | Q6 | 76480 | 12480 |
| s28(id=20 S2->S3) | sw01-p2 | Q6 | 105280 | 12480 |
| s21(id=4 S1->S3) | S1-p0 | Q7 | 12480 | 12480 |
| s21(id=4 S1->S3) | sw02-p5 | Q7 | 68480 | 12480 |
| s21(id=4 S1->S3) | sw01-p2 | Q7 | 90560 | 12480 |
| s24(id=13 S3->S2) | S3-p0 | Q6 | 12480 | 12480 |
| s24(id=13 S3->S2) | sw01-p4 | Q6 | 20160 | 12480 |
| s24(id=13 S3->S2) | sw03-p5 | Q6 | 27840 | 12480 |
| s24(id=13 S3->S2) | sw05-p4 | Q6 | 35520 | 12480 |
| s24(id=13 S3->S2) | sw07-p5 | Q6 | 61760 | 12480 |
| s24(id=13 S3->S2) | sw08-p2 | Q6 | 70720 | 12480 |
| s25(id=14 S2->S1) | S2-p0 | Q7 | 140800 | 12480 |
| s25(id=14 S2->S1) | sw08-p4 | Q7 | 147520 | 12480 |
| s25(id=14 S2->S1) | sw06-p5 | Q7 | 154240 | 12480 |
| s25(id=14 S2->S1) | sw04-p4 | Q7 | 160960 | 12480 |
| s25(id=14 S2->S1) | sw02-p2 | Q7 | 167680 | 12480 |
| s20(id=2 S3->S2) | S3-p0 | Q7 | 62400 | 12480 |
| s20(id=2 S3->S2) | sw01-p4 | Q7 | 69120 | 12480 |
| s20(id=2 S3->S2) | sw03-p5 | Q7 | 75840 | 12480 |
| s20(id=2 S3->S2) | sw05-p4 | Q7 | 82560 | 12480 |
| s20(id=2 S3->S2) | sw07-p5 | Q7 | 89280 | 12480 |
| s20(id=2 S3->S2) | sw08-p2 | Q7 | 119040 | 12480 |
| s23(id=8 S1->S3) | S1-p0 | Q7 | 158720 | 12480 |
| s23(id=8 S1->S3) | sw02-p5 | Q7 | 163840 | 12480 |
| s23(id=8 S1->S3) | sw01-p2 | Q7 | 181440 | 12480 |
| s22(id=6 S1->S3) | S1-p0 | Q7 | 254400 | 12480 |
| s22(id=6 S1->S3) | sw02-p5 | Q7 | 262720 | 12480 |
| s22(id=6 S1->S3) | sw01-p2 | Q7 | 271360 | 12480 |
| s27(id=19 S3->S1) | S3-p0 | Q6 | 137600 | 12480 |
| s27(id=19 S3->S1) | sw01-p5 | Q6 | 309760 | 12480 |
| s27(id=19 S3->S1) | sw02-p2 | Q6 | 400000 | 12480 |
| s42(id=34 S3->S1) | S3-p0 | Q7 | 87360 | 12480 |
| s42(id=34 S3->S1) | sw01-p5 | Q7 | 95040 | 12480 |
| s42(id=34 S3->S1) | sw02-p2 | Q7 | 105920 | 12480 |
| s55(id=47 S3->S1) | S3-p0 | Q6 | 337600 | 12480 |
| s55(id=47 S3->S1) | sw01-p5 | Q6 | 400000 | 12480 |
| s55(id=47 S3->S1) | sw02-p2 | Q6 | 412480 | 12480 |
| s29(id=21 S1->S2) | S1-p0 | Q6 | 87360 | 12480 |
| s29(id=21 S1->S2) | sw02-p4 | Q6 | 95040 | 12480 |
| s29(id=21 S1->S2) | sw04-p5 | Q6 | 102720 | 12480 |
| s29(id=21 S1->S2) | sw06-p4 | Q6 | 110400 | 12480 |
| s29(id=21 S1->S2) | sw08-p2 | Q6 | 200000 | 12480 |
| s30(id=22 S1->S2) | S1-p0 | Q6 | 99840 | 12480 |
| s30(id=22 S1->S2) | sw02-p4 | Q6 | 110400 | 12480 |
| s30(id=22 S1->S2) | sw04-p5 | Q6 | 118720 | 12480 |
| s30(id=22 S1->S2) | sw06-p4 | Q6 | 205120 | 12480 |
| s30(id=22 S1->S2) | sw08-p2 | Q6 | 212800 | 12480 |
| s48(id=40 S2->S1) | S2-p0 | Q6 | 62400 | 12480 |
| s48(id=40 S2->S1) | sw08-p4 | Q6 | 300160 | 12480 |
| s48(id=40 S2->S1) | sw06-p5 | Q6 | 306240 | 12480 |
| s48(id=40 S2->S1) | sw04-p4 | Q6 | 419200 | 12480 |
| s48(id=40 S2->S1) | sw02-p2 | Q6 | 425280 | 12480 |
| s31(id=23 S2->S3) | S2-p0 | Q6 | 74880 | 12480 |
| s31(id=23 S2->S3) | sw08-p5 | Q6 | 83200 | 12480 |
| s31(id=23 S2->S3) | sw07-p4 | Q6 | 91520 | 12480 |
| s31(id=23 S2->S3) | sw05-p5 | Q6 | 99840 | 12480 |
| s31(id=23 S2->S3) | sw03-p4 | Q6 | 108160 | 12480 |
| s31(id=23 S2->S3) | sw01-p2 | Q6 | 117760 | 12480 |
| s32(id=24 S3->S2) | S3-p0 | Q7 | 99840 | 12480 |
| s32(id=24 S3->S2) | sw01-p4 | Q7 | 150080 | 12480 |
| s32(id=24 S3->S2) | sw03-p5 | Q7 | 155200 | 12480 |
| s32(id=24 S3->S2) | sw05-p4 | Q7 | 160320 | 12480 |
| s32(id=24 S3->S2) | sw07-p5 | Q7 | 165440 | 12480 |
| s32(id=24 S3->S2) | sw08-p2 | Q7 | 170560 | 12480 |
| s36(id=28 S1->S3) | S1-p0 | Q7 | 266880 | 12480 |
| s36(id=28 S1->S3) | sw02-p5 | Q7 | 282240 | 12480 |
| s36(id=28 S1->S3) | sw01-p2 | Q7 | 289920 | 12480 |
| s38(id=30 S3->S2) | S3-p0 | Q6 | 37440 | 12480 |
| s38(id=30 S3->S2) | sw01-p4 | Q6 | 43520 | 12480 |
| s38(id=30 S3->S2) | sw03-p5 | Q6 | 49600 | 12480 |
| s38(id=30 S3->S2) | sw05-p4 | Q6 | 129280 | 12480 |
| s38(id=30 S3->S2) | sw07-p5 | Q6 | 336960 | 12480 |
| s38(id=30 S3->S2) | sw08-p2 | Q6 | 400000 | 12480 |
| s46(id=38 S3->S1) | S3-p0 | Q7 | 163840 | 12480 |
| s46(id=38 S3->S1) | sw01-p5 | Q7 | 172160 | 12480 |
| s46(id=38 S3->S1) | sw02-p2 | Q7 | 180480 | 12480 |
| s47(id=39 S1->S3) | S1-p0 | Q7 | 279360 | 12480 |
| s47(id=39 S1->S3) | sw02-p5 | Q7 | 294720 | 12480 |
| s47(id=39 S1->S3) | sw01-p2 | Q7 | 381440 | 12480 |
| s54(id=46 S2->S3) | S2-p0 | Q6 | 87360 | 12480 |
| s54(id=46 S2->S3) | sw08-p5 | Q6 | 95680 | 12480 |
| s54(id=46 S2->S3) | sw07-p4 | Q6 | 104000 | 12480 |
| s54(id=46 S2->S3) | sw05-p5 | Q6 | 112320 | 12480 |
| s54(id=46 S2->S3) | sw03-p4 | Q6 | 120640 | 12480 |
| s54(id=46 S2->S3) | sw01-p2 | Q6 | 130240 | 12480 |
| s58(id=50 S2->S3) | S2-p0 | Q6 | 99840 | 12480 |
| s58(id=50 S2->S3) | sw08-p5 | Q6 | 108160 | 12480 |
| s58(id=50 S2->S3) | sw07-p4 | Q6 | 116480 | 12480 |
| s58(id=50 S2->S3) | sw05-p5 | Q6 | 124800 | 12480 |
| s58(id=50 S2->S3) | sw03-p4 | Q6 | 133120 | 12480 |
| s58(id=50 S2->S3) | sw01-p2 | Q6 | 142720 | 12480 |
| s35(id=27 S2->S1) | S2-p0 | Q7 | 153280 | 12480 |
| s35(id=27 S2->S1) | sw08-p4 | Q7 | 160000 | 12480 |
| s35(id=27 S2->S1) | sw06-p5 | Q7 | 166720 | 12480 |
| s35(id=27 S2->S1) | sw04-p4 | Q7 | 187200 | 12480 |
| s35(id=27 S2->S1) | sw02-p2 | Q7 | 193280 | 12480 |
| s37(id=29 S2->S1) | S2-p0 | Q7 | 165760 | 12480 |
| s37(id=29 S2->S1) | sw08-p4 | Q7 | 174080 | 12480 |
| s37(id=29 S2->S1) | sw06-p5 | Q7 | 189440 | 12480 |
| s37(id=29 S2->S1) | sw04-p4 | Q7 | 199680 | 12480 |
| s37(id=29 S2->S1) | sw02-p2 | Q7 | 208000 | 12480 |
| s39(id=31 S3->S2) | S3-p0 | Q7 | 213760 | 12480 |
| s39(id=31 S3->S2) | sw01-p4 | Q7 | 220480 | 12480 |
| s39(id=31 S3->S2) | sw03-p5 | Q7 | 227840 | 12480 |
| s39(id=31 S3->S2) | sw05-p4 | Q7 | 235520 | 12480 |
| s39(id=31 S3->S2) | sw07-p5 | Q7 | 264320 | 12480 |
| s39(id=31 S3->S2) | sw08-p2 | Q7 | 271040 | 12480 |
| s40(id=32 S3->S2) | S3-p0 | Q7 | 226240 | 12480 |
| s40(id=32 S3->S2) | sw01-p4 | Q7 | 234560 | 12480 |
| s40(id=32 S3->S2) | sw03-p5 | Q7 | 242880 | 12480 |
| s40(id=32 S3->S2) | sw05-p4 | Q7 | 267200 | 12480 |
| s40(id=32 S3->S2) | sw07-p5 | Q7 | 276800 | 12480 |
| s40(id=32 S3->S2) | sw08-p2 | Q7 | 285120 | 12480 |
| s43(id=35 S2->S3) | S2-p0 | Q6 | 224960 | 12480 |
| s43(id=35 S2->S3) | sw08-p5 | Q6 | 233280 | 12480 |
| s43(id=35 S2->S3) | sw07-p4 | Q6 | 241600 | 12480 |
| s43(id=35 S2->S3) | sw05-p5 | Q6 | 283200 | 12480 |
| s43(id=35 S2->S3) | sw03-p4 | Q6 | 312000 | 12480 |
| s43(id=35 S2->S3) | sw01-p2 | Q6 | 318080 | 12480 |
| s56(id=48 S3->S2) | S3-p0 | Q7 | 238720 | 12480 |
| s56(id=48 S3->S2) | sw01-p4 | Q7 | 247040 | 12480 |
| s56(id=48 S3->S2) | sw03-p5 | Q7 | 271680 | 12480 |
| s56(id=48 S3->S2) | sw05-p4 | Q7 | 280000 | 12480 |
| s56(id=48 S3->S2) | sw07-p5 | Q7 | 289280 | 12480 |
| s56(id=48 S3->S2) | sw08-p2 | Q7 | 297600 | 12480 |

## Constraint check

- C1-C7, C9: OK
- window-boundary integrity (no window's psi/delta changed anywhere): OK

## GCL per egress port

### sw01-p2  (40 entries, util 49.9200 %)

```
sgs 15360 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 2560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 9920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 2240 0x3F # 00111111   BE
sgs 76160 0x40 # 01000000   Q6
sgs 18560 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 2560 0x3F # 00111111   BE
sgs 40960 0x80 # 10000000   Q7
sgs 33920 0xBF # 10111111   Q7
sgs 76160 0x40 # 01000000   Q6
sgs 18560 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 2560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 9920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 2240 0x3F # 00111111   BE
sgs 76160 0x40 # 01000000   Q6
sgs 18560 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 2560 0x3F # 00111111   BE
sgs 40960 0x80 # 10000000   Q7
sgs 33920 0xBF # 10111111   Q7
sgs 60800 0x40 # 01000000   Q6
sgs 33920 0xBF # 10111111   Q7
```

### sw01-p4  (19 entries, util 23.4000 %)

```
sgs 7680 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 23360 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 13120 0xBF # 10111111   Q7
sgs 44800 0x80 # 10000000   Q7
sgs 36160 0x7F # 01111111   Q6
sgs 57600 0xBF # 10111111   Q7
sgs 106240 0x80 # 10000000   Q7
sgs 36160 0x7F # 01111111   Q6
sgs 57600 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 23360 0x7F # 01111111   Q6
sgs 70400 0x40 # 01000000   Q6
sgs 36160 0x7F # 01111111   Q6
sgs 57600 0xBF # 10111111   Q7
sgs 98560 0x80 # 10000000   Q7
sgs 43840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p5  (11 entries, util 15.6000 %)

```
sgs 32640 0x7F # 01111111   Q6
sgs 36480 0x40 # 01000000   Q6
sgs 13440 0xBF # 10111111   Q7
sgs 227200 0x80 # 10000000   Q7
sgs 40320 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 32640 0x7F # 01111111   Q6
sgs 244480 0x40 # 01000000   Q6
sgs 23040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (11 entries, util 28.0800 %)

```
sgs 40320 0x7F # 01111111   Q6
sgs 52800 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 256320 0x80 # 10000000   Q7
sgs 50240 0xBF # 10111111   Q7
sgs 40320 0x7F # 01111111   Q6
sgs 35520 0x40 # 01000000   Q6
sgs 30720 0xBF # 10111111   Q7
sgs 202880 0x80 # 10000000   Q7
sgs 40640 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p4  (19 entries, util 10.9200 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 36800 0xBF # 10111111   Q7
sgs 27840 0x40 # 01000000   Q6
sgs 39680 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 77120 0x80 # 10000000   Q7
sgs 39680 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 77120 0x80 # 10000000   Q7
sgs 39680 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 43840 0x80 # 10000000   Q7
sgs 23040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p5  (24 entries, util 26.5200 %)

```
sgs 7680 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 35840 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 13760 0xBF # 10111111   Q7
sgs 59520 0x80 # 10000000   Q7
sgs 65920 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 29760 0x7F # 01111111   Q6
sgs 32320 0xBF # 10111111   Q7
sgs 59520 0x80 # 10000000   Q7
sgs 65920 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 35840 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 13760 0xBF # 10111111   Q7
sgs 59520 0x80 # 10000000   Q7
sgs 65920 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 29760 0x7F # 01111111   Q6
sgs 32320 0xBF # 10111111   Q7
sgs 51840 0x80 # 10000000   Q7
sgs 16000 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (27 entries, util 23.4000 %)

```
sgs 24320 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 14720 0xBF # 10111111   Q7
sgs 81920 0x40 # 01000000   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 24320 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0x7F # 01111111   Q6
sgs 26560 0xBF # 10111111   Q7
sgs 81920 0x40 # 01000000   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 24320 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 14720 0xBF # 10111111   Q7
sgs 81920 0x40 # 01000000   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 24320 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0x7F # 01111111   Q6
sgs 26560 0xBF # 10111111   Q7
sgs 57600 0x40 # 01000000   Q6
sgs 16000 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p5  (22 entries, util 23.4000 %)

```
sgs 15360 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 21760 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 13760 0xBF # 10111111   Q7
sgs 45760 0x80 # 10000000   Q7
sgs 28480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 106240 0x80 # 10000000   Q7
sgs 28480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 21760 0x7F # 01111111   Q6
sgs 72000 0x40 # 01000000   Q6
sgs 28480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 90880 0x80 # 10000000   Q7
sgs 43840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p4  (14 entries, util 12.4800 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 23040 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0xBF # 10111111   Q7
sgs 203200 0x80 # 10000000   Q7
sgs 47040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 103360 0x80 # 10000000   Q7
sgs 46720 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (19 entries, util 10.9200 %)

```
sgs 41600 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 36160 0xBF # 10111111   Q7
sgs 28480 0x40 # 01000000   Q6
sgs 31360 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 77120 0x80 # 10000000   Q7
sgs 31360 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 77120 0x80 # 10000000   Q7
sgs 31360 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 35520 0x80 # 10000000   Q7
sgs 23040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (22 entries, util 23.4000 %)

```
sgs 23040 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0xBF # 10111111   Q7
sgs 46720 0x80 # 10000000   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 106240 0x80 # 10000000   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 73600 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 83200 0x80 # 10000000   Q7
sgs 43840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p5  (27 entries, util 23.4000 %)

```
sgs 18240 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 84160 0x40 # 01000000   Q6
sgs 47680 0xBF # 10111111   Q7
sgs 18240 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 19200 0x7F # 01111111   Q6
sgs 18240 0xBF # 10111111   Q7
sgs 84160 0x40 # 01000000   Q6
sgs 47680 0xBF # 10111111   Q7
sgs 18240 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 84160 0x40 # 01000000   Q6
sgs 47680 0xBF # 10111111   Q7
sgs 18240 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 19200 0x7F # 01111111   Q6
sgs 18240 0xBF # 10111111   Q7
sgs 65920 0x40 # 01000000   Q6
sgs 16000 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p4  (19 entries, util 10.9200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 35520 0xBF # 10111111   Q7
sgs 29120 0x40 # 01000000   Q6
sgs 23040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 77120 0x80 # 10000000   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 77120 0x80 # 10000000   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 27200 0x80 # 10000000   Q7
sgs 23040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (14 entries, util 12.4800 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 15360 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 9600 0x3F # 00111111   BE
sgs 203200 0x80 # 10000000   Q7
sgs 59520 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 37440 0xBF # 10111111   Q7
sgs 115840 0x80 # 10000000   Q7
sgs 46720 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (22 entries, util 23.4000 %)

```
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 10240 0x3F # 00111111   BE
sgs 86400 0x40 # 01000000   Q6
sgs 65920 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 35200 0x7F # 01111111   Q6
sgs 86400 0x40 # 01000000   Q6
sgs 65920 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 10240 0x3F # 00111111   BE
sgs 86400 0x40 # 01000000   Q6
sgs 65920 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 35200 0x7F # 01111111   Q6
sgs 74240 0x40 # 01000000   Q6
sgs 16000 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p5  (22 entries, util 23.4000 %)

```
sgs 30720 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 18560 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 15040 0xBF # 10111111   Q7
sgs 47680 0x80 # 10000000   Q7
sgs 13120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 106240 0x80 # 10000000   Q7
sgs 13120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 18560 0xBF # 10111111   Q7
sgs 75200 0x40 # 01000000   Q6
sgs 13120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 75520 0x80 # 10000000   Q7
sgs 43840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p2  (18 entries, util 34.3200 %)

```
sgs 38400 0x7F # 01111111   Q6
sgs 32320 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 22400 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 960 0x3F # 00111111   BE
sgs 66560 0x80 # 10000000   Q7
sgs 14400 0xBF # 10111111   Q7
sgs 38400 0x7F # 01111111   Q6
sgs 147200 0x80 # 10000000   Q7
sgs 14400 0xBF # 10111111   Q7
sgs 38400 0x7F # 01111111   Q6
sgs 32320 0x80 # 10000000   Q7
sgs 114880 0x40 # 01000000   Q6
sgs 14400 0xBF # 10111111   Q7
sgs 38400 0x7F # 01111111   Q6
sgs 108800 0x80 # 10000000   Q7
sgs 52800 0xBF # 10111111   Q7
```

### sw08-p4  (14 entries, util 12.4800 %)

```
sgs 57600 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 4800 0x3F # 00111111   BE
sgs 203200 0x80 # 10000000   Q7
sgs 22080 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 128320 0x80 # 10000000   Q7
sgs 46720 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (22 entries, util 23.4000 %)

```
sgs 6080 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 8000 0x3F # 00111111   BE
sgs 88640 0x40 # 01000000   Q6
sgs 65920 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 32960 0x7F # 01111111   Q6
sgs 88640 0x40 # 01000000   Q6
sgs 65920 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 8000 0x3F # 00111111   BE
sgs 88640 0x40 # 01000000   Q6
sgs 65920 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 32960 0x7F # 01111111   Q6
sgs 82560 0x40 # 01000000   Q6
sgs 16000 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

