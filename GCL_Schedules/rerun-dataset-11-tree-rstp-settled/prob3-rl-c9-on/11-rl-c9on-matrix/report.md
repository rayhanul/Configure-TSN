# Reconfiguration-free admission (Problem 3)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Frozen schedule W loaded from: **result/result-2026-10-13-dataset-testbed-11-tree-avgwin/rl-c9-on/11-matrix-c9on**

## Admission: W (before) vs. after this run's arrivals

| | admitted | of total |
|---|---|---|
| W (base, unchanged) | 10 | 10 |
| + this run's arrivals | 17 | 40 |

Every arrival admitted here required **zero** window-boundary changes -- see the GCL-entry table below (unchanged from W by construction) and the window-boundary integrity check. No previously-admitted flow was rerouted.

## Arrivals

| id | src->dst | RS(s) size | admitted | route | queue | phi_s (ns) | e2e (ns) | rerouted to make room | reason if rejected |
|---|---|---|---|---|---|---|---|---|---|
| 6 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q7 | 62400 | 136320 | - | - |
| 11 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 14 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 16 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q7 | 274880 | 125120 | - | - |
| 4 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 24960 | 67200 | - | - |
| 12 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 74880 | 207680 | - | - |
| 17 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 13 | S1->S3 | - | yes | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 12480 | 139200 | - | - |
| 19 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q6 | 87360 | 98880 | - | - |
| 15 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 12480 | 54080 | - | - |
| 23 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 49920 | 39360 | - | - |
| 25 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 212480 | 39360 | - | - |
| 27 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 28 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 168320 | 191040 | - | - |
| 36 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 224960 | 45760 | - | - |
| 49 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 50 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 367680 | 102400 | - | - |
| 48 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 37 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q6 | 120320 | 492160 | - | - |
| 46 | S1->S3 | - | yes | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 150080 | 149760 | - | - |
| 33 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 34 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 35 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 237440 | 45760 | - | - |
| 41 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 44 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 22 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 40 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 127680 | 215360 | - | - |
| 42 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 350080 | 46080 | - | - |
| 43 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 39 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
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
| sw01-p2 | 24 | 24 | 255 |
| sw01-p4 | 18 | 18 | 255 |
| sw02-p2 | 24 | 24 | 255 |
| sw02-p4 | 29 | 29 | 255 |
| sw03-p4 | 23 | 23 | 255 |
| sw03-p5 | 18 | 18 | 255 |
| sw04-p4 | 23 | 23 | 255 |
| sw04-p5 | 32 | 32 | 255 |
| sw05-p4 | 18 | 18 | 255 |
| sw05-p5 | 21 | 21 | 255 |
| sw06-p4 | 30 | 30 | 255 |
| sw06-p5 | 21 | 21 | 255 |
| sw07-p4 | 23 | 23 | 255 |
| sw07-p5 | 15 | 15 | 255 |
| sw08-p2 | 25 | 25 | 255 |
| sw08-p4 | 21 | 21 | 255 |
| sw08-p5 | 23 | 23 | 255 |

## Per-hop windows used by newly admitted flows

| flow | egress port | queue | psi (ns, unchanged) | delta (ns, unchanged) |
|---|---|---|---|---|
| s21(id=6 S3->S1) | S3-p0 | Q7 | 62400 | 12480 |
| s21(id=6 S3->S1) | sw01-p4 | Q7 | 101440 | 12480 |
| s21(id=6 S3->S1) | sw03-p5 | Q7 | 109760 | 12480 |
| s21(id=6 S3->S1) | sw05-p4 | Q7 | 118080 | 12480 |
| s21(id=6 S3->S1) | sw07-p5 | Q7 | 126400 | 12480 |
| s21(id=6 S3->S1) | sw08-p4 | Q7 | 163200 | 12480 |
| s21(id=6 S3->S1) | sw06-p5 | Q7 | 170880 | 12480 |
| s21(id=6 S3->S1) | sw04-p4 | Q7 | 178560 | 12480 |
| s21(id=6 S3->S1) | sw02-p2 | Q7 | 186240 | 12480 |
| s27(id=16 S3->S1) | S3-p0 | Q7 | 274880 | 12480 |
| s27(id=16 S3->S1) | sw01-p4 | Q7 | 283200 | 12480 |
| s27(id=16 S3->S1) | sw03-p5 | Q7 | 291520 | 12480 |
| s27(id=16 S3->S1) | sw05-p4 | Q7 | 299840 | 12480 |
| s27(id=16 S3->S1) | sw07-p5 | Q7 | 347840 | 12480 |
| s27(id=16 S3->S1) | sw08-p4 | Q7 | 362560 | 12480 |
| s27(id=16 S3->S1) | sw06-p5 | Q7 | 370880 | 12480 |
| s27(id=16 S3->S1) | sw04-p4 | Q7 | 379200 | 12480 |
| s27(id=16 S3->S1) | sw02-p2 | Q7 | 387520 | 12480 |
| s20(id=4 S2->S3) | S2-p0 | Q7 | 24960 | 12480 |
| s20(id=4 S2->S3) | sw08-p5 | Q7 | 33600 | 12480 |
| s20(id=4 S2->S3) | sw07-p4 | Q7 | 42240 | 12480 |
| s20(id=4 S2->S3) | sw05-p5 | Q7 | 62400 | 12480 |
| s20(id=4 S2->S3) | sw03-p4 | Q7 | 71040 | 12480 |
| s20(id=4 S2->S3) | sw01-p2 | Q7 | 79680 | 12480 |
| s23(id=12 S2->S3) | S2-p0 | Q7 | 74880 | 12480 |
| s23(id=12 S2->S3) | sw08-p5 | Q7 | 83200 | 12480 |
| s23(id=12 S2->S3) | sw07-p4 | Q7 | 249920 | 12480 |
| s23(id=12 S2->S3) | sw05-p5 | Q7 | 256640 | 12480 |
| s23(id=12 S2->S3) | sw03-p4 | Q7 | 263360 | 12480 |
| s23(id=12 S2->S3) | sw01-p2 | Q7 | 270080 | 12480 |
| s24(id=13 S1->S3) | S1-p0 | Q6 | 12480 | 12480 |
| s24(id=13 S1->S3) | sw02-p4 | Q6 | 20800 | 12480 |
| s24(id=13 S1->S3) | sw04-p5 | Q6 | 29120 | 12480 |
| s24(id=13 S1->S3) | sw06-p4 | Q6 | 37440 | 12480 |
| s24(id=13 S1->S3) | sw08-p5 | Q6 | 112320 | 12480 |
| s24(id=13 S1->S3) | sw07-p4 | Q6 | 119040 | 12480 |
| s24(id=13 S1->S3) | sw05-p5 | Q6 | 125760 | 12480 |
| s24(id=13 S1->S3) | sw03-p4 | Q6 | 132480 | 12480 |
| s24(id=13 S1->S3) | sw01-p2 | Q6 | 139200 | 12480 |
| s29(id=19 S3->S1) | S3-p0 | Q6 | 87360 | 12480 |
| s29(id=19 S3->S1) | sw01-p4 | Q6 | 118080 | 12480 |
| s29(id=19 S3->S1) | sw03-p5 | Q6 | 125760 | 12480 |
| s29(id=19 S3->S1) | sw05-p4 | Q6 | 133440 | 12480 |
| s29(id=19 S3->S1) | sw07-p5 | Q6 | 141120 | 12480 |
| s29(id=19 S3->S1) | sw08-p4 | Q6 | 150720 | 12480 |
| s29(id=19 S3->S1) | sw06-p5 | Q6 | 158400 | 12480 |
| s29(id=19 S3->S1) | sw04-p4 | Q6 | 166080 | 12480 |
| s29(id=19 S3->S1) | sw02-p2 | Q6 | 173760 | 12480 |
| s26(id=15 S2->S3) | S2-p0 | Q6 | 12480 | 12480 |
| s26(id=15 S2->S3) | sw08-p5 | Q6 | 20800 | 12480 |
| s26(id=15 S2->S3) | sw07-p4 | Q6 | 29120 | 12480 |
| s26(id=15 S2->S3) | sw05-p5 | Q6 | 37440 | 12480 |
| s26(id=15 S2->S3) | sw03-p4 | Q6 | 45760 | 12480 |
| s26(id=15 S2->S3) | sw01-p2 | Q6 | 54080 | 12480 |
| s32(id=23 S2->S1) | S2-p0 | Q7 | 49920 | 12480 |
| s32(id=23 S2->S1) | sw08-p4 | Q7 | 56640 | 12480 |
| s32(id=23 S2->S1) | sw06-p5 | Q7 | 63360 | 12480 |
| s32(id=23 S2->S1) | sw04-p4 | Q7 | 70080 | 12480 |
| s32(id=23 S2->S1) | sw02-p2 | Q7 | 76800 | 12480 |
| s34(id=25 S2->S1) | S2-p0 | Q6 | 212480 | 12480 |
| s34(id=25 S2->S1) | sw08-p4 | Q6 | 219200 | 12480 |
| s34(id=25 S2->S1) | sw06-p5 | Q6 | 225920 | 12480 |
| s34(id=25 S2->S1) | sw04-p4 | Q6 | 232640 | 12480 |
| s34(id=25 S2->S1) | sw02-p2 | Q6 | 239360 | 12480 |
| s37(id=28 S2->S1) | S2-p0 | Q7 | 168320 | 12480 |
| s37(id=28 S2->S1) | sw08-p4 | Q7 | 176000 | 12480 |
| s37(id=28 S2->S1) | sw06-p5 | Q7 | 183680 | 12480 |
| s37(id=28 S2->S1) | sw04-p4 | Q7 | 339200 | 12480 |
| s37(id=28 S2->S1) | sw02-p2 | Q7 | 346880 | 12480 |
| s45(id=36 S2->S1) | S2-p0 | Q6 | 224960 | 12480 |
| s45(id=36 S2->S1) | sw08-p4 | Q6 | 233280 | 12480 |
| s45(id=36 S2->S1) | sw06-p5 | Q6 | 241600 | 12480 |
| s45(id=36 S2->S1) | sw04-p4 | Q6 | 249920 | 12480 |
| s45(id=36 S2->S1) | sw02-p2 | Q6 | 258240 | 12480 |
| s59(id=50 S2->S1) | S2-p0 | Q7 | 367680 | 12480 |
| s59(id=50 S2->S1) | sw08-p4 | Q7 | 375360 | 12480 |
| s59(id=50 S2->S1) | sw06-p5 | Q7 | 383360 | 12480 |
| s59(id=50 S2->S1) | sw04-p4 | Q7 | 449920 | 12480 |
| s59(id=50 S2->S1) | sw02-p2 | Q7 | 457600 | 12480 |
| s46(id=37 S3->S1) | S3-p0 | Q6 | 120320 | 12480 |
| s46(id=37 S3->S1) | sw01-p4 | Q6 | 130560 | 12480 |
| s46(id=37 S3->S1) | sw03-p5 | Q6 | 138880 | 12480 |
| s46(id=37 S3->S1) | sw05-p4 | Q6 | 147200 | 12480 |
| s46(id=37 S3->S1) | sw07-p5 | Q6 | 403840 | 12480 |
| s46(id=37 S3->S1) | sw08-p4 | Q6 | 418560 | 12480 |
| s46(id=37 S3->S1) | sw06-p5 | Q6 | 426880 | 12480 |
| s46(id=37 S3->S1) | sw04-p4 | Q6 | 435200 | 12480 |
| s46(id=37 S3->S1) | sw02-p2 | Q6 | 600000 | 12480 |
| s55(id=46 S1->S3) | S1-p0 | Q7 | 150080 | 12480 |
| s55(id=46 S1->S3) | sw02-p4 | Q7 | 158400 | 12480 |
| s55(id=46 S1->S3) | sw04-p5 | Q7 | 166720 | 12480 |
| s55(id=46 S1->S3) | sw06-p4 | Q7 | 175040 | 12480 |
| s55(id=46 S1->S3) | sw08-p5 | Q7 | 249920 | 12480 |
| s55(id=46 S1->S3) | sw07-p4 | Q7 | 262400 | 12480 |
| s55(id=46 S1->S3) | sw05-p5 | Q7 | 270720 | 12480 |
| s55(id=46 S1->S3) | sw03-p4 | Q7 | 279040 | 12480 |
| s55(id=46 S1->S3) | sw01-p2 | Q7 | 287360 | 12480 |
| s44(id=35 S2->S1) | S2-p0 | Q6 | 237440 | 12480 |
| s44(id=35 S2->S1) | sw08-p4 | Q6 | 245760 | 12480 |
| s44(id=35 S2->S1) | sw06-p5 | Q6 | 254080 | 12480 |
| s44(id=35 S2->S1) | sw04-p4 | Q6 | 262400 | 12480 |
| s44(id=35 S2->S1) | sw02-p2 | Q6 | 270720 | 12480 |
| s49(id=40 S2->S3) | S2-p0 | Q6 | 127680 | 12480 |
| s49(id=40 S2->S3) | sw08-p5 | Q6 | 136000 | 12480 |
| s49(id=40 S2->S3) | sw07-p4 | Q6 | 144320 | 12480 |
| s49(id=40 S2->S3) | sw05-p5 | Q6 | 152640 | 12480 |
| s49(id=40 S2->S3) | sw03-p4 | Q6 | 160960 | 12480 |
| s49(id=40 S2->S3) | sw01-p2 | Q6 | 169280 | 12480 |
| s51(id=42 S2->S3) | S2-p0 | Q7 | 350080 | 12480 |
| s51(id=42 S2->S3) | sw08-p5 | Q7 | 356800 | 12480 |
| s51(id=42 S2->S3) | sw07-p4 | Q7 | 363520 | 12480 |
| s51(id=42 S2->S3) | sw05-p5 | Q7 | 370240 | 12480 |
| s51(id=42 S2->S3) | sw03-p4 | Q7 | 376960 | 12480 |
| s51(id=42 S2->S3) | sw01-p2 | Q7 | 383680 | 12480 |

## Constraint check

- C1-C7, C9: OK
- window-boundary integrity (no window's psi/delta changed anywhere): OK

## GCL per egress port

### sw01-p2  (24 entries, util 18.7200 %)

```
sgs 54080 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 24320 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 22720 0x7F # 01111111   Q6
sgs 98880 0x40 # 01000000   Q6
sgs 62080 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 58560 0x80 # 10000000   Q7
sgs 24640 0xBF # 10111111   Q7
sgs 54080 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 20480 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 121280 0x80 # 10000000   Q7
sgs 62080 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p4  (18 entries, util 29.6400 %)

```
sgs 15360 0x7F # 01111111   Q6
sgs 53760 0x80 # 10000000   Q7
sgs 10880 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 8960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 50240 0x40 # 01000000   Q6
sgs 31680 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 152960 0x80 # 10000000   Q7
sgs 31680 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 152960 0x80 # 10000000   Q7
sgs 31680 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 137600 0x80 # 10000000   Q7
sgs 47040 0xBF # 10111111   Q7
```

### sw02-p2  (24 entries, util 34.3200 %)

```
sgs 24320 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 13120 0x7F # 01111111   Q6
sgs 14400 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 26880 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 33920 0x7F # 01111111   Q6
sgs 23680 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 13760 0xBF # 10111111   Q7
sgs 24320 0x7F # 01111111   Q6
sgs 120960 0x40 # 01000000   Q6
sgs 54720 0xBF # 10111111   Q7
sgs 24320 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 13120 0x7F # 01111111   Q6
sgs 53760 0xBF # 10111111   Q7
sgs 41600 0x80 # 10000000   Q7
sgs 54720 0xBF # 10111111   Q7
sgs 24320 0x7F # 01111111   Q6
sgs 96640 0x40 # 01000000   Q6
sgs 29120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p4  (29 entries, util 15.6000 %)

```
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 640 0x3F # 00111111   BE
sgs 66240 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20800 0x80 # 10000000   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 79360 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 8320 0x3F # 00111111   BE
sgs 79360 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
sgs 20800 0x80 # 10000000   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 71040 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (23 entries, util 18.7200 %)

```
sgs 45760 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 24640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 24320 0x7F # 01111111   Q6
sgs 98560 0x40 # 01000000   Q6
sgs 18880 0x7F # 01111111   Q6
sgs 59840 0xBF # 10111111   Q7
sgs 57280 0x80 # 10000000   Q7
sgs 32960 0xBF # 10111111   Q7
sgs 45760 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 38720 0xBF # 10111111   Q7
sgs 121280 0x80 # 10000000   Q7
sgs 18880 0x7F # 01111111   Q6
sgs 59840 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p5  (18 entries, util 29.6400 %)

```
sgs 23040 0x7F # 01111111   Q6
sgs 52800 0x80 # 10000000   Q7
sgs 9280 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 3520 0x3F # 00111111   BE
sgs 50240 0x40 # 01000000   Q6
sgs 24000 0xBF # 10111111   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 152960 0x80 # 10000000   Q7
sgs 24000 0xBF # 10111111   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 152960 0x80 # 10000000   Q7
sgs 24000 0xBF # 10111111   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 129920 0x80 # 10000000   Q7
sgs 47040 0xBF # 10111111   Q7
```

### sw04-p4  (23 entries, util 34.3200 %)

```
sgs 18240 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 26880 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 26880 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 40640 0x7F # 01111111   Q6
sgs 16000 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 21440 0xBF # 10111111   Q7
sgs 18240 0x7F # 01111111   Q6
sgs 120960 0x40 # 01000000   Q6
sgs 60800 0xBF # 10111111   Q7
sgs 18240 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 19200 0x7F # 01111111   Q6
sgs 47040 0xBF # 10111111   Q7
sgs 42240 0x80 # 10000000   Q7
sgs 60800 0xBF # 10111111   Q7
sgs 18240 0x7F # 01111111   Q6
sgs 102720 0x40 # 01000000   Q6
sgs 29120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (32 entries, util 15.6000 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 5120 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 2240 0x3F # 00111111   BE
sgs 67840 0x40 # 01000000   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 17600 0x80 # 10000000   Q7
sgs 15680 0x7F # 01111111   Q6
sgs 34240 0xBF # 10111111   Q7
sgs 82560 0x80 # 10000000   Q7
sgs 33280 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 5120 0x3F # 00111111   BE
sgs 82560 0x80 # 10000000   Q7
sgs 33280 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 17600 0x80 # 10000000   Q7
sgs 15680 0x7F # 01111111   Q6
sgs 34240 0xBF # 10111111   Q7
sgs 65920 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (18 entries, util 29.6400 %)

```
sgs 30720 0x7F # 01111111   Q6
sgs 51840 0x80 # 10000000   Q7
sgs 7680 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 15360 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 2880 0x3F # 00111111   BE
sgs 50240 0x40 # 01000000   Q6
sgs 16320 0xBF # 10111111   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 152960 0x80 # 10000000   Q7
sgs 16320 0xBF # 10111111   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 152960 0x80 # 10000000   Q7
sgs 16320 0xBF # 10111111   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 122240 0x80 # 10000000   Q7
sgs 47040 0xBF # 10111111   Q7
```

### sw05-p5  (21 entries, util 18.7200 %)

```
sgs 37440 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 25920 0x7F # 01111111   Q6
sgs 100160 0x40 # 01000000   Q6
sgs 24000 0x7F # 01111111   Q6
sgs 54720 0xBF # 10111111   Q7
sgs 54080 0x80 # 10000000   Q7
sgs 41280 0xBF # 10111111   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 42240 0xBF # 10111111   Q7
sgs 121280 0x80 # 10000000   Q7
sgs 24000 0x7F # 01111111   Q6
sgs 54720 0xBF # 10111111   Q7
sgs 16640 0x80 # 10000000   Q7
sgs 28800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p4  (30 entries, util 15.6000 %)

```
sgs 24960 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 1920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 3840 0x3F # 00111111   BE
sgs 69440 0x40 # 01000000   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 14400 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
sgs 85760 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 1920 0x3F # 00111111   BE
sgs 85760 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 14400 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
sgs 60800 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (21 entries, util 34.3200 %)

```
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 26240 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 26880 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 55680 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 41280 0xBF # 10111111   Q7
sgs 120960 0x40 # 01000000   Q6
sgs 16960 0x7F # 01111111   Q6
sgs 62080 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 25280 0x7F # 01111111   Q6
sgs 40320 0xBF # 10111111   Q7
sgs 42880 0x80 # 10000000   Q7
sgs 16960 0x7F # 01111111   Q6
sgs 62080 0xBF # 10111111   Q7
sgs 108800 0x40 # 01000000   Q6
sgs 29120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (23 entries, util 18.7200 %)

```
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 24320 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 27520 0x7F # 01111111   Q6
sgs 101760 0x40 # 01000000   Q6
sgs 29120 0x7F # 01111111   Q6
sgs 49600 0xBF # 10111111   Q7
sgs 50880 0x80 # 10000000   Q7
sgs 49600 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 44800 0xBF # 10111111   Q7
sgs 121280 0x80 # 10000000   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 49600 0xBF # 10111111   Q7
sgs 21760 0x80 # 10000000   Q7
sgs 28800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p5  (15 entries, util 29.6400 %)

```
sgs 38400 0x7F # 01111111   Q6
sgs 50880 0x80 # 10000000   Q7
sgs 6080 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 18560 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 2240 0x3F # 00111111   BE
sgs 50240 0x40 # 01000000   Q6
sgs 47040 0x7F # 01111111   Q6
sgs 152960 0x80 # 10000000   Q7
sgs 47040 0x7F # 01111111   Q6
sgs 152960 0x80 # 10000000   Q7
sgs 47040 0x7F # 01111111   Q6
sgs 114560 0x80 # 10000000   Q7
sgs 47040 0xBF # 10111111   Q7
```

### sw08-p2  (25 entries, util 26.5200 %)

```
sgs 33280 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 28480 0x40 # 01000000   Q6
sgs 120320 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 13120 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 149120 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 136320 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 13120 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 115840 0x3F # 00111111   BE
```

### sw08-p4  (21 entries, util 34.3200 %)

```
sgs 6080 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 25600 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 26880 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 54720 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 42880 0xBF # 10111111   Q7
sgs 120960 0x40 # 01000000   Q6
sgs 23040 0x7F # 01111111   Q6
sgs 56000 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 31360 0x7F # 01111111   Q6
sgs 33600 0xBF # 10111111   Q7
sgs 43520 0x80 # 10000000   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 56000 0xBF # 10111111   Q7
sgs 114880 0x40 # 01000000   Q6
sgs 29120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (23 entries, util 18.7200 %)

```
sgs 20800 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 24640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 29120 0xBF # 10111111   Q7
sgs 103360 0x40 # 01000000   Q6
sgs 34240 0x7F # 01111111   Q6
sgs 44480 0xBF # 10111111   Q7
sgs 47680 0x80 # 10000000   Q7
sgs 57920 0xBF # 10111111   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 48320 0xBF # 10111111   Q7
sgs 121280 0x80 # 10000000   Q7
sgs 34240 0x7F # 01111111   Q6
sgs 44480 0xBF # 10111111   Q7
sgs 26880 0x80 # 10000000   Q7
sgs 28800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

