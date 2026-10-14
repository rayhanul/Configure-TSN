# Reconfiguration-free admission (Problem 3)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Frozen schedule W loaded from: **result/result-2026-10-13-dataset-testbed-12-tree-avgwin/heuristic-c9-on/12-matrix-c9on**

## Admission: W (before) vs. after this run's arrivals

| | admitted | of total |
|---|---|---|
| W (base, unchanged) | 11 | 11 |
| + this run's arrivals | 25 | 39 |

Every arrival admitted here required **zero** window-boundary changes -- see the GCL-entry table below (unchanged from W by construction) and the window-boundary integrity check. No previously-admitted flow was rerouted.

## Arrivals

| id | src->dst | RS(s) size | admitted | route | queue | phi_s (ns) | e2e (ns) | rerouted to make room | reason if rejected |
|---|---|---|---|---|---|---|---|---|---|
| 10 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 20 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 3 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q6 | 62400 | 79040 | - | - |
| 15 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 132480 | 56320 | - | - |
| 16 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 | 212480 | 175680 | - | - |
| 1 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 62400 | 130880 | - | - |
| 17 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q6 | 237440 | 44160 | - | - |
| 6 | S1->S3 | - | yes | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 163840 | 312000 | - | - |
| 13 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 300160 | 38080 | - | - |
| 27 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 12480 | 100160 | - | - |
| 32 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 100160 | 112320 | - | - |
| 38 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 474880 | 43200 | - | - |
| 45 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 49920 | 39360 | - | - |
| 50 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 112640 | 112320 | - | - |
| 30 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 150080 | 122560 | - | - |
| 42 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 312640 | 54080 | - | - |
| 43 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q6 | 74880 | 137600 | - | - |
| 31 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q6 | 87360 | 251520 | - | - |
| 40 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q7 | 224960 | 63680 | - | - |
| 22 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 212480 | 45760 | - | - |
| 24 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 224960 | 45760 | - | - |
| 25 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q6 | 212480 | 50880 | - | - |
| 33 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q6 | 249920 | 44160 | - | - |
| 34 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q6 | 262400 | 44160 | - | - |
| 36 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q6 | 274880 | 45760 | - | - |
| 49 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 262080 | 100480 | - | - |
| 28 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q6 | 111040 | 113920 | - | - |
| 46 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 47 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 29 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 41 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 48 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 23 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 37 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 44 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 21 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 26 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 35 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 39 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |

## Per-port GCL entries (should equal W exactly)

| port | W entries | after arrivals | GCL_size |
|---|---|---|---|
| sw01-p2 | 17 | 17 | 255 |
| sw01-p4 | 22 | 22 | 255 |
| sw02-p2 | 23 | 23 | 255 |
| sw02-p4 | 28 | 28 | 255 |
| sw03-p4 | 20 | 20 | 255 |
| sw03-p5 | 23 | 23 | 255 |
| sw04-p4 | 23 | 23 | 255 |
| sw04-p5 | 28 | 28 | 255 |
| sw05-p4 | 22 | 22 | 255 |
| sw05-p5 | 22 | 22 | 255 |
| sw06-p4 | 28 | 28 | 255 |
| sw06-p5 | 22 | 22 | 255 |
| sw07-p4 | 22 | 22 | 255 |
| sw07-p5 | 22 | 22 | 255 |
| sw08-p2 | 24 | 24 | 255 |
| sw08-p4 | 21 | 21 | 255 |
| sw08-p5 | 23 | 23 | 255 |

## Per-hop windows used by newly admitted flows

| flow | egress port | queue | psi (ns, unchanged) | delta (ns, unchanged) |
|---|---|---|---|---|
| s21(id=3 S3->S1) | S3-p0 | Q6 | 62400 | 12480 |
| s21(id=3 S3->S1) | sw01-p4 | Q6 | 70720 | 12480 |
| s21(id=3 S3->S1) | sw03-p5 | Q6 | 79040 | 12480 |
| s21(id=3 S3->S1) | sw05-p4 | Q6 | 87360 | 12480 |
| s21(id=3 S3->S1) | sw07-p5 | Q6 | 95680 | 12480 |
| s21(id=3 S3->S1) | sw08-p4 | Q6 | 104000 | 12480 |
| s21(id=3 S3->S1) | sw06-p5 | Q6 | 112320 | 12480 |
| s21(id=3 S3->S1) | sw04-p4 | Q6 | 120640 | 12480 |
| s21(id=3 S3->S1) | sw02-p2 | Q6 | 128960 | 12480 |
| s25(id=15 S2->S3) | S2-p0 | Q6 | 132480 | 12480 |
| s25(id=15 S2->S3) | sw08-p5 | Q6 | 143040 | 12480 |
| s25(id=15 S2->S3) | sw07-p4 | Q6 | 151360 | 12480 |
| s25(id=15 S2->S3) | sw05-p5 | Q6 | 159680 | 12480 |
| s25(id=15 S2->S3) | sw03-p4 | Q6 | 168000 | 12480 |
| s25(id=15 S2->S3) | sw01-p2 | Q6 | 176320 | 12480 |
| s26(id=16 S3->S2) | S3-p0 | Q7 | 212480 | 12480 |
| s26(id=16 S3->S2) | sw01-p4 | Q7 | 220160 | 12480 |
| s26(id=16 S3->S2) | sw03-p5 | Q7 | 227840 | 12480 |
| s26(id=16 S3->S2) | sw05-p4 | Q7 | 235520 | 12480 |
| s26(id=16 S3->S2) | sw07-p5 | Q7 | 243200 | 12480 |
| s26(id=16 S3->S2) | sw08-p2 | Q7 | 375680 | 12480 |
| s20(id=1 S1->S2) | S1-p0 | Q7 | 62400 | 12480 |
| s20(id=1 S1->S2) | sw02-p4 | Q7 | 157760 | 12480 |
| s20(id=1 S1->S2) | sw04-p5 | Q7 | 165440 | 12480 |
| s20(id=1 S1->S2) | sw06-p4 | Q7 | 173120 | 12480 |
| s20(id=1 S1->S2) | sw08-p2 | Q7 | 180800 | 12480 |
| s27(id=17 S1->S2) | S1-p0 | Q6 | 237440 | 12480 |
| s27(id=17 S1->S2) | sw02-p4 | Q6 | 245760 | 12480 |
| s27(id=17 S1->S2) | sw04-p5 | Q6 | 254080 | 12480 |
| s27(id=17 S1->S2) | sw06-p4 | Q6 | 262400 | 12480 |
| s27(id=17 S1->S2) | sw08-p2 | Q6 | 269120 | 12480 |
| s22(id=6 S1->S3) | S1-p0 | Q7 | 163840 | 12480 |
| s22(id=6 S1->S3) | sw02-p4 | Q7 | 170560 | 12480 |
| s22(id=6 S1->S3) | sw04-p5 | Q7 | 177920 | 12480 |
| s22(id=6 S1->S3) | sw06-p4 | Q7 | 185600 | 12480 |
| s22(id=6 S1->S3) | sw08-p5 | Q7 | 379200 | 12480 |
| s22(id=6 S1->S3) | sw07-p4 | Q7 | 387520 | 12480 |
| s22(id=6 S1->S3) | sw05-p5 | Q7 | 449920 | 12480 |
| s22(id=6 S1->S3) | sw03-p4 | Q7 | 456640 | 12480 |
| s22(id=6 S1->S3) | sw01-p2 | Q7 | 463360 | 12480 |
| s24(id=13 S2->S3) | S2-p0 | Q6 | 300160 | 12480 |
| s24(id=13 S2->S3) | sw08-p5 | Q6 | 305280 | 12480 |
| s24(id=13 S2->S3) | sw07-p4 | Q6 | 310400 | 12480 |
| s24(id=13 S2->S3) | sw05-p5 | Q6 | 315520 | 12480 |
| s24(id=13 S2->S3) | sw03-p4 | Q6 | 320640 | 12480 |
| s24(id=13 S2->S3) | sw01-p2 | Q6 | 325760 | 12480 |
| s35(id=27 S2->S1) | S2-p0 | Q6 | 12480 | 12480 |
| s35(id=27 S2->S1) | sw08-p4 | Q6 | 20160 | 12480 |
| s35(id=27 S2->S1) | sw06-p5 | Q6 | 27840 | 12480 |
| s35(id=27 S2->S1) | sw04-p4 | Q6 | 35520 | 12480 |
| s35(id=27 S2->S1) | sw02-p2 | Q6 | 100160 | 12480 |
| s40(id=32 S2->S1) | S2-p0 | Q6 | 100160 | 12480 |
| s40(id=32 S2->S1) | sw08-p4 | Q6 | 116480 | 12480 |
| s40(id=32 S2->S1) | sw06-p5 | Q6 | 124800 | 12480 |
| s40(id=32 S2->S1) | sw04-p4 | Q6 | 133120 | 12480 |
| s40(id=32 S2->S1) | sw02-p2 | Q6 | 200000 | 12480 |
| s46(id=38 S1->S2) | S1-p0 | Q7 | 474880 | 12480 |
| s46(id=38 S1->S2) | sw02-p4 | Q7 | 482560 | 12480 |
| s46(id=38 S1->S2) | sw04-p5 | Q7 | 490240 | 12480 |
| s46(id=38 S1->S2) | sw06-p4 | Q7 | 497920 | 12480 |
| s46(id=38 S1->S2) | sw08-p2 | Q7 | 505600 | 12480 |
| s53(id=45 S2->S1) | S2-p0 | Q7 | 49920 | 12480 |
| s53(id=45 S2->S1) | sw08-p4 | Q7 | 56640 | 12480 |
| s53(id=45 S2->S1) | sw06-p5 | Q7 | 63360 | 12480 |
| s53(id=45 S2->S1) | sw04-p4 | Q7 | 70080 | 12480 |
| s53(id=45 S2->S1) | sw02-p2 | Q7 | 76800 | 12480 |
| s58(id=50 S2->S1) | S2-p0 | Q6 | 112640 | 12480 |
| s58(id=50 S2->S1) | sw08-p4 | Q6 | 128960 | 12480 |
| s58(id=50 S2->S1) | sw06-p5 | Q6 | 137280 | 12480 |
| s58(id=50 S2->S1) | sw04-p4 | Q6 | 200000 | 12480 |
| s58(id=50 S2->S1) | sw02-p2 | Q6 | 212480 | 12480 |
| s38(id=30 S2->S3) | S2-p0 | Q7 | 150080 | 12480 |
| s38(id=30 S2->S3) | sw08-p5 | Q7 | 179200 | 12480 |
| s38(id=30 S2->S3) | sw07-p4 | Q7 | 187520 | 12480 |
| s38(id=30 S2->S3) | sw05-p5 | Q7 | 249920 | 12480 |
| s38(id=30 S2->S3) | sw03-p4 | Q7 | 255040 | 12480 |
| s38(id=30 S2->S3) | sw01-p2 | Q7 | 260160 | 12480 |
| s50(id=42 S2->S3) | S2-p0 | Q6 | 312640 | 12480 |
| s50(id=42 S2->S3) | sw08-p5 | Q6 | 320960 | 12480 |
| s50(id=42 S2->S3) | sw07-p4 | Q6 | 329280 | 12480 |
| s50(id=42 S2->S3) | sw05-p5 | Q6 | 337600 | 12480 |
| s50(id=42 S2->S3) | sw03-p4 | Q6 | 345920 | 12480 |
| s50(id=42 S2->S3) | sw01-p2 | Q6 | 354240 | 12480 |
| s51(id=43 S3->S2) | S3-p0 | Q6 | 74880 | 12480 |
| s51(id=43 S3->S2) | sw01-p4 | Q6 | 83200 | 12480 |
| s51(id=43 S3->S2) | sw03-p5 | Q6 | 91520 | 12480 |
| s51(id=43 S3->S2) | sw05-p4 | Q6 | 99840 | 12480 |
| s51(id=43 S3->S2) | sw07-p5 | Q6 | 108160 | 12480 |
| s51(id=43 S3->S2) | sw08-p2 | Q6 | 200000 | 12480 |
| s39(id=31 S3->S1) | S3-p0 | Q6 | 87360 | 12480 |
| s39(id=31 S3->S1) | sw01-p4 | Q6 | 95680 | 12480 |
| s39(id=31 S3->S1) | sw03-p5 | Q6 | 104000 | 12480 |
| s39(id=31 S3->S1) | sw05-p4 | Q6 | 112320 | 12480 |
| s39(id=31 S3->S1) | sw07-p5 | Q6 | 131520 | 12480 |
| s39(id=31 S3->S1) | sw08-p4 | Q6 | 303360 | 12480 |
| s39(id=31 S3->S1) | sw06-p5 | Q6 | 311040 | 12480 |
| s39(id=31 S3->S1) | sw04-p4 | Q6 | 318720 | 12480 |
| s39(id=31 S3->S1) | sw02-p2 | Q6 | 326400 | 12480 |
| s48(id=40 S3->S1) | S3-p0 | Q7 | 224960 | 12480 |
| s48(id=40 S3->S1) | sw01-p4 | Q7 | 232640 | 12480 |
| s48(id=40 S3->S1) | sw03-p5 | Q7 | 240320 | 12480 |
| s48(id=40 S3->S1) | sw05-p4 | Q7 | 248000 | 12480 |
| s48(id=40 S3->S1) | sw07-p5 | Q7 | 255680 | 12480 |
| s48(id=40 S3->S1) | sw08-p4 | Q7 | 260800 | 12480 |
| s48(id=40 S3->S1) | sw06-p5 | Q7 | 265920 | 12480 |
| s48(id=40 S3->S1) | sw04-p4 | Q7 | 271040 | 12480 |
| s48(id=40 S3->S1) | sw02-p2 | Q7 | 276160 | 12480 |
| s30(id=22 S2->S1) | S2-p0 | Q7 | 212480 | 12480 |
| s30(id=22 S2->S1) | sw08-p4 | Q7 | 220800 | 12480 |
| s30(id=22 S2->S1) | sw06-p5 | Q7 | 229120 | 12480 |
| s30(id=22 S2->S1) | sw04-p4 | Q7 | 237440 | 12480 |
| s30(id=22 S2->S1) | sw02-p2 | Q7 | 245760 | 12480 |
| s32(id=24 S2->S1) | S2-p0 | Q7 | 224960 | 12480 |
| s32(id=24 S2->S1) | sw08-p4 | Q7 | 233280 | 12480 |
| s32(id=24 S2->S1) | sw06-p5 | Q7 | 241600 | 12480 |
| s32(id=24 S2->S1) | sw04-p4 | Q7 | 249920 | 12480 |
| s32(id=24 S2->S1) | sw02-p2 | Q7 | 258240 | 12480 |
| s33(id=25 S1->S2) | S1-p0 | Q6 | 212480 | 12480 |
| s33(id=25 S1->S2) | sw02-p4 | Q6 | 220160 | 12480 |
| s33(id=25 S1->S2) | sw04-p5 | Q6 | 227840 | 12480 |
| s33(id=25 S1->S2) | sw06-p4 | Q6 | 235520 | 12480 |
| s33(id=25 S1->S2) | sw08-p2 | Q6 | 250880 | 12480 |
| s41(id=33 S1->S2) | S1-p0 | Q6 | 249920 | 12480 |
| s41(id=33 S1->S2) | sw02-p4 | Q6 | 258240 | 12480 |
| s41(id=33 S1->S2) | sw04-p5 | Q6 | 266560 | 12480 |
| s41(id=33 S1->S2) | sw06-p4 | Q6 | 274880 | 12480 |
| s41(id=33 S1->S2) | sw08-p2 | Q6 | 281600 | 12480 |
| s42(id=34 S1->S2) | S1-p0 | Q6 | 262400 | 12480 |
| s42(id=34 S1->S2) | sw02-p4 | Q6 | 270720 | 12480 |
| s42(id=34 S1->S2) | sw04-p5 | Q6 | 279040 | 12480 |
| s42(id=34 S1->S2) | sw06-p4 | Q6 | 287360 | 12480 |
| s42(id=34 S1->S2) | sw08-p2 | Q6 | 294080 | 12480 |
| s44(id=36 S1->S2) | S1-p0 | Q6 | 274880 | 12480 |
| s44(id=36 S1->S2) | sw02-p4 | Q6 | 283200 | 12480 |
| s44(id=36 S1->S2) | sw04-p5 | Q6 | 291520 | 12480 |
| s44(id=36 S1->S2) | sw06-p4 | Q6 | 299840 | 12480 |
| s44(id=36 S1->S2) | sw08-p2 | Q6 | 308160 | 12480 |
| s57(id=49 S2->S1) | S2-p0 | Q7 | 262080 | 12480 |
| s57(id=49 S2->S1) | sw08-p4 | Q7 | 273280 | 12480 |
| s57(id=49 S2->S1) | sw06-p5 | Q7 | 280000 | 12480 |
| s57(id=49 S2->S1) | sw04-p4 | Q7 | 286720 | 12480 |
| s57(id=49 S2->S1) | sw02-p2 | Q7 | 293440 | 12480 |
| s36(id=28 S3->S2) | S3-p0 | Q6 | 111040 | 12480 |
| s36(id=28 S3->S2) | sw01-p4 | Q6 | 116160 | 12480 |
| s36(id=28 S3->S2) | sw03-p5 | Q6 | 121280 | 12480 |
| s36(id=28 S3->S2) | sw05-p4 | Q6 | 200000 | 12480 |
| s36(id=28 S3->S2) | sw07-p5 | Q6 | 205120 | 12480 |
| s36(id=28 S3->S2) | sw08-p2 | Q6 | 212480 | 12480 |

## Constraint check

- C1-C7, C9: OK
- window-boundary integrity (no window's psi/delta changed anywhere): OK

## GCL per egress port

### sw01-p2  (17 entries, util 20.2800 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 49600 0x40 # 01000000   Q6
sgs 20160 0x3F # 00111111   BE
sgs 51200 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 120960 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 120960 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 29440 0x40 # 01000000   Q6
sgs 29120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p4  (22 entries, util 24.9600 %)

```
sgs 5120 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13440 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 14720 0x3F # 00111111   BE
sgs 57920 0x40 # 01000000   Q6
sgs 33920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 5120 0x3F # 00111111   BE
sgs 111040 0x80 # 10000000   Q7
sgs 33920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 5120 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13440 0x7F # 01111111   Q6
sgs 85120 0x40 # 01000000   Q6
sgs 33920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 5120 0x3F # 00111111   BE
sgs 105920 0x80 # 10000000   Q7
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (23 entries, util 31.2000 %)

```
sgs 26880 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 10560 0x3F # 00111111   BE
sgs 14400 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 23360 0xBF # 10111111   Q7
sgs 16320 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 21120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 26880 0x7F # 01111111   Q6
sgs 96640 0x80 # 10000000   Q7
sgs 26560 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 26880 0x7F # 01111111   Q6
sgs 96640 0x80 # 10000000   Q7
sgs 26560 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 26880 0x7F # 01111111   Q6
sgs 69760 0x80 # 10000000   Q7
sgs 3520 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p4  (28 entries, util 40.5600 %)

```
sgs 7680 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 13120 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 10240 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 13440 0x3F # 00111111   BE
sgs 50240 0x40 # 01000000   Q6
sgs 42240 0xBF # 10111111   Q7
sgs 7680 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 13120 0x7F # 01111111   Q6
sgs 124480 0x40 # 01000000   Q6
sgs 42240 0xBF # 10111111   Q7
sgs 7680 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 13120 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 10240 0x3F # 00111111   BE
sgs 101760 0x80 # 10000000   Q7
sgs 42240 0xBF # 10111111   Q7
sgs 7680 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 13120 0x7F # 01111111   Q6
sgs 116800 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (20 entries, util 20.2800 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 25280 0x40 # 01000000   Q6
sgs 13440 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 15680 0x7F # 01111111   Q6
sgs 3520 0x3F # 00111111   BE
sgs 50560 0x40 # 01000000   Q6
sgs 45760 0x7F # 01111111   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 120960 0x40 # 01000000   Q6
sgs 45760 0x7F # 01111111   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 120960 0x40 # 01000000   Q6
sgs 45760 0x7F # 01111111   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 37760 0x40 # 01000000   Q6
sgs 29120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p5  (23 entries, util 24.9600 %)

```
sgs 10240 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 14400 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 16640 0xBF # 10111111   Q7
sgs 54720 0x40 # 01000000   Q6
sgs 28800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 10240 0x3F # 00111111   BE
sgs 111040 0x80 # 10000000   Q7
sgs 28800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 10240 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 14400 0x7F # 01111111   Q6
sgs 84160 0x40 # 01000000   Q6
sgs 28800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 10240 0x3F # 00111111   BE
sgs 100800 0x80 # 10000000   Q7
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p4  (23 entries, util 31.2000 %)

```
sgs 20160 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 17280 0x7F # 01111111   Q6
sgs 7680 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 30080 0xBF # 10111111   Q7
sgs 8000 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 29440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 96640 0x80 # 10000000   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 96640 0x80 # 10000000   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 76480 0x80 # 10000000   Q7
sgs 3520 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (28 entries, util 40.5600 %)

```
sgs 15360 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 13760 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 8000 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13760 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0x7F # 01111111   Q6
sgs 50240 0x40 # 01000000   Q6
sgs 34560 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 13760 0x7F # 01111111   Q6
sgs 123840 0x40 # 01000000   Q6
sgs 34560 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 13760 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 8000 0x3F # 00111111   BE
sgs 103360 0x80 # 10000000   Q7
sgs 34560 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 13760 0x7F # 01111111   Q6
sgs 108480 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (22 entries, util 24.9600 %)

```
sgs 15360 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 19200 0xBF # 10111111   Q7
sgs 51520 0x40 # 01000000   Q6
sgs 23680 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 111040 0x80 # 10000000   Q7
sgs 23680 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 83200 0x40 # 01000000   Q6
sgs 23680 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 95680 0x80 # 10000000   Q7
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p5  (22 entries, util 20.2800 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 25280 0x40 # 01000000   Q6
sgs 15040 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 18240 0x7F # 01111111   Q6
sgs 49920 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 120960 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 120960 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 46080 0x40 # 01000000   Q6
sgs 29120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p4  (28 entries, util 40.5600 %)

```
sgs 23040 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 14400 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 15360 0x7F # 01111111   Q6
sgs 50240 0x40 # 01000000   Q6
sgs 26880 0xBF # 10111111   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0x7F # 01111111   Q6
sgs 123200 0x40 # 01000000   Q6
sgs 26880 0xBF # 10111111   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 104960 0x80 # 10000000   Q7
sgs 26880 0xBF # 10111111   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0x7F # 01111111   Q6
sgs 100160 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (22 entries, util 31.2000 %)

```
sgs 13440 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24000 0x7F # 01111111   Q6
sgs 960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 36480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 37760 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 13440 0x7F # 01111111   Q6
sgs 96640 0x80 # 10000000   Q7
sgs 40000 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 13440 0x7F # 01111111   Q6
sgs 96640 0x80 # 10000000   Q7
sgs 40000 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 13440 0x7F # 01111111   Q6
sgs 83200 0x80 # 10000000   Q7
sgs 3520 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (22 entries, util 20.2800 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 25280 0x40 # 01000000   Q6
sgs 16640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 17280 0x7F # 01111111   Q6
sgs 49280 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 120960 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 120960 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 54400 0x40 # 01000000   Q6
sgs 29120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p5  (22 entries, util 24.9600 %)

```
sgs 20480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 16320 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 21440 0xBF # 10111111   Q7
sgs 48320 0x40 # 01000000   Q6
sgs 18560 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 111040 0x80 # 10000000   Q7
sgs 18560 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 16320 0x7F # 01111111   Q6
sgs 82240 0x40 # 01000000   Q6
sgs 18560 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 90560 0x80 # 10000000   Q7
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p2  (24 entries, util 46.8000 %)

```
sgs 25600 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 29440 0x40 # 01000000   Q6
sgs 6400 0x3F # 00111111   BE
sgs 101440 0x80 # 10000000   Q7
sgs 24320 0xBF # 10111111   Q7
sgs 25600 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 137280 0x40 # 01000000   Q6
sgs 24320 0xBF # 10111111   Q7
sgs 25600 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 29440 0x40 # 01000000   Q6
sgs 6400 0x3F # 00111111   BE
sgs 101440 0x80 # 10000000   Q7
sgs 24320 0xBF # 10111111   Q7
sgs 25600 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 111680 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p4  (21 entries, util 31.2000 %)

```
sgs 6720 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 34880 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 46080 0x7F # 01111111   Q6
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

### sw08-p5  (23 entries, util 20.2800 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 8320 0x3F # 00111111   BE
sgs 25280 0x40 # 01000000   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 1600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 16320 0x7F # 01111111   Q6
sgs 48640 0x40 # 01000000   Q6
sgs 20800 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 8320 0x3F # 00111111   BE
sgs 120960 0x40 # 01000000   Q6
sgs 20800 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 8320 0x3F # 00111111   BE
sgs 120960 0x40 # 01000000   Q6
sgs 20800 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 8320 0x3F # 00111111   BE
sgs 62720 0x40 # 01000000   Q6
sgs 29120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

