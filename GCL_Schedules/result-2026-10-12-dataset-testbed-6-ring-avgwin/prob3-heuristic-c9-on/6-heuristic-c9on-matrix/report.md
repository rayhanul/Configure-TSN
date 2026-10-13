# Reconfiguration-free admission (Problem 3)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Frozen schedule W loaded from: **result/result-2026-10-12-dataset-testbed-6-ring-avgwin/heuristic-c9-on/6-matrix-c9on**

## Admission: W (before) vs. after this run's arrivals

| | admitted | of total |
|---|---|---|
| W (base, unchanged) | 10 | 10 |
| + this run's arrivals | 15 | 40 |

Every arrival admitted here required **zero** window-boundary changes -- see the GCL-entry table below (unchanged from W by construction) and the window-boundary integrity check. No previously-admitted flow was rerouted.

## Arrivals

| id | src->dst | RS(s) size | admitted | route | queue | phi_s (ns) | e2e (ns) | rerouted to make room | reason if rejected |
|---|---|---|---|---|---|---|---|---|---|
| 3 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 16 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 15 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 12480 | 115520 | - | - |
| 18 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 5 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 13 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q6 | 300160 | 39360 | - | - |
| 8 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 62400 | 500160 | - | - |
| 11 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 17 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 87360 | 488000 | - | - |
| 10 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q6 | 12480 | 22720 | - | - |
| 27 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q6 | 37440 | 27840 | - | - |
| 37 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 39 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q7 | 77120 | 511040 | - | - |
| 43 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 47 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 25 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q6 | 49920 | 80960 | - | - |
| 36 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 99840 | 45760 | - | - |
| 40 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 150080 | 36800 | - | - |
| 32 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q6 | 118080 | 32000 | - | - |
| 35 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 38 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 150080 | 512320 | - | - |
| 45 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q6 | 130560 | 90240 | - | - |
| 46 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 29 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 50 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 162560 | 36800 | - | - |
| 22 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 37440 | 196160 | - | - |
| 26 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 30 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 31 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 41 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 42 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 49 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 23 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 24 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 34 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 21 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 28 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 33 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 44 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 48 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |

## Per-port GCL entries (should equal W exactly)

| port | W entries | after arrivals | GCL_size |
|---|---|---|---|
| sw01-p2 | 9 | 9 | 255 |
| sw01-p4 | 18 | 18 | 255 |
| sw01-p5 | 32 | 32 | 255 |
| sw02-p2 | 29 | 29 | 255 |
| sw02-p4 | 20 | 20 | 255 |
| sw02-p5 | 9 | 9 | 255 |
| sw03-p4 | 18 | 18 | 255 |
| sw03-p5 | 18 | 18 | 255 |
| sw04-p4 | 18 | 18 | 255 |
| sw04-p5 | 20 | 20 | 255 |
| sw05-p4 | 18 | 18 | 255 |
| sw05-p5 | 18 | 18 | 255 |
| sw06-p4 | 21 | 21 | 255 |
| sw06-p5 | 19 | 19 | 255 |
| sw07-p4 | 18 | 18 | 255 |
| sw07-p5 | 22 | 22 | 255 |
| sw08-p2 | 28 | 28 | 255 |
| sw08-p4 | 18 | 18 | 255 |
| sw08-p5 | 18 | 18 | 255 |

## Per-hop windows used by newly admitted flows

| flow | egress port | queue | psi (ns, unchanged) | delta (ns, unchanged) |
|---|---|---|---|---|
| s26(id=15 S2->S3) | S2-p0 | Q6 | 12480 | 12480 |
| s26(id=15 S2->S3) | sw08-p5 | Q6 | 24960 | 12480 |
| s26(id=15 S2->S3) | sw07-p4 | Q6 | 32640 | 12480 |
| s26(id=15 S2->S3) | sw05-p5 | Q6 | 100160 | 12480 |
| s26(id=15 S2->S3) | sw03-p4 | Q6 | 107840 | 12480 |
| s26(id=15 S2->S3) | sw01-p2 | Q6 | 115520 | 12480 |
| s25(id=13 S1->S2) | S1-p0 | Q6 | 300160 | 12480 |
| s25(id=13 S1->S2) | sw02-p4 | Q6 | 306880 | 12480 |
| s25(id=13 S1->S2) | sw04-p5 | Q6 | 313600 | 12480 |
| s25(id=13 S1->S2) | sw06-p4 | Q6 | 320320 | 12480 |
| s25(id=13 S1->S2) | sw08-p2 | Q6 | 327040 | 12480 |
| s22(id=8 S2->S3) | S2-p0 | Q7 | 62400 | 12480 |
| s22(id=8 S2->S3) | sw08-p5 | Q7 | 67520 | 12480 |
| s22(id=8 S2->S3) | sw07-p4 | Q7 | 72640 | 12480 |
| s22(id=8 S2->S3) | sw05-p5 | Q7 | 77760 | 12480 |
| s22(id=8 S2->S3) | sw03-p4 | Q7 | 82880 | 12480 |
| s22(id=8 S2->S3) | sw01-p2 | Q7 | 550080 | 12480 |
| s28(id=17 S2->S3) | S2-p0 | Q7 | 87360 | 12480 |
| s28(id=17 S2->S3) | sw08-p5 | Q7 | 150080 | 12480 |
| s28(id=17 S2->S3) | sw07-p4 | Q7 | 156160 | 12480 |
| s28(id=17 S2->S3) | sw05-p5 | Q7 | 162240 | 12480 |
| s28(id=17 S2->S3) | sw03-p4 | Q7 | 556800 | 12480 |
| s28(id=17 S2->S3) | sw01-p2 | Q7 | 562880 | 12480 |
| s23(id=10 S1->S3) | S1-p0 | Q6 | 12480 | 12480 |
| s23(id=10 S1->S3) | sw02-p5 | Q6 | 17600 | 12480 |
| s23(id=10 S1->S3) | sw01-p2 | Q6 | 22720 | 12480 |
| s36(id=27 S1->S3) | S1-p0 | Q6 | 37440 | 12480 |
| s36(id=27 S1->S3) | sw02-p5 | Q6 | 45120 | 12480 |
| s36(id=27 S1->S3) | sw01-p2 | Q6 | 52800 | 12480 |
| s48(id=39 S1->S3) | S1-p0 | Q7 | 77120 | 12480 |
| s48(id=39 S1->S3) | sw02-p5 | Q7 | 568960 | 12480 |
| s48(id=39 S1->S3) | sw01-p2 | Q7 | 575680 | 12480 |
| s34(id=25 S1->S2) | S1-p0 | Q6 | 49920 | 12480 |
| s34(id=25 S1->S2) | sw02-p4 | Q6 | 100160 | 12480 |
| s34(id=25 S1->S2) | sw04-p5 | Q6 | 106240 | 12480 |
| s34(id=25 S1->S2) | sw06-p4 | Q6 | 112320 | 12480 |
| s34(id=25 S1->S2) | sw08-p2 | Q6 | 118400 | 12480 |
| s45(id=36 S2->S1) | S2-p0 | Q7 | 99840 | 12480 |
| s45(id=36 S2->S1) | sw08-p4 | Q7 | 108160 | 12480 |
| s45(id=36 S2->S1) | sw06-p5 | Q7 | 116480 | 12480 |
| s45(id=36 S2->S1) | sw04-p4 | Q7 | 124800 | 12480 |
| s45(id=36 S2->S1) | sw02-p2 | Q7 | 133120 | 12480 |
| s49(id=40 S1->S2) | S1-p0 | Q7 | 150080 | 12480 |
| s49(id=40 S1->S2) | sw02-p4 | Q7 | 156160 | 12480 |
| s49(id=40 S1->S2) | sw04-p5 | Q7 | 162240 | 12480 |
| s49(id=40 S1->S2) | sw06-p4 | Q7 | 168320 | 12480 |
| s49(id=40 S1->S2) | sw08-p2 | Q7 | 174400 | 12480 |
| s41(id=32 S1->S3) | S1-p0 | Q6 | 118080 | 12480 |
| s41(id=32 S1->S3) | sw02-p5 | Q6 | 123200 | 12480 |
| s41(id=32 S1->S3) | sw01-p2 | Q6 | 128320 | 12480 |
| s47(id=38 S2->S3) | S2-p0 | Q7 | 150080 | 12480 |
| s47(id=38 S2->S3) | sw08-p5 | Q7 | 162560 | 12480 |
| s47(id=38 S2->S3) | sw07-p4 | Q7 | 168640 | 12480 |
| s47(id=38 S2->S3) | sw05-p5 | Q7 | 564480 | 12480 |
| s47(id=38 S2->S3) | sw03-p4 | Q7 | 583360 | 12480 |
| s47(id=38 S2->S3) | sw01-p2 | Q7 | 649920 | 12480 |
| s54(id=45 S1->S3) | S1-p0 | Q6 | 130560 | 12480 |
| s54(id=45 S1->S3) | sw02-p5 | Q6 | 138880 | 12480 |
| s54(id=45 S1->S3) | sw01-p2 | Q6 | 147200 | 12480 |
| s59(id=50 S1->S2) | S1-p0 | Q7 | 162560 | 12480 |
| s59(id=50 S1->S2) | sw02-p4 | Q7 | 168640 | 12480 |
| s59(id=50 S1->S2) | sw04-p5 | Q7 | 174720 | 12480 |
| s59(id=50 S1->S2) | sw06-p4 | Q7 | 180800 | 12480 |
| s59(id=50 S1->S2) | sw08-p2 | Q7 | 186880 | 12480 |
| s31(id=22 S2->S3) | S2-p0 | Q6 | 37440 | 12480 |
| s31(id=22 S2->S3) | sw08-p5 | Q6 | 100160 | 12480 |
| s31(id=22 S2->S3) | sw07-p4 | Q6 | 106880 | 12480 |
| s31(id=22 S2->S3) | sw05-p5 | Q6 | 113600 | 12480 |
| s31(id=22 S2->S3) | sw03-p4 | Q6 | 200000 | 12480 |
| s31(id=22 S2->S3) | sw01-p2 | Q6 | 206720 | 12480 |

## Constraint check

- C1-C7, C9: OK
- window-boundary integrity (no window's psi/delta changed anywhere): OK

## GCL per egress port

### sw01-p2  (9 entries, util 23.4000 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 25920 0x7F # 01111111   Q6
sgs 499200 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p4  (18 entries, util 6.2400 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 75200 0x40 # 01000000   Q6
sgs 41600 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 75200 0x40 # 01000000   Q6
sgs 41600 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 75200 0x40 # 01000000   Q6
sgs 41600 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 41920 0x40 # 01000000   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p5  (32 entries, util 15.6000 %)

```
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 6080 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 14720 0xBF # 10111111   Q7
sgs 64000 0x40 # 01000000   Q6
sgs 2880 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 6080 0x3F # 00111111   BE
sgs 91200 0x40 # 01000000   Q6
sgs 2880 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 6080 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 14720 0xBF # 10111111   Q7
sgs 64000 0x40 # 01000000   Q6
sgs 2880 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 6080 0x3F # 00111111   BE
sgs 82880 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (29 entries, util 29.6400 %)

```
sgs 16640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 1600 0x3F # 00111111   BE
sgs 43840 0x40 # 01000000   Q6
sgs 2240 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 2240 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 42880 0x80 # 10000000   Q7
sgs 69440 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 1600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 18880 0x3F # 00111111   BE
sgs 18560 0x40 # 01000000   Q6
sgs 136000 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 1600 0x3F # 00111111   BE
sgs 43840 0x40 # 01000000   Q6
sgs 16960 0x3F # 00111111   BE
sgs 17280 0x40 # 01000000   Q6
sgs 107840 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 1600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 18880 0x3F # 00111111   BE
sgs 17280 0x40 # 01000000   Q6
sgs 120640 0x3F # 00111111   BE
```

### sw02-p4  (20 entries, util 15.6000 %)

```
sgs 5120 0x3F # 00111111   BE
sgs 50240 0x80 # 10000000   Q7
sgs 44800 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 5120 0x3F # 00111111   BE
sgs 50240 0x80 # 10000000   Q7
sgs 44800 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 5120 0x3F # 00111111   BE
sgs 50240 0x80 # 10000000   Q7
sgs 44800 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 5120 0x3F # 00111111   BE
sgs 45120 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p5  (9 entries, util 12.4800 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 19200 0x7F # 01111111   Q6
sgs 505920 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (18 entries, util 10.9200 %)

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

### sw03-p5  (18 entries, util 6.2400 %)

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

### sw04-p4  (18 entries, util 14.0400 %)

```
sgs 23040 0x7F # 01111111   Q6
sgs 29760 0x40 # 01000000   Q6
sgs 17280 0xBF # 10111111   Q7
sgs 75200 0x80 # 10000000   Q7
sgs 4800 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 122240 0x40 # 01000000   Q6
sgs 4800 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 122240 0x40 # 01000000   Q6
sgs 4800 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 99200 0x40 # 01000000   Q6
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (20 entries, util 15.6000 %)

```
sgs 10240 0x3F # 00111111   BE
sgs 50240 0x80 # 10000000   Q7
sgs 39680 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 10240 0x3F # 00111111   BE
sgs 50240 0x80 # 10000000   Q7
sgs 39680 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 10240 0x3F # 00111111   BE
sgs 50240 0x80 # 10000000   Q7
sgs 39680 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 10240 0x3F # 00111111   BE
sgs 40000 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (18 entries, util 6.2400 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 75200 0x40 # 01000000   Q6
sgs 24960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 75200 0x40 # 01000000   Q6
sgs 24960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 75200 0x40 # 01000000   Q6
sgs 24960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 25280 0x40 # 01000000   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p5  (18 entries, util 10.9200 %)

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

### sw06-p4  (21 entries, util 15.6000 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 2880 0x3F # 00111111   BE
sgs 75200 0x80 # 10000000   Q7
sgs 9600 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 75200 0x80 # 10000000   Q7
sgs 9600 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 75200 0x80 # 10000000   Q7
sgs 9600 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 59840 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (19 entries, util 14.0400 %)

```
sgs 15360 0x7F # 01111111   Q6
sgs 32320 0x40 # 01000000   Q6
sgs 2240 0x3F # 00111111   BE
sgs 13440 0xBF # 10111111   Q7
sgs 74240 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 122240 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 122240 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 106880 0x40 # 01000000   Q6
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (18 entries, util 10.9200 %)

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

### sw07-p5  (22 entries, util 6.2400 %)

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

### sw08-p2  (28 entries, util 21.8400 %)

```
sgs 20480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 16960 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 76160 0x40 # 01000000   Q6
sgs 7360 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 16960 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 76160 0x40 # 01000000   Q6
sgs 7360 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 16960 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 76160 0x40 # 01000000   Q6
sgs 7360 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 16960 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 55680 0x40 # 01000000   Q6
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p4  (18 entries, util 14.0400 %)

```
sgs 7680 0x3F # 00111111   BE
sgs 34880 0x40 # 01000000   Q6
sgs 14080 0x3F # 00111111   BE
sgs 73280 0x80 # 10000000   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 7680 0x3F # 00111111   BE
sgs 122240 0x40 # 01000000   Q6
sgs 20160 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 7680 0x3F # 00111111   BE
sgs 122240 0x40 # 01000000   Q6
sgs 20160 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 7680 0x3F # 00111111   BE
sgs 114560 0x40 # 01000000   Q6
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (18 entries, util 10.9200 %)

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

