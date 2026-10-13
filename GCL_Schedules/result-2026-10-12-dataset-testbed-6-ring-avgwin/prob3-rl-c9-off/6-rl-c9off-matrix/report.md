# Reconfiguration-free admission (Problem 3)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Frozen schedule W loaded from: **result/result-2026-10-12-dataset-testbed-6-ring-avgwin/rl-c9-off/6-matrix-c9off**

## Admission: W (before) vs. after this run's arrivals

| | admitted | of total |
|---|---|---|
| W (base, unchanged) | 10 | 10 |
| + this run's arrivals | 17 | 40 |

Every arrival admitted here required **zero** window-boundary changes -- see the GCL-entry table below (unchanged from W by construction) and the window-boundary integrity check. No previously-admitted flow was rerouted.

## Arrivals

| id | src->dst | RS(s) size | admitted | route | queue | phi_s (ns) | e2e (ns) | rerouted to make room | reason if rejected |
|---|---|---|---|---|---|---|---|---|---|
| 3 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 | 12480 | 95680 | - | - |
| 16 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 | 37440 | 95680 | - | - |
| 15 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 12480 | 400000 | - | - |
| 18 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 5 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 13 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q6 | 12480 | 133760 | - | - |
| 8 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 37440 | 95680 | - | - |
| 11 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 | 87360 | 95680 | - | - |
| 17 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 62400 | 95680 | - | - |
| 10 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q6 | 118080 | 611200 | - | - |
| 27 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q7 | 37440 | 45760 | - | - |
| 37 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 39 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q7 | 50240 | 45760 | - | - |
| 43 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 47 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 25 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q6 | 130560 | 307520 | - | - |
| 36 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 40 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q6 | 425280 | 212800 | - | - |
| 32 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q7 | 150080 | 45760 | - | - |
| 35 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 38 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 87360 | 95680 | - | - |
| 45 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q7 | 162880 | 45760 | - | - |
| 46 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 29 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 50 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 212800 | 79040 | - | - |
| 22 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 100160 | 178880 | - | - |
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
| sw01-p2 | 14 | 14 | 255 |
| sw01-p4 | 20 | 20 | 255 |
| sw01-p5 | 28 | 28 | 255 |
| sw02-p2 | 27 | 27 | 255 |
| sw02-p4 | 22 | 22 | 255 |
| sw02-p5 | 9 | 9 | 255 |
| sw03-p4 | 13 | 13 | 255 |
| sw03-p5 | 17 | 17 | 255 |
| sw04-p4 | 19 | 19 | 255 |
| sw04-p5 | 20 | 20 | 255 |
| sw05-p4 | 21 | 21 | 255 |
| sw05-p5 | 14 | 14 | 255 |
| sw06-p4 | 19 | 19 | 255 |
| sw06-p5 | 19 | 19 | 255 |
| sw07-p4 | 14 | 14 | 255 |
| sw07-p5 | 21 | 21 | 255 |
| sw08-p2 | 33 | 33 | 255 |
| sw08-p4 | 19 | 19 | 255 |
| sw08-p5 | 12 | 12 | 255 |

## Per-hop windows used by newly admitted flows

| flow | egress port | queue | psi (ns, unchanged) | delta (ns, unchanged) |
|---|---|---|---|---|
| s20(id=3 S3->S2) | S3-p0 | Q7 | 12480 | 12480 |
| s20(id=3 S3->S2) | sw01-p4 | Q7 | 29120 | 12480 |
| s20(id=3 S3->S2) | sw03-p5 | Q7 | 45760 | 12480 |
| s20(id=3 S3->S2) | sw05-p4 | Q7 | 62400 | 12480 |
| s20(id=3 S3->S2) | sw07-p5 | Q7 | 79040 | 12480 |
| s20(id=3 S3->S2) | sw08-p2 | Q7 | 95680 | 12480 |
| s27(id=16 S3->S2) | S3-p0 | Q7 | 37440 | 12480 |
| s27(id=16 S3->S2) | sw01-p4 | Q7 | 54080 | 12480 |
| s27(id=16 S3->S2) | sw03-p5 | Q7 | 70720 | 12480 |
| s27(id=16 S3->S2) | sw05-p4 | Q7 | 87360 | 12480 |
| s27(id=16 S3->S2) | sw07-p5 | Q7 | 104000 | 12480 |
| s27(id=16 S3->S2) | sw08-p2 | Q7 | 120640 | 12480 |
| s26(id=15 S2->S3) | S2-p0 | Q6 | 12480 | 12480 |
| s26(id=15 S2->S3) | sw08-p5 | Q6 | 29120 | 12480 |
| s26(id=15 S2->S3) | sw07-p4 | Q6 | 300160 | 12480 |
| s26(id=15 S2->S3) | sw05-p5 | Q6 | 316800 | 12480 |
| s26(id=15 S2->S3) | sw03-p4 | Q6 | 333440 | 12480 |
| s26(id=15 S2->S3) | sw01-p2 | Q6 | 400000 | 12480 |
| s25(id=13 S1->S2) | S1-p0 | Q6 | 12480 | 12480 |
| s25(id=13 S1->S2) | sw02-p4 | Q6 | 29120 | 12480 |
| s25(id=13 S1->S2) | sw04-p5 | Q6 | 94720 | 12480 |
| s25(id=13 S1->S2) | sw06-p4 | Q6 | 114240 | 12480 |
| s25(id=13 S1->S2) | sw08-p2 | Q6 | 133760 | 12480 |
| s22(id=8 S2->S3) | S2-p0 | Q7 | 37440 | 12480 |
| s22(id=8 S2->S3) | sw08-p5 | Q7 | 54080 | 12480 |
| s22(id=8 S2->S3) | sw07-p4 | Q7 | 70720 | 12480 |
| s22(id=8 S2->S3) | sw05-p5 | Q7 | 87360 | 12480 |
| s22(id=8 S2->S3) | sw03-p4 | Q7 | 104000 | 12480 |
| s22(id=8 S2->S3) | sw01-p2 | Q7 | 120640 | 12480 |
| s24(id=11 S3->S2) | S3-p0 | Q7 | 87360 | 12480 |
| s24(id=11 S3->S2) | sw01-p4 | Q7 | 104000 | 12480 |
| s24(id=11 S3->S2) | sw03-p5 | Q7 | 120640 | 12480 |
| s24(id=11 S3->S2) | sw05-p4 | Q7 | 137280 | 12480 |
| s24(id=11 S3->S2) | sw07-p5 | Q7 | 153920 | 12480 |
| s24(id=11 S3->S2) | sw08-p2 | Q7 | 170560 | 12480 |
| s28(id=17 S2->S3) | S2-p0 | Q7 | 62400 | 12480 |
| s28(id=17 S2->S3) | sw08-p5 | Q7 | 79040 | 12480 |
| s28(id=17 S2->S3) | sw07-p4 | Q7 | 95680 | 12480 |
| s28(id=17 S2->S3) | sw05-p5 | Q7 | 112320 | 12480 |
| s28(id=17 S2->S3) | sw03-p4 | Q7 | 128960 | 12480 |
| s28(id=17 S2->S3) | sw01-p2 | Q7 | 145600 | 12480 |
| s23(id=10 S1->S3) | S1-p0 | Q6 | 118080 | 12480 |
| s23(id=10 S1->S3) | sw02-p5 | Q6 | 700160 | 12480 |
| s23(id=10 S1->S3) | sw01-p2 | Q6 | 716800 | 12480 |
| s36(id=27 S1->S3) | S1-p0 | Q7 | 37440 | 12480 |
| s36(id=27 S1->S3) | sw02-p5 | Q7 | 54080 | 12480 |
| s36(id=27 S1->S3) | sw01-p2 | Q7 | 70720 | 12480 |
| s48(id=39 S1->S3) | S1-p0 | Q7 | 50240 | 12480 |
| s48(id=39 S1->S3) | sw02-p5 | Q7 | 66880 | 12480 |
| s48(id=39 S1->S3) | sw01-p2 | Q7 | 83520 | 12480 |
| s34(id=25 S1->S2) | S1-p0 | Q6 | 130560 | 12480 |
| s34(id=25 S1->S2) | sw02-p4 | Q6 | 200000 | 12480 |
| s34(id=25 S1->S2) | sw04-p5 | Q6 | 216640 | 12480 |
| s34(id=25 S1->S2) | sw06-p4 | Q6 | 400000 | 12480 |
| s34(id=25 S1->S2) | sw08-p2 | Q6 | 425600 | 12480 |
| s49(id=40 S1->S2) | S1-p0 | Q6 | 425280 | 12480 |
| s49(id=40 S1->S2) | sw02-p4 | Q6 | 490880 | 12480 |
| s49(id=40 S1->S2) | sw04-p5 | Q6 | 510400 | 12480 |
| s49(id=40 S1->S2) | sw06-p4 | Q6 | 529920 | 12480 |
| s49(id=40 S1->S2) | sw08-p2 | Q6 | 625600 | 12480 |
| s41(id=32 S1->S3) | S1-p0 | Q7 | 150080 | 12480 |
| s41(id=32 S1->S3) | sw02-p5 | Q7 | 166720 | 12480 |
| s41(id=32 S1->S3) | sw01-p2 | Q7 | 183360 | 12480 |
| s47(id=38 S2->S3) | S2-p0 | Q7 | 87360 | 12480 |
| s47(id=38 S2->S3) | sw08-p5 | Q7 | 104000 | 12480 |
| s47(id=38 S2->S3) | sw07-p4 | Q7 | 120640 | 12480 |
| s47(id=38 S2->S3) | sw05-p5 | Q7 | 137280 | 12480 |
| s47(id=38 S2->S3) | sw03-p4 | Q7 | 153920 | 12480 |
| s47(id=38 S2->S3) | sw01-p2 | Q7 | 170560 | 12480 |
| s54(id=45 S1->S3) | S1-p0 | Q7 | 162880 | 12480 |
| s54(id=45 S1->S3) | sw02-p5 | Q7 | 179520 | 12480 |
| s54(id=45 S1->S3) | sw01-p2 | Q7 | 196160 | 12480 |
| s59(id=50 S1->S2) | S1-p0 | Q7 | 212800 | 12480 |
| s59(id=50 S1->S2) | sw02-p4 | Q7 | 229440 | 12480 |
| s59(id=50 S1->S2) | sw04-p5 | Q7 | 246080 | 12480 |
| s59(id=50 S1->S2) | sw06-p4 | Q7 | 262720 | 12480 |
| s59(id=50 S1->S2) | sw08-p2 | Q7 | 279360 | 12480 |
| s31(id=22 S2->S3) | S2-p0 | Q7 | 100160 | 12480 |
| s31(id=22 S2->S3) | sw08-p5 | Q7 | 116800 | 12480 |
| s31(id=22 S2->S3) | sw07-p4 | Q7 | 133440 | 12480 |
| s31(id=22 S2->S3) | sw05-p5 | Q7 | 150080 | 12480 |
| s31(id=22 S2->S3) | sw03-p4 | Q7 | 192320 | 12480 |
| s31(id=22 S2->S3) | sw01-p2 | Q7 | 208960 | 12480 |

## Constraint check

- C1-C7, C9: OK
- window-boundary integrity (no window's psi/delta changed anywhere): OK

## GCL per egress port

### sw01-p2  (14 entries, util 23.4000 %)

```
sgs 58240 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 16960 0xBF # 10111111   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 242560 0x80 # 10000000   Q7
sgs 36800 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 121920 0x80 # 10000000   Q7
sgs 57600 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p4  (20 entries, util 20.2800 %)

```
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 117440 0x80 # 10000000   Q7
sgs 28480 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 117440 0x80 # 10000000   Q7
sgs 28480 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 117440 0x80 # 10000000   Q7
sgs 28480 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 88320 0x80 # 10000000   Q7
sgs 57600 0xBF # 10111111   Q7
```

### sw01-p5  (28 entries, util 15.6000 %)

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
sgs 61120 0xBF # 10111111   Q7
```

### sw02-p2  (27 entries, util 28.0800 %)

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
sgs 32320 0x40 # 01000000   Q6
sgs 79360 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x3F # 00111111   BE
sgs 29120 0x80 # 10000000   Q7
sgs 137600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x3F # 00111111   BE
sgs 29120 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 112000 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x3F # 00111111   BE
sgs 29120 0x80 # 10000000   Q7
sgs 104320 0x3F # 00111111   BE
```

### sw02-p4  (22 entries, util 15.6000 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 25280 0xBF # 10111111   Q7
sgs 34560 0x40 # 01000000   Q6
sgs 40320 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 93120 0x80 # 10000000   Q7
sgs 40320 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 25280 0xBF # 10111111   Q7
sgs 34560 0x40 # 01000000   Q6
sgs 40320 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 76480 0x80 # 10000000   Q7
sgs 56960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p5  (9 entries, util 12.4800 %)

```
sgs 41600 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 483520 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (13 entries, util 10.9200 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 54080 0xBF # 10111111   Q7
sgs 200000 0x80 # 10000000   Q7
sgs 46080 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 54080 0xBF # 10111111   Q7
sgs 96000 0x80 # 10000000   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p5  (17 entries, util 20.2800 %)

```
sgs 45760 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 117440 0x80 # 10000000   Q7
sgs 57600 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 117440 0x80 # 10000000   Q7
sgs 57600 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 117440 0x80 # 10000000   Q7
sgs 57600 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 71680 0x80 # 10000000   Q7
sgs 57600 0xBF # 10111111   Q7
```

### sw04-p4  (19 entries, util 12.4800 %)

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

### sw04-p5  (20 entries, util 15.6000 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 48960 0xBF # 10111111   Q7
sgs 31680 0x40 # 01000000   Q6
sgs 23680 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 93120 0x80 # 10000000   Q7
sgs 23680 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 48960 0xBF # 10111111   Q7
sgs 31680 0x40 # 01000000   Q6
sgs 23680 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 59840 0x80 # 10000000   Q7
sgs 56960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (21 entries, util 20.2800 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 117440 0x80 # 10000000   Q7
sgs 45120 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 117440 0x80 # 10000000   Q7
sgs 45120 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 117440 0x80 # 10000000   Q7
sgs 45120 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 55040 0x80 # 10000000   Q7
sgs 57600 0xBF # 10111111   Q7
```

### sw05-p5  (14 entries, util 10.9200 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 37440 0xBF # 10111111   Q7
sgs 200000 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 37440 0xBF # 10111111   Q7
sgs 112640 0x80 # 10000000   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p4  (19 entries, util 15.6000 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 37760 0xBF # 10111111   Q7
sgs 14080 0x7F # 01111111   Q6
sgs 28800 0x40 # 01000000   Q6
sgs 56960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 93120 0x80 # 10000000   Q7
sgs 56960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 37760 0xBF # 10111111   Q7
sgs 14080 0x7F # 01111111   Q6
sgs 28800 0x40 # 01000000   Q6
sgs 56960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 43200 0x80 # 10000000   Q7
sgs 56960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (19 entries, util 12.4800 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 37120 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 47360 0x40 # 01000000   Q6
sgs 44480 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 122240 0x80 # 10000000   Q7
sgs 44480 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 96960 0x40 # 01000000   Q6
sgs 44480 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 88960 0x80 # 10000000   Q7
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (14 entries, util 10.9200 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 20800 0xBF # 10111111   Q7
sgs 200000 0x80 # 10000000   Q7
sgs 29440 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 20800 0xBF # 10111111   Q7
sgs 129280 0x80 # 10000000   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p5  (21 entries, util 20.2800 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 117440 0x80 # 10000000   Q7
sgs 28480 0x7F # 01111111   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 117440 0x80 # 10000000   Q7
sgs 28480 0x7F # 01111111   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 117440 0x80 # 10000000   Q7
sgs 28480 0x7F # 01111111   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 38400 0x80 # 10000000   Q7
sgs 57600 0xBF # 10111111   Q7
```

### sw08-p2  (33 entries, util 35.8800 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 29120 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 79040 0x80 # 10000000   Q7
sgs 24320 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 29120 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 104960 0x80 # 10000000   Q7
sgs 24320 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 29120 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 79040 0x80 # 10000000   Q7
sgs 24320 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 29120 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 38400 0x80 # 10000000   Q7
sgs 40960 0xBF # 10111111   Q7
```

### sw08-p4  (19 entries, util 12.4800 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0x7F # 01111111   Q6
sgs 37120 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 47360 0x40 # 01000000   Q6
sgs 61120 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 122240 0x80 # 10000000   Q7
sgs 61120 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0x7F # 01111111   Q6
sgs 96960 0x40 # 01000000   Q6
sgs 61120 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 105600 0x80 # 10000000   Q7
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (12 entries, util 10.9200 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 41600 0x7F # 01111111   Q6
sgs 200000 0x80 # 10000000   Q7
sgs 46080 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 54080 0x7F # 01111111   Q6
sgs 145920 0x80 # 10000000   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

