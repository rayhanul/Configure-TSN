# Reconfiguration-free admission (Problem 3)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Frozen schedule W loaded from: **result/result-2026-10-10-dataset-testbed-4-saf/heuristic-c9-on/4-matrix-c9on**

## Admission: W (before) vs. after this run's arrivals

| | admitted | of total |
|---|---|---|
| W (base, unchanged) | 11 | 11 |
| + this run's arrivals | 16 | 39 |

Every arrival admitted here required **zero** window-boundary changes -- see the GCL-entry table below (unchanged from W by construction) and the window-boundary integrity check. No previously-admitted flow was rerouted.

## Arrivals

| id | src->dst | RS(s) size | admitted | route | queue | phi_s (ns) | e2e (ns) | rerouted to make room | reason if rejected |
|---|---|---|---|---|---|---|---|---|---|
| 15 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 | 150080 | 46080 | - | - |
| 16 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 17 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 5 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q6 | 64320 | 65600 | - | - |
| 12 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 2 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q6 | 237440 | 39360 | - | - |
| 7 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 4 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 | 562560 | 207680 | - | - |
| 11 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 12480 | 36800 | - | - |
| 21 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 100160 | 47040 | - | - |
| 22 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 112640 | 47040 | - | - |
| 23 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 131520 | 40640 | - | - |
| 42 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 89280 | 693760 | - | - |
| 48 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q6 | 249920 | 39360 | - | - |
| 50 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 62400 | 500160 | - | - |
| 24 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q7 | 162560 | 420160 | - | - |
| 32 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 34 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 45 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q6 | 76800 | 111360 | - | - |
| 29 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q6 | 262400 | 39360 | - | - |
| 30 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q6 | 274880 | 45760 | - | - |
| 40 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 44 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 37 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 43 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 25 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 28 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 33 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 35 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q6 | 89280 | 161600 | - | - |
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
| sw01-p2 | 19 | 19 | 255 |
| sw01-p4 | 24 | 24 | 255 |
| sw02-p2 | 11 | 11 | 255 |
| sw02-p4 | 20 | 20 | 255 |
| sw03-p4 | 19 | 19 | 255 |
| sw03-p5 | 24 | 24 | 255 |
| sw04-p4 | 10 | 10 | 255 |
| sw04-p5 | 18 | 18 | 255 |
| sw05-p4 | 24 | 24 | 255 |
| sw05-p5 | 19 | 19 | 255 |
| sw06-p4 | 17 | 17 | 255 |
| sw06-p5 | 10 | 10 | 255 |
| sw07-p4 | 19 | 19 | 255 |
| sw07-p5 | 21 | 21 | 255 |
| sw08-p2 | 20 | 20 | 255 |
| sw08-p4 | 10 | 10 | 255 |
| sw08-p5 | 19 | 19 | 255 |

## Per-hop windows used by newly admitted flows

| flow | egress port | queue | psi (ns, unchanged) | delta (ns, unchanged) |
|---|---|---|---|---|
| s26(id=15 S3->S2) | S3-p0 | Q7 | 150080 | 12480 |
| s26(id=15 S3->S2) | sw01-p4 | Q7 | 156800 | 12480 |
| s26(id=15 S3->S2) | sw03-p5 | Q7 | 163520 | 12480 |
| s26(id=15 S3->S2) | sw05-p4 | Q7 | 170240 | 12480 |
| s26(id=15 S3->S2) | sw07-p5 | Q7 | 176960 | 12480 |
| s26(id=15 S3->S2) | sw08-p2 | Q7 | 183680 | 12480 |
| s22(id=5 S3->S1) | S3-p0 | Q6 | 64320 | 12480 |
| s22(id=5 S3->S1) | sw01-p4 | Q6 | 70400 | 12480 |
| s22(id=5 S3->S1) | sw03-p5 | Q6 | 77760 | 12480 |
| s22(id=5 S3->S1) | sw05-p4 | Q6 | 85440 | 12480 |
| s22(id=5 S3->S1) | sw07-p5 | Q6 | 93120 | 12480 |
| s22(id=5 S3->S1) | sw08-p4 | Q6 | 99200 | 12480 |
| s22(id=5 S3->S1) | sw06-p5 | Q6 | 105280 | 12480 |
| s22(id=5 S3->S1) | sw04-p4 | Q6 | 111360 | 12480 |
| s22(id=5 S3->S1) | sw02-p2 | Q6 | 117440 | 12480 |
| s20(id=2 S1->S2) | S1-p0 | Q6 | 237440 | 12480 |
| s20(id=2 S1->S2) | sw02-p4 | Q6 | 244160 | 12480 |
| s20(id=2 S1->S2) | sw04-p5 | Q6 | 250880 | 12480 |
| s20(id=2 S1->S2) | sw06-p4 | Q6 | 257600 | 12480 |
| s20(id=2 S1->S2) | sw08-p2 | Q6 | 264320 | 12480 |
| s21(id=4 S3->S2) | S3-p0 | Q7 | 562560 | 12480 |
| s21(id=4 S3->S2) | sw01-p4 | Q7 | 570240 | 12480 |
| s21(id=4 S3->S2) | sw03-p5 | Q7 | 577920 | 12480 |
| s21(id=4 S3->S2) | sw05-p4 | Q7 | 585600 | 12480 |
| s21(id=4 S3->S2) | sw07-p5 | Q7 | 750080 | 12480 |
| s21(id=4 S3->S2) | sw08-p2 | Q7 | 757760 | 12480 |
| s24(id=11 S2->S1) | S2-p0 | Q6 | 12480 | 12480 |
| s24(id=11 S2->S1) | sw08-p4 | Q6 | 18560 | 12480 |
| s24(id=11 S2->S1) | sw06-p5 | Q6 | 24640 | 12480 |
| s24(id=11 S2->S1) | sw04-p4 | Q6 | 30720 | 12480 |
| s24(id=11 S2->S1) | sw02-p2 | Q6 | 36800 | 12480 |
| s29(id=21 S2->S1) | S2-p0 | Q6 | 100160 | 12480 |
| s29(id=21 S2->S1) | sw08-p4 | Q6 | 111680 | 12480 |
| s29(id=21 S2->S1) | sw06-p5 | Q6 | 119360 | 12480 |
| s29(id=21 S2->S1) | sw04-p4 | Q6 | 127040 | 12480 |
| s29(id=21 S2->S1) | sw02-p2 | Q6 | 134720 | 12480 |
| s30(id=22 S2->S1) | S2-p0 | Q6 | 112640 | 12480 |
| s30(id=22 S2->S1) | sw08-p4 | Q6 | 124160 | 12480 |
| s30(id=22 S2->S1) | sw06-p5 | Q6 | 131840 | 12480 |
| s30(id=22 S2->S1) | sw04-p4 | Q6 | 139520 | 12480 |
| s30(id=22 S2->S1) | sw02-p2 | Q6 | 147200 | 12480 |
| s31(id=23 S2->S1) | S2-p0 | Q6 | 131520 | 12480 |
| s31(id=23 S2->S1) | sw08-p4 | Q6 | 138240 | 12480 |
| s31(id=23 S2->S1) | sw06-p5 | Q6 | 144960 | 12480 |
| s31(id=23 S2->S1) | sw04-p4 | Q6 | 152000 | 12480 |
| s31(id=23 S2->S1) | sw02-p2 | Q6 | 159680 | 12480 |
| s50(id=42 S1->S2) | S1-p0 | Q7 | 89280 | 12480 |
| s50(id=42 S1->S2) | sw02-p4 | Q7 | 95360 | 12480 |
| s50(id=42 S1->S2) | sw04-p5 | Q7 | 102720 | 12480 |
| s50(id=42 S1->S2) | sw06-p4 | Q7 | 764480 | 12480 |
| s50(id=42 S1->S2) | sw08-p2 | Q7 | 770560 | 12480 |
| s56(id=48 S1->S2) | S1-p0 | Q6 | 249920 | 12480 |
| s56(id=48 S1->S2) | sw02-p4 | Q6 | 256640 | 12480 |
| s56(id=48 S1->S2) | sw04-p5 | Q6 | 263360 | 12480 |
| s56(id=48 S1->S2) | sw06-p4 | Q6 | 270080 | 12480 |
| s56(id=48 S1->S2) | sw08-p2 | Q6 | 276800 | 12480 |
| s58(id=50 S2->S1) | S2-p0 | Q7 | 62400 | 12480 |
| s58(id=50 S2->S1) | sw08-p4 | Q7 | 69120 | 12480 |
| s58(id=50 S2->S1) | sw06-p5 | Q7 | 75840 | 12480 |
| s58(id=50 S2->S1) | sw04-p4 | Q7 | 82560 | 12480 |
| s58(id=50 S2->S1) | sw02-p2 | Q7 | 550080 | 12480 |
| s32(id=24 S3->S1) | S3-p0 | Q7 | 162560 | 12480 |
| s32(id=24 S3->S1) | sw01-p4 | Q7 | 169280 | 12480 |
| s32(id=24 S3->S1) | sw03-p5 | Q7 | 176000 | 12480 |
| s32(id=24 S3->S1) | sw05-p4 | Q7 | 182720 | 12480 |
| s32(id=24 S3->S1) | sw07-p5 | Q7 | 355840 | 12480 |
| s32(id=24 S3->S1) | sw08-p4 | Q7 | 550080 | 12480 |
| s32(id=24 S3->S1) | sw06-p5 | Q7 | 556800 | 12480 |
| s32(id=24 S3->S1) | sw04-p4 | Q7 | 563520 | 12480 |
| s32(id=24 S3->S1) | sw02-p2 | Q7 | 570240 | 12480 |
| s53(id=45 S3->S1) | S3-p0 | Q6 | 76800 | 12480 |
| s53(id=45 S3->S1) | sw01-p4 | Q6 | 85120 | 12480 |
| s53(id=45 S3->S1) | sw03-p5 | Q6 | 93440 | 12480 |
| s53(id=45 S3->S1) | sw05-p4 | Q6 | 101760 | 12480 |
| s53(id=45 S3->S1) | sw07-p5 | Q6 | 139200 | 12480 |
| s53(id=45 S3->S1) | sw08-p4 | Q6 | 150720 | 12480 |
| s53(id=45 S3->S1) | sw06-p5 | Q6 | 159040 | 12480 |
| s53(id=45 S3->S1) | sw04-p4 | Q6 | 167360 | 12480 |
| s53(id=45 S3->S1) | sw02-p2 | Q6 | 175680 | 12480 |
| s37(id=29 S1->S2) | S1-p0 | Q6 | 262400 | 12480 |
| s37(id=29 S1->S2) | sw02-p4 | Q6 | 269120 | 12480 |
| s37(id=29 S1->S2) | sw04-p5 | Q6 | 275840 | 12480 |
| s37(id=29 S1->S2) | sw06-p4 | Q6 | 282560 | 12480 |
| s37(id=29 S1->S2) | sw08-p2 | Q6 | 289280 | 12480 |
| s38(id=30 S1->S2) | S1-p0 | Q6 | 274880 | 12480 |
| s38(id=30 S1->S2) | sw02-p4 | Q6 | 283200 | 12480 |
| s38(id=30 S1->S2) | sw04-p5 | Q6 | 291520 | 12480 |
| s38(id=30 S1->S2) | sw06-p4 | Q6 | 299840 | 12480 |
| s38(id=30 S1->S2) | sw08-p2 | Q6 | 308160 | 12480 |
| s43(id=35 S3->S1) | S3-p0 | Q6 | 89280 | 12480 |
| s43(id=35 S3->S1) | sw01-p4 | Q6 | 97600 | 12480 |
| s43(id=35 S3->S1) | sw03-p5 | Q6 | 105920 | 12480 |
| s43(id=35 S3->S1) | sw05-p4 | Q6 | 200000 | 12480 |
| s43(id=35 S3->S1) | sw07-p5 | Q6 | 207680 | 12480 |
| s43(id=35 S3->S1) | sw08-p4 | Q6 | 215360 | 12480 |
| s43(id=35 S3->S1) | sw06-p5 | Q6 | 223040 | 12480 |
| s43(id=35 S3->S1) | sw04-p4 | Q6 | 230720 | 12480 |
| s43(id=35 S3->S1) | sw02-p2 | Q6 | 238400 | 12480 |

## Constraint check

- C1-C7, C9: OK
- window-boundary integrity (no window's psi/delta changed anywhere): OK

## GCL per egress port

### sw01-p2  (19 entries, util 21.8400 %)

```
sgs 41600 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 49600 0x40 # 01000000   Q6
sgs 19520 0x3F # 00111111   BE
sgs 25920 0x80 # 10000000   Q7
sgs 79360 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0x3F # 00111111   BE
sgs 14400 0x40 # 01000000   Q6
sgs 160000 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 38720 0x40 # 01000000   Q6
sgs 135680 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0x3F # 00111111   BE
sgs 14400 0x40 # 01000000   Q6
sgs 118400 0x3F # 00111111   BE
```

### sw01-p4  (24 entries, util 29.6400 %)

```
sgs 8640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 10560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13440 0x3F # 00111111   BE
sgs 73280 0x40 # 01000000   Q6
sgs 19200 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 8640 0x3F # 00111111   BE
sgs 122240 0x40 # 01000000   Q6
sgs 19200 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 8640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 10560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13440 0x3F # 00111111   BE
sgs 73280 0x40 # 01000000   Q6
sgs 19200 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 8640 0x3F # 00111111   BE
sgs 113600 0x40 # 01000000   Q6
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (11 entries, util 18.7200 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 1600 0x3F # 00111111   BE
sgs 435840 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p4  (20 entries, util 28.0800 %)

```
sgs 7680 0x3F # 00111111   BE
sgs 34880 0x40 # 01000000   Q6
sgs 14080 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 13440 0xBF # 10111111   Q7
sgs 64000 0x80 # 10000000   Q7
sgs 3520 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 7680 0x3F # 00111111   BE
sgs 138880 0x40 # 01000000   Q6
sgs 3520 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 7680 0x3F # 00111111   BE
sgs 138880 0x40 # 01000000   Q6
sgs 3520 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 7680 0x3F # 00111111   BE
sgs 131200 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (19 entries, util 21.8400 %)

```
sgs 33280 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 3520 0x3F # 00111111   BE
sgs 47360 0x40 # 01000000   Q6
sgs 19200 0x3F # 00111111   BE
sgs 17920 0x80 # 10000000   Q7
sgs 86720 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 16320 0x3F # 00111111   BE
sgs 14080 0x40 # 01000000   Q6
sgs 157120 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 3520 0x3F # 00111111   BE
sgs 35200 0x40 # 01000000   Q6
sgs 136000 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 16320 0x3F # 00111111   BE
sgs 14080 0x40 # 01000000   Q6
sgs 123840 0x3F # 00111111   BE
```

### sw03-p5  (24 entries, util 29.6400 %)

```
sgs 16960 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 8960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 14400 0xBF # 10111111   Q7
sgs 73920 0x40 # 01000000   Q6
sgs 10880 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 16960 0x7F # 01111111   Q6
sgs 122240 0x40 # 01000000   Q6
sgs 10880 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 16960 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 8960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 14400 0xBF # 10111111   Q7
sgs 73920 0x40 # 01000000   Q6
sgs 10880 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 16960 0x7F # 01111111   Q6
sgs 105280 0x40 # 01000000   Q6
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p4  (10 entries, util 18.7200 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 45120 0xBF # 10111111   Q7
sgs 442560 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (18 entries, util 28.0800 %)

```
sgs 15360 0x7F # 01111111   Q6
sgs 32320 0x40 # 01000000   Q6
sgs 2240 0x3F # 00111111   BE
sgs 13440 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0xBF # 10111111   Q7
sgs 64000 0x80 # 10000000   Q7
sgs 45760 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 138880 0x40 # 01000000   Q6
sgs 45760 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 138880 0x40 # 01000000   Q6
sgs 45760 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 123520 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (24 entries, util 29.6400 %)

```
sgs 25280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 7360 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 15360 0xBF # 10111111   Q7
sgs 74560 0x40 # 01000000   Q6
sgs 2560 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 25280 0x7F # 01111111   Q6
sgs 122240 0x40 # 01000000   Q6
sgs 2560 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 25280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 7360 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 15360 0xBF # 10111111   Q7
sgs 74560 0x40 # 01000000   Q6
sgs 2560 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 25280 0x7F # 01111111   Q6
sgs 96960 0x40 # 01000000   Q6
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p5  (19 entries, util 21.8400 %)

```
sgs 24960 0x3F # 00111111   BE
sgs 27840 0x80 # 10000000   Q7
sgs 2880 0x3F # 00111111   BE
sgs 47040 0x40 # 01000000   Q6
sgs 18240 0x3F # 00111111   BE
sgs 14400 0x80 # 10000000   Q7
sgs 89600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 18240 0x3F # 00111111   BE
sgs 13760 0x40 # 01000000   Q6
sgs 155520 0x3F # 00111111   BE
sgs 27840 0x80 # 10000000   Q7
sgs 2880 0x3F # 00111111   BE
sgs 32960 0x40 # 01000000   Q6
sgs 136320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 18240 0x3F # 00111111   BE
sgs 13760 0x40 # 01000000   Q6
sgs 130560 0x3F # 00111111   BE
```

### sw06-p4  (17 entries, util 28.0800 %)

```
sgs 23040 0x7F # 01111111   Q6
sgs 29760 0x40 # 01000000   Q6
sgs 17280 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 15360 0xBF # 10111111   Q7
sgs 64000 0x80 # 10000000   Q7
sgs 38080 0xBF # 10111111   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 138880 0x40 # 01000000   Q6
sgs 38080 0xBF # 10111111   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 138880 0x40 # 01000000   Q6
sgs 38080 0xBF # 10111111   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 115840 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (10 entries, util 18.7200 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 38400 0xBF # 10111111   Q7
sgs 449280 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (19 entries, util 21.8400 %)

```
sgs 16640 0x3F # 00111111   BE
sgs 31040 0x80 # 10000000   Q7
sgs 2880 0x3F # 00111111   BE
sgs 45440 0x40 # 01000000   Q6
sgs 17280 0x3F # 00111111   BE
sgs 14080 0x80 # 10000000   Q7
sgs 89280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 21440 0x3F # 00111111   BE
sgs 13440 0x40 # 01000000   Q6
sgs 152640 0x3F # 00111111   BE
sgs 31040 0x80 # 10000000   Q7
sgs 2880 0x3F # 00111111   BE
sgs 29440 0x40 # 01000000   Q6
sgs 136640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 21440 0x3F # 00111111   BE
sgs 13440 0x40 # 01000000   Q6
sgs 136000 0x3F # 00111111   BE
```

### sw07-p5  (21 entries, util 29.6400 %)

```
sgs 33600 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 16320 0xBF # 10111111   Q7
sgs 75200 0x40 # 01000000   Q6
sgs 44160 0xBF # 10111111   Q7
sgs 33600 0x7F # 01111111   Q6
sgs 122240 0x40 # 01000000   Q6
sgs 44160 0xBF # 10111111   Q7
sgs 33600 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 16320 0xBF # 10111111   Q7
sgs 75200 0x40 # 01000000   Q6
sgs 44160 0xBF # 10111111   Q7
sgs 33600 0x7F # 01111111   Q6
sgs 88640 0x40 # 01000000   Q6
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p2  (20 entries, util 39.0000 %)

```
sgs 30720 0x7F # 01111111   Q6
sgs 25280 0x40 # 01000000   Q6
sgs 2560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 17280 0xBF # 10111111   Q7
sgs 92480 0x40 # 01000000   Q6
sgs 19200 0xBF # 10111111   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 150080 0x40 # 01000000   Q6
sgs 19200 0xBF # 10111111   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 25280 0x40 # 01000000   Q6
sgs 2560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 17280 0xBF # 10111111   Q7
sgs 92480 0x40 # 01000000   Q6
sgs 19200 0xBF # 10111111   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 119360 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p4  (10 entries, util 18.7200 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 31680 0xBF # 10111111   Q7
sgs 456000 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (19 entries, util 21.8400 %)

```
sgs 8320 0x3F # 00111111   BE
sgs 34240 0x80 # 10000000   Q7
sgs 2880 0x3F # 00111111   BE
sgs 43840 0x40 # 01000000   Q6
sgs 16320 0x3F # 00111111   BE
sgs 13760 0x80 # 10000000   Q7
sgs 88960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 24640 0x3F # 00111111   BE
sgs 13120 0x40 # 01000000   Q6
sgs 149760 0x3F # 00111111   BE
sgs 34240 0x80 # 10000000   Q7
sgs 2880 0x3F # 00111111   BE
sgs 25920 0x40 # 01000000   Q6
sgs 136960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 24640 0x3F # 00111111   BE
sgs 13120 0x40 # 01000000   Q6
sgs 141440 0x3F # 00111111   BE
```

