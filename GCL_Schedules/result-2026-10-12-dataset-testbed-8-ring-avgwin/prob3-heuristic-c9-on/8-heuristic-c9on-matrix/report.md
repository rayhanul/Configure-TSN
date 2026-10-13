# Reconfiguration-free admission (Problem 3)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Frozen schedule W loaded from: **result/result-2026-10-12-dataset-testbed-8-ring-avgwin/heuristic-c9-on/8-matrix-c9on**

## Admission: W (before) vs. after this run's arrivals

| | admitted | of total |
|---|---|---|
| W (base, unchanged) | 10 | 10 |
| + this run's arrivals | 29 | 40 |

Every arrival admitted here required **zero** window-boundary changes -- see the GCL-entry table below (unchanged from W by construction) and the window-boundary integrity check. No previously-admitted flow was rerouted.

## Arrivals

| id | src->dst | RS(s) size | admitted | route | queue | phi_s (ns) | e2e (ns) | rerouted to make room | reason if rejected |
|---|---|---|---|---|---|---|---|---|---|
| 14 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 49920 | 135360 | - | - |
| 8 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q6 | 0 | 45120 | - | - |
| 16 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 49920 | 49920 | - | - |
| 11 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q6 | 0 | 212480 | - | - |
| 15 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 1 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 12480 | 333760 | - | - |
| 7 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 77440 | 59520 | - | - |
| 17 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q7 | 74880 | 123200 | - | - |
| 3 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q7 | 74880 | 29120 | - | - |
| 4 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q6 | 99840 | 49600 | - | - |
| 29 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q7 | 87360 | 29120 | - | - |
| 35 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q6 | 133120 | 87680 | - | - |
| 45 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q7 | 99840 | 29120 | - | - |
| 47 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q7 | 112320 | 29120 | - | - |
| 50 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q7 | 124800 | 29120 | - | - |
| 28 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 24960 | 394240 | - | - |
| 32 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 311040 | 136960 | - | - |
| 46 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q6 | 24960 | 200320 | - | - |
| 21 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q6 | 24960 | 387520 | - | - |
| 30 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 | 49920 | 118720 | - | - |
| 43 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 26 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q6 | 224960 | 200320 | - | - |
| 31 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 157440 | 104960 | - | - |
| 44 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 262400 | 106240 | - | - |
| 48 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 150080 | 39360 | - | - |
| 22 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 111040 | 301440 | - | - |
| 23 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 212480 | 52800 | - | - |
| 25 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 224960 | 52800 | - | - |
| 27 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 262400 | 113600 | - | - |
| 34 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 274880 | 113600 | - | - |
| 36 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 38 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 41 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 49 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 37 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 162560 | 39360 | - | - |
| 40 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 42 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 24 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 33 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 39 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |

## Per-port GCL entries (should equal W exactly)

| port | W entries | after arrivals | GCL_size |
|---|---|---|---|
| sw01-p2 | 28 | 28 | 255 |
| sw01-p4 | 18 | 18 | 255 |
| sw01-p5 | 16 | 16 | 255 |
| sw02-p2 | 18 | 18 | 255 |
| sw02-p4 | 18 | 18 | 255 |
| sw02-p5 | 24 | 24 | 255 |
| sw03-p4 | 20 | 20 | 255 |
| sw03-p5 | 18 | 18 | 255 |
| sw04-p4 | 14 | 14 | 255 |
| sw04-p5 | 22 | 22 | 255 |
| sw05-p4 | 18 | 18 | 255 |
| sw05-p5 | 20 | 20 | 255 |
| sw06-p4 | 22 | 22 | 255 |
| sw06-p5 | 14 | 14 | 255 |
| sw07-p4 | 23 | 23 | 255 |
| sw07-p5 | 18 | 18 | 255 |
| sw08-p2 | 22 | 22 | 255 |
| sw08-p4 | 13 | 13 | 255 |
| sw08-p5 | 23 | 23 | 255 |

## Per-hop windows used by newly admitted flows

| flow | egress port | queue | psi (ns, unchanged) | delta (ns, unchanged) |
|---|---|---|---|---|
| s26(id=14 S2->S3) | S2-p0 | Q7 | 49920 | 12480 |
| s26(id=14 S2->S3) | sw08-p5 | Q7 | 56640 | 12480 |
| s26(id=14 S2->S3) | sw07-p4 | Q7 | 63360 | 12480 |
| s26(id=14 S2->S3) | sw05-p5 | Q7 | 70080 | 12480 |
| s26(id=14 S2->S3) | sw03-p4 | Q7 | 76800 | 12480 |
| s26(id=14 S2->S3) | sw01-p2 | Q7 | 172800 | 12480 |
| s24(id=8 S1->S2) | S1-p0 | Q6 | 0 | 12480 |
| s24(id=8 S1->S2) | sw02-p4 | Q6 | 12480 | 12480 |
| s24(id=8 S1->S2) | sw04-p5 | Q6 | 19200 | 12480 |
| s24(id=8 S1->S2) | sw06-p4 | Q6 | 25920 | 12480 |
| s24(id=8 S1->S2) | sw08-p2 | Q6 | 32640 | 12480 |
| s28(id=16 S1->S2) | S1-p0 | Q7 | 49920 | 12480 |
| s28(id=16 S1->S2) | sw02-p4 | Q7 | 58240 | 12480 |
| s28(id=16 S1->S2) | sw04-p5 | Q7 | 66560 | 12480 |
| s28(id=16 S1->S2) | sw06-p4 | Q7 | 74880 | 12480 |
| s28(id=16 S1->S2) | sw08-p2 | Q7 | 83200 | 12480 |
| s25(id=11 S3->S2) | S3-p0 | Q6 | 0 | 12480 |
| s25(id=11 S3->S2) | sw01-p4 | Q6 | 24960 | 12480 |
| s25(id=11 S3->S2) | sw03-p5 | Q6 | 31680 | 12480 |
| s25(id=11 S3->S2) | sw05-p4 | Q6 | 100160 | 12480 |
| s25(id=11 S3->S2) | sw07-p5 | Q6 | 106880 | 12480 |
| s25(id=11 S3->S2) | sw08-p2 | Q6 | 200000 | 12480 |
| s20(id=1 S2->S1) | S2-p0 | Q6 | 12480 | 12480 |
| s20(id=1 S2->S1) | sw08-p4 | Q6 | 19200 | 12480 |
| s20(id=1 S2->S1) | sw06-p5 | Q6 | 25920 | 12480 |
| s20(id=1 S2->S1) | sw04-p4 | Q6 | 300160 | 12480 |
| s20(id=1 S2->S1) | sw02-p2 | Q6 | 333760 | 12480 |
| s23(id=7 S2->S3) | S2-p0 | Q6 | 77440 | 12480 |
| s23(id=7 S2->S3) | sw08-p5 | Q6 | 100160 | 12480 |
| s23(id=7 S2->S3) | sw07-p4 | Q6 | 106240 | 12480 |
| s23(id=7 S2->S3) | sw05-p5 | Q6 | 112320 | 12480 |
| s23(id=7 S2->S3) | sw03-p4 | Q6 | 118400 | 12480 |
| s23(id=7 S2->S3) | sw01-p2 | Q6 | 124480 | 12480 |
| s29(id=17 S1->S3) | S1-p0 | Q7 | 74880 | 12480 |
| s29(id=17 S1->S3) | sw02-p5 | Q7 | 178880 | 12480 |
| s29(id=17 S1->S3) | sw01-p2 | Q7 | 185600 | 12480 |
| s21(id=3 S3->S1) | S3-p0 | Q7 | 74880 | 12480 |
| s21(id=3 S3->S1) | sw01-p5 | Q7 | 83200 | 12480 |
| s21(id=3 S3->S1) | sw02-p2 | Q7 | 91520 | 12480 |
| s22(id=4 S1->S3) | S1-p0 | Q6 | 99840 | 12480 |
| s22(id=4 S1->S3) | sw02-p5 | Q6 | 128640 | 12480 |
| s22(id=4 S1->S3) | sw01-p2 | Q6 | 136960 | 12480 |
| s38(id=29 S3->S1) | S3-p0 | Q7 | 87360 | 12480 |
| s38(id=29 S3->S1) | sw01-p5 | Q7 | 95680 | 12480 |
| s38(id=29 S3->S1) | sw02-p2 | Q7 | 104000 | 12480 |
| s44(id=35 S1->S3) | S1-p0 | Q6 | 133120 | 12480 |
| s44(id=35 S1->S3) | sw02-p5 | Q6 | 200000 | 12480 |
| s44(id=35 S1->S3) | sw01-p2 | Q6 | 208320 | 12480 |
| s54(id=45 S3->S1) | S3-p0 | Q7 | 99840 | 12480 |
| s54(id=45 S3->S1) | sw01-p5 | Q7 | 108160 | 12480 |
| s54(id=45 S3->S1) | sw02-p2 | Q7 | 116480 | 12480 |
| s56(id=47 S3->S1) | S3-p0 | Q7 | 112320 | 12480 |
| s56(id=47 S3->S1) | sw01-p5 | Q7 | 120640 | 12480 |
| s56(id=47 S3->S1) | sw02-p2 | Q7 | 128960 | 12480 |
| s59(id=50 S3->S1) | S3-p0 | Q7 | 124800 | 12480 |
| s59(id=50 S3->S1) | sw01-p5 | Q7 | 133120 | 12480 |
| s59(id=50 S3->S1) | sw02-p2 | Q7 | 141440 | 12480 |
| s37(id=28 S2->S1) | S2-p0 | Q6 | 24960 | 12480 |
| s37(id=28 S2->S1) | sw08-p4 | Q6 | 300160 | 12480 |
| s37(id=28 S2->S1) | sw06-p5 | Q6 | 306880 | 12480 |
| s37(id=28 S2->S1) | sw04-p4 | Q6 | 400000 | 12480 |
| s37(id=28 S2->S1) | sw02-p2 | Q6 | 406720 | 12480 |
| s41(id=32 S2->S1) | S2-p0 | Q6 | 311040 | 12480 |
| s41(id=32 S2->S1) | sw08-p4 | Q6 | 319360 | 12480 |
| s41(id=32 S2->S1) | sw06-p5 | Q6 | 402880 | 12480 |
| s41(id=32 S2->S1) | sw04-p4 | Q6 | 427200 | 12480 |
| s41(id=32 S2->S1) | sw02-p2 | Q6 | 435520 | 12480 |
| s55(id=46 S1->S2) | S1-p0 | Q6 | 24960 | 12480 |
| s55(id=46 S1->S2) | sw02-p4 | Q6 | 32640 | 12480 |
| s55(id=46 S1->S2) | sw04-p5 | Q6 | 129280 | 12480 |
| s55(id=46 S1->S2) | sw06-p4 | Q6 | 205120 | 12480 |
| s55(id=46 S1->S2) | sw08-p2 | Q6 | 212800 | 12480 |
| s30(id=21 S3->S2) | S3-p0 | Q6 | 24960 | 12480 |
| s30(id=21 S3->S2) | sw01-p4 | Q6 | 37440 | 12480 |
| s30(id=21 S3->S2) | sw03-p5 | Q6 | 100160 | 12480 |
| s30(id=21 S3->S2) | sw05-p4 | Q6 | 112640 | 12480 |
| s30(id=21 S3->S2) | sw07-p5 | Q6 | 234560 | 12480 |
| s30(id=21 S3->S2) | sw08-p2 | Q6 | 400000 | 12480 |
| s39(id=30 S3->S2) | S3-p0 | Q7 | 49920 | 12480 |
| s39(id=30 S3->S2) | sw01-p4 | Q7 | 56000 | 12480 |
| s39(id=30 S3->S2) | sw03-p5 | Q7 | 62080 | 12480 |
| s39(id=30 S3->S2) | sw05-p4 | Q7 | 68160 | 12480 |
| s39(id=30 S3->S2) | sw07-p5 | Q7 | 150080 | 12480 |
| s39(id=30 S3->S2) | sw08-p2 | Q7 | 156160 | 12480 |
| s35(id=26 S1->S2) | S1-p0 | Q6 | 224960 | 12480 |
| s35(id=26 S1->S2) | sw02-p4 | Q6 | 230080 | 12480 |
| s35(id=26 S1->S2) | sw04-p5 | Q6 | 235200 | 12480 |
| s35(id=26 S1->S2) | sw06-p4 | Q6 | 407680 | 12480 |
| s35(id=26 S1->S2) | sw08-p2 | Q6 | 412800 | 12480 |
| s40(id=31 S1->S2) | S1-p0 | Q7 | 157440 | 12480 |
| s40(id=31 S1->S2) | sw02-p4 | Q7 | 165760 | 12480 |
| s40(id=31 S1->S2) | sw04-p5 | Q7 | 174080 | 12480 |
| s40(id=31 S1->S2) | sw06-p4 | Q7 | 182400 | 12480 |
| s40(id=31 S1->S2) | sw08-p2 | Q7 | 249920 | 12480 |
| s53(id=44 S1->S2) | S1-p0 | Q7 | 262400 | 12480 |
| s53(id=44 S1->S2) | sw02-p4 | Q7 | 270720 | 12480 |
| s53(id=44 S1->S2) | sw04-p5 | Q7 | 279040 | 12480 |
| s53(id=44 S1->S2) | sw06-p4 | Q7 | 287360 | 12480 |
| s53(id=44 S1->S2) | sw08-p2 | Q7 | 295680 | 12480 |
| s57(id=48 S2->S1) | S2-p0 | Q7 | 150080 | 12480 |
| s57(id=48 S2->S1) | sw08-p4 | Q7 | 156800 | 12480 |
| s57(id=48 S2->S1) | sw06-p5 | Q7 | 163520 | 12480 |
| s57(id=48 S2->S1) | sw04-p4 | Q7 | 170240 | 12480 |
| s57(id=48 S2->S1) | sw02-p2 | Q7 | 176960 | 12480 |
| s31(id=22 S2->S3) | S2-p0 | Q6 | 111040 | 12480 |
| s31(id=22 S2->S3) | sw08-p5 | Q6 | 117760 | 12480 |
| s31(id=22 S2->S3) | sw07-p4 | Q6 | 124480 | 12480 |
| s31(id=22 S2->S3) | sw05-p5 | Q6 | 131200 | 12480 |
| s31(id=22 S2->S3) | sw03-p4 | Q6 | 307520 | 12480 |
| s31(id=22 S2->S3) | sw01-p2 | Q6 | 400000 | 12480 |
| s32(id=23 S2->S3) | S2-p0 | Q7 | 212480 | 12480 |
| s32(id=23 S2->S3) | sw08-p5 | Q7 | 219200 | 12480 |
| s32(id=23 S2->S3) | sw07-p4 | Q7 | 232640 | 12480 |
| s32(id=23 S2->S3) | sw05-p5 | Q7 | 239360 | 12480 |
| s32(id=23 S2->S3) | sw03-p4 | Q7 | 246080 | 12480 |
| s32(id=23 S2->S3) | sw01-p2 | Q7 | 252800 | 12480 |
| s34(id=25 S2->S3) | S2-p0 | Q7 | 224960 | 12480 |
| s34(id=25 S2->S3) | sw08-p5 | Q7 | 231680 | 12480 |
| s34(id=25 S2->S3) | sw07-p4 | Q7 | 245120 | 12480 |
| s34(id=25 S2->S3) | sw05-p5 | Q7 | 251840 | 12480 |
| s34(id=25 S2->S3) | sw03-p4 | Q7 | 258560 | 12480 |
| s34(id=25 S2->S3) | sw01-p2 | Q7 | 265280 | 12480 |
| s36(id=27 S2->S3) | S2-p0 | Q7 | 262400 | 12480 |
| s36(id=27 S2->S3) | sw08-p5 | Q7 | 269120 | 12480 |
| s36(id=27 S2->S3) | sw07-p4 | Q7 | 275840 | 12480 |
| s36(id=27 S2->S3) | sw05-p5 | Q7 | 282560 | 12480 |
| s36(id=27 S2->S3) | sw03-p4 | Q7 | 289280 | 12480 |
| s36(id=27 S2->S3) | sw01-p2 | Q7 | 296000 | 12480 |
| s43(id=34 S2->S3) | S2-p0 | Q7 | 274880 | 12480 |
| s43(id=34 S2->S3) | sw08-p5 | Q7 | 282240 | 12480 |
| s43(id=34 S2->S3) | sw07-p4 | Q7 | 350080 | 12480 |
| s43(id=34 S2->S3) | sw05-p5 | Q7 | 356160 | 12480 |
| s43(id=34 S2->S3) | sw03-p4 | Q7 | 362240 | 12480 |
| s43(id=34 S2->S3) | sw01-p2 | Q7 | 372800 | 12480 |
| s46(id=37 S2->S1) | S2-p0 | Q7 | 162560 | 12480 |
| s46(id=37 S2->S1) | sw08-p4 | Q7 | 169280 | 12480 |
| s46(id=37 S2->S1) | sw06-p5 | Q7 | 176000 | 12480 |
| s46(id=37 S2->S1) | sw04-p4 | Q7 | 182720 | 12480 |
| s46(id=37 S2->S1) | sw02-p2 | Q7 | 189440 | 12480 |

## Constraint check

- C1-C7, C9: OK
- window-boundary integrity (no window's psi/delta changed anywhere): OK

## GCL per egress port

### sw01-p2  (28 entries, util 48.3600 %)

```
sgs 22720 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 1920 0x3F # 00111111   BE
sgs 25920 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 9280 0x3F # 00111111   BE
sgs 75200 0x40 # 01000000   Q6
sgs 27200 0xBF # 10111111   Q7
sgs 22720 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 137280 0x80 # 10000000   Q7
sgs 27200 0xBF # 10111111   Q7
sgs 22720 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 1920 0x3F # 00111111   BE
sgs 25920 0xBF # 10111111   Q7
sgs 96960 0x80 # 10000000   Q7
sgs 27200 0xBF # 10111111   Q7
sgs 22720 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 114560 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p4  (18 entries, util 6.2400 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p5  (16 entries, util 15.6000 %)

```
sgs 17600 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 15040 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 10880 0x3F # 00111111   BE
sgs 226240 0x80 # 10000000   Q7
sgs 5440 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 17600 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 15040 0x7F # 01111111   Q6
sgs 232000 0x40 # 01000000   Q6
sgs 23040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (18 entries, util 34.3200 %)

```
sgs 22720 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 14720 0x7F # 01111111   Q6
sgs 2880 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 268160 0x80 # 10000000   Q7
sgs 16320 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 22720 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 14720 0x7F # 01111111   Q6
sgs 2880 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 245440 0x80 # 10000000   Q7
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p4  (18 entries, util 29.6400 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 33280 0x7F # 01111111   Q6
sgs 75200 0x80 # 10000000   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 45760 0x7F # 01111111   Q6
sgs 75200 0x80 # 10000000   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 45760 0x7F # 01111111   Q6
sgs 75200 0x80 # 10000000   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 45760 0x7F # 01111111   Q6
sgs 29440 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p5  (24 entries, util 17.1600 %)

```
sgs 17600 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 19840 0x7F # 01111111   Q6
sgs 19200 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 10880 0x3F # 00111111   BE
sgs 36160 0x40 # 01000000   Q6
sgs 21440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 17600 0x7F # 01111111   Q6
sgs 111040 0x40 # 01000000   Q6
sgs 21440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 17600 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 19840 0x7F # 01111111   Q6
sgs 19200 0xBF # 10111111   Q7
sgs 59520 0x80 # 10000000   Q7
sgs 21440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 17600 0x7F # 01111111   Q6
sgs 93440 0x40 # 01000000   Q6
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (20 entries, util 31.2000 %)

```
sgs 30400 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 7040 0x3F # 00111111   BE
sgs 45760 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 41920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 30400 0x7F # 01111111   Q6
sgs 77120 0x80 # 10000000   Q7
sgs 42560 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 30400 0x7F # 01111111   Q6
sgs 77120 0x80 # 10000000   Q7
sgs 42560 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 30400 0x7F # 01111111   Q6
sgs 46720 0x80 # 10000000   Q7
sgs 23040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p5  (18 entries, util 6.2400 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p4  (14 entries, util 18.7200 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 10560 0x3F # 00111111   BE
sgs 206400 0x80 # 10000000   Q7
sgs 33280 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 10560 0x3F # 00111111   BE
sgs 145920 0x80 # 10000000   Q7
sgs 43520 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (22 entries, util 29.6400 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 4160 0x3F # 00111111   BE
sgs 75200 0x80 # 10000000   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 4160 0x3F # 00111111   BE
sgs 75200 0x80 # 10000000   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 4160 0x3F # 00111111   BE
sgs 75200 0x80 # 10000000   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 4160 0x3F # 00111111   BE
sgs 21120 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (18 entries, util 6.2400 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p5  (20 entries, util 31.2000 %)

```
sgs 25280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12160 0x3F # 00111111   BE
sgs 37440 0xBF # 10111111   Q7
sgs 15040 0x40 # 01000000   Q6
sgs 47680 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 25280 0x7F # 01111111   Q6
sgs 77120 0x80 # 10000000   Q7
sgs 47680 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 25280 0x7F # 01111111   Q6
sgs 77120 0x80 # 10000000   Q7
sgs 47680 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 25280 0x7F # 01111111   Q6
sgs 51840 0x80 # 10000000   Q7
sgs 23040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p4  (22 entries, util 29.6400 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 75200 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 75200 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 75200 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12800 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (14 entries, util 18.7200 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 5440 0x3F # 00111111   BE
sgs 206400 0x80 # 10000000   Q7
sgs 38400 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 5440 0x3F # 00111111   BE
sgs 151040 0x80 # 10000000   Q7
sgs 43520 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (23 entries, util 31.2000 %)

```
sgs 20160 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 17280 0x7F # 01111111   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 18240 0x40 # 01000000   Q6
sgs 2880 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 77120 0x80 # 10000000   Q7
sgs 2880 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 77120 0x80 # 10000000   Q7
sgs 2880 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 56960 0x80 # 10000000   Q7
sgs 23040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p5  (18 entries, util 6.2400 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p2  (22 entries, util 35.8800 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 20800 0xBF # 10111111   Q7
sgs 75200 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 20800 0xBF # 10111111   Q7
sgs 75200 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 20800 0xBF # 10111111   Q7
sgs 75200 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 20800 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 16960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p4  (13 entries, util 18.7200 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 30080 0x7F # 01111111   Q6
sgs 206400 0x80 # 10000000   Q7
sgs 960 0x3F # 00111111   BE
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 42560 0x7F # 01111111   Q6
sgs 163840 0x80 # 10000000   Q7
sgs 43520 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (23 entries, util 31.2000 %)

```
sgs 5120 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 32320 0x7F # 01111111   Q6
sgs 20800 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 16960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 5120 0x3F # 00111111   BE
sgs 77120 0x80 # 10000000   Q7
sgs 17920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 5120 0x3F # 00111111   BE
sgs 77120 0x80 # 10000000   Q7
sgs 17920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 5120 0x3F # 00111111   BE
sgs 72000 0x80 # 10000000   Q7
sgs 23040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

