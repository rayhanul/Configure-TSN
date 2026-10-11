# Reconfiguration-free admission (Problem 3)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Frozen schedule W loaded from: **result/result-2026-10-09-dataset-testbed-4-avgwin/rl-c9-on/4-matrix-c9on**

## Admission: W (before) vs. after this run's arrivals

| | admitted | of total |
|---|---|---|
| W (base, unchanged) | 11 | 11 |
| + this run's arrivals | 17 | 39 |

Every arrival admitted here required **zero** window-boundary changes -- see the GCL-entry table below (unchanged from W by construction) and the window-boundary integrity check. No previously-admitted flow was rerouted.

## Arrivals

| id | src->dst | RS(s) size | admitted | route | queue | phi_s (ns) | e2e (ns) | rerouted to make room | reason if rejected |
|---|---|---|---|---|---|---|---|---|---|
| 15 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 | 150080 | 43200 | - | - |
| 16 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 62400 | 33280 | - | - |
| 17 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 5 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q7 | 213120 | 78400 | - | - |
| 12 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 2 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 237440 | 35200 | - | - |
| 7 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 4 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q6 | 62400 | 64000 | - | - |
| 11 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 12480 | 70720 | - | - |
| 21 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 37440 | 84800 | - | - |
| 22 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 131520 | 89280 | - | - |
| 23 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 331520 | 89280 | - | - |
| 42 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q6 | 87360 | 51840 | - | - |
| 48 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q6 | 99840 | 52160 | - | - |
| 50 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 412480 | 70720 | - | - |
| 24 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q7 | 258560 | 45760 | - | - |
| 32 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 34 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 45 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q7 | 271040 | 49600 | - | - |
| 29 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 274880 | 33600 | - | - |
| 30 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 287360 | 33600 | - | - |
| 40 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 304320 | 70720 | - | - |
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
| sw01-p2 | 27 | 27 | 255 |
| sw01-p4 | 29 | 29 | 255 |
| sw02-p2 | 21 | 21 | 255 |
| sw02-p4 | 21 | 21 | 255 |
| sw03-p4 | 27 | 27 | 255 |
| sw03-p5 | 29 | 29 | 255 |
| sw04-p4 | 26 | 26 | 255 |
| sw04-p5 | 19 | 19 | 255 |
| sw05-p4 | 32 | 32 | 255 |
| sw05-p5 | 27 | 27 | 255 |
| sw06-p4 | 22 | 22 | 255 |
| sw06-p5 | 26 | 26 | 255 |
| sw07-p4 | 27 | 27 | 255 |
| sw07-p5 | 30 | 30 | 255 |
| sw08-p2 | 30 | 30 | 255 |
| sw08-p4 | 24 | 24 | 255 |
| sw08-p5 | 27 | 27 | 255 |

## Per-hop windows used by newly admitted flows

| flow | egress port | queue | psi (ns, unchanged) | delta (ns, unchanged) |
|---|---|---|---|---|
| s26(id=15 S3->S2) | S3-p0 | Q7 | 150080 | 12480 |
| s26(id=15 S3->S2) | sw01-p4 | Q7 | 154560 | 12480 |
| s26(id=15 S3->S2) | sw03-p5 | Q7 | 158720 | 12480 |
| s26(id=15 S3->S2) | sw05-p4 | Q7 | 162880 | 12480 |
| s26(id=15 S3->S2) | sw07-p5 | Q7 | 175360 | 12480 |
| s26(id=15 S3->S2) | sw08-p2 | Q7 | 180800 | 12480 |
| s27(id=16 S1->S2) | S1-p0 | Q7 | 62400 | 12480 |
| s27(id=16 S1->S2) | sw02-p4 | Q7 | 66560 | 12480 |
| s27(id=16 S1->S2) | sw04-p5 | Q7 | 70720 | 12480 |
| s27(id=16 S1->S2) | sw06-p4 | Q7 | 74880 | 12480 |
| s27(id=16 S1->S2) | sw08-p2 | Q7 | 83200 | 12480 |
| s22(id=5 S3->S1) | S3-p0 | Q7 | 213120 | 12480 |
| s22(id=5 S3->S1) | sw01-p4 | Q7 | 249920 | 12480 |
| s22(id=5 S3->S1) | sw03-p5 | Q7 | 254080 | 12480 |
| s22(id=5 S3->S1) | sw05-p4 | Q7 | 258240 | 12480 |
| s22(id=5 S3->S1) | sw07-p5 | Q7 | 262400 | 12480 |
| s22(id=5 S3->S1) | sw08-p4 | Q7 | 266560 | 12480 |
| s22(id=5 S3->S1) | sw06-p5 | Q7 | 270720 | 12480 |
| s22(id=5 S3->S1) | sw04-p4 | Q7 | 274880 | 12480 |
| s22(id=5 S3->S1) | sw02-p2 | Q7 | 279040 | 12480 |
| s20(id=2 S1->S2) | S1-p0 | Q7 | 237440 | 12480 |
| s20(id=2 S1->S2) | sw02-p4 | Q7 | 241600 | 12480 |
| s20(id=2 S1->S2) | sw04-p5 | Q7 | 246080 | 12480 |
| s20(id=2 S1->S2) | sw06-p4 | Q7 | 250240 | 12480 |
| s20(id=2 S1->S2) | sw08-p2 | Q7 | 260160 | 12480 |
| s21(id=4 S3->S2) | S3-p0 | Q6 | 62400 | 12480 |
| s21(id=4 S3->S2) | sw01-p4 | Q6 | 97280 | 12480 |
| s21(id=4 S3->S2) | sw03-p5 | Q6 | 101440 | 12480 |
| s21(id=4 S3->S2) | sw05-p4 | Q6 | 105600 | 12480 |
| s21(id=4 S3->S2) | sw07-p5 | Q6 | 109760 | 12480 |
| s21(id=4 S3->S2) | sw08-p2 | Q6 | 113920 | 12480 |
| s24(id=11 S2->S1) | S2-p0 | Q6 | 12480 | 12480 |
| s24(id=11 S2->S1) | sw08-p4 | Q6 | 29120 | 12480 |
| s24(id=11 S2->S1) | sw06-p5 | Q6 | 33280 | 12480 |
| s24(id=11 S2->S1) | sw04-p4 | Q6 | 37440 | 12480 |
| s24(id=11 S2->S1) | sw02-p2 | Q6 | 70720 | 12480 |
| s29(id=21 S2->S1) | S2-p0 | Q6 | 37440 | 12480 |
| s29(id=21 S2->S1) | sw08-p4 | Q6 | 41600 | 12480 |
| s29(id=21 S2->S1) | sw06-p5 | Q6 | 62400 | 12480 |
| s29(id=21 S2->S1) | sw04-p4 | Q6 | 105600 | 12480 |
| s29(id=21 S2->S1) | sw02-p2 | Q6 | 109760 | 12480 |
| s30(id=22 S2->S1) | S2-p0 | Q6 | 131520 | 12480 |
| s30(id=22 S2->S1) | sw08-p4 | Q6 | 135680 | 12480 |
| s30(id=22 S2->S1) | sw06-p5 | Q6 | 200000 | 12480 |
| s30(id=22 S2->S1) | sw04-p4 | Q6 | 204160 | 12480 |
| s30(id=22 S2->S1) | sw02-p2 | Q6 | 208320 | 12480 |
| s31(id=23 S2->S1) | S2-p0 | Q6 | 331520 | 12480 |
| s31(id=23 S2->S1) | sw08-p4 | Q6 | 335680 | 12480 |
| s31(id=23 S2->S1) | sw06-p5 | Q6 | 400000 | 12480 |
| s31(id=23 S2->S1) | sw04-p4 | Q6 | 404160 | 12480 |
| s31(id=23 S2->S1) | sw02-p2 | Q6 | 408320 | 12480 |
| s50(id=42 S1->S2) | S1-p0 | Q6 | 87360 | 12480 |
| s50(id=42 S1->S2) | sw02-p4 | Q6 | 91520 | 12480 |
| s50(id=42 S1->S2) | sw04-p5 | Q6 | 95680 | 12480 |
| s50(id=42 S1->S2) | sw06-p4 | Q6 | 122560 | 12480 |
| s50(id=42 S1->S2) | sw08-p2 | Q6 | 126720 | 12480 |
| s56(id=48 S1->S2) | S1-p0 | Q6 | 99840 | 12480 |
| s56(id=48 S1->S2) | sw02-p4 | Q6 | 104000 | 12480 |
| s56(id=48 S1->S2) | sw04-p5 | Q6 | 131200 | 12480 |
| s56(id=48 S1->S2) | sw06-p4 | Q6 | 135360 | 12480 |
| s56(id=48 S1->S2) | sw08-p2 | Q6 | 139520 | 12480 |
| s58(id=50 S2->S1) | S2-p0 | Q6 | 412480 | 12480 |
| s58(id=50 S2->S1) | sw08-p4 | Q6 | 429120 | 12480 |
| s58(id=50 S2->S1) | sw06-p5 | Q6 | 433280 | 12480 |
| s58(id=50 S2->S1) | sw04-p4 | Q6 | 437440 | 12480 |
| s58(id=50 S2->S1) | sw02-p2 | Q6 | 470720 | 12480 |
| s32(id=24 S3->S1) | S3-p0 | Q7 | 258560 | 12480 |
| s32(id=24 S3->S1) | sw01-p4 | Q7 | 262720 | 12480 |
| s32(id=24 S3->S1) | sw03-p5 | Q7 | 266880 | 12480 |
| s32(id=24 S3->S1) | sw05-p4 | Q7 | 271040 | 12480 |
| s32(id=24 S3->S1) | sw07-p5 | Q7 | 275200 | 12480 |
| s32(id=24 S3->S1) | sw08-p4 | Q7 | 279360 | 12480 |
| s32(id=24 S3->S1) | sw06-p5 | Q7 | 283520 | 12480 |
| s32(id=24 S3->S1) | sw04-p4 | Q7 | 287680 | 12480 |
| s32(id=24 S3->S1) | sw02-p2 | Q7 | 291840 | 12480 |
| s53(id=45 S3->S1) | S3-p0 | Q7 | 271040 | 12480 |
| s53(id=45 S3->S1) | sw01-p4 | Q7 | 278080 | 12480 |
| s53(id=45 S3->S1) | sw03-p5 | Q7 | 282560 | 12480 |
| s53(id=45 S3->S1) | sw05-p4 | Q7 | 287040 | 12480 |
| s53(id=45 S3->S1) | sw07-p5 | Q7 | 291520 | 12480 |
| s53(id=45 S3->S1) | sw08-p4 | Q7 | 295680 | 12480 |
| s53(id=45 S3->S1) | sw06-p5 | Q7 | 299840 | 12480 |
| s53(id=45 S3->S1) | sw04-p4 | Q7 | 304000 | 12480 |
| s53(id=45 S3->S1) | sw02-p2 | Q7 | 308160 | 12480 |
| s37(id=29 S1->S2) | S1-p0 | Q7 | 274880 | 12480 |
| s37(id=29 S1->S2) | sw02-p4 | Q7 | 279040 | 12480 |
| s37(id=29 S1->S2) | sw04-p5 | Q7 | 283200 | 12480 |
| s37(id=29 S1->S2) | sw06-p4 | Q7 | 287360 | 12480 |
| s37(id=29 S1->S2) | sw08-p2 | Q7 | 296000 | 12480 |
| s38(id=30 S1->S2) | S1-p0 | Q7 | 287360 | 12480 |
| s38(id=30 S1->S2) | sw02-p4 | Q7 | 291520 | 12480 |
| s38(id=30 S1->S2) | sw04-p5 | Q7 | 295680 | 12480 |
| s38(id=30 S1->S2) | sw06-p4 | Q7 | 299840 | 12480 |
| s38(id=30 S1->S2) | sw08-p2 | Q7 | 308480 | 12480 |
| s48(id=40 S2->S1) | S2-p0 | Q7 | 304320 | 12480 |
| s48(id=40 S2->S1) | sw08-p4 | Q7 | 308480 | 12480 |
| s48(id=40 S2->S1) | sw06-p5 | Q7 | 312640 | 12480 |
| s48(id=40 S2->S1) | sw04-p4 | Q7 | 316800 | 12480 |
| s48(id=40 S2->S1) | sw02-p2 | Q7 | 320960 | 12480 |

## Constraint check

- C1-C7, C9: OK
- window-boundary integrity (no window's psi/delta changed anywhere): OK

## GCL per egress port

### sw01-p2  (27 entries, util 21.8400 %)

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
sgs 12480 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 81920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 149760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 136960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 128960 0x3F # 00111111   BE
```

### sw01-p4  (29 entries, util 26.5200 %)

```
sgs 4480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 11520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 6720 0x3F # 00111111   BE
sgs 57280 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 23680 0x80 # 10000000   Q7
sgs 21760 0x7F # 01111111   Q6
sgs 28160 0xBF # 10111111   Q7
sgs 76480 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 11520 0x3F # 00111111   BE
sgs 76480 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
sgs 23680 0x80 # 10000000   Q7
sgs 21760 0x7F # 01111111   Q6
sgs 28160 0xBF # 10111111   Q7
sgs 72000 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (21 entries, util 18.7200 %)

```
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 29120 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 5760 0x3F # 00111111   BE
sgs 32000 0x40 # 01000000   Q6
sgs 58240 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 112640 0x80 # 10000000   Q7
sgs 58240 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 29120 0xBF # 10111111   Q7
sgs 71040 0x40 # 01000000   Q6
sgs 58240 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 83520 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p4  (21 entries, util 34.3200 %)

```
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 64000 0x40 # 01000000   Q6
sgs 61120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 113920 0x80 # 10000000   Q7
sgs 61120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 113920 0x80 # 10000000   Q7
sgs 61120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 109760 0x80 # 10000000   Q7
sgs 61120 0xBF # 10111111   Q7
```

### sw03-p4  (27 entries, util 21.8400 %)

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
sgs 12480 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 81920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 149760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 136960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 133120 0x3F # 00111111   BE
```

### sw03-p5  (29 entries, util 26.5200 %)

```
sgs 8640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 11840 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 6400 0x3F # 00111111   BE
sgs 57280 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 24000 0x80 # 10000000   Q7
sgs 17280 0x7F # 01111111   Q6
sgs 32640 0xBF # 10111111   Q7
sgs 76160 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 11840 0x3F # 00111111   BE
sgs 76160 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
sgs 24000 0x80 # 10000000   Q7
sgs 17280 0x7F # 01111111   Q6
sgs 32640 0xBF # 10111111   Q7
sgs 67520 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p4  (26 entries, util 18.7200 %)

```
sgs 24960 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 5760 0x3F # 00111111   BE
sgs 32000 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 112640 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 71040 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 87680 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (19 entries, util 34.3200 %)

```
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0x7F # 01111111   Q6
sgs 37120 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 64000 0x40 # 01000000   Q6
sgs 61120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0x7F # 01111111   Q6
sgs 113600 0x80 # 10000000   Q7
sgs 61120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0x7F # 01111111   Q6
sgs 113600 0x80 # 10000000   Q7
sgs 61120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0x7F # 01111111   Q6
sgs 105280 0x80 # 10000000   Q7
sgs 61120 0xBF # 10111111   Q7
```

### sw05-p4  (32 entries, util 26.5200 %)

```
sgs 12800 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 6080 0x3F # 00111111   BE
sgs 57280 0x40 # 01000000   Q6
sgs 37120 0xBF # 10111111   Q7
sgs 12800 0x7F # 01111111   Q6
sgs 24320 0x80 # 10000000   Q7
sgs 12800 0x7F # 01111111   Q6
sgs 37120 0xBF # 10111111   Q7
sgs 75840 0x80 # 10000000   Q7
sgs 37120 0xBF # 10111111   Q7
sgs 12800 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12160 0x3F # 00111111   BE
sgs 75840 0x80 # 10000000   Q7
sgs 37120 0xBF # 10111111   Q7
sgs 12800 0x7F # 01111111   Q6
sgs 24320 0x80 # 10000000   Q7
sgs 12800 0x7F # 01111111   Q6
sgs 37120 0xBF # 10111111   Q7
sgs 63040 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p5  (27 entries, util 21.8400 %)

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
sgs 12480 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 81920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 149760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 136960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 137280 0x3F # 00111111   BE
```

### sw06-p4  (22 entries, util 34.3200 %)

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
sgs 61120 0xBF # 10111111   Q7
```

### sw06-p5  (26 entries, util 18.7200 %)

```
sgs 20800 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 5760 0x3F # 00111111   BE
sgs 32000 0x40 # 01000000   Q6
sgs 16640 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 112640 0x80 # 10000000   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 71040 0x40 # 01000000   Q6
sgs 16640 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 91840 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (27 entries, util 21.8400 %)

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
sgs 12480 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 81920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 149760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 136960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 141440 0x3F # 00111111   BE
```

### sw07-p5  (30 entries, util 26.5200 %)

```
sgs 25280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 3840 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 5760 0x3F # 00111111   BE
sgs 65600 0x40 # 01000000   Q6
sgs 24640 0xBF # 10111111   Q7
sgs 25280 0x7F # 01111111   Q6
sgs 16320 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
sgs 83840 0x80 # 10000000   Q7
sgs 24640 0xBF # 10111111   Q7
sgs 25280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 3840 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 83840 0x80 # 10000000   Q7
sgs 24640 0xBF # 10111111   Q7
sgs 25280 0x7F # 01111111   Q6
sgs 16320 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
sgs 58560 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p2  (30 entries, util 45.2400 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 25280 0x80 # 10000000   Q7
sgs 3840 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12800 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 5440 0x3F # 00111111   BE
sgs 66880 0x40 # 01000000   Q6
sgs 19200 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 43520 0x80 # 10000000   Q7
sgs 35840 0xBF # 10111111   Q7
sgs 84800 0x80 # 10000000   Q7
sgs 19200 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 25280 0x80 # 10000000   Q7
sgs 3840 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12800 0xBF # 10111111   Q7
sgs 84800 0x80 # 10000000   Q7
sgs 19200 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 43520 0x80 # 10000000   Q7
sgs 35840 0xBF # 10111111   Q7
sgs 68160 0x80 # 10000000   Q7
sgs 35840 0xBF # 10111111   Q7
```

### sw08-p4  (24 entries, util 18.7200 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 5760 0x3F # 00111111   BE
sgs 32000 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 112640 0x80 # 10000000   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 71040 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 96000 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (27 entries, util 21.8400 %)

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
sgs 12480 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 81920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 149760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 136960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 145600 0x3F # 00111111   BE
```

