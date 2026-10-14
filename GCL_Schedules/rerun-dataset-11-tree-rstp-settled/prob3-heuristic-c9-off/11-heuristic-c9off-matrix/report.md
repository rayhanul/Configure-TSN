# Reconfiguration-free admission (Problem 3)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Frozen schedule W loaded from: **result/result-2026-10-13-dataset-testbed-11-tree-avgwin/heuristic-c9-off/11-matrix-c9off**

## Admission: W (before) vs. after this run's arrivals

| | admitted | of total |
|---|---|---|
| W (base, unchanged) | 10 | 10 |
| + this run's arrivals | 19 | 40 |

Every arrival admitted here required **zero** window-boundary changes -- see the GCL-entry table below (unchanged from W by construction) and the window-boundary integrity check. No previously-admitted flow was rerouted.

## Arrivals

| id | src->dst | RS(s) size | admitted | route | queue | phi_s (ns) | e2e (ns) | rerouted to make room | reason if rejected |
|---|---|---|---|---|---|---|---|---|---|
| 6 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 11 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 14 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 16 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q7 | 87680 | 274880 | - | - |
| 4 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 75200 | 104000 | - | - |
| 12 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 150080 | 145600 | - | - |
| 17 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 62720 | 120640 | - | - |
| 13 | S1->S3 | - | yes | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 37440 | 675200 | - | - |
| 19 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q7 | 100480 | 257600 | - | - |
| 15 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 12480 | 633280 | - | - |
| 23 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 24960 | 187520 | - | - |
| 25 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 100160 | 128960 | - | - |
| 27 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 75520 | 125760 | - | - |
| 28 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 112960 | 299520 | - | - |
| 36 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 300160 | 145600 | - | - |
| 49 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 93440 | 120640 | - | - |
| 50 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 333760 | 182720 | - | - |
| 48 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 37 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q7 | 462720 | 199680 | - | - |
| 46 | S1->S3 | - | yes | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 150080 | 317760 | - | - |
| 33 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 34 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 35 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 212800 | 79040 | - | - |
| 41 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 44 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 22 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 40 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 162880 | 199680 | - | - |
| 42 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 175680 | 203520 | - | - |
| 43 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 39 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 21 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 24 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 31 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 32 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 29 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 38 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 26 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 30 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 45 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 47 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |

## Per-port GCL entries (should equal W exactly)

| port | W entries | after arrivals | GCL_size |
|---|---|---|---|
| sw01-p2 | 11 | 11 | 255 |
| sw01-p4 | 27 | 27 | 255 |
| sw02-p2 | 27 | 27 | 255 |
| sw02-p4 | 24 | 24 | 255 |
| sw03-p4 | 11 | 11 | 255 |
| sw03-p5 | 27 | 27 | 255 |
| sw04-p4 | 24 | 24 | 255 |
| sw04-p5 | 21 | 21 | 255 |
| sw05-p4 | 27 | 27 | 255 |
| sw05-p5 | 11 | 11 | 255 |
| sw06-p4 | 23 | 23 | 255 |
| sw06-p5 | 23 | 23 | 255 |
| sw07-p4 | 10 | 10 | 255 |
| sw07-p5 | 28 | 28 | 255 |
| sw08-p2 | 27 | 27 | 255 |
| sw08-p4 | 26 | 26 | 255 |
| sw08-p5 | 10 | 10 | 255 |

## Per-hop windows used by newly admitted flows

| flow | egress port | queue | psi (ns, unchanged) | delta (ns, unchanged) |
|---|---|---|---|---|
| s27(id=16 S3->S1) | S3-p0 | Q7 | 87680 | 12480 |
| s27(id=16 S3->S1) | sw01-p4 | Q7 | 104320 | 12480 |
| s27(id=16 S3->S1) | sw03-p5 | Q7 | 120960 | 12480 |
| s27(id=16 S3->S1) | sw05-p4 | Q7 | 137600 | 12480 |
| s27(id=16 S3->S1) | sw07-p5 | Q7 | 249920 | 12480 |
| s27(id=16 S3->S1) | sw08-p4 | Q7 | 266560 | 12480 |
| s27(id=16 S3->S1) | sw06-p5 | Q7 | 283200 | 12480 |
| s27(id=16 S3->S1) | sw04-p4 | Q7 | 299840 | 12480 |
| s27(id=16 S3->S1) | sw02-p2 | Q7 | 316480 | 12480 |
| s20(id=4 S2->S3) | S2-p0 | Q7 | 75200 | 12480 |
| s20(id=4 S2->S3) | sw08-p5 | Q7 | 91840 | 12480 |
| s20(id=4 S2->S3) | sw07-p4 | Q7 | 108480 | 12480 |
| s20(id=4 S2->S3) | sw05-p5 | Q7 | 125120 | 12480 |
| s20(id=4 S2->S3) | sw03-p4 | Q7 | 141760 | 12480 |
| s20(id=4 S2->S3) | sw01-p2 | Q7 | 158400 | 12480 |
| s23(id=12 S2->S3) | S2-p0 | Q7 | 150080 | 12480 |
| s23(id=12 S2->S3) | sw08-p5 | Q7 | 166720 | 12480 |
| s23(id=12 S2->S3) | sw07-p4 | Q7 | 183360 | 12480 |
| s23(id=12 S2->S3) | sw05-p5 | Q7 | 200000 | 12480 |
| s23(id=12 S2->S3) | sw03-p4 | Q7 | 216640 | 12480 |
| s23(id=12 S2->S3) | sw01-p2 | Q7 | 233280 | 12480 |
| s28(id=17 S1->S2) | S1-p0 | Q7 | 62720 | 12480 |
| s28(id=17 S1->S2) | sw02-p4 | Q7 | 79360 | 12480 |
| s28(id=17 S1->S2) | sw04-p5 | Q7 | 101120 | 12480 |
| s28(id=17 S1->S2) | sw06-p4 | Q7 | 154240 | 12480 |
| s28(id=17 S1->S2) | sw08-p2 | Q7 | 170880 | 12480 |
| s24(id=13 S1->S3) | S1-p0 | Q6 | 37440 | 12480 |
| s24(id=13 S1->S3) | sw02-p4 | Q6 | 200000 | 12480 |
| s24(id=13 S1->S3) | sw04-p5 | Q6 | 216640 | 12480 |
| s24(id=13 S1->S3) | sw06-p4 | Q6 | 233280 | 12480 |
| s24(id=13 S1->S3) | sw08-p5 | Q6 | 537600 | 12480 |
| s24(id=13 S1->S3) | sw07-p4 | Q6 | 600000 | 12480 |
| s24(id=13 S1->S3) | sw05-p5 | Q6 | 616640 | 12480 |
| s24(id=13 S1->S3) | sw03-p4 | Q6 | 633280 | 12480 |
| s24(id=13 S1->S3) | sw01-p2 | Q6 | 700160 | 12480 |
| s29(id=19 S3->S1) | S3-p0 | Q7 | 100480 | 12480 |
| s29(id=19 S3->S1) | sw01-p4 | Q7 | 117120 | 12480 |
| s29(id=19 S3->S1) | sw03-p5 | Q7 | 133760 | 12480 |
| s29(id=19 S3->S1) | sw05-p4 | Q7 | 262400 | 12480 |
| s29(id=19 S3->S1) | sw07-p5 | Q7 | 279040 | 12480 |
| s29(id=19 S3->S1) | sw08-p4 | Q7 | 295680 | 12480 |
| s29(id=19 S3->S1) | sw06-p5 | Q7 | 312320 | 12480 |
| s29(id=19 S3->S1) | sw04-p4 | Q7 | 328960 | 12480 |
| s29(id=19 S3->S1) | sw02-p2 | Q7 | 345600 | 12480 |
| s26(id=15 S2->S3) | S2-p0 | Q6 | 12480 | 12480 |
| s26(id=15 S2->S3) | sw08-p5 | Q6 | 29120 | 12480 |
| s26(id=15 S2->S3) | sw07-p4 | Q6 | 537600 | 12480 |
| s26(id=15 S2->S3) | sw05-p5 | Q6 | 600000 | 12480 |
| s26(id=15 S2->S3) | sw03-p4 | Q6 | 616640 | 12480 |
| s26(id=15 S2->S3) | sw01-p2 | Q6 | 633280 | 12480 |
| s32(id=23 S2->S1) | S2-p0 | Q6 | 24960 | 12480 |
| s32(id=23 S2->S1) | sw08-p4 | Q6 | 100160 | 12480 |
| s32(id=23 S2->S1) | sw06-p5 | Q6 | 116800 | 12480 |
| s32(id=23 S2->S1) | sw04-p4 | Q6 | 133440 | 12480 |
| s32(id=23 S2->S1) | sw02-p2 | Q6 | 200000 | 12480 |
| s34(id=25 S2->S1) | S2-p0 | Q6 | 100160 | 12480 |
| s34(id=25 S2->S1) | sw08-p4 | Q6 | 116800 | 12480 |
| s34(id=25 S2->S1) | sw06-p5 | Q6 | 133440 | 12480 |
| s34(id=25 S2->S1) | sw04-p4 | Q6 | 200000 | 12480 |
| s34(id=25 S2->S1) | sw02-p2 | Q6 | 216640 | 12480 |
| s36(id=27 S1->S2) | S1-p0 | Q7 | 75520 | 12480 |
| s36(id=27 S1->S2) | sw02-p4 | Q7 | 97280 | 12480 |
| s36(id=27 S1->S2) | sw04-p5 | Q7 | 155520 | 12480 |
| s36(id=27 S1->S2) | sw06-p4 | Q7 | 172160 | 12480 |
| s36(id=27 S1->S2) | sw08-p2 | Q7 | 188800 | 12480 |
| s37(id=28 S2->S1) | S2-p0 | Q6 | 112960 | 12480 |
| s37(id=28 S2->S1) | sw08-p4 | Q6 | 200000 | 12480 |
| s37(id=28 S2->S1) | sw06-p5 | Q6 | 216640 | 12480 |
| s37(id=28 S2->S1) | sw04-p4 | Q6 | 233280 | 12480 |
| s37(id=28 S2->S1) | sw02-p2 | Q6 | 400000 | 12480 |
| s45(id=36 S2->S1) | S2-p0 | Q6 | 300160 | 12480 |
| s45(id=36 S2->S1) | sw08-p4 | Q6 | 337600 | 12480 |
| s45(id=36 S2->S1) | sw06-p5 | Q6 | 400000 | 12480 |
| s45(id=36 S2->S1) | sw04-p4 | Q6 | 416640 | 12480 |
| s45(id=36 S2->S1) | sw02-p2 | Q6 | 433280 | 12480 |
| s58(id=49 S1->S2) | S1-p0 | Q7 | 93440 | 12480 |
| s58(id=49 S1->S2) | sw02-p4 | Q7 | 151680 | 12480 |
| s58(id=49 S1->S2) | sw04-p5 | Q7 | 168320 | 12480 |
| s58(id=49 S1->S2) | sw06-p4 | Q7 | 184960 | 12480 |
| s58(id=49 S1->S2) | sw08-p2 | Q7 | 201600 | 12480 |
| s59(id=50 S2->S1) | S2-p0 | Q6 | 333760 | 12480 |
| s59(id=50 S2->S1) | sw08-p4 | Q6 | 400000 | 12480 |
| s59(id=50 S2->S1) | sw06-p5 | Q6 | 416640 | 12480 |
| s59(id=50 S2->S1) | sw04-p4 | Q6 | 433280 | 12480 |
| s59(id=50 S2->S1) | sw02-p2 | Q6 | 504000 | 12480 |
| s46(id=37 S3->S1) | S3-p0 | Q7 | 462720 | 12480 |
| s46(id=37 S3->S1) | sw01-p4 | Q7 | 479360 | 12480 |
| s46(id=37 S3->S1) | sw03-p5 | Q7 | 496000 | 12480 |
| s46(id=37 S3->S1) | sw05-p4 | Q7 | 512640 | 12480 |
| s46(id=37 S3->S1) | sw07-p5 | Q7 | 529280 | 12480 |
| s46(id=37 S3->S1) | sw08-p4 | Q7 | 550080 | 12480 |
| s46(id=37 S3->S1) | sw06-p5 | Q7 | 566720 | 12480 |
| s46(id=37 S3->S1) | sw04-p4 | Q7 | 583360 | 12480 |
| s46(id=37 S3->S1) | sw02-p2 | Q7 | 649920 | 12480 |
| s55(id=46 S1->S3) | S1-p0 | Q7 | 150080 | 12480 |
| s55(id=46 S1->S3) | sw02-p4 | Q7 | 166720 | 12480 |
| s55(id=46 S1->S3) | sw04-p5 | Q7 | 183360 | 12480 |
| s55(id=46 S1->S3) | sw06-p4 | Q7 | 372160 | 12480 |
| s55(id=46 S1->S3) | sw08-p5 | Q7 | 388800 | 12480 |
| s55(id=46 S1->S3) | sw07-p4 | Q7 | 405440 | 12480 |
| s55(id=46 S1->S3) | sw05-p5 | Q7 | 422080 | 12480 |
| s55(id=46 S1->S3) | sw03-p4 | Q7 | 438720 | 12480 |
| s55(id=46 S1->S3) | sw01-p2 | Q7 | 455360 | 12480 |
| s44(id=35 S2->S1) | S2-p0 | Q7 | 212800 | 12480 |
| s44(id=35 S2->S1) | sw08-p4 | Q7 | 229440 | 12480 |
| s44(id=35 S2->S1) | sw06-p5 | Q7 | 246080 | 12480 |
| s44(id=35 S2->S1) | sw04-p4 | Q7 | 262720 | 12480 |
| s44(id=35 S2->S1) | sw02-p2 | Q7 | 279360 | 12480 |
| s49(id=40 S2->S3) | S2-p0 | Q7 | 162880 | 12480 |
| s49(id=40 S2->S3) | sw08-p5 | Q7 | 179520 | 12480 |
| s49(id=40 S2->S3) | sw07-p4 | Q7 | 196160 | 12480 |
| s49(id=40 S2->S3) | sw05-p5 | Q7 | 212800 | 12480 |
| s49(id=40 S2->S3) | sw03-p4 | Q7 | 229440 | 12480 |
| s49(id=40 S2->S3) | sw01-p2 | Q7 | 246080 | 12480 |
| s51(id=42 S2->S3) | S2-p0 | Q7 | 175680 | 12480 |
| s51(id=42 S2->S3) | sw08-p5 | Q7 | 192320 | 12480 |
| s51(id=42 S2->S3) | sw07-p4 | Q7 | 208960 | 12480 |
| s51(id=42 S2->S3) | sw05-p5 | Q7 | 225600 | 12480 |
| s51(id=42 S2->S3) | sw03-p4 | Q7 | 242240 | 12480 |
| s51(id=42 S2->S3) | sw01-p2 | Q7 | 258880 | 12480 |

## Constraint check

- C1-C7, C9: OK
- window-boundary integrity (no window's psi/delta changed anywhere): OK

## GCL per egress port

### sw01-p2  (11 entries, util 18.7200 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 45440 0x7F # 01111111   Q6
sgs 392000 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p4  (27 entries, util 23.4000 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 70080 0x80 # 10000000   Q7
sgs 38400 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 120000 0x40 # 01000000   Q6
sgs 38400 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 95040 0x80 # 10000000   Q7
sgs 38400 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 103360 0x40 # 01000000   Q6
sgs 5120 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (27 entries, util 28.0800 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 21120 0xBF # 10111111   Q7
sgs 3840 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 33600 0x7F # 01111111   Q6
sgs 32960 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 4480 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 120960 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 37440 0x80 # 10000000   Q7
sgs 46080 0x7F # 01111111   Q6
sgs 32960 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 4480 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 54400 0x80 # 10000000   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p4  (24 entries, util 21.8400 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 72320 0x80 # 10000000   Q7
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 122240 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 72320 0x80 # 10000000   Q7
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 105600 0x40 # 01000000   Q6
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (11 entries, util 18.7200 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 28800 0x7F # 01111111   Q6
sgs 408640 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p5  (27 entries, util 23.4000 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 70080 0x80 # 10000000   Q7
sgs 21760 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 120000 0x40 # 01000000   Q6
sgs 21760 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 95040 0x80 # 10000000   Q7
sgs 21760 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 86720 0x40 # 01000000   Q6
sgs 5120 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p4  (24 entries, util 28.0800 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 16320 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 21120 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 120960 0x80 # 10000000   Q7
sgs 29120 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 37440 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16320 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 21120 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 71040 0x80 # 10000000   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (21 entries, util 21.8400 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 72320 0x80 # 10000000   Q7
sgs 44480 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 122240 0x40 # 01000000   Q6
sgs 44480 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 72320 0x80 # 10000000   Q7
sgs 44480 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 88960 0x40 # 01000000   Q6
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (27 entries, util 23.4000 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 70080 0x80 # 10000000   Q7
sgs 5120 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 120000 0x40 # 01000000   Q6
sgs 5120 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 95040 0x80 # 10000000   Q7
sgs 5120 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 70080 0x40 # 01000000   Q6
sgs 5120 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p5  (11 entries, util 18.7200 %)

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

### sw06-p4  (23 entries, util 21.8400 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 4800 0x3F # 00111111   BE
sgs 67200 0x80 # 10000000   Q7
sgs 27840 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 122240 0x40 # 01000000   Q6
sgs 27840 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 4800 0x3F # 00111111   BE
sgs 67200 0x80 # 10000000   Q7
sgs 27840 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 72320 0x40 # 01000000   Q6
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (23 entries, util 28.0800 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 20800 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 16960 0xBF # 10111111   Q7
sgs 49600 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 37760 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 120960 0x80 # 10000000   Q7
sgs 45760 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 37440 0x80 # 10000000   Q7
sgs 29440 0xBF # 10111111   Q7
sgs 49600 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 37760 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 87680 0x80 # 10000000   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (10 entries, util 18.7200 %)

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

### sw07-p5  (28 entries, util 23.4000 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 70080 0x80 # 10000000   Q7
sgs 38400 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 120000 0x40 # 01000000   Q6
sgs 38400 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 95040 0x80 # 10000000   Q7
sgs 38400 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 53440 0x40 # 01000000   Q6
sgs 5120 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p2  (27 entries, util 32.7600 %)

```
sgs 66560 0x3F # 00111111   BE
sgs 29120 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 24000 0x3F # 00111111   BE
sgs 75840 0x80 # 10000000   Q7
sgs 32640 0x3F # 00111111   BE
sgs 29120 0x40 # 01000000   Q6
sgs 13120 0x3F # 00111111   BE
sgs 13440 0x40 # 01000000   Q6
sgs 144320 0x3F # 00111111   BE
sgs 29120 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 34560 0x80 # 10000000   Q7
sgs 110400 0x3F # 00111111   BE
sgs 29120 0x40 # 01000000   Q6
sgs 13120 0x3F # 00111111   BE
sgs 13440 0x40 # 01000000   Q6
sgs 77760 0x3F # 00111111   BE
```

### sw08-p4  (26 entries, util 28.0800 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 33600 0xBF # 10111111   Q7
sgs 32960 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 4480 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 120960 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 37440 0x80 # 10000000   Q7
sgs 46080 0xBF # 10111111   Q7
sgs 32960 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 4480 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 104320 0x80 # 10000000   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (10 entries, util 18.7200 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 458560 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

