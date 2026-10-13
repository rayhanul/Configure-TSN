# Reconfiguration-free admission (Problem 3)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Frozen schedule W loaded from: **result/result-2026-10-12-dataset-testbed-7-ring-avgwin/rl-c9-on/7-matrix-c9on**

## Admission: W (before) vs. after this run's arrivals

| | admitted | of total |
|---|---|---|
| W (base, unchanged) | 11 | 11 |
| + this run's arrivals | 20 | 39 |

Every arrival admitted here required **zero** window-boundary changes -- see the GCL-entry table below (unchanged from W by construction) and the window-boundary integrity check. No previously-admitted flow was rerouted.

## Arrivals

| id | src->dst | RS(s) size | admitted | route | queue | phi_s (ns) | e2e (ns) | rerouted to make room | reason if rejected |
|---|---|---|---|---|---|---|---|---|---|
| 10 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 6 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 2 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 | 62400 | 261760 | - | - |
| 11 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 249920 | 42880 | - | - |
| 17 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q7 | 37440 | 29120 | - | - |
| 14 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q6 | 12480 | 29120 | - | - |
| 16 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 12480 | 107840 | - | - |
| 4 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q6 | 12480 | 22720 | - | - |
| 13 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q6 | 87360 | 58560 | - | - |
| 40 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q7 | 150080 | 24640 | - | - |
| 26 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q6 | 112320 | 43200 | - | - |
| 27 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 262400 | 315520 | - | - |
| 28 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 557760 | 32960 | - | - |
| 29 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q6 | 462400 | 102400 | - | - |
| 37 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 39 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 570240 | 100480 | - | - |
| 41 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 22 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 37440 | 121280 | - | - |
| 24 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q7 | 162560 | 40960 | - | - |
| 38 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q7 | 251840 | 53760 | - | - |
| 46 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q7 | 350080 | 27840 | - | - |
| 47 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q7 | 362560 | 27840 | - | - |
| 50 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 95680 | 116800 | - | - |
| 33 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 34 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 30 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 32 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 35 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 36 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 274880 | 97920 | - | - |
| 42 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 48 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 49 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 23 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 25 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 45 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 21 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 31 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 43 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 44 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |

## Per-port GCL entries (should equal W exactly)

| port | W entries | after arrivals | GCL_size |
|---|---|---|---|
| sw01-p2 | 23 | 23 | 255 |
| sw01-p4 | 21 | 21 | 255 |
| sw01-p5 | 22 | 22 | 255 |
| sw02-p2 | 24 | 24 | 255 |
| sw02-p4 | 25 | 25 | 255 |
| sw02-p5 | 19 | 19 | 255 |
| sw03-p4 | 14 | 14 | 255 |
| sw03-p5 | 21 | 21 | 255 |
| sw04-p4 | 9 | 9 | 255 |
| sw04-p5 | 25 | 25 | 255 |
| sw05-p4 | 21 | 21 | 255 |
| sw05-p5 | 15 | 15 | 255 |
| sw06-p4 | 24 | 24 | 255 |
| sw06-p5 | 9 | 9 | 255 |
| sw07-p4 | 15 | 15 | 255 |
| sw07-p5 | 25 | 25 | 255 |
| sw08-p2 | 29 | 29 | 255 |
| sw08-p4 | 9 | 9 | 255 |
| sw08-p5 | 14 | 14 | 255 |

## Per-hop windows used by newly admitted flows

| flow | egress port | queue | psi (ns, unchanged) | delta (ns, unchanged) |
|---|---|---|---|---|
| s20(id=2 S3->S2) | S3-p0 | Q7 | 62400 | 12480 |
| s20(id=2 S3->S2) | sw01-p4 | Q7 | 80640 | 12480 |
| s20(id=2 S3->S2) | sw03-p5 | Q7 | 88320 | 12480 |
| s20(id=2 S3->S2) | sw05-p4 | Q7 | 96000 | 12480 |
| s20(id=2 S3->S2) | sw07-p5 | Q7 | 257920 | 12480 |
| s20(id=2 S3->S2) | sw08-p2 | Q7 | 311680 | 12480 |
| s24(id=11 S2->S3) | S2-p0 | Q7 | 249920 | 12480 |
| s24(id=11 S2->S3) | sw08-p5 | Q7 | 256000 | 12480 |
| s24(id=11 S2->S3) | sw07-p4 | Q7 | 262080 | 12480 |
| s24(id=11 S2->S3) | sw05-p5 | Q7 | 268160 | 12480 |
| s24(id=11 S2->S3) | sw03-p4 | Q7 | 274240 | 12480 |
| s24(id=11 S2->S3) | sw01-p2 | Q7 | 280320 | 12480 |
| s28(id=17 S1->S3) | S1-p0 | Q7 | 37440 | 12480 |
| s28(id=17 S1->S3) | sw02-p5 | Q7 | 45760 | 12480 |
| s28(id=17 S1->S3) | sw01-p2 | Q7 | 54080 | 12480 |
| s26(id=14 S3->S1) | S3-p0 | Q6 | 12480 | 12480 |
| s26(id=14 S3->S1) | sw01-p5 | Q6 | 20800 | 12480 |
| s26(id=14 S3->S1) | sw02-p2 | Q6 | 29120 | 12480 |
| s27(id=16 S2->S3) | S2-p0 | Q6 | 12480 | 12480 |
| s27(id=16 S2->S3) | sw08-p5 | Q6 | 20800 | 12480 |
| s27(id=16 S2->S3) | sw07-p4 | Q6 | 29120 | 12480 |
| s27(id=16 S2->S3) | sw05-p5 | Q6 | 37440 | 12480 |
| s27(id=16 S2->S3) | sw03-p4 | Q6 | 100160 | 12480 |
| s27(id=16 S2->S3) | sw01-p2 | Q6 | 107840 | 12480 |
| s21(id=4 S1->S3) | S1-p0 | Q6 | 12480 | 12480 |
| s21(id=4 S1->S3) | sw02-p5 | Q6 | 17600 | 12480 |
| s21(id=4 S1->S3) | sw01-p2 | Q6 | 22720 | 12480 |
| s25(id=13 S1->S3) | S1-p0 | Q6 | 87360 | 12480 |
| s25(id=13 S1->S3) | sw02-p5 | Q6 | 113920 | 12480 |
| s25(id=13 S1->S3) | sw01-p2 | Q6 | 133440 | 12480 |
| s48(id=40 S3->S1) | S3-p0 | Q7 | 150080 | 12480 |
| s48(id=40 S3->S1) | sw01-p5 | Q7 | 156160 | 12480 |
| s48(id=40 S3->S1) | sw02-p2 | Q7 | 162240 | 12480 |
| s34(id=26 S1->S2) | S1-p0 | Q6 | 112320 | 12480 |
| s34(id=26 S1->S2) | sw02-p4 | Q6 | 120000 | 12480 |
| s34(id=26 S1->S2) | sw04-p5 | Q6 | 127680 | 12480 |
| s34(id=26 S1->S2) | sw06-p4 | Q6 | 135360 | 12480 |
| s34(id=26 S1->S2) | sw08-p2 | Q6 | 143040 | 12480 |
| s35(id=27 S2->S1) | S2-p0 | Q7 | 262400 | 12480 |
| s35(id=27 S2->S1) | sw08-p4 | Q7 | 550080 | 12480 |
| s35(id=27 S2->S1) | sw06-p5 | Q7 | 555200 | 12480 |
| s35(id=27 S2->S1) | sw04-p4 | Q7 | 560320 | 12480 |
| s35(id=27 S2->S1) | sw02-p2 | Q7 | 565440 | 12480 |
| s36(id=28 S2->S1) | S2-p0 | Q7 | 557760 | 12480 |
| s36(id=28 S2->S1) | sw08-p4 | Q7 | 562880 | 12480 |
| s36(id=28 S2->S1) | sw06-p5 | Q7 | 568000 | 12480 |
| s36(id=28 S2->S1) | sw04-p4 | Q7 | 573120 | 12480 |
| s36(id=28 S2->S1) | sw02-p2 | Q7 | 578240 | 12480 |
| s37(id=29 S1->S2) | S1-p0 | Q6 | 462400 | 12480 |
| s37(id=29 S1->S2) | sw02-p4 | Q6 | 470720 | 12480 |
| s37(id=29 S1->S2) | sw04-p5 | Q6 | 479040 | 12480 |
| s37(id=29 S1->S2) | sw06-p4 | Q6 | 487360 | 12480 |
| s37(id=29 S1->S2) | sw08-p2 | Q6 | 552320 | 12480 |
| s47(id=39 S2->S1) | S2-p0 | Q7 | 570240 | 12480 |
| s47(id=39 S2->S1) | sw08-p4 | Q7 | 578560 | 12480 |
| s47(id=39 S2->S1) | sw06-p5 | Q7 | 586880 | 12480 |
| s47(id=39 S2->S1) | sw04-p4 | Q7 | 649920 | 12480 |
| s47(id=39 S2->S1) | sw02-p2 | Q7 | 658240 | 12480 |
| s30(id=22 S2->S3) | S2-p0 | Q6 | 37440 | 12480 |
| s30(id=22 S2->S3) | sw08-p5 | Q6 | 91200 | 12480 |
| s30(id=22 S2->S3) | sw07-p4 | Q6 | 100800 | 12480 |
| s30(id=22 S2->S3) | sw05-p5 | Q6 | 110400 | 12480 |
| s30(id=22 S2->S3) | sw03-p4 | Q6 | 141120 | 12480 |
| s30(id=22 S2->S3) | sw01-p2 | Q6 | 146240 | 12480 |
| s32(id=24 S3->S1) | S3-p0 | Q7 | 162560 | 12480 |
| s32(id=24 S3->S1) | sw01-p5 | Q7 | 168640 | 12480 |
| s32(id=24 S3->S1) | sw02-p2 | Q7 | 174720 | 12480 |
| s46(id=38 S1->S3) | S1-p0 | Q7 | 251840 | 12480 |
| s46(id=38 S1->S3) | sw02-p5 | Q7 | 258560 | 12480 |
| s46(id=38 S1->S3) | sw01-p2 | Q7 | 266560 | 12480 |
| s54(id=46 S3->S1) | S3-p0 | Q7 | 350080 | 12480 |
| s54(id=46 S3->S1) | sw01-p5 | Q7 | 357760 | 12480 |
| s54(id=46 S3->S1) | sw02-p2 | Q7 | 365440 | 12480 |
| s55(id=47 S3->S1) | S3-p0 | Q7 | 362560 | 12480 |
| s55(id=47 S3->S1) | sw01-p5 | Q7 | 370240 | 12480 |
| s55(id=47 S3->S1) | sw02-p2 | Q7 | 377920 | 12480 |
| s58(id=50 S2->S3) | S2-p0 | Q6 | 95680 | 12480 |
| s58(id=50 S2->S3) | sw08-p5 | Q6 | 104000 | 12480 |
| s58(id=50 S2->S3) | sw07-p4 | Q6 | 113280 | 12480 |
| s58(id=50 S2->S3) | sw05-p5 | Q6 | 142400 | 12480 |
| s58(id=50 S2->S3) | sw03-p4 | Q6 | 153600 | 12480 |
| s58(id=50 S2->S3) | sw01-p2 | Q6 | 200000 | 12480 |
| s44(id=36 S2->S3) | S2-p0 | Q7 | 274880 | 12480 |
| s44(id=36 S2->S3) | sw08-p5 | Q7 | 280000 | 12480 |
| s44(id=36 S2->S3) | sw07-p4 | Q7 | 285120 | 12480 |
| s44(id=36 S2->S3) | sw05-p5 | Q7 | 350080 | 12480 |
| s44(id=36 S2->S3) | sw03-p4 | Q7 | 355200 | 12480 |
| s44(id=36 S2->S3) | sw01-p2 | Q7 | 360320 | 12480 |

## Constraint check

- C1-C7, C9: OK
- window-boundary integrity (no window's psi/delta changed anywhere): OK

## GCL per egress port

### sw01-p2  (23 entries, util 26.5200 %)

```
sgs 41600 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 18560 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 15040 0xBF # 10111111   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 34560 0x40 # 01000000   Q6
sgs 32000 0xBF # 10111111   Q7
sgs 54080 0x7F # 01111111   Q6
sgs 101440 0x80 # 10000000   Q7
sgs 44480 0xBF # 10111111   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 46080 0xBF # 10111111   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 47360 0x80 # 10000000   Q7
sgs 32000 0xBF # 10111111   Q7
sgs 54080 0x7F # 01111111   Q6
sgs 59840 0x80 # 10000000   Q7
sgs 36160 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p4  (21 entries, util 9.3600 %)

```
sgs 30080 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 38080 0xBF # 10111111   Q7
sgs 66240 0x80 # 10000000   Q7
sgs 53120 0xBF # 10111111   Q7
sgs 30080 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 38080 0xBF # 10111111   Q7
sgs 66240 0x80 # 10000000   Q7
sgs 53120 0xBF # 10111111   Q7
sgs 30080 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 38080 0xBF # 10111111   Q7
sgs 66240 0x80 # 10000000   Q7
sgs 53120 0xBF # 10111111   Q7
sgs 30080 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 38080 0xBF # 10111111   Q7
sgs 36160 0x80 # 10000000   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p5  (22 entries, util 26.5200 %)

```
sgs 5120 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 40640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 10880 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 7360 0x3F # 00111111   BE
sgs 40320 0x80 # 10000000   Q7
sgs 63360 0xBF # 10111111   Q7
sgs 136640 0x80 # 10000000   Q7
sgs 63360 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 40640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 10880 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 7360 0x3F # 00111111   BE
sgs 40320 0x80 # 10000000   Q7
sgs 63360 0xBF # 10111111   Q7
sgs 131520 0x80 # 10000000   Q7
sgs 13440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (24 entries, util 32.7600 %)

```
sgs 10240 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 35520 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 4800 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 10880 0x3F # 00111111   BE
sgs 41280 0x80 # 10000000   Q7
sgs 57280 0xBF # 10111111   Q7
sgs 142720 0x80 # 10000000   Q7
sgs 57280 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 27200 0x7F # 01111111   Q6
sgs 21120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 4800 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 10880 0x3F # 00111111   BE
sgs 41280 0x80 # 10000000   Q7
sgs 57280 0xBF # 10111111   Q7
sgs 132480 0x80 # 10000000   Q7
sgs 57280 0xBF # 10111111   Q7
```

### sw02-p4  (25 entries, util 21.8400 %)

```
sgs 6080 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 11840 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 50240 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0x7F # 01111111   Q6
sgs 124480 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 99520 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0x7F # 01111111   Q6
sgs 118400 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p5  (19 entries, util 12.4800 %)

```
sgs 45760 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 9280 0x3F # 00111111   BE
sgs 45120 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 45760 0x7F # 01111111   Q6
sgs 66880 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 45760 0x7F # 01111111   Q6
sgs 66880 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 45760 0x7F # 01111111   Q6
sgs 21120 0x80 # 10000000   Q7
sgs 33280 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (14 entries, util 14.0400 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 54400 0xBF # 10111111   Q7
sgs 19840 0x7F # 01111111   Q6
sgs 119680 0x40 # 01000000   Q6
sgs 60480 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 173120 0x80 # 10000000   Q7
sgs 43520 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p5  (21 entries, util 9.3600 %)

```
sgs 35200 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 40640 0xBF # 10111111   Q7
sgs 63680 0x80 # 10000000   Q7
sgs 48000 0xBF # 10111111   Q7
sgs 35200 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 40640 0xBF # 10111111   Q7
sgs 63680 0x80 # 10000000   Q7
sgs 48000 0xBF # 10111111   Q7
sgs 35200 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 40640 0xBF # 10111111   Q7
sgs 63680 0x80 # 10000000   Q7
sgs 48000 0xBF # 10111111   Q7
sgs 35200 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 40640 0xBF # 10111111   Q7
sgs 28480 0x80 # 10000000   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p4  (9 entries, util 6.2400 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 487680 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (25 entries, util 21.8400 %)

```
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13760 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 50240 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 13760 0x7F # 01111111   Q6
sgs 123840 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 13760 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 98880 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 13760 0x7F # 01111111   Q6
sgs 111680 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (21 entries, util 9.3600 %)

```
sgs 40320 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 43200 0xBF # 10111111   Q7
sgs 61120 0x80 # 10000000   Q7
sgs 42880 0xBF # 10111111   Q7
sgs 40320 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 43200 0xBF # 10111111   Q7
sgs 61120 0x80 # 10000000   Q7
sgs 42880 0xBF # 10111111   Q7
sgs 40320 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 43200 0xBF # 10111111   Q7
sgs 61120 0x80 # 10000000   Q7
sgs 42880 0xBF # 10111111   Q7
sgs 40320 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 43200 0xBF # 10111111   Q7
sgs 20800 0x80 # 10000000   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p5  (15 entries, util 14.0400 %)

```
sgs 24960 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 60480 0xBF # 10111111   Q7
sgs 120960 0x40 # 01000000   Q6
sgs 18560 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 181440 0x80 # 10000000   Q7
sgs 43520 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p4  (24 entries, util 21.8400 %)

```
sgs 18240 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 16320 0x7F # 01111111   Q6
sgs 35520 0x40 # 01000000   Q6
sgs 10560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 50240 0x40 # 01000000   Q6
sgs 31680 0xBF # 10111111   Q7
sgs 18240 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 16320 0x7F # 01111111   Q6
sgs 121280 0x40 # 01000000   Q6
sgs 31680 0xBF # 10111111   Q7
sgs 18240 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 16320 0x7F # 01111111   Q6
sgs 121280 0x40 # 01000000   Q6
sgs 31680 0xBF # 10111111   Q7
sgs 18240 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 16320 0x7F # 01111111   Q6
sgs 103040 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (9 entries, util 6.2400 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 496000 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (15 entries, util 14.0400 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 50880 0xBF # 10111111   Q7
sgs 122240 0x40 # 01000000   Q6
sgs 26880 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 189760 0x80 # 10000000   Q7
sgs 43520 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p5  (25 entries, util 9.3600 %)

```
sgs 45440 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 45760 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 30080 0x7F # 01111111   Q6
sgs 31040 0x40 # 01000000   Q6
sgs 22720 0xBF # 10111111   Q7
sgs 45440 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 45760 0xBF # 10111111   Q7
sgs 73600 0x80 # 10000000   Q7
sgs 22720 0xBF # 10111111   Q7
sgs 45440 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 45760 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 30080 0x7F # 01111111   Q6
sgs 31040 0x40 # 01000000   Q6
sgs 22720 0xBF # 10111111   Q7
sgs 45440 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 45760 0xBF # 10111111   Q7
sgs 28160 0x80 # 10000000   Q7
sgs 18240 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p2  (29 entries, util 31.2000 %)

```
sgs 24320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13760 0x3F # 00111111   BE
sgs 38720 0x40 # 01000000   Q6
sgs 9920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 40640 0x40 # 01000000   Q6
sgs 59520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13760 0x3F # 00111111   BE
sgs 25280 0x40 # 01000000   Q6
sgs 35840 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 100160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13760 0x3F # 00111111   BE
sgs 38720 0x40 # 01000000   Q6
sgs 22400 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 28160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 59520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13760 0x3F # 00111111   BE
sgs 25280 0x40 # 01000000   Q6
sgs 35840 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 75840 0x3F # 00111111   BE
```

### sw08-p4  (9 entries, util 6.2400 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 504320 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (14 entries, util 14.0400 %)

```
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 41280 0xBF # 10111111   Q7
sgs 123520 0x40 # 01000000   Q6
sgs 35200 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 58240 0xBF # 10111111   Q7
sgs 198080 0x80 # 10000000   Q7
sgs 43520 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

