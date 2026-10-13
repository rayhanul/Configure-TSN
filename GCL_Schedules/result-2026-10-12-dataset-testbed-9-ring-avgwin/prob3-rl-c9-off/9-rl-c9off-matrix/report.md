# Reconfiguration-free admission (Problem 3)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Frozen schedule W loaded from: **result/result-2026-10-12-dataset-testbed-9-ring-avgwin/rl-c9-off/9-matrix-c9off**

## Admission: W (before) vs. after this run's arrivals

| | admitted | of total |
|---|---|---|
| W (base, unchanged) | 11 | 11 |
| + this run's arrivals | 22 | 39 |

Every arrival admitted here required **zero** window-boundary changes -- see the GCL-entry table below (unchanged from W by construction) and the window-boundary integrity check. No previously-admitted flow was rerouted.

## Arrivals

| id | src->dst | RS(s) size | admitted | route | queue | phi_s (ns) | e2e (ns) | rerouted to make room | reason if rejected |
|---|---|---|---|---|---|---|---|---|---|
| 3 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q6 | 0 | 116800 | - | - |
| 15 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 12480 | 140480 | - | - |
| 13 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 37440 | 95680 | - | - |
| 18 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q6 | 24960 | 45760 | - | - |
| 19 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q6 | 49920 | 195840 | - | - |
| 17 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 225280 | 127680 | - | - |
| 2 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 | 100160 | 178880 | - | - |
| 5 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q7 | 12480 | 45760 | - | - |
| 11 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 462720 | 320320 | - | - |
| 27 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q6 | 237760 | 45760 | - | - |
| 30 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q6 | 250560 | 45760 | - | - |
| 31 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q6 | 263360 | 45760 | - | - |
| 33 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q6 | 276160 | 89600 | - | - |
| 39 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q7 | 37440 | 159360 | - | - |
| 44 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q6 | 332800 | 45760 | - | - |
| 26 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 62400 | 195840 | - | - |
| 29 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 112320 | 300160 | - | - |
| 32 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 40 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 | 146240 | 316160 | - | - |
| 41 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q6 | 107840 | 45760 | - | - |
| 43 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 87360 | 191680 | - | - |
| 49 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 22 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 49920 | 212480 | - | - |
| 23 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 42 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 25 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 | 163200 | 315840 | - | - |
| 34 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 37 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 38 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 46 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 47 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 50 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 21 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 35 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 45 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 24 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 28 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 36 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 48 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |

## Per-port GCL entries (should equal W exactly)

| port | W entries | after arrivals | GCL_size |
|---|---|---|---|
| sw01-p2 | 28 | 28 | 255 |
| sw01-p4 | 22 | 22 | 255 |
| sw01-p5 | 20 | 20 | 255 |
| sw02-p2 | 32 | 32 | 255 |
| sw02-p4 | 9 | 9 | 255 |
| sw02-p5 | 18 | 18 | 255 |
| sw03-p4 | 23 | 23 | 255 |
| sw03-p5 | 20 | 20 | 255 |
| sw04-p4 | 25 | 25 | 255 |
| sw04-p5 | 9 | 9 | 255 |
| sw05-p4 | 19 | 19 | 255 |
| sw05-p5 | 19 | 19 | 255 |
| sw06-p4 | 10 | 10 | 255 |
| sw06-p5 | 21 | 21 | 255 |
| sw07-p4 | 19 | 19 | 255 |
| sw07-p5 | 23 | 23 | 255 |
| sw08-p2 | 19 | 19 | 255 |
| sw08-p4 | 22 | 22 | 255 |
| sw08-p5 | 22 | 22 | 255 |

## Per-hop windows used by newly admitted flows

| flow | egress port | queue | psi (ns, unchanged) | delta (ns, unchanged) |
|---|---|---|---|---|
| s21(id=3 S3->S2) | S3-p0 | Q6 | 0 | 12480 |
| s21(id=3 S3->S2) | sw01-p4 | Q6 | 16640 | 12480 |
| s21(id=3 S3->S2) | sw03-p5 | Q6 | 33280 | 12480 |
| s21(id=3 S3->S2) | sw05-p4 | Q6 | 50240 | 12480 |
| s21(id=3 S3->S2) | sw07-p5 | Q6 | 67200 | 12480 |
| s21(id=3 S3->S2) | sw08-p2 | Q6 | 104320 | 12480 |
| s25(id=15 S2->S1) | S2-p0 | Q6 | 12480 | 12480 |
| s25(id=15 S2->S1) | sw08-p4 | Q6 | 29120 | 12480 |
| s25(id=15 S2->S1) | sw06-p5 | Q6 | 45760 | 12480 |
| s25(id=15 S2->S1) | sw04-p4 | Q6 | 123840 | 12480 |
| s25(id=15 S2->S1) | sw02-p2 | Q6 | 140480 | 12480 |
| s24(id=13 S2->S3) | S2-p0 | Q6 | 37440 | 12480 |
| s24(id=13 S2->S3) | sw08-p5 | Q6 | 54080 | 12480 |
| s24(id=13 S2->S3) | sw07-p4 | Q6 | 70720 | 12480 |
| s24(id=13 S2->S3) | sw05-p5 | Q6 | 87360 | 12480 |
| s24(id=13 S2->S3) | sw03-p4 | Q6 | 104000 | 12480 |
| s24(id=13 S2->S3) | sw01-p2 | Q6 | 120640 | 12480 |
| s27(id=18 S3->S1) | S3-p0 | Q6 | 24960 | 12480 |
| s27(id=18 S3->S1) | sw01-p5 | Q6 | 41600 | 12480 |
| s27(id=18 S3->S1) | sw02-p2 | Q6 | 58240 | 12480 |
| s28(id=19 S3->S2) | S3-p0 | Q6 | 49920 | 12480 |
| s28(id=19 S3->S2) | sw01-p4 | Q6 | 116480 | 12480 |
| s28(id=19 S3->S2) | sw03-p5 | Q6 | 133120 | 12480 |
| s28(id=19 S3->S2) | sw05-p4 | Q6 | 200000 | 12480 |
| s28(id=19 S3->S2) | sw07-p5 | Q6 | 216640 | 12480 |
| s28(id=19 S3->S2) | sw08-p2 | Q6 | 233280 | 12480 |
| s26(id=17 S2->S1) | S2-p0 | Q6 | 225280 | 12480 |
| s26(id=17 S2->S1) | sw08-p4 | Q6 | 241920 | 12480 |
| s26(id=17 S2->S1) | sw06-p5 | Q6 | 296320 | 12480 |
| s26(id=17 S2->S1) | sw04-p4 | Q6 | 323840 | 12480 |
| s26(id=17 S2->S1) | sw02-p2 | Q6 | 340480 | 12480 |
| s20(id=2 S3->S2) | S3-p0 | Q7 | 100160 | 12480 |
| s20(id=2 S3->S2) | sw01-p4 | Q7 | 150080 | 12480 |
| s20(id=2 S3->S2) | sw03-p5 | Q7 | 166720 | 12480 |
| s20(id=2 S3->S2) | sw05-p4 | Q7 | 183360 | 12480 |
| s20(id=2 S3->S2) | sw07-p5 | Q7 | 249920 | 12480 |
| s20(id=2 S3->S2) | sw08-p2 | Q7 | 266560 | 12480 |
| s22(id=5 S1->S3) | S1-p0 | Q7 | 12480 | 12480 |
| s22(id=5 S1->S3) | sw02-p5 | Q7 | 29120 | 12480 |
| s22(id=5 S1->S3) | sw01-p2 | Q7 | 45760 | 12480 |
| s23(id=11 S2->S1) | S2-p0 | Q7 | 462720 | 12480 |
| s23(id=11 S2->S1) | sw08-p4 | Q7 | 479360 | 12480 |
| s23(id=11 S2->S1) | sw06-p5 | Q7 | 496000 | 12480 |
| s23(id=11 S2->S1) | sw04-p4 | Q7 | 656960 | 12480 |
| s23(id=11 S2->S1) | sw02-p2 | Q7 | 770560 | 12480 |
| s35(id=27 S3->S1) | S3-p0 | Q6 | 237760 | 12480 |
| s35(id=27 S3->S1) | sw01-p5 | Q6 | 254400 | 12480 |
| s35(id=27 S3->S1) | sw02-p2 | Q6 | 271040 | 12480 |
| s38(id=30 S3->S1) | S3-p0 | Q6 | 250560 | 12480 |
| s38(id=30 S3->S1) | sw01-p5 | Q6 | 267200 | 12480 |
| s38(id=30 S3->S1) | sw02-p2 | Q6 | 283840 | 12480 |
| s39(id=31 S3->S1) | S3-p0 | Q6 | 263360 | 12480 |
| s39(id=31 S3->S1) | sw01-p5 | Q6 | 280000 | 12480 |
| s39(id=31 S3->S1) | sw02-p2 | Q6 | 296640 | 12480 |
| s41(id=33 S3->S1) | S3-p0 | Q6 | 276160 | 12480 |
| s41(id=33 S3->S1) | sw01-p5 | Q6 | 336640 | 12480 |
| s41(id=33 S3->S1) | sw02-p2 | Q6 | 353280 | 12480 |
| s47(id=39 S1->S3) | S1-p0 | Q7 | 37440 | 12480 |
| s47(id=39 S1->S3) | sw02-p5 | Q7 | 79360 | 12480 |
| s47(id=39 S1->S3) | sw01-p2 | Q7 | 184320 | 12480 |
| s52(id=44 S3->S1) | S3-p0 | Q6 | 332800 | 12480 |
| s52(id=44 S3->S1) | sw01-p5 | Q6 | 349440 | 12480 |
| s52(id=44 S3->S1) | sw02-p2 | Q6 | 366080 | 12480 |
| s34(id=26 S2->S3) | S2-p0 | Q7 | 62400 | 12480 |
| s34(id=26 S2->S3) | sw08-p5 | Q7 | 79040 | 12480 |
| s34(id=26 S2->S3) | sw07-p4 | Q7 | 95680 | 12480 |
| s34(id=26 S2->S3) | sw05-p5 | Q7 | 157760 | 12480 |
| s34(id=26 S2->S3) | sw03-p4 | Q7 | 180480 | 12480 |
| s34(id=26 S2->S3) | sw01-p2 | Q7 | 245760 | 12480 |
| s37(id=29 S2->S3) | S2-p0 | Q6 | 112320 | 12480 |
| s37(id=29 S2->S3) | sw08-p5 | Q6 | 128960 | 12480 |
| s37(id=29 S2->S3) | sw07-p4 | Q6 | 200000 | 12480 |
| s37(id=29 S2->S3) | sw05-p5 | Q6 | 216640 | 12480 |
| s37(id=29 S2->S3) | sw03-p4 | Q6 | 233280 | 12480 |
| s37(id=29 S2->S3) | sw01-p2 | Q6 | 400000 | 12480 |
| s48(id=40 S3->S2) | S3-p0 | Q7 | 146240 | 12480 |
| s48(id=40 S3->S2) | sw01-p4 | Q7 | 162880 | 12480 |
| s48(id=40 S3->S2) | sw03-p5 | Q7 | 179520 | 12480 |
| s48(id=40 S3->S2) | sw05-p4 | Q7 | 350080 | 12480 |
| s48(id=40 S3->S2) | sw07-p5 | Q7 | 366720 | 12480 |
| s48(id=40 S3->S2) | sw08-p2 | Q7 | 449920 | 12480 |
| s49(id=41 S1->S3) | S1-p0 | Q6 | 107840 | 12480 |
| s49(id=41 S1->S3) | sw02-p5 | Q6 | 124480 | 12480 |
| s49(id=41 S1->S3) | sw01-p2 | Q6 | 141120 | 12480 |
| s51(id=43 S2->S3) | S2-p0 | Q7 | 87360 | 12480 |
| s51(id=43 S2->S3) | sw08-p5 | Q7 | 150080 | 12480 |
| s51(id=43 S2->S3) | sw07-p4 | Q7 | 166720 | 12480 |
| s51(id=43 S2->S3) | sw05-p5 | Q7 | 183360 | 12480 |
| s51(id=43 S2->S3) | sw03-p4 | Q7 | 249920 | 12480 |
| s51(id=43 S2->S3) | sw01-p2 | Q7 | 266560 | 12480 |
| s30(id=22 S1->S2) | S1-p0 | Q7 | 49920 | 12480 |
| s30(id=22 S1->S2) | sw02-p4 | Q7 | 66560 | 12480 |
| s30(id=22 S1->S2) | sw04-p5 | Q7 | 83200 | 12480 |
| s30(id=22 S1->S2) | sw06-p4 | Q7 | 99840 | 12480 |
| s30(id=22 S1->S2) | sw08-p2 | Q7 | 150080 | 12480 |
| s33(id=25 S3->S2) | S3-p0 | Q7 | 163200 | 12480 |
| s33(id=25 S3->S2) | sw01-p4 | Q7 | 179840 | 12480 |
| s33(id=25 S3->S2) | sw03-p5 | Q7 | 350080 | 12480 |
| s33(id=25 S3->S2) | sw05-p4 | Q7 | 366720 | 12480 |
| s33(id=25 S3->S2) | sw07-p5 | Q7 | 449920 | 12480 |
| s33(id=25 S3->S2) | sw08-p2 | Q7 | 466560 | 12480 |

## Constraint check

- C1-C7, C9: OK
- window-boundary integrity (no window's psi/delta changed anywhere): OK

## GCL per egress port

### sw01-p2  (28 entries, util 29.6400 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 24960 0x7F # 01111111   Q6
sgs 26240 0x40 # 01000000   Q6
sgs 15680 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0xBF # 10111111   Q7
sgs 101120 0x80 # 10000000   Q7
sgs 15680 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 63680 0x40 # 01000000   Q6
sgs 15680 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0xBF # 10111111   Q7
sgs 67840 0x80 # 10000000   Q7
sgs 48960 0xBF # 10111111   Q7
```

### sw01-p4  (22 entries, util 17.1600 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 54080 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 33600 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 68800 0x40 # 01000000   Q6
sgs 14720 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 68800 0x40 # 01000000   Q6
sgs 14720 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 52160 0x40 # 01000000   Q6
sgs 31360 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p5  (20 entries, util 24.9600 %)

```
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 90880 0x40 # 01000000   Q6
sgs 30080 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 128320 0x40 # 01000000   Q6
sgs 30080 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 115840 0x80 # 10000000   Q7
sgs 30080 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 99200 0x40 # 01000000   Q6
sgs 59200 0xBF # 10111111   Q7
```

### sw02-p2  (32 entries, util 43.6800 %)

```
sgs 45760 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 33280 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 10880 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 49920 0x40 # 01000000   Q6
sgs 29440 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 52800 0x40 # 01000000   Q6
sgs 29440 0x7F # 01111111   Q6
sgs 75840 0x40 # 01000000   Q6
sgs 29440 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 33280 0x80 # 10000000   Q7
sgs 13120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 10880 0x3F # 00111111   BE
sgs 75840 0x40 # 01000000   Q6
sgs 29440 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 52800 0x40 # 01000000   Q6
sgs 29440 0x7F # 01111111   Q6
sgs 30080 0x40 # 01000000   Q6
sgs 29440 0xBF # 10111111   Q7
```

### sw02-p4  (9 entries, util 4.6800 %)

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

### sw02-p5  (18 entries, util 14.0400 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 80640 0x80 # 10000000   Q7
sgs 40320 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 93120 0x40 # 01000000   Q6
sgs 40320 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 80640 0x80 # 10000000   Q7
sgs 40320 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 76480 0x40 # 01000000   Q6
sgs 56960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (23 entries, util 15.6000 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 24960 0x7F # 01111111   Q6
sgs 32960 0x40 # 01000000   Q6
sgs 25600 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 107840 0x80 # 10000000   Q7
sgs 25600 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 70400 0x40 # 01000000   Q6
sgs 25600 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 41280 0x80 # 10000000   Q7
sgs 42240 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p5  (20 entries, util 17.1600 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 54400 0xBF # 10111111   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 16960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 68800 0x40 # 01000000   Q6
sgs 48000 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 68800 0x40 # 01000000   Q6
sgs 48000 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 35520 0x40 # 01000000   Q6
sgs 31360 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p4  (25 entries, util 18.7200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 11520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 107200 0x40 # 01000000   Q6
sgs 43200 0xBF # 10111111   Q7
sgs 23680 0x7F # 01111111   Q6
sgs 84160 0x40 # 01000000   Q6
sgs 41920 0x7F # 01111111   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 11520 0x3F # 00111111   BE
sgs 133120 0x40 # 01000000   Q6
sgs 43200 0xBF # 10111111   Q7
sgs 23680 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 13760 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (9 entries, util 4.6800 %)

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

### sw05-p4  (19 entries, util 17.1600 %)

```
sgs 50240 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0xBF # 10111111   Q7
sgs 37120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 50240 0xBF # 10111111   Q7
sgs 50240 0x7F # 01111111   Q6
sgs 68800 0x40 # 01000000   Q6
sgs 31040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 50240 0x7F # 01111111   Q6
sgs 68800 0x40 # 01000000   Q6
sgs 31040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 50240 0x7F # 01111111   Q6
sgs 18560 0x40 # 01000000   Q6
sgs 31360 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p5  (19 entries, util 15.6000 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 24960 0x7F # 01111111   Q6
sgs 32960 0x40 # 01000000   Q6
sgs 42240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 107840 0x80 # 10000000   Q7
sgs 42240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 70400 0x40 # 01000000   Q6
sgs 42240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 57920 0x80 # 10000000   Q7
sgs 42240 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p4  (10 entries, util 4.6800 %)

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

### sw06-p5  (21 entries, util 18.7200 %)

```
sgs 45760 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 39040 0x40 # 01000000   Q6
sgs 27840 0xBF # 10111111   Q7
sgs 45760 0x7F # 01111111   Q6
sgs 126400 0x40 # 01000000   Q6
sgs 27840 0xBF # 10111111   Q7
sgs 45760 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 88960 0x80 # 10000000   Q7
sgs 27840 0xBF # 10111111   Q7
sgs 45760 0x7F # 01111111   Q6
sgs 80640 0x40 # 01000000   Q6
sgs 23680 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (19 entries, util 15.6000 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 32960 0x40 # 01000000   Q6
sgs 58880 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 107840 0x80 # 10000000   Q7
sgs 58880 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 70400 0x40 # 01000000   Q6
sgs 58880 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 74560 0x80 # 10000000   Q7
sgs 42240 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p5  (23 entries, util 17.1600 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 17280 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 20480 0xBF # 10111111   Q7
sgs 53760 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 33600 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 17280 0xBF # 10111111   Q7
sgs 68800 0x40 # 01000000   Q6
sgs 14080 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 17280 0xBF # 10111111   Q7
sgs 68800 0x40 # 01000000   Q6
sgs 14080 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 17280 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 20480 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p2  (19 entries, util 21.8400 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 33280 0x7F # 01111111   Q6
sgs 20480 0xBF # 10111111   Q7
sgs 23040 0x80 # 10000000   Q7
sgs 56320 0x7F # 01111111   Q6
sgs 54400 0xBF # 10111111   Q7
sgs 89280 0x40 # 01000000   Q6
sgs 56320 0x7F # 01111111   Q6
sgs 54400 0xBF # 10111111   Q7
sgs 89280 0x40 # 01000000   Q6
sgs 56320 0x7F # 01111111   Q6
sgs 54400 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 33280 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p4  (22 entries, util 18.7200 %)

```
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 21120 0xBF # 10111111   Q7
sgs 16320 0x7F # 01111111   Q6
sgs 39040 0x40 # 01000000   Q6
sgs 44480 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 126400 0x40 # 01000000   Q6
sgs 44480 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 88960 0x80 # 10000000   Q7
sgs 44480 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 97280 0x40 # 01000000   Q6
sgs 23680 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (22 entries, util 15.6000 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 32960 0x40 # 01000000   Q6
sgs 25600 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 107840 0x80 # 10000000   Q7
sgs 25600 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 70400 0x40 # 01000000   Q6
sgs 25600 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 91200 0x80 # 10000000   Q7
sgs 42240 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

