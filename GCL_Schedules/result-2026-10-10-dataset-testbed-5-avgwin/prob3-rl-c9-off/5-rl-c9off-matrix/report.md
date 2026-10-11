# Reconfiguration-free admission (Problem 3)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Frozen schedule W loaded from: **result/result-2026-10-10-dataset-testbed-5-avgwin/rl-c9-off/5-matrix-c9off**

## Admission: W (before) vs. after this run's arrivals

| | admitted | of total |
|---|---|---|
| W (base, unchanged) | 10 | 10 |
| + this run's arrivals | 15 | 40 |

Every arrival admitted here required **zero** window-boundary changes -- see the GCL-entry table below (unchanged from W by construction) and the window-boundary integrity check. No previously-admitted flow was rerouted.

## Arrivals

| id | src->dst | RS(s) size | admitted | route | queue | phi_s (ns) | e2e (ns) | rerouted to make room | reason if rejected |
|---|---|---|---|---|---|---|---|---|---|
| 8 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q6 | 0 | 145600 | - | - |
| 14 | S1->S3 | - | yes | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 12480 | 162880 | - | - |
| 15 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 12480 | 95680 | - | - |
| 20 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 18 | S1->S3 | - | yes | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 49920 | 148480 | - | - |
| 6 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 24960 | 100480 | - | - |
| 7 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q6 | 24960 | 157120 | - | - |
| 11 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 225280 | 95680 | - | - |
| 1 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q6 | 49920 | 237760 | - | - |
| 4 | S1->S3 | - | yes | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 74880 | 176320 | - | - |
| 36 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 42 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 50 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 479360 | 79040 | - | - |
| 30 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 37 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 22 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q7 | 225280 | 253760 | - | - |
| 28 | S1->S3 | - | yes | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 465600 | 145600 | - | - |
| 31 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q7 | 238080 | 257600 | - | - |
| 43 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q7 | 250880 | 428160 | - | - |
| 45 | S1->S3 | - | yes | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 225280 | 162880 | - | - |
| 21 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 25 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 24 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 33 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 35 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 39 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 48 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 26 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 29 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 34 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 23 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 38 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 46 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 49 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 41 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 44 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 27 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 32 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 40 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 47 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |

## Per-port GCL entries (should equal W exactly)

| port | W entries | after arrivals | GCL_size |
|---|---|---|---|
| sw01-p2 | 39 | 39 | 255 |
| sw01-p4 | 24 | 24 | 255 |
| sw02-p2 | 22 | 22 | 255 |
| sw02-p4 | 28 | 28 | 255 |
| sw03-p4 | 39 | 39 | 255 |
| sw03-p5 | 25 | 25 | 255 |
| sw04-p4 | 22 | 22 | 255 |
| sw04-p5 | 29 | 29 | 255 |
| sw05-p4 | 21 | 21 | 255 |
| sw05-p5 | 35 | 35 | 255 |
| sw06-p4 | 29 | 29 | 255 |
| sw06-p5 | 21 | 21 | 255 |
| sw07-p4 | 35 | 35 | 255 |
| sw07-p5 | 25 | 25 | 255 |
| sw08-p2 | 33 | 33 | 255 |
| sw08-p4 | 21 | 21 | 255 |
| sw08-p5 | 38 | 38 | 255 |

## Per-hop windows used by newly admitted flows

| flow | egress port | queue | psi (ns, unchanged) | delta (ns, unchanged) |
|---|---|---|---|---|
| s24(id=8 S3->S1) | S3-p0 | Q6 | 0 | 12480 |
| s24(id=8 S3->S1) | sw01-p4 | Q6 | 16640 | 12480 |
| s24(id=8 S3->S1) | sw03-p5 | Q6 | 33280 | 12480 |
| s24(id=8 S3->S1) | sw05-p4 | Q6 | 49920 | 12480 |
| s24(id=8 S3->S1) | sw07-p5 | Q6 | 66560 | 12480 |
| s24(id=8 S3->S1) | sw08-p4 | Q6 | 83200 | 12480 |
| s24(id=8 S3->S1) | sw06-p5 | Q6 | 99840 | 12480 |
| s24(id=8 S3->S1) | sw04-p4 | Q6 | 116480 | 12480 |
| s24(id=8 S3->S1) | sw02-p2 | Q6 | 133120 | 12480 |
| s26(id=14 S1->S3) | S1-p0 | Q6 | 12480 | 12480 |
| s26(id=14 S1->S3) | sw02-p4 | Q6 | 29120 | 12480 |
| s26(id=14 S1->S3) | sw04-p5 | Q6 | 46080 | 12480 |
| s26(id=14 S1->S3) | sw06-p4 | Q6 | 63040 | 12480 |
| s26(id=14 S1->S3) | sw08-p5 | Q6 | 95040 | 12480 |
| s26(id=14 S1->S3) | sw07-p4 | Q6 | 112000 | 12480 |
| s26(id=14 S1->S3) | sw05-p5 | Q6 | 128960 | 12480 |
| s26(id=14 S1->S3) | sw03-p4 | Q6 | 145920 | 12480 |
| s26(id=14 S1->S3) | sw01-p2 | Q6 | 162880 | 12480 |
| s27(id=15 S2->S3) | S2-p0 | Q7 | 12480 | 12480 |
| s27(id=15 S2->S3) | sw08-p5 | Q7 | 29120 | 12480 |
| s27(id=15 S2->S3) | sw07-p4 | Q7 | 45760 | 12480 |
| s27(id=15 S2->S3) | sw05-p5 | Q7 | 62400 | 12480 |
| s27(id=15 S2->S3) | sw03-p4 | Q7 | 79040 | 12480 |
| s27(id=15 S2->S3) | sw01-p2 | Q7 | 95680 | 12480 |
| s28(id=18 S1->S3) | S1-p0 | Q7 | 49920 | 12480 |
| s28(id=18 S1->S3) | sw02-p4 | Q7 | 69440 | 12480 |
| s28(id=18 S1->S3) | sw04-p5 | Q7 | 86080 | 12480 |
| s28(id=18 S1->S3) | sw06-p4 | Q7 | 102720 | 12480 |
| s28(id=18 S1->S3) | sw08-p5 | Q7 | 119360 | 12480 |
| s28(id=18 S1->S3) | sw07-p4 | Q7 | 136000 | 12480 |
| s28(id=18 S1->S3) | sw05-p5 | Q7 | 152640 | 12480 |
| s28(id=18 S1->S3) | sw03-p4 | Q7 | 169280 | 12480 |
| s28(id=18 S1->S3) | sw01-p2 | Q7 | 185920 | 12480 |
| s22(id=6 S2->S3) | S2-p0 | Q6 | 24960 | 12480 |
| s22(id=6 S2->S3) | sw08-p5 | Q6 | 42560 | 12480 |
| s22(id=6 S2->S3) | sw07-p4 | Q6 | 60160 | 12480 |
| s22(id=6 S2->S3) | sw05-p5 | Q6 | 77760 | 12480 |
| s22(id=6 S2->S3) | sw03-p4 | Q6 | 95360 | 12480 |
| s22(id=6 S2->S3) | sw01-p2 | Q6 | 112960 | 12480 |
| s23(id=7 S3->S2) | S3-p0 | Q6 | 24960 | 12480 |
| s23(id=7 S3->S2) | sw01-p4 | Q6 | 41600 | 12480 |
| s23(id=7 S3->S2) | sw03-p5 | Q6 | 119680 | 12480 |
| s23(id=7 S3->S2) | sw05-p4 | Q6 | 136320 | 12480 |
| s23(id=7 S3->S2) | sw07-p5 | Q6 | 152960 | 12480 |
| s23(id=7 S3->S2) | sw08-p2 | Q6 | 169600 | 12480 |
| s25(id=11 S2->S3) | S2-p0 | Q7 | 225280 | 12480 |
| s25(id=11 S2->S3) | sw08-p5 | Q7 | 241920 | 12480 |
| s25(id=11 S2->S3) | sw07-p4 | Q7 | 258560 | 12480 |
| s25(id=11 S2->S3) | sw05-p5 | Q7 | 275200 | 12480 |
| s25(id=11 S2->S3) | sw03-p4 | Q7 | 291840 | 12480 |
| s25(id=11 S2->S3) | sw01-p2 | Q7 | 308480 | 12480 |
| s20(id=1 S3->S1) | S3-p0 | Q6 | 49920 | 12480 |
| s20(id=1 S3->S1) | sw01-p4 | Q6 | 115840 | 12480 |
| s20(id=1 S3->S1) | sw03-p5 | Q6 | 132480 | 12480 |
| s20(id=1 S3->S1) | sw05-p4 | Q6 | 149120 | 12480 |
| s20(id=1 S3->S1) | sw07-p5 | Q6 | 165760 | 12480 |
| s20(id=1 S3->S1) | sw08-p4 | Q6 | 200000 | 12480 |
| s20(id=1 S3->S1) | sw06-p5 | Q6 | 216640 | 12480 |
| s20(id=1 S3->S1) | sw04-p4 | Q6 | 233280 | 12480 |
| s20(id=1 S3->S1) | sw02-p2 | Q6 | 275200 | 12480 |
| s21(id=4 S1->S3) | S1-p0 | Q7 | 74880 | 12480 |
| s21(id=4 S1->S3) | sw02-p4 | Q7 | 122240 | 12480 |
| s21(id=4 S1->S3) | sw04-p5 | Q7 | 138880 | 12480 |
| s21(id=4 S1->S3) | sw06-p4 | Q7 | 155520 | 12480 |
| s21(id=4 S1->S3) | sw08-p5 | Q7 | 172160 | 12480 |
| s21(id=4 S1->S3) | sw07-p4 | Q7 | 188800 | 12480 |
| s21(id=4 S1->S3) | sw05-p5 | Q7 | 205440 | 12480 |
| s21(id=4 S1->S3) | sw03-p4 | Q7 | 222080 | 12480 |
| s21(id=4 S1->S3) | sw01-p2 | Q7 | 238720 | 12480 |
| s59(id=50 S2->S1) | S2-p0 | Q6 | 479360 | 12480 |
| s59(id=50 S2->S1) | sw08-p4 | Q6 | 496000 | 12480 |
| s59(id=50 S2->S1) | sw06-p5 | Q6 | 512640 | 12480 |
| s59(id=50 S2->S1) | sw04-p4 | Q6 | 529280 | 12480 |
| s59(id=50 S2->S1) | sw02-p2 | Q6 | 545920 | 12480 |
| s31(id=22 S3->S1) | S3-p0 | Q7 | 225280 | 12480 |
| s31(id=22 S3->S1) | sw01-p4 | Q7 | 241920 | 12480 |
| s31(id=22 S3->S1) | sw03-p5 | Q7 | 258560 | 12480 |
| s31(id=22 S3->S1) | sw05-p4 | Q7 | 275200 | 12480 |
| s31(id=22 S3->S1) | sw07-p5 | Q7 | 291840 | 12480 |
| s31(id=22 S3->S1) | sw08-p4 | Q7 | 357440 | 12480 |
| s31(id=22 S3->S1) | sw06-p5 | Q7 | 374080 | 12480 |
| s31(id=22 S3->S1) | sw04-p4 | Q7 | 449920 | 12480 |
| s31(id=22 S3->S1) | sw02-p2 | Q7 | 466560 | 12480 |
| s37(id=28 S1->S3) | S1-p0 | Q7 | 465600 | 12480 |
| s37(id=28 S1->S3) | sw02-p4 | Q7 | 482240 | 12480 |
| s37(id=28 S1->S3) | sw04-p5 | Q7 | 498880 | 12480 |
| s37(id=28 S1->S3) | sw06-p4 | Q7 | 515520 | 12480 |
| s37(id=28 S1->S3) | sw08-p5 | Q7 | 532160 | 12480 |
| s37(id=28 S1->S3) | sw07-p4 | Q7 | 548800 | 12480 |
| s37(id=28 S1->S3) | sw05-p5 | Q7 | 565440 | 12480 |
| s37(id=28 S1->S3) | sw03-p4 | Q7 | 582080 | 12480 |
| s37(id=28 S1->S3) | sw01-p2 | Q7 | 598720 | 12480 |
| s40(id=31 S3->S1) | S3-p0 | Q7 | 238080 | 12480 |
| s40(id=31 S3->S1) | sw01-p4 | Q7 | 254720 | 12480 |
| s40(id=31 S3->S1) | sw03-p5 | Q7 | 271360 | 12480 |
| s40(id=31 S3->S1) | sw05-p4 | Q7 | 288000 | 12480 |
| s40(id=31 S3->S1) | sw07-p5 | Q7 | 353600 | 12480 |
| s40(id=31 S3->S1) | sw08-p4 | Q7 | 370240 | 12480 |
| s40(id=31 S3->S1) | sw06-p5 | Q7 | 449920 | 12480 |
| s40(id=31 S3->S1) | sw04-p4 | Q7 | 466560 | 12480 |
| s40(id=31 S3->S1) | sw02-p2 | Q7 | 483200 | 12480 |
| s52(id=43 S3->S1) | S3-p0 | Q7 | 250880 | 12480 |
| s52(id=43 S3->S1) | sw01-p4 | Q7 | 267520 | 12480 |
| s52(id=43 S3->S1) | sw03-p5 | Q7 | 284160 | 12480 |
| s52(id=43 S3->S1) | sw05-p4 | Q7 | 349760 | 12480 |
| s52(id=43 S3->S1) | sw07-p5 | Q7 | 450240 | 12480 |
| s52(id=43 S3->S1) | sw08-p4 | Q7 | 466880 | 12480 |
| s52(id=43 S3->S1) | sw06-p5 | Q7 | 483520 | 12480 |
| s52(id=43 S3->S1) | sw04-p4 | Q7 | 649920 | 12480 |
| s52(id=43 S3->S1) | sw02-p2 | Q7 | 666560 | 12480 |
| s54(id=45 S1->S3) | S1-p0 | Q6 | 225280 | 12480 |
| s54(id=45 S1->S3) | sw02-p4 | Q6 | 242240 | 12480 |
| s54(id=45 S1->S3) | sw04-p5 | Q6 | 259200 | 12480 |
| s54(id=45 S1->S3) | sw06-p4 | Q6 | 291200 | 12480 |
| s54(id=45 S1->S3) | sw08-p5 | Q6 | 308160 | 12480 |
| s54(id=45 S1->S3) | sw07-p4 | Q6 | 325120 | 12480 |
| s54(id=45 S1->S3) | sw05-p5 | Q6 | 342080 | 12480 |
| s54(id=45 S1->S3) | sw03-p4 | Q6 | 359040 | 12480 |
| s54(id=45 S1->S3) | sw01-p2 | Q6 | 375680 | 12480 |

## Constraint check

- C1-C7, C9: OK
- window-boundary integrity (no window's psi/delta changed anywhere): OK

## GCL per egress port

### sw01-p2  (39 entries, util 35.8800 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 4800 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 20160 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 4800 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 10560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 22080 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 32000 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 31040 0x80 # 10000000   Q7
sgs 23360 0x7F # 01111111   Q6
sgs 12800 0xBF # 10111111   Q7
sgs 84160 0x40 # 01000000   Q6
sgs 36160 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 4800 0x3F # 00111111   BE
sgs 13760 0x40 # 01000000   Q6
sgs 23360 0x7F # 01111111   Q6
sgs 12800 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 10560 0x3F # 00111111   BE
sgs 61120 0x80 # 10000000   Q7
sgs 36160 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 31040 0x80 # 10000000   Q7
sgs 23360 0x7F # 01111111   Q6
sgs 12800 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 24640 0xBF # 10111111   Q7
```

### sw01-p4  (24 entries, util 26.5200 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 32320 0x80 # 10000000   Q7
sgs 47360 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 28800 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 140160 0x80 # 10000000   Q7
sgs 30720 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 115200 0x80 # 10000000   Q7
sgs 30720 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 123520 0x80 # 10000000   Q7
sgs 47360 0xBF # 10111111   Q7
```

### sw02-p2  (22 entries, util 17.1600 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 54080 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 45440 0x40 # 01000000   Q6
sgs 21440 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 25280 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 32960 0x7F # 01111111   Q6
sgs 74240 0x40 # 01000000   Q6
sgs 42560 0x7F # 01111111   Q6
sgs 54080 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 103360 0x40 # 01000000   Q6
sgs 13440 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 32960 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 54400 0xBF # 10111111   Q7
```

### sw02-p4  (28 entries, util 26.5200 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 960 0x3F # 00111111   BE
sgs 33600 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 50880 0x80 # 10000000   Q7
sgs 26880 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 144000 0x40 # 01000000   Q6
sgs 26880 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 960 0x3F # 00111111   BE
sgs 103680 0x80 # 10000000   Q7
sgs 26880 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 127360 0x40 # 01000000   Q6
sgs 43520 0xBF # 10111111   Q7
```

### sw03-p4  (39 entries, util 35.8800 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 3840 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 21120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 4480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 10880 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 22080 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 30720 0x80 # 10000000   Q7
sgs 36160 0x7F # 01111111   Q6
sgs 84480 0x40 # 01000000   Q6
sgs 19520 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 3840 0x3F # 00111111   BE
sgs 14400 0x40 # 01000000   Q6
sgs 36160 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 10880 0x3F # 00111111   BE
sgs 61120 0x80 # 10000000   Q7
sgs 19520 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 30720 0x80 # 10000000   Q7
sgs 36160 0x7F # 01111111   Q6
sgs 17920 0x40 # 01000000   Q6
sgs 36160 0xBF # 10111111   Q7
```

### sw03-p5  (25 entries, util 26.5200 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0xBF # 10111111   Q7
sgs 36800 0x80 # 10000000   Q7
sgs 11520 0x3F # 00111111   BE
sgs 62720 0x40 # 01000000   Q6
sgs 17600 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 136640 0x80 # 10000000   Q7
sgs 17600 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 16320 0xBF # 10111111   Q7
sgs 19520 0x7F # 01111111   Q6
sgs 62720 0x40 # 01000000   Q6
sgs 17600 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 103360 0x80 # 10000000   Q7
sgs 50880 0xBF # 10111111   Q7
```

### sw04-p4  (22 entries, util 17.1600 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 37440 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 45440 0x40 # 01000000   Q6
sgs 38080 0xBF # 10111111   Q7
sgs 58560 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 16320 0x7F # 01111111   Q6
sgs 74240 0x40 # 01000000   Q6
sgs 59200 0x7F # 01111111   Q6
sgs 37440 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 103360 0x40 # 01000000   Q6
sgs 30080 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 16320 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 21120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (29 entries, util 26.5200 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 14080 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 960 0x3F # 00111111   BE
sgs 33600 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 50880 0x80 # 10000000   Q7
sgs 43520 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 143680 0x40 # 01000000   Q6
sgs 43520 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 14080 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 960 0x3F # 00111111   BE
sgs 103680 0x80 # 10000000   Q7
sgs 43520 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 110400 0x40 # 01000000   Q6
sgs 43520 0xBF # 10111111   Q7
```

### sw05-p4  (21 entries, util 26.5200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0xBF # 10111111   Q7
sgs 36800 0x80 # 10000000   Q7
sgs 11520 0x3F # 00111111   BE
sgs 62720 0x40 # 01000000   Q6
sgs 50880 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 136640 0x80 # 10000000   Q7
sgs 50880 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 35840 0x7F # 01111111   Q6
sgs 62720 0x40 # 01000000   Q6
sgs 50880 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 86720 0x80 # 10000000   Q7
sgs 50880 0xBF # 10111111   Q7
```

### sw05-p5  (35 entries, util 35.8800 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 2880 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 22080 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 22080 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 32000 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 30400 0x80 # 10000000   Q7
sgs 36160 0x7F # 01111111   Q6
sgs 84800 0x40 # 01000000   Q6
sgs 36160 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 2880 0x3F # 00111111   BE
sgs 15040 0x40 # 01000000   Q6
sgs 36160 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 61120 0x80 # 10000000   Q7
sgs 36160 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 30400 0x80 # 10000000   Q7
sgs 36160 0x7F # 01111111   Q6
sgs 34880 0x40 # 01000000   Q6
sgs 36160 0xBF # 10111111   Q7
```

### sw06-p4  (29 entries, util 26.5200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 13760 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 960 0x3F # 00111111   BE
sgs 33600 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 50880 0x80 # 10000000   Q7
sgs 43520 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 640 0x3F # 00111111   BE
sgs 143360 0x40 # 01000000   Q6
sgs 43520 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 13760 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 960 0x3F # 00111111   BE
sgs 103680 0x80 # 10000000   Q7
sgs 43520 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 640 0x3F # 00111111   BE
sgs 93440 0x40 # 01000000   Q6
sgs 43520 0xBF # 10111111   Q7
```

### sw06-p5  (21 entries, util 17.1600 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 20800 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 16640 0xBF # 10111111   Q7
sgs 45440 0x40 # 01000000   Q6
sgs 54720 0xBF # 10111111   Q7
sgs 41920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 45440 0xBF # 10111111   Q7
sgs 74240 0x40 # 01000000   Q6
sgs 25920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 20800 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 16640 0xBF # 10111111   Q7
sgs 103360 0x40 # 01000000   Q6
sgs 46720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 37760 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (35 entries, util 35.8800 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 1920 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 23040 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 3840 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 11520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 22080 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 32000 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 30080 0x80 # 10000000   Q7
sgs 36160 0xBF # 10111111   Q7
sgs 85120 0x40 # 01000000   Q6
sgs 36160 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 1920 0x3F # 00111111   BE
sgs 15680 0x40 # 01000000   Q6
sgs 36160 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 11520 0x3F # 00111111   BE
sgs 61120 0x80 # 10000000   Q7
sgs 36160 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 30080 0x80 # 10000000   Q7
sgs 36160 0xBF # 10111111   Q7
sgs 51840 0x40 # 01000000   Q6
sgs 36160 0xBF # 10111111   Q7
```

### sw07-p5  (25 entries, util 26.5200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0x7F # 01111111   Q6
sgs 36800 0x80 # 10000000   Q7
sgs 11520 0x3F # 00111111   BE
sgs 62720 0x40 # 01000000   Q6
sgs 34240 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 136640 0x80 # 10000000   Q7
sgs 34240 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 35840 0x7F # 01111111   Q6
sgs 62720 0x40 # 01000000   Q6
sgs 34240 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 70080 0x80 # 10000000   Q7
sgs 50880 0xBF # 10111111   Q7
```

### sw08-p2  (33 entries, util 24.9600 %)

```
sgs 66560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 16640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 10240 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 84480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 16640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 158400 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 16640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 35840 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 84480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 16640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 91840 0x3F # 00111111   BE
```

### sw08-p4  (21 entries, util 17.1600 %)

```
sgs 54080 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 16640 0xBF # 10111111   Q7
sgs 45440 0x40 # 01000000   Q6
sgs 21440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 25280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 45440 0xBF # 10111111   Q7
sgs 74240 0x40 # 01000000   Q6
sgs 42560 0xBF # 10111111   Q7
sgs 54080 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 16640 0xBF # 10111111   Q7
sgs 103360 0x40 # 01000000   Q6
sgs 13440 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 20160 0x40 # 01000000   Q6
sgs 46720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (38 entries, util 35.8800 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 960 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 24000 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 3520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 11840 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 22080 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 15360 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 29760 0x80 # 10000000   Q7
sgs 36160 0xBF # 10111111   Q7
sgs 85440 0x40 # 01000000   Q6
sgs 19520 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 960 0x3F # 00111111   BE
sgs 16320 0x40 # 01000000   Q6
sgs 36160 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 11840 0x3F # 00111111   BE
sgs 61120 0x80 # 10000000   Q7
sgs 19520 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 29760 0x80 # 10000000   Q7
sgs 36160 0xBF # 10111111   Q7
sgs 68800 0x40 # 01000000   Q6
sgs 36160 0xBF # 10111111   Q7
```

