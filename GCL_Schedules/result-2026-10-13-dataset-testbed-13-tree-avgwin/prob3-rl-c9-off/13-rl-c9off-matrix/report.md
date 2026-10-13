# Reconfiguration-free admission (Problem 3)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Frozen schedule W loaded from: **result/result-2026-10-13-dataset-testbed-13-tree-avgwin/rl-c9-off/13-matrix-c9off**

## Admission: W (before) vs. after this run's arrivals

| | admitted | of total |
|---|---|---|
| W (base, unchanged) | 11 | 11 |
| + this run's arrivals | 16 | 39 |

Every arrival admitted here required **zero** window-boundary changes -- see the GCL-entry table below (unchanged from W by construction) and the window-boundary integrity check. No previously-admitted flow was rerouted.

## Arrivals

| id | src->dst | RS(s) size | admitted | route | queue | phi_s (ns) | e2e (ns) | rerouted to make room | reason if rejected |
|---|---|---|---|---|---|---|---|---|---|
| 7 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 16 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 11 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 12480 | 95680 | - | - |
| 1 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 | 12480 | 249920 | - | - |
| 12 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 37440 | 97600 | - | - |
| 18 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 62400 | 109760 | - | - |
| 6 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q7 | 49920 | 145600 | - | - |
| 4 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 2 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 150080 | 312320 | - | - |
| 32 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 40 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 42 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 49 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 437760 | 341440 | - | - |
| 22 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 48 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 | 545280 | 216320 | - | - |
| 26 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q7 | 145280 | 212800 | - | - |
| 31 | S1->S3 | - | yes | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 70080 | 151680 | - | - |
| 37 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q7 | 158080 | 212800 | - | - |
| 44 | S1->S3 | - | yes | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 82880 | 151680 | - | - |
| 25 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 36 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 41 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q6 | 111040 | 134720 | - | - |
| 45 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q6 | 75200 | 95680 | - | - |
| 23 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q7 | 170880 | 212800 | - | - |
| 24 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 29 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 38 | S1->S3 | - | yes | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 212800 | 145600 | - | - |
| 46 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 47 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 30 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 34 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 35 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 39 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 21 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 28 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 33 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 43 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 50 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 27 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |

## Per-port GCL entries (should equal W exactly)

| port | W entries | after arrivals | GCL_size |
|---|---|---|---|
| sw01-p2 | 30 | 30 | 255 |
| sw01-p4 | 22 | 22 | 255 |
| sw02-p2 | 31 | 31 | 255 |
| sw02-p4 | 22 | 22 | 255 |
| sw03-p4 | 30 | 30 | 255 |
| sw03-p5 | 22 | 22 | 255 |
| sw04-p4 | 25 | 25 | 255 |
| sw04-p5 | 19 | 19 | 255 |
| sw05-p4 | 19 | 19 | 255 |
| sw05-p5 | 33 | 33 | 255 |
| sw06-p4 | 20 | 20 | 255 |
| sw06-p5 | 26 | 26 | 255 |
| sw07-p4 | 29 | 29 | 255 |
| sw07-p5 | 23 | 23 | 255 |
| sw08-p2 | 20 | 20 | 255 |
| sw08-p4 | 30 | 30 | 255 |
| sw08-p5 | 29 | 29 | 255 |

## Per-hop windows used by newly admitted flows

| flow | egress port | queue | psi (ns, unchanged) | delta (ns, unchanged) |
|---|---|---|---|---|
| s25(id=11 S2->S3) | S2-p0 | Q7 | 12480 | 12480 |
| s25(id=11 S2->S3) | sw08-p5 | Q7 | 29120 | 12480 |
| s25(id=11 S2->S3) | sw07-p4 | Q7 | 45760 | 12480 |
| s25(id=11 S2->S3) | sw05-p5 | Q7 | 62400 | 12480 |
| s25(id=11 S2->S3) | sw03-p4 | Q7 | 79040 | 12480 |
| s25(id=11 S2->S3) | sw01-p2 | Q7 | 95680 | 12480 |
| s20(id=1 S3->S2) | S3-p0 | Q7 | 12480 | 12480 |
| s20(id=1 S3->S2) | sw01-p4 | Q7 | 29120 | 12480 |
| s20(id=1 S3->S2) | sw03-p5 | Q7 | 45760 | 12480 |
| s20(id=1 S3->S2) | sw05-p4 | Q7 | 62400 | 12480 |
| s20(id=1 S3->S2) | sw07-p5 | Q7 | 79040 | 12480 |
| s20(id=1 S3->S2) | sw08-p2 | Q7 | 249920 | 12480 |
| s26(id=12 S2->S3) | S2-p0 | Q7 | 37440 | 12480 |
| s26(id=12 S2->S3) | sw08-p5 | Q7 | 56000 | 12480 |
| s26(id=12 S2->S3) | sw07-p4 | Q7 | 72640 | 12480 |
| s26(id=12 S2->S3) | sw05-p5 | Q7 | 89280 | 12480 |
| s26(id=12 S2->S3) | sw03-p4 | Q7 | 105920 | 12480 |
| s26(id=12 S2->S3) | sw01-p2 | Q7 | 122560 | 12480 |
| s28(id=18 S2->S1) | S2-p0 | Q6 | 62400 | 12480 |
| s28(id=18 S2->S1) | sw08-p4 | Q6 | 109760 | 12480 |
| s28(id=18 S2->S1) | sw06-p5 | Q6 | 126400 | 12480 |
| s28(id=18 S2->S1) | sw04-p4 | Q6 | 143040 | 12480 |
| s28(id=18 S2->S1) | sw02-p2 | Q6 | 159680 | 12480 |
| s23(id=6 S3->S1) | S3-p0 | Q7 | 49920 | 12480 |
| s23(id=6 S3->S1) | sw01-p4 | Q7 | 66560 | 12480 |
| s23(id=6 S3->S1) | sw03-p5 | Q7 | 83200 | 12480 |
| s23(id=6 S3->S1) | sw05-p4 | Q7 | 99840 | 12480 |
| s23(id=6 S3->S1) | sw07-p5 | Q7 | 116480 | 12480 |
| s23(id=6 S3->S1) | sw08-p4 | Q7 | 133120 | 12480 |
| s23(id=6 S3->S1) | sw06-p5 | Q7 | 149760 | 12480 |
| s23(id=6 S3->S1) | sw04-p4 | Q7 | 166400 | 12480 |
| s23(id=6 S3->S1) | sw02-p2 | Q7 | 183040 | 12480 |
| s21(id=2 S1->S2) | S1-p0 | Q7 | 150080 | 12480 |
| s21(id=2 S1->S2) | sw02-p4 | Q7 | 166720 | 12480 |
| s21(id=2 S1->S2) | sw04-p5 | Q7 | 183360 | 12480 |
| s21(id=2 S1->S2) | sw06-p4 | Q7 | 360960 | 12480 |
| s21(id=2 S1->S2) | sw08-p2 | Q7 | 449920 | 12480 |
| s57(id=49 S1->S2) | S1-p0 | Q7 | 437760 | 12480 |
| s57(id=49 S1->S2) | sw02-p4 | Q7 | 454400 | 12480 |
| s57(id=49 S1->S2) | sw04-p5 | Q7 | 471040 | 12480 |
| s57(id=49 S1->S2) | sw06-p4 | Q7 | 750080 | 12480 |
| s57(id=49 S1->S2) | sw08-p2 | Q7 | 766720 | 12480 |
| s56(id=48 S3->S2) | S3-p0 | Q7 | 545280 | 12480 |
| s56(id=48 S3->S2) | sw01-p4 | Q7 | 561920 | 12480 |
| s56(id=48 S3->S2) | sw03-p5 | Q7 | 578560 | 12480 |
| s56(id=48 S3->S2) | sw05-p4 | Q7 | 662400 | 12480 |
| s56(id=48 S3->S2) | sw07-p5 | Q7 | 679040 | 12480 |
| s56(id=48 S3->S2) | sw08-p2 | Q7 | 749120 | 12480 |
| s34(id=26 S3->S1) | S3-p0 | Q7 | 145280 | 12480 |
| s34(id=26 S3->S1) | sw01-p4 | Q7 | 161920 | 12480 |
| s34(id=26 S3->S1) | sw03-p5 | Q7 | 178560 | 12480 |
| s34(id=26 S3->S1) | sw05-p4 | Q7 | 262400 | 12480 |
| s34(id=26 S3->S1) | sw07-p5 | Q7 | 279040 | 12480 |
| s34(id=26 S3->S1) | sw08-p4 | Q7 | 295680 | 12480 |
| s34(id=26 S3->S1) | sw06-p5 | Q7 | 312320 | 12480 |
| s34(id=26 S3->S1) | sw04-p4 | Q7 | 328960 | 12480 |
| s34(id=26 S3->S1) | sw02-p2 | Q7 | 345600 | 12480 |
| s39(id=31 S1->S3) | S1-p0 | Q6 | 70080 | 12480 |
| s39(id=31 S1->S3) | sw02-p4 | Q6 | 86720 | 12480 |
| s39(id=31 S1->S3) | sw04-p5 | Q6 | 109440 | 12480 |
| s39(id=31 S1->S3) | sw06-p4 | Q6 | 126080 | 12480 |
| s39(id=31 S1->S3) | sw08-p5 | Q6 | 142720 | 12480 |
| s39(id=31 S1->S3) | sw07-p4 | Q6 | 159360 | 12480 |
| s39(id=31 S1->S3) | sw05-p5 | Q6 | 176000 | 12480 |
| s39(id=31 S1->S3) | sw03-p4 | Q6 | 192640 | 12480 |
| s39(id=31 S1->S3) | sw01-p2 | Q6 | 209280 | 12480 |
| s45(id=37 S3->S1) | S3-p0 | Q7 | 158080 | 12480 |
| s45(id=37 S3->S1) | sw01-p4 | Q7 | 174720 | 12480 |
| s45(id=37 S3->S1) | sw03-p5 | Q7 | 258560 | 12480 |
| s45(id=37 S3->S1) | sw05-p4 | Q7 | 275200 | 12480 |
| s45(id=37 S3->S1) | sw07-p5 | Q7 | 291840 | 12480 |
| s45(id=37 S3->S1) | sw08-p4 | Q7 | 308480 | 12480 |
| s45(id=37 S3->S1) | sw06-p5 | Q7 | 325120 | 12480 |
| s45(id=37 S3->S1) | sw04-p4 | Q7 | 341760 | 12480 |
| s45(id=37 S3->S1) | sw02-p2 | Q7 | 358400 | 12480 |
| s52(id=44 S1->S3) | S1-p0 | Q6 | 82880 | 12480 |
| s52(id=44 S1->S3) | sw02-p4 | Q6 | 105600 | 12480 |
| s52(id=44 S1->S3) | sw04-p5 | Q6 | 122240 | 12480 |
| s52(id=44 S1->S3) | sw06-p4 | Q6 | 138880 | 12480 |
| s52(id=44 S1->S3) | sw08-p5 | Q6 | 155520 | 12480 |
| s52(id=44 S1->S3) | sw07-p4 | Q6 | 172160 | 12480 |
| s52(id=44 S1->S3) | sw05-p5 | Q6 | 188800 | 12480 |
| s52(id=44 S1->S3) | sw03-p4 | Q6 | 205440 | 12480 |
| s52(id=44 S1->S3) | sw01-p2 | Q6 | 222080 | 12480 |
| s49(id=41 S1->S2) | S1-p0 | Q6 | 111040 | 12480 |
| s49(id=41 S1->S2) | sw02-p4 | Q6 | 127680 | 12480 |
| s49(id=41 S1->S2) | sw04-p5 | Q6 | 200000 | 12480 |
| s49(id=41 S1->S2) | sw06-p4 | Q6 | 216640 | 12480 |
| s49(id=41 S1->S2) | sw08-p2 | Q6 | 233280 | 12480 |
| s53(id=45 S3->S2) | S3-p0 | Q6 | 75200 | 12480 |
| s53(id=45 S3->S2) | sw01-p4 | Q6 | 91840 | 12480 |
| s53(id=45 S3->S2) | sw03-p5 | Q6 | 108480 | 12480 |
| s53(id=45 S3->S2) | sw05-p4 | Q6 | 125120 | 12480 |
| s53(id=45 S3->S2) | sw07-p5 | Q6 | 141760 | 12480 |
| s53(id=45 S3->S2) | sw08-p2 | Q6 | 158400 | 12480 |
| s31(id=23 S3->S1) | S3-p0 | Q7 | 170880 | 12480 |
| s31(id=23 S3->S1) | sw01-p4 | Q7 | 254720 | 12480 |
| s31(id=23 S3->S1) | sw03-p5 | Q7 | 271360 | 12480 |
| s31(id=23 S3->S1) | sw05-p4 | Q7 | 288000 | 12480 |
| s31(id=23 S3->S1) | sw07-p5 | Q7 | 304640 | 12480 |
| s31(id=23 S3->S1) | sw08-p4 | Q7 | 321280 | 12480 |
| s31(id=23 S3->S1) | sw06-p5 | Q7 | 337920 | 12480 |
| s31(id=23 S3->S1) | sw04-p4 | Q7 | 354560 | 12480 |
| s31(id=23 S3->S1) | sw02-p2 | Q7 | 371200 | 12480 |
| s46(id=38 S1->S3) | S1-p0 | Q6 | 212800 | 12480 |
| s46(id=38 S1->S3) | sw02-p4 | Q6 | 229440 | 12480 |
| s46(id=38 S1->S3) | sw04-p5 | Q6 | 246080 | 12480 |
| s46(id=38 S1->S3) | sw06-p4 | Q6 | 262720 | 12480 |
| s46(id=38 S1->S3) | sw08-p5 | Q6 | 279360 | 12480 |
| s46(id=38 S1->S3) | sw07-p4 | Q6 | 296000 | 12480 |
| s46(id=38 S1->S3) | sw05-p5 | Q6 | 312640 | 12480 |
| s46(id=38 S1->S3) | sw03-p4 | Q6 | 329280 | 12480 |
| s46(id=38 S1->S3) | sw01-p2 | Q6 | 345920 | 12480 |

## Constraint check

- C1-C7, C9: OK
- window-boundary integrity (no window's psi/delta changed anywhere): OK

## GCL per egress port

### sw01-p2  (30 entries, util 31.2000 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 45760 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 1920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 59520 0x40 # 01000000   Q6
sgs 39680 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 147840 0x40 # 01000000   Q6
sgs 39680 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 1920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 85120 0x40 # 01000000   Q6
sgs 39680 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 52160 0x40 # 01000000   Q6
sgs 39680 0xBF # 10111111   Q7
```

### sw01-p4  (22 entries, util 26.5200 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 82880 0x40 # 01000000   Q6
sgs 38080 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 132800 0x80 # 10000000   Q7
sgs 38080 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 107840 0x40 # 01000000   Q6
sgs 38080 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 116160 0x80 # 10000000   Q7
sgs 54720 0xBF # 10111111   Q7
```

### sw02-p2  (31 entries, util 20.2800 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 21120 0xBF # 10111111   Q7
sgs 16320 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 10880 0x3F # 00111111   BE
sgs 23360 0x80 # 10000000   Q7
sgs 43520 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 18880 0x40 # 01000000   Q6
sgs 14720 0xBF # 10111111   Q7
sgs 45440 0x7F # 01111111   Q6
sgs 60800 0x80 # 10000000   Q7
sgs 43520 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 21120 0xBF # 10111111   Q7
sgs 16320 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 46720 0x40 # 01000000   Q6
sgs 43520 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 18880 0x40 # 01000000   Q6
sgs 14720 0xBF # 10111111   Q7
sgs 45440 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 41920 0xBF # 10111111   Q7
```

### sw02-p4  (22 entries, util 23.4000 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 19840 0xBF # 10111111   Q7
sgs 53760 0x40 # 01000000   Q6
sgs 22400 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 111040 0x40 # 01000000   Q6
sgs 22400 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 86080 0x80 # 10000000   Q7
sgs 22400 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 94400 0x40 # 01000000   Q6
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (30 entries, util 31.2000 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 1920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 59520 0x40 # 01000000   Q6
sgs 39680 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 147840 0x40 # 01000000   Q6
sgs 39680 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 1920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 85120 0x40 # 01000000   Q6
sgs 39680 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 68800 0x40 # 01000000   Q6
sgs 39680 0xBF # 10111111   Q7
```

### sw03-p5  (22 entries, util 26.5200 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 82880 0x40 # 01000000   Q6
sgs 21440 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 132800 0x80 # 10000000   Q7
sgs 21440 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 107840 0x40 # 01000000   Q6
sgs 21440 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 99520 0x80 # 10000000   Q7
sgs 54720 0xBF # 10111111   Q7
```

### sw04-p4  (25 entries, util 20.2800 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 10880 0x3F # 00111111   BE
sgs 23360 0x80 # 10000000   Q7
sgs 60160 0x7F # 01111111   Q6
sgs 18880 0x40 # 01000000   Q6
sgs 31360 0xBF # 10111111   Q7
sgs 28800 0x7F # 01111111   Q6
sgs 60800 0x80 # 10000000   Q7
sgs 60160 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 46720 0x40 # 01000000   Q6
sgs 60160 0x7F # 01111111   Q6
sgs 18880 0x40 # 01000000   Q6
sgs 31360 0xBF # 10111111   Q7
sgs 28800 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 58560 0xBF # 10111111   Q7
```

### sw04-p5  (19 entries, util 23.4000 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 19840 0xBF # 10111111   Q7
sgs 53760 0x40 # 01000000   Q6
sgs 55680 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 111040 0x40 # 01000000   Q6
sgs 55680 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 86080 0x80 # 10000000   Q7
sgs 55680 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 77760 0x40 # 01000000   Q6
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (19 entries, util 26.5200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 82880 0x40 # 01000000   Q6
sgs 54720 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 132800 0x80 # 10000000   Q7
sgs 54720 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 107840 0x40 # 01000000   Q6
sgs 54720 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 82880 0x80 # 10000000   Q7
sgs 54720 0xBF # 10111111   Q7
```

### sw05-p5  (33 entries, util 31.2000 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 1920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 59520 0x40 # 01000000   Q6
sgs 27200 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 147840 0x40 # 01000000   Q6
sgs 27200 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 1920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 85120 0x40 # 01000000   Q6
sgs 27200 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 85440 0x40 # 01000000   Q6
sgs 39680 0xBF # 10111111   Q7
```

### sw06-p4  (20 entries, util 23.4000 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 13120 0x7F # 01111111   Q6
sgs 47680 0x40 # 01000000   Q6
sgs 39040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 111040 0x40 # 01000000   Q6
sgs 39040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 86080 0x80 # 10000000   Q7
sgs 39040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 61120 0x40 # 01000000   Q6
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (26 entries, util 20.2800 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 10880 0x3F # 00111111   BE
sgs 23360 0x80 # 10000000   Q7
sgs 26880 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 18880 0x40 # 01000000   Q6
sgs 60160 0xBF # 10111111   Q7
sgs 60800 0x80 # 10000000   Q7
sgs 26880 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 46720 0x40 # 01000000   Q6
sgs 26880 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 18880 0x40 # 01000000   Q6
sgs 60160 0xBF # 10111111   Q7
sgs 27520 0x80 # 10000000   Q7
sgs 60160 0xBF # 10111111   Q7
```

### sw07-p4  (29 entries, util 31.2000 %)

```
sgs 45760 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 1920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 23040 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 59520 0x40 # 01000000   Q6
sgs 39680 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 147840 0x40 # 01000000   Q6
sgs 39680 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 1920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 23040 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 85120 0x40 # 01000000   Q6
sgs 39680 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 102080 0x40 # 01000000   Q6
sgs 39680 0xBF # 10111111   Q7
```

### sw07-p5  (23 entries, util 26.5200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 82880 0x40 # 01000000   Q6
sgs 38080 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 132800 0x80 # 10000000   Q7
sgs 38080 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 107840 0x40 # 01000000   Q6
sgs 38080 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 66240 0x80 # 10000000   Q7
sgs 54720 0xBF # 10111111   Q7
```

### sw08-p2  (20 entries, util 31.2000 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 29120 0x40 # 01000000   Q6
sgs 24960 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 70080 0x40 # 01000000   Q6
sgs 34240 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 149120 0x40 # 01000000   Q6
sgs 34240 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 29120 0x40 # 01000000   Q6
sgs 24960 0x7F # 01111111   Q6
sgs 95040 0x40 # 01000000   Q6
sgs 34240 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 82560 0x40 # 01000000   Q6
sgs 50880 0xBF # 10111111   Q7
```

### sw08-p4  (30 entries, util 20.2800 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 30720 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 10880 0x3F # 00111111   BE
sgs 23360 0x80 # 10000000   Q7
sgs 43520 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 18880 0x40 # 01000000   Q6
sgs 14400 0x7F # 01111111   Q6
sgs 45760 0xBF # 10111111   Q7
sgs 60800 0x80 # 10000000   Q7
sgs 43520 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 30720 0xBF # 10111111   Q7
sgs 46720 0x40 # 01000000   Q6
sgs 43520 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 18880 0x40 # 01000000   Q6
sgs 14400 0x7F # 01111111   Q6
sgs 45760 0xBF # 10111111   Q7
sgs 44160 0x80 # 10000000   Q7
sgs 60160 0xBF # 10111111   Q7
```

### sw08-p5  (29 entries, util 31.2000 %)

```
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 1920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 23040 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 59520 0x40 # 01000000   Q6
sgs 39680 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 147840 0x40 # 01000000   Q6
sgs 39680 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 1920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 23040 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 85120 0x40 # 01000000   Q6
sgs 39680 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 118720 0x40 # 01000000   Q6
sgs 39680 0xBF # 10111111   Q7
```

