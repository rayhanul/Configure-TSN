# Reconfiguration-free admission (Problem 3)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Frozen schedule W loaded from: **result/result-2026-10-12-dataset-testbed-8-ring-avgwin/rl-c9-off/8-matrix-c9off**

## Admission: W (before) vs. after this run's arrivals

| | admitted | of total |
|---|---|---|
| W (base, unchanged) | 10 | 10 |
| + this run's arrivals | 24 | 40 |

Every arrival admitted here required **zero** window-boundary changes -- see the GCL-entry table below (unchanged from W by construction) and the window-boundary integrity check. No previously-admitted flow was rerouted.

## Arrivals

| id | src->dst | RS(s) size | admitted | route | queue | phi_s (ns) | e2e (ns) | rerouted to make room | reason if rejected |
|---|---|---|---|---|---|---|---|---|---|
| 14 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 8 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 0 | 79040 | - | - |
| 16 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 11 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q6 | 24960 | 107200 | - | - |
| 15 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q7 | 0 | 45760 | - | - |
| 1 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 24960 | 109760 | - | - |
| 7 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 75200 | 203840 | - | - |
| 17 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q6 | 262720 | 166400 | - | - |
| 3 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q6 | 49920 | 45760 | - | - |
| 4 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q6 | 100160 | 76160 | - | - |
| 29 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q6 | 133120 | 96000 | - | - |
| 35 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q6 | 112960 | 116160 | - | - |
| 45 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q6 | 333120 | 96000 | - | - |
| 47 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q6 | 533120 | 96000 | - | - |
| 50 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q7 | 75200 | 72320 | - | - |
| 28 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 87680 | 79040 | - | - |
| 32 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 100480 | 79040 | - | - |
| 46 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q6 | 250240 | 79040 | - | - |
| 21 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 | 87680 | 308160 | - | - |
| 30 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 | 240640 | 221760 | - | - |
| 43 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q7 | 114560 | 83840 | - | - |
| 26 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 49920 | 212480 | - | - |
| 31 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 44 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 48 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 150080 | 108480 | - | - |
| 22 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 212800 | 95680 | - | - |
| 23 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 225600 | 127360 | - | - |
| 25 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 162560 | 316480 | - | - |
| 27 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
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
| sw01-p2 | 27 | 27 | 255 |
| sw01-p4 | 12 | 12 | 255 |
| sw01-p5 | 21 | 21 | 255 |
| sw02-p2 | 28 | 28 | 255 |
| sw02-p4 | 24 | 24 | 255 |
| sw02-p5 | 19 | 19 | 255 |
| sw03-p4 | 22 | 22 | 255 |
| sw03-p5 | 14 | 14 | 255 |
| sw04-p4 | 15 | 15 | 255 |
| sw04-p5 | 21 | 21 | 255 |
| sw05-p4 | 14 | 14 | 255 |
| sw05-p5 | 19 | 19 | 255 |
| sw06-p4 | 21 | 21 | 255 |
| sw06-p5 | 15 | 15 | 255 |
| sw07-p4 | 19 | 19 | 255 |
| sw07-p5 | 13 | 13 | 255 |
| sw08-p2 | 25 | 25 | 255 |
| sw08-p4 | 13 | 13 | 255 |
| sw08-p5 | 20 | 20 | 255 |

## Per-hop windows used by newly admitted flows

| flow | egress port | queue | psi (ns, unchanged) | delta (ns, unchanged) |
|---|---|---|---|---|
| s24(id=8 S1->S2) | S1-p0 | Q7 | 0 | 12480 |
| s24(id=8 S1->S2) | sw02-p4 | Q7 | 16640 | 12480 |
| s24(id=8 S1->S2) | sw04-p5 | Q7 | 33280 | 12480 |
| s24(id=8 S1->S2) | sw06-p4 | Q7 | 49920 | 12480 |
| s24(id=8 S1->S2) | sw08-p2 | Q7 | 66560 | 12480 |
| s25(id=11 S3->S2) | S3-p0 | Q6 | 24960 | 12480 |
| s25(id=11 S3->S2) | sw01-p4 | Q6 | 44480 | 12480 |
| s25(id=11 S3->S2) | sw03-p5 | Q6 | 64000 | 12480 |
| s25(id=11 S3->S2) | sw05-p4 | Q6 | 83520 | 12480 |
| s25(id=11 S3->S2) | sw07-p5 | Q6 | 103040 | 12480 |
| s25(id=11 S3->S2) | sw08-p2 | Q6 | 119680 | 12480 |
| s27(id=15 S3->S1) | S3-p0 | Q7 | 0 | 12480 |
| s27(id=15 S3->S1) | sw01-p5 | Q7 | 16640 | 12480 |
| s27(id=15 S3->S1) | sw02-p2 | Q7 | 33280 | 12480 |
| s20(id=1 S2->S1) | S2-p0 | Q7 | 24960 | 12480 |
| s20(id=1 S2->S1) | sw08-p4 | Q7 | 72320 | 12480 |
| s20(id=1 S2->S1) | sw06-p5 | Q7 | 88960 | 12480 |
| s20(id=1 S2->S1) | sw04-p4 | Q7 | 105600 | 12480 |
| s20(id=1 S2->S1) | sw02-p2 | Q7 | 122240 | 12480 |
| s23(id=7 S2->S3) | S2-p0 | Q7 | 75200 | 12480 |
| s23(id=7 S2->S3) | sw08-p5 | Q7 | 150080 | 12480 |
| s23(id=7 S2->S3) | sw07-p4 | Q7 | 166720 | 12480 |
| s23(id=7 S2->S3) | sw05-p5 | Q7 | 183360 | 12480 |
| s23(id=7 S2->S3) | sw03-p4 | Q7 | 249920 | 12480 |
| s23(id=7 S2->S3) | sw01-p2 | Q7 | 266560 | 12480 |
| s29(id=17 S1->S3) | S1-p0 | Q6 | 262720 | 12480 |
| s29(id=17 S1->S3) | sw02-p5 | Q6 | 400000 | 12480 |
| s29(id=17 S1->S3) | sw01-p2 | Q6 | 416640 | 12480 |
| s21(id=3 S3->S1) | S3-p0 | Q6 | 49920 | 12480 |
| s21(id=3 S3->S1) | sw01-p5 | Q6 | 66560 | 12480 |
| s21(id=3 S3->S1) | sw02-p2 | Q6 | 83200 | 12480 |
| s22(id=4 S1->S3) | S1-p0 | Q6 | 100160 | 12480 |
| s22(id=4 S1->S3) | sw02-p5 | Q6 | 116800 | 12480 |
| s22(id=4 S1->S3) | sw01-p2 | Q6 | 163840 | 12480 |
| s38(id=29 S3->S1) | S3-p0 | Q6 | 133120 | 12480 |
| s38(id=29 S3->S1) | sw01-p5 | Q6 | 200000 | 12480 |
| s38(id=29 S3->S1) | sw02-p2 | Q6 | 216640 | 12480 |
| s44(id=35 S1->S3) | S1-p0 | Q6 | 112960 | 12480 |
| s44(id=35 S1->S3) | sw02-p5 | Q6 | 200000 | 12480 |
| s44(id=35 S1->S3) | sw01-p2 | Q6 | 216640 | 12480 |
| s54(id=45 S3->S1) | S3-p0 | Q6 | 333120 | 12480 |
| s54(id=45 S3->S1) | sw01-p5 | Q6 | 400000 | 12480 |
| s54(id=45 S3->S1) | sw02-p2 | Q6 | 416640 | 12480 |
| s56(id=47 S3->S1) | S3-p0 | Q6 | 533120 | 12480 |
| s56(id=47 S3->S1) | sw01-p5 | Q6 | 600000 | 12480 |
| s56(id=47 S3->S1) | sw02-p2 | Q6 | 616640 | 12480 |
| s59(id=50 S3->S1) | S3-p0 | Q7 | 75200 | 12480 |
| s59(id=50 S3->S1) | sw01-p5 | Q7 | 118400 | 12480 |
| s59(id=50 S3->S1) | sw02-p2 | Q7 | 135040 | 12480 |
| s37(id=28 S2->S1) | S2-p0 | Q7 | 87680 | 12480 |
| s37(id=28 S2->S1) | sw08-p4 | Q7 | 104320 | 12480 |
| s37(id=28 S2->S1) | sw06-p5 | Q7 | 120960 | 12480 |
| s37(id=28 S2->S1) | sw04-p4 | Q7 | 137600 | 12480 |
| s37(id=28 S2->S1) | sw02-p2 | Q7 | 154240 | 12480 |
| s41(id=32 S2->S1) | S2-p0 | Q7 | 100480 | 12480 |
| s41(id=32 S2->S1) | sw08-p4 | Q7 | 117120 | 12480 |
| s41(id=32 S2->S1) | sw06-p5 | Q7 | 133760 | 12480 |
| s41(id=32 S2->S1) | sw04-p4 | Q7 | 150400 | 12480 |
| s41(id=32 S2->S1) | sw02-p2 | Q7 | 167040 | 12480 |
| s55(id=46 S1->S2) | S1-p0 | Q6 | 250240 | 12480 |
| s55(id=46 S1->S2) | sw02-p4 | Q6 | 266880 | 12480 |
| s55(id=46 S1->S2) | sw04-p5 | Q6 | 283520 | 12480 |
| s55(id=46 S1->S2) | sw06-p4 | Q6 | 300160 | 12480 |
| s55(id=46 S1->S2) | sw08-p2 | Q6 | 316800 | 12480 |
| s30(id=21 S3->S2) | S3-p0 | Q7 | 87680 | 12480 |
| s30(id=21 S3->S2) | sw01-p4 | Q7 | 244480 | 12480 |
| s30(id=21 S3->S2) | sw03-p5 | Q7 | 264000 | 12480 |
| s30(id=21 S3->S2) | sw05-p4 | Q7 | 283520 | 12480 |
| s30(id=21 S3->S2) | sw07-p5 | Q7 | 350080 | 12480 |
| s30(id=21 S3->S2) | sw08-p2 | Q7 | 383360 | 12480 |
| s39(id=30 S3->S2) | S3-p0 | Q7 | 240640 | 12480 |
| s39(id=30 S3->S2) | sw01-p4 | Q7 | 260160 | 12480 |
| s39(id=30 S3->S2) | sw03-p5 | Q7 | 279680 | 12480 |
| s39(id=30 S3->S2) | sw05-p4 | Q7 | 350080 | 12480 |
| s39(id=30 S3->S2) | sw07-p5 | Q7 | 379520 | 12480 |
| s39(id=30 S3->S2) | sw08-p2 | Q7 | 449920 | 12480 |
| s52(id=43 S3->S1) | S3-p0 | Q7 | 114560 | 12480 |
| s52(id=43 S3->S1) | sw01-p5 | Q7 | 163200 | 12480 |
| s52(id=43 S3->S1) | sw02-p2 | Q7 | 185920 | 12480 |
| s35(id=26 S1->S2) | S1-p0 | Q7 | 49920 | 12480 |
| s35(id=26 S1->S2) | sw02-p4 | Q7 | 150080 | 12480 |
| s35(id=26 S1->S2) | sw04-p5 | Q7 | 166720 | 12480 |
| s35(id=26 S1->S2) | sw06-p4 | Q7 | 183360 | 12480 |
| s35(id=26 S1->S2) | sw08-p2 | Q7 | 249920 | 12480 |
| s57(id=48 S2->S1) | S2-p0 | Q7 | 150080 | 12480 |
| s57(id=48 S2->S1) | sw08-p4 | Q7 | 166720 | 12480 |
| s57(id=48 S2->S1) | sw06-p5 | Q7 | 183360 | 12480 |
| s57(id=48 S2->S1) | sw04-p4 | Q7 | 229440 | 12480 |
| s57(id=48 S2->S1) | sw02-p2 | Q7 | 246080 | 12480 |
| s31(id=22 S2->S3) | S2-p0 | Q6 | 212800 | 12480 |
| s31(id=22 S2->S3) | sw08-p5 | Q6 | 229440 | 12480 |
| s31(id=22 S2->S3) | sw07-p4 | Q6 | 246080 | 12480 |
| s31(id=22 S2->S3) | sw05-p5 | Q6 | 262720 | 12480 |
| s31(id=22 S2->S3) | sw03-p4 | Q6 | 279360 | 12480 |
| s31(id=22 S2->S3) | sw01-p2 | Q6 | 296000 | 12480 |
| s32(id=23 S2->S3) | S2-p0 | Q6 | 225600 | 12480 |
| s32(id=23 S2->S3) | sw08-p5 | Q6 | 242240 | 12480 |
| s32(id=23 S2->S3) | sw07-p4 | Q6 | 258880 | 12480 |
| s32(id=23 S2->S3) | sw05-p5 | Q6 | 275520 | 12480 |
| s32(id=23 S2->S3) | sw03-p4 | Q6 | 292160 | 12480 |
| s32(id=23 S2->S3) | sw01-p2 | Q6 | 308800 | 12480 |
| s34(id=25 S2->S3) | S2-p0 | Q7 | 162560 | 12480 |
| s34(id=25 S2->S3) | sw08-p5 | Q7 | 179200 | 12480 |
| s34(id=25 S2->S3) | sw07-p4 | Q7 | 350080 | 12480 |
| s34(id=25 S2->S3) | sw05-p5 | Q7 | 366720 | 12480 |
| s34(id=25 S2->S3) | sw03-p4 | Q7 | 449920 | 12480 |
| s34(id=25 S2->S3) | sw01-p2 | Q7 | 466560 | 12480 |

## Constraint check

- C1-C7, C9: OK
- window-boundary integrity (no window's psi/delta changed anywhere): OK

## GCL per egress port

### sw01-p2  (27 entries, util 35.8800 %)

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
sgs 12480 0x80 # 10000000   Q7
sgs 5760 0x3F # 00111111   BE
sgs 35520 0x40 # 01000000   Q6
sgs 46400 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 116160 0x40 # 01000000   Q6
sgs 46400 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 103360 0x80 # 10000000   Q7
sgs 46400 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 70400 0x40 # 01000000   Q6
sgs 46400 0xBF # 10111111   Q7
```

### sw01-p4  (12 entries, util 6.2400 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 32000 0x7F # 01111111   Q6
sgs 200000 0x40 # 01000000   Q6
sgs 55680 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 44480 0x7F # 01111111   Q6
sgs 155520 0x40 # 01000000   Q6
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p5  (21 entries, util 24.9600 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 70720 0x80 # 10000000   Q7
sgs 50240 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 133120 0x80 # 10000000   Q7
sgs 50240 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 95680 0x80 # 10000000   Q7
sgs 50240 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 116480 0x80 # 10000000   Q7
sgs 16960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (28 entries, util 37.4400 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 1280 0x3F # 00111111   BE
sgs 63680 0x80 # 10000000   Q7
sgs 14080 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 152640 0x80 # 10000000   Q7
sgs 14080 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 1280 0x3F # 00111111   BE
sgs 63680 0x80 # 10000000   Q7
sgs 14080 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 119360 0x80 # 10000000   Q7
sgs 47360 0xBF # 10111111   Q7
```

### sw02-p4  (24 entries, util 17.1600 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 79360 0x40 # 01000000   Q6
sgs 16640 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 79360 0x40 # 01000000   Q6
sgs 16640 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 79360 0x40 # 01000000   Q6
sgs 16640 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 62720 0x40 # 01000000   Q6
sgs 33280 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p5  (19 entries, util 17.1600 %)

```
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 37760 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12160 0x3F # 00111111   BE
sgs 36160 0x40 # 01000000   Q6
sgs 59840 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 111040 0x80 # 10000000   Q7
sgs 59840 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 37760 0xBF # 10111111   Q7
sgs 60800 0x80 # 10000000   Q7
sgs 59840 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 81920 0x80 # 10000000   Q7
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (22 entries, util 18.7200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 21120 0xBF # 10111111   Q7
sgs 28800 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 5760 0x3F # 00111111   BE
sgs 14080 0x40 # 01000000   Q6
sgs 38720 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 94720 0x40 # 01000000   Q6
sgs 38720 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 94720 0x40 # 01000000   Q6
sgs 38720 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 28160 0x40 # 01000000   Q6
sgs 55360 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p5  (14 entries, util 6.2400 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 14080 0xBF # 10111111   Q7
sgs 200000 0x40 # 01000000   Q6
sgs 36160 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 14080 0xBF # 10111111   Q7
sgs 136000 0x40 # 01000000   Q6
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p4  (15 entries, util 12.4800 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 37760 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 5440 0x3F # 00111111   BE
sgs 227200 0x80 # 10000000   Q7
sgs 17280 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 37760 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 5440 0x3F # 00111111   BE
sgs 139520 0x80 # 10000000   Q7
sgs 55040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (21 entries, util 17.1600 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 79360 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 79360 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 79360 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 46080 0x40 # 01000000   Q6
sgs 33280 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (14 entries, util 6.2400 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 33600 0xBF # 10111111   Q7
sgs 200000 0x40 # 01000000   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 33600 0xBF # 10111111   Q7
sgs 116480 0x40 # 01000000   Q6
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p5  (19 entries, util 18.7200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
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

### sw06-p4  (21 entries, util 17.1600 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 79360 0x40 # 01000000   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 79360 0x40 # 01000000   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 79360 0x40 # 01000000   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 29440 0x40 # 01000000   Q6
sgs 33280 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (15 entries, util 12.4800 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 21120 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 5440 0x3F # 00111111   BE
sgs 227200 0x80 # 10000000   Q7
sgs 33920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 21120 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 5440 0x3F # 00111111   BE
sgs 156160 0x80 # 10000000   Q7
sgs 55040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (19 entries, util 18.7200 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
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

### sw07-p5  (13 entries, util 6.2400 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 53120 0xBF # 10111111   Q7
sgs 200000 0x40 # 01000000   Q6
sgs 47040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 53120 0xBF # 10111111   Q7
sgs 96960 0x40 # 01000000   Q6
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p2  (25 entries, util 23.4000 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 79360 0x40 # 01000000   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 79360 0x40 # 01000000   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 79360 0x40 # 01000000   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 12800 0x40 # 01000000   Q6
sgs 33280 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p4  (13 entries, util 12.4800 %)

```
sgs 54400 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 5440 0x3F # 00111111   BE
sgs 227200 0x80 # 10000000   Q7
sgs 50560 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 54400 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 5440 0x3F # 00111111   BE
sgs 172800 0x80 # 10000000   Q7
sgs 55040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (20 entries, util 18.7200 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 14720 0x80 # 10000000   Q7
sgs 56320 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 77120 0x40 # 01000000   Q6
sgs 56320 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 77120 0x40 # 01000000   Q6
sgs 56320 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 60480 0x40 # 01000000   Q6
sgs 23040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

