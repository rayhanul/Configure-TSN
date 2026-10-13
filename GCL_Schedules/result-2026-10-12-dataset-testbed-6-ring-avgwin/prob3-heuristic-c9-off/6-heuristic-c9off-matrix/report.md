# Reconfiguration-free admission (Problem 3)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Frozen schedule W loaded from: **result/result-2026-10-12-dataset-testbed-6-ring-avgwin/heuristic-c9-off/6-matrix-c9off**

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
| 15 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 12480 | 200000 | - | - |
| 18 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 5 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 13 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 77120 | 185280 | - | - |
| 8 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 62400 | 500160 | - | - |
| 11 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 17 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 150080 | 429120 | - | - |
| 10 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q6 | 37760 | 45760 | - | - |
| 27 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q6 | 50560 | 45760 | - | - |
| 37 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 39 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q6 | 63360 | 45760 | - | - |
| 43 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 47 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 25 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q6 | 12480 | 150080 | - | - |
| 36 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 212800 | 95680 | - | - |
| 40 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q6 | 100160 | 128960 | - | - |
| 32 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q6 | 112640 | 116480 | - | - |
| 35 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 38 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 37440 | 191680 | - | - |
| 45 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q6 | 300160 | 45760 | - | - |
| 46 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 29 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 50 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 212800 | 79040 | - | - |
| 22 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 96320 | 149440 | - | - |
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
| sw01-p2 | 10 | 10 | 255 |
| sw01-p4 | 18 | 18 | 255 |
| sw01-p5 | 29 | 29 | 255 |
| sw02-p2 | 27 | 27 | 255 |
| sw02-p4 | 21 | 21 | 255 |
| sw02-p5 | 9 | 9 | 255 |
| sw03-p4 | 18 | 18 | 255 |
| sw03-p5 | 22 | 22 | 255 |
| sw04-p4 | 19 | 19 | 255 |
| sw04-p5 | 18 | 18 | 255 |
| sw05-p4 | 19 | 19 | 255 |
| sw05-p5 | 18 | 18 | 255 |
| sw06-p4 | 18 | 18 | 255 |
| sw06-p5 | 19 | 19 | 255 |
| sw07-p4 | 18 | 18 | 255 |
| sw07-p5 | 18 | 18 | 255 |
| sw08-p2 | 29 | 29 | 255 |
| sw08-p4 | 22 | 22 | 255 |
| sw08-p5 | 18 | 18 | 255 |

## Per-hop windows used by newly admitted flows

| flow | egress port | queue | psi (ns, unchanged) | delta (ns, unchanged) |
|---|---|---|---|---|
| s26(id=15 S2->S3) | S2-p0 | Q6 | 12480 | 12480 |
| s26(id=15 S2->S3) | sw08-p5 | Q6 | 29120 | 12480 |
| s26(id=15 S2->S3) | sw07-p4 | Q6 | 100160 | 12480 |
| s26(id=15 S2->S3) | sw05-p5 | Q6 | 116800 | 12480 |
| s26(id=15 S2->S3) | sw03-p4 | Q6 | 133440 | 12480 |
| s26(id=15 S2->S3) | sw01-p2 | Q6 | 150080 | 12480 |
| s25(id=13 S1->S2) | S1-p0 | Q7 | 77120 | 12480 |
| s25(id=13 S1->S2) | sw02-p4 | Q7 | 150080 | 12480 |
| s25(id=13 S1->S2) | sw04-p5 | Q7 | 166720 | 12480 |
| s25(id=13 S1->S2) | sw06-p4 | Q7 | 183360 | 12480 |
| s25(id=13 S1->S2) | sw08-p2 | Q7 | 249920 | 12480 |
| s22(id=8 S2->S3) | S2-p0 | Q7 | 62400 | 12480 |
| s22(id=8 S2->S3) | sw08-p5 | Q7 | 79040 | 12480 |
| s22(id=8 S2->S3) | sw07-p4 | Q7 | 150080 | 12480 |
| s22(id=8 S2->S3) | sw05-p5 | Q7 | 166720 | 12480 |
| s22(id=8 S2->S3) | sw03-p4 | Q7 | 183360 | 12480 |
| s22(id=8 S2->S3) | sw01-p2 | Q7 | 550080 | 12480 |
| s28(id=17 S2->S3) | S2-p0 | Q7 | 150080 | 12480 |
| s28(id=17 S2->S3) | sw08-p5 | Q7 | 166720 | 12480 |
| s28(id=17 S2->S3) | sw07-p4 | Q7 | 183360 | 12480 |
| s28(id=17 S2->S3) | sw05-p5 | Q7 | 249920 | 12480 |
| s28(id=17 S2->S3) | sw03-p4 | Q7 | 550080 | 12480 |
| s28(id=17 S2->S3) | sw01-p2 | Q7 | 566720 | 12480 |
| s23(id=10 S1->S3) | S1-p0 | Q6 | 37760 | 12480 |
| s23(id=10 S1->S3) | sw02-p5 | Q6 | 54400 | 12480 |
| s23(id=10 S1->S3) | sw01-p2 | Q6 | 71040 | 12480 |
| s36(id=27 S1->S3) | S1-p0 | Q6 | 50560 | 12480 |
| s36(id=27 S1->S3) | sw02-p5 | Q6 | 67200 | 12480 |
| s36(id=27 S1->S3) | sw01-p2 | Q6 | 83840 | 12480 |
| s48(id=39 S1->S3) | S1-p0 | Q6 | 63360 | 12480 |
| s48(id=39 S1->S3) | sw02-p5 | Q6 | 80000 | 12480 |
| s48(id=39 S1->S3) | sw01-p2 | Q6 | 96640 | 12480 |
| s34(id=25 S1->S2) | S1-p0 | Q6 | 12480 | 12480 |
| s34(id=25 S1->S2) | sw02-p4 | Q6 | 100160 | 12480 |
| s34(id=25 S1->S2) | sw04-p5 | Q6 | 116800 | 12480 |
| s34(id=25 S1->S2) | sw06-p4 | Q6 | 133440 | 12480 |
| s34(id=25 S1->S2) | sw08-p2 | Q6 | 150080 | 12480 |
| s45(id=36 S2->S1) | S2-p0 | Q7 | 212800 | 12480 |
| s45(id=36 S2->S1) | sw08-p4 | Q7 | 229440 | 12480 |
| s45(id=36 S2->S1) | sw06-p5 | Q7 | 246080 | 12480 |
| s45(id=36 S2->S1) | sw04-p4 | Q7 | 279360 | 12480 |
| s45(id=36 S2->S1) | sw02-p2 | Q7 | 296000 | 12480 |
| s49(id=40 S1->S2) | S1-p0 | Q6 | 100160 | 12480 |
| s49(id=40 S1->S2) | sw02-p4 | Q6 | 116800 | 12480 |
| s49(id=40 S1->S2) | sw04-p5 | Q6 | 133440 | 12480 |
| s49(id=40 S1->S2) | sw06-p4 | Q6 | 200000 | 12480 |
| s49(id=40 S1->S2) | sw08-p2 | Q6 | 216640 | 12480 |
| s41(id=32 S1->S3) | S1-p0 | Q6 | 112640 | 12480 |
| s41(id=32 S1->S3) | sw02-p5 | Q6 | 146240 | 12480 |
| s41(id=32 S1->S3) | sw01-p2 | Q6 | 162880 | 12480 |
| s47(id=38 S2->S3) | S2-p0 | Q6 | 37440 | 12480 |
| s47(id=38 S2->S3) | sw08-p5 | Q6 | 100160 | 12480 |
| s47(id=38 S2->S3) | sw07-p4 | Q6 | 116800 | 12480 |
| s47(id=38 S2->S3) | sw05-p5 | Q6 | 133440 | 12480 |
| s47(id=38 S2->S3) | sw03-p4 | Q6 | 200000 | 12480 |
| s47(id=38 S2->S3) | sw01-p2 | Q6 | 216640 | 12480 |
| s54(id=45 S1->S3) | S1-p0 | Q6 | 300160 | 12480 |
| s54(id=45 S1->S3) | sw02-p5 | Q6 | 316800 | 12480 |
| s54(id=45 S1->S3) | sw01-p2 | Q6 | 333440 | 12480 |
| s59(id=50 S1->S2) | S1-p0 | Q7 | 212800 | 12480 |
| s59(id=50 S1->S2) | sw02-p4 | Q7 | 229440 | 12480 |
| s59(id=50 S1->S2) | sw04-p5 | Q7 | 246080 | 12480 |
| s59(id=50 S1->S2) | sw06-p4 | Q7 | 262720 | 12480 |
| s59(id=50 S1->S2) | sw08-p2 | Q7 | 279360 | 12480 |
| s31(id=22 S2->S3) | S2-p0 | Q6 | 96320 | 12480 |
| s31(id=22 S2->S3) | sw08-p5 | Q6 | 112960 | 12480 |
| s31(id=22 S2->S3) | sw07-p4 | Q6 | 129600 | 12480 |
| s31(id=22 S2->S3) | sw05-p5 | Q6 | 200000 | 12480 |
| s31(id=22 S2->S3) | sw03-p4 | Q6 | 216640 | 12480 |
| s31(id=22 S2->S3) | sw01-p2 | Q6 | 233280 | 12480 |

## Constraint check

- C1-C7, C9: OK
- window-boundary integrity (no window's psi/delta changed anywhere): OK

## GCL per egress port

### sw01-p2  (10 entries, util 23.4000 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 8320 0x3F # 00111111   BE
sgs 479360 0x40 # 01000000   Q6
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

### sw01-p5  (29 entries, util 15.6000 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 63680 0x80 # 10000000   Q7
sgs 44480 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 88960 0x80 # 10000000   Q7
sgs 44480 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 63680 0x80 # 10000000   Q7
sgs 44480 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 72320 0x80 # 10000000   Q7
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (27 entries, util 29.6400 %)

```
sgs 33280 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x3F # 00111111   BE
sgs 29120 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 38080 0x40 # 01000000   Q6
sgs 73600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x3F # 00111111   BE
sgs 56640 0x80 # 10000000   Q7
sgs 110080 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x3F # 00111111   BE
sgs 29120 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 17920 0x80 # 10000000   Q7
sgs 106560 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x3F # 00111111   BE
sgs 34560 0x80 # 10000000   Q7
sgs 98880 0x3F # 00111111   BE
```

### sw02-p4  (21 entries, util 15.6000 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 75200 0x80 # 10000000   Q7
sgs 8320 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 75200 0x80 # 10000000   Q7
sgs 8320 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 75200 0x80 # 10000000   Q7
sgs 8320 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 58560 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p5  (9 entries, util 12.4800 %)

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

### sw04-p4  (19 entries, util 14.0400 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 37120 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 47360 0x40 # 01000000   Q6
sgs 27840 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 122240 0x80 # 10000000   Q7
sgs 27840 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 96960 0x40 # 01000000   Q6
sgs 27840 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 72320 0x80 # 10000000   Q7
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (18 entries, util 15.6000 %)

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

### sw06-p4  (18 entries, util 15.6000 %)

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

### sw06-p5  (19 entries, util 14.0400 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0x3F # 00111111   BE
sgs 37120 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 47360 0x40 # 01000000   Q6
sgs 44480 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 122240 0x80 # 10000000   Q7
sgs 44480 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0x3F # 00111111   BE
sgs 96960 0x40 # 01000000   Q6
sgs 44480 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 88960 0x80 # 10000000   Q7
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

### sw08-p2  (29 entries, util 21.8400 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 21120 0xBF # 10111111   Q7
sgs 8000 0x3F # 00111111   BE
sgs 80640 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 21120 0xBF # 10111111   Q7
sgs 8000 0x3F # 00111111   BE
sgs 80640 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 21120 0xBF # 10111111   Q7
sgs 8000 0x3F # 00111111   BE
sgs 80640 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 21120 0xBF # 10111111   Q7
sgs 8000 0x3F # 00111111   BE
sgs 14080 0x40 # 01000000   Q6
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p4  (22 entries, util 14.0400 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0x7F # 01111111   Q6
sgs 37120 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 47360 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 122240 0x80 # 10000000   Q7
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0x7F # 01111111   Q6
sgs 96960 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 105600 0x80 # 10000000   Q7
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

