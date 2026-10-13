# Reconfiguration-free admission (Problem 3)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Frozen schedule W loaded from: **result/result-2026-10-12-dataset-testbed-8-ring-avgwin/rl-c9-on/8-matrix-c9on**

## Admission: W (before) vs. after this run's arrivals

| | admitted | of total |
|---|---|---|
| W (base, unchanged) | 10 | 10 |
| + this run's arrivals | 28 | 40 |

Every arrival admitted here required **zero** window-boundary changes -- see the GCL-entry table below (unchanged from W by construction) and the window-boundary integrity check. No previously-admitted flow was rerouted.

## Arrivals

| id | src->dst | RS(s) size | admitted | route | queue | phi_s (ns) | e2e (ns) | rerouted to make room | reason if rejected |
|---|---|---|---|---|---|---|---|---|---|
| 14 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 49920 | 85760 | - | - |
| 8 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q6 | 0 | 39360 | - | - |
| 16 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 74880 | 96320 | - | - |
| 11 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 | 350080 | 46080 | - | - |
| 15 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 1 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 12480 | 39360 | - | - |
| 7 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 77440 | 335040 | - | - |
| 17 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q6 | 24960 | 50880 | - | - |
| 3 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q7 | 74880 | 296000 | - | - |
| 4 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q7 | 163200 | 36160 | - | - |
| 29 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q6 | 289600 | 25920 | - | - |
| 35 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q6 | 99840 | 112640 | - | - |
| 45 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q7 | 362560 | 22720 | - | - |
| 47 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q6 | 302080 | 29440 | - | - |
| 50 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q7 | 375040 | 394240 | - | - |
| 28 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 24960 | 91200 | - | - |
| 32 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 89920 | 45760 | - | - |
| 46 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 250880 | 44800 | - | - |
| 21 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q6 | 0 | 97920 | - | - |
| 30 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 | 49920 | 321280 | - | - |
| 43 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q6 | 314560 | 33280 | - | - |
| 26 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q6 | 49920 | 104640 | - | - |
| 31 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 287360 | 83520 | - | - |
| 44 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q6 | 224960 | 187520 | - | - |
| 48 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 150080 | 248000 | - | - |
| 22 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 212480 | 52800 | - | - |
| 23 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 224960 | 52800 | - | - |
| 25 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 262400 | 114240 | - | - |
| 27 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 274880 | 114240 | - | - |
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
| sw01-p2 | 36 | 36 | 255 |
| sw01-p4 | 13 | 13 | 255 |
| sw01-p5 | 16 | 16 | 255 |
| sw02-p2 | 19 | 19 | 255 |
| sw02-p4 | 21 | 21 | 255 |
| sw02-p5 | 24 | 24 | 255 |
| sw03-p4 | 19 | 19 | 255 |
| sw03-p5 | 12 | 12 | 255 |
| sw04-p4 | 13 | 13 | 255 |
| sw04-p5 | 24 | 24 | 255 |
| sw05-p4 | 12 | 12 | 255 |
| sw05-p5 | 19 | 19 | 255 |
| sw06-p4 | 28 | 28 | 255 |
| sw06-p5 | 13 | 13 | 255 |
| sw07-p4 | 21 | 21 | 255 |
| sw07-p5 | 14 | 14 | 255 |
| sw08-p2 | 25 | 25 | 255 |
| sw08-p4 | 14 | 14 | 255 |
| sw08-p5 | 18 | 18 | 255 |

## Per-hop windows used by newly admitted flows

| flow | egress port | queue | psi (ns, unchanged) | delta (ns, unchanged) |
|---|---|---|---|---|
| s26(id=14 S2->S3) | S2-p0 | Q7 | 49920 | 12480 |
| s26(id=14 S2->S3) | sw08-p5 | Q7 | 56640 | 12480 |
| s26(id=14 S2->S3) | sw07-p4 | Q7 | 63360 | 12480 |
| s26(id=14 S2->S3) | sw05-p5 | Q7 | 70080 | 12480 |
| s26(id=14 S2->S3) | sw03-p4 | Q7 | 76800 | 12480 |
| s26(id=14 S2->S3) | sw01-p2 | Q7 | 123200 | 12480 |
| s24(id=8 S1->S2) | S1-p0 | Q6 | 0 | 12480 |
| s24(id=8 S1->S2) | sw02-p4 | Q6 | 6720 | 12480 |
| s24(id=8 S1->S2) | sw04-p5 | Q6 | 13440 | 12480 |
| s24(id=8 S1->S2) | sw06-p4 | Q6 | 20160 | 12480 |
| s24(id=8 S1->S2) | sw08-p2 | Q6 | 26880 | 12480 |
| s28(id=16 S1->S2) | S1-p0 | Q7 | 74880 | 12480 |
| s28(id=16 S1->S2) | sw02-p4 | Q7 | 80960 | 12480 |
| s28(id=16 S1->S2) | sw04-p5 | Q7 | 87040 | 12480 |
| s28(id=16 S1->S2) | sw06-p4 | Q7 | 93120 | 12480 |
| s28(id=16 S1->S2) | sw08-p2 | Q7 | 158720 | 12480 |
| s25(id=11 S3->S2) | S3-p0 | Q7 | 350080 | 12480 |
| s25(id=11 S3->S2) | sw01-p4 | Q7 | 356800 | 12480 |
| s25(id=11 S3->S2) | sw03-p5 | Q7 | 363520 | 12480 |
| s25(id=11 S3->S2) | sw05-p4 | Q7 | 370240 | 12480 |
| s25(id=11 S3->S2) | sw07-p5 | Q7 | 376960 | 12480 |
| s25(id=11 S3->S2) | sw08-p2 | Q7 | 383680 | 12480 |
| s20(id=1 S2->S1) | S2-p0 | Q6 | 12480 | 12480 |
| s20(id=1 S2->S1) | sw08-p4 | Q6 | 19200 | 12480 |
| s20(id=1 S2->S1) | sw06-p5 | Q6 | 25920 | 12480 |
| s20(id=1 S2->S1) | sw04-p4 | Q6 | 32640 | 12480 |
| s20(id=1 S2->S1) | sw02-p2 | Q6 | 39360 | 12480 |
| s23(id=7 S2->S3) | S2-p0 | Q6 | 77440 | 12480 |
| s23(id=7 S2->S3) | sw08-p5 | Q6 | 114560 | 12480 |
| s23(id=7 S2->S3) | sw07-p4 | Q6 | 128320 | 12480 |
| s23(id=7 S2->S3) | sw05-p5 | Q6 | 200000 | 12480 |
| s23(id=7 S2->S3) | sw03-p4 | Q6 | 325120 | 12480 |
| s23(id=7 S2->S3) | sw01-p2 | Q6 | 400000 | 12480 |
| s29(id=17 S1->S3) | S1-p0 | Q6 | 24960 | 12480 |
| s29(id=17 S1->S3) | sw02-p5 | Q6 | 31680 | 12480 |
| s29(id=17 S1->S3) | sw01-p2 | Q6 | 63360 | 12480 |
| s21(id=3 S3->S1) | S3-p0 | Q7 | 74880 | 12480 |
| s21(id=3 S3->S1) | sw01-p5 | Q7 | 350080 | 12480 |
| s21(id=3 S3->S1) | sw02-p2 | Q7 | 358400 | 12480 |
| s22(id=4 S1->S3) | S1-p0 | Q7 | 163200 | 12480 |
| s22(id=4 S1->S3) | sw02-p5 | Q7 | 169920 | 12480 |
| s22(id=4 S1->S3) | sw01-p2 | Q7 | 186880 | 12480 |
| s38(id=29 S3->S1) | S3-p0 | Q6 | 289600 | 12480 |
| s38(id=29 S3->S1) | sw01-p5 | Q6 | 296320 | 12480 |
| s38(id=29 S3->S1) | sw02-p2 | Q6 | 303040 | 12480 |
| s44(id=35 S1->S3) | S1-p0 | Q6 | 99840 | 12480 |
| s44(id=35 S1->S3) | sw02-p5 | Q6 | 108160 | 12480 |
| s44(id=35 S1->S3) | sw01-p2 | Q6 | 200000 | 12480 |
| s54(id=45 S3->S1) | S3-p0 | Q7 | 362560 | 12480 |
| s54(id=45 S3->S1) | sw01-p5 | Q7 | 367680 | 12480 |
| s54(id=45 S3->S1) | sw02-p2 | Q7 | 372800 | 12480 |
| s56(id=47 S3->S1) | S3-p0 | Q6 | 302080 | 12480 |
| s56(id=47 S3->S1) | sw01-p5 | Q6 | 312320 | 12480 |
| s56(id=47 S3->S1) | sw02-p2 | Q6 | 319040 | 12480 |
| s59(id=50 S3->S1) | S3-p0 | Q7 | 375040 | 12480 |
| s59(id=50 S3->S1) | sw01-p5 | Q7 | 750080 | 12480 |
| s59(id=50 S3->S1) | sw02-p2 | Q7 | 756800 | 12480 |
| s37(id=28 S2->S1) | S2-p0 | Q6 | 24960 | 12480 |
| s37(id=28 S2->S1) | sw08-p4 | Q6 | 77760 | 12480 |
| s37(id=28 S2->S1) | sw06-p5 | Q6 | 87360 | 12480 |
| s37(id=28 S2->S1) | sw04-p4 | Q6 | 96960 | 12480 |
| s37(id=28 S2->S1) | sw02-p2 | Q6 | 103680 | 12480 |
| s41(id=32 S2->S1) | S2-p0 | Q6 | 89920 | 12480 |
| s41(id=32 S2->S1) | sw08-p4 | Q6 | 98240 | 12480 |
| s41(id=32 S2->S1) | sw06-p5 | Q6 | 106560 | 12480 |
| s41(id=32 S2->S1) | sw04-p4 | Q6 | 114880 | 12480 |
| s41(id=32 S2->S1) | sw02-p2 | Q6 | 123200 | 12480 |
| s55(id=46 S1->S2) | S1-p0 | Q7 | 250880 | 12480 |
| s55(id=46 S1->S2) | sw02-p4 | Q7 | 258560 | 12480 |
| s55(id=46 S1->S2) | sw04-p5 | Q7 | 266560 | 12480 |
| s55(id=46 S1->S2) | sw06-p4 | Q7 | 274880 | 12480 |
| s55(id=46 S1->S2) | sw08-p2 | Q7 | 283200 | 12480 |
| s30(id=21 S3->S2) | S3-p0 | Q6 | 0 | 12480 |
| s30(id=21 S3->S2) | sw01-p4 | Q6 | 12480 | 12480 |
| s30(id=21 S3->S2) | sw03-p5 | Q6 | 17600 | 12480 |
| s30(id=21 S3->S2) | sw05-p4 | Q6 | 22720 | 12480 |
| s30(id=21 S3->S2) | sw07-p5 | Q6 | 27840 | 12480 |
| s30(id=21 S3->S2) | sw08-p2 | Q6 | 85440 | 12480 |
| s39(id=30 S3->S2) | S3-p0 | Q7 | 49920 | 12480 |
| s39(id=30 S3->S2) | sw01-p4 | Q7 | 249920 | 12480 |
| s39(id=30 S3->S2) | sw03-p5 | Q7 | 256000 | 12480 |
| s39(id=30 S3->S2) | sw05-p4 | Q7 | 262080 | 12480 |
| s39(id=30 S3->S2) | sw07-p5 | Q7 | 350080 | 12480 |
| s39(id=30 S3->S2) | sw08-p2 | Q7 | 358720 | 12480 |
| s52(id=43 S3->S1) | S3-p0 | Q6 | 314560 | 12480 |
| s52(id=43 S3->S1) | sw01-p5 | Q6 | 324800 | 12480 |
| s52(id=43 S3->S1) | sw02-p2 | Q6 | 333120 | 12480 |
| s35(id=26 S1->S2) | S1-p0 | Q6 | 49920 | 12480 |
| s35(id=26 S1->S2) | sw02-p4 | Q6 | 123520 | 12480 |
| s35(id=26 S1->S2) | sw04-p5 | Q6 | 130240 | 12480 |
| s35(id=26 S1->S2) | sw06-p4 | Q6 | 136960 | 12480 |
| s35(id=26 S1->S2) | sw08-p2 | Q6 | 142080 | 12480 |
| s40(id=31 S1->S2) | S1-p0 | Q7 | 287360 | 12480 |
| s40(id=31 S1->S2) | sw02-p4 | Q7 | 295680 | 12480 |
| s40(id=31 S1->S2) | sw04-p5 | Q7 | 304000 | 12480 |
| s40(id=31 S1->S2) | sw06-p4 | Q7 | 312320 | 12480 |
| s40(id=31 S1->S2) | sw08-p2 | Q7 | 320640 | 12480 |
| s53(id=44 S1->S2) | S1-p0 | Q6 | 224960 | 12480 |
| s53(id=44 S1->S2) | sw02-p4 | Q6 | 231040 | 12480 |
| s53(id=44 S1->S2) | sw04-p5 | Q6 | 237120 | 12480 |
| s53(id=44 S1->S2) | sw06-p4 | Q6 | 336960 | 12480 |
| s53(id=44 S1->S2) | sw08-p2 | Q6 | 400000 | 12480 |
| s57(id=48 S2->S1) | S2-p0 | Q7 | 150080 | 12480 |
| s57(id=48 S2->S1) | sw08-p4 | Q7 | 287680 | 12480 |
| s57(id=48 S2->S1) | sw06-p5 | Q7 | 350080 | 12480 |
| s57(id=48 S2->S1) | sw04-p4 | Q7 | 378880 | 12480 |
| s57(id=48 S2->S1) | sw02-p2 | Q7 | 385600 | 12480 |
| s31(id=22 S2->S3) | S2-p0 | Q7 | 212480 | 12480 |
| s31(id=22 S2->S3) | sw08-p5 | Q7 | 219200 | 12480 |
| s31(id=22 S2->S3) | sw07-p4 | Q7 | 232640 | 12480 |
| s31(id=22 S2->S3) | sw05-p5 | Q7 | 239360 | 12480 |
| s31(id=22 S2->S3) | sw03-p4 | Q7 | 246080 | 12480 |
| s31(id=22 S2->S3) | sw01-p2 | Q7 | 252800 | 12480 |
| s32(id=23 S2->S3) | S2-p0 | Q7 | 224960 | 12480 |
| s32(id=23 S2->S3) | sw08-p5 | Q7 | 231680 | 12480 |
| s32(id=23 S2->S3) | sw07-p4 | Q7 | 245120 | 12480 |
| s32(id=23 S2->S3) | sw05-p5 | Q7 | 251840 | 12480 |
| s32(id=23 S2->S3) | sw03-p4 | Q7 | 258560 | 12480 |
| s32(id=23 S2->S3) | sw01-p2 | Q7 | 265280 | 12480 |
| s34(id=25 S2->S3) | S2-p0 | Q7 | 262400 | 12480 |
| s34(id=25 S2->S3) | sw08-p5 | Q7 | 269120 | 12480 |
| s34(id=25 S2->S3) | sw07-p4 | Q7 | 275840 | 12480 |
| s34(id=25 S2->S3) | sw05-p5 | Q7 | 282560 | 12480 |
| s34(id=25 S2->S3) | sw03-p4 | Q7 | 289280 | 12480 |
| s34(id=25 S2->S3) | sw01-p2 | Q7 | 323200 | 12480 |
| s36(id=27 S2->S3) | S2-p0 | Q7 | 274880 | 12480 |
| s36(id=27 S2->S3) | sw08-p5 | Q7 | 281600 | 12480 |
| s36(id=27 S2->S3) | sw07-p4 | Q7 | 288320 | 12480 |
| s36(id=27 S2->S3) | sw05-p5 | Q7 | 295040 | 12480 |
| s36(id=27 S2->S3) | sw03-p4 | Q7 | 350080 | 12480 |
| s36(id=27 S2->S3) | sw01-p2 | Q7 | 356800 | 12480 |

## Constraint check

- C1-C7, C9: OK
- window-boundary integrity (no window's psi/delta changed anywhere): OK

## GCL per egress port

### sw01-p2  (36 entries, util 45.2400 %)

```
sgs 22720 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 15360 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 9280 0x3F # 00111111   BE
sgs 25280 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 63680 0x80 # 10000000   Q7
sgs 13120 0xBF # 10111111   Q7
sgs 22720 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 51840 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 63680 0x80 # 10000000   Q7
sgs 13120 0xBF # 10111111   Q7
sgs 22720 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 15360 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 111040 0x80 # 10000000   Q7
sgs 13120 0xBF # 10111111   Q7
sgs 22720 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 51840 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 40960 0x80 # 10000000   Q7
sgs 35840 0xBF # 10111111   Q7
```

### sw01-p4  (13 entries, util 6.2400 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 22080 0x7F # 01111111   Q6
sgs 200000 0x40 # 01000000   Q6
sgs 15360 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 34560 0x7F # 01111111   Q6
sgs 165440 0x40 # 01000000   Q6
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p5  (16 entries, util 18.7200 %)

```
sgs 17600 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 15040 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 10880 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 231040 0x40 # 01000000   Q6
sgs 37760 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 17600 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 15040 0x7F # 01111111   Q6
sgs 249600 0x40 # 01000000   Q6
sgs 55360 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (19 entries, util 31.2000 %)

```
sgs 22720 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 17600 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 640 0x3F # 00111111   BE
sgs 266560 0x40 # 01000000   Q6
sgs 41920 0xBF # 10111111   Q7
sgs 22720 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 17600 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 28480 0xBF # 10111111   Q7
sgs 228800 0x40 # 01000000   Q6
sgs 14720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p4  (21 entries, util 29.6400 %)

```
sgs 6720 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 26560 0x7F # 01111111   Q6
sgs 77760 0x80 # 10000000   Q7
sgs 26560 0x7F # 01111111   Q6
sgs 56640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 26560 0x7F # 01111111   Q6
sgs 77760 0x80 # 10000000   Q7
sgs 26560 0x7F # 01111111   Q6
sgs 56640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 26560 0x7F # 01111111   Q6
sgs 77760 0x80 # 10000000   Q7
sgs 26560 0x7F # 01111111   Q6
sgs 56640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 26560 0x7F # 01111111   Q6
sgs 71040 0x80 # 10000000   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p5  (24 entries, util 17.1600 %)

```
sgs 17600 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 19840 0x7F # 01111111   Q6
sgs 19200 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 10880 0x3F # 00111111   BE
sgs 46080 0x40 # 01000000   Q6
sgs 61440 0xBF # 10111111   Q7
sgs 17600 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 19840 0x7F # 01111111   Q6
sgs 16000 0xBF # 10111111   Q7
sgs 72640 0x80 # 10000000   Q7
sgs 61440 0xBF # 10111111   Q7
sgs 17600 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 19840 0x7F # 01111111   Q6
sgs 19200 0xBF # 10111111   Q7
sgs 69440 0x80 # 10000000   Q7
sgs 61440 0xBF # 10111111   Q7
sgs 17600 0x7F # 01111111   Q6
sgs 103360 0x40 # 01000000   Q6
sgs 29120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (19 entries, util 28.0800 %)

```
sgs 30400 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 52800 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 29440 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
sgs 30400 0x7F # 01111111   Q6
sgs 94720 0x80 # 10000000   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 30400 0x7F # 01111111   Q6
sgs 94720 0x80 # 10000000   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 30400 0x7F # 01111111   Q6
sgs 64320 0x80 # 10000000   Q7
sgs 55360 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p5  (12 entries, util 6.2400 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 31680 0x7F # 01111111   Q6
sgs 200000 0x40 # 01000000   Q6
sgs 56000 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 44160 0x7F # 01111111   Q6
sgs 155840 0x40 # 01000000   Q6
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p4  (13 entries, util 12.4800 %)

```
sgs 60480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24000 0xBF # 10111111   Q7
sgs 208640 0x40 # 01000000   Q6
sgs 44480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 60480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24000 0xBF # 10111111   Q7
sgs 148160 0x40 # 01000000   Q6
sgs 55040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (24 entries, util 29.6400 %)

```
sgs 13440 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 28160 0x7F # 01111111   Q6
sgs 76160 0x80 # 10000000   Q7
sgs 19840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 13440 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 28160 0x7F # 01111111   Q6
sgs 76160 0x80 # 10000000   Q7
sgs 19840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 13440 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 28160 0x7F # 01111111   Q6
sgs 76160 0x80 # 10000000   Q7
sgs 19840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 13440 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 28160 0x7F # 01111111   Q6
sgs 62720 0x80 # 10000000   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (12 entries, util 6.2400 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 41280 0x7F # 01111111   Q6
sgs 200000 0x40 # 01000000   Q6
sgs 46400 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 53760 0x7F # 01111111   Q6
sgs 146240 0x40 # 01000000   Q6
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p5  (19 entries, util 28.0800 %)

```
sgs 25280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 49600 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 29760 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 57920 0xBF # 10111111   Q7
sgs 25280 0x7F # 01111111   Q6
sgs 94720 0x80 # 10000000   Q7
sgs 30080 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 25280 0x7F # 01111111   Q6
sgs 94720 0x80 # 10000000   Q7
sgs 30080 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 25280 0x7F # 01111111   Q6
sgs 69440 0x80 # 10000000   Q7
sgs 55360 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p4  (28 entries, util 29.6400 %)

```
sgs 20160 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 17280 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 74560 0x80 # 10000000   Q7
sgs 13120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 17280 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 74560 0x80 # 10000000   Q7
sgs 13120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 17280 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 74560 0x80 # 10000000   Q7
sgs 13120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 17280 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 54400 0x80 # 10000000   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (13 entries, util 12.4800 %)

```
sgs 55360 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 19520 0xBF # 10111111   Q7
sgs 213120 0x40 # 01000000   Q6
sgs 49600 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 55360 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 19520 0xBF # 10111111   Q7
sgs 157760 0x40 # 01000000   Q6
sgs 55040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (21 entries, util 28.0800 %)

```
sgs 20160 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 17280 0x7F # 01111111   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 24320 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 21760 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 94720 0x80 # 10000000   Q7
sgs 35200 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 94720 0x80 # 10000000   Q7
sgs 35200 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 74560 0x80 # 10000000   Q7
sgs 55360 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p5  (14 entries, util 6.2400 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 13440 0xBF # 10111111   Q7
sgs 200000 0x40 # 01000000   Q6
sgs 36800 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 13440 0xBF # 10111111   Q7
sgs 136640 0x40 # 01000000   Q6
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p2  (25 entries, util 35.8800 %)

```
sgs 26880 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 31360 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 2240 0x3F # 00111111   BE
sgs 73280 0x40 # 01000000   Q6
sgs 41280 0xBF # 10111111   Q7
sgs 26880 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 31360 0xBF # 10111111   Q7
sgs 88000 0x80 # 10000000   Q7
sgs 41280 0xBF # 10111111   Q7
sgs 26880 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 31360 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 2240 0x3F # 00111111   BE
sgs 73280 0x40 # 01000000   Q6
sgs 41280 0xBF # 10111111   Q7
sgs 26880 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 31360 0xBF # 10111111   Q7
sgs 61120 0x80 # 10000000   Q7
sgs 18240 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p4  (14 entries, util 12.4800 %)

```
sgs 42560 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 22720 0xBF # 10111111   Q7
sgs 209920 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 42560 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 22720 0xBF # 10111111   Q7
sgs 167360 0x40 # 01000000   Q6
sgs 55040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (18 entries, util 28.0800 %)

```
sgs 5120 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 32320 0x7F # 01111111   Q6
sgs 20800 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 18880 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 35520 0x7F # 01111111   Q6
sgs 55040 0xBF # 10111111   Q7
sgs 94720 0x80 # 10000000   Q7
sgs 50240 0x7F # 01111111   Q6
sgs 55040 0xBF # 10111111   Q7
sgs 94720 0x80 # 10000000   Q7
sgs 50240 0x7F # 01111111   Q6
sgs 55040 0xBF # 10111111   Q7
sgs 89600 0x80 # 10000000   Q7
sgs 55360 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

