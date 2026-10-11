# Reconfiguration-free admission (Problem 3)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Frozen schedule W loaded from: **result/result-2026-10-10-dataset-testbed-5-avgwin/heuristic-c9-on/5-matrix-c9on**

## Admission: W (before) vs. after this run's arrivals

| | admitted | of total |
|---|---|---|
| W (base, unchanged) | 10 | 10 |
| + this run's arrivals | 18 | 40 |

Every arrival admitted here required **zero** window-boundary changes -- see the GCL-entry table below (unchanged from W by construction) and the window-boundary integrity check. No previously-admitted flow was rerouted.

## Arrivals

| id | src->dst | RS(s) size | admitted | route | queue | phi_s (ns) | e2e (ns) | rerouted to make room | reason if rejected |
|---|---|---|---|---|---|---|---|---|---|
| 8 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 14 | S1->S3 | - | yes | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 12480 | 200000 | - | - |
| 15 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 20 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 18 | S1->S3 | - | yes | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 100160 | 93120 | - | - |
| 6 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 111040 | 119680 | - | - |
| 7 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 11 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 212480 | 54080 | - | - |
| 1 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q7 | 0 | 289600 | - | - |
| 4 | S1->S3 | - | yes | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 150080 | 246080 | - | - |
| 36 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 42 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 50 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 123520 | 45760 | - | - |
| 30 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 12480 | 105280 | - | - |
| 37 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 311040 | 116800 | - | - |
| 22 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q7 | 157760 | 241920 | - | - |
| 28 | S1->S3 | - | yes | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 449920 | 79040 | - | - |
| 31 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q7 | 170240 | 508800 | - | - |
| 43 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q7 | 182720 | 508800 | - | - |
| 45 | S1->S3 | - | yes | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 550080 | 242880 | - | - |
| 21 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 25 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 24 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 33 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 35 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 224960 | 54080 | - | - |
| 39 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 237440 | 54080 | - | - |
| 48 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 249920 | 54080 | - | - |
| 26 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 29 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 34 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q6 | 74880 | 66240 | - | - |
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
| sw01-p2 | 21 | 21 | 255 |
| sw01-p4 | 21 | 21 | 255 |
| sw02-p2 | 14 | 14 | 255 |
| sw02-p4 | 22 | 22 | 255 |
| sw03-p4 | 22 | 22 | 255 |
| sw03-p5 | 18 | 18 | 255 |
| sw04-p4 | 14 | 14 | 255 |
| sw04-p5 | 25 | 25 | 255 |
| sw05-p4 | 18 | 18 | 255 |
| sw05-p5 | 23 | 23 | 255 |
| sw06-p4 | 24 | 24 | 255 |
| sw06-p5 | 14 | 14 | 255 |
| sw07-p4 | 23 | 23 | 255 |
| sw07-p5 | 18 | 18 | 255 |
| sw08-p2 | 19 | 19 | 255 |
| sw08-p4 | 12 | 12 | 255 |
| sw08-p5 | 23 | 23 | 255 |

## Per-hop windows used by newly admitted flows

| flow | egress port | queue | psi (ns, unchanged) | delta (ns, unchanged) |
|---|---|---|---|---|
| s26(id=14 S1->S3) | S1-p0 | Q6 | 12480 | 12480 |
| s26(id=14 S1->S3) | sw02-p4 | Q6 | 20800 | 12480 |
| s26(id=14 S1->S3) | sw04-p5 | Q6 | 29120 | 12480 |
| s26(id=14 S1->S3) | sw06-p4 | Q6 | 37440 | 12480 |
| s26(id=14 S1->S3) | sw08-p5 | Q6 | 100160 | 12480 |
| s26(id=14 S1->S3) | sw07-p4 | Q6 | 105280 | 12480 |
| s26(id=14 S1->S3) | sw05-p5 | Q6 | 110400 | 12480 |
| s26(id=14 S1->S3) | sw03-p4 | Q6 | 115520 | 12480 |
| s26(id=14 S1->S3) | sw01-p2 | Q6 | 120640 | 12480 |
| s28(id=18 S1->S3) | S1-p0 | Q7 | 100160 | 12480 |
| s28(id=18 S1->S3) | sw02-p4 | Q7 | 107840 | 12480 |
| s28(id=18 S1->S3) | sw04-p5 | Q7 | 115520 | 12480 |
| s28(id=18 S1->S3) | sw06-p4 | Q7 | 123200 | 12480 |
| s28(id=18 S1->S3) | sw08-p5 | Q7 | 150080 | 12480 |
| s28(id=18 S1->S3) | sw07-p4 | Q7 | 157760 | 12480 |
| s28(id=18 S1->S3) | sw05-p5 | Q7 | 165440 | 12480 |
| s28(id=18 S1->S3) | sw03-p4 | Q7 | 173120 | 12480 |
| s28(id=18 S1->S3) | sw01-p2 | Q7 | 180800 | 12480 |
| s22(id=6 S2->S3) | S2-p0 | Q6 | 111040 | 12480 |
| s22(id=6 S2->S3) | sw08-p5 | Q6 | 130560 | 12480 |
| s22(id=6 S2->S3) | sw07-p4 | Q6 | 200000 | 12480 |
| s22(id=6 S2->S3) | sw05-p5 | Q6 | 206080 | 12480 |
| s22(id=6 S2->S3) | sw03-p4 | Q6 | 212160 | 12480 |
| s22(id=6 S2->S3) | sw01-p2 | Q6 | 218240 | 12480 |
| s25(id=11 S2->S3) | S2-p0 | Q7 | 212480 | 12480 |
| s25(id=11 S2->S3) | sw08-p5 | Q7 | 220800 | 12480 |
| s25(id=11 S2->S3) | sw07-p4 | Q7 | 229120 | 12480 |
| s25(id=11 S2->S3) | sw05-p5 | Q7 | 237440 | 12480 |
| s25(id=11 S2->S3) | sw03-p4 | Q7 | 245760 | 12480 |
| s25(id=11 S2->S3) | sw01-p2 | Q7 | 254080 | 12480 |
| s20(id=1 S3->S1) | S3-p0 | Q7 | 0 | 12480 |
| s20(id=1 S3->S1) | sw01-p4 | Q7 | 150080 | 12480 |
| s20(id=1 S3->S1) | sw03-p5 | Q7 | 156160 | 12480 |
| s20(id=1 S3->S1) | sw05-p4 | Q7 | 162240 | 12480 |
| s20(id=1 S3->S1) | sw07-p5 | Q7 | 168320 | 12480 |
| s20(id=1 S3->S1) | sw08-p4 | Q7 | 252160 | 12480 |
| s20(id=1 S3->S1) | sw06-p5 | Q7 | 260480 | 12480 |
| s20(id=1 S3->S1) | sw04-p4 | Q7 | 268800 | 12480 |
| s20(id=1 S3->S1) | sw02-p2 | Q7 | 277120 | 12480 |
| s21(id=4 S1->S3) | S1-p0 | Q7 | 150080 | 12480 |
| s21(id=4 S1->S3) | sw02-p4 | Q7 | 156800 | 12480 |
| s21(id=4 S1->S3) | sw04-p5 | Q7 | 163520 | 12480 |
| s21(id=4 S1->S3) | sw06-p4 | Q7 | 350080 | 12480 |
| s21(id=4 S1->S3) | sw08-p5 | Q7 | 356800 | 12480 |
| s21(id=4 S1->S3) | sw07-p4 | Q7 | 363520 | 12480 |
| s21(id=4 S1->S3) | sw05-p5 | Q7 | 370240 | 12480 |
| s21(id=4 S1->S3) | sw03-p4 | Q7 | 376960 | 12480 |
| s21(id=4 S1->S3) | sw01-p2 | Q7 | 383680 | 12480 |
| s59(id=50 S2->S1) | S2-p0 | Q6 | 123520 | 12480 |
| s59(id=50 S2->S1) | sw08-p4 | Q6 | 131840 | 12480 |
| s59(id=50 S2->S1) | sw06-p5 | Q6 | 140160 | 12480 |
| s59(id=50 S2->S1) | sw04-p4 | Q6 | 148480 | 12480 |
| s59(id=50 S2->S1) | sw02-p2 | Q6 | 156800 | 12480 |
| s39(id=30 S2->S3) | S2-p0 | Q6 | 12480 | 12480 |
| s39(id=30 S2->S3) | sw08-p5 | Q6 | 19200 | 12480 |
| s39(id=30 S2->S3) | sw07-p4 | Q6 | 25920 | 12480 |
| s39(id=30 S2->S3) | sw05-p5 | Q6 | 32640 | 12480 |
| s39(id=30 S2->S3) | sw03-p4 | Q6 | 100160 | 12480 |
| s39(id=30 S2->S3) | sw01-p2 | Q6 | 105280 | 12480 |
| s46(id=37 S2->S3) | S2-p0 | Q6 | 311040 | 12480 |
| s46(id=37 S2->S3) | sw08-p5 | Q6 | 326720 | 12480 |
| s46(id=37 S2->S3) | sw07-p4 | Q6 | 335360 | 12480 |
| s46(id=37 S2->S3) | sw05-p5 | Q6 | 400000 | 12480 |
| s46(id=37 S2->S3) | sw03-p4 | Q6 | 407680 | 12480 |
| s46(id=37 S2->S3) | sw01-p2 | Q6 | 415360 | 12480 |
| s31(id=22 S3->S1) | S3-p0 | Q7 | 157760 | 12480 |
| s31(id=22 S3->S1) | sw01-p4 | Q7 | 162880 | 12480 |
| s31(id=22 S3->S1) | sw03-p5 | Q7 | 168640 | 12480 |
| s31(id=22 S3->S1) | sw05-p4 | Q7 | 174720 | 12480 |
| s31(id=22 S3->S1) | sw07-p5 | Q7 | 366720 | 12480 |
| s31(id=22 S3->S1) | sw08-p4 | Q7 | 371840 | 12480 |
| s31(id=22 S3->S1) | sw06-p5 | Q7 | 376960 | 12480 |
| s31(id=22 S3->S1) | sw04-p4 | Q7 | 382080 | 12480 |
| s31(id=22 S3->S1) | sw02-p2 | Q7 | 387200 | 12480 |
| s37(id=28 S1->S3) | S1-p0 | Q7 | 449920 | 12480 |
| s37(id=28 S1->S3) | sw02-p4 | Q7 | 458240 | 12480 |
| s37(id=28 S1->S3) | sw04-p5 | Q7 | 466560 | 12480 |
| s37(id=28 S1->S3) | sw06-p4 | Q7 | 474880 | 12480 |
| s37(id=28 S1->S3) | sw08-p5 | Q7 | 483200 | 12480 |
| s37(id=28 S1->S3) | sw07-p4 | Q7 | 491520 | 12480 |
| s37(id=28 S1->S3) | sw05-p5 | Q7 | 499840 | 12480 |
| s37(id=28 S1->S3) | sw03-p4 | Q7 | 508160 | 12480 |
| s37(id=28 S1->S3) | sw01-p2 | Q7 | 516480 | 12480 |
| s40(id=31 S3->S1) | S3-p0 | Q7 | 170240 | 12480 |
| s40(id=31 S3->S1) | sw01-p4 | Q7 | 178560 | 12480 |
| s40(id=31 S3->S1) | sw03-p5 | Q7 | 186880 | 12480 |
| s40(id=31 S3->S1) | sw05-p4 | Q7 | 364800 | 12480 |
| s40(id=31 S3->S1) | sw07-p5 | Q7 | 379200 | 12480 |
| s40(id=31 S3->S1) | sw08-p4 | Q7 | 387520 | 12480 |
| s40(id=31 S3->S1) | sw06-p5 | Q7 | 649920 | 12480 |
| s40(id=31 S3->S1) | sw04-p4 | Q7 | 658240 | 12480 |
| s40(id=31 S3->S1) | sw02-p2 | Q7 | 666560 | 12480 |
| s52(id=43 S3->S1) | S3-p0 | Q7 | 182720 | 12480 |
| s52(id=43 S3->S1) | sw01-p4 | Q7 | 350080 | 12480 |
| s52(id=43 S3->S1) | sw03-p5 | Q7 | 361280 | 12480 |
| s52(id=43 S3->S1) | sw05-p4 | Q7 | 377280 | 12480 |
| s52(id=43 S3->S1) | sw07-p5 | Q7 | 458240 | 12480 |
| s52(id=43 S3->S1) | sw08-p4 | Q7 | 649920 | 12480 |
| s52(id=43 S3->S1) | sw06-p5 | Q7 | 662400 | 12480 |
| s52(id=43 S3->S1) | sw04-p4 | Q7 | 670720 | 12480 |
| s52(id=43 S3->S1) | sw02-p2 | Q7 | 679040 | 12480 |
| s54(id=45 S1->S3) | S1-p0 | Q7 | 550080 | 12480 |
| s54(id=45 S1->S3) | sw02-p4 | Q7 | 556160 | 12480 |
| s54(id=45 S1->S3) | sw04-p5 | Q7 | 562240 | 12480 |
| s54(id=45 S1->S3) | sw06-p4 | Q7 | 750080 | 12480 |
| s54(id=45 S1->S3) | sw08-p5 | Q7 | 756160 | 12480 |
| s54(id=45 S1->S3) | sw07-p4 | Q7 | 762240 | 12480 |
| s54(id=45 S1->S3) | sw05-p5 | Q7 | 768320 | 12480 |
| s54(id=45 S1->S3) | sw03-p4 | Q7 | 774400 | 12480 |
| s54(id=45 S1->S3) | sw01-p2 | Q7 | 780480 | 12480 |
| s44(id=35 S2->S3) | S2-p0 | Q7 | 224960 | 12480 |
| s44(id=35 S2->S3) | sw08-p5 | Q7 | 233280 | 12480 |
| s44(id=35 S2->S3) | sw07-p4 | Q7 | 241600 | 12480 |
| s44(id=35 S2->S3) | sw05-p5 | Q7 | 249920 | 12480 |
| s44(id=35 S2->S3) | sw03-p4 | Q7 | 258240 | 12480 |
| s44(id=35 S2->S3) | sw01-p2 | Q7 | 266560 | 12480 |
| s48(id=39 S2->S3) | S2-p0 | Q7 | 237440 | 12480 |
| s48(id=39 S2->S3) | sw08-p5 | Q7 | 245760 | 12480 |
| s48(id=39 S2->S3) | sw07-p4 | Q7 | 254080 | 12480 |
| s48(id=39 S2->S3) | sw05-p5 | Q7 | 262400 | 12480 |
| s48(id=39 S2->S3) | sw03-p4 | Q7 | 270720 | 12480 |
| s48(id=39 S2->S3) | sw01-p2 | Q7 | 279040 | 12480 |
| s57(id=48 S2->S3) | S2-p0 | Q7 | 249920 | 12480 |
| s57(id=48 S2->S3) | sw08-p5 | Q7 | 258240 | 12480 |
| s57(id=48 S2->S3) | sw07-p4 | Q7 | 266560 | 12480 |
| s57(id=48 S2->S3) | sw05-p5 | Q7 | 274880 | 12480 |
| s57(id=48 S2->S3) | sw03-p4 | Q7 | 283200 | 12480 |
| s57(id=48 S2->S3) | sw01-p2 | Q7 | 291520 | 12480 |
| s43(id=34 S3->S1) | S3-p0 | Q6 | 74880 | 12480 |
| s43(id=34 S3->S1) | sw01-p4 | Q6 | 81600 | 12480 |
| s43(id=34 S3->S1) | sw03-p5 | Q6 | 88320 | 12480 |
| s43(id=34 S3->S1) | sw05-p4 | Q6 | 95040 | 12480 |
| s43(id=34 S3->S1) | sw07-p5 | Q6 | 101760 | 12480 |
| s43(id=34 S3->S1) | sw08-p4 | Q6 | 108480 | 12480 |
| s43(id=34 S3->S1) | sw06-p5 | Q6 | 115200 | 12480 |
| s43(id=34 S3->S1) | sw04-p4 | Q6 | 121920 | 12480 |
| s43(id=34 S3->S1) | sw02-p2 | Q6 | 128640 | 12480 |

## Constraint check

- C1-C7, C9: OK
- window-boundary integrity (no window's psi/delta changed anywhere): OK

## GCL per egress port

### sw01-p2  (21 entries, util 42.1200 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 21120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 3840 0x3F # 00111111   BE
sgs 38080 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 48320 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 38720 0xBF # 10111111   Q7
sgs 33600 0x7F # 01111111   Q6
sgs 109440 0x80 # 10000000   Q7
sgs 7040 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 33600 0x7F # 01111111   Q6
sgs 109440 0x80 # 10000000   Q7
sgs 7040 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 33600 0x7F # 01111111   Q6
sgs 75840 0x80 # 10000000   Q7
sgs 40640 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p4  (21 entries, util 20.2800 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0x7F # 01111111   Q6
sgs 94080 0x40 # 01000000   Q6
sgs 8320 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 120960 0x40 # 01000000   Q6
sgs 8320 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0x7F # 01111111   Q6
sgs 94080 0x40 # 01000000   Q6
sgs 8320 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 100160 0x40 # 01000000   Q6
sgs 29120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (14 entries, util 14.0400 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 20800 0xBF # 10111111   Q7
sgs 206400 0x40 # 01000000   Q6
sgs 23040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 20800 0xBF # 10111111   Q7
sgs 135680 0x40 # 01000000   Q6
sgs 43520 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p4  (22 entries, util 26.5200 %)

```
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 24320 0x7F # 01111111   Q6
sgs 34880 0x80 # 10000000   Q7
sgs 15040 0xBF # 10111111   Q7
sgs 35520 0x80 # 10000000   Q7
sgs 19520 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 8320 0x3F # 00111111   BE
sgs 122240 0x40 # 01000000   Q6
sgs 19520 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 24320 0x7F # 01111111   Q6
sgs 85440 0x80 # 10000000   Q7
sgs 19520 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 8320 0x3F # 00111111   BE
sgs 113920 0x40 # 01000000   Q6
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (22 entries, util 42.1200 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 10560 0x3F # 00111111   BE
sgs 32960 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 4800 0x3F # 00111111   BE
sgs 40960 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 46400 0xBF # 10111111   Q7
sgs 26880 0x7F # 01111111   Q6
sgs 109440 0x80 # 10000000   Q7
sgs 13760 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 26880 0x7F # 01111111   Q6
sgs 109440 0x80 # 10000000   Q7
sgs 13760 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 26880 0x7F # 01111111   Q6
sgs 82560 0x80 # 10000000   Q7
sgs 40640 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p5  (18 entries, util 20.2800 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0x3F # 00111111   BE
sgs 94080 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 120960 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0x3F # 00111111   BE
sgs 94080 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 91840 0x40 # 01000000   Q6
sgs 29120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p4  (14 entries, util 14.0400 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 206400 0x40 # 01000000   Q6
sgs 31360 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 144000 0x40 # 01000000   Q6
sgs 43520 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (25 entries, util 26.5200 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 2880 0x3F # 00111111   BE
sgs 32320 0x80 # 10000000   Q7
sgs 15040 0xBF # 10111111   Q7
sgs 2560 0x3F # 00111111   BE
sgs 36160 0x80 # 10000000   Q7
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 122240 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 2880 0x3F # 00111111   BE
sgs 86080 0x80 # 10000000   Q7
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 105600 0x40 # 01000000   Q6
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (18 entries, util 20.2800 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0xBF # 10111111   Q7
sgs 94080 0x40 # 01000000   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 120960 0x40 # 01000000   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0xBF # 10111111   Q7
sgs 94080 0x40 # 01000000   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 83520 0x40 # 01000000   Q6
sgs 29120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p5  (23 entries, util 42.1200 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 7680 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 17280 0x7F # 01111111   Q6
sgs 27840 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 9920 0x3F # 00111111   BE
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 109440 0x80 # 10000000   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 109440 0x80 # 10000000   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 89280 0x80 # 10000000   Q7
sgs 40640 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p4  (24 entries, util 26.5200 %)

```
sgs 24960 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 10560 0x3F # 00111111   BE
sgs 29760 0x80 # 10000000   Q7
sgs 20160 0x3F # 00111111   BE
sgs 36800 0x80 # 10000000   Q7
sgs 2880 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 122240 0x40 # 01000000   Q6
sgs 2880 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 10560 0x3F # 00111111   BE
sgs 86720 0x80 # 10000000   Q7
sgs 2880 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 97280 0x40 # 01000000   Q6
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (14 entries, util 14.0400 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 4160 0x3F # 00111111   BE
sgs 206400 0x40 # 01000000   Q6
sgs 39680 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 4160 0x3F # 00111111   BE
sgs 152320 0x40 # 01000000   Q6
sgs 43520 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (23 entries, util 42.1200 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 24000 0x7F # 01111111   Q6
sgs 22720 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 15040 0xBF # 10111111   Q7
sgs 25600 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 11840 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 13440 0x7F # 01111111   Q6
sgs 109440 0x80 # 10000000   Q7
sgs 27200 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 13440 0x7F # 01111111   Q6
sgs 109440 0x80 # 10000000   Q7
sgs 27200 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 13440 0x7F # 01111111   Q6
sgs 96000 0x80 # 10000000   Q7
sgs 40640 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p5  (18 entries, util 20.2800 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0xBF # 10111111   Q7
sgs 94080 0x40 # 01000000   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 45760 0x7F # 01111111   Q6
sgs 120960 0x40 # 01000000   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 45760 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0xBF # 10111111   Q7
sgs 94080 0x40 # 01000000   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 45760 0x7F # 01111111   Q6
sgs 75200 0x40 # 01000000   Q6
sgs 29120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p2  (19 entries, util 21.8400 %)

```
sgs 33280 0x3F # 00111111   BE
sgs 33280 0x40 # 01000000   Q6
sgs 1600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 25280 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 24960 0x80 # 10000000   Q7
sgs 101760 0x3F # 00111111   BE
sgs 35840 0x40 # 01000000   Q6
sgs 164160 0x3F # 00111111   BE
sgs 33280 0x40 # 01000000   Q6
sgs 1600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 15040 0x40 # 01000000   Q6
sgs 137280 0x3F # 00111111   BE
sgs 35840 0x40 # 01000000   Q6
sgs 130880 0x3F # 00111111   BE
```

### sw08-p4  (12 entries, util 14.0400 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 206400 0x40 # 01000000   Q6
sgs 48000 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 45760 0x7F # 01111111   Q6
sgs 160640 0x40 # 01000000   Q6
sgs 43520 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (23 entries, util 42.1200 %)

```
sgs 6720 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 17600 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 20160 0xBF # 10111111   Q7
sgs 17920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 19520 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 6720 0x3F # 00111111   BE
sgs 96640 0x80 # 10000000   Q7
sgs 46720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 6720 0x3F # 00111111   BE
sgs 96640 0x80 # 10000000   Q7
sgs 46720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 6720 0x3F # 00111111   BE
sgs 89920 0x80 # 10000000   Q7
sgs 3520 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

