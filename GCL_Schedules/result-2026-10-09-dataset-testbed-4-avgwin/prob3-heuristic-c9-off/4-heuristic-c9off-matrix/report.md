# Reconfiguration-free admission (Problem 3)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Frozen schedule W loaded from: **result/result-2026-10-09-dataset-testbed-4-avgwin/heuristic-c9-off/4-matrix-c9off**

## Admission: W (before) vs. after this run's arrivals

| | admitted | of total |
|---|---|---|
| W (base, unchanged) | 11 | 11 |
| + this run's arrivals | 13 | 39 |

Every arrival admitted here required **zero** window-boundary changes -- see the GCL-entry table below (unchanged from W by construction) and the window-boundary integrity check. No previously-admitted flow was rerouted.

## Arrivals

| id | src->dst | RS(s) size | admitted | route | queue | phi_s (ns) | e2e (ns) | rerouted to make room | reason if rejected |
|---|---|---|---|---|---|---|---|---|---|
| 15 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 16 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 17 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 5 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 12 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 2 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 150080 | 312320 | - | - |
| 7 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 4 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q6 | 212800 | 95680 | - | - |
| 11 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 62400 | 533440 | - | - |
| 21 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 87680 | 79040 | - | - |
| 22 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 150080 | 512320 | - | - |
| 23 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 100480 | 79040 | - | - |
| 42 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 562880 | 232960 | - | - |
| 48 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q6 | 87680 | 141440 | - | - |
| 50 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 550080 | 128960 | - | - |
| 24 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q7 | 462720 | 232960 | - | - |
| 32 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 34 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 45 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q6 | 225600 | 145600 | - | - |
| 29 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q6 | 100480 | 141440 | - | - |
| 30 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q6 | 237760 | 83520 | - | - |
| 40 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 44 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 37 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 43 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 25 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 28 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 33 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 35 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 36 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 46 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 47 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 26 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 49 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 27 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 31 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 38 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 39 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 41 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |

## Per-port GCL entries (should equal W exactly)

| port | W entries | after arrivals | GCL_size |
|---|---|---|---|
| sw01-p2 | 29 | 29 | 255 |
| sw01-p4 | 24 | 24 | 255 |
| sw02-p2 | 11 | 11 | 255 |
| sw02-p4 | 26 | 26 | 255 |
| sw03-p4 | 29 | 29 | 255 |
| sw03-p5 | 21 | 21 | 255 |
| sw04-p4 | 11 | 11 | 255 |
| sw04-p5 | 26 | 26 | 255 |
| sw05-p4 | 21 | 21 | 255 |
| sw05-p5 | 29 | 29 | 255 |
| sw06-p4 | 26 | 26 | 255 |
| sw06-p5 | 11 | 11 | 255 |
| sw07-p4 | 29 | 29 | 255 |
| sw07-p5 | 25 | 25 | 255 |
| sw08-p2 | 21 | 21 | 255 |
| sw08-p4 | 10 | 10 | 255 |
| sw08-p5 | 29 | 29 | 255 |

## Per-hop windows used by newly admitted flows

| flow | egress port | queue | psi (ns, unchanged) | delta (ns, unchanged) |
|---|---|---|---|---|
| s20(id=2 S1->S2) | S1-p0 | Q7 | 150080 | 12480 |
| s20(id=2 S1->S2) | sw02-p4 | Q7 | 166720 | 12480 |
| s20(id=2 S1->S2) | sw04-p5 | Q7 | 183360 | 12480 |
| s20(id=2 S1->S2) | sw06-p4 | Q7 | 262400 | 12480 |
| s20(id=2 S1->S2) | sw08-p2 | Q7 | 449920 | 12480 |
| s21(id=4 S3->S2) | S3-p0 | Q6 | 212800 | 12480 |
| s21(id=4 S3->S2) | sw01-p4 | Q6 | 229440 | 12480 |
| s21(id=4 S3->S2) | sw03-p5 | Q6 | 246080 | 12480 |
| s21(id=4 S3->S2) | sw05-p4 | Q6 | 262720 | 12480 |
| s21(id=4 S3->S2) | sw07-p5 | Q6 | 279360 | 12480 |
| s21(id=4 S3->S2) | sw08-p2 | Q6 | 296000 | 12480 |
| s24(id=11 S2->S1) | S2-p0 | Q7 | 62400 | 12480 |
| s24(id=11 S2->S1) | sw08-p4 | Q7 | 79040 | 12480 |
| s24(id=11 S2->S1) | sw06-p5 | Q7 | 550080 | 12480 |
| s24(id=11 S2->S1) | sw04-p4 | Q7 | 566720 | 12480 |
| s24(id=11 S2->S1) | sw02-p2 | Q7 | 583360 | 12480 |
| s29(id=21 S2->S1) | S2-p0 | Q6 | 87680 | 12480 |
| s29(id=21 S2->S1) | sw08-p4 | Q6 | 104320 | 12480 |
| s29(id=21 S2->S1) | sw06-p5 | Q6 | 120960 | 12480 |
| s29(id=21 S2->S1) | sw04-p4 | Q6 | 137600 | 12480 |
| s29(id=21 S2->S1) | sw02-p2 | Q6 | 154240 | 12480 |
| s30(id=22 S2->S1) | S2-p0 | Q7 | 150080 | 12480 |
| s30(id=22 S2->S1) | sw08-p4 | Q7 | 550080 | 12480 |
| s30(id=22 S2->S1) | sw06-p5 | Q7 | 566720 | 12480 |
| s30(id=22 S2->S1) | sw04-p4 | Q7 | 583360 | 12480 |
| s30(id=22 S2->S1) | sw02-p2 | Q7 | 649920 | 12480 |
| s31(id=23 S2->S1) | S2-p0 | Q6 | 100480 | 12480 |
| s31(id=23 S2->S1) | sw08-p4 | Q6 | 117120 | 12480 |
| s31(id=23 S2->S1) | sw06-p5 | Q6 | 133760 | 12480 |
| s31(id=23 S2->S1) | sw04-p4 | Q6 | 150400 | 12480 |
| s31(id=23 S2->S1) | sw02-p2 | Q6 | 167040 | 12480 |
| s50(id=42 S1->S2) | S1-p0 | Q7 | 562880 | 12480 |
| s50(id=42 S1->S2) | sw02-p4 | Q7 | 579520 | 12480 |
| s50(id=42 S1->S2) | sw04-p5 | Q7 | 750080 | 12480 |
| s50(id=42 S1->S2) | sw06-p4 | Q7 | 766720 | 12480 |
| s50(id=42 S1->S2) | sw08-p2 | Q7 | 783360 | 12480 |
| s56(id=48 S1->S2) | S1-p0 | Q6 | 87680 | 12480 |
| s56(id=48 S1->S2) | sw02-p4 | Q6 | 104320 | 12480 |
| s56(id=48 S1->S2) | sw04-p5 | Q6 | 120960 | 12480 |
| s56(id=48 S1->S2) | sw06-p4 | Q6 | 137600 | 12480 |
| s56(id=48 S1->S2) | sw08-p2 | Q6 | 216640 | 12480 |
| s58(id=50 S2->S1) | S2-p0 | Q7 | 550080 | 12480 |
| s58(id=50 S2->S1) | sw08-p4 | Q7 | 566720 | 12480 |
| s58(id=50 S2->S1) | sw06-p5 | Q7 | 583360 | 12480 |
| s58(id=50 S2->S1) | sw04-p4 | Q7 | 649920 | 12480 |
| s58(id=50 S2->S1) | sw02-p2 | Q7 | 666560 | 12480 |
| s32(id=24 S3->S1) | S3-p0 | Q7 | 462720 | 12480 |
| s32(id=24 S3->S1) | sw01-p4 | Q7 | 479360 | 12480 |
| s32(id=24 S3->S1) | sw03-p5 | Q7 | 496000 | 12480 |
| s32(id=24 S3->S1) | sw05-p4 | Q7 | 512640 | 12480 |
| s32(id=24 S3->S1) | sw07-p5 | Q7 | 562880 | 12480 |
| s32(id=24 S3->S1) | sw08-p4 | Q7 | 579520 | 12480 |
| s32(id=24 S3->S1) | sw06-p5 | Q7 | 649920 | 12480 |
| s32(id=24 S3->S1) | sw04-p4 | Q7 | 666560 | 12480 |
| s32(id=24 S3->S1) | sw02-p2 | Q7 | 683200 | 12480 |
| s53(id=45 S3->S1) | S3-p0 | Q6 | 225600 | 12480 |
| s53(id=45 S3->S1) | sw01-p4 | Q6 | 242240 | 12480 |
| s53(id=45 S3->S1) | sw03-p5 | Q6 | 258880 | 12480 |
| s53(id=45 S3->S1) | sw05-p4 | Q6 | 275520 | 12480 |
| s53(id=45 S3->S1) | sw07-p5 | Q6 | 292160 | 12480 |
| s53(id=45 S3->S1) | sw08-p4 | Q6 | 308800 | 12480 |
| s53(id=45 S3->S1) | sw06-p5 | Q6 | 325440 | 12480 |
| s53(id=45 S3->S1) | sw04-p4 | Q6 | 342080 | 12480 |
| s53(id=45 S3->S1) | sw02-p2 | Q6 | 358720 | 12480 |
| s37(id=29 S1->S2) | S1-p0 | Q6 | 100480 | 12480 |
| s37(id=29 S1->S2) | sw02-p4 | Q6 | 117120 | 12480 |
| s37(id=29 S1->S2) | sw04-p5 | Q6 | 133760 | 12480 |
| s37(id=29 S1->S2) | sw06-p4 | Q6 | 212800 | 12480 |
| s37(id=29 S1->S2) | sw08-p2 | Q6 | 229440 | 12480 |
| s38(id=30 S1->S2) | S1-p0 | Q6 | 237760 | 12480 |
| s38(id=30 S1->S2) | sw02-p4 | Q6 | 254400 | 12480 |
| s38(id=30 S1->S2) | sw04-p5 | Q6 | 271040 | 12480 |
| s38(id=30 S1->S2) | sw06-p4 | Q6 | 292160 | 12480 |
| s38(id=30 S1->S2) | sw08-p2 | Q6 | 308800 | 12480 |

## Constraint check

- C1-C7, C9: OK
- window-boundary integrity (no window's psi/delta changed anywhere): OK

## GCL per egress port

### sw01-p2  (29 entries, util 21.8400 %)

```
sgs 83200 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12800 0x40 # 01000000   Q6
sgs 62400 0x3F # 00111111   BE
sgs 12800 0x40 # 01000000   Q6
sgs 62080 0x3F # 00111111   BE
sgs 12800 0x40 # 01000000   Q6
sgs 112320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12800 0x40 # 01000000   Q6
sgs 112320 0x3F # 00111111   BE
sgs 12800 0x40 # 01000000   Q6
sgs 62080 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 29440 0x3F # 00111111   BE
```

### sw01-p4  (24 entries, util 17.1600 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 72320 0x80 # 10000000   Q7
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 122240 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 72320 0x80 # 10000000   Q7
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 105600 0x40 # 01000000   Q6
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (11 entries, util 12.4800 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 41280 0x7F # 01111111   Q6
sgs 396160 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p4  (26 entries, util 28.0800 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 69120 0x40 # 01000000   Q6
sgs 39360 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 119040 0x40 # 01000000   Q6
sgs 39360 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 119040 0x40 # 01000000   Q6
sgs 39360 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 102400 0x40 # 01000000   Q6
sgs 6080 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (29 entries, util 21.8400 %)

```
sgs 66560 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12800 0x40 # 01000000   Q6
sgs 62400 0x3F # 00111111   BE
sgs 12800 0x40 # 01000000   Q6
sgs 62080 0x3F # 00111111   BE
sgs 12800 0x40 # 01000000   Q6
sgs 112320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12800 0x40 # 01000000   Q6
sgs 112320 0x3F # 00111111   BE
sgs 12800 0x40 # 01000000   Q6
sgs 62080 0x3F # 00111111   BE
sgs 12800 0x40 # 01000000   Q6
sgs 45760 0x3F # 00111111   BE
```

### sw03-p5  (21 entries, util 17.1600 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 72320 0x80 # 10000000   Q7
sgs 44480 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 122240 0x40 # 01000000   Q6
sgs 44480 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 72320 0x80 # 10000000   Q7
sgs 44480 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 88960 0x40 # 01000000   Q6
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p4  (11 entries, util 12.4800 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 24640 0x7F # 01111111   Q6
sgs 412800 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (26 entries, util 28.0800 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 69120 0x40 # 01000000   Q6
sgs 22720 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 119040 0x40 # 01000000   Q6
sgs 22720 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 119040 0x40 # 01000000   Q6
sgs 22720 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 85760 0x40 # 01000000   Q6
sgs 6080 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (21 entries, util 17.1600 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 72320 0x80 # 10000000   Q7
sgs 27840 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 122240 0x40 # 01000000   Q6
sgs 27840 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 72320 0x80 # 10000000   Q7
sgs 27840 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 72320 0x40 # 01000000   Q6
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p5  (29 entries, util 21.8400 %)

```
sgs 49920 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12800 0x40 # 01000000   Q6
sgs 62400 0x3F # 00111111   BE
sgs 12800 0x40 # 01000000   Q6
sgs 62080 0x3F # 00111111   BE
sgs 12800 0x40 # 01000000   Q6
sgs 112320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12800 0x40 # 01000000   Q6
sgs 112320 0x3F # 00111111   BE
sgs 12800 0x40 # 01000000   Q6
sgs 62080 0x3F # 00111111   BE
sgs 12800 0x40 # 01000000   Q6
sgs 62400 0x3F # 00111111   BE
```

### sw06-p4  (26 entries, util 28.0800 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 69120 0x40 # 01000000   Q6
sgs 6080 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 119040 0x40 # 01000000   Q6
sgs 6080 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 119040 0x40 # 01000000   Q6
sgs 6080 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 69120 0x40 # 01000000   Q6
sgs 6080 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (11 entries, util 12.4800 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 8000 0x3F # 00111111   BE
sgs 429440 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (29 entries, util 21.8400 %)

```
sgs 33280 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 62720 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 62400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 112640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 112640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 62400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 79360 0x3F # 00111111   BE
```

### sw07-p5  (25 entries, util 17.1600 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 72320 0x80 # 10000000   Q7
sgs 11200 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 122240 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 72320 0x80 # 10000000   Q7
sgs 11200 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 55680 0x40 # 01000000   Q6
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p2  (21 entries, util 32.7600 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 29120 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 83520 0x80 # 10000000   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 150080 0x40 # 01000000   Q6
sgs 33280 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 29120 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 83520 0x80 # 10000000   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 83520 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p4  (10 entries, util 12.4800 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 446080 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (29 entries, util 21.8400 %)

```
sgs 16640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 62720 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 62400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 112640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 112640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 62400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 96000 0x3F # 00111111   BE
```

