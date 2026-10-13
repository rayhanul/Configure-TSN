# Reconfiguration-free admission (Problem 3)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Frozen schedule W loaded from: **result/result-2026-10-13-dataset-testbed-11-tree-avgwin/heuristic-c9-on/11-matrix-c9on**

## Admission: W (before) vs. after this run's arrivals

| | admitted | of total |
|---|---|---|
| W (base, unchanged) | 10 | 10 |
| + this run's arrivals | 17 | 40 |

Every arrival admitted here required **zero** window-boundary changes -- see the GCL-entry table below (unchanged from W by construction) and the window-boundary integrity check. No previously-admitted flow was rerouted.

## Arrivals

| id | src->dst | RS(s) size | admitted | route | queue | phi_s (ns) | e2e (ns) | rerouted to make room | reason if rejected |
|---|---|---|---|---|---|---|---|---|---|
| 6 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 11 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 14 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 16 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q7 | 62400 | 325120 | - | - |
| 4 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 12 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 17 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q6 | 62400 | 63360 | - | - |
| 13 | S1->S3 | - | yes | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 150080 | 66240 | - | - |
| 19 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q6 | 87360 | 132800 | - | - |
| 15 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 49920 | 46080 | - | - |
| 23 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 150080 | 39360 | - | - |
| 25 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 162560 | 200000 | - | - |
| 27 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q6 | 74880 | 64000 | - | - |
| 28 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 350080 | 49920 | - | - |
| 36 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 212480 | 45760 | - | - |
| 49 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q6 | 87360 | 64000 | - | - |
| 50 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 362560 | 107520 | - | - |
| 48 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q6 | 99840 | 64320 | - | - |
| 37 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q6 | 112320 | 158720 | - | - |
| 46 | S1->S3 | - | yes | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 162560 | 79040 | - | - |
| 33 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 34 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 35 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 238080 | 45760 | - | - |
| 41 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 44 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 22 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 40 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 42 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 43 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 39 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q7 | 237440 | 249920 | - | - |
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
| sw01-p2 | 11 | 11 | 255 |
| sw01-p4 | 15 | 15 | 255 |
| sw02-p2 | 26 | 26 | 255 |
| sw02-p4 | 24 | 24 | 255 |
| sw03-p4 | 10 | 10 | 255 |
| sw03-p5 | 15 | 15 | 255 |
| sw04-p4 | 24 | 24 | 255 |
| sw04-p5 | 24 | 24 | 255 |
| sw05-p4 | 15 | 15 | 255 |
| sw05-p5 | 10 | 10 | 255 |
| sw06-p4 | 24 | 24 | 255 |
| sw06-p5 | 24 | 24 | 255 |
| sw07-p4 | 10 | 10 | 255 |
| sw07-p5 | 15 | 15 | 255 |
| sw08-p2 | 25 | 25 | 255 |
| sw08-p4 | 23 | 23 | 255 |
| sw08-p5 | 10 | 10 | 255 |

## Per-hop windows used by newly admitted flows

| flow | egress port | queue | psi (ns, unchanged) | delta (ns, unchanged) |
|---|---|---|---|---|
| s27(id=16 S3->S1) | S3-p0 | Q7 | 62400 | 12480 |
| s27(id=16 S3->S1) | sw01-p4 | Q7 | 160320 | 12480 |
| s27(id=16 S3->S1) | sw03-p5 | Q7 | 168640 | 12480 |
| s27(id=16 S3->S1) | sw05-p4 | Q7 | 176960 | 12480 |
| s27(id=16 S3->S1) | sw07-p5 | Q7 | 185280 | 12480 |
| s27(id=16 S3->S1) | sw08-p4 | Q7 | 350080 | 12480 |
| s27(id=16 S3->S1) | sw06-p5 | Q7 | 358400 | 12480 |
| s27(id=16 S3->S1) | sw04-p4 | Q7 | 366720 | 12480 |
| s27(id=16 S3->S1) | sw02-p2 | Q7 | 375040 | 12480 |
| s28(id=17 S1->S2) | S1-p0 | Q6 | 62400 | 12480 |
| s28(id=17 S1->S2) | sw02-p4 | Q6 | 70720 | 12480 |
| s28(id=17 S1->S2) | sw04-p5 | Q6 | 79040 | 12480 |
| s28(id=17 S1->S2) | sw06-p4 | Q6 | 105600 | 12480 |
| s28(id=17 S1->S2) | sw08-p2 | Q6 | 113280 | 12480 |
| s24(id=13 S1->S3) | S1-p0 | Q7 | 150080 | 12480 |
| s24(id=13 S1->S3) | sw02-p4 | Q7 | 156800 | 12480 |
| s24(id=13 S1->S3) | sw04-p5 | Q7 | 163520 | 12480 |
| s24(id=13 S1->S3) | sw06-p4 | Q7 | 170240 | 12480 |
| s24(id=13 S1->S3) | sw08-p5 | Q7 | 176960 | 12480 |
| s24(id=13 S1->S3) | sw07-p4 | Q7 | 183680 | 12480 |
| s24(id=13 S1->S3) | sw05-p5 | Q7 | 190400 | 12480 |
| s24(id=13 S1->S3) | sw03-p4 | Q7 | 197120 | 12480 |
| s24(id=13 S1->S3) | sw01-p2 | Q7 | 203840 | 12480 |
| s29(id=19 S3->S1) | S3-p0 | Q6 | 87360 | 12480 |
| s29(id=19 S3->S1) | sw01-p4 | Q6 | 95040 | 12480 |
| s29(id=19 S3->S1) | sw03-p5 | Q6 | 102720 | 12480 |
| s29(id=19 S3->S1) | sw05-p4 | Q6 | 110400 | 12480 |
| s29(id=19 S3->S1) | sw07-p5 | Q6 | 118080 | 12480 |
| s29(id=19 S3->S1) | sw08-p4 | Q6 | 125760 | 12480 |
| s29(id=19 S3->S1) | sw06-p5 | Q6 | 133440 | 12480 |
| s29(id=19 S3->S1) | sw04-p4 | Q6 | 200000 | 12480 |
| s29(id=19 S3->S1) | sw02-p2 | Q6 | 207680 | 12480 |
| s26(id=15 S2->S3) | S2-p0 | Q7 | 49920 | 12480 |
| s26(id=15 S2->S3) | sw08-p5 | Q7 | 56640 | 12480 |
| s26(id=15 S2->S3) | sw07-p4 | Q7 | 63360 | 12480 |
| s26(id=15 S2->S3) | sw05-p5 | Q7 | 70080 | 12480 |
| s26(id=15 S2->S3) | sw03-p4 | Q7 | 76800 | 12480 |
| s26(id=15 S2->S3) | sw01-p2 | Q7 | 83520 | 12480 |
| s32(id=23 S2->S1) | S2-p0 | Q7 | 150080 | 12480 |
| s32(id=23 S2->S1) | sw08-p4 | Q7 | 156800 | 12480 |
| s32(id=23 S2->S1) | sw06-p5 | Q7 | 163520 | 12480 |
| s32(id=23 S2->S1) | sw04-p4 | Q7 | 170240 | 12480 |
| s32(id=23 S2->S1) | sw02-p2 | Q7 | 176960 | 12480 |
| s34(id=25 S2->S1) | S2-p0 | Q7 | 162560 | 12480 |
| s34(id=25 S2->S1) | sw08-p4 | Q7 | 169280 | 12480 |
| s34(id=25 S2->S1) | sw06-p5 | Q7 | 176000 | 12480 |
| s34(id=25 S2->S1) | sw04-p4 | Q7 | 182720 | 12480 |
| s34(id=25 S2->S1) | sw02-p2 | Q7 | 350080 | 12480 |
| s36(id=27 S1->S2) | S1-p0 | Q6 | 74880 | 12480 |
| s36(id=27 S1->S2) | sw02-p4 | Q6 | 83200 | 12480 |
| s36(id=27 S1->S2) | sw04-p5 | Q6 | 109440 | 12480 |
| s36(id=27 S1->S2) | sw06-p4 | Q6 | 118080 | 12480 |
| s36(id=27 S1->S2) | sw08-p2 | Q6 | 126400 | 12480 |
| s37(id=28 S2->S1) | S2-p0 | Q7 | 350080 | 12480 |
| s37(id=28 S2->S1) | sw08-p4 | Q7 | 362560 | 12480 |
| s37(id=28 S2->S1) | sw06-p5 | Q7 | 370880 | 12480 |
| s37(id=28 S2->S1) | sw04-p4 | Q7 | 379200 | 12480 |
| s37(id=28 S2->S1) | sw02-p2 | Q7 | 387520 | 12480 |
| s45(id=36 S2->S1) | S2-p0 | Q6 | 212480 | 12480 |
| s45(id=36 S2->S1) | sw08-p4 | Q6 | 220800 | 12480 |
| s45(id=36 S2->S1) | sw06-p5 | Q6 | 229120 | 12480 |
| s45(id=36 S2->S1) | sw04-p4 | Q6 | 237440 | 12480 |
| s45(id=36 S2->S1) | sw02-p2 | Q6 | 245760 | 12480 |
| s58(id=49 S1->S2) | S1-p0 | Q6 | 87360 | 12480 |
| s58(id=49 S1->S2) | sw02-p4 | Q6 | 105920 | 12480 |
| s58(id=49 S1->S2) | sw04-p5 | Q6 | 121920 | 12480 |
| s58(id=49 S1->S2) | sw06-p4 | Q6 | 130560 | 12480 |
| s58(id=49 S1->S2) | sw08-p2 | Q6 | 138880 | 12480 |
| s59(id=50 S2->S1) | S2-p0 | Q7 | 362560 | 12480 |
| s59(id=50 S2->S1) | sw08-p4 | Q7 | 375040 | 12480 |
| s59(id=50 S2->S1) | sw06-p5 | Q7 | 383360 | 12480 |
| s59(id=50 S2->S1) | sw04-p4 | Q7 | 449920 | 12480 |
| s59(id=50 S2->S1) | sw02-p2 | Q7 | 457600 | 12480 |
| s57(id=48 S3->S2) | S3-p0 | Q6 | 99840 | 12480 |
| s57(id=48 S3->S2) | sw01-p4 | Q6 | 108160 | 12480 |
| s57(id=48 S3->S2) | sw03-p5 | Q6 | 116480 | 12480 |
| s57(id=48 S3->S2) | sw05-p4 | Q6 | 124800 | 12480 |
| s57(id=48 S3->S2) | sw07-p5 | Q6 | 143360 | 12480 |
| s57(id=48 S3->S2) | sw08-p2 | Q6 | 151680 | 12480 |
| s46(id=37 S3->S1) | S3-p0 | Q6 | 112320 | 12480 |
| s46(id=37 S3->S1) | sw01-p4 | Q6 | 120640 | 12480 |
| s46(id=37 S3->S1) | sw03-p5 | Q6 | 128960 | 12480 |
| s46(id=37 S3->S1) | sw05-p4 | Q6 | 147840 | 12480 |
| s46(id=37 S3->S1) | sw07-p5 | Q6 | 225280 | 12480 |
| s46(id=37 S3->S1) | sw08-p4 | Q6 | 233600 | 12480 |
| s46(id=37 S3->S1) | sw06-p5 | Q6 | 241920 | 12480 |
| s46(id=37 S3->S1) | sw04-p4 | Q6 | 250240 | 12480 |
| s46(id=37 S3->S1) | sw02-p2 | Q6 | 258560 | 12480 |
| s55(id=46 S1->S3) | S1-p0 | Q7 | 162560 | 12480 |
| s55(id=46 S1->S3) | sw02-p4 | Q7 | 170880 | 12480 |
| s55(id=46 S1->S3) | sw04-p5 | Q7 | 179200 | 12480 |
| s55(id=46 S1->S3) | sw06-p4 | Q7 | 187520 | 12480 |
| s55(id=46 S1->S3) | sw08-p5 | Q7 | 195840 | 12480 |
| s55(id=46 S1->S3) | sw07-p4 | Q7 | 204160 | 12480 |
| s55(id=46 S1->S3) | sw05-p5 | Q7 | 212480 | 12480 |
| s55(id=46 S1->S3) | sw03-p4 | Q7 | 220800 | 12480 |
| s55(id=46 S1->S3) | sw01-p2 | Q7 | 229120 | 12480 |
| s44(id=35 S2->S1) | S2-p0 | Q6 | 238080 | 12480 |
| s44(id=35 S2->S1) | sw08-p4 | Q6 | 246400 | 12480 |
| s44(id=35 S2->S1) | sw06-p5 | Q6 | 254720 | 12480 |
| s44(id=35 S2->S1) | sw04-p4 | Q6 | 263040 | 12480 |
| s44(id=35 S2->S1) | sw02-p2 | Q6 | 271360 | 12480 |
| s48(id=39 S3->S1) | S3-p0 | Q7 | 237440 | 12480 |
| s48(id=39 S3->S1) | sw01-p4 | Q7 | 247680 | 12480 |
| s48(id=39 S3->S1) | sw03-p5 | Q7 | 256000 | 12480 |
| s48(id=39 S3->S1) | sw05-p4 | Q7 | 264320 | 12480 |
| s48(id=39 S3->S1) | sw07-p5 | Q7 | 383360 | 12480 |
| s48(id=39 S3->S1) | sw08-p4 | Q7 | 449920 | 12480 |
| s48(id=39 S3->S1) | sw06-p5 | Q7 | 458240 | 12480 |
| s48(id=39 S3->S1) | sw04-p4 | Q7 | 466560 | 12480 |
| s48(id=39 S3->S1) | sw02-p2 | Q7 | 474880 | 12480 |

## Constraint check

- C1-C7, C9: OK
- window-boundary integrity (no window's psi/delta changed anywhere): OK

## GCL per egress port

### sw01-p2  (11 entries, util 6.2400 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 3840 0x3F # 00111111   BE
sgs 433600 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p4  (15 entries, util 28.0800 %)

```
sgs 15360 0x7F # 01111111   Q6
sgs 53760 0x80 # 10000000   Q7
sgs 10880 0x3F # 00111111   BE
sgs 80320 0x40 # 01000000   Q6
sgs 39680 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 144960 0x80 # 10000000   Q7
sgs 39680 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 144960 0x80 # 10000000   Q7
sgs 39680 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 129600 0x80 # 10000000   Q7
sgs 5120 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (26 entries, util 31.2000 %)

```
sgs 24320 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 13120 0x7F # 01111111   Q6
sgs 14400 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 23360 0xBF # 10111111   Q7
sgs 3520 0x3F # 00111111   BE
sgs 31680 0x80 # 10000000   Q7
sgs 14720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 24320 0x7F # 01111111   Q6
sgs 111040 0x40 # 01000000   Q6
sgs 14720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 24320 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 13120 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 3520 0x3F # 00111111   BE
sgs 31680 0x80 # 10000000   Q7
sgs 14720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 24320 0x7F # 01111111   Q6
sgs 86720 0x40 # 01000000   Q6
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p4  (24 entries, util 21.8400 %)

```
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 72320 0x40 # 01000000   Q6
sgs 19520 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 8320 0x3F # 00111111   BE
sgs 122240 0x80 # 10000000   Q7
sgs 19520 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 72320 0x40 # 01000000   Q6
sgs 19520 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 8320 0x3F # 00111111   BE
sgs 113920 0x80 # 10000000   Q7
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (10 entries, util 6.2400 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 45760 0xBF # 10111111   Q7
sgs 441920 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p5  (15 entries, util 28.0800 %)

```
sgs 23040 0x7F # 01111111   Q6
sgs 52800 0x80 # 10000000   Q7
sgs 9280 0x3F # 00111111   BE
sgs 82880 0x40 # 01000000   Q6
sgs 32000 0xBF # 10111111   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 144960 0x80 # 10000000   Q7
sgs 32000 0xBF # 10111111   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 144960 0x80 # 10000000   Q7
sgs 32000 0xBF # 10111111   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 121920 0x80 # 10000000   Q7
sgs 5120 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p4  (24 entries, util 31.2000 %)

```
sgs 18240 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 19200 0x7F # 01111111   Q6
sgs 7680 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 26880 0xBF # 10111111   Q7
sgs 32320 0x80 # 10000000   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 18240 0x7F # 01111111   Q6
sgs 111040 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 18240 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 19200 0x7F # 01111111   Q6
sgs 47040 0xBF # 10111111   Q7
sgs 32320 0x80 # 10000000   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 18240 0x7F # 01111111   Q6
sgs 92800 0x40 # 01000000   Q6
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (24 entries, util 21.8400 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 72320 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 122240 0x80 # 10000000   Q7
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 72320 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 105600 0x80 # 10000000   Q7
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (15 entries, util 28.0800 %)

```
sgs 30720 0x7F # 01111111   Q6
sgs 51840 0x80 # 10000000   Q7
sgs 7680 0x3F # 00111111   BE
sgs 85440 0x40 # 01000000   Q6
sgs 24320 0xBF # 10111111   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 144960 0x80 # 10000000   Q7
sgs 24320 0xBF # 10111111   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 144960 0x80 # 10000000   Q7
sgs 24320 0xBF # 10111111   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 114240 0x80 # 10000000   Q7
sgs 5120 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p5  (10 entries, util 6.2400 %)

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

### sw06-p4  (24 entries, util 21.8400 %)

```
sgs 24960 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 72320 0x40 # 01000000   Q6
sgs 2880 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 122240 0x80 # 10000000   Q7
sgs 2880 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 72320 0x40 # 01000000   Q6
sgs 2880 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 97280 0x80 # 10000000   Q7
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (24 entries, util 31.2000 %)

```
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 25280 0x7F # 01111111   Q6
sgs 960 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 26880 0xBF # 10111111   Q7
sgs 32960 0x80 # 10000000   Q7
sgs 26880 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 12160 0x3F # 00111111   BE
sgs 111040 0x40 # 01000000   Q6
sgs 26880 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 25280 0x7F # 01111111   Q6
sgs 40320 0xBF # 10111111   Q7
sgs 32960 0x80 # 10000000   Q7
sgs 26880 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 12160 0x3F # 00111111   BE
sgs 98880 0x40 # 01000000   Q6
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (10 entries, util 6.2400 %)

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

### sw07-p5  (15 entries, util 28.0800 %)

```
sgs 38400 0x7F # 01111111   Q6
sgs 50880 0x80 # 10000000   Q7
sgs 6080 0x3F # 00111111   BE
sgs 88000 0x40 # 01000000   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 38400 0x7F # 01111111   Q6
sgs 144960 0x80 # 10000000   Q7
sgs 16640 0xBF # 10111111   Q7
sgs 38400 0x7F # 01111111   Q6
sgs 144960 0x80 # 10000000   Q7
sgs 16640 0xBF # 10111111   Q7
sgs 38400 0x7F # 01111111   Q6
sgs 106560 0x80 # 10000000   Q7
sgs 5120 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p2  (25 entries, util 34.3200 %)

```
sgs 33280 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 116160 0x40 # 01000000   Q6
sgs 32640 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 13120 0x3F # 00111111   BE
sgs 13440 0x80 # 10000000   Q7
sgs 148160 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 36800 0x40 # 01000000   Q6
sgs 112000 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 13120 0x3F # 00111111   BE
sgs 13440 0x80 # 10000000   Q7
sgs 114880 0x3F # 00111111   BE
```

### sw08-p4  (23 entries, util 31.2000 %)

```
sgs 6080 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 25600 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 26880 0xBF # 10111111   Q7
sgs 33600 0x80 # 10000000   Q7
sgs 32960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 6080 0x3F # 00111111   BE
sgs 111040 0x40 # 01000000   Q6
sgs 32960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 6080 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 31360 0x7F # 01111111   Q6
sgs 33600 0xBF # 10111111   Q7
sgs 33600 0x80 # 10000000   Q7
sgs 32960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 6080 0x3F # 00111111   BE
sgs 104960 0x40 # 01000000   Q6
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (10 entries, util 6.2400 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 20800 0xBF # 10111111   Q7
sgs 466880 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

