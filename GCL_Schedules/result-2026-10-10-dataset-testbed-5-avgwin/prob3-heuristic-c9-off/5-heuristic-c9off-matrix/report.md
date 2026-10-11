# Reconfiguration-free admission (Problem 3)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Frozen schedule W loaded from: **result/result-2026-10-10-dataset-testbed-5-avgwin/heuristic-c9-off/5-matrix-c9off**

## Admission: W (before) vs. after this run's arrivals

| | admitted | of total |
|---|---|---|
| W (base, unchanged) | 10 | 10 |
| + this run's arrivals | 14 | 40 |

Every arrival admitted here required **zero** window-boundary changes -- see the GCL-entry table below (unchanged from W by construction) and the window-boundary integrity check. No previously-admitted flow was rerouted.

## Arrivals

| id | src->dst | RS(s) size | admitted | route | queue | phi_s (ns) | e2e (ns) | rerouted to make room | reason if rejected |
|---|---|---|---|---|---|---|---|---|---|
| 8 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 14 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 15 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 20 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 18 | S1->S3 | - | yes | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 100160 | 212480 | - | - |
| 6 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 75200 | 320640 | - | - |
| 7 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 11 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 225600 | 103680 | - | - |
| 1 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q6 | 0 | 412480 | - | - |
| 4 | S1->S3 | - | yes | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 49920 | 429120 | - | - |
| 36 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 42 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 50 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 87680 | 79040 | - | - |
| 30 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 238400 | 95680 | - | - |
| 37 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 350080 | 245760 | - | - |
| 22 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q6 | 24960 | 610560 | - | - |
| 28 | S1->S3 | - | yes | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 122240 | 386240 | - | - |
| 31 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q6 | 200000 | 512640 | - | - |
| 43 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q6 | 333440 | 395840 | - | - |
| 45 | S1->S3 | - | yes | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 322240 | 206720 | - | - |
| 21 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 25 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 24 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 33 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 35 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 39 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 48 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 26 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 29 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 34 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q7 | 75200 | 187200 | - | - |
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
| sw01-p2 | 23 | 23 | 255 |
| sw01-p4 | 20 | 20 | 255 |
| sw02-p2 | 15 | 15 | 255 |
| sw02-p4 | 24 | 24 | 255 |
| sw03-p4 | 24 | 24 | 255 |
| sw03-p5 | 18 | 18 | 255 |
| sw04-p4 | 14 | 14 | 255 |
| sw04-p5 | 21 | 21 | 255 |
| sw05-p4 | 22 | 22 | 255 |
| sw05-p5 | 22 | 22 | 255 |
| sw06-p4 | 19 | 19 | 255 |
| sw06-p5 | 14 | 14 | 255 |
| sw07-p4 | 22 | 22 | 255 |
| sw07-p5 | 19 | 19 | 255 |
| sw08-p2 | 29 | 29 | 255 |
| sw08-p4 | 14 | 14 | 255 |
| sw08-p5 | 23 | 23 | 255 |

## Per-hop windows used by newly admitted flows

| flow | egress port | queue | psi (ns, unchanged) | delta (ns, unchanged) |
|---|---|---|---|---|
| s28(id=18 S1->S3) | S1-p0 | Q6 | 100160 | 12480 |
| s28(id=18 S1->S3) | sw02-p4 | Q6 | 116800 | 12480 |
| s28(id=18 S1->S3) | sw04-p5 | Q6 | 133440 | 12480 |
| s28(id=18 S1->S3) | sw06-p4 | Q6 | 212800 | 12480 |
| s28(id=18 S1->S3) | sw08-p5 | Q6 | 229440 | 12480 |
| s28(id=18 S1->S3) | sw07-p4 | Q6 | 246080 | 12480 |
| s28(id=18 S1->S3) | sw05-p5 | Q6 | 262720 | 12480 |
| s28(id=18 S1->S3) | sw03-p4 | Q6 | 279360 | 12480 |
| s28(id=18 S1->S3) | sw01-p2 | Q6 | 296000 | 12480 |
| s22(id=6 S2->S3) | S2-p0 | Q7 | 75200 | 12480 |
| s22(id=6 S2->S3) | sw08-p5 | Q7 | 166400 | 12480 |
| s22(id=6 S2->S3) | sw07-p4 | Q7 | 183040 | 12480 |
| s22(id=6 S2->S3) | sw05-p5 | Q7 | 350080 | 12480 |
| s22(id=6 S2->S3) | sw03-p4 | Q7 | 366720 | 12480 |
| s22(id=6 S2->S3) | sw01-p2 | Q7 | 383360 | 12480 |
| s25(id=11 S2->S3) | S2-p0 | Q6 | 225600 | 12480 |
| s25(id=11 S2->S3) | sw08-p5 | Q6 | 242240 | 12480 |
| s25(id=11 S2->S3) | sw07-p4 | Q6 | 258880 | 12480 |
| s25(id=11 S2->S3) | sw05-p5 | Q6 | 275520 | 12480 |
| s25(id=11 S2->S3) | sw03-p4 | Q6 | 292160 | 12480 |
| s25(id=11 S2->S3) | sw01-p2 | Q6 | 308800 | 12480 |
| s20(id=1 S3->S1) | S3-p0 | Q6 | 0 | 12480 |
| s20(id=1 S3->S1) | sw01-p4 | Q6 | 16640 | 12480 |
| s20(id=1 S3->S1) | sw03-p5 | Q6 | 33280 | 12480 |
| s20(id=1 S3->S1) | sw05-p4 | Q6 | 200000 | 12480 |
| s20(id=1 S3->S1) | sw07-p5 | Q6 | 216640 | 12480 |
| s20(id=1 S3->S1) | sw08-p4 | Q6 | 300160 | 12480 |
| s20(id=1 S3->S1) | sw06-p5 | Q6 | 316800 | 12480 |
| s20(id=1 S3->S1) | sw04-p4 | Q6 | 333440 | 12480 |
| s20(id=1 S3->S1) | sw02-p2 | Q6 | 400000 | 12480 |
| s21(id=4 S1->S3) | S1-p0 | Q7 | 49920 | 12480 |
| s21(id=4 S1->S3) | sw02-p4 | Q7 | 68480 | 12480 |
| s21(id=4 S1->S3) | sw04-p5 | Q7 | 85120 | 12480 |
| s21(id=4 S1->S3) | sw06-p4 | Q7 | 172160 | 12480 |
| s21(id=4 S1->S3) | sw08-p5 | Q7 | 350080 | 12480 |
| s21(id=4 S1->S3) | sw07-p4 | Q7 | 366720 | 12480 |
| s21(id=4 S1->S3) | sw05-p5 | Q7 | 383360 | 12480 |
| s21(id=4 S1->S3) | sw03-p4 | Q7 | 449920 | 12480 |
| s21(id=4 S1->S3) | sw01-p2 | Q7 | 466560 | 12480 |
| s59(id=50 S2->S1) | S2-p0 | Q7 | 87680 | 12480 |
| s59(id=50 S2->S1) | sw08-p4 | Q7 | 104320 | 12480 |
| s59(id=50 S2->S1) | sw06-p5 | Q7 | 120960 | 12480 |
| s59(id=50 S2->S1) | sw04-p4 | Q7 | 137600 | 12480 |
| s59(id=50 S2->S1) | sw02-p2 | Q7 | 154240 | 12480 |
| s39(id=30 S2->S3) | S2-p0 | Q6 | 238400 | 12480 |
| s39(id=30 S2->S3) | sw08-p5 | Q6 | 255040 | 12480 |
| s39(id=30 S2->S3) | sw07-p4 | Q6 | 271680 | 12480 |
| s39(id=30 S2->S3) | sw05-p5 | Q6 | 288320 | 12480 |
| s39(id=30 S2->S3) | sw03-p4 | Q6 | 304960 | 12480 |
| s39(id=30 S2->S3) | sw01-p2 | Q6 | 321600 | 12480 |
| s46(id=37 S2->S3) | S2-p0 | Q7 | 350080 | 12480 |
| s46(id=37 S2->S3) | sw08-p5 | Q7 | 366720 | 12480 |
| s46(id=37 S2->S3) | sw07-p4 | Q7 | 383360 | 12480 |
| s46(id=37 S2->S3) | sw05-p5 | Q7 | 550080 | 12480 |
| s46(id=37 S2->S3) | sw03-p4 | Q7 | 566720 | 12480 |
| s46(id=37 S2->S3) | sw01-p2 | Q7 | 583360 | 12480 |
| s31(id=22 S3->S1) | S3-p0 | Q6 | 24960 | 12480 |
| s31(id=22 S3->S1) | sw01-p4 | Q6 | 200000 | 12480 |
| s31(id=22 S3->S1) | sw03-p5 | Q6 | 216640 | 12480 |
| s31(id=22 S3->S1) | sw05-p4 | Q6 | 233280 | 12480 |
| s31(id=22 S3->S1) | sw07-p5 | Q6 | 400000 | 12480 |
| s31(id=22 S3->S1) | sw08-p4 | Q6 | 416640 | 12480 |
| s31(id=22 S3->S1) | sw06-p5 | Q6 | 433280 | 12480 |
| s31(id=22 S3->S1) | sw04-p4 | Q6 | 606400 | 12480 |
| s31(id=22 S3->S1) | sw02-p2 | Q6 | 623040 | 12480 |
| s37(id=28 S1->S3) | S1-p0 | Q6 | 122240 | 12480 |
| s37(id=28 S1->S3) | sw02-p4 | Q6 | 200000 | 12480 |
| s37(id=28 S1->S3) | sw04-p5 | Q6 | 216640 | 12480 |
| s37(id=28 S1->S3) | sw06-p4 | Q6 | 412800 | 12480 |
| s37(id=28 S1->S3) | sw08-p5 | Q6 | 429440 | 12480 |
| s37(id=28 S1->S3) | sw07-p4 | Q6 | 446080 | 12480 |
| s37(id=28 S1->S3) | sw05-p5 | Q6 | 462720 | 12480 |
| s37(id=28 S1->S3) | sw03-p4 | Q6 | 479360 | 12480 |
| s37(id=28 S1->S3) | sw01-p2 | Q6 | 496000 | 12480 |
| s40(id=31 S3->S1) | S3-p0 | Q6 | 200000 | 12480 |
| s40(id=31 S3->S1) | sw01-p4 | Q6 | 216640 | 12480 |
| s40(id=31 S3->S1) | sw03-p5 | Q6 | 233280 | 12480 |
| s40(id=31 S3->S1) | sw05-p4 | Q6 | 400000 | 12480 |
| s40(id=31 S3->S1) | sw07-p5 | Q6 | 416640 | 12480 |
| s40(id=31 S3->S1) | sw08-p4 | Q6 | 433280 | 12480 |
| s40(id=31 S3->S1) | sw06-p5 | Q6 | 606400 | 12480 |
| s40(id=31 S3->S1) | sw04-p4 | Q6 | 623040 | 12480 |
| s40(id=31 S3->S1) | sw02-p2 | Q6 | 700160 | 12480 |
| s52(id=43 S3->S1) | S3-p0 | Q6 | 333440 | 12480 |
| s52(id=43 S3->S1) | sw01-p4 | Q6 | 400000 | 12480 |
| s52(id=43 S3->S1) | sw03-p5 | Q6 | 416640 | 12480 |
| s52(id=43 S3->S1) | sw05-p4 | Q6 | 433280 | 12480 |
| s52(id=43 S3->S1) | sw07-p5 | Q6 | 600000 | 12480 |
| s52(id=43 S3->S1) | sw08-p4 | Q6 | 616640 | 12480 |
| s52(id=43 S3->S1) | sw06-p5 | Q6 | 633280 | 12480 |
| s52(id=43 S3->S1) | sw04-p4 | Q6 | 700160 | 12480 |
| s52(id=43 S3->S1) | sw02-p2 | Q6 | 716800 | 12480 |
| s54(id=45 S1->S3) | S1-p0 | Q6 | 322240 | 12480 |
| s54(id=45 S1->S3) | sw02-p4 | Q6 | 400000 | 12480 |
| s54(id=45 S1->S3) | sw04-p5 | Q6 | 416640 | 12480 |
| s54(id=45 S1->S3) | sw06-p4 | Q6 | 433280 | 12480 |
| s54(id=45 S1->S3) | sw08-p5 | Q6 | 449920 | 12480 |
| s54(id=45 S1->S3) | sw07-p4 | Q6 | 466560 | 12480 |
| s54(id=45 S1->S3) | sw05-p5 | Q6 | 483200 | 12480 |
| s54(id=45 S1->S3) | sw03-p4 | Q6 | 499840 | 12480 |
| s54(id=45 S1->S3) | sw01-p2 | Q6 | 516480 | 12480 |
| s43(id=34 S3->S1) | S3-p0 | Q7 | 75200 | 12480 |
| s43(id=34 S3->S1) | sw01-p4 | Q7 | 91840 | 12480 |
| s43(id=34 S3->S1) | sw03-p5 | Q7 | 108480 | 12480 |
| s43(id=34 S3->S1) | sw05-p4 | Q7 | 125120 | 12480 |
| s43(id=34 S3->S1) | sw07-p5 | Q7 | 141760 | 12480 |
| s43(id=34 S3->S1) | sw08-p4 | Q7 | 158400 | 12480 |
| s43(id=34 S3->S1) | sw06-p5 | Q7 | 175040 | 12480 |
| s43(id=34 S3->S1) | sw04-p4 | Q7 | 191680 | 12480 |
| s43(id=34 S3->S1) | sw02-p2 | Q7 | 208320 | 12480 |

## Constraint check

- C1-C7, C9: OK
- window-boundary integrity (no window's psi/delta changed anywhere): OK

## GCL per egress port

### sw01-p2  (23 entries, util 26.5200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 4480 0x3F # 00111111   BE
sgs 45440 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 41920 0xBF # 10111111   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 16960 0x7F # 01111111   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 96640 0x40 # 01000000   Q6
sgs 20160 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 96640 0x40 # 01000000   Q6
sgs 20160 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 13440 0x40 # 01000000   Q6
sgs 3520 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p4  (20 entries, util 20.2800 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 71040 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 120960 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 96000 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 91840 0x80 # 10000000   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (15 entries, util 14.0400 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 3840 0x3F # 00111111   BE
sgs 206400 0x80 # 10000000   Q7
sgs 39680 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 3840 0x3F # 00111111   BE
sgs 102400 0x80 # 10000000   Q7
sgs 43520 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p4  (24 entries, util 20.2800 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 6080 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0xBF # 10111111   Q7
sgs 56000 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 122240 0x80 # 10000000   Q7
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 6080 0x3F # 00111111   BE
sgs 82880 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 105600 0x80 # 10000000   Q7
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (24 entries, util 26.5200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 21120 0xBF # 10111111   Q7
sgs 28800 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 8640 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 3840 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 33600 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 96640 0x40 # 01000000   Q6
sgs 36800 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 96640 0x40 # 01000000   Q6
sgs 36800 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 30080 0x40 # 01000000   Q6
sgs 3520 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p5  (18 entries, util 20.2800 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0xBF # 10111111   Q7
sgs 95360 0x80 # 10000000   Q7
sgs 33280 0xBF # 10111111   Q7
sgs 45760 0x7F # 01111111   Q6
sgs 120960 0x80 # 10000000   Q7
sgs 33280 0xBF # 10111111   Q7
sgs 45760 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0xBF # 10111111   Q7
sgs 95360 0x80 # 10000000   Q7
sgs 33280 0xBF # 10111111   Q7
sgs 45760 0x7F # 01111111   Q6
sgs 75200 0x80 # 10000000   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p4  (14 entries, util 14.0400 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 37440 0xBF # 10111111   Q7
sgs 206400 0x80 # 10000000   Q7
sgs 6400 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 37440 0xBF # 10111111   Q7
sgs 119040 0x80 # 10000000   Q7
sgs 43520 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (21 entries, util 20.2800 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 22720 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0xBF # 10111111   Q7
sgs 56000 0x40 # 01000000   Q6
sgs 44480 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 122240 0x80 # 10000000   Q7
sgs 44480 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 22720 0xBF # 10111111   Q7
sgs 82880 0x40 # 01000000   Q6
sgs 44480 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 88960 0x80 # 10000000   Q7
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (22 entries, util 20.2800 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0xBF # 10111111   Q7
sgs 95360 0x80 # 10000000   Q7
sgs 16640 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 120960 0x80 # 10000000   Q7
sgs 16640 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0xBF # 10111111   Q7
sgs 95360 0x80 # 10000000   Q7
sgs 16640 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 58560 0x80 # 10000000   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p5  (22 entries, util 26.5200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 37760 0xBF # 10111111   Q7
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0x7F # 01111111   Q6
sgs 37120 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 96640 0x40 # 01000000   Q6
sgs 3520 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 96640 0x40 # 01000000   Q6
sgs 3520 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 46720 0x40 # 01000000   Q6
sgs 3520 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p4  (19 entries, util 20.2800 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 26880 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0x7F # 01111111   Q6
sgs 56000 0x40 # 01000000   Q6
sgs 27840 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 122240 0x80 # 10000000   Q7
sgs 27840 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 26880 0xBF # 10111111   Q7
sgs 82880 0x40 # 01000000   Q6
sgs 27840 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 72320 0x80 # 10000000   Q7
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (14 entries, util 14.0400 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 20800 0xBF # 10111111   Q7
sgs 206400 0x80 # 10000000   Q7
sgs 23040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 20800 0xBF # 10111111   Q7
sgs 135680 0x80 # 10000000   Q7
sgs 43520 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (22 entries, util 26.5200 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 45760 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 41920 0x7F # 01111111   Q6
sgs 20480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 16960 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 96640 0x40 # 01000000   Q6
sgs 20160 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 96640 0x40 # 01000000   Q6
sgs 20160 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 63360 0x40 # 01000000   Q6
sgs 3520 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p5  (19 entries, util 20.2800 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0x3F # 00111111   BE
sgs 95360 0x80 # 10000000   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 120960 0x80 # 10000000   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0x3F # 00111111   BE
sgs 95360 0x80 # 10000000   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 41920 0x80 # 10000000   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p2  (29 entries, util 21.8400 %)

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
sgs 14400 0x80 # 10000000   Q7
sgs 105280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 16640 0x3F # 00111111   BE
sgs 14400 0x80 # 10000000   Q7
sgs 156480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 16640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 14400 0x80 # 10000000   Q7
sgs 130880 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 16640 0x3F # 00111111   BE
sgs 14400 0x80 # 10000000   Q7
sgs 89920 0x3F # 00111111   BE
```

### sw08-p4  (14 entries, util 14.0400 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 4160 0x3F # 00111111   BE
sgs 206400 0x80 # 10000000   Q7
sgs 39680 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 4160 0x3F # 00111111   BE
sgs 152320 0x80 # 10000000   Q7
sgs 43520 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (23 entries, util 26.5200 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 8640 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 3840 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 33600 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 96640 0x40 # 01000000   Q6
sgs 36800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 96640 0x40 # 01000000   Q6
sgs 36800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 80000 0x40 # 01000000   Q6
sgs 3520 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

