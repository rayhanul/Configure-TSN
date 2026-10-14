# Reconfiguration-free admission (Problem 3)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Frozen schedule W loaded from: **result/result-2026-10-13-dataset-testbed-11-tree-avgwin/rl-c9-off/11-matrix-c9off**

## Admission: W (before) vs. after this run's arrivals

| | admitted | of total |
|---|---|---|
| W (base, unchanged) | 10 | 10 |
| + this run's arrivals | 15 | 40 |

Every arrival admitted here required **zero** window-boundary changes -- see the GCL-entry table below (unchanged from W by construction) and the window-boundary integrity check. No previously-admitted flow was rerouted.

## Arrivals

| id | src->dst | RS(s) size | admitted | route | queue | phi_s (ns) | e2e (ns) | rerouted to make room | reason if rejected |
|---|---|---|---|---|---|---|---|---|---|
| 6 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 11 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 14 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 16 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q7 | 165120 | 192960 | - | - |
| 4 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 12480 | 108160 | - | - |
| 12 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 49920 | 126400 | - | - |
| 17 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q6 | 37440 | 109760 | - | - |
| 13 | S1->S3 | - | yes | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 141760 | 366400 | - | - |
| 19 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q7 | 177920 | 380160 | - | - |
| 15 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 127680 | 134080 | - | - |
| 23 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 24960 | 115840 | - | - |
| 25 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 327680 | 175680 | - | - |
| 27 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 28 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 291840 | 79040 | - | - |
| 36 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 424960 | 183040 | - | - |
| 49 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 50 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 304640 | 79040 | - | - |
| 48 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 37 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q6 | 62400 | 145600 | - | - |
| 46 | S1->S3 | - | yes | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 62400 | 233280 | - | - |
| 33 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 34 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 35 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 41 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 44 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 22 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 40 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 42 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 43 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 39 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q6 | 87360 | 216000 | - | - |
| 21 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 24 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 31 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 32 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 29 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 38 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 26 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 30 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 45 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 47 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |

## Per-port GCL entries (should equal W exactly)

| port | W entries | after arrivals | GCL_size |
|---|---|---|---|
| sw01-p2 | 17 | 17 | 255 |
| sw01-p4 | 29 | 29 | 255 |
| sw02-p2 | 28 | 28 | 255 |
| sw02-p4 | 22 | 22 | 255 |
| sw03-p4 | 18 | 18 | 255 |
| sw03-p5 | 26 | 26 | 255 |
| sw04-p4 | 27 | 27 | 255 |
| sw04-p5 | 22 | 22 | 255 |
| sw05-p4 | 27 | 27 | 255 |
| sw05-p5 | 18 | 18 | 255 |
| sw06-p4 | 25 | 25 | 255 |
| sw06-p5 | 26 | 26 | 255 |
| sw07-p4 | 16 | 16 | 255 |
| sw07-p5 | 30 | 30 | 255 |
| sw08-p2 | 31 | 31 | 255 |
| sw08-p4 | 27 | 27 | 255 |
| sw08-p5 | 17 | 17 | 255 |

## Per-hop windows used by newly admitted flows

| flow | egress port | queue | psi (ns, unchanged) | delta (ns, unchanged) |
|---|---|---|---|---|
| s27(id=16 S3->S1) | S3-p0 | Q7 | 165120 | 12480 |
| s27(id=16 S3->S1) | sw01-p4 | Q7 | 181760 | 12480 |
| s27(id=16 S3->S1) | sw03-p5 | Q7 | 245760 | 12480 |
| s27(id=16 S3->S1) | sw05-p4 | Q7 | 262400 | 12480 |
| s27(id=16 S3->S1) | sw07-p5 | Q7 | 279040 | 12480 |
| s27(id=16 S3->S1) | sw08-p4 | Q7 | 295680 | 12480 |
| s27(id=16 S3->S1) | sw06-p5 | Q7 | 312320 | 12480 |
| s27(id=16 S3->S1) | sw04-p4 | Q7 | 328960 | 12480 |
| s27(id=16 S3->S1) | sw02-p2 | Q7 | 345600 | 12480 |
| s20(id=4 S2->S3) | S2-p0 | Q6 | 12480 | 12480 |
| s20(id=4 S2->S3) | sw08-p5 | Q6 | 41600 | 12480 |
| s20(id=4 S2->S3) | sw07-p4 | Q6 | 58240 | 12480 |
| s20(id=4 S2->S3) | sw05-p5 | Q6 | 74880 | 12480 |
| s20(id=4 S2->S3) | sw03-p4 | Q6 | 91520 | 12480 |
| s20(id=4 S2->S3) | sw01-p2 | Q6 | 108160 | 12480 |
| s23(id=12 S2->S3) | S2-p0 | Q6 | 49920 | 12480 |
| s23(id=12 S2->S3) | sw08-p5 | Q6 | 97280 | 12480 |
| s23(id=12 S2->S3) | sw07-p4 | Q6 | 113920 | 12480 |
| s23(id=12 S2->S3) | sw05-p5 | Q6 | 130560 | 12480 |
| s23(id=12 S2->S3) | sw03-p4 | Q6 | 147200 | 12480 |
| s23(id=12 S2->S3) | sw01-p2 | Q6 | 163840 | 12480 |
| s28(id=17 S1->S2) | S1-p0 | Q6 | 37440 | 12480 |
| s28(id=17 S1->S2) | sw02-p4 | Q6 | 54080 | 12480 |
| s28(id=17 S1->S2) | sw04-p5 | Q6 | 70720 | 12480 |
| s28(id=17 S1->S2) | sw06-p4 | Q6 | 118080 | 12480 |
| s28(id=17 S1->S2) | sw08-p2 | Q6 | 134720 | 12480 |
| s24(id=13 S1->S3) | S1-p0 | Q7 | 141760 | 12480 |
| s24(id=13 S1->S3) | sw02-p4 | Q7 | 158400 | 12480 |
| s24(id=13 S1->S3) | sw04-p5 | Q7 | 175040 | 12480 |
| s24(id=13 S1->S3) | sw06-p4 | Q7 | 386560 | 12480 |
| s24(id=13 S1->S3) | sw08-p5 | Q7 | 429120 | 12480 |
| s24(id=13 S1->S3) | sw07-p4 | Q7 | 445760 | 12480 |
| s24(id=13 S1->S3) | sw05-p5 | Q7 | 462400 | 12480 |
| s24(id=13 S1->S3) | sw03-p4 | Q7 | 479040 | 12480 |
| s24(id=13 S1->S3) | sw01-p2 | Q7 | 495680 | 12480 |
| s29(id=19 S3->S1) | S3-p0 | Q7 | 177920 | 12480 |
| s29(id=19 S3->S1) | sw01-p4 | Q7 | 381760 | 12480 |
| s29(id=19 S3->S1) | sw03-p5 | Q7 | 445760 | 12480 |
| s29(id=19 S3->S1) | sw05-p4 | Q7 | 462400 | 12480 |
| s29(id=19 S3->S1) | sw07-p5 | Q7 | 479040 | 12480 |
| s29(id=19 S3->S1) | sw08-p4 | Q7 | 495680 | 12480 |
| s29(id=19 S3->S1) | sw06-p5 | Q7 | 512320 | 12480 |
| s29(id=19 S3->S1) | sw04-p4 | Q7 | 528960 | 12480 |
| s29(id=19 S3->S1) | sw02-p2 | Q7 | 545600 | 12480 |
| s26(id=15 S2->S3) | S2-p0 | Q6 | 127680 | 12480 |
| s26(id=15 S2->S3) | sw08-p5 | Q6 | 182720 | 12480 |
| s26(id=15 S2->S3) | sw07-p4 | Q6 | 199360 | 12480 |
| s26(id=15 S2->S3) | sw05-p5 | Q6 | 216000 | 12480 |
| s26(id=15 S2->S3) | sw03-p4 | Q6 | 232640 | 12480 |
| s26(id=15 S2->S3) | sw01-p2 | Q6 | 249280 | 12480 |
| s32(id=23 S2->S1) | S2-p0 | Q6 | 24960 | 12480 |
| s32(id=23 S2->S1) | sw08-p4 | Q6 | 41600 | 12480 |
| s32(id=23 S2->S1) | sw06-p5 | Q6 | 95040 | 12480 |
| s32(id=23 S2->S1) | sw04-p4 | Q6 | 111680 | 12480 |
| s32(id=23 S2->S1) | sw02-p2 | Q6 | 128320 | 12480 |
| s34(id=25 S2->S1) | S2-p0 | Q6 | 327680 | 12480 |
| s34(id=25 S2->S1) | sw08-p4 | Q6 | 400000 | 12480 |
| s34(id=25 S2->S1) | sw06-p5 | Q6 | 416640 | 12480 |
| s34(id=25 S2->S1) | sw04-p4 | Q6 | 433280 | 12480 |
| s34(id=25 S2->S1) | sw02-p2 | Q6 | 490880 | 12480 |
| s37(id=28 S2->S1) | S2-p0 | Q7 | 291840 | 12480 |
| s37(id=28 S2->S1) | sw08-p4 | Q7 | 308480 | 12480 |
| s37(id=28 S2->S1) | sw06-p5 | Q7 | 325120 | 12480 |
| s37(id=28 S2->S1) | sw04-p4 | Q7 | 341760 | 12480 |
| s37(id=28 S2->S1) | sw02-p2 | Q7 | 358400 | 12480 |
| s45(id=36 S2->S1) | S2-p0 | Q6 | 424960 | 12480 |
| s45(id=36 S2->S1) | sw08-p4 | Q6 | 508160 | 12480 |
| s45(id=36 S2->S1) | sw06-p5 | Q6 | 524800 | 12480 |
| s45(id=36 S2->S1) | sw04-p4 | Q6 | 578880 | 12480 |
| s45(id=36 S2->S1) | sw02-p2 | Q6 | 595520 | 12480 |
| s59(id=50 S2->S1) | S2-p0 | Q7 | 304640 | 12480 |
| s59(id=50 S2->S1) | sw08-p4 | Q7 | 321280 | 12480 |
| s59(id=50 S2->S1) | sw06-p5 | Q7 | 337920 | 12480 |
| s59(id=50 S2->S1) | sw04-p4 | Q7 | 354560 | 12480 |
| s59(id=50 S2->S1) | sw02-p2 | Q7 | 371200 | 12480 |
| s46(id=37 S3->S1) | S3-p0 | Q6 | 62400 | 12480 |
| s46(id=37 S3->S1) | sw01-p4 | Q6 | 79040 | 12480 |
| s46(id=37 S3->S1) | sw03-p5 | Q6 | 95680 | 12480 |
| s46(id=37 S3->S1) | sw05-p4 | Q6 | 112320 | 12480 |
| s46(id=37 S3->S1) | sw07-p5 | Q6 | 128960 | 12480 |
| s46(id=37 S3->S1) | sw08-p4 | Q6 | 145600 | 12480 |
| s46(id=37 S3->S1) | sw06-p5 | Q6 | 162240 | 12480 |
| s46(id=37 S3->S1) | sw04-p4 | Q6 | 178880 | 12480 |
| s46(id=37 S3->S1) | sw02-p2 | Q6 | 195520 | 12480 |
| s55(id=46 S1->S3) | S1-p0 | Q6 | 62400 | 12480 |
| s55(id=46 S1->S3) | sw02-p4 | Q6 | 109760 | 12480 |
| s55(id=46 S1->S3) | sw04-p5 | Q6 | 126400 | 12480 |
| s55(id=46 S1->S3) | sw06-p4 | Q6 | 200000 | 12480 |
| s55(id=46 S1->S3) | sw08-p5 | Q6 | 216640 | 12480 |
| s55(id=46 S1->S3) | sw07-p4 | Q6 | 233280 | 12480 |
| s55(id=46 S1->S3) | sw05-p5 | Q6 | 249920 | 12480 |
| s55(id=46 S1->S3) | sw03-p4 | Q6 | 266560 | 12480 |
| s55(id=46 S1->S3) | sw01-p2 | Q6 | 283200 | 12480 |
| s48(id=39 S3->S1) | S3-p0 | Q6 | 87360 | 12480 |
| s48(id=39 S3->S1) | sw01-p4 | Q6 | 104000 | 12480 |
| s48(id=39 S3->S1) | sw03-p5 | Q6 | 120640 | 12480 |
| s48(id=39 S3->S1) | sw05-p4 | Q6 | 137280 | 12480 |
| s48(id=39 S3->S1) | sw07-p5 | Q6 | 184640 | 12480 |
| s48(id=39 S3->S1) | sw08-p4 | Q6 | 201280 | 12480 |
| s48(id=39 S3->S1) | sw06-p5 | Q6 | 217920 | 12480 |
| s48(id=39 S3->S1) | sw04-p4 | Q6 | 234560 | 12480 |
| s48(id=39 S3->S1) | sw02-p2 | Q6 | 290880 | 12480 |

## Constraint check

- C1-C7, C9: OK
- window-boundary integrity (no window's psi/delta changed anywhere): OK

## GCL per egress port

### sw01-p2  (17 entries, util 12.4800 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 45760 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 24960 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 5760 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 23680 0xBF # 10111111   Q7
sgs 49280 0x7F # 01111111   Q6
sgs 148160 0x40 # 01000000   Q6
sgs 52480 0x7F # 01111111   Q6
sgs 45760 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 193600 0x40 # 01000000   Q6
sgs 48320 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p4  (29 entries, util 26.5200 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 47040 0x40 # 01000000   Q6
sgs 18240 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 140160 0x40 # 01000000   Q6
sgs 18240 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 102720 0x40 # 01000000   Q6
sgs 18240 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 123520 0x40 # 01000000   Q6
sgs 34880 0xBF # 10111111   Q7
```

### sw02-p2  (28 entries, util 28.0800 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 24320 0x80 # 10000000   Q7
sgs 21760 0x7F # 01111111   Q6
sgs 32960 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 16320 0x40 # 01000000   Q6
sgs 38080 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 24320 0x80 # 10000000   Q7
sgs 54720 0x7F # 01111111   Q6
sgs 66240 0x80 # 10000000   Q7
sgs 38080 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 24320 0x80 # 10000000   Q7
sgs 54720 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 16320 0x40 # 01000000   Q6
sgs 38080 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 24320 0x80 # 10000000   Q7
sgs 54720 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 41920 0xBF # 10111111   Q7
```

### sw02-p4  (22 entries, util 18.7200 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 30720 0xBF # 10111111   Q7
sgs 48640 0x40 # 01000000   Q6
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

### sw03-p4  (18 entries, util 12.4800 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 24960 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 5760 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 40320 0xBF # 10111111   Q7
sgs 32640 0x7F # 01111111   Q6
sgs 148160 0x40 # 01000000   Q6
sgs 19200 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 210240 0x40 # 01000000   Q6
sgs 48320 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p5  (26 entries, util 26.5200 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 47040 0x40 # 01000000   Q6
sgs 34880 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 140160 0x40 # 01000000   Q6
sgs 34880 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 102720 0x40 # 01000000   Q6
sgs 34880 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 106880 0x40 # 01000000   Q6
sgs 34880 0xBF # 10111111   Q7
```

### sw04-p4  (27 entries, util 28.0800 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 24320 0x80 # 10000000   Q7
sgs 38400 0x7F # 01111111   Q6
sgs 16320 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 16320 0x40 # 01000000   Q6
sgs 54720 0x7F # 01111111   Q6
sgs 24320 0x80 # 10000000   Q7
sgs 25920 0xBF # 10111111   Q7
sgs 28800 0x7F # 01111111   Q6
sgs 66240 0x80 # 10000000   Q7
sgs 54720 0x7F # 01111111   Q6
sgs 24320 0x80 # 10000000   Q7
sgs 25920 0xBF # 10111111   Q7
sgs 28800 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 16320 0x40 # 01000000   Q6
sgs 54720 0x7F # 01111111   Q6
sgs 24320 0x80 # 10000000   Q7
sgs 25920 0xBF # 10111111   Q7
sgs 28800 0x7F # 01111111   Q6
sgs 16320 0x80 # 10000000   Q7
sgs 54720 0xBF # 10111111   Q7
```

### sw04-p5  (22 entries, util 18.7200 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 53760 0x7F # 01111111   Q6
sgs 25600 0x40 # 01000000   Q6
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

### sw05-p4  (27 entries, util 26.5200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0x7F # 01111111   Q6
sgs 17920 0xBF # 10111111   Q7
sgs 47040 0x40 # 01000000   Q6
sgs 34880 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 140160 0x40 # 01000000   Q6
sgs 34880 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 102720 0x40 # 01000000   Q6
sgs 34880 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 90240 0x40 # 01000000   Q6
sgs 34880 0xBF # 10111111   Q7
```

### sw05-p5  (18 entries, util 12.4800 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 5760 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 56960 0xBF # 10111111   Q7
sgs 16000 0x7F # 01111111   Q6
sgs 148160 0x40 # 01000000   Q6
sgs 35840 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 226880 0x40 # 01000000   Q6
sgs 48320 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p4  (25 entries, util 18.7200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 17600 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 640 0x3F # 00111111   BE
sgs 68480 0x40 # 01000000   Q6
sgs 13440 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 136640 0x40 # 01000000   Q6
sgs 13440 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 17600 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 640 0x3F # 00111111   BE
sgs 68480 0x40 # 01000000   Q6
sgs 13440 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 86720 0x40 # 01000000   Q6
sgs 13440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (26 entries, util 28.0800 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 24320 0x80 # 10000000   Q7
sgs 54720 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 16320 0x40 # 01000000   Q6
sgs 21440 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 24320 0x80 # 10000000   Q7
sgs 54720 0xBF # 10111111   Q7
sgs 66240 0x80 # 10000000   Q7
sgs 21440 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 24320 0x80 # 10000000   Q7
sgs 54720 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 16320 0x40 # 01000000   Q6
sgs 21440 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 24320 0x80 # 10000000   Q7
sgs 54720 0xBF # 10111111   Q7
sgs 32960 0x80 # 10000000   Q7
sgs 54720 0xBF # 10111111   Q7
```

### sw07-p4  (16 entries, util 12.4800 %)

```
sgs 45760 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 5760 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 23680 0x7F # 01111111   Q6
sgs 49280 0xBF # 10111111   Q7
sgs 148160 0x40 # 01000000   Q6
sgs 52480 0xBF # 10111111   Q7
sgs 45760 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 243520 0x40 # 01000000   Q6
sgs 48320 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p5  (30 entries, util 26.5200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 30720 0xBF # 10111111   Q7
sgs 47040 0x40 # 01000000   Q6
sgs 18240 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 140160 0x40 # 01000000   Q6
sgs 18240 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 102720 0x40 # 01000000   Q6
sgs 18240 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 73600 0x40 # 01000000   Q6
sgs 34880 0xBF # 10111111   Q7
```

### sw08-p2  (31 entries, util 29.6400 %)

```
sgs 66560 0x3F # 00111111   BE
sgs 29120 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 10880 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 96000 0x3F # 00111111   BE
sgs 29120 0x40 # 01000000   Q6
sgs 13120 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 145280 0x3F # 00111111   BE
sgs 29120 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 119360 0x3F # 00111111   BE
sgs 29120 0x40 # 01000000   Q6
sgs 13120 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 78720 0x3F # 00111111   BE
```

### sw08-p4  (27 entries, util 28.0800 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 24320 0x80 # 10000000   Q7
sgs 21760 0xBF # 10111111   Q7
sgs 32960 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 16320 0x40 # 01000000   Q6
sgs 38080 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 24320 0x80 # 10000000   Q7
sgs 54720 0xBF # 10111111   Q7
sgs 66240 0x80 # 10000000   Q7
sgs 38080 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 24320 0x80 # 10000000   Q7
sgs 54720 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 16320 0x40 # 01000000   Q6
sgs 38080 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 24320 0x80 # 10000000   Q7
sgs 54720 0xBF # 10111111   Q7
sgs 49600 0x80 # 10000000   Q7
sgs 54720 0xBF # 10111111   Q7
```

### sw08-p5  (17 entries, util 12.4800 %)

```
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 5760 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 40320 0x7F # 01111111   Q6
sgs 32640 0xBF # 10111111   Q7
sgs 148160 0x40 # 01000000   Q6
sgs 19200 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 260160 0x40 # 01000000   Q6
sgs 48320 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

