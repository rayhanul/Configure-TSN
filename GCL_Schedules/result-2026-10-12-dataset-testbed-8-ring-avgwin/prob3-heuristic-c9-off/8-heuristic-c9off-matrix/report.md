# Reconfiguration-free admission (Problem 3)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Frozen schedule W loaded from: **result/result-2026-10-12-dataset-testbed-8-ring-avgwin/heuristic-c9-off/8-matrix-c9off**

## Admission: W (before) vs. after this run's arrivals

| | admitted | of total |
|---|---|---|
| W (base, unchanged) | 10 | 10 |
| + this run's arrivals | 23 | 40 |

Every arrival admitted here required **zero** window-boundary changes -- see the GCL-entry table below (unchanged from W by construction) and the window-boundary integrity check. No previously-admitted flow was rerouted.

## Arrivals

| id | src->dst | RS(s) size | admitted | route | queue | phi_s (ns) | e2e (ns) | rerouted to make room | reason if rejected |
|---|---|---|---|---|---|---|---|---|---|
| 14 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 8 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 16 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 11 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q6 | 0 | 162560 | - | - |
| 15 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 1 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 111040 | 79040 | - | - |
| 7 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 75200 | 203840 | - | - |
| 17 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q6 | 0 | 45760 | - | - |
| 3 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q7 | 75200 | 294080 | - | - |
| 4 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q7 | 475520 | 45760 | - | - |
| 29 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q6 | 300160 | 45760 | - | - |
| 35 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q6 | 100160 | 112320 | - | - |
| 45 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q7 | 88000 | 294080 | - | - |
| 47 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q6 | 312960 | 99520 | - | - |
| 50 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q7 | 350080 | 45760 | - | - |
| 28 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 49920 | 446080 | - | - |
| 32 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 350080 | 412480 | - | - |
| 46 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 49920 | 212480 | - | - |
| 21 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q6 | 24960 | 204160 | - | - |
| 30 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 | 49920 | 145920 | - | - |
| 43 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 26 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 157440 | 138240 | - | - |
| 31 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 170240 | 292160 | - | - |
| 44 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 48 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 123840 | 79040 | - | - |
| 22 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 150080 | 328960 | - | - |
| 23 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 12800 | 216320 | - | - |
| 25 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 212800 | 116480 | - | - |
| 27 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 225600 | 120320 | - | - |
| 34 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 36 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 38 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 41 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 49 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 37 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 40 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 42 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 24 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 33 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 39 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |

## Per-port GCL entries (should equal W exactly)

| port | W entries | after arrivals | GCL_size |
|---|---|---|---|
| sw01-p2 | 28 | 28 | 255 |
| sw01-p4 | 18 | 18 | 255 |
| sw01-p5 | 15 | 15 | 255 |
| sw02-p2 | 18 | 18 | 255 |
| sw02-p4 | 22 | 22 | 255 |
| sw02-p5 | 24 | 24 | 255 |
| sw03-p4 | 24 | 24 | 255 |
| sw03-p5 | 18 | 18 | 255 |
| sw04-p4 | 14 | 14 | 255 |
| sw04-p5 | 22 | 22 | 255 |
| sw05-p4 | 18 | 18 | 255 |
| sw05-p5 | 20 | 20 | 255 |
| sw06-p4 | 19 | 19 | 255 |
| sw06-p5 | 14 | 14 | 255 |
| sw07-p4 | 20 | 20 | 255 |
| sw07-p5 | 18 | 18 | 255 |
| sw08-p2 | 22 | 22 | 255 |
| sw08-p4 | 14 | 14 | 255 |
| sw08-p5 | 23 | 23 | 255 |

## Per-hop windows used by newly admitted flows

| flow | egress port | queue | psi (ns, unchanged) | delta (ns, unchanged) |
|---|---|---|---|---|
| s25(id=11 S3->S2) | S3-p0 | Q6 | 0 | 12480 |
| s25(id=11 S3->S2) | sw01-p4 | Q6 | 24960 | 12480 |
| s25(id=11 S3->S2) | sw03-p5 | Q6 | 100160 | 12480 |
| s25(id=11 S3->S2) | sw05-p4 | Q6 | 116800 | 12480 |
| s25(id=11 S3->S2) | sw07-p5 | Q6 | 133440 | 12480 |
| s25(id=11 S3->S2) | sw08-p2 | Q6 | 150080 | 12480 |
| s20(id=1 S2->S1) | S2-p0 | Q6 | 111040 | 12480 |
| s20(id=1 S2->S1) | sw08-p4 | Q6 | 127680 | 12480 |
| s20(id=1 S2->S1) | sw06-p5 | Q6 | 144320 | 12480 |
| s20(id=1 S2->S1) | sw04-p4 | Q6 | 160960 | 12480 |
| s20(id=1 S2->S1) | sw02-p2 | Q6 | 177600 | 12480 |
| s23(id=7 S2->S3) | S2-p0 | Q7 | 75200 | 12480 |
| s23(id=7 S2->S3) | sw08-p5 | Q7 | 150080 | 12480 |
| s23(id=7 S2->S3) | sw07-p4 | Q7 | 166720 | 12480 |
| s23(id=7 S2->S3) | sw05-p5 | Q7 | 183360 | 12480 |
| s23(id=7 S2->S3) | sw03-p4 | Q7 | 249920 | 12480 |
| s23(id=7 S2->S3) | sw01-p2 | Q7 | 266560 | 12480 |
| s29(id=17 S1->S3) | S1-p0 | Q6 | 0 | 12480 |
| s29(id=17 S1->S3) | sw02-p5 | Q6 | 16640 | 12480 |
| s29(id=17 S1->S3) | sw01-p2 | Q6 | 33280 | 12480 |
| s21(id=3 S3->S1) | S3-p0 | Q7 | 75200 | 12480 |
| s21(id=3 S3->S1) | sw01-p5 | Q7 | 91840 | 12480 |
| s21(id=3 S3->S1) | sw02-p2 | Q7 | 356800 | 12480 |
| s22(id=4 S1->S3) | S1-p0 | Q7 | 475520 | 12480 |
| s22(id=4 S1->S3) | sw02-p5 | Q7 | 492160 | 12480 |
| s22(id=4 S1->S3) | sw01-p2 | Q7 | 508800 | 12480 |
| s38(id=29 S3->S1) | S3-p0 | Q6 | 300160 | 12480 |
| s38(id=29 S3->S1) | sw01-p5 | Q6 | 316800 | 12480 |
| s38(id=29 S3->S1) | sw02-p2 | Q6 | 333440 | 12480 |
| s44(id=35 S1->S3) | S1-p0 | Q6 | 100160 | 12480 |
| s44(id=35 S1->S3) | sw02-p5 | Q6 | 116800 | 12480 |
| s44(id=35 S1->S3) | sw01-p2 | Q6 | 200000 | 12480 |
| s54(id=45 S3->S1) | S3-p0 | Q7 | 88000 | 12480 |
| s54(id=45 S3->S1) | sw01-p5 | Q7 | 352960 | 12480 |
| s54(id=45 S3->S1) | sw02-p2 | Q7 | 369600 | 12480 |
| s56(id=47 S3->S1) | S3-p0 | Q6 | 312960 | 12480 |
| s56(id=47 S3->S1) | sw01-p5 | Q6 | 329600 | 12480 |
| s56(id=47 S3->S1) | sw02-p2 | Q6 | 400000 | 12480 |
| s59(id=50 S3->S1) | S3-p0 | Q7 | 350080 | 12480 |
| s59(id=50 S3->S1) | sw01-p5 | Q7 | 366720 | 12480 |
| s59(id=50 S3->S1) | sw02-p2 | Q7 | 383360 | 12480 |
| s37(id=28 S2->S1) | S2-p0 | Q7 | 49920 | 12480 |
| s37(id=28 S2->S1) | sw08-p4 | Q7 | 260800 | 12480 |
| s37(id=28 S2->S1) | sw06-p5 | Q7 | 277440 | 12480 |
| s37(id=28 S2->S1) | sw04-p4 | Q7 | 466880 | 12480 |
| s37(id=28 S2->S1) | sw02-p2 | Q7 | 483520 | 12480 |
| s41(id=32 S2->S1) | S2-p0 | Q7 | 350080 | 12480 |
| s41(id=32 S2->S1) | sw08-p4 | Q7 | 366720 | 12480 |
| s41(id=32 S2->S1) | sw06-p5 | Q7 | 649920 | 12480 |
| s41(id=32 S2->S1) | sw04-p4 | Q7 | 666560 | 12480 |
| s41(id=32 S2->S1) | sw02-p2 | Q7 | 750080 | 12480 |
| s55(id=46 S1->S2) | S1-p0 | Q7 | 49920 | 12480 |
| s55(id=46 S1->S2) | sw02-p4 | Q7 | 150080 | 12480 |
| s55(id=46 S1->S2) | sw04-p5 | Q7 | 166720 | 12480 |
| s55(id=46 S1->S2) | sw06-p4 | Q7 | 183360 | 12480 |
| s55(id=46 S1->S2) | sw08-p2 | Q7 | 249920 | 12480 |
| s30(id=21 S3->S2) | S3-p0 | Q6 | 24960 | 12480 |
| s30(id=21 S3->S2) | sw01-p4 | Q6 | 100160 | 12480 |
| s30(id=21 S3->S2) | sw03-p5 | Q6 | 116800 | 12480 |
| s30(id=21 S3->S2) | sw05-p4 | Q6 | 133440 | 12480 |
| s30(id=21 S3->S2) | sw07-p5 | Q6 | 200000 | 12480 |
| s30(id=21 S3->S2) | sw08-p2 | Q6 | 216640 | 12480 |
| s39(id=30 S3->S2) | S3-p0 | Q7 | 49920 | 12480 |
| s39(id=30 S3->S2) | sw01-p4 | Q7 | 66560 | 12480 |
| s39(id=30 S3->S2) | sw03-p5 | Q7 | 83200 | 12480 |
| s39(id=30 S3->S2) | sw05-p4 | Q7 | 150080 | 12480 |
| s39(id=30 S3->S2) | sw07-p5 | Q7 | 166720 | 12480 |
| s39(id=30 S3->S2) | sw08-p2 | Q7 | 183360 | 12480 |
| s35(id=26 S1->S2) | S1-p0 | Q7 | 157440 | 12480 |
| s35(id=26 S1->S2) | sw02-p4 | Q7 | 174080 | 12480 |
| s35(id=26 S1->S2) | sw04-p5 | Q7 | 249920 | 12480 |
| s35(id=26 S1->S2) | sw06-p4 | Q7 | 266560 | 12480 |
| s35(id=26 S1->S2) | sw08-p2 | Q7 | 283200 | 12480 |
| s40(id=31 S1->S2) | S1-p0 | Q7 | 170240 | 12480 |
| s40(id=31 S1->S2) | sw02-p4 | Q7 | 350080 | 12480 |
| s40(id=31 S1->S2) | sw04-p5 | Q7 | 366720 | 12480 |
| s40(id=31 S1->S2) | sw06-p4 | Q7 | 383360 | 12480 |
| s40(id=31 S1->S2) | sw08-p2 | Q7 | 449920 | 12480 |
| s57(id=48 S2->S1) | S2-p0 | Q6 | 123840 | 12480 |
| s57(id=48 S2->S1) | sw08-p4 | Q6 | 140480 | 12480 |
| s57(id=48 S2->S1) | sw06-p5 | Q6 | 157120 | 12480 |
| s57(id=48 S2->S1) | sw04-p4 | Q6 | 173760 | 12480 |
| s57(id=48 S2->S1) | sw02-p2 | Q6 | 190400 | 12480 |
| s31(id=22 S2->S3) | S2-p0 | Q7 | 150080 | 12480 |
| s31(id=22 S2->S3) | sw08-p5 | Q7 | 166720 | 12480 |
| s31(id=22 S2->S3) | sw07-p4 | Q7 | 183360 | 12480 |
| s31(id=22 S2->S3) | sw05-p5 | Q7 | 350080 | 12480 |
| s31(id=22 S2->S3) | sw03-p4 | Q7 | 449920 | 12480 |
| s31(id=22 S2->S3) | sw01-p2 | Q7 | 466560 | 12480 |
| s32(id=23 S2->S3) | S2-p0 | Q6 | 12800 | 12480 |
| s32(id=23 S2->S3) | sw08-p5 | Q6 | 29440 | 12480 |
| s32(id=23 S2->S3) | sw07-p4 | Q6 | 110400 | 12480 |
| s32(id=23 S2->S3) | sw05-p5 | Q6 | 127040 | 12480 |
| s32(id=23 S2->S3) | sw03-p4 | Q6 | 200000 | 12480 |
| s32(id=23 S2->S3) | sw01-p2 | Q6 | 216640 | 12480 |
| s34(id=25 S2->S3) | S2-p0 | Q6 | 212800 | 12480 |
| s34(id=25 S2->S3) | sw08-p5 | Q6 | 229440 | 12480 |
| s34(id=25 S2->S3) | sw07-p4 | Q6 | 246080 | 12480 |
| s34(id=25 S2->S3) | sw05-p5 | Q6 | 262720 | 12480 |
| s34(id=25 S2->S3) | sw03-p4 | Q6 | 279360 | 12480 |
| s34(id=25 S2->S3) | sw01-p2 | Q6 | 296000 | 12480 |
| s36(id=27 S2->S3) | S2-p0 | Q6 | 225600 | 12480 |
| s36(id=27 S2->S3) | sw08-p5 | Q6 | 242240 | 12480 |
| s36(id=27 S2->S3) | sw07-p4 | Q6 | 258880 | 12480 |
| s36(id=27 S2->S3) | sw05-p5 | Q6 | 275520 | 12480 |
| s36(id=27 S2->S3) | sw03-p4 | Q6 | 292160 | 12480 |
| s36(id=27 S2->S3) | sw01-p2 | Q6 | 308800 | 12480 |

## Constraint check

- C1-C7, C9: OK
- window-boundary integrity (no window's psi/delta changed anywhere): OK

## GCL per egress port

### sw01-p2  (28 entries, util 39.0000 %)

```
sgs 45760 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 50240 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 45760 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 112640 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 45760 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 99840 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 45760 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 66880 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p4  (18 entries, util 6.2400 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p5  (15 entries, util 15.6000 %)

```
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 227200 0x80 # 10000000   Q7
sgs 43840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 223040 0x80 # 10000000   Q7
sgs 23040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (18 entries, util 28.0800 %)

```
sgs 45760 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 248320 0x40 # 01000000   Q6
sgs 43200 0xBF # 10111111   Q7
sgs 45760 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 16960 0xBF # 10111111   Q7
sgs 8320 0x3F # 00111111   BE
sgs 202560 0x40 # 01000000   Q6
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p4  (22 entries, util 14.0400 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 4160 0x3F # 00111111   BE
sgs 75200 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 4160 0x3F # 00111111   BE
sgs 75200 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 4160 0x3F # 00111111   BE
sgs 75200 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 4160 0x3F # 00111111   BE
sgs 21120 0x40 # 01000000   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p5  (24 entries, util 17.1600 %)

```
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 8320 0x3F # 00111111   BE
sgs 29440 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12160 0x3F # 00111111   BE
sgs 36160 0x40 # 01000000   Q6
sgs 9920 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 111040 0x80 # 10000000   Q7
sgs 9920 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 8320 0x3F # 00111111   BE
sgs 29440 0xBF # 10111111   Q7
sgs 60800 0x80 # 10000000   Q7
sgs 9920 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 81920 0x80 # 10000000   Q7
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (24 entries, util 21.8400 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 21120 0xBF # 10111111   Q7
sgs 28800 0x7F # 01111111   Q6
sgs 14720 0x80 # 10000000   Q7
sgs 6400 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 77120 0x40 # 01000000   Q6
sgs 6400 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 77120 0x40 # 01000000   Q6
sgs 6400 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 21120 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p5  (18 entries, util 6.2400 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p4  (14 entries, util 12.4800 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 37760 0xBF # 10111111   Q7
sgs 206400 0x40 # 01000000   Q6
sgs 6080 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 37760 0xBF # 10111111   Q7
sgs 118720 0x40 # 01000000   Q6
sgs 43520 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (22 entries, util 14.0400 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 20800 0xBF # 10111111   Q7
sgs 75200 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 20800 0xBF # 10111111   Q7
sgs 75200 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 20800 0xBF # 10111111   Q7
sgs 75200 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 20800 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 16960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (18 entries, util 6.2400 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p5  (20 entries, util 21.8400 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 37760 0xBF # 10111111   Q7
sgs 12160 0x3F # 00111111   BE
sgs 14720 0x80 # 10000000   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 77120 0x40 # 01000000   Q6
sgs 23040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 77120 0x40 # 01000000   Q6
sgs 23040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 27200 0x40 # 01000000   Q6
sgs 23040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p4  (19 entries, util 14.0400 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 37440 0xBF # 10111111   Q7
sgs 75200 0x40 # 01000000   Q6
sgs 37440 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 37440 0xBF # 10111111   Q7
sgs 75200 0x40 # 01000000   Q6
sgs 37440 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 37440 0xBF # 10111111   Q7
sgs 75200 0x40 # 01000000   Q6
sgs 37440 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 37440 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (14 entries, util 12.4800 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 21120 0xBF # 10111111   Q7
sgs 206400 0x40 # 01000000   Q6
sgs 22720 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 21120 0xBF # 10111111   Q7
sgs 135360 0x40 # 01000000   Q6
sgs 43520 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (20 entries, util 21.8400 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 45760 0xBF # 10111111   Q7
sgs 14720 0x80 # 10000000   Q7
sgs 39680 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 77120 0x40 # 01000000   Q6
sgs 39680 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 77120 0x40 # 01000000   Q6
sgs 39680 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 43840 0x40 # 01000000   Q6
sgs 23040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p5  (18 entries, util 6.2400 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p2  (22 entries, util 20.2800 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 3840 0x3F # 00111111   BE
sgs 75200 0x40 # 01000000   Q6
sgs 20800 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 3840 0x3F # 00111111   BE
sgs 75200 0x40 # 01000000   Q6
sgs 20800 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 3840 0x3F # 00111111   BE
sgs 75200 0x40 # 01000000   Q6
sgs 20800 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 3840 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 33600 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p4  (14 entries, util 12.4800 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 4480 0x3F # 00111111   BE
sgs 206400 0x40 # 01000000   Q6
sgs 39360 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 4480 0x3F # 00111111   BE
sgs 152000 0x40 # 01000000   Q6
sgs 43520 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (23 entries, util 21.8400 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 14720 0x80 # 10000000   Q7
sgs 6400 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 77120 0x40 # 01000000   Q6
sgs 6400 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 77120 0x40 # 01000000   Q6
sgs 6400 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 60480 0x40 # 01000000   Q6
sgs 23040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

