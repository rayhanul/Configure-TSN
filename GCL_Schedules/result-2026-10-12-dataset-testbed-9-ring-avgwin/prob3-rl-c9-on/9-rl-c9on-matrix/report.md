# Reconfiguration-free admission (Problem 3)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Frozen schedule W loaded from: **result/result-2026-10-12-dataset-testbed-9-ring-avgwin/rl-c9-on/9-matrix-c9on**

## Admission: W (before) vs. after this run's arrivals

| | admitted | of total |
|---|---|---|
| W (base, unchanged) | 11 | 11 |
| + this run's arrivals | 26 | 39 |

Every arrival admitted here required **zero** window-boundary changes -- see the GCL-entry table below (unchanged from W by construction) and the window-boundary integrity check. No previously-admitted flow was rerouted.

## Arrivals

| id | src->dst | RS(s) size | admitted | route | queue | phi_s (ns) | e2e (ns) | rerouted to make room | reason if rejected |
|---|---|---|---|---|---|---|---|---|---|
| 3 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 | 0 | 42880 | - | - |
| 15 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 12480 | 107200 | - | - |
| 13 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 37440 | 46080 | - | - |
| 18 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 19 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q6 | 24960 | 187520 | - | - |
| 17 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 254400 | 45760 | - | - |
| 2 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q6 | 224960 | 121280 | - | - |
| 5 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q7 | 12480 | 41280 | - | - |
| 11 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 62400 | 95040 | - | - |
| 27 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q7 | 49920 | 120000 | - | - |
| 30 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q6 | 237440 | 27840 | - | - |
| 31 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q7 | 150080 | 32640 | - | - |
| 33 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q6 | 249920 | 154560 | - | - |
| 39 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q7 | 150080 | 27840 | - | - |
| 44 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q7 | 162560 | 207680 | - | - |
| 26 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 87360 | 103040 | - | - |
| 29 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 462400 | 150080 | - | - |
| 32 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q7 | 350080 | 32640 | - | - |
| 40 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q6 | 298240 | 114240 | - | - |
| 41 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q7 | 162560 | 208000 | - | - |
| 43 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 162560 | 220800 | - | - |
| 49 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 22 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q6 | 212480 | 212800 | - | - |
| 23 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 112320 | 140480 | - | - |
| 42 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 266880 | 52800 | - | - |
| 25 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 | 100800 | 92480 | - | - |
| 34 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 37 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 38 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 175040 | 224000 | - | - |
| 46 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 187520 | 280960 | - | - |
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
| sw01-p2 | 19 | 19 | 255 |
| sw01-p4 | 19 | 19 | 255 |
| sw01-p5 | 22 | 22 | 255 |
| sw02-p2 | 29 | 29 | 255 |
| sw02-p4 | 9 | 9 | 255 |
| sw02-p5 | 17 | 17 | 255 |
| sw03-p4 | 24 | 24 | 255 |
| sw03-p5 | 19 | 19 | 255 |
| sw04-p4 | 25 | 25 | 255 |
| sw04-p5 | 9 | 9 | 255 |
| sw05-p4 | 21 | 21 | 255 |
| sw05-p5 | 22 | 22 | 255 |
| sw06-p4 | 9 | 9 | 255 |
| sw06-p5 | 25 | 25 | 255 |
| sw07-p4 | 19 | 19 | 255 |
| sw07-p5 | 22 | 22 | 255 |
| sw08-p2 | 21 | 21 | 255 |
| sw08-p4 | 25 | 25 | 255 |
| sw08-p5 | 19 | 19 | 255 |

## Per-hop windows used by newly admitted flows

| flow | egress port | queue | psi (ns, unchanged) | delta (ns, unchanged) |
|---|---|---|---|---|
| s21(id=3 S3->S2) | S3-p0 | Q7 | 0 | 12480 |
| s21(id=3 S3->S2) | sw01-p4 | Q7 | 6080 | 12480 |
| s21(id=3 S3->S2) | sw03-p5 | Q7 | 12160 | 12480 |
| s21(id=3 S3->S2) | sw05-p4 | Q7 | 18240 | 12480 |
| s21(id=3 S3->S2) | sw07-p5 | Q7 | 24320 | 12480 |
| s21(id=3 S3->S2) | sw08-p2 | Q7 | 30400 | 12480 |
| s25(id=15 S2->S1) | S2-p0 | Q7 | 12480 | 12480 |
| s25(id=15 S2->S1) | sw08-p4 | Q7 | 42560 | 12480 |
| s25(id=15 S2->S1) | sw06-p5 | Q7 | 50880 | 12480 |
| s25(id=15 S2->S1) | sw04-p4 | Q7 | 59200 | 12480 |
| s25(id=15 S2->S1) | sw02-p2 | Q7 | 107200 | 12480 |
| s24(id=13 S2->S3) | S2-p0 | Q7 | 37440 | 12480 |
| s24(id=13 S2->S3) | sw08-p5 | Q7 | 44160 | 12480 |
| s24(id=13 S2->S3) | sw07-p4 | Q7 | 50880 | 12480 |
| s24(id=13 S2->S3) | sw05-p5 | Q7 | 57600 | 12480 |
| s24(id=13 S2->S3) | sw03-p4 | Q7 | 64320 | 12480 |
| s24(id=13 S2->S3) | sw01-p2 | Q7 | 71040 | 12480 |
| s28(id=19 S3->S2) | S3-p0 | Q6 | 24960 | 12480 |
| s28(id=19 S3->S2) | sw01-p4 | Q6 | 31680 | 12480 |
| s28(id=19 S3->S2) | sw03-p5 | Q6 | 116480 | 12480 |
| s28(id=19 S3->S2) | sw05-p4 | Q6 | 124800 | 12480 |
| s28(id=19 S3->S2) | sw07-p5 | Q6 | 133120 | 12480 |
| s28(id=19 S3->S2) | sw08-p2 | Q6 | 200000 | 12480 |
| s26(id=17 S2->S1) | S2-p0 | Q7 | 254400 | 12480 |
| s26(id=17 S2->S1) | sw08-p4 | Q7 | 262720 | 12480 |
| s26(id=17 S2->S1) | sw06-p5 | Q7 | 271040 | 12480 |
| s26(id=17 S2->S1) | sw04-p4 | Q7 | 279360 | 12480 |
| s26(id=17 S2->S1) | sw02-p2 | Q7 | 287680 | 12480 |
| s20(id=2 S3->S2) | S3-p0 | Q6 | 224960 | 12480 |
| s20(id=2 S3->S2) | sw01-p4 | Q6 | 300160 | 12480 |
| s20(id=2 S3->S2) | sw03-p5 | Q6 | 305280 | 12480 |
| s20(id=2 S3->S2) | sw05-p4 | Q6 | 310400 | 12480 |
| s20(id=2 S3->S2) | sw07-p5 | Q6 | 315520 | 12480 |
| s20(id=2 S3->S2) | sw08-p2 | Q6 | 333760 | 12480 |
| s22(id=5 S1->S3) | S1-p0 | Q7 | 12480 | 12480 |
| s22(id=5 S1->S3) | sw02-p5 | Q7 | 23040 | 12480 |
| s22(id=5 S1->S3) | sw01-p2 | Q7 | 41280 | 12480 |
| s23(id=11 S2->S1) | S2-p0 | Q7 | 62400 | 12480 |
| s23(id=11 S2->S1) | sw08-p4 | Q7 | 82240 | 12480 |
| s23(id=11 S2->S1) | sw06-p5 | Q7 | 90560 | 12480 |
| s23(id=11 S2->S1) | sw04-p4 | Q7 | 138240 | 12480 |
| s23(id=11 S2->S1) | sw02-p2 | Q7 | 144960 | 12480 |
| s35(id=27 S3->S1) | S3-p0 | Q7 | 49920 | 12480 |
| s35(id=27 S3->S1) | sw01-p5 | Q7 | 150080 | 12480 |
| s35(id=27 S3->S1) | sw02-p2 | Q7 | 157440 | 12480 |
| s38(id=30 S3->S1) | S3-p0 | Q6 | 237440 | 12480 |
| s38(id=30 S3->S1) | sw01-p5 | Q6 | 245120 | 12480 |
| s38(id=30 S3->S1) | sw02-p2 | Q6 | 252800 | 12480 |
| s39(id=31 S3->S1) | S3-p0 | Q7 | 150080 | 12480 |
| s39(id=31 S3->S1) | sw01-p5 | Q7 | 162560 | 12480 |
| s39(id=31 S3->S1) | sw02-p2 | Q7 | 170240 | 12480 |
| s41(id=33 S3->S1) | S3-p0 | Q6 | 249920 | 12480 |
| s41(id=33 S3->S1) | sw01-p5 | Q6 | 257600 | 12480 |
| s41(id=33 S3->S1) | sw02-p2 | Q6 | 392000 | 12480 |
| s47(id=39 S1->S3) | S1-p0 | Q7 | 150080 | 12480 |
| s47(id=39 S1->S3) | sw02-p5 | Q7 | 157760 | 12480 |
| s47(id=39 S1->S3) | sw01-p2 | Q7 | 165440 | 12480 |
| s52(id=44 S3->S1) | S3-p0 | Q7 | 162560 | 12480 |
| s52(id=44 S3->S1) | sw01-p5 | Q7 | 350080 | 12480 |
| s52(id=44 S3->S1) | sw02-p2 | Q7 | 357760 | 12480 |
| s34(id=26 S2->S3) | S2-p0 | Q7 | 87360 | 12480 |
| s34(id=26 S2->S3) | sw08-p5 | Q7 | 150080 | 12480 |
| s34(id=26 S2->S3) | sw07-p4 | Q7 | 156160 | 12480 |
| s34(id=26 S2->S3) | sw05-p5 | Q7 | 162240 | 12480 |
| s34(id=26 S2->S3) | sw03-p4 | Q7 | 168320 | 12480 |
| s34(id=26 S2->S3) | sw01-p2 | Q7 | 177920 | 12480 |
| s37(id=29 S2->S3) | S2-p0 | Q6 | 462400 | 12480 |
| s37(id=29 S2->S3) | sw08-p5 | Q6 | 512960 | 12480 |
| s37(id=29 S2->S3) | sw07-p4 | Q6 | 520640 | 12480 |
| s37(id=29 S2->S3) | sw05-p5 | Q6 | 528320 | 12480 |
| s37(id=29 S2->S3) | sw03-p4 | Q6 | 536000 | 12480 |
| s37(id=29 S2->S3) | sw01-p2 | Q6 | 600000 | 12480 |
| s40(id=32 S3->S1) | S3-p0 | Q7 | 350080 | 12480 |
| s40(id=32 S3->S1) | sw01-p5 | Q7 | 362560 | 12480 |
| s40(id=32 S3->S1) | sw02-p2 | Q7 | 370240 | 12480 |
| s48(id=40 S3->S2) | S3-p0 | Q6 | 298240 | 12480 |
| s48(id=40 S3->S2) | sw01-p4 | Q6 | 312640 | 12480 |
| s48(id=40 S3->S2) | sw03-p5 | Q6 | 320960 | 12480 |
| s48(id=40 S3->S2) | sw05-p4 | Q6 | 329280 | 12480 |
| s48(id=40 S3->S2) | sw07-p5 | Q6 | 337600 | 12480 |
| s48(id=40 S3->S2) | sw08-p2 | Q6 | 400000 | 12480 |
| s49(id=41 S1->S3) | S1-p0 | Q7 | 162560 | 12480 |
| s49(id=41 S1->S3) | sw02-p5 | Q7 | 184640 | 12480 |
| s49(id=41 S1->S3) | sw01-p2 | Q7 | 358080 | 12480 |
| s51(id=43 S2->S3) | S2-p0 | Q7 | 162560 | 12480 |
| s51(id=43 S2->S3) | sw08-p5 | Q7 | 167680 | 12480 |
| s51(id=43 S2->S3) | sw07-p4 | Q7 | 172800 | 12480 |
| s51(id=43 S2->S3) | sw05-p5 | Q7 | 177920 | 12480 |
| s51(id=43 S2->S3) | sw03-p4 | Q7 | 365760 | 12480 |
| s51(id=43 S2->S3) | sw01-p2 | Q7 | 370880 | 12480 |
| s30(id=22 S1->S2) | S1-p0 | Q6 | 212480 | 12480 |
| s30(id=22 S1->S2) | sw02-p4 | Q6 | 218560 | 12480 |
| s30(id=22 S1->S2) | sw04-p5 | Q6 | 224640 | 12480 |
| s30(id=22 S1->S2) | sw06-p4 | Q6 | 406720 | 12480 |
| s30(id=22 S1->S2) | sw08-p2 | Q6 | 412800 | 12480 |
| s31(id=23 S2->S1) | S2-p0 | Q6 | 112320 | 12480 |
| s31(id=23 S2->S1) | sw08-p4 | Q6 | 215360 | 12480 |
| s31(id=23 S2->S1) | sw06-p5 | Q6 | 223680 | 12480 |
| s31(id=23 S2->S1) | sw04-p4 | Q6 | 232000 | 12480 |
| s31(id=23 S2->S1) | sw02-p2 | Q6 | 240320 | 12480 |
| s50(id=42 S2->S1) | S2-p0 | Q7 | 266880 | 12480 |
| s50(id=42 S2->S1) | sw08-p4 | Q7 | 282240 | 12480 |
| s50(id=42 S2->S1) | sw06-p5 | Q7 | 290560 | 12480 |
| s50(id=42 S2->S1) | sw04-p4 | Q7 | 298880 | 12480 |
| s50(id=42 S2->S1) | sw02-p2 | Q7 | 307200 | 12480 |
| s33(id=25 S3->S2) | S3-p0 | Q7 | 100800 | 12480 |
| s33(id=25 S3->S2) | sw01-p4 | Q7 | 150080 | 12480 |
| s33(id=25 S3->S2) | sw03-p5 | Q7 | 157760 | 12480 |
| s33(id=25 S3->S2) | sw05-p4 | Q7 | 165440 | 12480 |
| s33(id=25 S3->S2) | sw07-p5 | Q7 | 173120 | 12480 |
| s33(id=25 S3->S2) | sw08-p2 | Q7 | 180800 | 12480 |
| s46(id=38 S2->S3) | S2-p0 | Q7 | 175040 | 12480 |
| s46(id=38 S2->S3) | sw08-p5 | Q7 | 183360 | 12480 |
| s46(id=38 S2->S3) | sw07-p4 | Q7 | 191680 | 12480 |
| s46(id=38 S2->S3) | sw05-p5 | Q7 | 367040 | 12480 |
| s46(id=38 S2->S3) | sw03-p4 | Q7 | 378240 | 12480 |
| s46(id=38 S2->S3) | sw01-p2 | Q7 | 386560 | 12480 |
| s54(id=46 S2->S3) | S2-p0 | Q7 | 187520 | 12480 |
| s54(id=46 S2->S3) | sw08-p5 | Q7 | 350080 | 12480 |
| s54(id=46 S2->S3) | sw07-p4 | Q7 | 366080 | 12480 |
| s54(id=46 S2->S3) | sw05-p5 | Q7 | 379520 | 12480 |
| s54(id=46 S2->S3) | sw03-p4 | Q7 | 449920 | 12480 |
| s54(id=46 S2->S3) | sw01-p2 | Q7 | 456000 | 12480 |

## Constraint check

- C1-C7, C9: OK
- window-boundary integrity (no window's psi/delta changed anywhere): OK

## GCL per egress port

### sw01-p2  (19 entries, util 35.8800 %)

```
sgs 15360 0x7F # 01111111   Q6
sgs 25280 0x40 # 01000000   Q6
sgs 640 0x3F # 00111111   BE
sgs 14720 0x80 # 10000000   Q7
sgs 44160 0xBF # 10111111   Q7
sgs 13120 0x7F # 01111111   Q6
sgs 44800 0x40 # 01000000   Q6
sgs 41920 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 142720 0x40 # 01000000   Q6
sgs 41920 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 25280 0x40 # 01000000   Q6
sgs 640 0x3F # 00111111   BE
sgs 116800 0x80 # 10000000   Q7
sgs 41920 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 127360 0x40 # 01000000   Q6
sgs 57280 0xBF # 10111111   Q7
```

### sw01-p4  (19 entries, util 17.1600 %)

```
sgs 6080 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 31360 0x7F # 01111111   Q6
sgs 45760 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 41920 0x7F # 01111111   Q6
sgs 56000 0xBF # 10111111   Q7
sgs 68800 0x80 # 10000000   Q7
sgs 25280 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 56000 0xBF # 10111111   Q7
sgs 68800 0x80 # 10000000   Q7
sgs 25280 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 56000 0xBF # 10111111   Q7
sgs 62720 0x80 # 10000000   Q7
sgs 31360 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p5  (22 entries, util 21.8400 %)

```
sgs 20160 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 20480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 2880 0x3F # 00111111   BE
sgs 62720 0x40 # 01000000   Q6
sgs 18880 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 111040 0x40 # 01000000   Q6
sgs 18880 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 20480 0x7F # 01111111   Q6
sgs 78080 0x80 # 10000000   Q7
sgs 18880 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 90880 0x40 # 01000000   Q6
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (29 entries, util 46.8000 %)

```
sgs 27840 0x7F # 01111111   Q6
sgs 30080 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 3840 0x3F # 00111111   BE
sgs 25280 0x40 # 01000000   Q6
sgs 7360 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 4480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 8320 0x3F # 00111111   BE
sgs 47040 0x80 # 10000000   Q7
sgs 35840 0x7F # 01111111   Q6
sgs 43520 0x40 # 01000000   Q6
sgs 35840 0xBF # 10111111   Q7
sgs 84800 0x80 # 10000000   Q7
sgs 35840 0x7F # 01111111   Q6
sgs 30080 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 7360 0x3F # 00111111   BE
sgs 84800 0x80 # 10000000   Q7
sgs 35840 0x7F # 01111111   Q6
sgs 43520 0x40 # 01000000   Q6
sgs 35840 0xBF # 10111111   Q7
sgs 56960 0x80 # 10000000   Q7
sgs 35840 0xBF # 10111111   Q7
```

### sw02-p4  (9 entries, util 4.6800 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 18560 0x7F # 01111111   Q6
sgs 506560 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p5  (17 entries, util 14.0400 %)

```
sgs 7680 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 2880 0x3F # 00111111   BE
sgs 77760 0x80 # 10000000   Q7
sgs 49280 0x7F # 01111111   Q6
sgs 57600 0xBF # 10111111   Q7
sgs 93120 0x40 # 01000000   Q6
sgs 49280 0x7F # 01111111   Q6
sgs 57600 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 2880 0x3F # 00111111   BE
sgs 77760 0x80 # 10000000   Q7
sgs 49280 0x7F # 01111111   Q6
sgs 57600 0xBF # 10111111   Q7
sgs 85440 0x40 # 01000000   Q6
sgs 56960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (24 entries, util 21.8400 %)

```
sgs 20480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 16960 0x7F # 01111111   Q6
sgs 14400 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 28800 0xBF # 10111111   Q7
sgs 22720 0x40 # 01000000   Q6
sgs 21760 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 107840 0x40 # 01000000   Q6
sgs 21760 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 16960 0x7F # 01111111   Q6
sgs 14400 0xBF # 10111111   Q7
sgs 64000 0x80 # 10000000   Q7
sgs 21760 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 87360 0x40 # 01000000   Q6
sgs 42240 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p5  (19 entries, util 17.1600 %)

```
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0x7F # 01111111   Q6
sgs 54080 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 33600 0x7F # 01111111   Q6
sgs 62080 0xBF # 10111111   Q7
sgs 68800 0x80 # 10000000   Q7
sgs 19200 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 62080 0xBF # 10111111   Q7
sgs 68800 0x80 # 10000000   Q7
sgs 19200 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 62080 0xBF # 10111111   Q7
sgs 56640 0x80 # 10000000   Q7
sgs 31360 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p4  (25 entries, util 24.9600 %)

```
sgs 40320 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 24640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 8960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 6720 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 7680 0x3F # 00111111   BE
sgs 93760 0x80 # 10000000   Q7
sgs 17920 0x7F # 01111111   Q6
sgs 48960 0xBF # 10111111   Q7
sgs 74560 0x80 # 10000000   Q7
sgs 26560 0xBF # 10111111   Q7
sgs 40320 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 24640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 8960 0x3F # 00111111   BE
sgs 133120 0x80 # 10000000   Q7
sgs 17920 0x7F # 01111111   Q6
sgs 48960 0xBF # 10111111   Q7
sgs 34240 0x80 # 10000000   Q7
sgs 16960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (9 entries, util 4.6800 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 24640 0x7F # 01111111   Q6
sgs 500480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (21 entries, util 17.1600 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 19200 0x7F # 01111111   Q6
sgs 62400 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 18240 0x7F # 01111111   Q6
sgs 87680 0x80 # 10000000   Q7
sgs 44160 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 18240 0x7F # 01111111   Q6
sgs 87680 0x80 # 10000000   Q7
sgs 44160 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 18240 0x7F # 01111111   Q6
sgs 69440 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p5  (22 entries, util 21.8400 %)

```
sgs 15360 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 29760 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 27840 0xBF # 10111111   Q7
sgs 25280 0x40 # 01000000   Q6
sgs 26880 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 107840 0x40 # 01000000   Q6
sgs 26880 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 29760 0x7F # 01111111   Q6
sgs 65600 0x80 # 10000000   Q7
sgs 26880 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 92480 0x40 # 01000000   Q6
sgs 42240 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p4  (9 entries, util 4.6800 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 494400 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (25 entries, util 24.9600 %)

```
sgs 35200 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 21440 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 8960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 8960 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 7040 0x3F # 00111111   BE
sgs 92160 0x80 # 10000000   Q7
sgs 26240 0x7F # 01111111   Q6
sgs 40640 0xBF # 10111111   Q7
sgs 77760 0x80 # 10000000   Q7
sgs 31680 0xBF # 10111111   Q7
sgs 35200 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 21440 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 8960 0x3F # 00111111   BE
sgs 133120 0x80 # 10000000   Q7
sgs 26240 0x7F # 01111111   Q6
sgs 40640 0xBF # 10111111   Q7
sgs 42560 0x80 # 10000000   Q7
sgs 16960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (19 entries, util 21.8400 %)

```
sgs 10240 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 28160 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 26880 0xBF # 10111111   Q7
sgs 27840 0x40 # 01000000   Q6
sgs 32000 0x7F # 01111111   Q6
sgs 60160 0xBF # 10111111   Q7
sgs 107840 0x40 # 01000000   Q6
sgs 32000 0x7F # 01111111   Q6
sgs 60160 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 28160 0x7F # 01111111   Q6
sgs 67200 0x80 # 10000000   Q7
sgs 32000 0x7F # 01111111   Q6
sgs 60160 0xBF # 10111111   Q7
sgs 97600 0x40 # 01000000   Q6
sgs 42240 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p5  (22 entries, util 17.1600 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 11840 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 16960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 24320 0x7F # 01111111   Q6
sgs 87680 0x80 # 10000000   Q7
sgs 38080 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 24320 0x7F # 01111111   Q6
sgs 87680 0x80 # 10000000   Q7
sgs 38080 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 24320 0x7F # 01111111   Q6
sgs 63360 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p2  (21 entries, util 21.8400 %)

```
sgs 30400 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 6400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 21760 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 32960 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 58560 0xBF # 10111111   Q7
sgs 30400 0x7F # 01111111   Q6
sgs 103360 0x80 # 10000000   Q7
sgs 16320 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 30400 0x7F # 01111111   Q6
sgs 103360 0x80 # 10000000   Q7
sgs 16320 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 30400 0x7F # 01111111   Q6
sgs 72960 0x80 # 10000000   Q7
sgs 46720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p4  (25 entries, util 24.9600 %)

```
sgs 30080 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 18240 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 8960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 11200 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 6400 0x3F # 00111111   BE
sgs 90560 0x80 # 10000000   Q7
sgs 34560 0x7F # 01111111   Q6
sgs 32320 0xBF # 10111111   Q7
sgs 80960 0x80 # 10000000   Q7
sgs 36800 0xBF # 10111111   Q7
sgs 30080 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 18240 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 8960 0x3F # 00111111   BE
sgs 133120 0x80 # 10000000   Q7
sgs 34560 0x7F # 01111111   Q6
sgs 32320 0xBF # 10111111   Q7
sgs 50880 0x80 # 10000000   Q7
sgs 16960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (19 entries, util 21.8400 %)

```
sgs 5120 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 26560 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 25920 0xBF # 10111111   Q7
sgs 30400 0x40 # 01000000   Q6
sgs 37120 0x7F # 01111111   Q6
sgs 55040 0xBF # 10111111   Q7
sgs 107840 0x40 # 01000000   Q6
sgs 37120 0x7F # 01111111   Q6
sgs 55040 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 26560 0x7F # 01111111   Q6
sgs 68800 0x80 # 10000000   Q7
sgs 37120 0x7F # 01111111   Q6
sgs 55040 0xBF # 10111111   Q7
sgs 102720 0x40 # 01000000   Q6
sgs 42240 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

