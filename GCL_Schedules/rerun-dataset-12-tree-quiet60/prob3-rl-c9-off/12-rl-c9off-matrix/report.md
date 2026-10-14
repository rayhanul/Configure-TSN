# Reconfiguration-free admission (Problem 3)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Frozen schedule W loaded from: **result/result-2026-10-13-dataset-testbed-12-tree-avgwin/rl-c9-off/12-matrix-c9off**

## Admission: W (before) vs. after this run's arrivals

| | admitted | of total |
|---|---|---|
| W (base, unchanged) | 11 | 11 |
| + this run's arrivals | 22 | 39 |

Every arrival admitted here required **zero** window-boundary changes -- see the GCL-entry table below (unchanged from W by construction) and the window-boundary integrity check. No previously-admitted flow was rerouted.

## Arrivals

| id | src->dst | RS(s) size | admitted | route | queue | phi_s (ns) | e2e (ns) | rerouted to make room | reason if rejected |
|---|---|---|---|---|---|---|---|---|---|
| 10 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 20 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 12480 | 95680 | - | - |
| 3 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q7 | 37440 | 224960 | - | - |
| 15 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 24960 | 95680 | - | - |
| 16 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 | 212800 | 95680 | - | - |
| 1 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 237760 | 83520 | - | - |
| 17 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 250880 | 83200 | - | - |
| 6 | S1->S3 | - | yes | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 112640 | 210880 | - | - |
| 13 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 49920 | 95680 | - | - |
| 27 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 147520 | 228160 | - | - |
| 32 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 437440 | 79040 | - | - |
| 38 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q6 | 125440 | 103680 | - | - |
| 45 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q7 | 160320 | 235520 | - | - |
| 50 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 450240 | 79040 | - | - |
| 30 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 288000 | 95680 | - | - |
| 42 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 462720 | 260800 | - | - |
| 43 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q6 | 62720 | 179200 | - | - |
| 31 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q6 | 75520 | 229120 | - | - |
| 40 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q6 | 88320 | 403520 | - | - |
| 22 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 24 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 25 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 263680 | 83200 | - | - |
| 33 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 280640 | 81920 | - | - |
| 34 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 293440 | 85760 | - | - |
| 36 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 306240 | 89600 | - | - |
| 49 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
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
| sw01-p2 | 27 | 27 | 255 |
| sw01-p4 | 20 | 20 | 255 |
| sw02-p2 | 21 | 21 | 255 |
| sw02-p4 | 26 | 26 | 255 |
| sw03-p4 | 30 | 30 | 255 |
| sw03-p5 | 20 | 20 | 255 |
| sw04-p4 | 18 | 18 | 255 |
| sw04-p5 | 26 | 26 | 255 |
| sw05-p4 | 20 | 20 | 255 |
| sw05-p5 | 34 | 34 | 255 |
| sw06-p4 | 23 | 23 | 255 |
| sw06-p5 | 20 | 20 | 255 |
| sw07-p4 | 26 | 26 | 255 |
| sw07-p5 | 24 | 24 | 255 |
| sw08-p2 | 21 | 21 | 255 |
| sw08-p4 | 20 | 20 | 255 |
| sw08-p5 | 29 | 29 | 255 |

## Per-hop windows used by newly admitted flows

| flow | egress port | queue | psi (ns, unchanged) | delta (ns, unchanged) |
|---|---|---|---|---|
| s28(id=20 S2->S3) | S2-p0 | Q7 | 12480 | 12480 |
| s28(id=20 S2->S3) | sw08-p5 | Q7 | 29120 | 12480 |
| s28(id=20 S2->S3) | sw07-p4 | Q7 | 45760 | 12480 |
| s28(id=20 S2->S3) | sw05-p5 | Q7 | 62400 | 12480 |
| s28(id=20 S2->S3) | sw03-p4 | Q7 | 79040 | 12480 |
| s28(id=20 S2->S3) | sw01-p2 | Q7 | 95680 | 12480 |
| s21(id=3 S3->S1) | S3-p0 | Q7 | 37440 | 12480 |
| s21(id=3 S3->S1) | sw01-p4 | Q7 | 54080 | 12480 |
| s21(id=3 S3->S1) | sw03-p5 | Q7 | 70720 | 12480 |
| s21(id=3 S3->S1) | sw05-p4 | Q7 | 87360 | 12480 |
| s21(id=3 S3->S1) | sw07-p5 | Q7 | 134720 | 12480 |
| s21(id=3 S3->S1) | sw08-p4 | Q7 | 151360 | 12480 |
| s21(id=3 S3->S1) | sw06-p5 | Q7 | 168000 | 12480 |
| s21(id=3 S3->S1) | sw04-p4 | Q7 | 184640 | 12480 |
| s21(id=3 S3->S1) | sw02-p2 | Q7 | 249920 | 12480 |
| s25(id=15 S2->S3) | S2-p0 | Q6 | 24960 | 12480 |
| s25(id=15 S2->S3) | sw08-p5 | Q6 | 41600 | 12480 |
| s25(id=15 S2->S3) | sw07-p4 | Q6 | 58240 | 12480 |
| s25(id=15 S2->S3) | sw05-p5 | Q6 | 74880 | 12480 |
| s25(id=15 S2->S3) | sw03-p4 | Q6 | 91520 | 12480 |
| s25(id=15 S2->S3) | sw01-p2 | Q6 | 108160 | 12480 |
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
| s22(id=6 S1->S3) | sw08-p5 | Q6 | 200000 | 12480 |
| s22(id=6 S1->S3) | sw07-p4 | Q6 | 216640 | 12480 |
| s22(id=6 S1->S3) | sw05-p5 | Q6 | 233280 | 12480 |
| s22(id=6 S1->S3) | sw03-p4 | Q6 | 294400 | 12480 |
| s22(id=6 S1->S3) | sw01-p2 | Q6 | 311040 | 12480 |
| s24(id=13 S2->S3) | S2-p0 | Q7 | 49920 | 12480 |
| s24(id=13 S2->S3) | sw08-p5 | Q7 | 66560 | 12480 |
| s24(id=13 S2->S3) | sw07-p4 | Q7 | 83200 | 12480 |
| s24(id=13 S2->S3) | sw05-p5 | Q7 | 99840 | 12480 |
| s24(id=13 S2->S3) | sw03-p4 | Q7 | 116480 | 12480 |
| s24(id=13 S2->S3) | sw01-p2 | Q7 | 133120 | 12480 |
| s35(id=27 S2->S1) | S2-p0 | Q7 | 147520 | 12480 |
| s35(id=27 S2->S1) | sw08-p4 | Q7 | 164160 | 12480 |
| s35(id=27 S2->S1) | sw06-p5 | Q7 | 180800 | 12480 |
| s35(id=27 S2->S1) | sw04-p4 | Q7 | 346560 | 12480 |
| s35(id=27 S2->S1) | sw02-p2 | Q7 | 363200 | 12480 |
| s40(id=32 S2->S1) | S2-p0 | Q6 | 437440 | 12480 |
| s40(id=32 S2->S1) | sw08-p4 | Q6 | 454080 | 12480 |
| s40(id=32 S2->S1) | sw06-p5 | Q6 | 470720 | 12480 |
| s40(id=32 S2->S1) | sw04-p4 | Q6 | 487360 | 12480 |
| s40(id=32 S2->S1) | sw02-p2 | Q6 | 504000 | 12480 |
| s46(id=38 S1->S2) | S1-p0 | Q6 | 125440 | 12480 |
| s46(id=38 S1->S2) | sw02-p4 | Q6 | 142080 | 12480 |
| s46(id=38 S1->S2) | sw04-p5 | Q6 | 158720 | 12480 |
| s46(id=38 S1->S2) | sw06-p4 | Q6 | 175360 | 12480 |
| s46(id=38 S1->S2) | sw08-p2 | Q6 | 216640 | 12480 |
| s53(id=45 S2->S1) | S2-p0 | Q7 | 160320 | 12480 |
| s53(id=45 S2->S1) | sw08-p4 | Q7 | 176960 | 12480 |
| s53(id=45 S2->S1) | sw06-p5 | Q7 | 350080 | 12480 |
| s53(id=45 S2->S1) | sw04-p4 | Q7 | 366720 | 12480 |
| s53(id=45 S2->S1) | sw02-p2 | Q7 | 383360 | 12480 |
| s58(id=50 S2->S1) | S2-p0 | Q6 | 450240 | 12480 |
| s58(id=50 S2->S1) | sw08-p4 | Q6 | 466880 | 12480 |
| s58(id=50 S2->S1) | sw06-p5 | Q6 | 483520 | 12480 |
| s58(id=50 S2->S1) | sw04-p4 | Q6 | 500160 | 12480 |
| s58(id=50 S2->S1) | sw02-p2 | Q6 | 516800 | 12480 |
| s38(id=30 S2->S3) | S2-p0 | Q7 | 288000 | 12480 |
| s38(id=30 S2->S3) | sw08-p5 | Q7 | 304640 | 12480 |
| s38(id=30 S2->S3) | sw07-p4 | Q7 | 321280 | 12480 |
| s38(id=30 S2->S3) | sw05-p5 | Q7 | 337920 | 12480 |
| s38(id=30 S2->S3) | sw03-p4 | Q7 | 354560 | 12480 |
| s38(id=30 S2->S3) | sw01-p2 | Q7 | 371200 | 12480 |
| s50(id=42 S2->S3) | S2-p0 | Q6 | 462720 | 12480 |
| s50(id=42 S2->S3) | sw08-p5 | Q6 | 600000 | 12480 |
| s50(id=42 S2->S3) | sw07-p4 | Q6 | 616640 | 12480 |
| s50(id=42 S2->S3) | sw05-p5 | Q6 | 633280 | 12480 |
| s50(id=42 S2->S3) | sw03-p4 | Q6 | 694400 | 12480 |
| s50(id=42 S2->S3) | sw01-p2 | Q6 | 711040 | 12480 |
| s51(id=43 S3->S2) | S3-p0 | Q6 | 62720 | 12480 |
| s51(id=43 S3->S2) | sw01-p4 | Q6 | 79360 | 12480 |
| s51(id=43 S3->S2) | sw03-p5 | Q6 | 96000 | 12480 |
| s51(id=43 S3->S2) | sw05-p4 | Q6 | 112640 | 12480 |
| s51(id=43 S3->S2) | sw07-p5 | Q6 | 212800 | 12480 |
| s51(id=43 S3->S2) | sw08-p2 | Q6 | 229440 | 12480 |
| s39(id=31 S3->S1) | S3-p0 | Q6 | 75520 | 12480 |
| s39(id=31 S3->S1) | sw01-p4 | Q6 | 92160 | 12480 |
| s39(id=31 S3->S1) | sw03-p5 | Q6 | 108800 | 12480 |
| s39(id=31 S3->S1) | sw05-p4 | Q6 | 208960 | 12480 |
| s39(id=31 S3->S1) | sw07-p5 | Q6 | 225600 | 12480 |
| s39(id=31 S3->S1) | sw08-p4 | Q6 | 242240 | 12480 |
| s39(id=31 S3->S1) | sw06-p5 | Q6 | 258880 | 12480 |
| s39(id=31 S3->S1) | sw04-p4 | Q6 | 275520 | 12480 |
| s39(id=31 S3->S1) | sw02-p2 | Q6 | 292160 | 12480 |
| s48(id=40 S3->S1) | S3-p0 | Q6 | 88320 | 12480 |
| s48(id=40 S3->S1) | sw01-p4 | Q6 | 104960 | 12480 |
| s48(id=40 S3->S1) | sw03-p5 | Q6 | 205120 | 12480 |
| s48(id=40 S3->S1) | sw05-p4 | Q6 | 221760 | 12480 |
| s48(id=40 S3->S1) | sw07-p5 | Q6 | 412800 | 12480 |
| s48(id=40 S3->S1) | sw08-p4 | Q6 | 429440 | 12480 |
| s48(id=40 S3->S1) | sw06-p5 | Q6 | 446080 | 12480 |
| s48(id=40 S3->S1) | sw04-p4 | Q6 | 462720 | 12480 |
| s48(id=40 S3->S1) | sw02-p2 | Q6 | 479360 | 12480 |
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

## Constraint check

- C1-C7, C9: OK
- window-boundary integrity (no window's psi/delta changed anywhere): OK

## GCL per egress port

### sw01-p2  (27 entries, util 26.5200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 45760 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 37120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 15360 0x40 # 01000000   Q6
sgs 47360 0xBF # 10111111   Q7
sgs 15360 0x80 # 10000000   Q7
sgs 47360 0x7F # 01111111   Q6
sgs 89920 0x80 # 10000000   Q7
sgs 47360 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 37760 0x7F # 01111111   Q6
sgs 89920 0x80 # 10000000   Q7
sgs 47360 0xBF # 10111111   Q7
sgs 15360 0x80 # 10000000   Q7
sgs 47360 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 29120 0xBF # 10111111   Q7
```

### sw01-p4  (20 entries, util 21.8400 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 79040 0x40 # 01000000   Q6
sgs 54400 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 128960 0x80 # 10000000   Q7
sgs 54400 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 91520 0x80 # 10000000   Q7
sgs 54400 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 112320 0x80 # 10000000   Q7
sgs 21120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (21 entries, util 21.8400 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 33600 0x7F # 01111111   Q6
sgs 32960 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 54400 0x7F # 01111111   Q6
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
sgs 53440 0x7F # 01111111   Q6
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

### sw03-p4  (30 entries, util 26.5200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 37120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 15360 0x40 # 01000000   Q6
sgs 18240 0x7F # 01111111   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 15360 0x80 # 10000000   Q7
sgs 47360 0x7F # 01111111   Q6
sgs 89920 0x80 # 10000000   Q7
sgs 18240 0x7F # 01111111   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 37760 0x7F # 01111111   Q6
sgs 89920 0x80 # 10000000   Q7
sgs 18240 0x7F # 01111111   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 15360 0x80 # 10000000   Q7
sgs 47360 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 45760 0xBF # 10111111   Q7
```

### sw03-p5  (20 entries, util 21.8400 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 79040 0x40 # 01000000   Q6
sgs 37760 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 128960 0x80 # 10000000   Q7
sgs 37760 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 91520 0x80 # 10000000   Q7
sgs 37760 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 95680 0x80 # 10000000   Q7
sgs 21120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p4  (18 entries, util 21.8400 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 50240 0x7F # 01111111   Q6
sgs 16320 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 21120 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 96640 0x40 # 01000000   Q6
sgs 53440 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 96640 0x40 # 01000000   Q6
sgs 53440 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 46720 0x40 # 01000000   Q6
sgs 53440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (26 entries, util 40.5600 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 37120 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 50240 0x40 # 01000000   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 124800 0x80 # 10000000   Q7
sgs 16640 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 99840 0x80 # 10000000   Q7
sgs 16640 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 91520 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (20 entries, util 21.8400 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 79040 0x40 # 01000000   Q6
sgs 21120 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 128960 0x80 # 10000000   Q7
sgs 21120 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 91520 0x80 # 10000000   Q7
sgs 21120 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 79040 0x80 # 10000000   Q7
sgs 21120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p5  (34 entries, util 26.5200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 24640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 15360 0x40 # 01000000   Q6
sgs 34880 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 15360 0x80 # 10000000   Q7
sgs 22400 0xBF # 10111111   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 89920 0x80 # 10000000   Q7
sgs 34880 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12800 0xBF # 10111111   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 89920 0x80 # 10000000   Q7
sgs 34880 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 15360 0x80 # 10000000   Q7
sgs 22400 0xBF # 10111111   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 27520 0x80 # 10000000   Q7
sgs 47360 0xBF # 10111111   Q7
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

### sw06-p5  (20 entries, util 21.8400 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 24960 0xBF # 10111111   Q7
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
sgs 53440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (26 entries, util 26.5200 %)

```
sgs 45760 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 37120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 15360 0x40 # 01000000   Q6
sgs 47360 0x7F # 01111111   Q6
sgs 15360 0x80 # 10000000   Q7
sgs 47360 0xBF # 10111111   Q7
sgs 89920 0x80 # 10000000   Q7
sgs 47360 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 37760 0xBF # 10111111   Q7
sgs 89920 0x80 # 10000000   Q7
sgs 47360 0x7F # 01111111   Q6
sgs 15360 0x80 # 10000000   Q7
sgs 47360 0xBF # 10111111   Q7
sgs 44160 0x80 # 10000000   Q7
sgs 47360 0xBF # 10111111   Q7
```

### sw07-p5  (24 entries, util 21.8400 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 60800 0x80 # 10000000   Q7
sgs 54400 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 128960 0x80 # 10000000   Q7
sgs 54400 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 30720 0x7F # 01111111   Q6
sgs 60800 0x80 # 10000000   Q7
sgs 54400 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 62400 0x80 # 10000000   Q7
sgs 21120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p2  (21 entries, util 43.6800 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 29120 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 95680 0x80 # 10000000   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 150080 0x80 # 10000000   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 29120 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 95680 0x80 # 10000000   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 83520 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p4  (20 entries, util 21.8400 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 24960 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 33600 0xBF # 10111111   Q7
sgs 32960 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 54400 0xBF # 10111111   Q7
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
sgs 53440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (29 entries, util 26.5200 %)

```
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 37120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 15360 0x40 # 01000000   Q6
sgs 18240 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 15360 0x80 # 10000000   Q7
sgs 47360 0xBF # 10111111   Q7
sgs 89920 0x80 # 10000000   Q7
sgs 18240 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 37760 0xBF # 10111111   Q7
sgs 89920 0x80 # 10000000   Q7
sgs 18240 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 15360 0x80 # 10000000   Q7
sgs 47360 0xBF # 10111111   Q7
sgs 60800 0x80 # 10000000   Q7
sgs 47360 0xBF # 10111111   Q7
```

