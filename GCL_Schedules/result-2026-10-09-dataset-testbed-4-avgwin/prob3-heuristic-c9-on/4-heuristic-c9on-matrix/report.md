# Reconfiguration-free admission (Problem 3)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Frozen schedule W loaded from: **result/result-2026-10-09-dataset-testbed-4-avgwin/heuristic-c9-on/4-matrix-c9on**

## Admission: W (before) vs. after this run's arrivals

| | admitted | of total |
|---|---|---|
| W (base, unchanged) | 11 | 11 |
| + this run's arrivals | 18 | 39 |

Every arrival admitted here required **zero** window-boundary changes -- see the GCL-entry table below (unchanged from W by construction) and the window-boundary integrity check. No previously-admitted flow was rerouted.

## Arrivals

| id | src->dst | RS(s) size | admitted | route | queue | phi_s (ns) | e2e (ns) | rerouted to make room | reason if rejected |
|---|---|---|---|---|---|---|---|---|---|
| 15 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 | 150080 | 33280 | - | - |
| 16 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 62400 | 133760 | - | - |
| 17 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 5 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q7 | 162560 | 104000 | - | - |
| 12 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 2 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 237440 | 29440 | - | - |
| 7 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 4 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q6 | 62400 | 33280 | - | - |
| 11 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 12480 | 29120 | - | - |
| 21 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 37440 | 583360 | - | - |
| 22 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 62400 | 29120 | - | - |
| 23 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 87360 | 29120 | - | - |
| 42 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q6 | 87360 | 29120 | - | - |
| 48 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q6 | 99840 | 29120 | - | - |
| 50 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 99840 | 29120 | - | - |
| 24 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q6 | 462400 | 170880 | - | - |
| 32 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 34 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 45 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q6 | 474880 | 170880 | - | - |
| 29 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 274880 | 29120 | - | - |
| 30 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 287360 | 29120 | - | - |
| 40 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 212480 | 66560 | - | - |
| 44 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 37 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 43 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 25 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 28 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 33 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 35 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q7 | 212480 | 79040 | - | - |
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
| sw01-p2 | 25 | 25 | 255 |
| sw01-p4 | 24 | 24 | 255 |
| sw02-p2 | 10 | 10 | 255 |
| sw02-p4 | 28 | 28 | 255 |
| sw03-p4 | 25 | 25 | 255 |
| sw03-p5 | 24 | 24 | 255 |
| sw04-p4 | 10 | 10 | 255 |
| sw04-p5 | 26 | 26 | 255 |
| sw05-p4 | 24 | 24 | 255 |
| sw05-p5 | 25 | 25 | 255 |
| sw06-p4 | 23 | 23 | 255 |
| sw06-p5 | 10 | 10 | 255 |
| sw07-p4 | 25 | 25 | 255 |
| sw07-p5 | 24 | 24 | 255 |
| sw08-p2 | 20 | 20 | 255 |
| sw08-p4 | 10 | 10 | 255 |
| sw08-p5 | 25 | 25 | 255 |

## Per-hop windows used by newly admitted flows

| flow | egress port | queue | psi (ns, unchanged) | delta (ns, unchanged) |
|---|---|---|---|---|
| s26(id=15 S3->S2) | S3-p0 | Q7 | 150080 | 12480 |
| s26(id=15 S3->S2) | sw01-p4 | Q7 | 154240 | 12480 |
| s26(id=15 S3->S2) | sw03-p5 | Q7 | 158400 | 12480 |
| s26(id=15 S3->S2) | sw05-p4 | Q7 | 162560 | 12480 |
| s26(id=15 S3->S2) | sw07-p5 | Q7 | 166720 | 12480 |
| s26(id=15 S3->S2) | sw08-p2 | Q7 | 170880 | 12480 |
| s27(id=16 S1->S2) | S1-p0 | Q7 | 62400 | 12480 |
| s27(id=16 S1->S2) | sw02-p4 | Q7 | 66560 | 12480 |
| s27(id=16 S1->S2) | sw04-p5 | Q7 | 70720 | 12480 |
| s27(id=16 S1->S2) | sw06-p4 | Q7 | 179520 | 12480 |
| s27(id=16 S1->S2) | sw08-p2 | Q7 | 183680 | 12480 |
| s22(id=5 S3->S1) | S3-p0 | Q7 | 162560 | 12480 |
| s22(id=5 S3->S1) | sw01-p4 | Q7 | 166720 | 12480 |
| s22(id=5 S3->S1) | sw03-p5 | Q7 | 170880 | 12480 |
| s22(id=5 S3->S1) | sw05-p4 | Q7 | 175040 | 12480 |
| s22(id=5 S3->S1) | sw07-p5 | Q7 | 179200 | 12480 |
| s22(id=5 S3->S1) | sw08-p4 | Q7 | 183360 | 12480 |
| s22(id=5 S3->S1) | sw06-p5 | Q7 | 187520 | 12480 |
| s22(id=5 S3->S1) | sw04-p4 | Q7 | 191680 | 12480 |
| s22(id=5 S3->S1) | sw02-p2 | Q7 | 195840 | 12480 |
| s20(id=2 S1->S2) | S1-p0 | Q7 | 237440 | 12480 |
| s20(id=2 S1->S2) | sw02-p4 | Q7 | 241600 | 12480 |
| s20(id=2 S1->S2) | sw04-p5 | Q7 | 246080 | 12480 |
| s20(id=2 S1->S2) | sw06-p4 | Q7 | 250240 | 12480 |
| s20(id=2 S1->S2) | sw08-p2 | Q7 | 254400 | 12480 |
| s21(id=4 S3->S2) | S3-p0 | Q6 | 62400 | 12480 |
| s21(id=4 S3->S2) | sw01-p4 | Q6 | 66560 | 12480 |
| s21(id=4 S3->S2) | sw03-p5 | Q6 | 70720 | 12480 |
| s21(id=4 S3->S2) | sw05-p4 | Q6 | 74880 | 12480 |
| s21(id=4 S3->S2) | sw07-p5 | Q6 | 79040 | 12480 |
| s21(id=4 S3->S2) | sw08-p2 | Q6 | 83200 | 12480 |
| s24(id=11 S2->S1) | S2-p0 | Q6 | 12480 | 12480 |
| s24(id=11 S2->S1) | sw08-p4 | Q6 | 16640 | 12480 |
| s24(id=11 S2->S1) | sw06-p5 | Q6 | 20800 | 12480 |
| s24(id=11 S2->S1) | sw04-p4 | Q6 | 24960 | 12480 |
| s24(id=11 S2->S1) | sw02-p2 | Q6 | 29120 | 12480 |
| s29(id=21 S2->S1) | S2-p0 | Q6 | 37440 | 12480 |
| s29(id=21 S2->S1) | sw08-p4 | Q6 | 537600 | 12480 |
| s29(id=21 S2->S1) | sw06-p5 | Q6 | 600000 | 12480 |
| s29(id=21 S2->S1) | sw04-p4 | Q6 | 604160 | 12480 |
| s29(id=21 S2->S1) | sw02-p2 | Q6 | 608320 | 12480 |
| s30(id=22 S2->S1) | S2-p0 | Q7 | 62400 | 12480 |
| s30(id=22 S2->S1) | sw08-p4 | Q7 | 66560 | 12480 |
| s30(id=22 S2->S1) | sw06-p5 | Q7 | 70720 | 12480 |
| s30(id=22 S2->S1) | sw04-p4 | Q7 | 74880 | 12480 |
| s30(id=22 S2->S1) | sw02-p2 | Q7 | 79040 | 12480 |
| s31(id=23 S2->S1) | S2-p0 | Q7 | 87360 | 12480 |
| s31(id=23 S2->S1) | sw08-p4 | Q7 | 91520 | 12480 |
| s31(id=23 S2->S1) | sw06-p5 | Q7 | 95680 | 12480 |
| s31(id=23 S2->S1) | sw04-p4 | Q7 | 99840 | 12480 |
| s31(id=23 S2->S1) | sw02-p2 | Q7 | 104000 | 12480 |
| s50(id=42 S1->S2) | S1-p0 | Q6 | 87360 | 12480 |
| s50(id=42 S1->S2) | sw02-p4 | Q6 | 91520 | 12480 |
| s50(id=42 S1->S2) | sw04-p5 | Q6 | 95680 | 12480 |
| s50(id=42 S1->S2) | sw06-p4 | Q6 | 99840 | 12480 |
| s50(id=42 S1->S2) | sw08-p2 | Q6 | 104000 | 12480 |
| s56(id=48 S1->S2) | S1-p0 | Q6 | 99840 | 12480 |
| s56(id=48 S1->S2) | sw02-p4 | Q6 | 104000 | 12480 |
| s56(id=48 S1->S2) | sw04-p5 | Q6 | 108160 | 12480 |
| s56(id=48 S1->S2) | sw06-p4 | Q6 | 112320 | 12480 |
| s56(id=48 S1->S2) | sw08-p2 | Q6 | 116480 | 12480 |
| s58(id=50 S2->S1) | S2-p0 | Q7 | 99840 | 12480 |
| s58(id=50 S2->S1) | sw08-p4 | Q7 | 104000 | 12480 |
| s58(id=50 S2->S1) | sw06-p5 | Q7 | 108160 | 12480 |
| s58(id=50 S2->S1) | sw04-p4 | Q7 | 112320 | 12480 |
| s58(id=50 S2->S1) | sw02-p2 | Q7 | 116480 | 12480 |
| s32(id=24 S3->S1) | S3-p0 | Q6 | 462400 | 12480 |
| s32(id=24 S3->S1) | sw01-p4 | Q6 | 466560 | 12480 |
| s32(id=24 S3->S1) | sw03-p5 | Q6 | 470720 | 12480 |
| s32(id=24 S3->S1) | sw05-p4 | Q6 | 474880 | 12480 |
| s32(id=24 S3->S1) | sw07-p5 | Q6 | 600000 | 12480 |
| s32(id=24 S3->S1) | sw08-p4 | Q6 | 604160 | 12480 |
| s32(id=24 S3->S1) | sw06-p5 | Q6 | 612480 | 12480 |
| s32(id=24 S3->S1) | sw04-p4 | Q6 | 616640 | 12480 |
| s32(id=24 S3->S1) | sw02-p2 | Q6 | 620800 | 12480 |
| s53(id=45 S3->S1) | S3-p0 | Q6 | 474880 | 12480 |
| s53(id=45 S3->S1) | sw01-p4 | Q6 | 479040 | 12480 |
| s53(id=45 S3->S1) | sw03-p5 | Q6 | 483200 | 12480 |
| s53(id=45 S3->S1) | sw05-p4 | Q6 | 600000 | 12480 |
| s53(id=45 S3->S1) | sw07-p5 | Q6 | 612480 | 12480 |
| s53(id=45 S3->S1) | sw08-p4 | Q6 | 616640 | 12480 |
| s53(id=45 S3->S1) | sw06-p5 | Q6 | 624960 | 12480 |
| s53(id=45 S3->S1) | sw04-p4 | Q6 | 629120 | 12480 |
| s53(id=45 S3->S1) | sw02-p2 | Q6 | 633280 | 12480 |
| s37(id=29 S1->S2) | S1-p0 | Q7 | 274880 | 12480 |
| s37(id=29 S1->S2) | sw02-p4 | Q7 | 279040 | 12480 |
| s37(id=29 S1->S2) | sw04-p5 | Q7 | 283200 | 12480 |
| s37(id=29 S1->S2) | sw06-p4 | Q7 | 287360 | 12480 |
| s37(id=29 S1->S2) | sw08-p2 | Q7 | 291520 | 12480 |
| s38(id=30 S1->S2) | S1-p0 | Q7 | 287360 | 12480 |
| s38(id=30 S1->S2) | sw02-p4 | Q7 | 291520 | 12480 |
| s38(id=30 S1->S2) | sw04-p5 | Q7 | 295680 | 12480 |
| s38(id=30 S1->S2) | sw06-p4 | Q7 | 299840 | 12480 |
| s38(id=30 S1->S2) | sw08-p2 | Q7 | 304000 | 12480 |
| s48(id=40 S2->S1) | S2-p0 | Q7 | 212480 | 12480 |
| s48(id=40 S2->S1) | sw08-p4 | Q7 | 216640 | 12480 |
| s48(id=40 S2->S1) | sw06-p5 | Q7 | 220800 | 12480 |
| s48(id=40 S2->S1) | sw04-p4 | Q7 | 224960 | 12480 |
| s48(id=40 S2->S1) | sw02-p2 | Q7 | 229120 | 12480 |
| s43(id=35 S3->S1) | S3-p0 | Q7 | 212480 | 12480 |
| s43(id=35 S3->S1) | sw01-p4 | Q7 | 216960 | 12480 |
| s43(id=35 S3->S1) | sw03-p5 | Q7 | 221120 | 12480 |
| s43(id=35 S3->S1) | sw05-p4 | Q7 | 225280 | 12480 |
| s43(id=35 S3->S1) | sw07-p5 | Q7 | 237760 | 12480 |
| s43(id=35 S3->S1) | sw08-p4 | Q7 | 241920 | 12480 |
| s43(id=35 S3->S1) | sw06-p5 | Q7 | 246080 | 12480 |
| s43(id=35 S3->S1) | sw04-p4 | Q7 | 250240 | 12480 |
| s43(id=35 S3->S1) | sw02-p2 | Q7 | 254400 | 12480 |

## Constraint check

- C1-C7, C9: OK
- window-boundary integrity (no window's psi/delta changed anywhere): OK

## GCL per egress port

### sw01-p2  (25 entries, util 21.8400 %)

```
sgs 20800 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 11520 0x3F # 00111111   BE
sgs 34560 0x40 # 01000000   Q6
sgs 78080 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0x3F # 00111111   BE
sgs 14080 0x80 # 10000000   Q7
sgs 148160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 23680 0x40 # 01000000   Q6
sgs 125760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0x3F # 00111111   BE
sgs 14080 0x80 # 10000000   Q7
sgs 127360 0x3F # 00111111   BE
```

### sw01-p4  (24 entries, util 29.6400 %)

```
sgs 4480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 72640 0x40 # 01000000   Q6
sgs 23360 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 4480 0x3F # 00111111   BE
sgs 122240 0x80 # 10000000   Q7
sgs 23360 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 4480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 72640 0x40 # 01000000   Q6
sgs 23360 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 4480 0x3F # 00111111   BE
sgs 117760 0x80 # 10000000   Q7
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (10 entries, util 21.8400 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 446080 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p4  (28 entries, util 34.3200 %)

```
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 64000 0x40 # 01000000   Q6
sgs 7040 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 113920 0x80 # 10000000   Q7
sgs 7040 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 113920 0x80 # 10000000   Q7
sgs 7040 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 109760 0x80 # 10000000   Q7
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (25 entries, util 21.8400 %)

```
sgs 16640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 11520 0x3F # 00111111   BE
sgs 30720 0x40 # 01000000   Q6
sgs 81920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0x3F # 00111111   BE
sgs 13440 0x80 # 10000000   Q7
sgs 148800 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 21760 0x40 # 01000000   Q6
sgs 127680 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0x3F # 00111111   BE
sgs 13440 0x80 # 10000000   Q7
sgs 132160 0x3F # 00111111   BE
```

### sw03-p5  (24 entries, util 29.6400 %)

```
sgs 8640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 72640 0x40 # 01000000   Q6
sgs 19200 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 8640 0x3F # 00111111   BE
sgs 122240 0x80 # 10000000   Q7
sgs 19200 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 8640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 72640 0x40 # 01000000   Q6
sgs 19200 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 8640 0x3F # 00111111   BE
sgs 113600 0x80 # 10000000   Q7
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p4  (10 entries, util 21.8400 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 37440 0xBF # 10111111   Q7
sgs 450240 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (26 entries, util 34.3200 %)

```
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0x7F # 01111111   Q6
sgs 37120 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 64000 0x40 # 01000000   Q6
sgs 2880 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0x7F # 01111111   Q6
sgs 113600 0x80 # 10000000   Q7
sgs 2880 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0x7F # 01111111   Q6
sgs 113600 0x80 # 10000000   Q7
sgs 2880 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0x7F # 01111111   Q6
sgs 105280 0x80 # 10000000   Q7
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (24 entries, util 29.6400 %)

```
sgs 12800 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 72640 0x40 # 01000000   Q6
sgs 15040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 12800 0x7F # 01111111   Q6
sgs 122240 0x80 # 10000000   Q7
sgs 15040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 12800 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 72640 0x40 # 01000000   Q6
sgs 15040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 12800 0x7F # 01111111   Q6
sgs 109440 0x80 # 10000000   Q7
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p5  (25 entries, util 21.8400 %)

```
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 11520 0x3F # 00111111   BE
sgs 27840 0x40 # 01000000   Q6
sgs 84800 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0x3F # 00111111   BE
sgs 13440 0x80 # 10000000   Q7
sgs 148800 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 20160 0x40 # 01000000   Q6
sgs 129280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0x3F # 00111111   BE
sgs 13440 0x80 # 10000000   Q7
sgs 136320 0x3F # 00111111   BE
```

### sw06-p4  (23 entries, util 34.3200 %)

```
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0x7F # 01111111   Q6
sgs 37120 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 64000 0x40 # 01000000   Q6
sgs 48640 0xBF # 10111111   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0x7F # 01111111   Q6
sgs 113600 0x80 # 10000000   Q7
sgs 48640 0xBF # 10111111   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0x7F # 01111111   Q6
sgs 113600 0x80 # 10000000   Q7
sgs 48640 0xBF # 10111111   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0x7F # 01111111   Q6
sgs 101120 0x80 # 10000000   Q7
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (10 entries, util 21.8400 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 454400 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (25 entries, util 21.8400 %)

```
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 11520 0x3F # 00111111   BE
sgs 24960 0x40 # 01000000   Q6
sgs 87680 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0x3F # 00111111   BE
sgs 13120 0x80 # 10000000   Q7
sgs 149120 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 18880 0x40 # 01000000   Q6
sgs 130560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0x3F # 00111111   BE
sgs 13120 0x80 # 10000000   Q7
sgs 140800 0x3F # 00111111   BE
```

### sw07-p5  (24 entries, util 29.6400 %)

```
sgs 25280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 3840 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 80960 0x40 # 01000000   Q6
sgs 2560 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 25280 0x7F # 01111111   Q6
sgs 122240 0x80 # 10000000   Q7
sgs 2560 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 25280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 3840 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 80960 0x40 # 01000000   Q6
sgs 2560 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 25280 0x7F # 01111111   Q6
sgs 96960 0x80 # 10000000   Q7
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p2  (20 entries, util 45.2400 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 25280 0x80 # 10000000   Q7
sgs 3840 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 96000 0x40 # 01000000   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 150080 0x80 # 10000000   Q7
sgs 33280 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 25280 0x80 # 10000000   Q7
sgs 3840 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 96000 0x40 # 01000000   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 133440 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p4  (10 entries, util 21.8400 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 458560 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (25 entries, util 21.8400 %)

```
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 11520 0x3F # 00111111   BE
sgs 22720 0x40 # 01000000   Q6
sgs 89920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0x3F # 00111111   BE
sgs 13120 0x80 # 10000000   Q7
sgs 149120 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 17600 0x40 # 01000000   Q6
sgs 131840 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0x3F # 00111111   BE
sgs 13120 0x80 # 10000000   Q7
sgs 144960 0x3F # 00111111   BE
```

