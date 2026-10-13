# Reconfiguration-free admission (Problem 3)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Frozen schedule W loaded from: **result/result-2026-10-13-dataset-testbed-13-tree-avgwin/heuristic-c9-off/13-matrix-c9off**

## Admission: W (before) vs. after this run's arrivals

| | admitted | of total |
|---|---|---|
| W (base, unchanged) | 11 | 11 |
| + this run's arrivals | 12 | 39 |

Every arrival admitted here required **zero** window-boundary changes -- see the GCL-entry table below (unchanged from W by construction) and the window-boundary integrity check. No previously-admitted flow was rerouted.

## Arrivals

| id | src->dst | RS(s) size | admitted | route | queue | phi_s (ns) | e2e (ns) | rerouted to make room | reason if rejected |
|---|---|---|---|---|---|---|---|---|---|
| 7 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 16 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 11 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 1 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q6 | 75200 | 95680 | - | - |
| 12 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 18 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 6 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q7 | 49920 | 412480 | - | - |
| 4 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 2 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 150080 | 312320 | - | - |
| 32 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 112320 | 150080 | - | - |
| 40 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 42 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 49 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 437760 | 224640 | - | - |
| 22 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 48 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 | 150080 | 612480 | - | - |
| 26 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q6 | 88000 | 203840 | - | - |
| 31 | S1->S3 | - | yes | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 70080 | 151680 | - | - |
| 37 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q6 | 111040 | 201280 | - | - |
| 44 | S1->S3 | - | yes | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 82880 | 151680 | - | - |
| 25 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 36 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 41 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q6 | 111040 | 134720 | - | - |
| 45 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q6 | 212800 | 95680 | - | - |
| 23 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 24 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 29 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 38 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 46 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 47 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 30 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 34 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 35 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 39 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 21 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 28 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 33 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 43 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 50 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 27 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |

## Per-port GCL entries (should equal W exactly)

| port | W entries | after arrivals | GCL_size |
|---|---|---|---|
| sw01-p2 | 32 | 32 | 255 |
| sw01-p4 | 25 | 25 | 255 |
| sw02-p2 | 24 | 24 | 255 |
| sw02-p4 | 22 | 22 | 255 |
| sw03-p4 | 26 | 26 | 255 |
| sw03-p5 | 22 | 22 | 255 |
| sw04-p4 | 21 | 21 | 255 |
| sw04-p5 | 22 | 22 | 255 |
| sw05-p4 | 20 | 20 | 255 |
| sw05-p5 | 28 | 28 | 255 |
| sw06-p4 | 20 | 20 | 255 |
| sw06-p5 | 23 | 23 | 255 |
| sw07-p4 | 31 | 31 | 255 |
| sw07-p5 | 26 | 26 | 255 |
| sw08-p2 | 23 | 23 | 255 |
| sw08-p4 | 23 | 23 | 255 |
| sw08-p5 | 25 | 25 | 255 |

## Per-hop windows used by newly admitted flows

| flow | egress port | queue | psi (ns, unchanged) | delta (ns, unchanged) |
|---|---|---|---|---|
| s20(id=1 S3->S2) | S3-p0 | Q6 | 75200 | 12480 |
| s20(id=1 S3->S2) | sw01-p4 | Q6 | 91840 | 12480 |
| s20(id=1 S3->S2) | sw03-p5 | Q6 | 108480 | 12480 |
| s20(id=1 S3->S2) | sw05-p4 | Q6 | 125120 | 12480 |
| s20(id=1 S3->S2) | sw07-p5 | Q6 | 141760 | 12480 |
| s20(id=1 S3->S2) | sw08-p2 | Q6 | 158400 | 12480 |
| s23(id=6 S3->S1) | S3-p0 | Q7 | 49920 | 12480 |
| s23(id=6 S3->S1) | sw01-p4 | Q7 | 66560 | 12480 |
| s23(id=6 S3->S1) | sw03-p5 | Q7 | 83200 | 12480 |
| s23(id=6 S3->S1) | sw05-p4 | Q7 | 170880 | 12480 |
| s23(id=6 S3->S1) | sw07-p5 | Q7 | 187520 | 12480 |
| s23(id=6 S3->S1) | sw08-p4 | Q7 | 350080 | 12480 |
| s23(id=6 S3->S1) | sw06-p5 | Q7 | 366720 | 12480 |
| s23(id=6 S3->S1) | sw04-p4 | Q7 | 383360 | 12480 |
| s23(id=6 S3->S1) | sw02-p2 | Q7 | 449920 | 12480 |
| s21(id=2 S1->S2) | S1-p0 | Q7 | 150080 | 12480 |
| s21(id=2 S1->S2) | sw02-p4 | Q7 | 166720 | 12480 |
| s21(id=2 S1->S2) | sw04-p5 | Q7 | 183360 | 12480 |
| s21(id=2 S1->S2) | sw06-p4 | Q7 | 360960 | 12480 |
| s21(id=2 S1->S2) | sw08-p2 | Q7 | 449920 | 12480 |
| s40(id=32 S2->S1) | S2-p0 | Q7 | 112320 | 12480 |
| s40(id=32 S2->S1) | sw08-p4 | Q7 | 150080 | 12480 |
| s40(id=32 S2->S1) | sw06-p5 | Q7 | 166720 | 12480 |
| s40(id=32 S2->S1) | sw04-p4 | Q7 | 183360 | 12480 |
| s40(id=32 S2->S1) | sw02-p2 | Q7 | 249920 | 12480 |
| s57(id=49 S1->S2) | S1-p0 | Q7 | 437760 | 12480 |
| s57(id=49 S1->S2) | sw02-p4 | Q7 | 454400 | 12480 |
| s57(id=49 S1->S2) | sw04-p5 | Q7 | 471040 | 12480 |
| s57(id=49 S1->S2) | sw06-p4 | Q7 | 487680 | 12480 |
| s57(id=49 S1->S2) | sw08-p2 | Q7 | 649920 | 12480 |
| s56(id=48 S3->S2) | S3-p0 | Q7 | 150080 | 12480 |
| s56(id=48 S3->S2) | sw01-p4 | Q7 | 166720 | 12480 |
| s56(id=48 S3->S2) | sw03-p5 | Q7 | 183360 | 12480 |
| s56(id=48 S3->S2) | sw05-p4 | Q7 | 370880 | 12480 |
| s56(id=48 S3->S2) | sw07-p5 | Q7 | 649920 | 12480 |
| s56(id=48 S3->S2) | sw08-p2 | Q7 | 750080 | 12480 |
| s34(id=26 S3->S1) | S3-p0 | Q6 | 88000 | 12480 |
| s34(id=26 S3->S1) | sw01-p4 | Q6 | 104640 | 12480 |
| s34(id=26 S3->S1) | sw03-p5 | Q6 | 121280 | 12480 |
| s34(id=26 S3->S1) | sw05-p4 | Q6 | 137920 | 12480 |
| s34(id=26 S3->S1) | sw07-p5 | Q6 | 212800 | 12480 |
| s34(id=26 S3->S1) | sw08-p4 | Q6 | 229440 | 12480 |
| s34(id=26 S3->S1) | sw06-p5 | Q6 | 246080 | 12480 |
| s34(id=26 S3->S1) | sw04-p4 | Q6 | 262720 | 12480 |
| s34(id=26 S3->S1) | sw02-p2 | Q6 | 279360 | 12480 |
| s39(id=31 S1->S3) | S1-p0 | Q6 | 70080 | 12480 |
| s39(id=31 S1->S3) | sw02-p4 | Q6 | 86720 | 12480 |
| s39(id=31 S1->S3) | sw04-p5 | Q6 | 109440 | 12480 |
| s39(id=31 S1->S3) | sw06-p4 | Q6 | 126080 | 12480 |
| s39(id=31 S1->S3) | sw08-p5 | Q6 | 142720 | 12480 |
| s39(id=31 S1->S3) | sw07-p4 | Q6 | 159360 | 12480 |
| s39(id=31 S1->S3) | sw05-p5 | Q6 | 176000 | 12480 |
| s39(id=31 S1->S3) | sw03-p4 | Q6 | 192640 | 12480 |
| s39(id=31 S1->S3) | sw01-p2 | Q6 | 209280 | 12480 |
| s45(id=37 S3->S1) | S3-p0 | Q6 | 111040 | 12480 |
| s45(id=37 S3->S1) | sw01-p4 | Q6 | 137600 | 12480 |
| s45(id=37 S3->S1) | sw03-p5 | Q6 | 200000 | 12480 |
| s45(id=37 S3->S1) | sw05-p4 | Q6 | 216640 | 12480 |
| s45(id=37 S3->S1) | sw07-p5 | Q6 | 233280 | 12480 |
| s45(id=37 S3->S1) | sw08-p4 | Q6 | 249920 | 12480 |
| s45(id=37 S3->S1) | sw06-p5 | Q6 | 266560 | 12480 |
| s45(id=37 S3->S1) | sw04-p4 | Q6 | 283200 | 12480 |
| s45(id=37 S3->S1) | sw02-p2 | Q6 | 299840 | 12480 |
| s52(id=44 S1->S3) | S1-p0 | Q6 | 82880 | 12480 |
| s52(id=44 S1->S3) | sw02-p4 | Q6 | 105600 | 12480 |
| s52(id=44 S1->S3) | sw04-p5 | Q6 | 122240 | 12480 |
| s52(id=44 S1->S3) | sw06-p4 | Q6 | 138880 | 12480 |
| s52(id=44 S1->S3) | sw08-p5 | Q6 | 155520 | 12480 |
| s52(id=44 S1->S3) | sw07-p4 | Q6 | 172160 | 12480 |
| s52(id=44 S1->S3) | sw05-p5 | Q6 | 188800 | 12480 |
| s52(id=44 S1->S3) | sw03-p4 | Q6 | 205440 | 12480 |
| s52(id=44 S1->S3) | sw01-p2 | Q6 | 222080 | 12480 |
| s49(id=41 S1->S2) | S1-p0 | Q6 | 111040 | 12480 |
| s49(id=41 S1->S2) | sw02-p4 | Q6 | 127680 | 12480 |
| s49(id=41 S1->S2) | sw04-p5 | Q6 | 200000 | 12480 |
| s49(id=41 S1->S2) | sw06-p4 | Q6 | 216640 | 12480 |
| s49(id=41 S1->S2) | sw08-p2 | Q6 | 233280 | 12480 |
| s53(id=45 S3->S2) | S3-p0 | Q6 | 212800 | 12480 |
| s53(id=45 S3->S2) | sw01-p4 | Q6 | 229440 | 12480 |
| s53(id=45 S3->S2) | sw03-p5 | Q6 | 246080 | 12480 |
| s53(id=45 S3->S2) | sw05-p4 | Q6 | 262720 | 12480 |
| s53(id=45 S3->S2) | sw07-p5 | Q6 | 279360 | 12480 |
| s53(id=45 S3->S2) | sw08-p2 | Q6 | 296000 | 12480 |

## Constraint check

- C1-C7, C9: OK
- window-boundary integrity (no window's psi/delta changed anywhere): OK

## GCL per egress port

### sw01-p2  (32 entries, util 18.7200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 8000 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 29440 0x7F # 01111111   Q6
sgs 8000 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 50560 0x40 # 01000000   Q6
sgs 2880 0x3F # 00111111   BE
sgs 50240 0xBF # 10111111   Q7
sgs 8000 0x3F # 00111111   BE
sgs 138880 0x40 # 01000000   Q6
sgs 2880 0x3F # 00111111   BE
sgs 50240 0xBF # 10111111   Q7
sgs 8000 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 29440 0x7F # 01111111   Q6
sgs 8000 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 76160 0x40 # 01000000   Q6
sgs 2880 0x3F # 00111111   BE
sgs 50240 0xBF # 10111111   Q7
sgs 8000 0x3F # 00111111   BE
sgs 30720 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p4  (25 entries, util 23.4000 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 58560 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 120960 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 4160 0x3F # 00111111   BE
sgs 83520 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 104320 0x40 # 01000000   Q6
sgs 29120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (24 entries, util 15.6000 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 21120 0xBF # 10111111   Q7
sgs 16320 0x7F # 01111111   Q6
sgs 46720 0x80 # 10000000   Q7
sgs 36800 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 96640 0x40 # 01000000   Q6
sgs 36800 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 21120 0xBF # 10111111   Q7
sgs 16320 0x7F # 01111111   Q6
sgs 46720 0x80 # 10000000   Q7
sgs 36800 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 30080 0x40 # 01000000   Q6
sgs 3520 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p4  (22 entries, util 20.2800 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 19840 0xBF # 10111111   Q7
sgs 53760 0x40 # 01000000   Q6
sgs 22400 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 111040 0x40 # 01000000   Q6
sgs 22400 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 86080 0x80 # 10000000   Q7
sgs 22400 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 94400 0x40 # 01000000   Q6
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (26 entries, util 18.7200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 50560 0x40 # 01000000   Q6
sgs 19520 0x7F # 01111111   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 138880 0x40 # 01000000   Q6
sgs 19520 0x7F # 01111111   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 76160 0x40 # 01000000   Q6
sgs 19520 0x7F # 01111111   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 47360 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p5  (22 entries, util 23.4000 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 20800 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 58560 0x40 # 01000000   Q6
sgs 45760 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 120960 0x40 # 01000000   Q6
sgs 45760 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 20800 0xBF # 10111111   Q7
sgs 83520 0x40 # 01000000   Q6
sgs 45760 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 87680 0x40 # 01000000   Q6
sgs 29120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p4  (21 entries, util 15.6000 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0xBF # 10111111   Q7
sgs 46720 0x80 # 10000000   Q7
sgs 3520 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 96640 0x40 # 01000000   Q6
sgs 3520 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0xBF # 10111111   Q7
sgs 46720 0x80 # 10000000   Q7
sgs 3520 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 46720 0x40 # 01000000   Q6
sgs 3520 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (22 entries, util 20.2800 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 19840 0xBF # 10111111   Q7
sgs 53760 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 111040 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 86080 0x80 # 10000000   Q7
sgs 5760 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 77760 0x40 # 01000000   Q6
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (20 entries, util 23.4000 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 58560 0x40 # 01000000   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 120960 0x40 # 01000000   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 83520 0x40 # 01000000   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 71040 0x40 # 01000000   Q6
sgs 29120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p5  (28 entries, util 18.7200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12800 0xBF # 10111111   Q7
sgs 24640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 50560 0x40 # 01000000   Q6
sgs 36160 0x7F # 01111111   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 138880 0x40 # 01000000   Q6
sgs 36160 0x7F # 01111111   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12800 0xBF # 10111111   Q7
sgs 24640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 76160 0x40 # 01000000   Q6
sgs 36160 0x7F # 01111111   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 64000 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p4  (20 entries, util 20.2800 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 13120 0x7F # 01111111   Q6
sgs 47680 0x40 # 01000000   Q6
sgs 39040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 111040 0x40 # 01000000   Q6
sgs 39040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 86080 0x80 # 10000000   Q7
sgs 39040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 61120 0x40 # 01000000   Q6
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (23 entries, util 15.6000 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 33280 0xBF # 10111111   Q7
sgs 46720 0x80 # 10000000   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 96640 0x40 # 01000000   Q6
sgs 20160 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 33280 0xBF # 10111111   Q7
sgs 46720 0x80 # 10000000   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 63360 0x40 # 01000000   Q6
sgs 3520 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (31 entries, util 18.7200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 29440 0xBF # 10111111   Q7
sgs 8000 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 50560 0x40 # 01000000   Q6
sgs 2880 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 8320 0x3F # 00111111   BE
sgs 138880 0x40 # 01000000   Q6
sgs 2880 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 29440 0xBF # 10111111   Q7
sgs 8000 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 76160 0x40 # 01000000   Q6
sgs 2880 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 8320 0x3F # 00111111   BE
sgs 80640 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p5  (26 entries, util 23.4000 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 21120 0xBF # 10111111   Q7
sgs 3840 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 58560 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 120960 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 21120 0xBF # 10111111   Q7
sgs 3840 0x3F # 00111111   BE
sgs 83520 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 54400 0x40 # 01000000   Q6
sgs 29120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p2  (23 entries, util 31.2000 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 29120 0x40 # 01000000   Q6
sgs 4480 0x3F # 00111111   BE
sgs 20480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 70080 0x40 # 01000000   Q6
sgs 34240 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 149120 0x40 # 01000000   Q6
sgs 34240 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 29120 0x40 # 01000000   Q6
sgs 4480 0x3F # 00111111   BE
sgs 20480 0x7F # 01111111   Q6
sgs 95040 0x40 # 01000000   Q6
sgs 34240 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 82560 0x40 # 01000000   Q6
sgs 960 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p4  (23 entries, util 15.6000 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 46720 0x80 # 10000000   Q7
sgs 36800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 96640 0x40 # 01000000   Q6
sgs 36800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 46720 0x80 # 10000000   Q7
sgs 36800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 80000 0x40 # 01000000   Q6
sgs 3520 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (25 entries, util 18.7200 %)

```
sgs 41600 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 50560 0x40 # 01000000   Q6
sgs 19520 0xBF # 10111111   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 138880 0x40 # 01000000   Q6
sgs 19520 0xBF # 10111111   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 76160 0x40 # 01000000   Q6
sgs 19520 0xBF # 10111111   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 97280 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

