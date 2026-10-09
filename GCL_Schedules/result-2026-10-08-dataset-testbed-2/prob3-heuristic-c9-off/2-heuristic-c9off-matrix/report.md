# Reconfiguration-free admission (Problem 3)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4000 ns
- Frozen schedule W loaded from: **result/result-2026-10-08-dataset-testbed-2/heuristic-c9-off/2-matrix-c9off**

## Admission: W (before) vs. after this run's arrivals

| | admitted | of total |
|---|---|---|
| W (base, unchanged) | 11 | 11 |
| + this run's arrivals | 11 | 39 |

Every arrival admitted here required **zero** window-boundary changes -- see the GCL-entry table below (unchanged from W by construction) and the window-boundary integrity check. No previously-admitted flow was rerouted.

## Arrivals

| id | src->dst | RS(s) size | admitted | route | queue | phi_s (ns) | e2e (ns) | rerouted to make room | reason if rejected |
|---|---|---|---|---|---|---|---|---|---|
| 3 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 17 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 19 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 5 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 15 | S2->S3 | - | yes | S2->sw08->sw06->sw03->sw01->S3 | Q6 | 12480 | 333440 | - | - |
| 13 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q7 | 62400 | 233920 | - | - |
| 2 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 6 | S2->S1 | - | yes | S2->sw08->sw07->sw05->sw02->S1 | Q6 | 87680 | 79040 | - | - |
| 8 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 50 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q6 | 62720 | 255360 | - | - |
| 21 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 22 | S2->S3 | - | yes | S2->sw08->sw06->sw03->sw01->S3 | Q6 | 37440 | 375040 | - | - |
| 24 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 28 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 35 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 37 | S2->S3 | - | yes | S2->sw08->sw06->sw03->sw01->S3 | Q6 | 331520 | 290560 | - | - |
| 40 | S2->S1 | - | yes | S2->sw08->sw07->sw05->sw02->S1 | Q6 | 100480 | 145280 | - | - |
| 41 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 43 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 23 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 29 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 26 | S2->S3 | - | yes | S2->sw08->sw06->sw03->sw01->S3 | Q7 | 62400 | 79040 | - | - |
| 33 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 36 | S2->S3 | - | yes | S2->sw08->sw06->sw03->sw01->S3 | Q7 | 150080 | 128960 | - | - |
| 45 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 46 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 47 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 48 | S2->S3 | - | yes | S2->sw08->sw06->sw03->sw01->S3 | Q7 | 162880 | 132800 | - | - |
| 49 | S2->S1 | - | yes | S2->sw08->sw07->sw05->sw02->S1 | Q6 | 131520 | 280960 | - | - |
| 30 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 34 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 42 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
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
| sw01-p3 | 14 | 14 | 255 |
| sw01-p4 | 24 | 24 | 255 |
| sw01-p5 | 13 | 13 | 255 |
| sw02-p2 | 27 | 27 | 255 |
| sw02-p3 | 10 | 10 | 255 |
| sw02-p4 | 18 | 18 | 255 |
| sw02-p5 | 25 | 25 | 255 |
| sw03-p3 | 14 | 14 | 255 |
| sw03-p4 | 19 | 19 | 255 |
| sw03-p5 | 18 | 18 | 255 |
| sw04-p3 | 18 | 18 | 255 |
| sw04-p4 | 18 | 18 | 255 |
| sw04-p5 | 18 | 18 | 255 |
| sw05-p2 | 22 | 22 | 255 |
| sw05-p3 | 18 | 18 | 255 |
| sw05-p4 | 18 | 18 | 255 |
| sw05-p5 | 23 | 23 | 255 |
| sw06-p2 | 23 | 23 | 255 |
| sw06-p3 | 14 | 14 | 255 |
| sw06-p4 | 18 | 18 | 255 |
| sw06-p5 | 18 | 18 | 255 |
| sw07-p3 | 22 | 22 | 255 |
| sw07-p4 | 22 | 22 | 255 |
| sw07-p5 | 18 | 18 | 255 |
| sw08-p2 | 27 | 27 | 255 |
| sw08-p4 | 12 | 12 | 255 |
| sw08-p5 | 24 | 24 | 255 |

## Per-hop windows used by newly admitted flows

| flow | egress port | queue | psi (ns, unchanged) | delta (ns, unchanged) |
|---|---|---|---|---|
| s26(id=15 S2->S3) | S2-p0 | Q6 | 12480 | 12480 |
| s26(id=15 S2->S3) | sw08-p4 | Q6 | 29120 | 12480 |
| s26(id=15 S2->S3) | sw06-p3 | Q6 | 300160 | 12480 |
| s26(id=15 S2->S3) | sw03-p3 | Q6 | 316800 | 12480 |
| s26(id=15 S2->S3) | sw01-p3 | Q6 | 333440 | 12480 |
| s25(id=13 S3->S1) | S3-p0 | Q7 | 62400 | 12480 |
| s25(id=13 S3->S1) | sw01-p5 | Q7 | 267200 | 12480 |
| s25(id=13 S3->S1) | sw02-p2 | Q7 | 283840 | 12480 |
| s23(id=6 S2->S1) | S2-p0 | Q6 | 87680 | 12480 |
| s23(id=6 S2->S1) | sw08-p5 | Q6 | 104320 | 12480 |
| s23(id=6 S2->S1) | sw07-p3 | Q6 | 120960 | 12480 |
| s23(id=6 S2->S1) | sw05-p5 | Q6 | 137600 | 12480 |
| s23(id=6 S2->S1) | sw02-p2 | Q6 | 154240 | 12480 |
| s58(id=50 S1->S3) | S1-p0 | Q6 | 62720 | 12480 |
| s58(id=50 S1->S3) | sw02-p3 | Q6 | 79360 | 12480 |
| s58(id=50 S1->S3) | sw01-p3 | Q6 | 305600 | 12480 |
| s30(id=22 S2->S3) | S2-p0 | Q6 | 37440 | 12480 |
| s30(id=22 S2->S3) | sw08-p4 | Q6 | 300160 | 12480 |
| s30(id=22 S2->S3) | sw06-p3 | Q6 | 316800 | 12480 |
| s30(id=22 S2->S3) | sw03-p3 | Q6 | 333440 | 12480 |
| s30(id=22 S2->S3) | sw01-p3 | Q6 | 400000 | 12480 |
| s45(id=37 S2->S3) | S2-p0 | Q6 | 331520 | 12480 |
| s45(id=37 S2->S3) | sw08-p4 | Q6 | 400000 | 12480 |
| s45(id=37 S2->S3) | sw06-p3 | Q6 | 416640 | 12480 |
| s45(id=37 S2->S3) | sw03-p3 | Q6 | 433280 | 12480 |
| s45(id=37 S2->S3) | sw01-p3 | Q6 | 609600 | 12480 |
| s48(id=40 S2->S1) | S2-p0 | Q6 | 100480 | 12480 |
| s48(id=40 S2->S1) | sw08-p5 | Q6 | 128320 | 12480 |
| s48(id=40 S2->S1) | sw07-p3 | Q6 | 200000 | 12480 |
| s48(id=40 S2->S1) | sw05-p5 | Q6 | 216640 | 12480 |
| s48(id=40 S2->S1) | sw02-p2 | Q6 | 233280 | 12480 |
| s34(id=26 S2->S3) | S2-p0 | Q7 | 62400 | 12480 |
| s34(id=26 S2->S3) | sw08-p4 | Q7 | 79040 | 12480 |
| s34(id=26 S2->S3) | sw06-p3 | Q7 | 95680 | 12480 |
| s34(id=26 S2->S3) | sw03-p3 | Q7 | 112320 | 12480 |
| s34(id=26 S2->S3) | sw01-p3 | Q7 | 128960 | 12480 |
| s44(id=36 S2->S3) | S2-p0 | Q7 | 150080 | 12480 |
| s44(id=36 S2->S3) | sw08-p4 | Q7 | 166720 | 12480 |
| s44(id=36 S2->S3) | sw06-p3 | Q7 | 183360 | 12480 |
| s44(id=36 S2->S3) | sw03-p3 | Q7 | 200000 | 12480 |
| s44(id=36 S2->S3) | sw01-p3 | Q7 | 216640 | 12480 |
| s56(id=48 S2->S3) | S2-p0 | Q7 | 162880 | 12480 |
| s56(id=48 S2->S3) | sw08-p4 | Q7 | 179520 | 12480 |
| s56(id=48 S2->S3) | sw06-p3 | Q7 | 196160 | 12480 |
| s56(id=48 S2->S3) | sw03-p3 | Q7 | 212800 | 12480 |
| s56(id=48 S2->S3) | sw01-p3 | Q7 | 229440 | 12480 |
| s57(id=49 S2->S1) | S2-p0 | Q6 | 131520 | 12480 |
| s57(id=49 S2->S1) | sw08-p5 | Q6 | 200000 | 12480 |
| s57(id=49 S2->S1) | sw07-p3 | Q6 | 216640 | 12480 |
| s57(id=49 S2->S1) | sw05-p5 | Q6 | 233280 | 12480 |
| s57(id=49 S2->S1) | sw02-p2 | Q6 | 400000 | 12480 |

## Constraint check

- C1-C7, C9: OK
- window-boundary integrity (no window's psi/delta changed anywhere): OK

## GCL per egress port

### sw01-p3  (14 entries, util 21.8400 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 209600 0x80 # 10000000   Q7
sgs 44480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 46080 0xBF # 10111111   Q7
sgs 113600 0x80 # 10000000   Q7
sgs 40320 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p4  (24 entries, util 10.9200 %)

```
sgs 22400 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 15040 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 41920 0x40 # 01000000   Q6
sgs 16640 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 22400 0x7F # 01111111   Q6
sgs 111040 0x40 # 01000000   Q6
sgs 16640 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 22400 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 15040 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 66880 0x80 # 10000000   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 22400 0x7F # 01111111   Q6
sgs 88640 0x40 # 01000000   Q6
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p5  (13 entries, util 6.2400 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 206400 0x40 # 01000000   Q6
sgs 1920 0x3F # 00111111   BE
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 164800 0x40 # 01000000   Q6
sgs 43520 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (27 entries, util 23.4000 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 16640 0xBF # 10111111   Q7
sgs 16320 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 61120 0x40 # 01000000   Q6
sgs 47360 0x7F # 01111111   Q6
sgs 21120 0xBF # 10111111   Q7
sgs 118720 0x80 # 10000000   Q7
sgs 10240 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 16640 0xBF # 10111111   Q7
sgs 16320 0x7F # 01111111   Q6
sgs 86080 0x80 # 10000000   Q7
sgs 47360 0x7F # 01111111   Q6
sgs 21120 0xBF # 10111111   Q7
sgs 60480 0x80 # 10000000   Q7
sgs 18560 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p3  (10 entries, util 3.1200 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 471040 0x40 # 01000000   Q6
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

### sw02-p5  (25 entries, util 12.4800 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 105280 0x80 # 10000000   Q7
sgs 3200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 105280 0x80 # 10000000   Q7
sgs 3200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 105280 0x80 # 10000000   Q7
sgs 3200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 88640 0x80 # 10000000   Q7
sgs 19840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p3  (14 entries, util 18.7200 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 29440 0xBF # 10111111   Q7
sgs 206400 0x80 # 10000000   Q7
sgs 14400 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 29440 0xBF # 10111111   Q7
sgs 127040 0x80 # 10000000   Q7
sgs 43520 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (19 entries, util 10.9200 %)

```
sgs 39040 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 31680 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 41920 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 39040 0x7F # 01111111   Q6
sgs 111040 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 39040 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 31680 0xBF # 10111111   Q7
sgs 66880 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
sgs 39040 0x7F # 01111111   Q6
sgs 72000 0x40 # 01000000   Q6
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
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

### sw05-p2  (22 entries, util 12.4800 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 105280 0x80 # 10000000   Q7
sgs 36480 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 105280 0x80 # 10000000   Q7
sgs 36480 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 105280 0x80 # 10000000   Q7
sgs 36480 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 72000 0x80 # 10000000   Q7
sgs 19840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
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

### sw05-p5  (23 entries, util 17.1600 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 4480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 32960 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 40640 0x40 # 01000000   Q6
sgs 34560 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 4480 0x3F # 00111111   BE
sgs 111040 0x80 # 10000000   Q7
sgs 34560 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 4480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 32960 0xBF # 10111111   Q7
sgs 65600 0x80 # 10000000   Q7
sgs 34560 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 4480 0x3F # 00111111   BE
sgs 56640 0x80 # 10000000   Q7
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p2  (23 entries, util 10.9200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12800 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 24640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 48960 0x40 # 01000000   Q6
sgs 26240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12800 0xBF # 10111111   Q7
sgs 111040 0x40 # 01000000   Q6
sgs 26240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12800 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 24640 0xBF # 10111111   Q7
sgs 73920 0x80 # 10000000   Q7
sgs 26240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12800 0xBF # 10111111   Q7
sgs 48320 0x40 # 01000000   Q6
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p3  (14 entries, util 18.7200 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 10880 0x3F # 00111111   BE
sgs 206400 0x80 # 10000000   Q7
sgs 32960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 10880 0x3F # 00111111   BE
sgs 145600 0x80 # 10000000   Q7
sgs 43520 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
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

### sw07-p3  (22 entries, util 17.1600 %)

```
sgs 37760 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 32960 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 40640 0x40 # 01000000   Q6
sgs 1280 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 37760 0x7F # 01111111   Q6
sgs 111040 0x80 # 10000000   Q7
sgs 1280 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 37760 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 32960 0xBF # 10111111   Q7
sgs 65600 0x80 # 10000000   Q7
sgs 1280 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 37760 0x7F # 01111111   Q6
sgs 73280 0x80 # 10000000   Q7
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (22 entries, util 12.4800 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0xBF # 10111111   Q7
sgs 104640 0x80 # 10000000   Q7
sgs 19840 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0xBF # 10111111   Q7
sgs 104640 0x80 # 10000000   Q7
sgs 19840 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0xBF # 10111111   Q7
sgs 104640 0x80 # 10000000   Q7
sgs 19840 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0xBF # 10111111   Q7
sgs 54720 0x80 # 10000000   Q7
sgs 19840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
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

### sw08-p2  (27 entries, util 23.4000 %)

```
sgs 66560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 36800 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 24640 0x40 # 01000000   Q6
sgs 100480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 15680 0x80 # 10000000   Q7
sgs 158720 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 40000 0x80 # 10000000   Q7
sgs 134400 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 15680 0x80 # 10000000   Q7
sgs 92160 0x3F # 00111111   BE
```

### sw08-p4  (12 entries, util 18.7200 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 31360 0x7F # 01111111   Q6
sgs 206400 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 43840 0x7F # 01111111   Q6
sgs 162560 0x80 # 10000000   Q7
sgs 43520 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (24 entries, util 17.1600 %)

```
sgs 17280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 36800 0x40 # 01000000   Q6
sgs 21760 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 17280 0x7F # 01111111   Q6
sgs 111040 0x80 # 10000000   Q7
sgs 21760 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 17280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 61760 0x80 # 10000000   Q7
sgs 21760 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 17280 0x7F # 01111111   Q6
sgs 93760 0x80 # 10000000   Q7
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

