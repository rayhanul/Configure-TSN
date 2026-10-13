# Reconfiguration-free admission (Problem 3)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Frozen schedule W loaded from: **result/result-2026-10-12-dataset-testbed-10-ring-avgwin/heuristic-c9-on/10-matrix-c9on**

## Admission: W (before) vs. after this run's arrivals

| | admitted | of total |
|---|---|---|
| W (base, unchanged) | 11 | 11 |
| + this run's arrivals | 22 | 39 |

Every arrival admitted here required **zero** window-boundary changes -- see the GCL-entry table below (unchanged from W by construction) and the window-boundary integrity check. No previously-admitted flow was rerouted.

## Arrivals

| id | src->dst | RS(s) size | admitted | route | queue | phi_s (ns) | e2e (ns) | rerouted to make room | reason if rejected |
|---|---|---|---|---|---|---|---|---|---|
| 20 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 4 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 13 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q6 | 12480 | 200000 | - | - |
| 16 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 14 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 2 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 | 62400 | 120000 | - | - |
| 8 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q7 | 237440 | 140480 | - | - |
| 6 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q7 | 62400 | 115520 | - | - |
| 19 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q6 | 131520 | 217920 | - | - |
| 34 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q7 | 87360 | 31040 | - | - |
| 47 | S3->S1 | - | yes | S3->sw01->sw02->S1 | Q6 | 331520 | 88640 | - | - |
| 21 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q6 | 90240 | 55680 | - | - |
| 22 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q7 | 150080 | 44800 | - | - |
| 40 | S2->S1 | - | yes | S2->sw08->sw06->sw04->sw02->S1 | Q6 | 62400 | 370560 | - | - |
| 23 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 12480 | 144320 | - | - |
| 24 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 | 215360 | 68160 | - | - |
| 28 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q6 | 102720 | 27840 | - | - |
| 30 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q6 | 507840 | 117440 | - | - |
| 38 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 39 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q7 | 162560 | 27840 | - | - |
| 42 | S1->S3 | - | yes | S1->sw02->sw01->S3 | Q6 | 115200 | 27840 | - | - |
| 46 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 111040 | 301440 | - | - |
| 50 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 123520 | 432000 | - | - |
| 27 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 29 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 31 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 | 227840 | 69760 | - | - |
| 32 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 | 240320 | 71680 | - | - |
| 35 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 212800 | 42880 | - | - |
| 36 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 41 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 45 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 48 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 | 256320 | 131200 | - | - |
| 25 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 33 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 43 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 44 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 49 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 26 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 37 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |

## Per-port GCL entries (should equal W exactly)

| port | W entries | after arrivals | GCL_size |
|---|---|---|---|
| sw01-p2 | 28 | 28 | 255 |
| sw01-p4 | 20 | 20 | 255 |
| sw01-p5 | 11 | 11 | 255 |
| sw02-p2 | 11 | 11 | 255 |
| sw02-p4 | 20 | 20 | 255 |
| sw02-p5 | 23 | 23 | 255 |
| sw03-p4 | 21 | 21 | 255 |
| sw03-p5 | 21 | 21 | 255 |
| sw04-p4 | 10 | 10 | 255 |
| sw04-p5 | 19 | 19 | 255 |
| sw05-p4 | 21 | 21 | 255 |
| sw05-p5 | 21 | 21 | 255 |
| sw06-p4 | 19 | 19 | 255 |
| sw06-p5 | 10 | 10 | 255 |
| sw07-p4 | 21 | 21 | 255 |
| sw07-p5 | 18 | 18 | 255 |
| sw08-p2 | 16 | 16 | 255 |
| sw08-p4 | 10 | 10 | 255 |
| sw08-p5 | 21 | 21 | 255 |

## Per-hop windows used by newly admitted flows

| flow | egress port | queue | psi (ns, unchanged) | delta (ns, unchanged) |
|---|---|---|---|---|
| s24(id=13 S3->S2) | S3-p0 | Q6 | 12480 | 12480 |
| s24(id=13 S3->S2) | sw01-p4 | Q6 | 100160 | 12480 |
| s24(id=13 S3->S2) | sw03-p5 | Q6 | 105280 | 12480 |
| s24(id=13 S3->S2) | sw05-p4 | Q6 | 110400 | 12480 |
| s24(id=13 S3->S2) | sw07-p5 | Q6 | 115520 | 12480 |
| s24(id=13 S3->S2) | sw08-p2 | Q6 | 120640 | 12480 |
| s20(id=2 S3->S2) | S3-p0 | Q7 | 62400 | 12480 |
| s20(id=2 S3->S2) | sw01-p4 | Q7 | 69120 | 12480 |
| s20(id=2 S3->S2) | sw03-p5 | Q7 | 75840 | 12480 |
| s20(id=2 S3->S2) | sw05-p4 | Q7 | 82560 | 12480 |
| s20(id=2 S3->S2) | sw07-p5 | Q7 | 89280 | 12480 |
| s20(id=2 S3->S2) | sw08-p2 | Q7 | 169920 | 12480 |
| s23(id=8 S1->S3) | S1-p0 | Q7 | 237440 | 12480 |
| s23(id=8 S1->S3) | sw02-p5 | Q7 | 350080 | 12480 |
| s23(id=8 S1->S3) | sw01-p2 | Q7 | 365440 | 12480 |
| s22(id=6 S1->S3) | S1-p0 | Q7 | 62400 | 12480 |
| s22(id=6 S1->S3) | sw02-p5 | Q7 | 150080 | 12480 |
| s22(id=6 S1->S3) | sw01-p2 | Q7 | 165440 | 12480 |
| s27(id=19 S3->S1) | S3-p0 | Q6 | 131520 | 12480 |
| s27(id=19 S3->S1) | sw01-p5 | Q6 | 309760 | 12480 |
| s27(id=19 S3->S1) | sw02-p2 | Q6 | 336960 | 12480 |
| s42(id=34 S3->S1) | S3-p0 | Q7 | 87360 | 12480 |
| s42(id=34 S3->S1) | sw01-p5 | Q7 | 95040 | 12480 |
| s42(id=34 S3->S1) | sw02-p2 | Q7 | 105920 | 12480 |
| s55(id=47 S3->S1) | S3-p0 | Q6 | 331520 | 12480 |
| s55(id=47 S3->S1) | sw01-p5 | Q6 | 400000 | 12480 |
| s55(id=47 S3->S1) | sw02-p2 | Q6 | 407680 | 12480 |
| s29(id=21 S1->S2) | S1-p0 | Q6 | 90240 | 12480 |
| s29(id=21 S1->S2) | sw02-p4 | Q6 | 95360 | 12480 |
| s29(id=21 S1->S2) | sw04-p5 | Q6 | 102720 | 12480 |
| s29(id=21 S1->S2) | sw06-p4 | Q6 | 128320 | 12480 |
| s29(id=21 S1->S2) | sw08-p2 | Q6 | 133440 | 12480 |
| s30(id=22 S1->S2) | S1-p0 | Q7 | 150080 | 12480 |
| s30(id=22 S1->S2) | sw02-p4 | Q7 | 157760 | 12480 |
| s30(id=22 S1->S2) | sw04-p5 | Q7 | 165440 | 12480 |
| s30(id=22 S1->S2) | sw06-p4 | Q7 | 173120 | 12480 |
| s30(id=22 S1->S2) | sw08-p2 | Q7 | 182400 | 12480 |
| s48(id=40 S2->S1) | S2-p0 | Q6 | 62400 | 12480 |
| s48(id=40 S2->S1) | sw08-p4 | Q6 | 70080 | 12480 |
| s48(id=40 S2->S1) | sw06-p5 | Q6 | 77760 | 12480 |
| s48(id=40 S2->S1) | sw04-p4 | Q6 | 414400 | 12480 |
| s48(id=40 S2->S1) | sw02-p2 | Q6 | 420480 | 12480 |
| s31(id=23 S2->S3) | S2-p0 | Q6 | 12480 | 12480 |
| s31(id=23 S2->S3) | sw08-p5 | Q6 | 102720 | 12480 |
| s31(id=23 S2->S3) | sw07-p4 | Q6 | 111040 | 12480 |
| s31(id=23 S2->S3) | sw05-p5 | Q6 | 127680 | 12480 |
| s31(id=23 S2->S3) | sw03-p4 | Q6 | 136000 | 12480 |
| s31(id=23 S2->S3) | sw01-p2 | Q6 | 144320 | 12480 |
| s32(id=24 S3->S2) | S3-p0 | Q7 | 215360 | 12480 |
| s32(id=24 S3->S2) | sw01-p4 | Q7 | 220480 | 12480 |
| s32(id=24 S3->S2) | sw03-p5 | Q7 | 227840 | 12480 |
| s32(id=24 S3->S2) | sw05-p4 | Q7 | 235520 | 12480 |
| s32(id=24 S3->S2) | sw07-p5 | Q7 | 265920 | 12480 |
| s32(id=24 S3->S2) | sw08-p2 | Q7 | 271040 | 12480 |
| s36(id=28 S1->S3) | S1-p0 | Q6 | 102720 | 12480 |
| s36(id=28 S1->S3) | sw02-p5 | Q6 | 110400 | 12480 |
| s36(id=28 S1->S3) | sw01-p2 | Q6 | 118080 | 12480 |
| s38(id=30 S3->S2) | S3-p0 | Q6 | 507840 | 12480 |
| s38(id=30 S3->S2) | sw01-p4 | Q6 | 512960 | 12480 |
| s38(id=30 S3->S2) | sw03-p5 | Q6 | 518080 | 12480 |
| s38(id=30 S3->S2) | sw05-p4 | Q6 | 523200 | 12480 |
| s38(id=30 S3->S2) | sw07-p5 | Q6 | 607680 | 12480 |
| s38(id=30 S3->S2) | sw08-p2 | Q6 | 612800 | 12480 |
| s47(id=39 S1->S3) | S1-p0 | Q7 | 162560 | 12480 |
| s47(id=39 S1->S3) | sw02-p5 | Q7 | 167680 | 12480 |
| s47(id=39 S1->S3) | sw01-p2 | Q7 | 177920 | 12480 |
| s50(id=42 S1->S3) | S1-p0 | Q6 | 115200 | 12480 |
| s50(id=42 S1->S3) | sw02-p5 | Q6 | 122880 | 12480 |
| s50(id=42 S1->S3) | sw01-p2 | Q6 | 130560 | 12480 |
| s54(id=46 S2->S3) | S2-p0 | Q6 | 111040 | 12480 |
| s54(id=46 S2->S3) | sw08-p5 | Q6 | 119360 | 12480 |
| s54(id=46 S2->S3) | sw07-p4 | Q6 | 127680 | 12480 |
| s54(id=46 S2->S3) | sw05-p5 | Q6 | 200000 | 12480 |
| s54(id=46 S2->S3) | sw03-p4 | Q6 | 333760 | 12480 |
| s54(id=46 S2->S3) | sw01-p2 | Q6 | 400000 | 12480 |
| s58(id=50 S2->S3) | S2-p0 | Q6 | 123520 | 12480 |
| s58(id=50 S2->S3) | sw08-p5 | Q6 | 131840 | 12480 |
| s58(id=50 S2->S3) | sw07-p4 | Q6 | 308800 | 12480 |
| s58(id=50 S2->S3) | sw05-p5 | Q6 | 400000 | 12480 |
| s58(id=50 S2->S3) | sw03-p4 | Q6 | 533760 | 12480 |
| s58(id=50 S2->S3) | sw01-p2 | Q6 | 543040 | 12480 |
| s39(id=31 S3->S2) | S3-p0 | Q7 | 227840 | 12480 |
| s39(id=31 S3->S2) | sw01-p4 | Q7 | 234560 | 12480 |
| s39(id=31 S3->S2) | sw03-p5 | Q7 | 241280 | 12480 |
| s39(id=31 S3->S2) | sw05-p4 | Q7 | 270400 | 12480 |
| s39(id=31 S3->S2) | sw07-p5 | Q7 | 278400 | 12480 |
| s39(id=31 S3->S2) | sw08-p2 | Q7 | 285120 | 12480 |
| s40(id=32 S3->S2) | S3-p0 | Q7 | 240320 | 12480 |
| s40(id=32 S3->S2) | sw01-p4 | Q7 | 257920 | 12480 |
| s40(id=32 S3->S2) | sw03-p5 | Q7 | 272960 | 12480 |
| s40(id=32 S3->S2) | sw05-p4 | Q7 | 282880 | 12480 |
| s40(id=32 S3->S2) | sw07-p5 | Q7 | 291200 | 12480 |
| s40(id=32 S3->S2) | sw08-p2 | Q7 | 299520 | 12480 |
| s43(id=35 S2->S3) | S2-p0 | Q7 | 212800 | 12480 |
| s43(id=35 S2->S3) | sw08-p5 | Q7 | 218880 | 12480 |
| s43(id=35 S2->S3) | sw07-p4 | Q7 | 224960 | 12480 |
| s43(id=35 S2->S3) | sw05-p5 | Q7 | 231040 | 12480 |
| s43(id=35 S2->S3) | sw03-p4 | Q7 | 237120 | 12480 |
| s43(id=35 S2->S3) | sw01-p2 | Q7 | 243200 | 12480 |
| s56(id=48 S3->S2) | S3-p0 | Q7 | 256320 | 12480 |
| s56(id=48 S3->S2) | sw01-p4 | Q7 | 270400 | 12480 |
| s56(id=48 S3->S2) | sw03-p5 | Q7 | 350080 | 12480 |
| s56(id=48 S3->S2) | sw05-p4 | Q7 | 358400 | 12480 |
| s56(id=48 S3->S2) | sw07-p5 | Q7 | 366720 | 12480 |
| s56(id=48 S3->S2) | sw08-p2 | Q7 | 375040 | 12480 |

## Constraint check

- C1-C7, C9: OK
- window-boundary integrity (no window's psi/delta changed anywhere): OK

## GCL per egress port

### sw01-p2  (28 entries, util 40.5600 %)

```
sgs 15360 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 2560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 97280 0x40 # 01000000   Q6
sgs 34560 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 2560 0x3F # 00111111   BE
sgs 135040 0x80 # 10000000   Q7
sgs 34560 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 2560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 97280 0x40 # 01000000   Q6
sgs 34560 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 2560 0x3F # 00111111   BE
sgs 119680 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p4  (20 entries, util 23.4000 %)

```
sgs 7680 0x3F # 00111111   BE
sgs 50240 0x80 # 10000000   Q7
sgs 42240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 7680 0x3F # 00111111   BE
sgs 50240 0x80 # 10000000   Q7
sgs 42240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 7680 0x3F # 00111111   BE
sgs 50240 0x80 # 10000000   Q7
sgs 42240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 7680 0x3F # 00111111   BE
sgs 42560 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p5  (11 entries, util 12.4800 %)

```
sgs 32640 0x7F # 01111111   Q6
sgs 36480 0x40 # 01000000   Q6
sgs 13440 0xBF # 10111111   Q7
sgs 227200 0x80 # 10000000   Q7
sgs 40320 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 32640 0x7F # 01111111   Q6
sgs 244480 0x40 # 01000000   Q6
sgs 23040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (11 entries, util 15.6000 %)

```
sgs 40320 0x7F # 01111111   Q6
sgs 52800 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 243520 0x80 # 10000000   Q7
sgs 13120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 40320 0x7F # 01111111   Q6
sgs 256320 0x40 # 01000000   Q6
sgs 3520 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p4  (20 entries, util 10.9200 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 32640 0xBF # 10111111   Q7
sgs 27840 0x40 # 01000000   Q6
sgs 39680 0x7F # 01111111   Q6
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

### sw02-p5  (23 entries, util 23.4000 %)

```
sgs 7680 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 29760 0x7F # 01111111   Q6
sgs 6080 0x3F # 00111111   BE
sgs 48320 0x40 # 01000000   Q6
sgs 45760 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 7680 0x3F # 00111111   BE
sgs 96640 0x40 # 01000000   Q6
sgs 45760 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 7680 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 29760 0x7F # 01111111   Q6
sgs 6080 0x3F # 00111111   BE
sgs 48320 0x40 # 01000000   Q6
sgs 45760 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 7680 0x3F # 00111111   BE
sgs 88960 0x40 # 01000000   Q6
sgs 3520 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (21 entries, util 17.1600 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 11840 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 84480 0x80 # 10000000   Q7
sgs 16320 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 24320 0x7F # 01111111   Q6
sgs 109440 0x80 # 10000000   Q7
sgs 16320 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 24320 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 84480 0x80 # 10000000   Q7
sgs 16320 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 24320 0x7F # 01111111   Q6
sgs 85120 0x80 # 10000000   Q7
sgs 40640 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p5  (21 entries, util 23.4000 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 2880 0x3F # 00111111   BE
sgs 75200 0x80 # 10000000   Q7
sgs 9600 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 75200 0x80 # 10000000   Q7
sgs 9600 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 75200 0x80 # 10000000   Q7
sgs 9600 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 59840 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p4  (10 entries, util 3.1200 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 23040 0xBF # 10111111   Q7
sgs 464640 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (19 entries, util 10.9200 %)

```
sgs 41600 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 36160 0xBF # 10111111   Q7
sgs 28480 0x40 # 01000000   Q6
sgs 31360 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 77120 0x80 # 10000000   Q7
sgs 31360 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 77120 0x80 # 10000000   Q7
sgs 31360 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 35520 0x80 # 10000000   Q7
sgs 23040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (21 entries, util 23.4000 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 10560 0x3F # 00111111   BE
sgs 75200 0x80 # 10000000   Q7
sgs 1920 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 75200 0x80 # 10000000   Q7
sgs 1920 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 75200 0x80 # 10000000   Q7
sgs 1920 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 52160 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p5  (21 entries, util 17.1600 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 84480 0x80 # 10000000   Q7
sgs 22400 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 18240 0x7F # 01111111   Q6
sgs 109440 0x80 # 10000000   Q7
sgs 22400 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 18240 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 84480 0x80 # 10000000   Q7
sgs 22400 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 18240 0x7F # 01111111   Q6
sgs 91200 0x80 # 10000000   Q7
sgs 40640 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p4  (19 entries, util 10.9200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 35520 0xBF # 10111111   Q7
sgs 29120 0x40 # 01000000   Q6
sgs 23040 0x7F # 01111111   Q6
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

### sw06-p5  (10 entries, util 3.1200 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 15360 0xBF # 10111111   Q7
sgs 472320 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (21 entries, util 17.1600 %)

```
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 71680 0x80 # 10000000   Q7
sgs 41280 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 12160 0x3F # 00111111   BE
sgs 96640 0x80 # 10000000   Q7
sgs 41280 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 71680 0x80 # 10000000   Q7
sgs 41280 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 12160 0x3F # 00111111   BE
sgs 84480 0x80 # 10000000   Q7
sgs 3520 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p5  (18 entries, util 23.4000 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 18240 0x7F # 01111111   Q6
sgs 75200 0x80 # 10000000   Q7
sgs 44160 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 75200 0x80 # 10000000   Q7
sgs 44160 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 75200 0x80 # 10000000   Q7
sgs 44160 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 44480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p2  (16 entries, util 34.3200 %)

```
sgs 38400 0x7F # 01111111   Q6
sgs 32320 0x80 # 10000000   Q7
sgs 29440 0xBF # 10111111   Q7
sgs 5440 0x3F # 00111111   BE
sgs 64320 0x40 # 01000000   Q6
sgs 30080 0xBF # 10111111   Q7
sgs 38400 0x7F # 01111111   Q6
sgs 131520 0x80 # 10000000   Q7
sgs 30080 0xBF # 10111111   Q7
sgs 38400 0x7F # 01111111   Q6
sgs 131520 0x80 # 10000000   Q7
sgs 30080 0xBF # 10111111   Q7
sgs 38400 0x7F # 01111111   Q6
sgs 93120 0x80 # 10000000   Q7
sgs 18560 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p4  (10 entries, util 3.1200 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 7680 0x3F # 00111111   BE
sgs 480000 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (21 entries, util 17.1600 %)

```
sgs 6080 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 71680 0x80 # 10000000   Q7
sgs 47360 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 6080 0x3F # 00111111   BE
sgs 96640 0x80 # 10000000   Q7
sgs 47360 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 6080 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 71680 0x80 # 10000000   Q7
sgs 47360 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 6080 0x3F # 00111111   BE
sgs 90560 0x80 # 10000000   Q7
sgs 3520 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

