# Reconfiguration-free admission (Problem 3)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4000 ns
- Frozen schedule W loaded from: **result/result-2026-10-08-dataset-testbed-2/rl-c9-off/2-matrix-c9off**

## Admission: W (before) vs. after this run's arrivals

| | admitted | of total |
|---|---|---|
| W (base, unchanged) | 11 | 11 |
| + this run's arrivals | 15 | 39 |

Every arrival admitted here required **zero** window-boundary changes -- see the GCL-entry table below (unchanged from W by construction) and the window-boundary integrity check. No previously-admitted flow was rerouted.

## Arrivals

| id | src->dst | RS(s) size | admitted | route | queue | phi_s (ns) | e2e (ns) | rerouted to make room | reason if rejected |
|---|---|---|---|---|---|---|---|---|---|
| 3 | S1->S2 | - | yes | S1->sw02->sw05->sw07->sw08->S2 | Q6 | 12480 | 156160 | - | - |
| 17 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 19 | S2->S1 | - | yes | S2->sw08->sw07->sw05->sw02->S1 | Q6 | 12480 | 84160 | - | - |
| 5 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 15 | S2->S3 | - | yes | S2->sw08->sw06->sw03->sw01->S3 | Q6 | 37440 | 84800 | - | - |
| 13 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q7 | 37440 | 137920 | - | - |
| 2 | S3->S2 | - | yes | S3->sw01->sw03->sw06->sw08->S2 | Q6 | 87680 | 93440 | - | - |
| 6 | S2->S1 | - | yes | S2->sw08->sw07->sw05->sw02->S1 | Q6 | 87680 | 150080 | - | - |
| 8 | S1->S2 | - | yes | S1->sw02->sw05->sw07->sw08->S2 | Q6 | 437440 | 144000 | - | - |
| 50 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q6 | 449920 | 85120 | - | - |
| 21 | S1->S2 | - | yes | S1->sw02->sw05->sw07->sw08->S2 | Q6 | 499520 | 94720 | - | - |
| 22 | S2->S3 | - | yes | S2->sw08->sw06->sw03->sw01->S3 | Q6 | 100160 | 79040 | - | - |
| 24 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 28 | S1->S2 | - | yes | S1->sw02->sw05->sw07->sw08->S2 | Q6 | 512320 | 96320 | - | - |
| 35 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 37 | S2->S3 | - | yes | S2->sw08->sw06->sw03->sw01->S3 | Q7 | 62400 | 400000 | - | - |
| 40 | S2->S1 | - | yes | S2->sw08->sw07->sw05->sw02->S1 | Q6 | 227200 | 82240 | - | - |
| 41 | S1->S2 | - | yes | S1->sw02->sw05->sw07->sw08->S2 | Q7 | 62400 | 163520 | - | - |
| 43 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 23 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 29 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 26 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 33 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 36 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 45 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 46 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 47 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 48 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 49 | S2->S1 | - | yes | S2->sw08->sw07->sw05->sw02->S1 | Q6 | 242560 | 79680 | - | - |
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
| sw01-p3 | 16 | 16 | 255 |
| sw01-p4 | 24 | 24 | 255 |
| sw01-p5 | 16 | 16 | 255 |
| sw02-p2 | 31 | 31 | 255 |
| sw02-p3 | 10 | 10 | 255 |
| sw02-p4 | 18 | 18 | 255 |
| sw02-p5 | 24 | 24 | 255 |
| sw03-p3 | 15 | 15 | 255 |
| sw03-p4 | 19 | 19 | 255 |
| sw03-p5 | 18 | 18 | 255 |
| sw04-p3 | 18 | 18 | 255 |
| sw04-p4 | 18 | 18 | 255 |
| sw04-p5 | 18 | 18 | 255 |
| sw05-p2 | 30 | 30 | 255 |
| sw05-p3 | 18 | 18 | 255 |
| sw05-p4 | 18 | 18 | 255 |
| sw05-p5 | 23 | 23 | 255 |
| sw06-p2 | 23 | 23 | 255 |
| sw06-p3 | 13 | 13 | 255 |
| sw06-p4 | 18 | 18 | 255 |
| sw06-p5 | 18 | 18 | 255 |
| sw07-p3 | 22 | 22 | 255 |
| sw07-p4 | 27 | 27 | 255 |
| sw07-p5 | 18 | 18 | 255 |
| sw08-p2 | 35 | 35 | 255 |
| sw08-p4 | 13 | 13 | 255 |
| sw08-p5 | 26 | 26 | 255 |

## Per-hop windows used by newly admitted flows

| flow | egress port | queue | psi (ns, unchanged) | delta (ns, unchanged) |
|---|---|---|---|---|
| s21(id=3 S1->S2) | S1-p0 | Q6 | 12480 | 12480 |
| s21(id=3 S1->S2) | sw02-p5 | Q6 | 29120 | 12480 |
| s21(id=3 S1->S2) | sw05-p2 | Q6 | 107200 | 12480 |
| s21(id=3 S1->S2) | sw07-p4 | Q6 | 139200 | 12480 |
| s21(id=3 S1->S2) | sw08-p2 | Q6 | 155840 | 12480 |
| s28(id=19 S2->S1) | S2-p0 | Q6 | 12480 | 12480 |
| s28(id=19 S2->S1) | sw08-p5 | Q6 | 31040 | 12480 |
| s28(id=19 S2->S1) | sw07-p3 | Q6 | 50240 | 12480 |
| s28(id=19 S2->S1) | sw05-p5 | Q6 | 67200 | 12480 |
| s28(id=19 S2->S1) | sw02-p2 | Q6 | 84160 | 12480 |
| s26(id=15 S2->S3) | S2-p0 | Q6 | 37440 | 12480 |
| s26(id=15 S2->S3) | sw08-p4 | Q6 | 56960 | 12480 |
| s26(id=15 S2->S3) | sw06-p3 | Q6 | 74560 | 12480 |
| s26(id=15 S2->S3) | sw03-p3 | Q6 | 92160 | 12480 |
| s26(id=15 S2->S3) | sw01-p3 | Q6 | 109760 | 12480 |
| s25(id=13 S3->S1) | S3-p0 | Q7 | 37440 | 12480 |
| s25(id=13 S3->S1) | sw01-p5 | Q7 | 146240 | 12480 |
| s25(id=13 S3->S1) | sw02-p2 | Q7 | 162880 | 12480 |
| s20(id=2 S3->S2) | S3-p0 | Q6 | 87680 | 12480 |
| s20(id=2 S3->S2) | sw01-p4 | Q6 | 104320 | 12480 |
| s20(id=2 S3->S2) | sw03-p4 | Q6 | 120960 | 12480 |
| s20(id=2 S3->S2) | sw06-p2 | Q6 | 152000 | 12480 |
| s20(id=2 S3->S2) | sw08-p2 | Q6 | 168640 | 12480 |
| s23(id=6 S2->S1) | S2-p0 | Q6 | 87680 | 12480 |
| s23(id=6 S2->S1) | sw08-p5 | Q6 | 104320 | 12480 |
| s23(id=6 S2->S1) | sw07-p3 | Q6 | 120960 | 12480 |
| s23(id=6 S2->S1) | sw05-p5 | Q6 | 137600 | 12480 |
| s23(id=6 S2->S1) | sw02-p2 | Q6 | 225280 | 12480 |
| s24(id=8 S1->S2) | S1-p0 | Q6 | 437440 | 12480 |
| s24(id=8 S1->S2) | sw02-p5 | Q6 | 503360 | 12480 |
| s24(id=8 S1->S2) | sw05-p2 | Q6 | 520000 | 12480 |
| s24(id=8 S1->S2) | sw07-p4 | Q6 | 552320 | 12480 |
| s24(id=8 S1->S2) | sw08-p2 | Q6 | 568960 | 12480 |
| s58(id=50 S1->S3) | S1-p0 | Q6 | 449920 | 12480 |
| s58(id=50 S1->S3) | sw02-p3 | Q6 | 505920 | 12480 |
| s58(id=50 S1->S3) | sw01-p3 | Q6 | 522560 | 12480 |
| s29(id=21 S1->S2) | S1-p0 | Q6 | 499520 | 12480 |
| s29(id=21 S1->S2) | sw02-p5 | Q6 | 516160 | 12480 |
| s29(id=21 S1->S2) | sw05-p2 | Q6 | 548480 | 12480 |
| s29(id=21 S1->S2) | sw07-p4 | Q6 | 565120 | 12480 |
| s29(id=21 S1->S2) | sw08-p2 | Q6 | 581760 | 12480 |
| s30(id=22 S2->S3) | S2-p0 | Q6 | 100160 | 12480 |
| s30(id=22 S2->S3) | sw08-p4 | Q6 | 116800 | 12480 |
| s30(id=22 S2->S3) | sw06-p3 | Q6 | 133440 | 12480 |
| s30(id=22 S2->S3) | sw03-p3 | Q6 | 150080 | 12480 |
| s30(id=22 S2->S3) | sw01-p3 | Q6 | 166720 | 12480 |
| s36(id=28 S1->S2) | S1-p0 | Q6 | 512320 | 12480 |
| s36(id=28 S1->S2) | sw02-p5 | Q6 | 546240 | 12480 |
| s36(id=28 S1->S2) | sw05-p2 | Q6 | 562880 | 12480 |
| s36(id=28 S1->S2) | sw07-p4 | Q6 | 579520 | 12480 |
| s36(id=28 S1->S2) | sw08-p2 | Q6 | 596160 | 12480 |
| s45(id=37 S2->S3) | S2-p0 | Q7 | 62400 | 12480 |
| s45(id=37 S2->S3) | sw08-p4 | Q7 | 350080 | 12480 |
| s45(id=37 S2->S3) | sw06-p3 | Q7 | 366720 | 12480 |
| s45(id=37 S2->S3) | sw03-p3 | Q7 | 383360 | 12480 |
| s45(id=37 S2->S3) | sw01-p3 | Q7 | 449920 | 12480 |
| s48(id=40 S2->S1) | S2-p0 | Q6 | 227200 | 12480 |
| s48(id=40 S2->S1) | sw08-p5 | Q6 | 246400 | 12480 |
| s48(id=40 S2->S1) | sw07-p3 | Q6 | 263360 | 12480 |
| s48(id=40 S2->S1) | sw05-p5 | Q6 | 280320 | 12480 |
| s48(id=40 S2->S1) | sw02-p2 | Q6 | 296960 | 12480 |
| s49(id=41 S1->S2) | S1-p0 | Q7 | 62400 | 12480 |
| s49(id=41 S1->S2) | sw02-p5 | Q7 | 79040 | 12480 |
| s49(id=41 S1->S2) | sw05-p2 | Q7 | 150080 | 12480 |
| s49(id=41 S1->S2) | sw07-p4 | Q7 | 166720 | 12480 |
| s49(id=41 S1->S2) | sw08-p2 | Q7 | 213440 | 12480 |
| s57(id=49 S2->S1) | S2-p0 | Q6 | 242560 | 12480 |
| s57(id=49 S2->S1) | sw08-p5 | Q6 | 259520 | 12480 |
| s57(id=49 S2->S1) | sw07-p3 | Q6 | 276480 | 12480 |
| s57(id=49 S2->S1) | sw05-p5 | Q6 | 293120 | 12480 |
| s57(id=49 S2->S1) | sw02-p2 | Q6 | 309760 | 12480 |

## Constraint check

- C1-C7, C9: OK
- window-boundary integrity (no window's psi/delta changed anywhere): OK

## GCL per egress port

### sw01-p3  (16 entries, util 12.4800 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 1280 0x3F # 00111111   BE
sgs 259200 0x40 # 01000000   Q6
sgs 31040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 46080 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 1280 0x3F # 00111111   BE
sgs 163200 0x40 # 01000000   Q6
sgs 27200 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p4  (24 entries, util 12.4800 %)

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

### sw01-p5  (16 entries, util 6.2400 %)

```
sgs 41600 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 46080 0xBF # 10111111   Q7
sgs 46080 0x7F # 01111111   Q6
sgs 140480 0x80 # 10000000   Q7
sgs 13440 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 46080 0xBF # 10111111   Q7
sgs 46080 0x7F # 01111111   Q6
sgs 98880 0x80 # 10000000   Q7
sgs 55040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (31 entries, util 29.6400 %)

```
sgs 58240 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 19840 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 8960 0x3F # 00111111   BE
sgs 62400 0x80 # 10000000   Q7
sgs 24640 0x7F # 01111111   Q6
sgs 21120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 640 0x3F # 00111111   BE
sgs 128320 0x40 # 01000000   Q6
sgs 45760 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 19840 0x7F # 01111111   Q6
sgs 108800 0x80 # 10000000   Q7
sgs 24640 0x7F # 01111111   Q6
sgs 21120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 640 0x3F # 00111111   BE
sgs 70080 0x40 # 01000000   Q6
sgs 45760 0xBF # 10111111   Q7
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

### sw02-p5  (24 entries, util 24.9600 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 58240 0x80 # 10000000   Q7
sgs 46400 0x7F # 01111111   Q6
sgs 24000 0x40 # 01000000   Q6
sgs 29760 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 128640 0x80 # 10000000   Q7
sgs 29760 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 58240 0x80 # 10000000   Q7
sgs 46400 0x7F # 01111111   Q6
sgs 24000 0x40 # 01000000   Q6
sgs 29760 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 112000 0x80 # 10000000   Q7
sgs 46400 0xBF # 10111111   Q7
```

### sw03-p3  (15 entries, util 9.3600 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 29440 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 232320 0x40 # 01000000   Q6
sgs 25600 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 29440 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 152960 0x40 # 01000000   Q6
sgs 55040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (19 entries, util 12.4800 %)

```
sgs 39040 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 31680 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
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

### sw05-p2  (30 entries, util 24.9600 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 36480 0xBF # 10111111   Q7
sgs 23040 0x40 # 01000000   Q6
sgs 19840 0x7F # 01111111   Q6
sgs 30080 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 40640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 36480 0xBF # 10111111   Q7
sgs 76160 0x40 # 01000000   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 36480 0xBF # 10111111   Q7
sgs 76160 0x40 # 01000000   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 36480 0xBF # 10111111   Q7
sgs 42880 0x40 # 01000000   Q6
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

### sw05-p5  (23 entries, util 23.4000 %)

```
sgs 54400 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 20160 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 70400 0x40 # 01000000   Q6
sgs 59200 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 128000 0x40 # 01000000   Q6
sgs 59200 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 20160 0xBF # 10111111   Q7
sgs 95360 0x80 # 10000000   Q7
sgs 59200 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 73600 0x40 # 01000000   Q6
sgs 59200 0xBF # 10111111   Q7
```

### sw06-p2  (23 entries, util 12.4800 %)

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

### sw06-p3  (13 entries, util 9.3600 %)

```
sgs 60800 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 1280 0x3F # 00111111   BE
sgs 231360 0x40 # 01000000   Q6
sgs 44160 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 60800 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 1280 0x3F # 00111111   BE
sgs 170560 0x40 # 01000000   Q6
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

### sw07-p3  (22 entries, util 23.4000 %)

```
sgs 37760 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 20480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 70400 0x40 # 01000000   Q6
sgs 21440 0xBF # 10111111   Q7
sgs 37760 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 128320 0x40 # 01000000   Q6
sgs 21440 0xBF # 10111111   Q7
sgs 37760 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 20480 0xBF # 10111111   Q7
sgs 95360 0x80 # 10000000   Q7
sgs 21440 0xBF # 10111111   Q7
sgs 37760 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 90560 0x40 # 01000000   Q6
sgs 59200 0xBF # 10111111   Q7
```

### sw07-p4  (27 entries, util 24.9600 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0xBF # 10111111   Q7
sgs 13760 0x80 # 10000000   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 45120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 40640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0xBF # 10111111   Q7
sgs 13760 0x80 # 10000000   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 60800 0x40 # 01000000   Q6
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0xBF # 10111111   Q7
sgs 13760 0x80 # 10000000   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 60800 0x40 # 01000000   Q6
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0xBF # 10111111   Q7
sgs 13760 0x80 # 10000000   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 48320 0xBF # 10111111   Q7
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

### sw08-p2  (35 entries, util 37.4400 %)

```
sgs 66560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 36800 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 41600 0x40 # 01000000   Q6
sgs 30400 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 40640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 51520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 97920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 36800 0x80 # 10000000   Q7
sgs 27200 0x3F # 00111111   BE
sgs 54400 0x40 # 01000000   Q6
sgs 56000 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 51520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 31360 0x3F # 00111111   BE
```

### sw08-p4  (13 entries, util 9.3600 %)

```
sgs 43840 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 640 0x3F # 00111111   BE
sgs 232000 0x40 # 01000000   Q6
sgs 61120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 43840 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 640 0x3F # 00111111   BE
sgs 188160 0x40 # 01000000   Q6
sgs 55040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (26 entries, util 23.4000 %)

```
sgs 17280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 1280 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 23040 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 66560 0x40 # 01000000   Q6
sgs 41920 0xBF # 10111111   Q7
sgs 17280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 1280 0x3F # 00111111   BE
sgs 127040 0x40 # 01000000   Q6
sgs 41920 0xBF # 10111111   Q7
sgs 17280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 1280 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 23040 0xBF # 10111111   Q7
sgs 91520 0x80 # 10000000   Q7
sgs 41920 0xBF # 10111111   Q7
sgs 17280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 1280 0x3F # 00111111   BE
sgs 109760 0x40 # 01000000   Q6
sgs 59200 0xBF # 10111111   Q7
```

