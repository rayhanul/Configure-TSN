# Reconfiguration-free admission (Problem 3)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Frozen schedule W loaded from: **result/result-2026-10-10-dataset-testbed-5-avgwin/rl-c9-on/5-matrix-c9on**

## Admission: W (before) vs. after this run's arrivals

| | admitted | of total |
|---|---|---|
| W (base, unchanged) | 10 | 10 |
| + this run's arrivals | 19 | 40 |

Every arrival admitted here required **zero** window-boundary changes -- see the GCL-entry table below (unchanged from W by construction) and the window-boundary integrity check. No previously-admitted flow was rerouted.

## Arrivals

| id | src->dst | RS(s) size | admitted | route | queue | phi_s (ns) | e2e (ns) | rerouted to make room | reason if rejected |
|---|---|---|---|---|---|---|---|---|---|
| 8 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q7 | 0 | 100480 | - | - |
| 14 | S1->S3 | - | yes | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 12480 | 102080 | - | - |
| 15 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 12480 | 54080 | - | - |
| 20 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 18 | S1->S3 | - | yes | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 24960 | 171200 | - | - |
| 6 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 24960 | 54400 | - | - |
| 7 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 | 24960 | 106880 | - | - |
| 11 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 255360 | 81280 | - | - |
| 1 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q7 | 49920 | 122560 | - | - |
| 4 | S1->S3 | - | yes | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 224960 | 124160 | - | - |
| 36 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 42 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 50 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 149120 | 113280 | - | - |
| 30 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 301760 | 59840 | - | - |
| 37 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 74880 | 71040 | - | - |
| 22 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q6 | 74880 | 163200 | - | - |
| 28 | S1->S3 | - | yes | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 237440 | 136640 | - | - |
| 31 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q6 | 224960 | 212480 | - | - |
| 43 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q6 | 237440 | 212480 | - | - |
| 45 | S1->S3 | - | yes | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 550080 | 248640 | - | - |
| 21 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 25 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 24 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 33 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 35 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 39 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 320640 | 65920 | - | - |
| 48 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 26 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 29 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 34 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 23 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 38 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 161600 | 113280 | - | - |
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
| sw01-p2 | 35 | 35 | 255 |
| sw01-p4 | 24 | 24 | 255 |
| sw02-p2 | 21 | 21 | 255 |
| sw02-p4 | 21 | 21 | 255 |
| sw03-p4 | 35 | 35 | 255 |
| sw03-p5 | 25 | 25 | 255 |
| sw04-p4 | 23 | 23 | 255 |
| sw04-p5 | 23 | 23 | 255 |
| sw05-p4 | 24 | 24 | 255 |
| sw05-p5 | 39 | 39 | 255 |
| sw06-p4 | 25 | 25 | 255 |
| sw06-p5 | 22 | 22 | 255 |
| sw07-p4 | 40 | 40 | 255 |
| sw07-p5 | 24 | 24 | 255 |
| sw08-p2 | 21 | 21 | 255 |
| sw08-p4 | 20 | 20 | 255 |
| sw08-p5 | 38 | 38 | 255 |

## Per-hop windows used by newly admitted flows

| flow | egress port | queue | psi (ns, unchanged) | delta (ns, unchanged) |
|---|---|---|---|---|
| s24(id=8 S3->S1) | S3-p0 | Q7 | 0 | 12480 |
| s24(id=8 S3->S1) | sw01-p4 | Q7 | 8320 | 12480 |
| s24(id=8 S3->S1) | sw03-p5 | Q7 | 16640 | 12480 |
| s24(id=8 S3->S1) | sw05-p4 | Q7 | 24960 | 12480 |
| s24(id=8 S3->S1) | sw07-p5 | Q7 | 33280 | 12480 |
| s24(id=8 S3->S1) | sw08-p4 | Q7 | 62080 | 12480 |
| s24(id=8 S3->S1) | sw06-p5 | Q7 | 70720 | 12480 |
| s24(id=8 S3->S1) | sw04-p4 | Q7 | 79360 | 12480 |
| s24(id=8 S3->S1) | sw02-p2 | Q7 | 88000 | 12480 |
| s26(id=14 S1->S3) | S1-p0 | Q6 | 12480 | 12480 |
| s26(id=14 S1->S3) | sw02-p4 | Q6 | 20800 | 12480 |
| s26(id=14 S1->S3) | sw04-p5 | Q6 | 29120 | 12480 |
| s26(id=14 S1->S3) | sw06-p4 | Q6 | 37440 | 12480 |
| s26(id=14 S1->S3) | sw08-p5 | Q6 | 50880 | 12480 |
| s26(id=14 S1->S3) | sw07-p4 | Q6 | 86720 | 12480 |
| s26(id=14 S1->S3) | sw05-p5 | Q6 | 91840 | 12480 |
| s26(id=14 S1->S3) | sw03-p4 | Q6 | 96960 | 12480 |
| s26(id=14 S1->S3) | sw01-p2 | Q6 | 102080 | 12480 |
| s27(id=15 S2->S3) | S2-p0 | Q6 | 12480 | 12480 |
| s27(id=15 S2->S3) | sw08-p5 | Q6 | 20800 | 12480 |
| s27(id=15 S2->S3) | sw07-p4 | Q6 | 29120 | 12480 |
| s27(id=15 S2->S3) | sw05-p5 | Q6 | 37440 | 12480 |
| s27(id=15 S2->S3) | sw03-p4 | Q6 | 45760 | 12480 |
| s27(id=15 S2->S3) | sw01-p2 | Q6 | 54080 | 12480 |
| s28(id=18 S1->S3) | S1-p0 | Q6 | 24960 | 12480 |
| s28(id=18 S1->S3) | sw02-p4 | Q6 | 107520 | 12480 |
| s28(id=18 S1->S3) | sw04-p5 | Q6 | 115200 | 12480 |
| s28(id=18 S1->S3) | sw06-p4 | Q6 | 122880 | 12480 |
| s28(id=18 S1->S3) | sw08-p5 | Q6 | 130560 | 12480 |
| s28(id=18 S1->S3) | sw07-p4 | Q6 | 158720 | 12480 |
| s28(id=18 S1->S3) | sw05-p5 | Q6 | 167040 | 12480 |
| s28(id=18 S1->S3) | sw03-p4 | Q6 | 175360 | 12480 |
| s28(id=18 S1->S3) | sw01-p2 | Q6 | 183680 | 12480 |
| s22(id=6 S2->S3) | S2-p0 | Q7 | 24960 | 12480 |
| s22(id=6 S2->S3) | sw08-p5 | Q7 | 33920 | 12480 |
| s22(id=6 S2->S3) | sw07-p4 | Q7 | 47680 | 12480 |
| s22(id=6 S2->S3) | sw05-p5 | Q7 | 53760 | 12480 |
| s22(id=6 S2->S3) | sw03-p4 | Q7 | 59840 | 12480 |
| s22(id=6 S2->S3) | sw01-p2 | Q7 | 66880 | 12480 |
| s23(id=7 S3->S2) | S3-p0 | Q7 | 24960 | 12480 |
| s23(id=7 S3->S2) | sw01-p4 | Q7 | 34240 | 12480 |
| s23(id=7 S3->S2) | sw03-p5 | Q7 | 43520 | 12480 |
| s23(id=7 S3->S2) | sw05-p4 | Q7 | 51840 | 12480 |
| s23(id=7 S3->S2) | sw07-p5 | Q7 | 108160 | 12480 |
| s23(id=7 S3->S2) | sw08-p2 | Q7 | 119040 | 12480 |
| s25(id=11 S2->S3) | S2-p0 | Q6 | 255360 | 12480 |
| s25(id=11 S2->S3) | sw08-p5 | Q6 | 284800 | 12480 |
| s25(id=11 S2->S3) | sw07-p4 | Q6 | 299200 | 12480 |
| s25(id=11 S2->S3) | sw05-p5 | Q6 | 307520 | 12480 |
| s25(id=11 S2->S3) | sw03-p4 | Q6 | 315840 | 12480 |
| s25(id=11 S2->S3) | sw01-p2 | Q6 | 324160 | 12480 |
| s20(id=1 S3->S1) | S3-p0 | Q7 | 49920 | 12480 |
| s20(id=1 S3->S1) | sw01-p4 | Q7 | 80960 | 12480 |
| s20(id=1 S3->S1) | sw03-p5 | Q7 | 87040 | 12480 |
| s20(id=1 S3->S1) | sw05-p4 | Q7 | 114880 | 12480 |
| s20(id=1 S3->S1) | sw07-p5 | Q7 | 120960 | 12480 |
| s20(id=1 S3->S1) | sw08-p4 | Q7 | 141760 | 12480 |
| s20(id=1 S3->S1) | sw06-p5 | Q7 | 147840 | 12480 |
| s20(id=1 S3->S1) | sw04-p4 | Q7 | 153920 | 12480 |
| s20(id=1 S3->S1) | sw02-p2 | Q7 | 160000 | 12480 |
| s21(id=4 S1->S3) | S1-p0 | Q6 | 224960 | 12480 |
| s21(id=4 S1->S3) | sw02-p4 | Q6 | 233280 | 12480 |
| s21(id=4 S1->S3) | sw04-p5 | Q6 | 241600 | 12480 |
| s21(id=4 S1->S3) | sw06-p4 | Q6 | 281280 | 12480 |
| s21(id=4 S1->S3) | sw08-p5 | Q6 | 297280 | 12480 |
| s21(id=4 S1->S3) | sw07-p4 | Q6 | 311680 | 12480 |
| s21(id=4 S1->S3) | sw05-p5 | Q6 | 320000 | 12480 |
| s21(id=4 S1->S3) | sw03-p4 | Q6 | 328320 | 12480 |
| s21(id=4 S1->S3) | sw01-p2 | Q6 | 336640 | 12480 |
| s59(id=50 S2->S1) | S2-p0 | Q7 | 149120 | 12480 |
| s59(id=50 S2->S1) | sw08-p4 | Q7 | 165440 | 12480 |
| s59(id=50 S2->S1) | sw06-p5 | Q7 | 174080 | 12480 |
| s59(id=50 S2->S1) | sw04-p4 | Q7 | 182720 | 12480 |
| s59(id=50 S2->S1) | sw02-p2 | Q7 | 249920 | 12480 |
| s39(id=30 S2->S3) | S2-p0 | Q6 | 301760 | 12480 |
| s39(id=30 S2->S3) | sw08-p5 | Q6 | 309760 | 12480 |
| s39(id=30 S2->S3) | sw07-p4 | Q6 | 324160 | 12480 |
| s39(id=30 S2->S3) | sw05-p5 | Q6 | 332480 | 12480 |
| s39(id=30 S2->S3) | sw03-p4 | Q6 | 340800 | 12480 |
| s39(id=30 S2->S3) | sw01-p2 | Q6 | 349120 | 12480 |
| s46(id=37 S2->S3) | S2-p0 | Q7 | 74880 | 12480 |
| s46(id=37 S2->S3) | sw08-p5 | Q7 | 82560 | 12480 |
| s46(id=37 S2->S3) | sw07-p4 | Q7 | 110400 | 12480 |
| s46(id=37 S2->S3) | sw05-p5 | Q7 | 118080 | 12480 |
| s46(id=37 S2->S3) | sw03-p4 | Q7 | 125760 | 12480 |
| s46(id=37 S2->S3) | sw01-p2 | Q7 | 133440 | 12480 |
| s31(id=22 S3->S1) | S3-p0 | Q6 | 74880 | 12480 |
| s31(id=22 S3->S1) | sw01-p4 | Q6 | 100160 | 12480 |
| s31(id=22 S3->S1) | sw03-p5 | Q6 | 105280 | 12480 |
| s31(id=22 S3->S1) | sw05-p4 | Q6 | 200000 | 12480 |
| s31(id=22 S3->S1) | sw07-p5 | Q6 | 205120 | 12480 |
| s31(id=22 S3->S1) | sw08-p4 | Q6 | 210240 | 12480 |
| s31(id=22 S3->S1) | sw06-p5 | Q6 | 215360 | 12480 |
| s31(id=22 S3->S1) | sw04-p4 | Q6 | 220480 | 12480 |
| s31(id=22 S3->S1) | sw02-p2 | Q6 | 225600 | 12480 |
| s37(id=28 S1->S3) | S1-p0 | Q6 | 237440 | 12480 |
| s37(id=28 S1->S3) | sw02-p4 | Q6 | 245760 | 12480 |
| s37(id=28 S1->S3) | sw04-p5 | Q6 | 280960 | 12480 |
| s37(id=28 S1->S3) | sw06-p4 | Q6 | 307840 | 12480 |
| s37(id=28 S1->S3) | sw08-p5 | Q6 | 322240 | 12480 |
| s37(id=28 S1->S3) | sw07-p4 | Q6 | 336640 | 12480 |
| s37(id=28 S1->S3) | sw05-p5 | Q6 | 344960 | 12480 |
| s37(id=28 S1->S3) | sw03-p4 | Q6 | 353280 | 12480 |
| s37(id=28 S1->S3) | sw01-p2 | Q6 | 361600 | 12480 |
| s40(id=31 S3->S1) | S3-p0 | Q6 | 224960 | 12480 |
| s40(id=31 S3->S1) | sw01-p4 | Q6 | 233280 | 12480 |
| s40(id=31 S3->S1) | sw03-p5 | Q6 | 241600 | 12480 |
| s40(id=31 S3->S1) | sw05-p4 | Q6 | 249920 | 12480 |
| s40(id=31 S3->S1) | sw07-p5 | Q6 | 258240 | 12480 |
| s40(id=31 S3->S1) | sw08-p4 | Q6 | 400000 | 12480 |
| s40(id=31 S3->S1) | sw06-p5 | Q6 | 408320 | 12480 |
| s40(id=31 S3->S1) | sw04-p4 | Q6 | 416640 | 12480 |
| s40(id=31 S3->S1) | sw02-p2 | Q6 | 424960 | 12480 |
| s52(id=43 S3->S1) | S3-p0 | Q6 | 237440 | 12480 |
| s52(id=43 S3->S1) | sw01-p4 | Q6 | 245760 | 12480 |
| s52(id=43 S3->S1) | sw03-p5 | Q6 | 254080 | 12480 |
| s52(id=43 S3->S1) | sw05-p4 | Q6 | 262400 | 12480 |
| s52(id=43 S3->S1) | sw07-p5 | Q6 | 406080 | 12480 |
| s52(id=43 S3->S1) | sw08-p4 | Q6 | 412800 | 12480 |
| s52(id=43 S3->S1) | sw06-p5 | Q6 | 420800 | 12480 |
| s52(id=43 S3->S1) | sw04-p4 | Q6 | 429120 | 12480 |
| s52(id=43 S3->S1) | sw02-p2 | Q6 | 437440 | 12480 |
| s54(id=45 S1->S3) | S1-p0 | Q7 | 550080 | 12480 |
| s54(id=45 S1->S3) | sw02-p4 | Q7 | 562240 | 12480 |
| s54(id=45 S1->S3) | sw04-p5 | Q7 | 571840 | 12480 |
| s54(id=45 S1->S3) | sw06-p4 | Q7 | 750080 | 12480 |
| s54(id=45 S1->S3) | sw08-p5 | Q7 | 761920 | 12480 |
| s54(id=45 S1->S3) | sw07-p4 | Q7 | 768000 | 12480 |
| s54(id=45 S1->S3) | sw05-p5 | Q7 | 774080 | 12480 |
| s54(id=45 S1->S3) | sw03-p4 | Q7 | 780160 | 12480 |
| s54(id=45 S1->S3) | sw01-p2 | Q7 | 786240 | 12480 |
| s48(id=39 S2->S3) | S2-p0 | Q6 | 320640 | 12480 |
| s48(id=39 S2->S3) | sw08-p5 | Q6 | 334720 | 12480 |
| s48(id=39 S2->S3) | sw07-p4 | Q6 | 349120 | 12480 |
| s48(id=39 S2->S3) | sw05-p5 | Q6 | 357440 | 12480 |
| s48(id=39 S2->S3) | sw03-p4 | Q6 | 365760 | 12480 |
| s48(id=39 S2->S3) | sw01-p2 | Q6 | 374080 | 12480 |
| s47(id=38 S2->S1) | S2-p0 | Q7 | 161600 | 12480 |
| s47(id=38 S2->S1) | sw08-p4 | Q7 | 177920 | 12480 |
| s47(id=38 S2->S1) | sw06-p5 | Q7 | 186560 | 12480 |
| s47(id=38 S2->S1) | sw04-p4 | Q7 | 249920 | 12480 |
| s47(id=38 S2->S1) | sw02-p2 | Q7 | 262400 | 12480 |

## Constraint check

- C1-C7, C9: OK
- window-boundary integrity (no window's psi/delta changed anywhere): OK

## GCL per egress port

### sw01-p2  (35 entries, util 42.1200 %)

```
sgs 33600 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 8000 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 33600 0x80 # 10000000   Q7
sgs 1600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 16000 0x7F # 01111111   Q6
sgs 30720 0x80 # 10000000   Q7
sgs 22400 0xBF # 10111111   Q7
sgs 13760 0x40 # 01000000   Q6
sgs 36160 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 8000 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 35520 0xBF # 10111111   Q7
sgs 95360 0x40 # 01000000   Q6
sgs 36160 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 8000 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 22720 0xBF # 10111111   Q7
sgs 45440 0x40 # 01000000   Q6
sgs 36160 0xBF # 10111111   Q7
sgs 13760 0x40 # 01000000   Q6
sgs 36160 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 8000 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 35520 0xBF # 10111111   Q7
sgs 61760 0x40 # 01000000   Q6
sgs 36160 0xBF # 10111111   Q7
```

### sw01-p4  (24 entries, util 26.5200 %)

```
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 960 0x3F # 00111111   BE
sgs 33280 0x40 # 01000000   Q6
sgs 19200 0xBF # 10111111   Q7
sgs 17280 0x7F # 01111111   Q6
sgs 43520 0x80 # 10000000   Q7
sgs 47360 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 140160 0x40 # 01000000   Q6
sgs 47360 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 960 0x3F # 00111111   BE
sgs 113280 0x40 # 01000000   Q6
sgs 47360 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 131840 0x40 # 01000000   Q6
sgs 47360 0xBF # 10111111   Q7
```

### sw02-p2  (21 entries, util 23.4000 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 20800 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 4800 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 59520 0x7F # 01111111   Q6
sgs 31360 0x80 # 10000000   Q7
sgs 58560 0x7F # 01111111   Q6
sgs 38080 0xBF # 10111111   Q7
sgs 86080 0x80 # 10000000   Q7
sgs 25920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 20800 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 4800 0x3F # 00111111   BE
sgs 103360 0x80 # 10000000   Q7
sgs 58560 0x7F # 01111111   Q6
sgs 38080 0xBF # 10111111   Q7
sgs 15360 0x80 # 10000000   Q7
sgs 46720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p4  (21 entries, util 26.5200 %)

```
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 24320 0x7F # 01111111   Q6
sgs 34880 0x80 # 10000000   Q7
sgs 15040 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 42240 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 46080 0xBF # 10111111   Q7
sgs 136640 0x40 # 01000000   Q6
sgs 63360 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 24320 0x7F # 01111111   Q6
sgs 41280 0x80 # 10000000   Q7
sgs 13760 0xBF # 10111111   Q7
sgs 49600 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 46080 0xBF # 10111111   Q7
sgs 128320 0x40 # 01000000   Q6
sgs 13440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (35 entries, util 42.1200 %)

```
sgs 26880 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 6400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 1600 0x3F # 00111111   BE
sgs 35520 0x80 # 10000000   Q7
sgs 1600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0x7F # 01111111   Q6
sgs 29760 0x80 # 10000000   Q7
sgs 21760 0xBF # 10111111   Q7
sgs 15360 0x40 # 01000000   Q6
sgs 36160 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 6400 0x3F # 00111111   BE
sgs 15040 0x40 # 01000000   Q6
sgs 36160 0xBF # 10111111   Q7
sgs 93760 0x40 # 01000000   Q6
sgs 36160 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 6400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 1600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 24640 0xBF # 10111111   Q7
sgs 42240 0x40 # 01000000   Q6
sgs 36160 0xBF # 10111111   Q7
sgs 15360 0x40 # 01000000   Q6
sgs 36160 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 6400 0x3F # 00111111   BE
sgs 15040 0x40 # 01000000   Q6
sgs 36160 0xBF # 10111111   Q7
sgs 66880 0x40 # 01000000   Q6
sgs 36160 0xBF # 10111111   Q7
```

### sw03-p5  (25 entries, util 26.5200 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 1920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 31040 0x40 # 01000000   Q6
sgs 13120 0xBF # 10111111   Q7
sgs 23360 0x7F # 01111111   Q6
sgs 45760 0x80 # 10000000   Q7
sgs 30720 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 140160 0x40 # 01000000   Q6
sgs 30720 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 1920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 113280 0x40 # 01000000   Q6
sgs 30720 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 123520 0x40 # 01000000   Q6
sgs 47360 0xBF # 10111111   Q7
```

### sw04-p4  (23 entries, util 23.4000 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 4480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 62080 0x7F # 01111111   Q6
sgs 28800 0x80 # 10000000   Q7
sgs 17280 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 29440 0xBF # 10111111   Q7
sgs 86400 0x80 # 10000000   Q7
sgs 34240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 4480 0x3F # 00111111   BE
sgs 103360 0x80 # 10000000   Q7
sgs 17280 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 29440 0xBF # 10111111   Q7
sgs 24000 0x80 # 10000000   Q7
sgs 46720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (23 entries, util 26.5200 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 23680 0x7F # 01111111   Q6
sgs 32320 0x80 # 10000000   Q7
sgs 17600 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 44160 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 28160 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 136640 0x40 # 01000000   Q6
sgs 46720 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 23680 0x7F # 01111111   Q6
sgs 43200 0x80 # 10000000   Q7
sgs 63360 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 28160 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 120000 0x40 # 01000000   Q6
sgs 13440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (24 entries, util 26.5200 %)

```
sgs 24960 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0xBF # 10111111   Q7
sgs 28800 0x40 # 01000000   Q6
sgs 4800 0x3F # 00111111   BE
sgs 76160 0x80 # 10000000   Q7
sgs 25920 0xBF # 10111111   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 136640 0x40 # 01000000   Q6
sgs 25920 0xBF # 10111111   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 21120 0xBF # 10111111   Q7
sgs 76160 0x80 # 10000000   Q7
sgs 25920 0xBF # 10111111   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 111680 0x40 # 01000000   Q6
sgs 50880 0xBF # 10111111   Q7
```

### sw05-p5  (39 entries, util 42.1200 %)

```
sgs 20160 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 4800 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 3840 0x3F # 00111111   BE
sgs 36480 0x80 # 10000000   Q7
sgs 1600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12800 0x7F # 01111111   Q6
sgs 28800 0x80 # 10000000   Q7
sgs 21120 0xBF # 10111111   Q7
sgs 16960 0x40 # 01000000   Q6
sgs 16000 0xBF # 10111111   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 4800 0x3F # 00111111   BE
sgs 18240 0x40 # 01000000   Q6
sgs 36160 0xBF # 10111111   Q7
sgs 92160 0x40 # 01000000   Q6
sgs 16000 0xBF # 10111111   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 4800 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 3840 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 25600 0xBF # 10111111   Q7
sgs 39040 0x40 # 01000000   Q6
sgs 19200 0x7F # 01111111   Q6
sgs 16960 0xBF # 10111111   Q7
sgs 16960 0x40 # 01000000   Q6
sgs 16000 0xBF # 10111111   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 4800 0x3F # 00111111   BE
sgs 18240 0x40 # 01000000   Q6
sgs 36160 0xBF # 10111111   Q7
sgs 72000 0x40 # 01000000   Q6
sgs 36160 0xBF # 10111111   Q7
```

### sw06-p4  (25 entries, util 26.5200 %)

```
sgs 24960 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 23040 0x7F # 01111111   Q6
sgs 29760 0x80 # 10000000   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 27200 0x7F # 01111111   Q6
sgs 16960 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 20480 0xBF # 10111111   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 136640 0x40 # 01000000   Q6
sgs 38400 0xBF # 10111111   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 23040 0x7F # 01111111   Q6
sgs 43200 0x80 # 10000000   Q7
sgs 46400 0x7F # 01111111   Q6
sgs 16960 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 20480 0xBF # 10111111   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 111680 0x40 # 01000000   Q6
sgs 13440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (22 entries, util 23.4000 %)

```
sgs 54080 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 16960 0xBF # 10111111   Q7
sgs 47680 0x7F # 01111111   Q6
sgs 26240 0x80 # 10000000   Q7
sgs 25920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 20800 0xBF # 10111111   Q7
sgs 86720 0x80 # 10000000   Q7
sgs 42560 0xBF # 10111111   Q7
sgs 54080 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 103360 0x80 # 10000000   Q7
sgs 25920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 20800 0xBF # 10111111   Q7
sgs 32640 0x80 # 10000000   Q7
sgs 46720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (40 entries, util 42.1200 %)

```
sgs 13440 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 3200 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 6080 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 1600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 27840 0x80 # 10000000   Q7
sgs 20480 0xBF # 10111111   Q7
sgs 18560 0x40 # 01000000   Q6
sgs 22720 0xBF # 10111111   Q7
sgs 13440 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 3200 0x3F # 00111111   BE
sgs 21440 0x40 # 01000000   Q6
sgs 36160 0xBF # 10111111   Q7
sgs 90560 0x40 # 01000000   Q6
sgs 22720 0xBF # 10111111   Q7
sgs 13440 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 3200 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 6080 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 26560 0xBF # 10111111   Q7
sgs 35840 0x40 # 01000000   Q6
sgs 36160 0x7F # 01111111   Q6
sgs 18560 0x40 # 01000000   Q6
sgs 22720 0xBF # 10111111   Q7
sgs 13440 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 3200 0x3F # 00111111   BE
sgs 21440 0x40 # 01000000   Q6
sgs 36160 0xBF # 10111111   Q7
sgs 77120 0x40 # 01000000   Q6
sgs 36160 0xBF # 10111111   Q7
```

### sw07-p5  (24 entries, util 26.5200 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0xBF # 10111111   Q7
sgs 27520 0x40 # 01000000   Q6
sgs 8000 0x3F # 00111111   BE
sgs 74240 0x80 # 10000000   Q7
sgs 17600 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 136640 0x40 # 01000000   Q6
sgs 17600 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 23040 0xBF # 10111111   Q7
sgs 74240 0x80 # 10000000   Q7
sgs 17600 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 103360 0x40 # 01000000   Q6
sgs 50880 0xBF # 10111111   Q7
```

### sw08-p2  (21 entries, util 24.9600 %)

```
sgs 33280 0x3F # 00111111   BE
sgs 33280 0x40 # 01000000   Q6
sgs 1600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 25280 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 101440 0x3F # 00111111   BE
sgs 33280 0x40 # 01000000   Q6
sgs 166720 0x3F # 00111111   BE
sgs 33280 0x40 # 01000000   Q6
sgs 1600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 25920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 101440 0x3F # 00111111   BE
sgs 33280 0x40 # 01000000   Q6
sgs 133440 0x3F # 00111111   BE
```

### sw08-p4  (20 entries, util 23.4000 %)

```
sgs 45760 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 3840 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 25600 0xBF # 10111111   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 23680 0x80 # 10000000   Q7
sgs 34560 0xBF # 10111111   Q7
sgs 62080 0x7F # 01111111   Q6
sgs 87040 0x80 # 10000000   Q7
sgs 50880 0xBF # 10111111   Q7
sgs 45760 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 3840 0x3F # 00111111   BE
sgs 103360 0x80 # 10000000   Q7
sgs 34560 0xBF # 10111111   Q7
sgs 62080 0x7F # 01111111   Q6
sgs 41280 0x80 # 10000000   Q7
sgs 46720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (38 entries, util 42.1200 %)

```
sgs 6720 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 1600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 4480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 20160 0xBF # 10111111   Q7
sgs 17920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 19840 0x7F # 01111111   Q6
sgs 18240 0x40 # 01000000   Q6
sgs 38080 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 1600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 17600 0x7F # 01111111   Q6
sgs 117760 0x40 # 01000000   Q6
sgs 38080 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 1600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 4480 0x3F # 00111111   BE
sgs 61440 0x40 # 01000000   Q6
sgs 38080 0x7F # 01111111   Q6
sgs 18240 0x40 # 01000000   Q6
sgs 38080 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 1600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 17600 0x7F # 01111111   Q6
sgs 111040 0x40 # 01000000   Q6
sgs 38080 0xBF # 10111111   Q7
```

