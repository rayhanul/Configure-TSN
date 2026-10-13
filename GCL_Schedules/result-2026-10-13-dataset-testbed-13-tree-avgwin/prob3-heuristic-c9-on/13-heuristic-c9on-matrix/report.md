# Reconfiguration-free admission (Problem 3)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Frozen schedule W loaded from: **result/result-2026-10-13-dataset-testbed-13-tree-avgwin/heuristic-c9-on/13-matrix-c9on**

## Admission: W (before) vs. after this run's arrivals

| | admitted | of total |
|---|---|---|
| W (base, unchanged) | 11 | 11 |
| + this run's arrivals | 14 | 39 |

Every arrival admitted here required **zero** window-boundary changes -- see the GCL-entry table below (unchanged from W by construction) and the window-boundary integrity check. No previously-admitted flow was rerouted.

## Arrivals

| id | src->dst | RS(s) size | admitted | route | queue | phi_s (ns) | e2e (ns) | rerouted to make room | reason if rejected |
|---|---|---|---|---|---|---|---|---|---|
| 7 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 16 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 11 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 1 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q6 | 111040 | 109120 | - | - |
| 12 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 18 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 6 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q7 | 49920 | 73920 | - | - |
| 4 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 2 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q6 | 12480 | 406080 | - | - |
| 32 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 40 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 42 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 49 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q6 | 37440 | 701120 | - | - |
| 22 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 48 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 | 74880 | 54080 | - | - |
| 26 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q7 | 87360 | 95360 | - | - |
| 31 | S1->S3 | - | yes | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 62400 | 419520 | - | - |
| 37 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q7 | 150080 | 236800 | - | - |
| 44 | S1->S3 | - | yes | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 437440 | 332800 | - | - |
| 25 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 36 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 41 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 74880 | 106880 | - | - |
| 45 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 | 162560 | 219200 | - | - |
| 23 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q6 | 123520 | 288960 | - | - |
| 24 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 29 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q6 | 212480 | 212480 | - | - |
| 38 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 46 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 47 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 30 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 87360 | 107200 | - | - |
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
| sw01-p2 | 25 | 25 | 255 |
| sw01-p4 | 22 | 22 | 255 |
| sw02-p2 | 23 | 23 | 255 |
| sw02-p4 | 20 | 20 | 255 |
| sw03-p4 | 21 | 21 | 255 |
| sw03-p5 | 22 | 22 | 255 |
| sw04-p4 | 23 | 23 | 255 |
| sw04-p5 | 20 | 20 | 255 |
| sw05-p4 | 24 | 24 | 255 |
| sw05-p5 | 21 | 21 | 255 |
| sw06-p4 | 21 | 21 | 255 |
| sw06-p5 | 23 | 23 | 255 |
| sw07-p4 | 23 | 23 | 255 |
| sw07-p5 | 22 | 22 | 255 |
| sw08-p2 | 28 | 28 | 255 |
| sw08-p4 | 23 | 23 | 255 |
| sw08-p5 | 21 | 21 | 255 |

## Per-hop windows used by newly admitted flows

| flow | egress port | queue | psi (ns, unchanged) | delta (ns, unchanged) |
|---|---|---|---|---|
| s20(id=1 S3->S2) | S3-p0 | Q6 | 111040 | 12480 |
| s20(id=1 S3->S2) | sw01-p4 | Q6 | 119360 | 12480 |
| s20(id=1 S3->S2) | sw03-p5 | Q6 | 127680 | 12480 |
| s20(id=1 S3->S2) | sw05-p4 | Q6 | 136000 | 12480 |
| s20(id=1 S3->S2) | sw07-p5 | Q6 | 200000 | 12480 |
| s20(id=1 S3->S2) | sw08-p2 | Q6 | 207680 | 12480 |
| s23(id=6 S3->S1) | S3-p0 | Q7 | 49920 | 12480 |
| s23(id=6 S3->S1) | sw01-p4 | Q7 | 57600 | 12480 |
| s23(id=6 S3->S1) | sw03-p5 | Q7 | 65280 | 12480 |
| s23(id=6 S3->S1) | sw05-p4 | Q7 | 72960 | 12480 |
| s23(id=6 S3->S1) | sw07-p5 | Q7 | 80640 | 12480 |
| s23(id=6 S3->S1) | sw08-p4 | Q7 | 88320 | 12480 |
| s23(id=6 S3->S1) | sw06-p5 | Q7 | 96000 | 12480 |
| s23(id=6 S3->S1) | sw04-p4 | Q7 | 103680 | 12480 |
| s23(id=6 S3->S1) | sw02-p2 | Q7 | 111360 | 12480 |
| s21(id=2 S1->S2) | S1-p0 | Q6 | 12480 | 12480 |
| s21(id=2 S1->S2) | sw02-p4 | Q6 | 18560 | 12480 |
| s21(id=2 S1->S2) | sw04-p5 | Q6 | 24640 | 12480 |
| s21(id=2 S1->S2) | sw06-p4 | Q6 | 400000 | 12480 |
| s21(id=2 S1->S2) | sw08-p2 | Q6 | 406080 | 12480 |
| s57(id=49 S1->S2) | S1-p0 | Q6 | 37440 | 12480 |
| s57(id=49 S1->S2) | sw02-p4 | Q6 | 117120 | 12480 |
| s57(id=49 S1->S2) | sw04-p5 | Q6 | 424640 | 12480 |
| s57(id=49 S1->S2) | sw06-p4 | Q6 | 720960 | 12480 |
| s57(id=49 S1->S2) | sw08-p2 | Q6 | 726080 | 12480 |
| s56(id=48 S3->S2) | S3-p0 | Q7 | 74880 | 12480 |
| s56(id=48 S3->S2) | sw01-p4 | Q7 | 83200 | 12480 |
| s56(id=48 S3->S2) | sw03-p5 | Q7 | 91520 | 12480 |
| s56(id=48 S3->S2) | sw05-p4 | Q7 | 99840 | 12480 |
| s56(id=48 S3->S2) | sw07-p5 | Q7 | 108160 | 12480 |
| s56(id=48 S3->S2) | sw08-p2 | Q7 | 116480 | 12480 |
| s34(id=26 S3->S1) | S3-p0 | Q7 | 87360 | 12480 |
| s34(id=26 S3->S1) | sw01-p4 | Q7 | 95680 | 12480 |
| s34(id=26 S3->S1) | sw03-p5 | Q7 | 104000 | 12480 |
| s34(id=26 S3->S1) | sw05-p4 | Q7 | 112320 | 12480 |
| s34(id=26 S3->S1) | sw07-p5 | Q7 | 120640 | 12480 |
| s34(id=26 S3->S1) | sw08-p4 | Q7 | 150080 | 12480 |
| s34(id=26 S3->S1) | sw06-p5 | Q7 | 156800 | 12480 |
| s34(id=26 S3->S1) | sw04-p4 | Q7 | 163520 | 12480 |
| s34(id=26 S3->S1) | sw02-p2 | Q7 | 170240 | 12480 |
| s39(id=31 S1->S3) | S1-p0 | Q7 | 62400 | 12480 |
| s39(id=31 S1->S3) | sw02-p4 | Q7 | 70080 | 12480 |
| s39(id=31 S1->S3) | sw04-p5 | Q7 | 77760 | 12480 |
| s39(id=31 S1->S3) | sw06-p4 | Q7 | 85440 | 12480 |
| s39(id=31 S1->S3) | sw08-p5 | Q7 | 169920 | 12480 |
| s39(id=31 S1->S3) | sw07-p4 | Q7 | 177600 | 12480 |
| s39(id=31 S1->S3) | sw05-p5 | Q7 | 185280 | 12480 |
| s39(id=31 S1->S3) | sw03-p4 | Q7 | 461760 | 12480 |
| s39(id=31 S1->S3) | sw01-p2 | Q7 | 469440 | 12480 |
| s45(id=37 S3->S1) | S3-p0 | Q7 | 150080 | 12480 |
| s45(id=37 S3->S1) | sw01-p4 | Q7 | 156160 | 12480 |
| s45(id=37 S3->S1) | sw03-p5 | Q7 | 162240 | 12480 |
| s45(id=37 S3->S1) | sw05-p4 | Q7 | 168320 | 12480 |
| s45(id=37 S3->S1) | sw07-p5 | Q7 | 350080 | 12480 |
| s45(id=37 S3->S1) | sw08-p4 | Q7 | 356160 | 12480 |
| s45(id=37 S3->S1) | sw06-p5 | Q7 | 362240 | 12480 |
| s45(id=37 S3->S1) | sw04-p4 | Q7 | 368320 | 12480 |
| s45(id=37 S3->S1) | sw02-p2 | Q7 | 374400 | 12480 |
| s52(id=44 S1->S3) | S1-p0 | Q7 | 437440 | 12480 |
| s52(id=44 S1->S3) | sw02-p4 | Q7 | 445120 | 12480 |
| s52(id=44 S1->S3) | sw04-p5 | Q7 | 452800 | 12480 |
| s52(id=44 S1->S3) | sw06-p4 | Q7 | 460480 | 12480 |
| s52(id=44 S1->S3) | sw08-p5 | Q7 | 468160 | 12480 |
| s52(id=44 S1->S3) | sw07-p4 | Q7 | 475840 | 12480 |
| s52(id=44 S1->S3) | sw05-p5 | Q7 | 483520 | 12480 |
| s52(id=44 S1->S3) | sw03-p4 | Q7 | 750080 | 12480 |
| s52(id=44 S1->S3) | sw01-p2 | Q7 | 757760 | 12480 |
| s49(id=41 S1->S2) | S1-p0 | Q7 | 74880 | 12480 |
| s49(id=41 S1->S2) | sw02-p4 | Q7 | 83200 | 12480 |
| s49(id=41 S1->S2) | sw04-p5 | Q7 | 91520 | 12480 |
| s49(id=41 S1->S2) | sw06-p4 | Q7 | 120960 | 12480 |
| s49(id=41 S1->S2) | sw08-p2 | Q7 | 129280 | 12480 |
| s53(id=45 S3->S2) | S3-p0 | Q7 | 162560 | 12480 |
| s53(id=45 S3->S2) | sw01-p4 | Q7 | 169280 | 12480 |
| s53(id=45 S3->S2) | sw03-p5 | Q7 | 176000 | 12480 |
| s53(id=45 S3->S2) | sw05-p4 | Q7 | 350080 | 12480 |
| s53(id=45 S3->S2) | sw07-p5 | Q7 | 362560 | 12480 |
| s53(id=45 S3->S2) | sw08-p2 | Q7 | 369280 | 12480 |
| s31(id=23 S3->S1) | S3-p0 | Q6 | 123520 | 12480 |
| s31(id=23 S3->S1) | sw01-p4 | Q6 | 131840 | 12480 |
| s31(id=23 S3->S1) | sw03-p5 | Q6 | 200000 | 12480 |
| s31(id=23 S3->S1) | sw05-p4 | Q6 | 207680 | 12480 |
| s31(id=23 S3->S1) | sw07-p5 | Q6 | 215360 | 12480 |
| s31(id=23 S3->S1) | sw08-p4 | Q6 | 303360 | 12480 |
| s31(id=23 S3->S1) | sw06-p5 | Q6 | 322880 | 12480 |
| s31(id=23 S3->S1) | sw04-p4 | Q6 | 330560 | 12480 |
| s31(id=23 S3->S1) | sw02-p2 | Q6 | 400000 | 12480 |
| s37(id=29 S3->S1) | S3-p0 | Q6 | 212480 | 12480 |
| s37(id=29 S3->S1) | sw01-p4 | Q6 | 220800 | 12480 |
| s37(id=29 S3->S1) | sw03-p5 | Q6 | 229120 | 12480 |
| s37(id=29 S3->S1) | sw05-p4 | Q6 | 237440 | 12480 |
| s37(id=29 S3->S1) | sw07-p5 | Q6 | 311040 | 12480 |
| s37(id=29 S3->S1) | sw08-p4 | Q6 | 330560 | 12480 |
| s37(id=29 S3->S1) | sw06-p5 | Q6 | 335680 | 12480 |
| s37(id=29 S3->S1) | sw04-p4 | Q6 | 400000 | 12480 |
| s37(id=29 S3->S1) | sw02-p2 | Q6 | 412480 | 12480 |
| s38(id=30 S1->S2) | S1-p0 | Q7 | 87360 | 12480 |
| s38(id=30 S1->S2) | sw02-p4 | Q7 | 95680 | 12480 |
| s38(id=30 S1->S2) | sw04-p5 | Q7 | 150080 | 12480 |
| s38(id=30 S1->S2) | sw06-p4 | Q7 | 156800 | 12480 |
| s38(id=30 S1->S2) | sw08-p2 | Q7 | 169280 | 12480 |

## Constraint check

- C1-C7, C9: OK
- window-boundary integrity (no window's psi/delta changed anywhere): OK

## GCL per egress port

### sw01-p2  (25 entries, util 18.7200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 5440 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 18560 0xBF # 10111111   Q7
sgs 25280 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 82240 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 5440 0x3F # 00111111   BE
sgs 138880 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 5440 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 18560 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0x3F # 00111111   BE
sgs 82240 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 5440 0x3F # 00111111   BE
sgs 83520 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p4  (22 entries, util 29.6400 %)

```
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 22720 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 14720 0xBF # 10111111   Q7
sgs 48640 0x80 # 10000000   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 8320 0x3F # 00111111   BE
sgs 111040 0x40 # 01000000   Q6
sgs 30720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 22720 0x7F # 01111111   Q6
sgs 75840 0x40 # 01000000   Q6
sgs 30720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 8320 0x3F # 00111111   BE
sgs 102720 0x40 # 01000000   Q6
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (23 entries, util 20.2800 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 10560 0x3F # 00111111   BE
sgs 33280 0xBF # 10111111   Q7
sgs 53120 0x80 # 10000000   Q7
sgs 13760 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 26880 0x7F # 01111111   Q6
sgs 109440 0x80 # 10000000   Q7
sgs 13760 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 26880 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 10560 0x3F # 00111111   BE
sgs 33280 0xBF # 10111111   Q7
sgs 53120 0x80 # 10000000   Q7
sgs 13760 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 26880 0x7F # 01111111   Q6
sgs 82560 0x80 # 10000000   Q7
sgs 40640 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p4  (20 entries, util 26.5200 %)

```
sgs 6080 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 14080 0x7F # 01111111   Q6
sgs 84480 0x80 # 10000000   Q7
sgs 32960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 6080 0x3F # 00111111   BE
sgs 111040 0x80 # 10000000   Q7
sgs 32960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 6080 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 14080 0x7F # 01111111   Q6
sgs 84480 0x80 # 10000000   Q7
sgs 32960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 6080 0x3F # 00111111   BE
sgs 104960 0x80 # 10000000   Q7
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (21 entries, util 18.7200 %)

```
sgs 49280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 16960 0xBF # 10111111   Q7
sgs 25280 0x80 # 10000000   Q7
sgs 1280 0x3F # 00111111   BE
sgs 82880 0x40 # 01000000   Q6
sgs 11840 0x3F # 00111111   BE
sgs 49280 0x7F # 01111111   Q6
sgs 138880 0x40 # 01000000   Q6
sgs 11840 0x3F # 00111111   BE
sgs 49280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 16960 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 14080 0x3F # 00111111   BE
sgs 82880 0x40 # 01000000   Q6
sgs 11840 0x3F # 00111111   BE
sgs 49280 0x7F # 01111111   Q6
sgs 89600 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p5  (22 entries, util 29.6400 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 20480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 16960 0xBF # 10111111   Q7
sgs 48640 0x80 # 10000000   Q7
sgs 22400 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 111040 0x40 # 01000000   Q6
sgs 22400 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 20480 0x7F # 01111111   Q6
sgs 78080 0x40 # 01000000   Q6
sgs 22400 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 94400 0x40 # 01000000   Q6
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p4  (23 entries, util 20.2800 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 7680 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 17280 0x7F # 01111111   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 54720 0x80 # 10000000   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 109440 0x80 # 10000000   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 17280 0x7F # 01111111   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 54720 0x80 # 10000000   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 89280 0x80 # 10000000   Q7
sgs 40640 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (20 entries, util 26.5200 %)

```
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 15680 0x7F # 01111111   Q6
sgs 82880 0x80 # 10000000   Q7
sgs 26880 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 12160 0x3F # 00111111   BE
sgs 111040 0x80 # 10000000   Q7
sgs 26880 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 15680 0x7F # 01111111   Q6
sgs 82880 0x80 # 10000000   Q7
sgs 26880 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 12160 0x3F # 00111111   BE
sgs 98880 0x80 # 10000000   Q7
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (24 entries, util 29.6400 %)

```
sgs 24960 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 5760 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 19200 0xBF # 10111111   Q7
sgs 48640 0x80 # 10000000   Q7
sgs 14080 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 111040 0x40 # 01000000   Q6
sgs 14080 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 5760 0x3F # 00111111   BE
sgs 80320 0x40 # 01000000   Q6
sgs 14080 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 86080 0x40 # 01000000   Q6
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p5  (21 entries, util 18.7200 %)

```
sgs 43200 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 15360 0xBF # 10111111   Q7
sgs 25280 0x80 # 10000000   Q7
sgs 2240 0x3F # 00111111   BE
sgs 83520 0x40 # 01000000   Q6
sgs 17920 0xBF # 10111111   Q7
sgs 43200 0x7F # 01111111   Q6
sgs 138880 0x40 # 01000000   Q6
sgs 17920 0xBF # 10111111   Q7
sgs 43200 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 15360 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 15040 0xBF # 10111111   Q7
sgs 83520 0x40 # 01000000   Q6
sgs 17920 0xBF # 10111111   Q7
sgs 43200 0x7F # 01111111   Q6
sgs 95680 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p4  (21 entries, util 26.5200 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 17280 0x7F # 01111111   Q6
sgs 91200 0x80 # 10000000   Q7
sgs 10880 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 18240 0x7F # 01111111   Q6
sgs 120960 0x80 # 10000000   Q7
sgs 10880 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 18240 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 17280 0x7F # 01111111   Q6
sgs 91200 0x80 # 10000000   Q7
sgs 10880 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 18240 0x7F # 01111111   Q6
sgs 102720 0x80 # 10000000   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (23 entries, util 20.2800 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 24000 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 56320 0x80 # 10000000   Q7
sgs 27200 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 13440 0x7F # 01111111   Q6
sgs 109440 0x80 # 10000000   Q7
sgs 27200 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 13440 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24000 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 56320 0x80 # 10000000   Q7
sgs 27200 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 13440 0x7F # 01111111   Q6
sgs 96000 0x80 # 10000000   Q7
sgs 40640 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (23 entries, util 18.7200 %)

```
sgs 37120 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 13440 0xBF # 10111111   Q7
sgs 27840 0x80 # 10000000   Q7
sgs 640 0x3F # 00111111   BE
sgs 84160 0x40 # 01000000   Q6
sgs 24000 0xBF # 10111111   Q7
sgs 37120 0x7F # 01111111   Q6
sgs 138880 0x40 # 01000000   Q6
sgs 24000 0xBF # 10111111   Q7
sgs 37120 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 13440 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 16000 0xBF # 10111111   Q7
sgs 84160 0x40 # 01000000   Q6
sgs 24000 0xBF # 10111111   Q7
sgs 37120 0x7F # 01111111   Q6
sgs 101760 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p5  (22 entries, util 29.6400 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 16000 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 21440 0xBF # 10111111   Q7
sgs 48640 0x80 # 10000000   Q7
sgs 5760 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 111040 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 16000 0x3F # 00111111   BE
sgs 82560 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 77760 0x40 # 01000000   Q6
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p2  (28 entries, util 37.4400 %)

```
sgs 24320 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 4800 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 13760 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 19840 0xBF # 10111111   Q7
sgs 3840 0x3F # 00111111   BE
sgs 65280 0x80 # 10000000   Q7
sgs 30720 0xBF # 10111111   Q7
sgs 24320 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 4800 0x3F # 00111111   BE
sgs 127680 0x40 # 01000000   Q6
sgs 30720 0xBF # 10111111   Q7
sgs 24320 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 4800 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 13760 0xBF # 10111111   Q7
sgs 101440 0x40 # 01000000   Q6
sgs 30720 0xBF # 10111111   Q7
sgs 24320 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 4800 0x3F # 00111111   BE
sgs 103360 0x40 # 01000000   Q6
sgs 5120 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p4  (23 entries, util 20.2800 %)

```
sgs 6720 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 8320 0x3F # 00111111   BE
sgs 45120 0x80 # 10000000   Q7
sgs 46720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 6720 0x3F # 00111111   BE
sgs 96640 0x80 # 10000000   Q7
sgs 46720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 6720 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 8320 0x3F # 00111111   BE
sgs 45120 0x80 # 10000000   Q7
sgs 46720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 6720 0x3F # 00111111   BE
sgs 89920 0x80 # 10000000   Q7
sgs 3520 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (21 entries, util 18.7200 %)

```
sgs 31040 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12160 0x3F # 00111111   BE
sgs 29120 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 84800 0x40 # 01000000   Q6
sgs 30080 0xBF # 10111111   Q7
sgs 31040 0x7F # 01111111   Q6
sgs 138880 0x40 # 01000000   Q6
sgs 30080 0xBF # 10111111   Q7
sgs 31040 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 16960 0xBF # 10111111   Q7
sgs 84800 0x40 # 01000000   Q6
sgs 30080 0xBF # 10111111   Q7
sgs 31040 0x7F # 01111111   Q6
sgs 107840 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

