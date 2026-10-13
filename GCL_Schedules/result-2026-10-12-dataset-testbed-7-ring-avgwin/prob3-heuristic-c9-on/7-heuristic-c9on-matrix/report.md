# Reconfiguration-free admission (Problem 3)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Frozen schedule W loaded from: **result/result-2026-10-12-dataset-testbed-7-ring-avgwin/heuristic-c9-on/7-matrix-c9on**

## Admission: W (before) vs. after this run's arrivals

| | admitted | of total |
|---|---|---|
| W (base, unchanged) | 11 | 11 |
| + this run's arrivals | 18 | 39 |

Every arrival admitted here required **zero** window-boundary changes -- see the GCL-entry table below (unchanged from W by construction) and the window-boundary integrity check. No previously-admitted flow was rerouted.

## Arrivals

| id | src->dst | RS(s) size | admitted | route | queue | phi_s (ns) | e2e (ns) | rerouted to make room | reason if rejected |
|---|---|---|---|---|---|---|---|---|---|
| 10 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 6 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 2 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 11 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 249920 | 42880 | - | - |
| 17 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 14 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q6 | 12480 | 29120 | - | - |
| 16 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 12480 | 307840 | - | - |
| 4 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q7 | 62400 | 22720 | - | - |
| 13 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q7 | 87360 | 81920 | - | - |
| 40 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q7 | 62400 | 106240 | - | - |
| 26 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q6 | 112320 | 43200 | - | - |
| 27 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 37440 | 76160 | - | - |
| 28 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 49920 | 76480 | - | - |
| 29 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 37 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 39 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 62400 | 451200 | - | - |
| 41 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 22 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 262400 | 100160 | - | - |
| 24 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q7 | 150080 | 31040 | - | - |
| 38 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q7 | 150080 | 31680 | - | - |
| 46 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q7 | 162560 | 32640 | - | - |
| 47 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q7 | 350080 | 25920 | - | - |
| 50 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 209600 | 123840 | - | - |
| 33 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 34 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 30 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 32 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q7 | 162560 | 32640 | - | - |
| 35 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 36 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 274880 | 100160 | - | - |
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
| sw01-p2 | 13 | 13 | 255 |
| sw01-p4 | 18 | 18 | 255 |
| sw01-p5 | 26 | 26 | 255 |
| sw02-p2 | 28 | 28 | 255 |
| sw02-p4 | 28 | 28 | 255 |
| sw02-p5 | 18 | 18 | 255 |
| sw03-p4 | 13 | 13 | 255 |
| sw03-p5 | 18 | 18 | 255 |
| sw04-p4 | 9 | 9 | 255 |
| sw04-p5 | 28 | 28 | 255 |
| sw05-p4 | 18 | 18 | 255 |
| sw05-p5 | 13 | 13 | 255 |
| sw06-p4 | 24 | 24 | 255 |
| sw06-p5 | 9 | 9 | 255 |
| sw07-p4 | 13 | 13 | 255 |
| sw07-p5 | 18 | 18 | 255 |
| sw08-p2 | 21 | 21 | 255 |
| sw08-p4 | 9 | 9 | 255 |
| sw08-p5 | 15 | 15 | 255 |

## Per-hop windows used by newly admitted flows

| flow | egress port | queue | psi (ns, unchanged) | delta (ns, unchanged) |
|---|---|---|---|---|
| s24(id=11 S2->S3) | S2-p0 | Q7 | 249920 | 12480 |
| s24(id=11 S2->S3) | sw08-p5 | Q7 | 256000 | 12480 |
| s24(id=11 S2->S3) | sw07-p4 | Q7 | 262080 | 12480 |
| s24(id=11 S2->S3) | sw05-p5 | Q7 | 268160 | 12480 |
| s24(id=11 S2->S3) | sw03-p4 | Q7 | 274240 | 12480 |
| s24(id=11 S2->S3) | sw01-p2 | Q7 | 280320 | 12480 |
| s26(id=14 S3->S1) | S3-p0 | Q6 | 12480 | 12480 |
| s26(id=14 S3->S1) | sw01-p5 | Q6 | 20800 | 12480 |
| s26(id=14 S3->S1) | sw02-p2 | Q6 | 29120 | 12480 |
| s27(id=16 S2->S3) | S2-p0 | Q6 | 12480 | 12480 |
| s27(id=16 S2->S3) | sw08-p5 | Q6 | 200000 | 12480 |
| s27(id=16 S2->S3) | sw07-p4 | Q6 | 223040 | 12480 |
| s27(id=16 S2->S3) | sw05-p5 | Q6 | 231360 | 12480 |
| s27(id=16 S2->S3) | sw03-p4 | Q6 | 300160 | 12480 |
| s27(id=16 S2->S3) | sw01-p2 | Q6 | 307840 | 12480 |
| s21(id=4 S1->S3) | S1-p0 | Q7 | 62400 | 12480 |
| s21(id=4 S1->S3) | sw02-p5 | Q7 | 67520 | 12480 |
| s21(id=4 S1->S3) | sw01-p2 | Q7 | 72640 | 12480 |
| s25(id=13 S1->S3) | S1-p0 | Q7 | 87360 | 12480 |
| s25(id=13 S1->S3) | sw02-p5 | Q7 | 150080 | 12480 |
| s25(id=13 S1->S3) | sw01-p2 | Q7 | 156800 | 12480 |
| s48(id=40 S3->S1) | S3-p0 | Q7 | 62400 | 12480 |
| s48(id=40 S3->S1) | sw01-p5 | Q7 | 150080 | 12480 |
| s48(id=40 S3->S1) | sw02-p2 | Q7 | 156160 | 12480 |
| s34(id=26 S1->S2) | S1-p0 | Q6 | 112320 | 12480 |
| s34(id=26 S1->S2) | sw02-p4 | Q6 | 120000 | 12480 |
| s34(id=26 S1->S2) | sw04-p5 | Q6 | 127680 | 12480 |
| s34(id=26 S1->S2) | sw06-p4 | Q6 | 135360 | 12480 |
| s34(id=26 S1->S2) | sw08-p2 | Q6 | 143040 | 12480 |
| s35(id=27 S2->S1) | S2-p0 | Q6 | 37440 | 12480 |
| s35(id=27 S2->S1) | sw08-p4 | Q6 | 45760 | 12480 |
| s35(id=27 S2->S1) | sw06-p5 | Q6 | 54080 | 12480 |
| s35(id=27 S2->S1) | sw04-p4 | Q6 | 96000 | 12480 |
| s35(id=27 S2->S1) | sw02-p2 | Q6 | 101120 | 12480 |
| s36(id=28 S2->S1) | S2-p0 | Q6 | 49920 | 12480 |
| s36(id=28 S2->S1) | sw08-p4 | Q6 | 58240 | 12480 |
| s36(id=28 S2->S1) | sw06-p5 | Q6 | 103680 | 12480 |
| s36(id=28 S2->S1) | sw04-p4 | Q6 | 108800 | 12480 |
| s36(id=28 S2->S1) | sw02-p2 | Q6 | 113920 | 12480 |
| s47(id=39 S2->S1) | S2-p0 | Q6 | 62400 | 12480 |
| s47(id=39 S2->S1) | sw08-p4 | Q6 | 101760 | 12480 |
| s47(id=39 S2->S1) | sw06-p5 | Q6 | 116160 | 12480 |
| s47(id=39 S2->S1) | sw04-p4 | Q6 | 492800 | 12480 |
| s47(id=39 S2->S1) | sw02-p2 | Q6 | 501120 | 12480 |
| s30(id=22 S2->S3) | S2-p0 | Q7 | 262400 | 12480 |
| s30(id=22 S2->S3) | sw08-p5 | Q7 | 268480 | 12480 |
| s30(id=22 S2->S3) | sw07-p4 | Q7 | 274560 | 12480 |
| s30(id=22 S2->S3) | sw05-p5 | Q7 | 280640 | 12480 |
| s30(id=22 S2->S3) | sw03-p4 | Q7 | 286720 | 12480 |
| s30(id=22 S2->S3) | sw01-p2 | Q7 | 350080 | 12480 |
| s32(id=24 S3->S1) | S3-p0 | Q7 | 150080 | 12480 |
| s32(id=24 S3->S1) | sw01-p5 | Q7 | 162560 | 12480 |
| s32(id=24 S3->S1) | sw02-p2 | Q7 | 168640 | 12480 |
| s46(id=38 S1->S3) | S1-p0 | Q7 | 150080 | 12480 |
| s46(id=38 S1->S3) | sw02-p5 | Q7 | 162560 | 12480 |
| s46(id=38 S1->S3) | sw01-p2 | Q7 | 169280 | 12480 |
| s54(id=46 S3->S1) | S3-p0 | Q7 | 162560 | 12480 |
| s54(id=46 S3->S1) | sw01-p5 | Q7 | 175040 | 12480 |
| s54(id=46 S3->S1) | sw02-p2 | Q7 | 182720 | 12480 |
| s55(id=47 S3->S1) | S3-p0 | Q7 | 350080 | 12480 |
| s55(id=47 S3->S1) | sw01-p5 | Q7 | 356800 | 12480 |
| s55(id=47 S3->S1) | sw02-p2 | Q7 | 363520 | 12480 |
| s58(id=50 S2->S3) | S2-p0 | Q6 | 209600 | 12480 |
| s58(id=50 S2->S3) | sw08-p5 | Q6 | 227520 | 12480 |
| s58(id=50 S2->S3) | sw07-p4 | Q6 | 235840 | 12480 |
| s58(id=50 S2->S3) | sw05-p5 | Q6 | 300160 | 12480 |
| s58(id=50 S2->S3) | sw03-p4 | Q6 | 312640 | 12480 |
| s58(id=50 S2->S3) | sw01-p2 | Q6 | 320960 | 12480 |
| s40(id=32 S1->S3) | S1-p0 | Q7 | 162560 | 12480 |
| s40(id=32 S1->S3) | sw02-p5 | Q7 | 175040 | 12480 |
| s40(id=32 S1->S3) | sw01-p2 | Q7 | 182720 | 12480 |
| s44(id=36 S2->S3) | S2-p0 | Q7 | 274880 | 12480 |
| s44(id=36 S2->S3) | sw08-p5 | Q7 | 280960 | 12480 |
| s44(id=36 S2->S3) | sw07-p4 | Q7 | 287040 | 12480 |
| s44(id=36 S2->S3) | sw05-p5 | Q7 | 350080 | 12480 |
| s44(id=36 S2->S3) | sw03-p4 | Q7 | 355200 | 12480 |
| s44(id=36 S2->S3) | sw01-p2 | Q7 | 362560 | 12480 |

## Constraint check

- C1-C7, C9: OK
- window-boundary integrity (no window's psi/delta changed anywhere): OK

## GCL per egress port

### sw01-p2  (13 entries, util 26.5200 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 29120 0x7F # 01111111   Q6
sgs 206400 0x80 # 10000000   Q7
sgs 1920 0x3F # 00111111   BE
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 164800 0x80 # 10000000   Q7
sgs 43520 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p4  (18 entries, util 6.2400 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 17600 0x7F # 01111111   Q6
sgs 75200 0x40 # 01000000   Q6
sgs 44800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 30080 0x7F # 01111111   Q6
sgs 75200 0x40 # 01000000   Q6
sgs 44800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 30080 0x7F # 01111111   Q6
sgs 75200 0x40 # 01000000   Q6
sgs 44800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 30080 0x7F # 01111111   Q6
sgs 45120 0x40 # 01000000   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p5  (26 entries, util 26.5200 %)

```
sgs 5120 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 32320 0x7F # 01111111   Q6
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 10880 0x3F # 00111111   BE
sgs 45760 0x40 # 01000000   Q6
sgs 22720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 5120 0x3F # 00111111   BE
sgs 122240 0x80 # 10000000   Q7
sgs 22720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 5120 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 32320 0x7F # 01111111   Q6
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 10880 0x3F # 00111111   BE
sgs 45760 0x40 # 01000000   Q6
sgs 22720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 5120 0x3F # 00111111   BE
sgs 117120 0x80 # 10000000   Q7
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (28 entries, util 32.7600 %)

```
sgs 10240 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 27200 0x7F # 01111111   Q6
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 4800 0x3F # 00111111   BE
sgs 53440 0x40 # 01000000   Q6
sgs 8320 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 10240 0x3F # 00111111   BE
sgs 131520 0x80 # 10000000   Q7
sgs 8320 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 10240 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 27200 0x7F # 01111111   Q6
sgs 21120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 4800 0x3F # 00111111   BE
sgs 53440 0x40 # 01000000   Q6
sgs 8320 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 10240 0x3F # 00111111   BE
sgs 121280 0x80 # 10000000   Q7
sgs 18560 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p4  (28 entries, util 20.2800 %)

```
sgs 6080 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 11840 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 50240 0x40 # 01000000   Q6
sgs 43840 0xBF # 10111111   Q7
sgs 6080 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0x7F # 01111111   Q6
sgs 124480 0x40 # 01000000   Q6
sgs 43840 0xBF # 10111111   Q7
sgs 6080 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 99520 0x40 # 01000000   Q6
sgs 43840 0xBF # 10111111   Q7
sgs 6080 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0x7F # 01111111   Q6
sgs 118400 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p5  (18 entries, util 12.4800 %)

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

### sw03-p4  (13 entries, util 14.0400 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 206400 0x80 # 10000000   Q7
sgs 10240 0x3F # 00111111   BE
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 173120 0x80 # 10000000   Q7
sgs 43520 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p5  (18 entries, util 6.2400 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 22720 0x7F # 01111111   Q6
sgs 75200 0x40 # 01000000   Q6
sgs 39680 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 35200 0x7F # 01111111   Q6
sgs 75200 0x40 # 01000000   Q6
sgs 39680 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 35200 0x7F # 01111111   Q6
sgs 75200 0x40 # 01000000   Q6
sgs 39680 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 35200 0x7F # 01111111   Q6
sgs 40000 0x40 # 01000000   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
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

### sw04-p5  (28 entries, util 20.2800 %)

```
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13760 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 50240 0x40 # 01000000   Q6
sgs 37760 0xBF # 10111111   Q7
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13760 0x7F # 01111111   Q6
sgs 123840 0x40 # 01000000   Q6
sgs 37760 0xBF # 10111111   Q7
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13760 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 98880 0x40 # 01000000   Q6
sgs 37760 0xBF # 10111111   Q7
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13760 0x7F # 01111111   Q6
sgs 111680 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (18 entries, util 6.2400 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 27840 0x7F # 01111111   Q6
sgs 75200 0x40 # 01000000   Q6
sgs 34560 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 40320 0x7F # 01111111   Q6
sgs 75200 0x40 # 01000000   Q6
sgs 34560 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 40320 0x7F # 01111111   Q6
sgs 75200 0x40 # 01000000   Q6
sgs 34560 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 40320 0x7F # 01111111   Q6
sgs 34880 0x40 # 01000000   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p5  (13 entries, util 14.0400 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 206400 0x80 # 10000000   Q7
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

### sw06-p4  (24 entries, util 20.2800 %)

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

### sw07-p4  (13 entries, util 14.0400 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 206400 0x80 # 10000000   Q7
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

### sw07-p5  (18 entries, util 6.2400 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 32960 0x7F # 01111111   Q6
sgs 75200 0x40 # 01000000   Q6
sgs 29440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 45440 0x7F # 01111111   Q6
sgs 75200 0x40 # 01000000   Q6
sgs 29440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 45440 0x7F # 01111111   Q6
sgs 75200 0x40 # 01000000   Q6
sgs 29440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 45440 0x7F # 01111111   Q6
sgs 29760 0x40 # 01000000   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p2  (21 entries, util 26.5200 %)

```
sgs 24320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13760 0x3F # 00111111   BE
sgs 38720 0x40 # 01000000   Q6
sgs 9920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 38400 0x40 # 01000000   Q6
sgs 61760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13760 0x3F # 00111111   BE
sgs 29760 0x40 # 01000000   Q6
sgs 144000 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13760 0x3F # 00111111   BE
sgs 43200 0x40 # 01000000   Q6
sgs 130560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13760 0x3F # 00111111   BE
sgs 29760 0x40 # 01000000   Q6
sgs 119680 0x3F # 00111111   BE
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

### sw08-p5  (15 entries, util 14.0400 %)

```
sgs 8320 0x3F # 00111111   BE
sgs 141760 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 8320 0x3F # 00111111   BE
sgs 133440 0x80 # 10000000   Q7
sgs 8320 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

