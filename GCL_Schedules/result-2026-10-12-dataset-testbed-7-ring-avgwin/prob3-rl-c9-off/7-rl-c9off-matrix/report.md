# Reconfiguration-free admission (Problem 3)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Frozen schedule W loaded from: **result/result-2026-10-12-dataset-testbed-7-ring-avgwin/rl-c9-off/7-matrix-c9off**

## Admission: W (before) vs. after this run's arrivals

| | admitted | of total |
|---|---|---|
| W (base, unchanged) | 11 | 11 |
| + this run's arrivals | 17 | 39 |

Every arrival admitted here required **zero** window-boundary changes -- see the GCL-entry table below (unchanged from W by construction) and the window-boundary integrity check. No previously-admitted flow was rerouted.

## Arrivals

| id | src->dst | RS(s) size | admitted | route | queue | phi_s (ns) | e2e (ns) | rerouted to make room | reason if rejected |
|---|---|---|---|---|---|---|---|---|---|
| 10 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 6 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 2 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 | 37440 | 157120 | - | - |
| 11 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 12480 | 159040 | - | - |
| 17 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q6 | 12480 | 96320 | - | - |
| 14 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q7 | 62400 | 76480 | - | - |
| 16 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 300160 | 229120 | - | - |
| 4 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q6 | 37440 | 97600 | - | - |
| 13 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q7 | 62400 | 59200 | - | - |
| 40 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q6 | 88320 | 140800 | - | - |
| 26 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 462720 | 83520 | - | - |
| 27 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 37760 | 113920 | - | - |
| 28 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 50560 | 113920 | - | - |
| 29 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 475520 | 83520 | - | - |
| 37 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 492160 | 99840 | - | - |
| 39 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 63360 | 125120 | - | - |
| 41 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 22 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 425280 | 159040 | - | - |
| 24 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 38 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q6 | 237440 | 91840 | - | - |
| 46 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 47 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 50 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 484160 | 112960 | - | - |
| 33 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 34 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 30 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 32 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 35 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 36 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 42 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 48 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 49 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 23 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 25 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 45 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 21 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 31 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 43 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 44 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |

## Per-port GCL entries (should equal W exactly)

| port | W entries | after arrivals | GCL_size |
|---|---|---|---|
| sw01-p2 | 28 | 28 | 255 |
| sw01-p4 | 22 | 22 | 255 |
| sw01-p5 | 27 | 27 | 255 |
| sw02-p2 | 26 | 26 | 255 |
| sw02-p4 | 28 | 28 | 255 |
| sw02-p5 | 22 | 22 | 255 |
| sw03-p4 | 17 | 17 | 255 |
| sw03-p5 | 19 | 19 | 255 |
| sw04-p4 | 10 | 10 | 255 |
| sw04-p5 | 28 | 28 | 255 |
| sw05-p4 | 23 | 23 | 255 |
| sw05-p5 | 15 | 15 | 255 |
| sw06-p4 | 23 | 23 | 255 |
| sw06-p5 | 9 | 9 | 255 |
| sw07-p4 | 14 | 14 | 255 |
| sw07-p5 | 23 | 23 | 255 |
| sw08-p2 | 31 | 31 | 255 |
| sw08-p4 | 9 | 9 | 255 |
| sw08-p5 | 16 | 16 | 255 |

## Per-hop windows used by newly admitted flows

| flow | egress port | queue | psi (ns, unchanged) | delta (ns, unchanged) |
|---|---|---|---|---|
| s20(id=2 S3->S2) | S3-p0 | Q7 | 37440 | 12480 |
| s20(id=2 S3->S2) | sw01-p4 | Q7 | 54080 | 12480 |
| s20(id=2 S3->S2) | sw03-p5 | Q7 | 70720 | 12480 |
| s20(id=2 S3->S2) | sw05-p4 | Q7 | 87360 | 12480 |
| s20(id=2 S3->S2) | sw07-p5 | Q7 | 165440 | 12480 |
| s20(id=2 S3->S2) | sw08-p2 | Q7 | 182080 | 12480 |
| s24(id=11 S2->S3) | S2-p0 | Q6 | 12480 | 12480 |
| s24(id=11 S2->S3) | sw08-p5 | Q6 | 29120 | 12480 |
| s24(id=11 S2->S3) | sw07-p4 | Q6 | 91840 | 12480 |
| s24(id=11 S2->S3) | sw05-p5 | Q6 | 114240 | 12480 |
| s24(id=11 S2->S3) | sw03-p4 | Q6 | 136640 | 12480 |
| s24(id=11 S2->S3) | sw01-p2 | Q6 | 159040 | 12480 |
| s28(id=17 S1->S3) | S1-p0 | Q6 | 12480 | 12480 |
| s28(id=17 S1->S3) | sw02-p5 | Q6 | 29120 | 12480 |
| s28(id=17 S1->S3) | sw01-p2 | Q6 | 96320 | 12480 |
| s26(id=14 S3->S1) | S3-p0 | Q7 | 62400 | 12480 |
| s26(id=14 S3->S1) | sw01-p5 | Q7 | 109760 | 12480 |
| s26(id=14 S3->S1) | sw02-p2 | Q7 | 126400 | 12480 |
| s27(id=16 S2->S3) | S2-p0 | Q6 | 300160 | 12480 |
| s27(id=16 S2->S3) | sw08-p5 | Q6 | 316800 | 12480 |
| s27(id=16 S2->S3) | sw07-p4 | Q6 | 333440 | 12480 |
| s27(id=16 S2->S3) | sw05-p5 | Q6 | 400000 | 12480 |
| s27(id=16 S2->S3) | sw03-p4 | Q6 | 500160 | 12480 |
| s27(id=16 S2->S3) | sw01-p2 | Q6 | 516800 | 12480 |
| s21(id=4 S1->S3) | S1-p0 | Q6 | 37440 | 12480 |
| s21(id=4 S1->S3) | sw02-p5 | Q6 | 93440 | 12480 |
| s21(id=4 S1->S3) | sw01-p2 | Q6 | 122560 | 12480 |
| s25(id=13 S1->S3) | S1-p0 | Q7 | 62400 | 12480 |
| s25(id=13 S1->S3) | sw02-p5 | Q7 | 80960 | 12480 |
| s25(id=13 S1->S3) | sw01-p2 | Q7 | 109120 | 12480 |
| s48(id=40 S3->S1) | S3-p0 | Q6 | 88320 | 12480 |
| s48(id=40 S3->S1) | sw01-p5 | Q6 | 200000 | 12480 |
| s48(id=40 S3->S1) | sw02-p2 | Q6 | 216640 | 12480 |
| s34(id=26 S1->S2) | S1-p0 | Q7 | 462720 | 12480 |
| s34(id=26 S1->S2) | sw02-p4 | Q7 | 479360 | 12480 |
| s34(id=26 S1->S2) | sw04-p5 | Q7 | 499840 | 12480 |
| s34(id=26 S1->S2) | sw06-p4 | Q7 | 517120 | 12480 |
| s34(id=26 S1->S2) | sw08-p2 | Q7 | 533760 | 12480 |
| s35(id=27 S2->S1) | S2-p0 | Q7 | 37760 | 12480 |
| s35(id=27 S2->S1) | sw08-p4 | Q7 | 54400 | 12480 |
| s35(id=27 S2->S1) | sw06-p5 | Q7 | 71040 | 12480 |
| s35(id=27 S2->S1) | sw04-p4 | Q7 | 122560 | 12480 |
| s35(id=27 S2->S1) | sw02-p2 | Q7 | 139200 | 12480 |
| s36(id=28 S2->S1) | S2-p0 | Q7 | 50560 | 12480 |
| s36(id=28 S2->S1) | sw08-p4 | Q7 | 67200 | 12480 |
| s36(id=28 S2->S1) | sw06-p5 | Q7 | 118720 | 12480 |
| s36(id=28 S2->S1) | sw04-p4 | Q7 | 135360 | 12480 |
| s36(id=28 S2->S1) | sw02-p2 | Q7 | 152000 | 12480 |
| s37(id=29 S1->S2) | S1-p0 | Q7 | 475520 | 12480 |
| s37(id=29 S1->S2) | sw02-p4 | Q7 | 496000 | 12480 |
| s37(id=29 S1->S2) | sw04-p5 | Q7 | 513280 | 12480 |
| s37(id=29 S1->S2) | sw06-p4 | Q7 | 529920 | 12480 |
| s37(id=29 S1->S2) | sw08-p2 | Q7 | 546560 | 12480 |
| s45(id=37 S1->S2) | S1-p0 | Q7 | 492160 | 12480 |
| s45(id=37 S1->S2) | sw02-p4 | Q7 | 509440 | 12480 |
| s45(id=37 S1->S2) | sw04-p5 | Q7 | 526080 | 12480 |
| s45(id=37 S1->S2) | sw06-p4 | Q7 | 562880 | 12480 |
| s45(id=37 S1->S2) | sw08-p2 | Q7 | 579520 | 12480 |
| s47(id=39 S2->S1) | S2-p0 | Q7 | 63360 | 12480 |
| s47(id=39 S2->S1) | sw08-p4 | Q7 | 114880 | 12480 |
| s47(id=39 S2->S1) | sw06-p5 | Q7 | 131520 | 12480 |
| s47(id=39 S2->S1) | sw04-p4 | Q7 | 148160 | 12480 |
| s47(id=39 S2->S1) | sw02-p2 | Q7 | 176000 | 12480 |
| s30(id=22 S2->S3) | S2-p0 | Q6 | 425280 | 12480 |
| s30(id=22 S2->S3) | sw08-p5 | Q6 | 488000 | 12480 |
| s30(id=22 S2->S3) | sw07-p4 | Q6 | 510400 | 12480 |
| s30(id=22 S2->S3) | sw05-p5 | Q6 | 532800 | 12480 |
| s30(id=22 S2->S3) | sw03-p4 | Q6 | 555200 | 12480 |
| s30(id=22 S2->S3) | sw01-p2 | Q6 | 571840 | 12480 |
| s46(id=38 S1->S3) | S1-p0 | Q6 | 237440 | 12480 |
| s46(id=38 S1->S3) | sw02-p5 | Q6 | 292480 | 12480 |
| s46(id=38 S1->S3) | sw01-p2 | Q6 | 309120 | 12480 |
| s58(id=50 S2->S3) | S2-p0 | Q6 | 484160 | 12480 |
| s58(id=50 S2->S3) | sw08-p5 | Q6 | 506560 | 12480 |
| s58(id=50 S2->S3) | sw07-p4 | Q6 | 528960 | 12480 |
| s58(id=50 S2->S3) | sw05-p5 | Q6 | 551360 | 12480 |
| s58(id=50 S2->S3) | sw03-p4 | Q6 | 568000 | 12480 |
| s58(id=50 S2->S3) | sw01-p2 | Q6 | 584640 | 12480 |

## Constraint check

- C1-C7, C9: OK
- window-boundary integrity (no window's psi/delta changed anywhere): OK

## GCL per egress port

### sw01-p2  (28 entries, util 23.4000 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 960 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 4800 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 6720 0x3F # 00111111   BE
sgs 72960 0x40 # 01000000   Q6
sgs 17920 0x7F # 01111111   Q6
sgs 46400 0xBF # 10111111   Q7
sgs 122560 0x40 # 01000000   Q6
sgs 31040 0x7F # 01111111   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 50240 0x7F # 01111111   Q6
sgs 72960 0x40 # 01000000   Q6
sgs 17920 0x7F # 01111111   Q6
sgs 46400 0xBF # 10111111   Q7
sgs 39360 0x40 # 01000000   Q6
sgs 14400 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p4  (22 entries, util 9.3600 %)

```
sgs 41600 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 46080 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 19200 0x80 # 10000000   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 93120 0x40 # 01000000   Q6
sgs 15360 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 46080 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 19200 0x80 # 10000000   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 51520 0x40 # 01000000   Q6
sgs 56960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p5  (27 entries, util 17.1600 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 13120 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 5120 0x3F # 00111111   BE
sgs 43520 0x80 # 10000000   Q7
sgs 46720 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 136640 0x80 # 10000000   Q7
sgs 46720 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 13120 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 5120 0x3F # 00111111   BE
sgs 43520 0x80 # 10000000   Q7
sgs 46720 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 120000 0x80 # 10000000   Q7
sgs 13440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (26 entries, util 23.4000 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 5120 0x3F # 00111111   BE
sgs 49600 0x80 # 10000000   Q7
sgs 24000 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 142720 0x80 # 10000000   Q7
sgs 24000 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 13120 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 5120 0x3F # 00111111   BE
sgs 49600 0x80 # 10000000   Q7
sgs 24000 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 109440 0x80 # 10000000   Q7
sgs 57280 0xBF # 10111111   Q7
```

### sw02-p4  (28 entries, util 23.4000 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 50240 0x80 # 10000000   Q7
sgs 33280 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 125120 0x80 # 10000000   Q7
sgs 33280 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 100160 0x80 # 10000000   Q7
sgs 33280 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 108480 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p5  (22 entries, util 12.4800 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 14400 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 44160 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 14400 0xBF # 10111111   Q7
sgs 85760 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 14400 0xBF # 10111111   Q7
sgs 85760 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 14400 0xBF # 10111111   Q7
sgs 21440 0x40 # 01000000   Q6
sgs 14400 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (17 entries, util 10.9200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 21120 0xBF # 10111111   Q7
sgs 36480 0x7F # 01111111   Q6
sgs 175040 0x40 # 01000000   Q6
sgs 38400 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 21120 0xBF # 10111111   Q7
sgs 36480 0x7F # 01111111   Q6
sgs 108480 0x40 # 01000000   Q6
sgs 55040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p5  (19 entries, util 9.3600 %)

```
sgs 58240 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 29440 0xBF # 10111111   Q7
sgs 32000 0x7F # 01111111   Q6
sgs 19200 0x80 # 10000000   Q7
sgs 48640 0xBF # 10111111   Q7
sgs 58240 0x7F # 01111111   Q6
sgs 93120 0x40 # 01000000   Q6
sgs 48640 0xBF # 10111111   Q7
sgs 58240 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 29440 0xBF # 10111111   Q7
sgs 32000 0x7F # 01111111   Q6
sgs 19200 0x80 # 10000000   Q7
sgs 48640 0xBF # 10111111   Q7
sgs 58240 0x7F # 01111111   Q6
sgs 34880 0x40 # 01000000   Q6
sgs 56960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p4  (10 entries, util 6.2400 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 462720 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (28 entries, util 23.4000 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 50240 0x80 # 10000000   Q7
sgs 16640 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 125120 0x80 # 10000000   Q7
sgs 16640 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 100160 0x80 # 10000000   Q7
sgs 16640 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 91840 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (23 entries, util 9.3600 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12800 0xBF # 10111111   Q7
sgs 48640 0x7F # 01111111   Q6
sgs 19200 0x80 # 10000000   Q7
sgs 32000 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 93120 0x40 # 01000000   Q6
sgs 32000 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12800 0xBF # 10111111   Q7
sgs 48640 0x7F # 01111111   Q6
sgs 19200 0x80 # 10000000   Q7
sgs 32000 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 18240 0x40 # 01000000   Q6
sgs 56960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p5  (15 entries, util 10.9200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 37760 0xBF # 10111111   Q7
sgs 14080 0x7F # 01111111   Q6
sgs 180800 0x40 # 01000000   Q6
sgs 55040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 37760 0xBF # 10111111   Q7
sgs 14080 0x7F # 01111111   Q6
sgs 130880 0x40 # 01000000   Q6
sgs 55040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p4  (23 entries, util 23.4000 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 16320 0xBF # 10111111   Q7
sgs 33600 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 50240 0x80 # 10000000   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 125120 0x80 # 10000000   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 16320 0xBF # 10111111   Q7
sgs 96320 0x80 # 10000000   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 75200 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (9 entries, util 6.2400 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 45760 0x7F # 01111111   Q6
sgs 479360 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (14 entries, util 10.9200 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 46080 0xBF # 10111111   Q7
sgs 186560 0x40 # 01000000   Q6
sgs 21760 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 46080 0xBF # 10111111   Q7
sgs 153280 0x40 # 01000000   Q6
sgs 55040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p5  (23 entries, util 9.3600 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 46080 0x7F # 01111111   Q6
sgs 15360 0xBF # 10111111   Q7
sgs 19200 0x80 # 10000000   Q7
sgs 15360 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 93120 0x40 # 01000000   Q6
sgs 15360 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 46080 0x7F # 01111111   Q6
sgs 15360 0xBF # 10111111   Q7
sgs 19200 0x80 # 10000000   Q7
sgs 15360 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 46080 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p2  (31 entries, util 32.7600 %)

```
sgs 66560 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 32960 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 28160 0x80 # 10000000   Q7
sgs 72000 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 145920 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 73600 0x80 # 10000000   Q7
sgs 72000 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 79360 0x3F # 00111111   BE
```

### sw08-p4  (9 entries, util 6.2400 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 29120 0x7F # 01111111   Q6
sgs 496000 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (16 entries, util 10.9200 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 960 0x3F # 00111111   BE
sgs 229760 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 226560 0x40 # 01000000   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

