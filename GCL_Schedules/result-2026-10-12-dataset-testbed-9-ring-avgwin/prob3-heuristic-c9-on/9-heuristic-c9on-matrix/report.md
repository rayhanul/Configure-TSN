# Reconfiguration-free admission (Problem 3)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Frozen schedule W loaded from: **result/result-2026-10-12-dataset-testbed-9-ring-avgwin/heuristic-c9-on/9-matrix-c9on**

## Admission: W (before) vs. after this run's arrivals

| | admitted | of total |
|---|---|---|
| W (base, unchanged) | 11 | 11 |
| + this run's arrivals | 26 | 39 |

Every arrival admitted here required **zero** window-boundary changes -- see the GCL-entry table below (unchanged from W by construction) and the window-boundary integrity check. No previously-admitted flow was rerouted.

## Arrivals

| id | src->dst | RS(s) size | admitted | route | queue | phi_s (ns) | e2e (ns) | rerouted to make room | reason if rejected |
|---|---|---|---|---|---|---|---|---|---|
| 3 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 15 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 13 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 212480 | 46080 | - | - |
| 18 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 19 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 | 49920 | 46080 | - | - |
| 17 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 112320 | 45760 | - | - |
| 2 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q6 | 0 | 45440 | - | - |
| 5 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q7 | 77120 | 88320 | - | - |
| 11 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 62400 | 328000 | - | - |
| 27 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q7 | 74880 | 115520 | - | - |
| 30 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q6 | 134720 | 85440 | - | - |
| 31 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q7 | 462400 | 128000 | - | - |
| 33 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q6 | 224960 | 27840 | - | - |
| 39 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q7 | 150080 | 27840 | - | - |
| 44 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q7 | 474880 | 287680 | - | - |
| 26 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 87360 | 103040 | - | - |
| 29 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 150080 | 215360 | - | - |
| 32 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q6 | 237440 | 27840 | - | - |
| 40 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 | 99840 | 54080 | - | - |
| 41 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q7 | 162560 | 215680 | - | - |
| 43 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 162560 | 228480 | - | - |
| 49 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q6 | 249920 | 29120 | - | - |
| 22 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q6 | 37440 | 175040 | - | - |
| 23 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 124800 | 45760 | - | - |
| 42 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 224960 | 66880 | - | - |
| 25 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 | 112320 | 73280 | - | - |
| 34 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 37 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 | 150080 | 48000 | - | - |
| 38 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 237440 | 54080 | - | - |
| 46 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 350080 | 249920 | - | - |
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
| sw01-p2 | 17 | 17 | 255 |
| sw01-p4 | 10 | 10 | 255 |
| sw01-p5 | 24 | 24 | 255 |
| sw02-p2 | 23 | 23 | 255 |
| sw02-p4 | 9 | 9 | 255 |
| sw02-p5 | 20 | 20 | 255 |
| sw03-p4 | 22 | 22 | 255 |
| sw03-p5 | 11 | 11 | 255 |
| sw04-p4 | 17 | 17 | 255 |
| sw04-p5 | 9 | 9 | 255 |
| sw05-p4 | 11 | 11 | 255 |
| sw05-p5 | 21 | 21 | 255 |
| sw06-p4 | 9 | 9 | 255 |
| sw06-p5 | 19 | 19 | 255 |
| sw07-p4 | 22 | 22 | 255 |
| sw07-p5 | 11 | 11 | 255 |
| sw08-p2 | 11 | 11 | 255 |
| sw08-p4 | 17 | 17 | 255 |
| sw08-p5 | 23 | 23 | 255 |

## Per-hop windows used by newly admitted flows

| flow | egress port | queue | psi (ns, unchanged) | delta (ns, unchanged) |
|---|---|---|---|---|
| s24(id=13 S2->S3) | S2-p0 | Q6 | 212480 | 12480 |
| s24(id=13 S2->S3) | sw08-p5 | Q6 | 219200 | 12480 |
| s24(id=13 S2->S3) | sw07-p4 | Q6 | 225920 | 12480 |
| s24(id=13 S2->S3) | sw05-p5 | Q6 | 232640 | 12480 |
| s24(id=13 S2->S3) | sw03-p4 | Q6 | 239360 | 12480 |
| s24(id=13 S2->S3) | sw01-p2 | Q6 | 246080 | 12480 |
| s28(id=19 S3->S2) | S3-p0 | Q7 | 49920 | 12480 |
| s28(id=19 S3->S2) | sw01-p4 | Q7 | 56640 | 12480 |
| s28(id=19 S3->S2) | sw03-p5 | Q7 | 63360 | 12480 |
| s28(id=19 S3->S2) | sw05-p4 | Q7 | 70080 | 12480 |
| s28(id=19 S3->S2) | sw07-p5 | Q7 | 76800 | 12480 |
| s28(id=19 S3->S2) | sw08-p2 | Q7 | 83520 | 12480 |
| s26(id=17 S2->S1) | S2-p0 | Q6 | 112320 | 12480 |
| s26(id=17 S2->S1) | sw08-p4 | Q6 | 120640 | 12480 |
| s26(id=17 S2->S1) | sw06-p5 | Q6 | 128960 | 12480 |
| s26(id=17 S2->S1) | sw04-p4 | Q6 | 137280 | 12480 |
| s26(id=17 S2->S1) | sw02-p2 | Q6 | 145600 | 12480 |
| s20(id=2 S3->S2) | S3-p0 | Q6 | 0 | 12480 |
| s20(id=2 S3->S2) | sw01-p4 | Q6 | 12480 | 12480 |
| s20(id=2 S3->S2) | sw03-p5 | Q6 | 17600 | 12480 |
| s20(id=2 S3->S2) | sw05-p4 | Q6 | 22720 | 12480 |
| s20(id=2 S3->S2) | sw07-p5 | Q6 | 27840 | 12480 |
| s20(id=2 S3->S2) | sw08-p2 | Q6 | 32960 | 12480 |
| s22(id=5 S1->S3) | S1-p0 | Q7 | 77120 | 12480 |
| s22(id=5 S1->S3) | sw02-p5 | Q7 | 83840 | 12480 |
| s22(id=5 S1->S3) | sw01-p2 | Q7 | 152960 | 12480 |
| s23(id=11 S2->S1) | S2-p0 | Q7 | 62400 | 12480 |
| s23(id=11 S2->S1) | sw08-p4 | Q7 | 73280 | 12480 |
| s23(id=11 S2->S1) | sw06-p5 | Q7 | 81600 | 12480 |
| s23(id=11 S2->S1) | sw04-p4 | Q7 | 350080 | 12480 |
| s23(id=11 S2->S1) | sw02-p2 | Q7 | 377920 | 12480 |
| s35(id=27 S3->S1) | S3-p0 | Q7 | 74880 | 12480 |
| s35(id=27 S3->S1) | sw01-p5 | Q7 | 150080 | 12480 |
| s35(id=27 S3->S1) | sw02-p2 | Q7 | 177920 | 12480 |
| s38(id=30 S3->S1) | S3-p0 | Q6 | 134720 | 12480 |
| s38(id=30 S3->S1) | sw01-p5 | Q6 | 200000 | 12480 |
| s38(id=30 S3->S1) | sw02-p2 | Q6 | 207680 | 12480 |
| s39(id=31 S3->S1) | S3-p0 | Q7 | 462400 | 12480 |
| s39(id=31 S3->S1) | sw01-p5 | Q7 | 470080 | 12480 |
| s39(id=31 S3->S1) | sw02-p2 | Q7 | 577920 | 12480 |
| s41(id=33 S3->S1) | S3-p0 | Q6 | 224960 | 12480 |
| s41(id=33 S3->S1) | sw01-p5 | Q6 | 232640 | 12480 |
| s41(id=33 S3->S1) | sw02-p2 | Q6 | 240320 | 12480 |
| s47(id=39 S1->S3) | S1-p0 | Q7 | 150080 | 12480 |
| s47(id=39 S1->S3) | sw02-p5 | Q7 | 157760 | 12480 |
| s47(id=39 S1->S3) | sw01-p2 | Q7 | 165440 | 12480 |
| s52(id=44 S3->S1) | S3-p0 | Q7 | 474880 | 12480 |
| s52(id=44 S3->S1) | sw01-p5 | Q7 | 583040 | 12480 |
| s52(id=44 S3->S1) | sw02-p2 | Q7 | 750080 | 12480 |
| s34(id=26 S2->S3) | S2-p0 | Q7 | 87360 | 12480 |
| s34(id=26 S2->S3) | sw08-p5 | Q7 | 150080 | 12480 |
| s34(id=26 S2->S3) | sw07-p4 | Q7 | 156160 | 12480 |
| s34(id=26 S2->S3) | sw05-p5 | Q7 | 162240 | 12480 |
| s34(id=26 S2->S3) | sw03-p4 | Q7 | 168320 | 12480 |
| s34(id=26 S2->S3) | sw01-p2 | Q7 | 177920 | 12480 |
| s37(id=29 S2->S3) | S2-p0 | Q7 | 150080 | 12480 |
| s37(id=29 S2->S3) | sw08-p5 | Q7 | 162560 | 12480 |
| s37(id=29 S2->S3) | sw07-p4 | Q7 | 170240 | 12480 |
| s37(id=29 S2->S3) | sw05-p5 | Q7 | 177920 | 12480 |
| s37(id=29 S2->S3) | sw03-p4 | Q7 | 185600 | 12480 |
| s37(id=29 S2->S3) | sw01-p2 | Q7 | 352960 | 12480 |
| s40(id=32 S3->S1) | S3-p0 | Q6 | 237440 | 12480 |
| s40(id=32 S3->S1) | sw01-p5 | Q6 | 245120 | 12480 |
| s40(id=32 S3->S1) | sw02-p2 | Q6 | 252800 | 12480 |
| s48(id=40 S3->S2) | S3-p0 | Q7 | 99840 | 12480 |
| s48(id=40 S3->S2) | sw01-p4 | Q7 | 108160 | 12480 |
| s48(id=40 S3->S2) | sw03-p5 | Q7 | 116480 | 12480 |
| s48(id=40 S3->S2) | sw05-p4 | Q7 | 124800 | 12480 |
| s48(id=40 S3->S2) | sw07-p5 | Q7 | 133120 | 12480 |
| s48(id=40 S3->S2) | sw08-p2 | Q7 | 141440 | 12480 |
| s49(id=41 S1->S3) | S1-p0 | Q7 | 162560 | 12480 |
| s49(id=41 S1->S3) | sw02-p5 | Q7 | 359680 | 12480 |
| s49(id=41 S1->S3) | sw01-p2 | Q7 | 365760 | 12480 |
| s51(id=43 S2->S3) | S2-p0 | Q7 | 162560 | 12480 |
| s51(id=43 S2->S3) | sw08-p5 | Q7 | 175040 | 12480 |
| s51(id=43 S2->S3) | sw07-p4 | Q7 | 182720 | 12480 |
| s51(id=43 S2->S3) | sw05-p5 | Q7 | 350080 | 12480 |
| s51(id=43 S2->S3) | sw03-p4 | Q7 | 373440 | 12480 |
| s51(id=43 S2->S3) | sw01-p2 | Q7 | 378560 | 12480 |
| s57(id=49 S3->S1) | S3-p0 | Q6 | 249920 | 12480 |
| s57(id=49 S3->S1) | sw01-p5 | Q6 | 258240 | 12480 |
| s57(id=49 S3->S1) | sw02-p2 | Q6 | 266560 | 12480 |
| s30(id=22 S1->S2) | S1-p0 | Q6 | 37440 | 12480 |
| s30(id=22 S1->S2) | sw02-p4 | Q6 | 43520 | 12480 |
| s30(id=22 S1->S2) | sw04-p5 | Q6 | 49600 | 12480 |
| s30(id=22 S1->S2) | sw06-p4 | Q6 | 55680 | 12480 |
| s30(id=22 S1->S2) | sw08-p2 | Q6 | 100160 | 12480 |
| s31(id=23 S2->S1) | S2-p0 | Q6 | 124800 | 12480 |
| s31(id=23 S2->S1) | sw08-p4 | Q6 | 133120 | 12480 |
| s31(id=23 S2->S1) | sw06-p5 | Q6 | 141440 | 12480 |
| s31(id=23 S2->S1) | sw04-p4 | Q6 | 149760 | 12480 |
| s31(id=23 S2->S1) | sw02-p2 | Q6 | 158080 | 12480 |
| s50(id=42 S2->S1) | S2-p0 | Q6 | 224960 | 12480 |
| s50(id=42 S2->S1) | sw08-p4 | Q6 | 230080 | 12480 |
| s50(id=42 S2->S1) | sw06-p5 | Q6 | 235200 | 12480 |
| s50(id=42 S2->S1) | sw04-p4 | Q6 | 274240 | 12480 |
| s50(id=42 S2->S1) | sw02-p2 | Q6 | 279360 | 12480 |
| s33(id=25 S3->S2) | S3-p0 | Q7 | 112320 | 12480 |
| s33(id=25 S3->S2) | sw01-p4 | Q7 | 120640 | 12480 |
| s33(id=25 S3->S2) | sw03-p5 | Q7 | 128960 | 12480 |
| s33(id=25 S3->S2) | sw05-p4 | Q7 | 137280 | 12480 |
| s33(id=25 S3->S2) | sw07-p5 | Q7 | 145600 | 12480 |
| s33(id=25 S3->S2) | sw08-p2 | Q7 | 153920 | 12480 |
| s45(id=37 S3->S2) | S3-p0 | Q7 | 150080 | 12480 |
| s45(id=37 S3->S2) | sw01-p4 | Q7 | 156800 | 12480 |
| s45(id=37 S3->S2) | sw03-p5 | Q7 | 163520 | 12480 |
| s45(id=37 S3->S2) | sw05-p4 | Q7 | 170240 | 12480 |
| s45(id=37 S3->S2) | sw07-p5 | Q7 | 176960 | 12480 |
| s45(id=37 S3->S2) | sw08-p2 | Q7 | 183680 | 12480 |
| s46(id=38 S2->S3) | S2-p0 | Q6 | 237440 | 12480 |
| s46(id=38 S2->S3) | sw08-p5 | Q6 | 245760 | 12480 |
| s46(id=38 S2->S3) | sw07-p4 | Q6 | 254080 | 12480 |
| s46(id=38 S2->S3) | sw05-p5 | Q6 | 262400 | 12480 |
| s46(id=38 S2->S3) | sw03-p4 | Q6 | 270720 | 12480 |
| s46(id=38 S2->S3) | sw01-p2 | Q6 | 279040 | 12480 |
| s54(id=46 S2->S3) | S2-p0 | Q7 | 350080 | 12480 |
| s54(id=46 S2->S3) | sw08-p5 | Q7 | 356160 | 12480 |
| s54(id=46 S2->S3) | sw07-p4 | Q7 | 362240 | 12480 |
| s54(id=46 S2->S3) | sw05-p5 | Q7 | 379520 | 12480 |
| s54(id=46 S2->S3) | sw03-p4 | Q7 | 581440 | 12480 |
| s54(id=46 S2->S3) | sw01-p2 | Q7 | 587520 | 12480 |

## Constraint check

- C1-C7, C9: OK
- window-boundary integrity (no window's psi/delta changed anywhere): OK

## GCL per egress port

### sw01-p2  (17 entries, util 35.8800 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 2880 0x3F # 00111111   BE
sgs 35520 0x40 # 01000000   Q6
sgs 49280 0xBF # 10111111   Q7
sgs 13120 0x7F # 01111111   Q6
sgs 39680 0x40 # 01000000   Q6
sgs 47040 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 137600 0x40 # 01000000   Q6
sgs 47040 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 137600 0x40 # 01000000   Q6
sgs 47040 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 122240 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p4  (10 entries, util 14.0400 %)

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

### sw01-p5  (24 entries, util 24.9600 %)

```
sgs 20160 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 17280 0x7F # 01111111   Q6
sgs 3200 0x3F # 00111111   BE
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
sgs 17280 0x7F # 01111111   Q6
sgs 3200 0x3F # 00111111   BE
sgs 78080 0x80 # 10000000   Q7
sgs 18880 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 90880 0x40 # 01000000   Q6
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (23 entries, util 43.6800 %)

```
sgs 27840 0x7F # 01111111   Q6
sgs 30080 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 3840 0x3F # 00111111   BE
sgs 25280 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 24000 0x7F # 01111111   Q6
sgs 53760 0x40 # 01000000   Q6
sgs 22080 0xBF # 10111111   Q7
sgs 27840 0x7F # 01111111   Q6
sgs 150080 0x40 # 01000000   Q6
sgs 22080 0xBF # 10111111   Q7
sgs 27840 0x7F # 01111111   Q6
sgs 30080 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 16640 0xBF # 10111111   Q7
sgs 90560 0x40 # 01000000   Q6
sgs 22080 0xBF # 10111111   Q7
sgs 27840 0x7F # 01111111   Q6
sgs 122240 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
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

### sw02-p5  (20 entries, util 14.0400 %)

```
sgs 7680 0x3F # 00111111   BE
sgs 50240 0x40 # 01000000   Q6
sgs 42240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 7680 0x3F # 00111111   BE
sgs 50240 0x40 # 01000000   Q6
sgs 42240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 7680 0x3F # 00111111   BE
sgs 50240 0x40 # 01000000   Q6
sgs 42240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 7680 0x3F # 00111111   BE
sgs 42560 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (22 entries, util 21.8400 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 8000 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 16960 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 5440 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 32000 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 94720 0x40 # 01000000   Q6
sgs 34880 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 94720 0x40 # 01000000   Q6
sgs 34880 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 74240 0x40 # 01000000   Q6
sgs 5440 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p5  (11 entries, util 14.0400 %)

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

### sw04-p4  (17 entries, util 18.7200 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 27840 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 24640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 10240 0x3F # 00111111   BE
sgs 17920 0x7F # 01111111   Q6
sgs 216960 0x40 # 01000000   Q6
sgs 15040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 40320 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 24640 0xBF # 10111111   Q7
sgs 217280 0x40 # 01000000   Q6
sgs 5440 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
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

### sw05-p4  (11 entries, util 14.0400 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 12160 0x3F # 00111111   BE
sgs 425280 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p5  (21 entries, util 21.8400 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 2880 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 22080 0x7F # 01111111   Q6
sgs 48000 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 39680 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 94720 0x40 # 01000000   Q6
sgs 40000 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 94720 0x40 # 01000000   Q6
sgs 40000 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 79360 0x40 # 01000000   Q6
sgs 5440 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
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

### sw06-p5  (19 entries, util 18.7200 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 22720 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 2240 0x3F # 00111111   BE
sgs 19200 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 18560 0xBF # 10111111   Q7
sgs 11840 0x3F # 00111111   BE
sgs 217920 0x40 # 01000000   Q6
sgs 20160 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 35200 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 2240 0x3F # 00111111   BE
sgs 19200 0xBF # 10111111   Q7
sgs 225600 0x40 # 01000000   Q6
sgs 5440 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (22 entries, util 21.8400 %)

```
sgs 10240 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 27200 0x7F # 01111111   Q6
sgs 40320 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 47360 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 10240 0x3F # 00111111   BE
sgs 77120 0x40 # 01000000   Q6
sgs 12800 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 10240 0x3F # 00111111   BE
sgs 77120 0x40 # 01000000   Q6
sgs 12800 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 10240 0x3F # 00111111   BE
sgs 66880 0x40 # 01000000   Q6
sgs 23040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p5  (11 entries, util 14.0400 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 416960 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p2  (11 entries, util 18.7200 %)

```
sgs 49280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 38400 0xBF # 10111111   Q7
sgs 28800 0x7F # 01111111   Q6
sgs 412800 0x80 # 10000000   Q7
sgs 8320 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p4  (17 entries, util 18.7200 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 17600 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 18240 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 26880 0xBF # 10111111   Q7
sgs 5760 0x3F # 00111111   BE
sgs 218880 0x40 # 01000000   Q6
sgs 25280 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 30080 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 18240 0x3F # 00111111   BE
sgs 233920 0x40 # 01000000   Q6
sgs 5440 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (23 entries, util 21.8400 %)

```
sgs 5120 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 32320 0x7F # 01111111   Q6
sgs 32640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 5120 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 5120 0x3F # 00111111   BE
sgs 77120 0x40 # 01000000   Q6
sgs 17920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 5120 0x3F # 00111111   BE
sgs 77120 0x40 # 01000000   Q6
sgs 17920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 5120 0x3F # 00111111   BE
sgs 72000 0x40 # 01000000   Q6
sgs 23040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

