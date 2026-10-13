# Reconfiguration-free admission (Problem 3)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Frozen schedule W loaded from: **result/result-2026-10-12-dataset-testbed-6-ring-avgwin/rl-c9-on/6-matrix-c9on**

## Admission: W (before) vs. after this run's arrivals

| | admitted | of total |
|---|---|---|
| W (base, unchanged) | 10 | 10 |
| + this run's arrivals | 17 | 40 |

Every arrival admitted here required **zero** window-boundary changes -- see the GCL-entry table below (unchanged from W by construction) and the window-boundary integrity check. No previously-admitted flow was rerouted.

## Arrivals

| id | src->dst | RS(s) size | admitted | route | queue | phi_s (ns) | e2e (ns) | rerouted to make room | reason if rejected |
|---|---|---|---|---|---|---|---|---|---|
| 3 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 | 37440 | 54400 | - | - |
| 16 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 15 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 37440 | 50880 | - | - |
| 18 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 | 62400 | 120640 | - | - |
| 5 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 13 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 77120 | 118720 | - | - |
| 8 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 62400 | 300160 | - | - |
| 11 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q6 | 87360 | 61760 | - | - |
| 17 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 141760 | 233600 | - | - |
| 10 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q6 | 12480 | 22720 | - | - |
| 27 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q6 | 37440 | 63360 | - | - |
| 37 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 39 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q6 | 49920 | 63680 | - | - |
| 43 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 47 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 25 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q6 | 62400 | 156160 | - | - |
| 36 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 40 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q6 | 100160 | 312320 | - | - |
| 32 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q6 | 112640 | 200000 | - | - |
| 35 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 38 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 12480 | 135680 | - | - |
| 45 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q7 | 350080 | 220800 | - | - |
| 46 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 29 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 50 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q6 | 125120 | 320320 | - | - |
| 22 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 341760 | 49920 | - | - |
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
| sw01-p4 | 30 | 30 | 255 |
| sw01-p5 | 21 | 21 | 255 |
| sw02-p2 | 29 | 29 | 255 |
| sw02-p4 | 17 | 17 | 255 |
| sw02-p5 | 9 | 9 | 255 |
| sw03-p4 | 15 | 15 | 255 |
| sw03-p5 | 26 | 26 | 255 |
| sw04-p4 | 15 | 15 | 255 |
| sw04-p5 | 17 | 17 | 255 |
| sw05-p4 | 31 | 31 | 255 |
| sw05-p5 | 13 | 13 | 255 |
| sw06-p4 | 23 | 23 | 255 |
| sw06-p5 | 18 | 18 | 255 |
| sw07-p4 | 13 | 13 | 255 |
| sw07-p5 | 27 | 27 | 255 |
| sw08-p2 | 34 | 34 | 255 |
| sw08-p4 | 15 | 15 | 255 |
| sw08-p5 | 13 | 13 | 255 |

## Per-hop windows used by newly admitted flows

| flow | egress port | queue | psi (ns, unchanged) | delta (ns, unchanged) |
|---|---|---|---|---|
| s20(id=3 S3->S2) | S3-p0 | Q7 | 37440 | 12480 |
| s20(id=3 S3->S2) | sw01-p4 | Q7 | 46080 | 12480 |
| s20(id=3 S3->S2) | sw03-p5 | Q7 | 54080 | 12480 |
| s20(id=3 S3->S2) | sw05-p4 | Q7 | 62720 | 12480 |
| s20(id=3 S3->S2) | sw07-p5 | Q7 | 70720 | 12480 |
| s20(id=3 S3->S2) | sw08-p2 | Q7 | 79360 | 12480 |
| s26(id=15 S2->S3) | S2-p0 | Q7 | 37440 | 12480 |
| s26(id=15 S2->S3) | sw08-p5 | Q7 | 45120 | 12480 |
| s26(id=15 S2->S3) | sw07-p4 | Q7 | 52800 | 12480 |
| s26(id=15 S2->S3) | sw05-p5 | Q7 | 60480 | 12480 |
| s26(id=15 S2->S3) | sw03-p4 | Q7 | 68160 | 12480 |
| s26(id=15 S2->S3) | sw01-p2 | Q7 | 75840 | 12480 |
| s29(id=18 S3->S2) | S3-p0 | Q7 | 62400 | 12480 |
| s29(id=18 S3->S2) | sw01-p4 | Q7 | 67520 | 12480 |
| s29(id=18 S3->S2) | sw03-p5 | Q7 | 72640 | 12480 |
| s29(id=18 S3->S2) | sw05-p4 | Q7 | 77760 | 12480 |
| s29(id=18 S3->S2) | sw07-p5 | Q7 | 83200 | 12480 |
| s29(id=18 S3->S2) | sw08-p2 | Q7 | 170560 | 12480 |
| s25(id=13 S1->S2) | S1-p0 | Q7 | 77120 | 12480 |
| s25(id=13 S1->S2) | sw02-p4 | Q7 | 83840 | 12480 |
| s25(id=13 S1->S2) | sw04-p5 | Q7 | 150080 | 12480 |
| s25(id=13 S1->S2) | sw06-p4 | Q7 | 176640 | 12480 |
| s25(id=13 S1->S2) | sw08-p2 | Q7 | 183360 | 12480 |
| s22(id=8 S2->S3) | S2-p0 | Q7 | 62400 | 12480 |
| s22(id=8 S2->S3) | sw08-p5 | Q7 | 67520 | 12480 |
| s22(id=8 S2->S3) | sw07-p4 | Q7 | 72640 | 12480 |
| s22(id=8 S2->S3) | sw05-p5 | Q7 | 77760 | 12480 |
| s22(id=8 S2->S3) | sw03-p4 | Q7 | 82880 | 12480 |
| s22(id=8 S2->S3) | sw01-p2 | Q7 | 350080 | 12480 |
| s24(id=11 S3->S2) | S3-p0 | Q6 | 87360 | 12480 |
| s24(id=11 S3->S2) | sw01-p4 | Q6 | 103360 | 12480 |
| s24(id=11 S3->S2) | sw03-p5 | Q6 | 111680 | 12480 |
| s24(id=11 S3->S2) | sw05-p4 | Q6 | 120000 | 12480 |
| s24(id=11 S3->S2) | sw07-p5 | Q6 | 128320 | 12480 |
| s24(id=11 S3->S2) | sw08-p2 | Q6 | 136640 | 12480 |
| s28(id=17 S2->S3) | S2-p0 | Q7 | 141760 | 12480 |
| s28(id=17 S2->S3) | sw08-p5 | Q7 | 245120 | 12480 |
| s28(id=17 S2->S3) | sw07-p4 | Q7 | 252800 | 12480 |
| s28(id=17 S2->S3) | sw05-p5 | Q7 | 260480 | 12480 |
| s28(id=17 S2->S3) | sw03-p4 | Q7 | 356800 | 12480 |
| s28(id=17 S2->S3) | sw01-p2 | Q7 | 362880 | 12480 |
| s23(id=10 S1->S3) | S1-p0 | Q6 | 12480 | 12480 |
| s23(id=10 S1->S3) | sw02-p5 | Q6 | 17600 | 12480 |
| s23(id=10 S1->S3) | sw01-p2 | Q6 | 22720 | 12480 |
| s36(id=27 S1->S3) | S1-p0 | Q6 | 37440 | 12480 |
| s36(id=27 S1->S3) | sw02-p5 | Q6 | 45120 | 12480 |
| s36(id=27 S1->S3) | sw01-p2 | Q6 | 88320 | 12480 |
| s48(id=39 S1->S3) | S1-p0 | Q6 | 49920 | 12480 |
| s48(id=39 S1->S3) | sw02-p5 | Q6 | 94400 | 12480 |
| s48(id=39 S1->S3) | sw01-p2 | Q6 | 101120 | 12480 |
| s34(id=25 S1->S2) | S1-p0 | Q6 | 62400 | 12480 |
| s34(id=25 S1->S2) | sw02-p4 | Q6 | 100160 | 12480 |
| s34(id=25 S1->S2) | sw04-p5 | Q6 | 106240 | 12480 |
| s34(id=25 S1->S2) | sw06-p4 | Q6 | 200000 | 12480 |
| s34(id=25 S1->S2) | sw08-p2 | Q6 | 206080 | 12480 |
| s49(id=40 S1->S2) | S1-p0 | Q6 | 100160 | 12480 |
| s49(id=40 S1->S2) | sw02-p4 | Q6 | 112640 | 12480 |
| s49(id=40 S1->S2) | sw04-p5 | Q6 | 300160 | 12480 |
| s49(id=40 S1->S2) | sw06-p4 | Q6 | 321600 | 12480 |
| s49(id=40 S1->S2) | sw08-p2 | Q6 | 400000 | 12480 |
| s41(id=32 S1->S3) | S1-p0 | Q6 | 112640 | 12480 |
| s41(id=32 S1->S3) | sw02-p5 | Q6 | 117760 | 12480 |
| s41(id=32 S1->S3) | sw01-p2 | Q6 | 122880 | 12480 |
| s47(id=38 S2->S3) | S2-p0 | Q6 | 12480 | 12480 |
| s47(id=38 S2->S3) | sw08-p5 | Q6 | 17600 | 12480 |
| s47(id=38 S2->S3) | sw07-p4 | Q6 | 22720 | 12480 |
| s47(id=38 S2->S3) | sw05-p5 | Q6 | 27840 | 12480 |
| s47(id=38 S2->S3) | sw03-p4 | Q6 | 130560 | 12480 |
| s47(id=38 S2->S3) | sw01-p2 | Q6 | 135680 | 12480 |
| s54(id=45 S1->S3) | S1-p0 | Q7 | 350080 | 12480 |
| s54(id=45 S1->S3) | sw02-p5 | Q7 | 550080 | 12480 |
| s54(id=45 S1->S3) | sw01-p2 | Q7 | 558400 | 12480 |
| s59(id=50 S1->S2) | S1-p0 | Q6 | 125120 | 12480 |
| s59(id=50 S1->S2) | sw02-p4 | Q6 | 300160 | 12480 |
| s59(id=50 S1->S2) | sw04-p5 | Q6 | 329280 | 12480 |
| s59(id=50 S1->S2) | sw06-p4 | Q6 | 427840 | 12480 |
| s59(id=50 S1->S2) | sw08-p2 | Q6 | 432960 | 12480 |
| s31(id=22 S2->S3) | S2-p0 | Q7 | 341760 | 12480 |
| s31(id=22 S2->S3) | sw08-p5 | Q7 | 350080 | 12480 |
| s31(id=22 S2->S3) | sw07-p4 | Q7 | 356800 | 12480 |
| s31(id=22 S2->S3) | sw05-p5 | Q7 | 363520 | 12480 |
| s31(id=22 S2->S3) | sw03-p4 | Q7 | 370240 | 12480 |
| s31(id=22 S2->S3) | sw01-p2 | Q7 | 376960 | 12480 |

## Constraint check

- C1-C7, C9: OK
- window-boundary integrity (no window's psi/delta changed anywhere): OK

## GCL per egress port

### sw01-p2  (14 entries, util 23.4000 %)

```
sgs 38400 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 29440 0x7F # 01111111   Q6
sgs 200640 0x40 # 01000000   Q6
sgs 31680 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 25920 0xBF # 10111111   Q7
sgs 166720 0x80 # 10000000   Q7
sgs 57600 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p4  (30 entries, util 17.1600 %)

```
sgs 17600 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 3200 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 44800 0xBF # 10111111   Q7
sgs 60800 0x40 # 01000000   Q6
sgs 35840 0xBF # 10111111   Q7
sgs 17600 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 3200 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 118080 0x80 # 10000000   Q7
sgs 35840 0xBF # 10111111   Q7
sgs 17600 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 3200 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 118080 0x80 # 10000000   Q7
sgs 35840 0xBF # 10111111   Q7
sgs 17600 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 3200 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 100480 0x80 # 10000000   Q7
sgs 53440 0xBF # 10111111   Q7
```

### sw01-p5  (21 entries, util 15.6000 %)

```
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 35200 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 14720 0xBF # 10111111   Q7
sgs 64000 0x40 # 01000000   Q6
sgs 61120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 35200 0x7F # 01111111   Q6
sgs 91200 0x40 # 01000000   Q6
sgs 61120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 35200 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 14720 0xBF # 10111111   Q7
sgs 64000 0x40 # 01000000   Q6
sgs 61120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 35200 0x7F # 01111111   Q6
sgs 82880 0x40 # 01000000   Q6
sgs 61120 0xBF # 10111111   Q7
```

### sw02-p2  (29 entries, util 28.0800 %)

```
sgs 16640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 1600 0x3F # 00111111   BE
sgs 43840 0x40 # 01000000   Q6
sgs 2240 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 2240 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 99840 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 1600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 18880 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 142080 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 1600 0x3F # 00111111   BE
sgs 43840 0x40 # 01000000   Q6
sgs 16960 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 112640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 1600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 18880 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 125440 0x3F # 00111111   BE
```

### sw02-p4  (17 entries, util 15.6000 %)

```
sgs 5120 0x3F # 00111111   BE
sgs 50240 0x80 # 10000000   Q7
sgs 44800 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 55040 0xBF # 10111111   Q7
sgs 50240 0x80 # 10000000   Q7
sgs 44800 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 55040 0xBF # 10111111   Q7
sgs 50240 0x80 # 10000000   Q7
sgs 44800 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 55040 0xBF # 10111111   Q7
sgs 45120 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p5  (9 entries, util 12.4800 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 19200 0x7F # 01111111   Q6
sgs 505920 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (15 entries, util 10.9200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 18240 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 31040 0xBF # 10111111   Q7
sgs 156480 0x40 # 01000000   Q6
sgs 32000 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 18240 0xBF # 10111111   Q7
sgs 131840 0x80 # 10000000   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p5  (26 entries, util 17.1600 %)

```
sgs 22720 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 6400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 45120 0xBF # 10111111   Q7
sgs 57600 0x40 # 01000000   Q6
sgs 30720 0xBF # 10111111   Q7
sgs 22720 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 6400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 115200 0x80 # 10000000   Q7
sgs 30720 0xBF # 10111111   Q7
sgs 22720 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 6400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 115200 0x80 # 10000000   Q7
sgs 30720 0xBF # 10111111   Q7
sgs 22720 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 6400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 92480 0x80 # 10000000   Q7
sgs 53440 0xBF # 10111111   Q7
```

### sw04-p4  (15 entries, util 12.4800 %)

```
sgs 23040 0x7F # 01111111   Q6
sgs 29760 0x40 # 01000000   Q6
sgs 17280 0xBF # 10111111   Q7
sgs 75200 0x80 # 10000000   Q7
sgs 54720 0xBF # 10111111   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 122240 0x40 # 01000000   Q6
sgs 54720 0xBF # 10111111   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 122240 0x40 # 01000000   Q6
sgs 54720 0xBF # 10111111   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 99200 0x40 # 01000000   Q6
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (17 entries, util 15.6000 %)

```
sgs 10240 0x3F # 00111111   BE
sgs 50240 0x80 # 10000000   Q7
sgs 39680 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 60160 0xBF # 10111111   Q7
sgs 50240 0x80 # 10000000   Q7
sgs 39680 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 60160 0xBF # 10111111   Q7
sgs 50240 0x80 # 10000000   Q7
sgs 39680 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 60160 0xBF # 10111111   Q7
sgs 40000 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (31 entries, util 17.1600 %)

```
sgs 27840 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 9600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 19840 0x7F # 01111111   Q6
sgs 54400 0x40 # 01000000   Q6
sgs 25600 0xBF # 10111111   Q7
sgs 27840 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 9600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 111680 0x80 # 10000000   Q7
sgs 25600 0xBF # 10111111   Q7
sgs 27840 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 9600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 111680 0x80 # 10000000   Q7
sgs 25600 0xBF # 10111111   Q7
sgs 27840 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 9600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 83840 0x80 # 10000000   Q7
sgs 53440 0xBF # 10111111   Q7
```

### sw05-p5  (13 entries, util 10.9200 %)

```
sgs 60480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 32640 0xBF # 10111111   Q7
sgs 154880 0x40 # 01000000   Q6
sgs 39680 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 60480 0x7F # 01111111   Q6
sgs 139520 0x80 # 10000000   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p4  (23 entries, util 15.6000 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 2880 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 22080 0x7F # 01111111   Q6
sgs 28800 0xBF # 10111111   Q7
sgs 42880 0x80 # 10000000   Q7
sgs 28480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 106240 0x80 # 10000000   Q7
sgs 28480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 22080 0x7F # 01111111   Q6
sgs 28800 0xBF # 10111111   Q7
sgs 42880 0x80 # 10000000   Q7
sgs 28480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 90880 0x80 # 10000000   Q7
sgs 43840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (18 entries, util 12.4800 %)

```
sgs 15360 0x7F # 01111111   Q6
sgs 32320 0x40 # 01000000   Q6
sgs 15680 0xBF # 10111111   Q7
sgs 74240 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 122240 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 122240 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 106880 0x40 # 01000000   Q6
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (13 entries, util 10.9200 %)

```
sgs 52800 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 34240 0xBF # 10111111   Q7
sgs 153280 0x40 # 01000000   Q6
sgs 47360 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 52800 0x7F # 01111111   Q6
sgs 147200 0x80 # 10000000   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p5  (27 entries, util 17.1600 %)

```
sgs 32960 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 16960 0xBF # 10111111   Q7
sgs 28160 0x7F # 01111111   Q6
sgs 51200 0x40 # 01000000   Q6
sgs 20480 0xBF # 10111111   Q7
sgs 32960 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 108800 0x80 # 10000000   Q7
sgs 20480 0xBF # 10111111   Q7
sgs 32960 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 108800 0x80 # 10000000   Q7
sgs 20480 0xBF # 10111111   Q7
sgs 32960 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 75840 0x80 # 10000000   Q7
sgs 53440 0xBF # 10111111   Q7
```

### sw08-p2  (34 entries, util 32.7600 %)

```
sgs 20480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 16960 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 44800 0x7F # 01111111   Q6
sgs 33920 0x40 # 01000000   Q6
sgs 29440 0xBF # 10111111   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 16960 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 91200 0x80 # 10000000   Q7
sgs 29440 0xBF # 10111111   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 16960 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 91200 0x80 # 10000000   Q7
sgs 29440 0xBF # 10111111   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 16960 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 70720 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p4  (15 entries, util 12.4800 %)

```
sgs 7680 0x3F # 00111111   BE
sgs 34880 0x40 # 01000000   Q6
sgs 14080 0xBF # 10111111   Q7
sgs 73280 0x80 # 10000000   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 57600 0xBF # 10111111   Q7
sgs 122240 0x40 # 01000000   Q6
sgs 20160 0x7F # 01111111   Q6
sgs 57600 0xBF # 10111111   Q7
sgs 122240 0x40 # 01000000   Q6
sgs 20160 0x7F # 01111111   Q6
sgs 57600 0xBF # 10111111   Q7
sgs 114560 0x40 # 01000000   Q6
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (13 entries, util 10.9200 %)

```
sgs 45120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 35840 0xBF # 10111111   Q7
sgs 151680 0x40 # 01000000   Q6
sgs 55040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 45120 0x7F # 01111111   Q6
sgs 154880 0x80 # 10000000   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

