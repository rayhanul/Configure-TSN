# Reconfiguration-free admission (Problem 3)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Frozen schedule W loaded from: **result/result-2026-10-12-dataset-testbed-7-ring-avgwin/heuristic-c9-off/7-matrix-c9off**

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
| 11 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 37440 | 95680 | - | - |
| 17 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q7 | 62400 | 100160 | - | - |
| 14 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q7 | 62400 | 116800 | - | - |
| 16 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 12480 | 400000 | - | - |
| 4 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q6 | 12480 | 300160 | - | - |
| 13 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q6 | 37440 | 291840 | - | - |
| 40 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q7 | 150080 | 45760 | - | - |
| 26 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 27 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 209600 | 534400 | - | - |
| 28 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 49920 | 208640 | - | - |
| 29 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 37 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 39 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 62720 | 208640 | - | - |
| 41 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 22 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 222080 | 207040 | - | - |
| 24 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q7 | 350080 | 45760 | - | - |
| 38 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q7 | 87360 | 91840 | - | - |
| 46 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q6 | 88320 | 45760 | - | - |
| 47 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q6 | 101120 | 45760 | - | - |
| 50 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 300160 | 145600 | - | - |
| 33 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 34 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 30 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 32 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q7 | 150080 | 45760 | - | - |
| 35 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 36 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 75200 | 187200 | - | - |
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
| sw01-p2 | 14 | 14 | 255 |
| sw01-p4 | 18 | 18 | 255 |
| sw01-p5 | 26 | 26 | 255 |
| sw02-p2 | 25 | 25 | 255 |
| sw02-p4 | 28 | 28 | 255 |
| sw02-p5 | 18 | 18 | 255 |
| sw03-p4 | 14 | 14 | 255 |
| sw03-p5 | 22 | 22 | 255 |
| sw04-p4 | 10 | 10 | 255 |
| sw04-p5 | 28 | 28 | 255 |
| sw05-p4 | 19 | 19 | 255 |
| sw05-p5 | 12 | 12 | 255 |
| sw06-p4 | 25 | 25 | 255 |
| sw06-p5 | 10 | 10 | 255 |
| sw07-p4 | 13 | 13 | 255 |
| sw07-p5 | 18 | 18 | 255 |
| sw08-p2 | 31 | 31 | 255 |
| sw08-p4 | 9 | 9 | 255 |
| sw08-p5 | 13 | 13 | 255 |

## Per-hop windows used by newly admitted flows

| flow | egress port | queue | psi (ns, unchanged) | delta (ns, unchanged) |
|---|---|---|---|---|
| s24(id=11 S2->S3) | S2-p0 | Q7 | 37440 | 12480 |
| s24(id=11 S2->S3) | sw08-p5 | Q7 | 54080 | 12480 |
| s24(id=11 S2->S3) | sw07-p4 | Q7 | 70720 | 12480 |
| s24(id=11 S2->S3) | sw05-p5 | Q7 | 87360 | 12480 |
| s24(id=11 S2->S3) | sw03-p4 | Q7 | 104000 | 12480 |
| s24(id=11 S2->S3) | sw01-p2 | Q7 | 120640 | 12480 |
| s28(id=17 S1->S3) | S1-p0 | Q7 | 62400 | 12480 |
| s28(id=17 S1->S3) | sw02-p5 | Q7 | 79360 | 12480 |
| s28(id=17 S1->S3) | sw01-p2 | Q7 | 96000 | 12480 |
| s26(id=14 S3->S1) | S3-p0 | Q7 | 62400 | 12480 |
| s26(id=14 S3->S1) | sw01-p5 | Q7 | 150080 | 12480 |
| s26(id=14 S3->S1) | sw02-p2 | Q7 | 166720 | 12480 |
| s27(id=16 S2->S3) | S2-p0 | Q6 | 12480 | 12480 |
| s27(id=16 S2->S3) | sw08-p5 | Q6 | 223040 | 12480 |
| s27(id=16 S2->S3) | sw07-p4 | Q6 | 300160 | 12480 |
| s27(id=16 S2->S3) | sw05-p5 | Q6 | 316800 | 12480 |
| s27(id=16 S2->S3) | sw03-p4 | Q6 | 333440 | 12480 |
| s27(id=16 S2->S3) | sw01-p2 | Q6 | 400000 | 12480 |
| s21(id=4 S1->S3) | S1-p0 | Q6 | 12480 | 12480 |
| s21(id=4 S1->S3) | sw02-p5 | Q6 | 29120 | 12480 |
| s21(id=4 S1->S3) | sw01-p2 | Q6 | 300160 | 12480 |
| s25(id=13 S1->S3) | S1-p0 | Q6 | 37440 | 12480 |
| s25(id=13 S1->S3) | sw02-p5 | Q6 | 300160 | 12480 |
| s25(id=13 S1->S3) | sw01-p2 | Q6 | 316800 | 12480 |
| s48(id=40 S3->S1) | S3-p0 | Q7 | 150080 | 12480 |
| s48(id=40 S3->S1) | sw01-p5 | Q7 | 166720 | 12480 |
| s48(id=40 S3->S1) | sw02-p2 | Q7 | 183360 | 12480 |
| s35(id=27 S2->S1) | S2-p0 | Q6 | 209600 | 12480 |
| s35(id=27 S2->S1) | sw08-p4 | Q6 | 537600 | 12480 |
| s35(id=27 S2->S1) | sw06-p5 | Q6 | 600000 | 12480 |
| s35(id=27 S2->S1) | sw04-p4 | Q6 | 616640 | 12480 |
| s35(id=27 S2->S1) | sw02-p2 | Q6 | 731520 | 12480 |
| s36(id=28 S2->S1) | S2-p0 | Q7 | 49920 | 12480 |
| s36(id=28 S2->S1) | sw08-p4 | Q7 | 66560 | 12480 |
| s36(id=28 S2->S1) | sw06-p5 | Q7 | 83200 | 12480 |
| s36(id=28 S2->S1) | sw04-p4 | Q7 | 229440 | 12480 |
| s36(id=28 S2->S1) | sw02-p2 | Q7 | 246080 | 12480 |
| s47(id=39 S2->S1) | S2-p0 | Q7 | 62720 | 12480 |
| s47(id=39 S2->S1) | sw08-p4 | Q7 | 79360 | 12480 |
| s47(id=39 S2->S1) | sw06-p5 | Q7 | 225600 | 12480 |
| s47(id=39 S2->S1) | sw04-p4 | Q7 | 242240 | 12480 |
| s47(id=39 S2->S1) | sw02-p2 | Q7 | 258880 | 12480 |
| s30(id=22 S2->S3) | S2-p0 | Q6 | 222080 | 12480 |
| s30(id=22 S2->S3) | sw08-p5 | Q6 | 300160 | 12480 |
| s30(id=22 S2->S3) | sw07-p4 | Q6 | 316800 | 12480 |
| s30(id=22 S2->S3) | sw05-p5 | Q6 | 333440 | 12480 |
| s30(id=22 S2->S3) | sw03-p4 | Q6 | 400000 | 12480 |
| s30(id=22 S2->S3) | sw01-p2 | Q6 | 416640 | 12480 |
| s32(id=24 S3->S1) | S3-p0 | Q7 | 350080 | 12480 |
| s32(id=24 S3->S1) | sw01-p5 | Q7 | 366720 | 12480 |
| s32(id=24 S3->S1) | sw02-p2 | Q7 | 383360 | 12480 |
| s46(id=38 S1->S3) | S1-p0 | Q7 | 87360 | 12480 |
| s46(id=38 S1->S3) | sw02-p5 | Q7 | 150080 | 12480 |
| s46(id=38 S1->S3) | sw01-p2 | Q7 | 166720 | 12480 |
| s54(id=46 S3->S1) | S3-p0 | Q6 | 88320 | 12480 |
| s54(id=46 S3->S1) | sw01-p5 | Q6 | 104960 | 12480 |
| s54(id=46 S3->S1) | sw02-p2 | Q6 | 121600 | 12480 |
| s55(id=47 S3->S1) | S3-p0 | Q6 | 101120 | 12480 |
| s55(id=47 S3->S1) | sw01-p5 | Q6 | 117760 | 12480 |
| s55(id=47 S3->S1) | sw02-p2 | Q6 | 134400 | 12480 |
| s58(id=50 S2->S3) | S2-p0 | Q6 | 300160 | 12480 |
| s58(id=50 S2->S3) | sw08-p5 | Q6 | 316800 | 12480 |
| s58(id=50 S2->S3) | sw07-p4 | Q6 | 333440 | 12480 |
| s58(id=50 S2->S3) | sw05-p5 | Q6 | 400000 | 12480 |
| s58(id=50 S2->S3) | sw03-p4 | Q6 | 416640 | 12480 |
| s58(id=50 S2->S3) | sw01-p2 | Q6 | 433280 | 12480 |
| s40(id=32 S1->S3) | S1-p0 | Q7 | 150080 | 12480 |
| s40(id=32 S1->S3) | sw02-p5 | Q7 | 166720 | 12480 |
| s40(id=32 S1->S3) | sw01-p2 | Q7 | 183360 | 12480 |
| s44(id=36 S2->S3) | S2-p0 | Q7 | 75200 | 12480 |
| s44(id=36 S2->S3) | sw08-p5 | Q7 | 91840 | 12480 |
| s44(id=36 S2->S3) | sw07-p4 | Q7 | 108480 | 12480 |
| s44(id=36 S2->S3) | sw05-p5 | Q7 | 125120 | 12480 |
| s44(id=36 S2->S3) | sw03-p4 | Q7 | 179520 | 12480 |
| s44(id=36 S2->S3) | sw01-p2 | Q7 | 196160 | 12480 |

## Constraint check

- C1-C7, C9: OK
- window-boundary integrity (no window's psi/delta changed anywhere): OK

## GCL per egress port

### sw01-p2  (14 entries, util 32.7600 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 206400 0x80 # 10000000   Q7
sgs 10560 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 123200 0x80 # 10000000   Q7
sgs 43520 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p4  (18 entries, util 6.2400 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 75200 0x40 # 01000000   Q6
sgs 33280 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 75200 0x40 # 01000000   Q6
sgs 33280 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 75200 0x40 # 01000000   Q6
sgs 33280 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 33600 0x40 # 01000000   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p5  (26 entries, util 26.5200 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 13120 0xBF # 10111111   Q7
sgs 46720 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 122240 0x80 # 10000000   Q7
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 13120 0xBF # 10111111   Q7
sgs 46720 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 105600 0x80 # 10000000   Q7
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (25 entries, util 32.7600 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 33280 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 56000 0x40 # 01000000   Q6
sgs 35200 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 131520 0x80 # 10000000   Q7
sgs 35200 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 33280 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 13120 0x3F # 00111111   BE
sgs 56000 0x40 # 01000000   Q6
sgs 35200 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 98240 0x80 # 10000000   Q7
sgs 18560 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p4  (28 entries, util 18.7200 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 50240 0x80 # 10000000   Q7
sgs 33280 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 125120 0x80 # 10000000   Q7
sgs 33280 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 100160 0x80 # 10000000   Q7
sgs 33280 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 108480 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p5  (18 entries, util 18.7200 %)

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

### sw03-p4  (14 entries, util 14.0400 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 206400 0x80 # 10000000   Q7
sgs 27200 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 139840 0x80 # 10000000   Q7
sgs 43520 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p5  (22 entries, util 6.2400 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 8320 0x3F # 00111111   BE
sgs 75200 0x40 # 01000000   Q6
sgs 16640 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 8320 0x3F # 00111111   BE
sgs 75200 0x40 # 01000000   Q6
sgs 16640 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 8320 0x3F # 00111111   BE
sgs 75200 0x40 # 01000000   Q6
sgs 16640 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 8320 0x3F # 00111111   BE
sgs 16960 0x40 # 01000000   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p4  (10 entries, util 6.2400 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 462720 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (28 entries, util 18.7200 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 50240 0x80 # 10000000   Q7
sgs 16640 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 125120 0x80 # 10000000   Q7
sgs 16640 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 100160 0x80 # 10000000   Q7
sgs 16640 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 91840 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (19 entries, util 6.2400 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 75200 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 75200 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 75200 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12800 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p5  (12 entries, util 14.0400 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 206400 0x80 # 10000000   Q7
sgs 43840 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 156480 0x80 # 10000000   Q7
sgs 43520 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p4  (25 entries, util 18.7200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 3520 0x3F # 00111111   BE
sgs 33600 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 50240 0x80 # 10000000   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 125120 0x80 # 10000000   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 3520 0x3F # 00111111   BE
sgs 96320 0x80 # 10000000   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 75200 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (10 entries, util 6.2400 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 8320 0x3F # 00111111   BE
sgs 479360 0x80 # 10000000   Q7
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

### sw07-p5  (18 entries, util 6.2400 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 75200 0x40 # 01000000   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 75200 0x40 # 01000000   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 75200 0x40 # 01000000   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 46080 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p2  (31 entries, util 24.9600 %)

```
sgs 66560 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 32960 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 16640 0x80 # 10000000   Q7
sgs 83520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 16000 0x40 # 01000000   Q6
sgs 142400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 16640 0x80 # 10000000   Q7
sgs 128960 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 16000 0x40 # 01000000   Q6
sgs 75840 0x3F # 00111111   BE
```

### sw08-p4  (9 entries, util 6.2400 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 29120 0x7F # 01111111   Q6
sgs 496000 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (13 entries, util 14.0400 %)

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

