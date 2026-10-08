# Reconfiguration-free admission (Problem 3)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4000 ns
- Frozen schedule W loaded from: **result/result-2026-10-08-dataset-testbed-2/rl-c9-on/2-matrix-c9on**

## Admission: W (before) vs. after this run's arrivals

| | admitted | of total |
|---|---|---|
| W (base, unchanged) | 11 | 11 |
| + this run's arrivals | 21 | 39 |

Every arrival admitted here required **zero** window-boundary changes -- see the GCL-entry table below (unchanged from W by construction) and the window-boundary integrity check. No previously-admitted flow was rerouted.

## Arrivals

| id | src->dst | RS(s) size | admitted | route | queue | phi_s (ns) | e2e (ns) | rerouted to make room | reason if rejected |
|---|---|---|---|---|---|---|---|---|---|
| 3 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 17 | S3->S2 | - | yes | S3->sw01->sw03->sw06->sw08->S2 | Q7 | 12480 | 105920 | - | - |
| 19 | S2->S1 | - | yes | S2->sw08->sw07->sw05->sw02->S1 | Q7 | 12480 | 45760 | - | - |
| 5 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 15 | S2->S3 | - | yes | S2->sw08->sw06->sw03->sw01->S3 | Q6 | 37440 | 52160 | - | - |
| 13 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q7 | 157120 | 133760 | - | - |
| 2 | S3->S2 | - | yes | S3->sw01->sw03->sw06->sw08->S2 | Q6 | 87360 | 43520 | - | - |
| 6 | S2->S1 | - | yes | S2->sw08->sw07->sw05->sw02->S1 | Q7 | 62400 | 29120 | - | - |
| 8 | S1->S2 | - | yes | S1->sw02->sw05->sw07->sw08->S2 | Q6 | 37440 | 146240 | - | - |
| 50 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q7 | 150080 | 510080 | - | - |
| 21 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 22 | S2->S3 | - | yes | S2->sw08->sw06->sw03->sw01->S3 | Q6 | 462400 | 39680 | - | - |
| 24 | S3->S2 | - | yes | S3->sw01->sw03->sw06->sw08->S2 | Q6 | 462400 | 68480 | - | - |
| 28 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 35 | S3->S2 | - | yes | S3->sw01->sw03->sw06->sw08->S2 | Q7 | 225920 | 138560 | - | - |
| 37 | S2->S3 | - | yes | S2->sw08->sw06->sw03->sw01->S3 | Q7 | 87360 | 275200 | - | - |
| 40 | S2->S1 | - | yes | S2->sw08->sw07->sw05->sw02->S1 | Q6 | 474880 | 29120 | - | - |
| 41 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 43 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 23 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q6 | 12480 | 20800 | - | - |
| 29 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q6 | 62400 | 52160 | - | - |
| 26 | S2->S3 | - | yes | S2->sw08->sw06->sw03->sw01->S3 | Q7 | 282880 | 92160 | - | - |
| 33 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 36 | S2->S3 | - | yes | S2->sw08->sw06->sw03->sw01->S3 | Q7 | 295360 | 92160 | - | - |
| 45 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 46 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 47 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 48 | S2->S3 | - | yes | S2->sw08->sw06->sw03->sw01->S3 | Q7 | 357120 | 42880 | - | - |
| 49 | S2->S1 | - | yes | S2->sw08->sw07->sw05->sw02->S1 | Q7 | 230400 | 52800 | - | - |
| 30 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q6 | 94400 | 32640 | - | - |
| 34 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 42 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q6 | 106880 | 32640 | - | - |
| 25 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 27 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 31 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 32 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 38 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 39 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 44 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |

## Per-port GCL entries (should equal W exactly)

| port | W entries | after arrivals | GCL_size |
|---|---|---|---|
| sw01-p3 | 13 | 13 | 255 |
| sw01-p4 | 23 | 23 | 255 |
| sw01-p5 | 14 | 14 | 255 |
| sw02-p2 | 28 | 28 | 255 |
| sw02-p3 | 9 | 9 | 255 |
| sw02-p4 | 18 | 18 | 255 |
| sw02-p5 | 27 | 27 | 255 |
| sw03-p3 | 14 | 14 | 255 |
| sw03-p4 | 23 | 23 | 255 |
| sw03-p5 | 18 | 18 | 255 |
| sw04-p3 | 18 | 18 | 255 |
| sw04-p4 | 18 | 18 | 255 |
| sw04-p5 | 18 | 18 | 255 |
| sw05-p2 | 27 | 27 | 255 |
| sw05-p3 | 18 | 18 | 255 |
| sw05-p4 | 18 | 18 | 255 |
| sw05-p5 | 28 | 28 | 255 |
| sw06-p2 | 26 | 26 | 255 |
| sw06-p3 | 14 | 14 | 255 |
| sw06-p4 | 18 | 18 | 255 |
| sw06-p5 | 18 | 18 | 255 |
| sw07-p3 | 25 | 25 | 255 |
| sw07-p4 | 30 | 30 | 255 |
| sw07-p5 | 18 | 18 | 255 |
| sw08-p2 | 47 | 47 | 255 |
| sw08-p4 | 14 | 14 | 255 |
| sw08-p5 | 25 | 25 | 255 |

## Per-hop windows used by newly admitted flows

| flow | egress port | queue | psi (ns, unchanged) | delta (ns, unchanged) |
|---|---|---|---|---|
| s27(id=17 S3->S2) | S3-p0 | Q7 | 12480 | 12480 |
| s27(id=17 S3->S2) | sw01-p4 | Q7 | 21760 | 12480 |
| s27(id=17 S3->S2) | sw03-p4 | Q7 | 36160 | 12480 |
| s27(id=17 S3->S2) | sw06-p2 | Q7 | 40320 | 12480 |
| s27(id=17 S3->S2) | sw08-p2 | Q7 | 105920 | 12480 |
| s28(id=19 S2->S1) | S2-p0 | Q7 | 12480 | 12480 |
| s28(id=19 S2->S1) | sw08-p5 | Q7 | 21760 | 12480 |
| s28(id=19 S2->S1) | sw07-p3 | Q7 | 36160 | 12480 |
| s28(id=19 S2->S1) | sw05-p5 | Q7 | 40960 | 12480 |
| s28(id=19 S2->S1) | sw02-p2 | Q7 | 45760 | 12480 |
| s26(id=15 S2->S3) | S2-p0 | Q6 | 37440 | 12480 |
| s26(id=15 S2->S3) | sw08-p4 | Q6 | 64640 | 12480 |
| s26(id=15 S2->S3) | sw06-p3 | Q6 | 68800 | 12480 |
| s26(id=15 S2->S3) | sw03-p3 | Q6 | 72960 | 12480 |
| s26(id=15 S2->S3) | sw01-p3 | Q6 | 77120 | 12480 |
| s25(id=13 S3->S1) | S3-p0 | Q7 | 157120 | 12480 |
| s25(id=13 S3->S1) | sw01-p5 | Q7 | 274240 | 12480 |
| s25(id=13 S3->S1) | sw02-p2 | Q7 | 278400 | 12480 |
| s20(id=2 S3->S2) | S3-p0 | Q6 | 87360 | 12480 |
| s20(id=2 S3->S2) | sw01-p4 | Q6 | 91520 | 12480 |
| s20(id=2 S3->S2) | sw03-p4 | Q6 | 95680 | 12480 |
| s20(id=2 S3->S2) | sw06-p2 | Q6 | 99840 | 12480 |
| s20(id=2 S3->S2) | sw08-p2 | Q6 | 118400 | 12480 |
| s23(id=6 S2->S1) | S2-p0 | Q7 | 62400 | 12480 |
| s23(id=6 S2->S1) | sw08-p5 | Q7 | 66560 | 12480 |
| s23(id=6 S2->S1) | sw07-p3 | Q7 | 70720 | 12480 |
| s23(id=6 S2->S1) | sw05-p5 | Q7 | 74880 | 12480 |
| s23(id=6 S2->S1) | sw02-p2 | Q7 | 79040 | 12480 |
| s24(id=8 S1->S2) | S1-p0 | Q6 | 37440 | 12480 |
| s24(id=8 S1->S2) | sw02-p5 | Q6 | 90560 | 12480 |
| s24(id=8 S1->S2) | sw05-p2 | Q6 | 94720 | 12480 |
| s24(id=8 S1->S2) | sw07-p4 | Q6 | 127040 | 12480 |
| s24(id=8 S1->S2) | sw08-p2 | Q6 | 171200 | 12480 |
| s58(id=50 S1->S3) | S1-p0 | Q7 | 150080 | 12480 |
| s58(id=50 S1->S3) | sw02-p3 | Q7 | 550080 | 12480 |
| s58(id=50 S1->S3) | sw01-p3 | Q7 | 647680 | 12480 |
| s30(id=22 S2->S3) | S2-p0 | Q6 | 462400 | 12480 |
| s30(id=22 S2->S3) | sw08-p4 | Q6 | 477120 | 12480 |
| s30(id=22 S2->S3) | sw06-p3 | Q6 | 481280 | 12480 |
| s30(id=22 S2->S3) | sw03-p3 | Q6 | 485440 | 12480 |
| s30(id=22 S2->S3) | sw01-p3 | Q6 | 489600 | 12480 |
| s32(id=24 S3->S2) | S3-p0 | Q6 | 462400 | 12480 |
| s32(id=24 S3->S2) | sw01-p4 | Q6 | 466560 | 12480 |
| s32(id=24 S3->S2) | sw03-p4 | Q6 | 470720 | 12480 |
| s32(id=24 S3->S2) | sw06-p2 | Q6 | 474880 | 12480 |
| s32(id=24 S3->S2) | sw08-p2 | Q6 | 518400 | 12480 |
| s43(id=35 S3->S2) | S3-p0 | Q7 | 225920 | 12480 |
| s43(id=35 S3->S2) | sw01-p4 | Q7 | 234240 | 12480 |
| s43(id=35 S3->S2) | sw03-p4 | Q7 | 248640 | 12480 |
| s43(id=35 S3->S2) | sw06-p2 | Q7 | 314560 | 12480 |
| s43(id=35 S3->S2) | sw08-p2 | Q7 | 352000 | 12480 |
| s45(id=37 S2->S3) | S2-p0 | Q7 | 87360 | 12480 |
| s45(id=37 S2->S3) | sw08-p4 | Q7 | 274240 | 12480 |
| s45(id=37 S2->S3) | sw06-p3 | Q7 | 278400 | 12480 |
| s45(id=37 S2->S3) | sw03-p3 | Q7 | 282560 | 12480 |
| s45(id=37 S2->S3) | sw01-p3 | Q7 | 350080 | 12480 |
| s48(id=40 S2->S1) | S2-p0 | Q6 | 474880 | 12480 |
| s48(id=40 S2->S1) | sw08-p5 | Q6 | 479040 | 12480 |
| s48(id=40 S2->S1) | sw07-p3 | Q6 | 483200 | 12480 |
| s48(id=40 S2->S1) | sw05-p5 | Q6 | 487360 | 12480 |
| s48(id=40 S2->S1) | sw02-p2 | Q6 | 491520 | 12480 |
| s31(id=23 S1->S3) | S1-p0 | Q6 | 12480 | 12480 |
| s31(id=23 S1->S3) | sw02-p3 | Q6 | 16640 | 12480 |
| s31(id=23 S1->S3) | sw01-p3 | Q6 | 20800 | 12480 |
| s37(id=29 S1->S3) | S1-p0 | Q6 | 62400 | 12480 |
| s37(id=29 S1->S3) | sw02-p3 | Q6 | 85760 | 12480 |
| s37(id=29 S1->S3) | sw01-p3 | Q6 | 89920 | 12480 |
| s34(id=26 S2->S3) | S2-p0 | Q7 | 282880 | 12480 |
| s34(id=26 S2->S3) | sw08-p4 | Q7 | 287040 | 12480 |
| s34(id=26 S2->S3) | sw06-p3 | Q7 | 350080 | 12480 |
| s34(id=26 S2->S3) | sw03-p3 | Q7 | 354240 | 12480 |
| s34(id=26 S2->S3) | sw01-p3 | Q7 | 362560 | 12480 |
| s44(id=36 S2->S3) | S2-p0 | Q7 | 295360 | 12480 |
| s44(id=36 S2->S3) | sw08-p4 | Q7 | 350080 | 12480 |
| s44(id=36 S2->S3) | sw06-p3 | Q7 | 362560 | 12480 |
| s44(id=36 S2->S3) | sw03-p3 | Q7 | 366720 | 12480 |
| s44(id=36 S2->S3) | sw01-p3 | Q7 | 375040 | 12480 |
| s56(id=48 S2->S3) | S2-p0 | Q7 | 357120 | 12480 |
| s56(id=48 S2->S3) | sw08-p4 | Q7 | 362560 | 12480 |
| s56(id=48 S2->S3) | sw06-p3 | Q7 | 375040 | 12480 |
| s56(id=48 S2->S3) | sw03-p3 | Q7 | 379200 | 12480 |
| s56(id=48 S2->S3) | sw01-p3 | Q7 | 387520 | 12480 |
| s57(id=49 S2->S1) | S2-p0 | Q7 | 230400 | 12480 |
| s57(id=49 S2->S1) | sw08-p5 | Q7 | 234560 | 12480 |
| s57(id=49 S2->S1) | sw07-p3 | Q7 | 248640 | 12480 |
| s57(id=49 S2->S1) | sw05-p5 | Q7 | 253440 | 12480 |
| s57(id=49 S2->S1) | sw02-p2 | Q7 | 258240 | 12480 |
| s38(id=30 S1->S3) | S1-p0 | Q6 | 94400 | 12480 |
| s38(id=30 S1->S3) | sw02-p3 | Q6 | 98560 | 12480 |
| s38(id=30 S1->S3) | sw01-p3 | Q6 | 102720 | 12480 |
| s50(id=42 S1->S3) | S1-p0 | Q6 | 106880 | 12480 |
| s50(id=42 S1->S3) | sw02-p3 | Q6 | 111040 | 12480 |
| s50(id=42 S1->S3) | sw01-p3 | Q6 | 115200 | 12480 |

## Constraint check

- C1-C7, C9: OK
- window-boundary integrity (no window's psi/delta changed anywhere): OK

## GCL per egress port

### sw01-p3  (13 entries, util 40.5600 %)

```
sgs 41600 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 231040 0x40 # 01000000   Q6
sgs 60800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 23040 0xBF # 10111111   Q7
sgs 170560 0x40 # 01000000   Q6
sgs 52480 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p4  (23 entries, util 21.8400 %)

```
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 5120 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 19840 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 65920 0x40 # 01000000   Q6
sgs 59200 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 5120 0x3F # 00111111   BE
sgs 123200 0x80 # 10000000   Q7
sgs 59200 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 5120 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 19840 0x7F # 01111111   Q6
sgs 90880 0x40 # 01000000   Q6
sgs 59200 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 5120 0x3F # 00111111   BE
sgs 119040 0x80 # 10000000   Q7
sgs 59200 0xBF # 10111111   Q7
```

### sw01-p5  (14 entries, util 6.2400 %)

```
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 30720 0xBF # 10111111   Q7
sgs 201920 0x40 # 01000000   Q6
sgs 25920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 30720 0xBF # 10111111   Q7
sgs 172800 0x40 # 01000000   Q6
sgs 55040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (28 entries, util 29.6400 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 20800 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 3200 0x3F # 00111111   BE
sgs 56640 0x40 # 01000000   Q6
sgs 36160 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 16640 0x7F # 01111111   Q6
sgs 118080 0x80 # 10000000   Q7
sgs 36160 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 20800 0xBF # 10111111   Q7
sgs 97280 0x40 # 01000000   Q6
sgs 36160 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 16640 0x7F # 01111111   Q6
sgs 101440 0x80 # 10000000   Q7
sgs 52800 0xBF # 10111111   Q7
```

### sw02-p3  (9 entries, util 21.8400 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 483520 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p4  (18 entries, util 0.0000 %)

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

### sw02-p5  (27 entries, util 14.0400 %)

```
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 36480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 22080 0x7F # 01111111   Q6
sgs 41600 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 36480 0xBF # 10111111   Q7
sgs 76160 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 36480 0xBF # 10111111   Q7
sgs 76160 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 36480 0xBF # 10111111   Q7
sgs 72000 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p3  (14 entries, util 18.7200 %)

```
sgs 37440 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 23040 0xBF # 10111111   Q7
sgs 209600 0x40 # 01000000   Q6
sgs 17600 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 23040 0xBF # 10111111   Q7
sgs 172160 0x40 # 01000000   Q6
sgs 55040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (23 entries, util 21.8400 %)

```
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 15360 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 9600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 65920 0x40 # 01000000   Q6
sgs 59200 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 15360 0x7F # 01111111   Q6
sgs 112960 0x80 # 10000000   Q7
sgs 59200 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 15360 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 9600 0x3F # 00111111   BE
sgs 90880 0x40 # 01000000   Q6
sgs 59200 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 15360 0x7F # 01111111   Q6
sgs 104640 0x80 # 10000000   Q7
sgs 59200 0xBF # 10111111   Q7
```

### sw03-p5  (18 entries, util 0.0000 %)

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

### sw04-p3  (18 entries, util 0.0000 %)

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

### sw04-p4  (18 entries, util 0.0000 %)

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

### sw04-p5  (18 entries, util 0.0000 %)

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

### sw05-p2  (27 entries, util 14.0400 %)

```
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 60480 0x40 # 01000000   Q6
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 6720 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 32960 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 60480 0x40 # 01000000   Q6
sgs 49920 0x7F # 01111111   Q6
sgs 14720 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 60480 0x40 # 01000000   Q6
sgs 49920 0x7F # 01111111   Q6
sgs 14720 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 60480 0x40 # 01000000   Q6
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 43840 0xBF # 10111111   Q7
```

### sw05-p3  (18 entries, util 0.0000 %)

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

### sw05-p4  (18 entries, util 0.0000 %)

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

### sw05-p5  (28 entries, util 23.4000 %)

```
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 16000 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 8960 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 21120 0x7F # 01111111   Q6
sgs 36800 0x40 # 01000000   Q6
sgs 42240 0xBF # 10111111   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 16000 0x7F # 01111111   Q6
sgs 116800 0x80 # 10000000   Q7
sgs 42240 0xBF # 10111111   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 16000 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 8960 0x3F # 00111111   BE
sgs 95360 0x40 # 01000000   Q6
sgs 42240 0xBF # 10111111   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 16000 0x7F # 01111111   Q6
sgs 104320 0x80 # 10000000   Q7
sgs 54720 0xBF # 10111111   Q7
```

### sw06-p2  (26 entries, util 21.8400 %)

```
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 15360 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 9600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 65920 0x40 # 01000000   Q6
sgs 46720 0xBF # 10111111   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 15360 0x7F # 01111111   Q6
sgs 112960 0x80 # 10000000   Q7
sgs 46720 0xBF # 10111111   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 15360 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 9600 0x3F # 00111111   BE
sgs 90880 0x40 # 01000000   Q6
sgs 46720 0xBF # 10111111   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 15360 0x7F # 01111111   Q6
sgs 100480 0x80 # 10000000   Q7
sgs 59200 0xBF # 10111111   Q7
```

### sw06-p3  (14 entries, util 18.7200 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 23040 0xBF # 10111111   Q7
sgs 209600 0x40 # 01000000   Q6
sgs 21760 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 23040 0xBF # 10111111   Q7
sgs 176320 0x40 # 01000000   Q6
sgs 55040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p4  (18 entries, util 0.0000 %)

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

### sw06-p5  (18 entries, util 0.0000 %)

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

### sw07-p3  (25 entries, util 23.4000 %)

```
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 15360 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 9600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 21120 0x7F # 01111111   Q6
sgs 36800 0x40 # 01000000   Q6
sgs 54720 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 15360 0x7F # 01111111   Q6
sgs 117440 0x80 # 10000000   Q7
sgs 54720 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 15360 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 9600 0x3F # 00111111   BE
sgs 95360 0x40 # 01000000   Q6
sgs 54720 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 15360 0x7F # 01111111   Q6
sgs 109120 0x80 # 10000000   Q7
sgs 54720 0xBF # 10111111   Q7
```

### sw07-p4  (30 entries, util 14.0400 %)

```
sgs 12800 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12160 0x3F # 00111111   BE
sgs 60480 0x40 # 01000000   Q6
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 6720 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 20480 0xBF # 10111111   Q7
sgs 12800 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12160 0x3F # 00111111   BE
sgs 60480 0x40 # 01000000   Q6
sgs 49920 0x7F # 01111111   Q6
sgs 15040 0x80 # 10000000   Q7
sgs 37120 0xBF # 10111111   Q7
sgs 12800 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12160 0x3F # 00111111   BE
sgs 60480 0x40 # 01000000   Q6
sgs 49920 0x7F # 01111111   Q6
sgs 15040 0x80 # 10000000   Q7
sgs 37120 0xBF # 10111111   Q7
sgs 12800 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12160 0x3F # 00111111   BE
sgs 60480 0x40 # 01000000   Q6
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 39680 0xBF # 10111111   Q7
```

### sw07-p5  (18 entries, util 0.0000 %)

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

### sw08-p2  (47 entries, util 35.8800 %)

```
sgs 16640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 36800 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 1920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 21120 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 6720 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 32960 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 51200 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 33600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 52160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 36800 0x40 # 01000000   Q6
sgs 26880 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 21120 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 52160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 51200 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 33600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 35520 0x3F # 00111111   BE
```

### sw08-p4  (14 entries, util 18.7200 %)

```
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 23040 0xBF # 10111111   Q7
sgs 209600 0x40 # 01000000   Q6
sgs 25920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 23040 0xBF # 10111111   Q7
sgs 180480 0x40 # 01000000   Q6
sgs 55040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (25 entries, util 23.4000 %)

```
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 5120 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 19840 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 21120 0x7F # 01111111   Q6
sgs 36800 0x40 # 01000000   Q6
sgs 54720 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 5120 0x3F # 00111111   BE
sgs 127680 0x80 # 10000000   Q7
sgs 54720 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 5120 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 19840 0x7F # 01111111   Q6
sgs 95360 0x40 # 01000000   Q6
sgs 54720 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 5120 0x3F # 00111111   BE
sgs 123520 0x80 # 10000000   Q7
sgs 54720 0xBF # 10111111   Q7
```

