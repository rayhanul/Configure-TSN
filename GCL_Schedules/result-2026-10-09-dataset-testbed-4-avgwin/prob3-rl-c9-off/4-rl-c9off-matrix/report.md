# Reconfiguration-free admission (Problem 3)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Frozen schedule W loaded from: **result/result-2026-10-09-dataset-testbed-4-avgwin/rl-c9-off/4-matrix-c9off**

## Admission: W (before) vs. after this run's arrivals

| | admitted | of total |
|---|---|---|
| W (base, unchanged) | 11 | 11 |
| + this run's arrivals | 17 | 39 |

Every arrival admitted here required **zero** window-boundary changes -- see the GCL-entry table below (unchanged from W by construction) and the window-boundary integrity check. No previously-admitted flow was rerouted.

## Arrivals

| id | src->dst | RS(s) size | admitted | route | queue | phi_s (ns) | e2e (ns) | rerouted to make room | reason if rejected |
|---|---|---|---|---|---|---|---|---|---|
| 15 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q6 | 37440 | 95680 | - | - |
| 16 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 17 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 12480 | 79040 | - | - |
| 5 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 12 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 37440 | 95680 | - | - |
| 2 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 37440 | 140480 | - | - |
| 7 | S1->S3 | - | yes | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 62400 | 247360 | - | - |
| 4 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 | 462720 | 95680 | - | - |
| 11 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 87680 | 79040 | - | - |
| 21 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 100480 | 128640 | - | - |
| 22 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 62400 | 116800 | - | - |
| 23 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 113280 | 132480 | - | - |
| 42 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 152000 | 310400 | - | - |
| 48 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 450240 | 140480 | - | - |
| 50 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 225280 | 79040 | - | - |
| 24 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q7 | 475520 | 303680 | - | - |
| 32 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 34 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 45 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q6 | 62400 | 350080 | - | - |
| 29 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q6 | 237760 | 79040 | - | - |
| 30 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q6 | 250560 | 95360 | - | - |
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
| sw01-p2 | 31 | 31 | 255 |
| sw01-p4 | 22 | 22 | 255 |
| sw02-p2 | 22 | 22 | 255 |
| sw02-p4 | 28 | 28 | 255 |
| sw03-p4 | 31 | 31 | 255 |
| sw03-p5 | 22 | 22 | 255 |
| sw04-p4 | 24 | 24 | 255 |
| sw04-p5 | 29 | 29 | 255 |
| sw05-p4 | 19 | 19 | 255 |
| sw05-p5 | 31 | 31 | 255 |
| sw06-p4 | 25 | 25 | 255 |
| sw06-p5 | 21 | 21 | 255 |
| sw07-p4 | 31 | 31 | 255 |
| sw07-p5 | 23 | 23 | 255 |
| sw08-p2 | 23 | 23 | 255 |
| sw08-p4 | 22 | 22 | 255 |
| sw08-p5 | 31 | 31 | 255 |

## Per-hop windows used by newly admitted flows

| flow | egress port | queue | psi (ns, unchanged) | delta (ns, unchanged) |
|---|---|---|---|---|
| s26(id=15 S3->S2) | S3-p0 | Q6 | 37440 | 12480 |
| s26(id=15 S3->S2) | sw01-p4 | Q6 | 54080 | 12480 |
| s26(id=15 S3->S2) | sw03-p5 | Q6 | 70720 | 12480 |
| s26(id=15 S3->S2) | sw05-p4 | Q6 | 87360 | 12480 |
| s26(id=15 S3->S2) | sw07-p5 | Q6 | 104000 | 12480 |
| s26(id=15 S3->S2) | sw08-p2 | Q6 | 120640 | 12480 |
| s28(id=17 S2->S1) | S2-p0 | Q7 | 12480 | 12480 |
| s28(id=17 S2->S1) | sw08-p4 | Q7 | 29120 | 12480 |
| s28(id=17 S2->S1) | sw06-p5 | Q7 | 45760 | 12480 |
| s28(id=17 S2->S1) | sw04-p4 | Q7 | 62400 | 12480 |
| s28(id=17 S2->S1) | sw02-p2 | Q7 | 79040 | 12480 |
| s25(id=12 S2->S3) | S2-p0 | Q6 | 37440 | 12480 |
| s25(id=12 S2->S3) | sw08-p5 | Q6 | 54080 | 12480 |
| s25(id=12 S2->S3) | sw07-p4 | Q6 | 70720 | 12480 |
| s25(id=12 S2->S3) | sw05-p5 | Q6 | 87360 | 12480 |
| s25(id=12 S2->S3) | sw03-p4 | Q6 | 104000 | 12480 |
| s25(id=12 S2->S3) | sw01-p2 | Q6 | 120640 | 12480 |
| s20(id=2 S1->S2) | S1-p0 | Q7 | 37440 | 12480 |
| s20(id=2 S1->S2) | sw02-p4 | Q7 | 54080 | 12480 |
| s20(id=2 S1->S2) | sw04-p5 | Q7 | 70720 | 12480 |
| s20(id=2 S1->S2) | sw06-p4 | Q7 | 148800 | 12480 |
| s20(id=2 S1->S2) | sw08-p2 | Q7 | 165440 | 12480 |
| s23(id=7 S1->S3) | S1-p0 | Q7 | 62400 | 12480 |
| s23(id=7 S1->S3) | sw02-p4 | Q7 | 79040 | 12480 |
| s23(id=7 S1->S3) | sw04-p5 | Q7 | 144960 | 12480 |
| s23(id=7 S1->S3) | sw06-p4 | Q7 | 161600 | 12480 |
| s23(id=7 S1->S3) | sw08-p5 | Q7 | 230720 | 12480 |
| s23(id=7 S1->S3) | sw07-p4 | Q7 | 247360 | 12480 |
| s23(id=7 S1->S3) | sw05-p5 | Q7 | 264000 | 12480 |
| s23(id=7 S1->S3) | sw03-p4 | Q7 | 280640 | 12480 |
| s23(id=7 S1->S3) | sw01-p2 | Q7 | 297280 | 12480 |
| s21(id=4 S3->S2) | S3-p0 | Q7 | 462720 | 12480 |
| s21(id=4 S3->S2) | sw01-p4 | Q7 | 479360 | 12480 |
| s21(id=4 S3->S2) | sw03-p5 | Q7 | 496000 | 12480 |
| s21(id=4 S3->S2) | sw05-p4 | Q7 | 512640 | 12480 |
| s21(id=4 S3->S2) | sw07-p5 | Q7 | 529280 | 12480 |
| s21(id=4 S3->S2) | sw08-p2 | Q7 | 545920 | 12480 |
| s24(id=11 S2->S1) | S2-p0 | Q6 | 87680 | 12480 |
| s24(id=11 S2->S1) | sw08-p4 | Q6 | 104320 | 12480 |
| s24(id=11 S2->S1) | sw06-p5 | Q6 | 120960 | 12480 |
| s24(id=11 S2->S1) | sw04-p4 | Q6 | 137600 | 12480 |
| s24(id=11 S2->S1) | sw02-p2 | Q6 | 154240 | 12480 |
| s29(id=21 S2->S1) | S2-p0 | Q6 | 100480 | 12480 |
| s29(id=21 S2->S1) | sw08-p4 | Q6 | 117120 | 12480 |
| s29(id=21 S2->S1) | sw06-p5 | Q6 | 133760 | 12480 |
| s29(id=21 S2->S1) | sw04-p4 | Q6 | 200000 | 12480 |
| s29(id=21 S2->S1) | sw02-p2 | Q6 | 216640 | 12480 |
| s30(id=22 S2->S1) | S2-p0 | Q7 | 62400 | 12480 |
| s30(id=22 S2->S1) | sw08-p4 | Q7 | 79040 | 12480 |
| s30(id=22 S2->S1) | sw06-p5 | Q7 | 95680 | 12480 |
| s30(id=22 S2->S1) | sw04-p4 | Q7 | 150080 | 12480 |
| s30(id=22 S2->S1) | sw02-p2 | Q7 | 166720 | 12480 |
| s31(id=23 S2->S1) | S2-p0 | Q6 | 113280 | 12480 |
| s31(id=23 S2->S1) | sw08-p4 | Q6 | 129920 | 12480 |
| s31(id=23 S2->S1) | sw06-p5 | Q6 | 200000 | 12480 |
| s31(id=23 S2->S1) | sw04-p4 | Q6 | 216640 | 12480 |
| s31(id=23 S2->S1) | sw02-p2 | Q6 | 233280 | 12480 |
| s50(id=42 S1->S2) | S1-p0 | Q7 | 152000 | 12480 |
| s50(id=42 S1->S2) | sw02-p4 | Q7 | 171200 | 12480 |
| s50(id=42 S1->S2) | sw04-p5 | Q7 | 245760 | 12480 |
| s50(id=42 S1->S2) | sw06-p4 | Q7 | 262400 | 12480 |
| s50(id=42 S1->S2) | sw08-p2 | Q7 | 449920 | 12480 |
| s56(id=48 S1->S2) | S1-p0 | Q7 | 450240 | 12480 |
| s56(id=48 S1->S2) | sw02-p4 | Q7 | 476480 | 12480 |
| s56(id=48 S1->S2) | sw04-p5 | Q7 | 544960 | 12480 |
| s56(id=48 S1->S2) | sw06-p4 | Q7 | 561600 | 12480 |
| s56(id=48 S1->S2) | sw08-p2 | Q7 | 578240 | 12480 |
| s58(id=50 S2->S1) | S2-p0 | Q7 | 225280 | 12480 |
| s58(id=50 S2->S1) | sw08-p4 | Q7 | 241920 | 12480 |
| s58(id=50 S2->S1) | sw06-p5 | Q7 | 258560 | 12480 |
| s58(id=50 S2->S1) | sw04-p4 | Q7 | 275200 | 12480 |
| s58(id=50 S2->S1) | sw02-p2 | Q7 | 291840 | 12480 |
| s32(id=24 S3->S1) | S3-p0 | Q7 | 475520 | 12480 |
| s32(id=24 S3->S1) | sw01-p4 | Q7 | 492160 | 12480 |
| s32(id=24 S3->S1) | sw03-p5 | Q7 | 508800 | 12480 |
| s32(id=24 S3->S1) | sw05-p4 | Q7 | 525440 | 12480 |
| s32(id=24 S3->S1) | sw07-p5 | Q7 | 649920 | 12480 |
| s32(id=24 S3->S1) | sw08-p4 | Q7 | 666560 | 12480 |
| s32(id=24 S3->S1) | sw06-p5 | Q7 | 687680 | 12480 |
| s32(id=24 S3->S1) | sw04-p4 | Q7 | 750080 | 12480 |
| s32(id=24 S3->S1) | sw02-p2 | Q7 | 766720 | 12480 |
| s53(id=45 S3->S1) | S3-p0 | Q6 | 62400 | 12480 |
| s53(id=45 S3->S1) | sw01-p4 | Q6 | 80960 | 12480 |
| s53(id=45 S3->S1) | sw03-p5 | Q6 | 99520 | 12480 |
| s53(id=45 S3->S1) | sw05-p4 | Q6 | 118080 | 12480 |
| s53(id=45 S3->S1) | sw07-p5 | Q6 | 140480 | 12480 |
| s53(id=45 S3->S1) | sw08-p4 | Q6 | 200000 | 12480 |
| s53(id=45 S3->S1) | sw06-p5 | Q6 | 216640 | 12480 |
| s53(id=45 S3->S1) | sw04-p4 | Q6 | 233280 | 12480 |
| s53(id=45 S3->S1) | sw02-p2 | Q6 | 400000 | 12480 |
| s37(id=29 S1->S2) | S1-p0 | Q6 | 237760 | 12480 |
| s37(id=29 S1->S2) | sw02-p4 | Q6 | 254400 | 12480 |
| s37(id=29 S1->S2) | sw04-p5 | Q6 | 271040 | 12480 |
| s37(id=29 S1->S2) | sw06-p4 | Q6 | 287680 | 12480 |
| s37(id=29 S1->S2) | sw08-p2 | Q6 | 304320 | 12480 |
| s38(id=30 S1->S2) | S1-p0 | Q6 | 250560 | 12480 |
| s38(id=30 S1->S2) | sw02-p4 | Q6 | 267200 | 12480 |
| s38(id=30 S1->S2) | sw04-p5 | Q6 | 283840 | 12480 |
| s38(id=30 S1->S2) | sw06-p4 | Q6 | 316800 | 12480 |
| s38(id=30 S1->S2) | sw08-p2 | Q6 | 333440 | 12480 |

## Constraint check

- C1-C7, C9: OK
- window-boundary integrity (no window's psi/delta changed anywhere): OK

## GCL per egress port

### sw01-p2  (31 entries, util 26.5200 %)

```
sgs 83200 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 62720 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 1600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 48320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 112640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 112640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 62400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 29440 0x3F # 00111111   BE
```

### sw01-p4  (22 entries, util 23.4000 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 1920 0x3F # 00111111   BE
sgs 77440 0x40 # 01000000   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 141760 0x40 # 01000000   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 91840 0x80 # 10000000   Q7
sgs 41600 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 125120 0x40 # 01000000   Q6
sgs 58240 0xBF # 10111111   Q7
```

### sw02-p2  (22 entries, util 18.7200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 25280 0x40 # 01000000   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 87680 0x80 # 10000000   Q7
sgs 33280 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 58560 0x7F # 01111111   Q6
sgs 20480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 16960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 58560 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p4  (28 entries, util 29.6400 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 31680 0x40 # 01000000   Q6
sgs 26880 0x7F # 01111111   Q6
sgs 21120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 16320 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 127040 0x40 # 01000000   Q6
sgs 31360 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 114560 0x80 # 10000000   Q7
sgs 31360 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 110400 0x40 # 01000000   Q6
sgs 48000 0xBF # 10111111   Q7
```

### sw03-p4  (31 entries, util 26.5200 %)

```
sgs 66560 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 62720 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 1600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 48320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 112640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 112640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 62400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 46080 0x3F # 00111111   BE
```

### sw03-p5  (22 entries, util 23.4000 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 3840 0x3F # 00111111   BE
sgs 75520 0x40 # 01000000   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 141760 0x40 # 01000000   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 91840 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 108480 0x40 # 01000000   Q6
sgs 58240 0xBF # 10111111   Q7
```

### sw04-p4  (24 entries, util 18.7200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0xBF # 10111111   Q7
sgs 24640 0x7F # 01111111   Q6
sgs 25280 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 87680 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0xBF # 10111111   Q7
sgs 53760 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 33600 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 25280 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (29 entries, util 29.6400 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 11520 0x3F # 00111111   BE
sgs 49280 0x80 # 10000000   Q7
sgs 18560 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 123200 0x40 # 01000000   Q6
sgs 18560 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 22080 0x40 # 01000000   Q6
sgs 19840 0xBF # 10111111   Q7
sgs 32000 0x7F # 01111111   Q6
sgs 49280 0x80 # 10000000   Q7
sgs 18560 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 89920 0x40 # 01000000   Q6
sgs 51840 0xBF # 10111111   Q7
```

### sw05-p4  (19 entries, util 23.4000 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 5760 0x3F # 00111111   BE
sgs 73600 0x40 # 01000000   Q6
sgs 58240 0x7F # 01111111   Q6
sgs 141760 0x40 # 01000000   Q6
sgs 58240 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 91840 0x80 # 10000000   Q7
sgs 58240 0x7F # 01111111   Q6
sgs 91840 0x40 # 01000000   Q6
sgs 58240 0xBF # 10111111   Q7
```

### sw05-p5  (31 entries, util 26.5200 %)

```
sgs 49920 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 62720 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 1600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 48320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 112640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 112640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 62400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 62720 0x3F # 00111111   BE
```

### sw06-p4  (25 entries, util 29.6400 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 11520 0x3F # 00111111   BE
sgs 49280 0x80 # 10000000   Q7
sgs 51840 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 123200 0x40 # 01000000   Q6
sgs 51840 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 22080 0x40 # 01000000   Q6
sgs 51840 0x7F # 01111111   Q6
sgs 49280 0x80 # 10000000   Q7
sgs 51840 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 73280 0x40 # 01000000   Q6
sgs 51840 0xBF # 10111111   Q7
```

### sw06-p5  (21 entries, util 18.7200 %)

```
sgs 45760 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
sgs 25280 0x40 # 01000000   Q6
sgs 16640 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 45760 0x7F # 01111111   Q6
sgs 87680 0x80 # 10000000   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 45760 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 41920 0xBF # 10111111   Q7
sgs 37120 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 45760 0x7F # 01111111   Q6
sgs 41920 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (31 entries, util 26.5200 %)

```
sgs 33280 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 62720 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 1600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 48320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 112640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 112640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 62400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 79360 0x3F # 00111111   BE
```

### sw07-p5  (23 entries, util 23.4000 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 11520 0x3F # 00111111   BE
sgs 67840 0x40 # 01000000   Q6
sgs 41600 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 141760 0x40 # 01000000   Q6
sgs 41600 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 91840 0x80 # 10000000   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 75200 0x40 # 01000000   Q6
sgs 58240 0xBF # 10111111   Q7
```

### sw08-p2  (23 entries, util 39.0000 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 29120 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 34560 0xBF # 10111111   Q7
sgs 40000 0x40 # 01000000   Q6
sgs 29760 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 153600 0x40 # 01000000   Q6
sgs 29760 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 29120 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 87040 0x80 # 10000000   Q7
sgs 29760 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 87040 0x40 # 01000000   Q6
sgs 46400 0xBF # 10111111   Q7
```

### sw08-p4  (22 entries, util 18.7200 %)

```
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
sgs 25280 0x40 # 01000000   Q6
sgs 33280 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 87680 0x80 # 10000000   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 58560 0xBF # 10111111   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 16960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 58560 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (31 entries, util 26.5200 %)

```
sgs 16640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 62720 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 1600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 48320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 112640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 112640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 62400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 96000 0x3F # 00111111   BE
```

