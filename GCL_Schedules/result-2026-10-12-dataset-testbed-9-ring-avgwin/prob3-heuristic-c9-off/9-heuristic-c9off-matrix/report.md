# Reconfiguration-free admission (Problem 3)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Frozen schedule W loaded from: **result/result-2026-10-12-dataset-testbed-9-ring-avgwin/heuristic-c9-off/9-matrix-c9off**

## Admission: W (before) vs. after this run's arrivals

| | admitted | of total |
|---|---|---|
| W (base, unchanged) | 11 | 11 |
| + this run's arrivals | 24 | 39 |

Every arrival admitted here required **zero** window-boundary changes -- see the GCL-entry table below (unchanged from W by construction) and the window-boundary integrity check. No previously-admitted flow was rerouted.

## Arrivals

| id | src->dst | RS(s) size | admitted | route | queue | phi_s (ns) | e2e (ns) | rerouted to make room | reason if rejected |
|---|---|---|---|---|---|---|---|---|---|
| 3 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 15 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 13 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 62400 | 200000 | - | - |
| 18 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q6 | 0 | 45760 | - | - |
| 19 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 | 100160 | 162240 | - | - |
| 17 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 2 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q6 | 24960 | 687680 | - | - |
| 5 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q7 | 277120 | 102080 | - | - |
| 11 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 12480 | 133440 | - | - |
| 27 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q6 | 134720 | 94400 | - | - |
| 30 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q6 | 334720 | 94400 | - | - |
| 31 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q6 | 424960 | 204160 | - | - |
| 33 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q7 | 225280 | 45760 | - | - |
| 39 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q7 | 37440 | 145600 | - | - |
| 44 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q7 | 238080 | 45760 | - | - |
| 26 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 112320 | 300160 | - | - |
| 29 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 125120 | 304000 | - | - |
| 32 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q7 | 250880 | 45760 | - | - |
| 40 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q6 | 534720 | 194560 | - | - |
| 41 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q6 | 100160 | 112320 | - | - |
| 43 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 412480 | 216640 | - | - |
| 49 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q7 | 263680 | 45760 | - | - |
| 22 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 150080 | 128960 | - | - |
| 23 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 42 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 25 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 | 112960 | 178880 | - | - |
| 34 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 37 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 | 150080 | 212480 | - | - |
| 38 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 87360 | 191680 | - | - |
| 46 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 212800 | 95680 | - | - |
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
| sw01-p2 | 29 | 29 | 255 |
| sw01-p4 | 11 | 11 | 255 |
| sw01-p5 | 22 | 22 | 255 |
| sw02-p2 | 25 | 25 | 255 |
| sw02-p4 | 9 | 9 | 255 |
| sw02-p5 | 21 | 21 | 255 |
| sw03-p4 | 23 | 23 | 255 |
| sw03-p5 | 11 | 11 | 255 |
| sw04-p4 | 16 | 16 | 255 |
| sw04-p5 | 10 | 10 | 255 |
| sw05-p4 | 11 | 11 | 255 |
| sw05-p5 | 20 | 20 | 255 |
| sw06-p4 | 10 | 10 | 255 |
| sw06-p5 | 18 | 18 | 255 |
| sw07-p4 | 21 | 21 | 255 |
| sw07-p5 | 12 | 12 | 255 |
| sw08-p2 | 11 | 11 | 255 |
| sw08-p4 | 16 | 16 | 255 |
| sw08-p5 | 22 | 22 | 255 |

## Per-hop windows used by newly admitted flows

| flow | egress port | queue | psi (ns, unchanged) | delta (ns, unchanged) |
|---|---|---|---|---|
| s24(id=13 S2->S3) | S2-p0 | Q7 | 62400 | 12480 |
| s24(id=13 S2->S3) | sw08-p5 | Q7 | 79040 | 12480 |
| s24(id=13 S2->S3) | sw07-p4 | Q7 | 150080 | 12480 |
| s24(id=13 S2->S3) | sw05-p5 | Q7 | 166720 | 12480 |
| s24(id=13 S2->S3) | sw03-p4 | Q7 | 183360 | 12480 |
| s24(id=13 S2->S3) | sw01-p2 | Q7 | 249920 | 12480 |
| s27(id=18 S3->S1) | S3-p0 | Q6 | 0 | 12480 |
| s27(id=18 S3->S1) | sw01-p5 | Q6 | 16640 | 12480 |
| s27(id=18 S3->S1) | sw02-p2 | Q6 | 33280 | 12480 |
| s28(id=19 S3->S2) | S3-p0 | Q7 | 100160 | 12480 |
| s28(id=19 S3->S2) | sw01-p4 | Q7 | 116800 | 12480 |
| s28(id=19 S3->S2) | sw03-p5 | Q7 | 133440 | 12480 |
| s28(id=19 S3->S2) | sw05-p4 | Q7 | 150080 | 12480 |
| s28(id=19 S3->S2) | sw07-p5 | Q7 | 166720 | 12480 |
| s28(id=19 S3->S2) | sw08-p2 | Q7 | 183360 | 12480 |
| s20(id=2 S3->S2) | S3-p0 | Q6 | 24960 | 12480 |
| s20(id=2 S3->S2) | sw01-p4 | Q6 | 537600 | 12480 |
| s20(id=2 S3->S2) | sw03-p5 | Q6 | 600000 | 12480 |
| s20(id=2 S3->S2) | sw05-p4 | Q6 | 616640 | 12480 |
| s20(id=2 S3->S2) | sw07-p5 | Q6 | 633280 | 12480 |
| s20(id=2 S3->S2) | sw08-p2 | Q6 | 700160 | 12480 |
| s22(id=5 S1->S3) | S1-p0 | Q7 | 277120 | 12480 |
| s22(id=5 S1->S3) | sw02-p5 | Q7 | 350080 | 12480 |
| s22(id=5 S1->S3) | sw01-p2 | Q7 | 366720 | 12480 |
| s23(id=11 S2->S1) | S2-p0 | Q6 | 12480 | 12480 |
| s23(id=11 S2->S1) | sw08-p4 | Q6 | 29120 | 12480 |
| s23(id=11 S2->S1) | sw06-p5 | Q6 | 100160 | 12480 |
| s23(id=11 S2->S1) | sw04-p4 | Q6 | 116800 | 12480 |
| s23(id=11 S2->S1) | sw02-p2 | Q6 | 133440 | 12480 |
| s35(id=27 S3->S1) | S3-p0 | Q6 | 134720 | 12480 |
| s35(id=27 S3->S1) | sw01-p5 | Q6 | 200000 | 12480 |
| s35(id=27 S3->S1) | sw02-p2 | Q6 | 216640 | 12480 |
| s38(id=30 S3->S1) | S3-p0 | Q6 | 334720 | 12480 |
| s38(id=30 S3->S1) | sw01-p5 | Q6 | 400000 | 12480 |
| s38(id=30 S3->S1) | sw02-p2 | Q6 | 416640 | 12480 |
| s39(id=31 S3->S1) | S3-p0 | Q6 | 424960 | 12480 |
| s39(id=31 S3->S1) | sw01-p5 | Q6 | 600000 | 12480 |
| s39(id=31 S3->S1) | sw02-p2 | Q6 | 616640 | 12480 |
| s41(id=33 S3->S1) | S3-p0 | Q7 | 225280 | 12480 |
| s41(id=33 S3->S1) | sw01-p5 | Q7 | 241920 | 12480 |
| s41(id=33 S3->S1) | sw02-p2 | Q7 | 258560 | 12480 |
| s47(id=39 S1->S3) | S1-p0 | Q7 | 37440 | 12480 |
| s47(id=39 S1->S3) | sw02-p5 | Q7 | 150080 | 12480 |
| s47(id=39 S1->S3) | sw01-p2 | Q7 | 170560 | 12480 |
| s52(id=44 S3->S1) | S3-p0 | Q7 | 238080 | 12480 |
| s52(id=44 S3->S1) | sw01-p5 | Q7 | 254720 | 12480 |
| s52(id=44 S3->S1) | sw02-p2 | Q7 | 271360 | 12480 |
| s34(id=26 S2->S3) | S2-p0 | Q6 | 112320 | 12480 |
| s34(id=26 S2->S3) | sw08-p5 | Q6 | 128960 | 12480 |
| s34(id=26 S2->S3) | sw07-p4 | Q6 | 200000 | 12480 |
| s34(id=26 S2->S3) | sw05-p5 | Q6 | 216640 | 12480 |
| s34(id=26 S2->S3) | sw03-p4 | Q6 | 233280 | 12480 |
| s34(id=26 S2->S3) | sw01-p2 | Q6 | 400000 | 12480 |
| s37(id=29 S2->S3) | S2-p0 | Q6 | 125120 | 12480 |
| s37(id=29 S2->S3) | sw08-p5 | Q6 | 200000 | 12480 |
| s37(id=29 S2->S3) | sw07-p4 | Q6 | 216640 | 12480 |
| s37(id=29 S2->S3) | sw05-p5 | Q6 | 233280 | 12480 |
| s37(id=29 S2->S3) | sw03-p4 | Q6 | 400000 | 12480 |
| s37(id=29 S2->S3) | sw01-p2 | Q6 | 416640 | 12480 |
| s40(id=32 S3->S1) | S3-p0 | Q7 | 250880 | 12480 |
| s40(id=32 S3->S1) | sw01-p5 | Q7 | 267520 | 12480 |
| s40(id=32 S3->S1) | sw02-p2 | Q7 | 284160 | 12480 |
| s48(id=40 S3->S2) | S3-p0 | Q6 | 534720 | 12480 |
| s48(id=40 S3->S2) | sw01-p4 | Q6 | 600000 | 12480 |
| s48(id=40 S3->S2) | sw03-p5 | Q6 | 616640 | 12480 |
| s48(id=40 S3->S2) | sw05-p4 | Q6 | 633280 | 12480 |
| s48(id=40 S3->S2) | sw07-p5 | Q6 | 700160 | 12480 |
| s48(id=40 S3->S2) | sw08-p2 | Q6 | 716800 | 12480 |
| s49(id=41 S1->S3) | S1-p0 | Q6 | 100160 | 12480 |
| s49(id=41 S1->S3) | sw02-p5 | Q6 | 116800 | 12480 |
| s49(id=41 S1->S3) | sw01-p2 | Q6 | 133440 | 12480 |
| s51(id=43 S2->S3) | S2-p0 | Q6 | 412480 | 12480 |
| s51(id=43 S2->S3) | sw08-p5 | Q6 | 500160 | 12480 |
| s51(id=43 S2->S3) | sw07-p4 | Q6 | 516800 | 12480 |
| s51(id=43 S2->S3) | sw05-p5 | Q6 | 533440 | 12480 |
| s51(id=43 S2->S3) | sw03-p4 | Q6 | 600000 | 12480 |
| s51(id=43 S2->S3) | sw01-p2 | Q6 | 616640 | 12480 |
| s57(id=49 S3->S1) | S3-p0 | Q7 | 263680 | 12480 |
| s57(id=49 S3->S1) | sw01-p5 | Q7 | 280320 | 12480 |
| s57(id=49 S3->S1) | sw02-p2 | Q7 | 296960 | 12480 |
| s30(id=22 S1->S2) | S1-p0 | Q7 | 150080 | 12480 |
| s30(id=22 S1->S2) | sw02-p4 | Q7 | 166720 | 12480 |
| s30(id=22 S1->S2) | sw04-p5 | Q7 | 183360 | 12480 |
| s30(id=22 S1->S2) | sw06-p4 | Q7 | 200000 | 12480 |
| s30(id=22 S1->S2) | sw08-p2 | Q7 | 216640 | 12480 |
| s33(id=25 S3->S2) | S3-p0 | Q7 | 112960 | 12480 |
| s33(id=25 S3->S2) | sw01-p4 | Q7 | 129600 | 12480 |
| s33(id=25 S3->S2) | sw03-p5 | Q7 | 146240 | 12480 |
| s33(id=25 S3->S2) | sw05-p4 | Q7 | 162880 | 12480 |
| s33(id=25 S3->S2) | sw07-p5 | Q7 | 179520 | 12480 |
| s33(id=25 S3->S2) | sw08-p2 | Q7 | 196160 | 12480 |
| s45(id=37 S3->S2) | S3-p0 | Q7 | 150080 | 12480 |
| s45(id=37 S3->S2) | sw01-p4 | Q7 | 166720 | 12480 |
| s45(id=37 S3->S2) | sw03-p5 | Q7 | 183360 | 12480 |
| s45(id=37 S3->S2) | sw05-p4 | Q7 | 200000 | 12480 |
| s45(id=37 S3->S2) | sw07-p5 | Q7 | 216640 | 12480 |
| s45(id=37 S3->S2) | sw08-p2 | Q7 | 233280 | 12480 |
| s46(id=38 S2->S3) | S2-p0 | Q7 | 87360 | 12480 |
| s46(id=38 S2->S3) | sw08-p5 | Q7 | 150080 | 12480 |
| s46(id=38 S2->S3) | sw07-p4 | Q7 | 166720 | 12480 |
| s46(id=38 S2->S3) | sw05-p5 | Q7 | 183360 | 12480 |
| s46(id=38 S2->S3) | sw03-p4 | Q7 | 249920 | 12480 |
| s46(id=38 S2->S3) | sw01-p2 | Q7 | 266560 | 12480 |
| s54(id=46 S2->S3) | S2-p0 | Q7 | 212800 | 12480 |
| s54(id=46 S2->S3) | sw08-p5 | Q7 | 229440 | 12480 |
| s54(id=46 S2->S3) | sw07-p4 | Q7 | 246080 | 12480 |
| s54(id=46 S2->S3) | sw05-p5 | Q7 | 262720 | 12480 |
| s54(id=46 S2->S3) | sw03-p4 | Q7 | 279360 | 12480 |
| s54(id=46 S2->S3) | sw01-p2 | Q7 | 296000 | 12480 |

## Constraint check

- C1-C7, C9: OK
- window-boundary integrity (no window's psi/delta changed anywhere): OK

## GCL per egress port

### sw01-p2  (29 entries, util 35.8800 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 33280 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 4480 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 8000 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 29440 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 33280 0xBF # 10111111   Q7
sgs 81600 0x80 # 10000000   Q7
sgs 35200 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 33280 0xBF # 10111111   Q7
sgs 81600 0x80 # 10000000   Q7
sgs 35200 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 33280 0xBF # 10111111   Q7
sgs 48320 0x80 # 10000000   Q7
sgs 18560 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p4  (11 entries, util 14.0400 %)

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

### sw01-p5  (22 entries, util 31.2000 %)

```
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 61120 0x40 # 01000000   Q6
sgs 9920 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 111040 0x80 # 10000000   Q7
sgs 9920 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 86080 0x80 # 10000000   Q7
sgs 9920 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 81920 0x80 # 10000000   Q7
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (25 entries, util 40.5600 %)

```
sgs 45760 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 33280 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 16320 0xBF # 10111111   Q7
sgs 29440 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 45760 0x7F # 01111111   Q6
sgs 150080 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 45760 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 33280 0x80 # 10000000   Q7
sgs 13120 0x7F # 01111111   Q6
sgs 78720 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 45760 0x7F # 01111111   Q6
sgs 104320 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p4  (9 entries, util 4.6800 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 29120 0x7F # 01111111   Q6
sgs 496000 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p5  (21 entries, util 14.0400 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 75200 0x40 # 01000000   Q6
sgs 8320 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 75200 0x40 # 01000000   Q6
sgs 8320 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 75200 0x40 # 01000000   Q6
sgs 8320 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 58560 0x40 # 01000000   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (23 entries, util 21.8400 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 21120 0xBF # 10111111   Q7
sgs 41280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 46080 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 77120 0x80 # 10000000   Q7
sgs 6400 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 77120 0x80 # 10000000   Q7
sgs 6400 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 21120 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p5  (11 entries, util 14.0400 %)

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

### sw04-p4  (16 entries, util 9.3600 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 202240 0x40 # 01000000   Q6
sgs 48000 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 177280 0x80 # 10000000   Q7
sgs 23040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (10 entries, util 4.6800 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 8320 0x3F # 00111111   BE
sgs 479360 0x80 # 10000000   Q7
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
sgs 37120 0x7F # 01111111   Q6
sgs 400320 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p5  (20 entries, util 21.8400 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 37760 0xBF # 10111111   Q7
sgs 24640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 77120 0x80 # 10000000   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 77120 0x80 # 10000000   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 27200 0x80 # 10000000   Q7
sgs 23040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p4  (10 entries, util 4.6800 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 462720 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (18 entries, util 9.3600 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 4480 0x3F # 00111111   BE
sgs 32960 0x7F # 01111111   Q6
sgs 202240 0x40 # 01000000   Q6
sgs 14720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 193920 0x80 # 10000000   Q7
sgs 23040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (21 entries, util 21.8400 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 50240 0xBF # 10111111   Q7
sgs 8000 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 29440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 77120 0x80 # 10000000   Q7
sgs 39680 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 77120 0x80 # 10000000   Q7
sgs 39680 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 43840 0x80 # 10000000   Q7
sgs 23040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p5  (12 entries, util 14.0400 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 3840 0x3F # 00111111   BE
sgs 383680 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p2  (11 entries, util 18.7200 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 46080 0x7F # 01111111   Q6
sgs 20480 0xBF # 10111111   Q7
sgs 435840 0x80 # 10000000   Q7
sgs 43520 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p4  (16 entries, util 9.3600 %)

```
sgs 41600 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 21120 0xBF # 10111111   Q7
sgs 16320 0x7F # 01111111   Q6
sgs 202240 0x40 # 01000000   Q6
sgs 31360 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 210560 0x80 # 10000000   Q7
sgs 23040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (22 entries, util 21.8400 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 46080 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 77120 0x80 # 10000000   Q7
sgs 6400 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 77120 0x80 # 10000000   Q7
sgs 6400 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 60480 0x80 # 10000000   Q7
sgs 23040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

