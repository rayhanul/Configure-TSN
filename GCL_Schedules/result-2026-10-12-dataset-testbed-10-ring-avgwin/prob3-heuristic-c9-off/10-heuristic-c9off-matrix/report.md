# Reconfiguration-free admission (Problem 3)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Frozen schedule W loaded from: **result/result-2026-10-12-dataset-testbed-10-ring-avgwin/heuristic-c9-off/10-matrix-c9off**

## Admission: W (before) vs. after this run's arrivals

| | admitted | of total |
|---|---|---|
| W (base, unchanged) | 11 | 11 |
| + this run's arrivals | 23 | 39 |

Every arrival admitted here required **zero** window-boundary changes -- see the GCL-entry table below (unchanged from W by construction) and the window-boundary integrity check. No previously-admitted flow was rerouted.

## Arrivals

| id | src->dst | RS(s) size | admitted | route | queue | phi_s (ns) | e2e (ns) | rerouted to make room | reason if rejected |
|---|---|---|---|---|---|---|---|---|---|
| 20 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 4 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 13 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q6 | 12480 | 216640 | - | - |
| 16 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 14 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 62720 | 249920 | - | - |
| 2 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q6 | 131520 | 297600 | - | - |
| 8 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q7 | 350080 | 45760 | - | - |
| 6 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q7 | 62400 | 133440 | - | - |
| 19 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q6 | 37440 | 375040 | - | - |
| 34 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q6 | 332480 | 96640 | - | - |
| 47 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q6 | 437440 | 291840 | - | - |
| 21 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 87680 | 79040 | - | - |
| 22 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 100480 | 112000 | - | - |
| 40 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 150080 | 462400 | - | - |
| 23 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 75200 | 95680 | - | - |
| 24 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q6 | 531520 | 197760 | - | - |
| 28 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q7 | 150080 | 112320 | - | - |
| 30 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 | 62400 | 117120 | - | - |
| 38 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q7 | 87680 | 279680 | - | - |
| 39 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q7 | 175680 | 203520 | - | - |
| 42 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 46 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 212800 | 108480 | - | - |
| 50 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 88000 | 324480 | - | - |
| 27 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 111040 | 231040 | - | - |
| 29 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 31 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 | 100160 | 178880 | - | - |
| 32 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 | 212800 | 249600 | - | - |
| 35 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 36 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 41 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 45 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 48 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 | 225600 | 253440 | - | - |
| 25 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 33 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 43 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 44 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 49 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 26 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 37 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |

## Per-port GCL entries (should equal W exactly)

| port | W entries | after arrivals | GCL_size |
|---|---|---|---|
| sw01-p2 | 32 | 32 | 255 |
| sw01-p4 | 21 | 21 | 255 |
| sw01-p5 | 16 | 16 | 255 |
| sw02-p2 | 18 | 18 | 255 |
| sw02-p4 | 19 | 19 | 255 |
| sw02-p5 | 23 | 23 | 255 |
| sw03-p4 | 22 | 22 | 255 |
| sw03-p5 | 18 | 18 | 255 |
| sw04-p4 | 10 | 10 | 255 |
| sw04-p5 | 24 | 24 | 255 |
| sw05-p4 | 18 | 18 | 255 |
| sw05-p5 | 22 | 22 | 255 |
| sw06-p4 | 21 | 21 | 255 |
| sw06-p5 | 10 | 10 | 255 |
| sw07-p4 | 21 | 21 | 255 |
| sw07-p5 | 22 | 22 | 255 |
| sw08-p2 | 24 | 24 | 255 |
| sw08-p4 | 10 | 10 | 255 |
| sw08-p5 | 21 | 21 | 255 |

## Per-hop windows used by newly admitted flows

| flow | egress port | queue | psi (ns, unchanged) | delta (ns, unchanged) |
|---|---|---|---|---|
| s24(id=13 S3->S2) | S3-p0 | Q6 | 12480 | 12480 |
| s24(id=13 S3->S2) | sw01-p4 | Q6 | 100160 | 12480 |
| s24(id=13 S3->S2) | sw03-p5 | Q6 | 116800 | 12480 |
| s24(id=13 S3->S2) | sw05-p4 | Q6 | 133440 | 12480 |
| s24(id=13 S3->S2) | sw07-p5 | Q6 | 200000 | 12480 |
| s24(id=13 S3->S2) | sw08-p2 | Q6 | 216640 | 12480 |
| s25(id=14 S2->S1) | S2-p0 | Q6 | 62720 | 12480 |
| s25(id=14 S2->S1) | sw08-p4 | Q6 | 79360 | 12480 |
| s25(id=14 S2->S1) | sw06-p5 | Q6 | 96000 | 12480 |
| s25(id=14 S2->S1) | sw04-p4 | Q6 | 117120 | 12480 |
| s25(id=14 S2->S1) | sw02-p2 | Q6 | 133760 | 12480 |
| s20(id=2 S3->S2) | S3-p0 | Q6 | 131520 | 12480 |
| s20(id=2 S3->S2) | sw01-p4 | Q6 | 200000 | 12480 |
| s20(id=2 S3->S2) | sw03-p5 | Q6 | 216640 | 12480 |
| s20(id=2 S3->S2) | sw05-p4 | Q6 | 233280 | 12480 |
| s20(id=2 S3->S2) | sw07-p5 | Q6 | 400000 | 12480 |
| s20(id=2 S3->S2) | sw08-p2 | Q6 | 416640 | 12480 |
| s23(id=8 S1->S3) | S1-p0 | Q7 | 350080 | 12480 |
| s23(id=8 S1->S3) | sw02-p5 | Q7 | 366720 | 12480 |
| s23(id=8 S1->S3) | sw01-p2 | Q7 | 383360 | 12480 |
| s22(id=6 S1->S3) | S1-p0 | Q7 | 62400 | 12480 |
| s22(id=6 S1->S3) | sw02-p5 | Q7 | 150080 | 12480 |
| s22(id=6 S1->S3) | sw01-p2 | Q7 | 183360 | 12480 |
| s27(id=19 S3->S1) | S3-p0 | Q6 | 37440 | 12480 |
| s27(id=19 S3->S1) | sw01-p5 | Q6 | 336320 | 12480 |
| s27(id=19 S3->S1) | sw02-p2 | Q6 | 400000 | 12480 |
| s42(id=34 S3->S1) | S3-p0 | Q6 | 332480 | 12480 |
| s42(id=34 S3->S1) | sw01-p5 | Q6 | 400000 | 12480 |
| s42(id=34 S3->S1) | sw02-p2 | Q6 | 416640 | 12480 |
| s55(id=47 S3->S1) | S3-p0 | Q6 | 437440 | 12480 |
| s55(id=47 S3->S1) | sw01-p5 | Q6 | 700160 | 12480 |
| s55(id=47 S3->S1) | sw02-p2 | Q6 | 716800 | 12480 |
| s29(id=21 S1->S2) | S1-p0 | Q7 | 87680 | 12480 |
| s29(id=21 S1->S2) | sw02-p4 | Q7 | 104320 | 12480 |
| s29(id=21 S1->S2) | sw04-p5 | Q7 | 120960 | 12480 |
| s29(id=21 S1->S2) | sw06-p4 | Q7 | 137600 | 12480 |
| s29(id=21 S1->S2) | sw08-p2 | Q7 | 154240 | 12480 |
| s30(id=22 S1->S2) | S1-p0 | Q7 | 100480 | 12480 |
| s30(id=22 S1->S2) | sw02-p4 | Q7 | 150080 | 12480 |
| s30(id=22 S1->S2) | sw04-p5 | Q7 | 166720 | 12480 |
| s30(id=22 S1->S2) | sw06-p4 | Q7 | 183360 | 12480 |
| s30(id=22 S1->S2) | sw08-p2 | Q7 | 200000 | 12480 |
| s48(id=40 S2->S1) | S2-p0 | Q7 | 150080 | 12480 |
| s48(id=40 S2->S1) | sw08-p4 | Q7 | 550080 | 12480 |
| s48(id=40 S2->S1) | sw06-p5 | Q7 | 566720 | 12480 |
| s48(id=40 S2->S1) | sw04-p4 | Q7 | 583360 | 12480 |
| s48(id=40 S2->S1) | sw02-p2 | Q7 | 600000 | 12480 |
| s31(id=23 S2->S3) | S2-p0 | Q6 | 75200 | 12480 |
| s31(id=23 S2->S3) | sw08-p5 | Q6 | 91840 | 12480 |
| s31(id=23 S2->S3) | sw07-p4 | Q6 | 108480 | 12480 |
| s31(id=23 S2->S3) | sw05-p5 | Q6 | 125120 | 12480 |
| s31(id=23 S2->S3) | sw03-p4 | Q6 | 141760 | 12480 |
| s31(id=23 S2->S3) | sw01-p2 | Q6 | 158400 | 12480 |
| s32(id=24 S3->S2) | S3-p0 | Q6 | 531520 | 12480 |
| s32(id=24 S3->S2) | sw01-p4 | Q6 | 600000 | 12480 |
| s32(id=24 S3->S2) | sw03-p5 | Q6 | 616640 | 12480 |
| s32(id=24 S3->S2) | sw05-p4 | Q6 | 633280 | 12480 |
| s32(id=24 S3->S2) | sw07-p5 | Q6 | 700160 | 12480 |
| s32(id=24 S3->S2) | sw08-p2 | Q6 | 716800 | 12480 |
| s36(id=28 S1->S3) | S1-p0 | Q7 | 150080 | 12480 |
| s36(id=28 S1->S3) | sw02-p5 | Q7 | 179520 | 12480 |
| s36(id=28 S1->S3) | sw01-p2 | Q7 | 249920 | 12480 |
| s38(id=30 S3->S2) | S3-p0 | Q7 | 62400 | 12480 |
| s38(id=30 S3->S2) | sw01-p4 | Q7 | 79040 | 12480 |
| s38(id=30 S3->S2) | sw03-p5 | Q7 | 95680 | 12480 |
| s38(id=30 S3->S2) | sw05-p4 | Q7 | 112320 | 12480 |
| s38(id=30 S3->S2) | sw07-p5 | Q7 | 150400 | 12480 |
| s38(id=30 S3->S2) | sw08-p2 | Q7 | 167040 | 12480 |
| s46(id=38 S3->S1) | S3-p0 | Q7 | 87680 | 12480 |
| s46(id=38 S3->S1) | sw01-p5 | Q7 | 104320 | 12480 |
| s46(id=38 S3->S1) | sw02-p2 | Q7 | 354880 | 12480 |
| s47(id=39 S1->S3) | S1-p0 | Q7 | 175680 | 12480 |
| s47(id=39 S1->S3) | sw02-p5 | Q7 | 350080 | 12480 |
| s47(id=39 S1->S3) | sw01-p2 | Q7 | 366720 | 12480 |
| s54(id=46 S2->S3) | S2-p0 | Q7 | 212800 | 12480 |
| s54(id=46 S2->S3) | sw08-p5 | Q7 | 236160 | 12480 |
| s54(id=46 S2->S3) | sw07-p4 | Q7 | 252800 | 12480 |
| s54(id=46 S2->S3) | sw05-p5 | Q7 | 269440 | 12480 |
| s54(id=46 S2->S3) | sw03-p4 | Q7 | 292160 | 12480 |
| s54(id=46 S2->S3) | sw01-p2 | Q7 | 308800 | 12480 |
| s58(id=50 S2->S3) | S2-p0 | Q6 | 88000 | 12480 |
| s58(id=50 S2->S3) | sw08-p5 | Q6 | 113280 | 12480 |
| s58(id=50 S2->S3) | sw07-p4 | Q6 | 136640 | 12480 |
| s58(id=50 S2->S3) | sw05-p5 | Q6 | 200000 | 12480 |
| s58(id=50 S2->S3) | sw03-p4 | Q6 | 229440 | 12480 |
| s58(id=50 S2->S3) | sw01-p2 | Q6 | 400000 | 12480 |
| s35(id=27 S2->S1) | S2-p0 | Q6 | 111040 | 12480 |
| s35(id=27 S2->S1) | sw08-p4 | Q6 | 127680 | 12480 |
| s35(id=27 S2->S1) | sw06-p5 | Q6 | 144320 | 12480 |
| s35(id=27 S2->S1) | sw04-p4 | Q6 | 160960 | 12480 |
| s35(id=27 S2->S1) | sw02-p2 | Q6 | 177600 | 12480 |
| s39(id=31 S3->S2) | S3-p0 | Q7 | 100160 | 12480 |
| s39(id=31 S3->S2) | sw01-p4 | Q7 | 150080 | 12480 |
| s39(id=31 S3->S2) | sw03-p5 | Q7 | 166720 | 12480 |
| s39(id=31 S3->S2) | sw05-p4 | Q7 | 183360 | 12480 |
| s39(id=31 S3->S2) | sw07-p5 | Q7 | 249920 | 12480 |
| s39(id=31 S3->S2) | sw08-p2 | Q7 | 266560 | 12480 |
| s40(id=32 S3->S2) | S3-p0 | Q7 | 212800 | 12480 |
| s40(id=32 S3->S2) | sw01-p4 | Q7 | 229440 | 12480 |
| s40(id=32 S3->S2) | sw03-p5 | Q7 | 246080 | 12480 |
| s40(id=32 S3->S2) | sw05-p4 | Q7 | 262720 | 12480 |
| s40(id=32 S3->S2) | sw07-p5 | Q7 | 279360 | 12480 |
| s40(id=32 S3->S2) | sw08-p2 | Q7 | 449920 | 12480 |
| s56(id=48 S3->S2) | S3-p0 | Q7 | 225600 | 12480 |
| s56(id=48 S3->S2) | sw01-p4 | Q7 | 242240 | 12480 |
| s56(id=48 S3->S2) | sw03-p5 | Q7 | 258880 | 12480 |
| s56(id=48 S3->S2) | sw05-p4 | Q7 | 275520 | 12480 |
| s56(id=48 S3->S2) | sw07-p5 | Q7 | 449920 | 12480 |
| s56(id=48 S3->S2) | sw08-p2 | Q7 | 466560 | 12480 |

## Constraint check

- C1-C7, C9: OK
- window-boundary integrity (no window's psi/delta changed anywhere): OK

## GCL per egress port

### sw01-p2  (32 entries, util 34.3200 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 33280 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 74560 0x40 # 01000000   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12800 0x40 # 01000000   Q6
sgs 3840 0x3F # 00111111   BE
sgs 46080 0xBF # 10111111   Q7
sgs 87360 0x80 # 10000000   Q7
sgs 16640 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 33280 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 74560 0x40 # 01000000   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12800 0x40 # 01000000   Q6
sgs 3840 0x3F # 00111111   BE
sgs 46080 0xBF # 10111111   Q7
sgs 54080 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p4  (21 entries, util 23.4000 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 75200 0x80 # 10000000   Q7
sgs 8320 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 75200 0x80 # 10000000   Q7
sgs 8320 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 75200 0x80 # 10000000   Q7
sgs 8320 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 58560 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p5  (16 entries, util 15.6000 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 244800 0x80 # 10000000   Q7
sgs 13760 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 228160 0x80 # 10000000   Q7
sgs 5440 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (18 entries, util 24.9600 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 233920 0x40 # 01000000   Q6
sgs 45120 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 213440 0x80 # 10000000   Q7
sgs 3520 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p4  (19 entries, util 10.9200 %)

```
sgs 42240 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 36800 0xBF # 10111111   Q7
sgs 27840 0x80 # 10000000   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 42240 0x7F # 01111111   Q6
sgs 77120 0x40 # 01000000   Q6
sgs 30720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 42240 0x7F # 01111111   Q6
sgs 77120 0x40 # 01000000   Q6
sgs 30720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 42240 0x7F # 01111111   Q6
sgs 34880 0x40 # 01000000   Q6
sgs 23040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p5  (23 entries, util 20.2800 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 59520 0x40 # 01000000   Q6
sgs 24000 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 109440 0x40 # 01000000   Q6
sgs 24000 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 59520 0x40 # 01000000   Q6
sgs 24000 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 92800 0x40 # 01000000   Q6
sgs 40640 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (22 entries, util 14.0400 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 23360 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 5760 0x3F # 00111111   BE
sgs 78400 0x40 # 01000000   Q6
sgs 30080 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 23360 0xBF # 10111111   Q7
sgs 96640 0x80 # 10000000   Q7
sgs 30080 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 23360 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 5760 0x3F # 00111111   BE
sgs 78400 0x40 # 01000000   Q6
sgs 30080 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 23360 0xBF # 10111111   Q7
sgs 23360 0x80 # 10000000   Q7
sgs 3520 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p5  (18 entries, util 23.4000 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 75200 0x80 # 10000000   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 75200 0x80 # 10000000   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 75200 0x80 # 10000000   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 41920 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p4  (10 entries, util 9.3600 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 437760 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (24 entries, util 10.9200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 8960 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 28800 0xBF # 10111111   Q7
sgs 8000 0x3F # 00111111   BE
sgs 27840 0x80 # 10000000   Q7
sgs 14080 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 8960 0x3F # 00111111   BE
sgs 77120 0x40 # 01000000   Q6
sgs 14080 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 8960 0x3F # 00111111   BE
sgs 77120 0x40 # 01000000   Q6
sgs 14080 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 8960 0x3F # 00111111   BE
sgs 18240 0x40 # 01000000   Q6
sgs 23040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (18 entries, util 23.4000 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 75200 0x80 # 10000000   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 75200 0x80 # 10000000   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 75200 0x80 # 10000000   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 25280 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p5  (22 entries, util 14.0400 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 6720 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 5760 0x3F # 00111111   BE
sgs 78400 0x40 # 01000000   Q6
sgs 46720 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 6720 0x3F # 00111111   BE
sgs 96640 0x80 # 10000000   Q7
sgs 46720 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 6720 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 5760 0x3F # 00111111   BE
sgs 78400 0x40 # 01000000   Q6
sgs 46720 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 6720 0x3F # 00111111   BE
sgs 40000 0x80 # 10000000   Q7
sgs 3520 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p4  (21 entries, util 10.9200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 25600 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12160 0x3F # 00111111   BE
sgs 24640 0x7F # 01111111   Q6
sgs 27840 0x80 # 10000000   Q7
sgs 47360 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 25600 0xBF # 10111111   Q7
sgs 77120 0x40 # 01000000   Q6
sgs 47360 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 25600 0xBF # 10111111   Q7
sgs 77120 0x40 # 01000000   Q6
sgs 47360 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 25600 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12160 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (10 entries, util 9.3600 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 454400 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (21 entries, util 14.0400 %)

```
sgs 40000 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 5760 0x3F # 00111111   BE
sgs 78400 0x40 # 01000000   Q6
sgs 13440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 40000 0x7F # 01111111   Q6
sgs 96640 0x80 # 10000000   Q7
sgs 13440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 40000 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 5760 0x3F # 00111111   BE
sgs 78400 0x40 # 01000000   Q6
sgs 13440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 40000 0x7F # 01111111   Q6
sgs 56640 0x80 # 10000000   Q7
sgs 3520 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p5  (22 entries, util 23.4000 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 75200 0x80 # 10000000   Q7
sgs 8320 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 75200 0x80 # 10000000   Q7
sgs 8320 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 75200 0x80 # 10000000   Q7
sgs 8320 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 21120 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p2  (24 entries, util 34.3200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 32960 0x7F # 01111111   Q6
sgs 73280 0x80 # 10000000   Q7
sgs 35200 0x7F # 01111111   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 118720 0x40 # 01000000   Q6
sgs 35200 0x7F # 01111111   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 118720 0x40 # 01000000   Q6
sgs 35200 0x7F # 01111111   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 35520 0x40 # 01000000   Q6
sgs 18560 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p4  (10 entries, util 9.3600 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 471040 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (21 entries, util 14.0400 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 71680 0x40 # 01000000   Q6
sgs 36800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 96640 0x80 # 10000000   Q7
sgs 36800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 71680 0x40 # 01000000   Q6
sgs 36800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 80000 0x80 # 10000000   Q7
sgs 3520 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

