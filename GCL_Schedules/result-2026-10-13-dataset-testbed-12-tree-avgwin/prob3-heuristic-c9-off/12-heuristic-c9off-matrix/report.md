# Reconfiguration-free admission (Problem 3)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Frozen schedule W loaded from: **result/result-2026-10-13-dataset-testbed-12-tree-avgwin/heuristic-c9-off/12-matrix-c9off**

## Admission: W (before) vs. after this run's arrivals

| | admitted | of total |
|---|---|---|
| W (base, unchanged) | 11 | 11 |
| + this run's arrivals | 23 | 39 |

Every arrival admitted here required **zero** window-boundary changes -- see the GCL-entry table below (unchanged from W by construction) and the window-boundary integrity check. No previously-admitted flow was rerouted.

## Arrivals

| id | src->dst | RS(s) size | admitted | route | queue | phi_s (ns) | e2e (ns) | rerouted to make room | reason if rejected |
|---|---|---|---|---|---|---|---|---|---|
| 10 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 20 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 3 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q6 | 62720 | 229120 | - | - |
| 15 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 16 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 | 212800 | 95680 | - | - |
| 1 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 237760 | 83520 | - | - |
| 17 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 250880 | 83200 | - | - |
| 6 | S1->S3 | - | yes | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 112640 | 145600 | - | - |
| 13 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 350080 | 95680 | - | - |
| 27 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 150080 | 229120 | - | - |
| 32 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 162880 | 232960 | - | - |
| 38 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q6 | 125440 | 103680 | - | - |
| 45 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 175680 | 286720 | - | - |
| 50 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 12800 | 133120 | - | - |
| 30 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 362880 | 95680 | - | - |
| 42 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 212480 | 316800 | - | - |
| 43 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q6 | 75520 | 353600 | - | - |
| 31 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q6 | 88320 | 403520 | - | - |
| 40 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q7 | 225600 | 353600 | - | - |
| 22 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 225600 | 87040 | - | - |
| 24 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 238400 | 90880 | - | - |
| 25 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 263680 | 83200 | - | - |
| 33 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 280640 | 81920 | - | - |
| 34 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 293440 | 85760 | - | - |
| 36 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 306240 | 89600 | - | - |
| 49 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 251200 | 94720 | - | - |
| 28 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
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
| sw01-p2 | 24 | 24 | 255 |
| sw01-p4 | 22 | 22 | 255 |
| sw02-p2 | 24 | 24 | 255 |
| sw02-p4 | 26 | 26 | 255 |
| sw03-p4 | 20 | 20 | 255 |
| sw03-p5 | 22 | 22 | 255 |
| sw04-p4 | 22 | 22 | 255 |
| sw04-p5 | 26 | 26 | 255 |
| sw05-p4 | 19 | 19 | 255 |
| sw05-p5 | 25 | 25 | 255 |
| sw06-p4 | 23 | 23 | 255 |
| sw06-p5 | 22 | 22 | 255 |
| sw07-p4 | 24 | 24 | 255 |
| sw07-p5 | 23 | 23 | 255 |
| sw08-p2 | 21 | 21 | 255 |
| sw08-p4 | 23 | 23 | 255 |
| sw08-p5 | 20 | 20 | 255 |

## Per-hop windows used by newly admitted flows

| flow | egress port | queue | psi (ns, unchanged) | delta (ns, unchanged) |
|---|---|---|---|---|
| s21(id=3 S3->S1) | S3-p0 | Q6 | 62720 | 12480 |
| s21(id=3 S3->S1) | sw01-p4 | Q6 | 79360 | 12480 |
| s21(id=3 S3->S1) | sw03-p5 | Q6 | 96000 | 12480 |
| s21(id=3 S3->S1) | sw05-p4 | Q6 | 112640 | 12480 |
| s21(id=3 S3->S1) | sw07-p5 | Q6 | 212800 | 12480 |
| s21(id=3 S3->S1) | sw08-p4 | Q6 | 229440 | 12480 |
| s21(id=3 S3->S1) | sw06-p5 | Q6 | 246080 | 12480 |
| s21(id=3 S3->S1) | sw04-p4 | Q6 | 262720 | 12480 |
| s21(id=3 S3->S1) | sw02-p2 | Q6 | 279360 | 12480 |
| s26(id=16 S3->S2) | S3-p0 | Q7 | 212800 | 12480 |
| s26(id=16 S3->S2) | sw01-p4 | Q7 | 229440 | 12480 |
| s26(id=16 S3->S2) | sw03-p5 | Q7 | 246080 | 12480 |
| s26(id=16 S3->S2) | sw05-p4 | Q7 | 262720 | 12480 |
| s26(id=16 S3->S2) | sw07-p5 | Q7 | 279360 | 12480 |
| s26(id=16 S3->S2) | sw08-p2 | Q7 | 296000 | 12480 |
| s20(id=1 S1->S2) | S1-p0 | Q7 | 237760 | 12480 |
| s20(id=1 S1->S2) | sw02-p4 | Q7 | 254720 | 12480 |
| s20(id=1 S1->S2) | sw04-p5 | Q7 | 271360 | 12480 |
| s20(id=1 S1->S2) | sw06-p4 | Q7 | 292160 | 12480 |
| s20(id=1 S1->S2) | sw08-p2 | Q7 | 308800 | 12480 |
| s27(id=17 S1->S2) | S1-p0 | Q7 | 250880 | 12480 |
| s27(id=17 S1->S2) | sw02-p4 | Q7 | 267520 | 12480 |
| s27(id=17 S1->S2) | sw04-p5 | Q7 | 288320 | 12480 |
| s27(id=17 S1->S2) | sw06-p4 | Q7 | 304960 | 12480 |
| s27(id=17 S1->S2) | sw08-p2 | Q7 | 321600 | 12480 |
| s22(id=6 S1->S3) | S1-p0 | Q6 | 112640 | 12480 |
| s22(id=6 S1->S3) | sw02-p4 | Q6 | 129280 | 12480 |
| s22(id=6 S1->S3) | sw04-p5 | Q6 | 145920 | 12480 |
| s22(id=6 S1->S3) | sw06-p4 | Q6 | 162560 | 12480 |
| s22(id=6 S1->S3) | sw08-p5 | Q6 | 179200 | 12480 |
| s22(id=6 S1->S3) | sw07-p4 | Q6 | 195840 | 12480 |
| s22(id=6 S1->S3) | sw05-p5 | Q6 | 212480 | 12480 |
| s22(id=6 S1->S3) | sw03-p4 | Q6 | 229120 | 12480 |
| s22(id=6 S1->S3) | sw01-p2 | Q6 | 245760 | 12480 |
| s24(id=13 S2->S3) | S2-p0 | Q7 | 350080 | 12480 |
| s24(id=13 S2->S3) | sw08-p5 | Q7 | 366720 | 12480 |
| s24(id=13 S2->S3) | sw07-p4 | Q7 | 383360 | 12480 |
| s24(id=13 S2->S3) | sw05-p5 | Q7 | 400000 | 12480 |
| s24(id=13 S2->S3) | sw03-p4 | Q7 | 416640 | 12480 |
| s24(id=13 S2->S3) | sw01-p2 | Q7 | 433280 | 12480 |
| s35(id=27 S2->S1) | S2-p0 | Q7 | 150080 | 12480 |
| s35(id=27 S2->S1) | sw08-p4 | Q7 | 166720 | 12480 |
| s35(id=27 S2->S1) | sw06-p5 | Q7 | 183360 | 12480 |
| s35(id=27 S2->S1) | sw04-p4 | Q7 | 350080 | 12480 |
| s35(id=27 S2->S1) | sw02-p2 | Q7 | 366720 | 12480 |
| s40(id=32 S2->S1) | S2-p0 | Q7 | 162880 | 12480 |
| s40(id=32 S2->S1) | sw08-p4 | Q7 | 179520 | 12480 |
| s40(id=32 S2->S1) | sw06-p5 | Q7 | 350080 | 12480 |
| s40(id=32 S2->S1) | sw04-p4 | Q7 | 366720 | 12480 |
| s40(id=32 S2->S1) | sw02-p2 | Q7 | 383360 | 12480 |
| s46(id=38 S1->S2) | S1-p0 | Q6 | 125440 | 12480 |
| s46(id=38 S1->S2) | sw02-p4 | Q6 | 142080 | 12480 |
| s46(id=38 S1->S2) | sw04-p5 | Q6 | 158720 | 12480 |
| s46(id=38 S1->S2) | sw06-p4 | Q6 | 175360 | 12480 |
| s46(id=38 S1->S2) | sw08-p2 | Q6 | 216640 | 12480 |
| s53(id=45 S2->S1) | S2-p0 | Q7 | 175680 | 12480 |
| s53(id=45 S2->S1) | sw08-p4 | Q7 | 350080 | 12480 |
| s53(id=45 S2->S1) | sw06-p5 | Q7 | 366720 | 12480 |
| s53(id=45 S2->S1) | sw04-p4 | Q7 | 383360 | 12480 |
| s53(id=45 S2->S1) | sw02-p2 | Q7 | 449920 | 12480 |
| s58(id=50 S2->S1) | S2-p0 | Q6 | 12800 | 12480 |
| s58(id=50 S2->S1) | sw08-p4 | Q6 | 29440 | 12480 |
| s58(id=50 S2->S1) | sw06-p5 | Q6 | 100160 | 12480 |
| s58(id=50 S2->S1) | sw04-p4 | Q6 | 116800 | 12480 |
| s58(id=50 S2->S1) | sw02-p2 | Q6 | 133440 | 12480 |
| s38(id=30 S2->S3) | S2-p0 | Q7 | 362880 | 12480 |
| s38(id=30 S2->S3) | sw08-p5 | Q7 | 379520 | 12480 |
| s38(id=30 S2->S3) | sw07-p4 | Q7 | 396160 | 12480 |
| s38(id=30 S2->S3) | sw05-p5 | Q7 | 412800 | 12480 |
| s38(id=30 S2->S3) | sw03-p4 | Q7 | 429440 | 12480 |
| s38(id=30 S2->S3) | sw01-p2 | Q7 | 446080 | 12480 |
| s50(id=42 S2->S3) | S2-p0 | Q6 | 212480 | 12480 |
| s50(id=42 S2->S3) | sw08-p5 | Q6 | 229120 | 12480 |
| s50(id=42 S2->S3) | sw07-p4 | Q6 | 419520 | 12480 |
| s50(id=42 S2->S3) | sw05-p5 | Q6 | 436160 | 12480 |
| s50(id=42 S2->S3) | sw03-p4 | Q6 | 500160 | 12480 |
| s50(id=42 S2->S3) | sw01-p2 | Q6 | 516800 | 12480 |
| s51(id=43 S3->S2) | S3-p0 | Q6 | 75520 | 12480 |
| s51(id=43 S3->S2) | sw01-p4 | Q6 | 92160 | 12480 |
| s51(id=43 S3->S2) | sw03-p5 | Q6 | 108800 | 12480 |
| s51(id=43 S3->S2) | sw05-p4 | Q6 | 208960 | 12480 |
| s51(id=43 S3->S2) | sw07-p5 | Q6 | 225600 | 12480 |
| s51(id=43 S3->S2) | sw08-p2 | Q6 | 416640 | 12480 |
| s39(id=31 S3->S1) | S3-p0 | Q6 | 88320 | 12480 |
| s39(id=31 S3->S1) | sw01-p4 | Q6 | 104960 | 12480 |
| s39(id=31 S3->S1) | sw03-p5 | Q6 | 205120 | 12480 |
| s39(id=31 S3->S1) | sw05-p4 | Q6 | 221760 | 12480 |
| s39(id=31 S3->S1) | sw07-p5 | Q6 | 412800 | 12480 |
| s39(id=31 S3->S1) | sw08-p4 | Q6 | 429440 | 12480 |
| s39(id=31 S3->S1) | sw06-p5 | Q6 | 446080 | 12480 |
| s39(id=31 S3->S1) | sw04-p4 | Q6 | 462720 | 12480 |
| s39(id=31 S3->S1) | sw02-p2 | Q6 | 479360 | 12480 |
| s48(id=40 S3->S1) | S3-p0 | Q7 | 225600 | 12480 |
| s48(id=40 S3->S1) | sw01-p4 | Q7 | 242240 | 12480 |
| s48(id=40 S3->S1) | sw03-p5 | Q7 | 258880 | 12480 |
| s48(id=40 S3->S1) | sw05-p4 | Q7 | 275520 | 12480 |
| s48(id=40 S3->S1) | sw07-p5 | Q7 | 346240 | 12480 |
| s48(id=40 S3->S1) | sw08-p4 | Q7 | 362880 | 12480 |
| s48(id=40 S3->S1) | sw06-p5 | Q7 | 379520 | 12480 |
| s48(id=40 S3->S1) | sw04-p4 | Q7 | 550080 | 12480 |
| s48(id=40 S3->S1) | sw02-p2 | Q7 | 566720 | 12480 |
| s30(id=22 S2->S1) | S2-p0 | Q6 | 225600 | 12480 |
| s30(id=22 S2->S1) | sw08-p4 | Q6 | 242240 | 12480 |
| s30(id=22 S2->S1) | sw06-p5 | Q6 | 258880 | 12480 |
| s30(id=22 S2->S1) | sw04-p4 | Q6 | 275520 | 12480 |
| s30(id=22 S2->S1) | sw02-p2 | Q6 | 292160 | 12480 |
| s32(id=24 S2->S1) | S2-p0 | Q6 | 238400 | 12480 |
| s32(id=24 S2->S1) | sw08-p4 | Q6 | 255040 | 12480 |
| s32(id=24 S2->S1) | sw06-p5 | Q6 | 271680 | 12480 |
| s32(id=24 S2->S1) | sw04-p4 | Q6 | 288320 | 12480 |
| s32(id=24 S2->S1) | sw02-p2 | Q6 | 304960 | 12480 |
| s33(id=25 S1->S2) | S1-p0 | Q7 | 263680 | 12480 |
| s33(id=25 S1->S2) | sw02-p4 | Q7 | 284480 | 12480 |
| s33(id=25 S1->S2) | sw04-p5 | Q7 | 301120 | 12480 |
| s33(id=25 S1->S2) | sw06-p4 | Q7 | 317760 | 12480 |
| s33(id=25 S1->S2) | sw08-p2 | Q7 | 334400 | 12480 |
| s41(id=33 S1->S2) | S1-p0 | Q7 | 280640 | 12480 |
| s41(id=33 S1->S2) | sw02-p4 | Q7 | 297280 | 12480 |
| s41(id=33 S1->S2) | sw04-p5 | Q7 | 313920 | 12480 |
| s41(id=33 S1->S2) | sw06-p4 | Q7 | 330560 | 12480 |
| s41(id=33 S1->S2) | sw08-p2 | Q7 | 347200 | 12480 |
| s42(id=34 S1->S2) | S1-p0 | Q7 | 293440 | 12480 |
| s42(id=34 S1->S2) | sw02-p4 | Q7 | 310080 | 12480 |
| s42(id=34 S1->S2) | sw04-p5 | Q7 | 326720 | 12480 |
| s42(id=34 S1->S2) | sw06-p4 | Q7 | 343360 | 12480 |
| s42(id=34 S1->S2) | sw08-p2 | Q7 | 360000 | 12480 |
| s44(id=36 S1->S2) | S1-p0 | Q7 | 306240 | 12480 |
| s44(id=36 S1->S2) | sw02-p4 | Q7 | 322880 | 12480 |
| s44(id=36 S1->S2) | sw04-p5 | Q7 | 339520 | 12480 |
| s44(id=36 S1->S2) | sw06-p4 | Q7 | 356160 | 12480 |
| s44(id=36 S1->S2) | sw08-p2 | Q7 | 372800 | 12480 |
| s57(id=49 S2->S1) | S2-p0 | Q6 | 251200 | 12480 |
| s57(id=49 S2->S1) | sw08-p4 | Q6 | 267840 | 12480 |
| s57(id=49 S2->S1) | sw06-p5 | Q6 | 284480 | 12480 |
| s57(id=49 S2->S1) | sw04-p4 | Q6 | 301120 | 12480 |
| s57(id=49 S2->S1) | sw02-p2 | Q6 | 317760 | 12480 |

## Constraint check

- C1-C7, C9: OK
- window-boundary integrity (no window's psi/delta changed anywhere): OK

## GCL per egress port

### sw01-p2  (24 entries, util 17.1600 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 45440 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 29120 0xBF # 10111111   Q7
sgs 8000 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 36480 0x40 # 01000000   Q6
sgs 30720 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 8320 0x3F # 00111111   BE
sgs 111040 0x80 # 10000000   Q7
sgs 30720 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 8320 0x3F # 00111111   BE
sgs 111040 0x80 # 10000000   Q7
sgs 30720 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 29120 0xBF # 10111111   Q7
```

### sw01-p4  (22 entries, util 21.8400 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 61120 0x40 # 01000000   Q6
sgs 22400 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 111040 0x80 # 10000000   Q7
sgs 22400 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 86080 0x40 # 01000000   Q6
sgs 22400 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 94400 0x80 # 10000000   Q7
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (24 entries, util 31.2000 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 21120 0xBF # 10111111   Q7
sgs 3840 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 33600 0x7F # 01111111   Q6
sgs 32960 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 4480 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
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

### sw02-p4  (26 entries, util 40.5600 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 37120 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 50240 0x40 # 01000000   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 125120 0x80 # 10000000   Q7
sgs 33280 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 99840 0x80 # 10000000   Q7
sgs 33280 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 108480 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (20 entries, util 17.1600 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 28800 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 37120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 36480 0x40 # 01000000   Q6
sgs 47360 0xBF # 10111111   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 111040 0x80 # 10000000   Q7
sgs 47360 0xBF # 10111111   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 111040 0x80 # 10000000   Q7
sgs 47360 0xBF # 10111111   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 45760 0xBF # 10111111   Q7
```

### sw03-p5  (22 entries, util 21.8400 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 61120 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 111040 0x80 # 10000000   Q7
sgs 5760 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 86080 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 77760 0x80 # 10000000   Q7
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p4  (22 entries, util 31.2000 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 16320 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 21120 0xBF # 10111111   Q7
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

### sw04-p5  (26 entries, util 40.5600 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 37120 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 50240 0x40 # 01000000   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0x3F # 00111111   BE
sgs 124800 0x80 # 10000000   Q7
sgs 16640 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 99840 0x80 # 10000000   Q7
sgs 16640 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0x3F # 00111111   BE
sgs 91520 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (19 entries, util 21.8400 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 61120 0x40 # 01000000   Q6
sgs 39040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 111040 0x80 # 10000000   Q7
sgs 39040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 86080 0x40 # 01000000   Q6
sgs 39040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 61120 0x80 # 10000000   Q7
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p5  (25 entries, util 17.1600 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 24640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 36480 0x40 # 01000000   Q6
sgs 13760 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 111040 0x80 # 10000000   Q7
sgs 13760 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 111040 0x80 # 10000000   Q7
sgs 13760 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p4  (23 entries, util 40.5600 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 37120 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 50240 0x40 # 01000000   Q6
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 124800 0x80 # 10000000   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 99840 0x80 # 10000000   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 74880 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (22 entries, util 31.2000 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 20800 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 16960 0xBF # 10111111   Q7
sgs 49600 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 37760 0xBF # 10111111   Q7
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

### sw07-p4  (24 entries, util 17.1600 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 45760 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 8000 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 36480 0x40 # 01000000   Q6
sgs 30400 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 8320 0x3F # 00111111   BE
sgs 111040 0x80 # 10000000   Q7
sgs 30400 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 8320 0x3F # 00111111   BE
sgs 111040 0x80 # 10000000   Q7
sgs 30400 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p5  (23 entries, util 21.8400 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 61120 0x40 # 01000000   Q6
sgs 22400 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 111040 0x80 # 10000000   Q7
sgs 22400 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 86080 0x40 # 01000000   Q6
sgs 22400 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 44480 0x80 # 10000000   Q7
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p2  (21 entries, util 43.6800 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 29120 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 95680 0x80 # 10000000   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 150080 0x80 # 10000000   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 29120 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 95680 0x80 # 10000000   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 83520 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p4  (23 entries, util 31.2000 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 33600 0xBF # 10111111   Q7
sgs 32960 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 4480 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
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

### sw08-p5  (20 entries, util 17.1600 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 37120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 36480 0x40 # 01000000   Q6
sgs 47040 0x7F # 01111111   Q6
sgs 41920 0xBF # 10111111   Q7
sgs 111040 0x80 # 10000000   Q7
sgs 47040 0x7F # 01111111   Q6
sgs 41920 0xBF # 10111111   Q7
sgs 111040 0x80 # 10000000   Q7
sgs 47040 0x7F # 01111111   Q6
sgs 41920 0xBF # 10111111   Q7
sgs 19200 0x80 # 10000000   Q7
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

