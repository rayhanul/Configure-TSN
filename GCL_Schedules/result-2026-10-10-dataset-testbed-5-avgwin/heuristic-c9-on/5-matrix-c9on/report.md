# Heuristic-enlarged GCL schedule (Problem 2: window enlargement)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Time-sensitive PCPs considered: [6, 7]
- Seeded from SMT run: **result/result-2026-10-10-dataset-testbed-5-avgwin/smt-c9-on/5-fair-retimed-c9on**

## Admission (unchanged by this package -- it only widens windows)

SMT-fixed flows: **10**/10. This package never admits a flow itself; it banks slack for a later admission pass (`prob_3_admit`, Problem 3) to use.

## Opportunistic idle top-up (Step 7 -- see enlarge.py)

Total: **12632320 ns**, drawn from idle capacity on ports at or below utilisation 0.2, independent of any route's deadline-slack budget.

| port | queue | applied (ns) |
|---|---|---|
| S1-p0 | Q6 | 403840 |
| S1-p0 | Q7 | 205760 |
| S2-p0 | Q6 | 49600 |
| S2-p0 | Q7 | 526400 |
| S3-p0 | Q6 | 685760 |
| sw01-p2 | Q7 | 669760 |
| sw01-p4 | Q6 | 679360 |
| sw02-p2 | Q6 | 673600 |
| sw02-p4 | Q6 | 397760 |
| sw02-p4 | Q7 | 220480 |
| sw03-p4 | Q7 | 680320 |
| sw03-p5 | Q6 | 672640 |
| sw04-p4 | Q6 | 686400 |
| sw04-p5 | Q6 | 390720 |
| sw04-p5 | Q7 | 232960 |
| sw05-p4 | Q6 | 665600 |
| sw05-p5 | Q7 | 689920 |
| sw06-p4 | Q6 | 383680 |
| sw06-p4 | Q7 | 242880 |
| sw06-p5 | Q6 | 698560 |
| sw07-p4 | Q7 | 699200 |
| sw07-p5 | Q6 | 658560 |
| sw08-p4 | Q6 | 710400 |
| sw08-p5 | Q7 | 708160 |

## Opportunistic window creation (Step 8 -- see enlarge.py)

**13** brand-new window(s) opened, **162240 ns** total, on ports at or below utilisation 0.2 whose TT queue had zero windows before this run.

| port | queue | size (ns) |
|---|---|---|
| S3-p0 | Q7 | 12480 |
| sw01-p2 | Q6 | 12480 |
| sw01-p4 | Q7 | 12480 |
| sw02-p2 | Q7 | 12480 |
| sw03-p4 | Q6 | 12480 |
| sw03-p5 | Q7 | 12480 |
| sw04-p4 | Q7 | 12480 |
| sw05-p4 | Q7 | 12480 |
| sw05-p5 | Q6 | 12480 |
| sw06-p5 | Q7 | 12480 |
| sw07-p4 | Q6 | 12480 |
| sw07-p5 | Q7 | 12480 |
| sw08-p4 | Q7 | 12480 |

## Best-effort gap equalization (Step 9 -- see enlarge.py)

**7488320 ns** given back from Steps 7/8's growth so each port's leftover non-TAS gaps land close to equal, instead of one gap staying huge while a neighbour is squeezed to the bare 1-tick C10 minimum.

| port | given back (ns) |
|---|---|
| sw08-p5 | 472640 |
| sw01-p2 | 434240 |
| sw03-p4 | 434240 |
| sw05-p5 | 434240 |
| sw07-p4 | 434240 |
| S2-p0 | 418240 |
| sw02-p2 | 387200 |
| sw04-p4 | 387200 |
| sw06-p5 | 387200 |
| sw08-p4 | 387200 |
| S1-p0 | 385920 |
| sw02-p4 | 384640 |
| sw04-p5 | 383360 |
| sw06-p4 | 382080 |
| S3-p0 | 353600 |
| sw01-p4 | 353280 |
| sw03-p5 | 351040 |
| sw05-p4 | 348800 |
| sw07-p5 | 347520 |
| sw08-p2 | 21440 |

## Opportunistic overlay window creation (Step 10 -- see enlarge.py)

**38** new overlay window(s), **7497280 ns** total, carved out of already-open best-effort spans on ports at or below utilisation 0.2 -- best-effort stays reachable inside each one (gate mask keeps its BE bits set), so none of this is closed off from BE.

| port | queue | size (ns) |
|---|---|---|
| S1-p0 | Q6 | 161280 |
| S1-p0 | Q7 | 224640 |
| S2-p0 | Q6 | 206080 |
| S2-p0 | Q7 | 212160 |
| S3-p0 | Q6 | 141440 |
| S3-p0 | Q7 | 212160 |
| sw01-p2 | Q6 | 210880 |
| sw01-p2 | Q7 | 226560 |
| sw01-p4 | Q6 | 120320 |
| sw01-p4 | Q7 | 199680 |
| sw02-p2 | Q6 | 230720 |
| sw02-p2 | Q7 | 214720 |
| sw02-p4 | Q6 | 135040 |
| sw02-p4 | Q7 | 214720 |
| sw03-p4 | Q6 | 204160 |
| sw03-p4 | Q7 | 229120 |
| sw03-p5 | Q6 | 133120 |
| sw03-p5 | Q7 | 199680 |
| sw04-p4 | Q6 | 230720 |
| sw04-p4 | Q7 | 206400 |
| sw04-p5 | Q6 | 136000 |
| sw04-p5 | Q7 | 214720 |
| sw05-p4 | Q6 | 166400 |
| sw05-p4 | Q7 | 203520 |
| sw05-p5 | Q6 | 192640 |
| sw05-p5 | Q7 | 227520 |
| sw06-p4 | Q6 | 152640 |
| sw06-p4 | Q7 | 199680 |
| sw06-p5 | Q6 | 230720 |
| sw06-p5 | Q7 | 189760 |
| sw07-p4 | Q6 | 184960 |
| sw07-p4 | Q7 | 237440 |
| sw07-p5 | Q6 | 199680 |
| sw07-p5 | Q7 | 178560 |
| sw08-p4 | Q6 | 222400 |
| sw08-p4 | Q7 | 198080 |
| sw08-p5 | Q6 | 211520 |
| sw08-p5 | Q7 | 237440 |

## Candidate routes (P^cand = routes of the fixed flows above)

| route | PCPs carried | flows |
|---|---|---|
| S1->sw02->sw04->sw06->sw08->S2 | Q6 (1), Q7 (2) | 3 |
| S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | Q7 (1) | 1 |
| S2->sw08->sw06->sw04->sw02->S1 | Q6 (1) | 1 |
| S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 (2) | 2 |
| S3->sw01->sw03->sw05->sw07->sw08->S2 | Q6 (3) | 3 |

## Per-link enlargement accounting

| link | sharing eta | route-safe slack (ns) | link budget (ns) | final slack (ns) | applied (ns) |
|---|---|---|---|---|---|
| S1-p0 | 2 | Q6:24359, Q7:69583 | 93942 | Q6:21216, Q7:69583 | Q6:380800, Q7:319360 |
| S2-p0 | 2 | Q6:145200, Q7:23973 | 169173 | Q6:113135, Q7:23973 | Q6:267200, Q7:445440 |
| sw01-p2 | 2 | Q6:0, Q7:21926 | 21926 | Q7:21926 | Q6:223360, Q7:483840 |
| sw02-p4 | 2 | Q6:20510, Q7:56010 | 76520 | Q6:17891, Q7:56010 | Q6:346240, Q7:310720 |
| sw03-p4 | 2 | Q6:0, Q7:18224 | 18224 | Q7:18224 | Q6:216640, Q7:493120 |
| sw04-p5 | 2 | Q6:17269, Q7:45084 | 62353 | Q6:15087, Q7:45084 | Q6:338880, Q7:312000 |
| sw05-p5 | 2 | Q6:0, Q7:15147 | 15147 | Q7:15147 | Q6:205120, Q7:498240 |
| sw06-p4 | 2 | Q6:14540, Q7:36290 | 50831 | Q6:12724, Q7:36290 | Q6:347200, Q7:298240 |
| sw07-p4 | 2 | Q6:0, Q7:12590 | 12590 | Q7:12590 | Q6:197440, Q7:514880 |
| sw08-p2 | 2 | Q6:28510, Q7:32909 | 61418 | Q6:28510, Q7:13408 | Q6:7680, Q7:12480 |
| sw08-p5 | 2 | Q6:0, Q7:10464 | 10464 | Q7:10464 | Q6:211520, Q7:483200 |
| S3-p0 | 1 | Q6:14600, Q7:0 | 14600 | Q6:14600 | Q6:488000, Q7:224640 |
| sw01-p4 | 1 | Q6:12784, Q7:0 | 12784 | Q6:12784 | Q6:458880, Q7:212160 |
| sw02-p2 | 1 | Q6:30823, Q7:0 | 30823 | Q6:30823 | Q6:547840, Q7:227200 |
| sw03-p5 | 1 | Q6:11193, Q7:0 | 11193 | Q6:11193 | Q6:465600, Q7:212160 |
| sw04-p4 | 1 | Q6:26276, Q7:0 | 26276 | Q6:26276 | Q6:556160, Q7:218880 |
| sw05-p4 | 1 | Q6:9800, Q7:0 | 9800 | Q6:9800 | Q6:492800, Q7:216000 |
| sw06-p5 | 1 | Q6:22400, Q7:0 | 22400 | Q6:22400 | Q6:564480, Q7:202240 |
| sw07-p5 | 1 | Q6:8580, Q7:0 | 8580 | Q6:8580 | Q6:519040, Q7:191040 |
| sw08-p4 | 1 | Q6:19096, Q7:0 | 19096 | Q6:19096 | Q6:564480, Q7:210560 |

Total applied: **13485760 ns** across 20 port(s). Network total slack now banked: **13562240 ns**. GCL_size overflow: 0.

## Per-port GCL entries: before (SMT) vs. after (heuristic-enlarged)

| port | SMT entries | enlarged entries | GCL_size |
|---|---|---|---|
| sw01-p2 | 13 | 21 | 255 |
| sw01-p4 | 15 | 21 | 255 |
| sw02-p2 | 5 | 14 | 255 |
| sw02-p4 | 17 | 22 | 255 |
| sw03-p4 | 13 | 22 | 255 |
| sw03-p5 | 15 | 18 | 255 |
| sw04-p4 | 5 | 14 | 255 |
| sw04-p5 | 17 | 25 | 255 |
| sw05-p4 | 15 | 18 | 255 |
| sw05-p5 | 13 | 23 | 255 |
| sw06-p4 | 17 | 24 | 255 |
| sw06-p5 | 5 | 14 | 255 |
| sw07-p4 | 13 | 23 | 255 |
| sw07-p5 | 15 | 18 | 255 |
| sw08-p2 | 29 | 19 | 255 |
| sw08-p4 | 5 | 12 | 255 |
| sw08-p5 | 13 | 23 | 255 |

## Flows

| flow | route | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|
| s0(id=1 S3->S1) | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | - | - | - | no |
| s1(id=2 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 7 | 0 | 46160 | yes |
| s2(id=3 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 7 | 62400 | 56720 | yes |
| s3(id=4 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | - | - | - | no |
| s4(id=5 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 7 | 62400 | 38160 | yes |
| s5(id=6 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | - | - | - | no |
| s6(id=7 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | - | - | - | no |
| s7(id=8 S3->S1) | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | - | - | - | no |
| s8(id=9 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | 6 | 37440 | 45840 | yes |
| s9(id=10 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 6 | 0 | 45840 | yes |
| s10(id=11 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | - | - | - | no |
| s11(id=12 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 6 | 12480 | 54160 | yes |
| s12(id=13 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | 7 | 87360 | 74000 | yes |
| s13(id=14 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | - | - | - | no |
| s14(id=15 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | - | - | - | no |
| s15(id=16 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 6 | 62400 | 43920 | yes |
| s16(id=17 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 7 | 37440 | 43280 | yes |
| s17(id=18 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | - | - | - | no |
| s18(id=19 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 6 | 37440 | 56080 | yes |
| s19(id=20 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | - | - | - | no |

## Per-hop windows (slack_ns > 0 means this window was enlarged)

| flow | egress port | queue | psi (ns) | delta (ns) |
|---|---|---|---|---|
| s1(id=2 S2->S3) | S2-p0 | Q7 | 0 | 12480 |
| s1(id=2 S2->S3) | sw08-p5 | Q7 | 6720 | 12480 |
| s1(id=2 S2->S3) | sw07-p4 | Q7 | 13440 | 12480 |
| s1(id=2 S2->S3) | sw05-p5 | Q7 | 20160 | 12480 |
| s1(id=2 S2->S3) | sw03-p4 | Q7 | 26880 | 12480 |
| s1(id=2 S2->S3) | sw01-p2 | Q7 | 33600 | 12480 |
| s2(id=3 S1->S2) | S1-p0 | Q7 | 62400 | 12480 |
| s2(id=3 S1->S2) | sw02-p4 | Q7 | 67520 | 12480 |
| s2(id=3 S1->S2) | sw04-p5 | Q7 | 72640 | 12480 |
| s2(id=3 S1->S2) | sw06-p4 | Q7 | 77760 | 12480 |
| s2(id=3 S1->S2) | sw08-p2 | Q7 | 106560 | 12480 |
| s4(id=5 S2->S3) | S2-p0 | Q7 | 62400 | 12480 |
| s4(id=5 S2->S3) | sw08-p5 | Q7 | 67520 | 12480 |
| s4(id=5 S2->S3) | sw07-p4 | Q7 | 72640 | 12480 |
| s4(id=5 S2->S3) | sw05-p5 | Q7 | 77760 | 12480 |
| s4(id=5 S2->S3) | sw03-p4 | Q7 | 82880 | 12480 |
| s4(id=5 S2->S3) | sw01-p2 | Q7 | 88000 | 12480 |
| s8(id=9 S2->S1) | S2-p0 | Q6 | 37440 | 12480 |
| s8(id=9 S2->S1) | sw08-p4 | Q6 | 45760 | 12480 |
| s8(id=9 S2->S1) | sw06-p5 | Q6 | 54080 | 12480 |
| s8(id=9 S2->S1) | sw04-p4 | Q6 | 62400 | 12480 |
| s8(id=9 S2->S1) | sw02-p2 | Q6 | 70720 | 12480 |
| s9(id=10 S1->S2) | S1-p0 | Q6 | 0 | 12480 |
| s9(id=10 S1->S2) | sw02-p4 | Q6 | 8320 | 12480 |
| s9(id=10 S1->S2) | sw04-p5 | Q6 | 16640 | 12480 |
| s9(id=10 S1->S2) | sw06-p4 | Q6 | 24960 | 12480 |
| s9(id=10 S1->S2) | sw08-p2 | Q6 | 33280 | 12480 |
| s11(id=12 S3->S2) | S3-p0 | Q6 | 12480 | 12480 |
| s11(id=12 S3->S2) | sw01-p4 | Q6 | 20800 | 12480 |
| s11(id=12 S3->S2) | sw03-p5 | Q6 | 29120 | 12480 |
| s11(id=12 S3->S2) | sw05-p4 | Q6 | 37440 | 12480 |
| s11(id=12 S3->S2) | sw07-p5 | Q6 | 45760 | 12480 |
| s11(id=12 S3->S2) | sw08-p2 | Q6 | 54080 | 12480 |
| s12(id=13 S1->S3) | S1-p0 | Q7 | 87360 | 12480 |
| s12(id=13 S1->S3) | sw02-p4 | Q7 | 95040 | 12480 |
| s12(id=13 S1->S3) | sw04-p5 | Q7 | 102720 | 12480 |
| s12(id=13 S1->S3) | sw06-p4 | Q7 | 110400 | 12480 |
| s12(id=13 S1->S3) | sw08-p5 | Q7 | 118080 | 12480 |
| s12(id=13 S1->S3) | sw07-p4 | Q7 | 125760 | 12480 |
| s12(id=13 S1->S3) | sw05-p5 | Q7 | 133440 | 12480 |
| s12(id=13 S1->S3) | sw03-p4 | Q7 | 141120 | 12480 |
| s12(id=13 S1->S3) | sw01-p2 | Q7 | 148800 | 12480 |
| s15(id=16 S3->S2) | S3-p0 | Q6 | 62400 | 12480 |
| s15(id=16 S3->S2) | sw01-p4 | Q6 | 68480 | 12480 |
| s15(id=16 S3->S2) | sw03-p5 | Q6 | 74560 | 12480 |
| s15(id=16 S3->S2) | sw05-p4 | Q6 | 80640 | 12480 |
| s15(id=16 S3->S2) | sw07-p5 | Q6 | 87680 | 12480 |
| s15(id=16 S3->S2) | sw08-p2 | Q6 | 93760 | 12480 |
| s16(id=17 S1->S2) | S1-p0 | Q7 | 37440 | 12480 |
| s16(id=17 S1->S2) | sw02-p4 | Q7 | 45120 | 12480 |
| s16(id=17 S1->S2) | sw04-p5 | Q7 | 52800 | 12480 |
| s16(id=17 S1->S2) | sw06-p4 | Q7 | 60480 | 12480 |
| s16(id=17 S1->S2) | sw08-p2 | Q7 | 68160 | 12480 |
| s18(id=19 S3->S2) | S3-p0 | Q6 | 37440 | 12480 |
| s18(id=19 S3->S2) | sw01-p4 | Q6 | 47680 | 12480 |
| s18(id=19 S3->S2) | sw03-p5 | Q6 | 56000 | 12480 |
| s18(id=19 S3->S2) | sw05-p4 | Q6 | 64320 | 12480 |
| s18(id=19 S3->S2) | sw07-p5 | Q6 | 72640 | 12480 |
| s18(id=19 S3->S2) | sw08-p2 | Q6 | 80960 | 12480 |

## Constraint check

- C1-C7, C9: OK
- seed-integrity (no SMT-fixed flow's placement changed): OK

## GCL per egress port

### sw01-p2  (21 entries, util 9.3600 %)

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

### sw01-p4  (21 entries, util 10.9200 %)

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

### sw02-p2  (14 entries, util 3.1200 %)

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

### sw02-p4  (22 entries, util 12.4800 %)

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

### sw03-p4  (22 entries, util 9.3600 %)

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

### sw03-p5  (18 entries, util 10.9200 %)

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

### sw04-p4  (14 entries, util 3.1200 %)

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

### sw04-p5  (25 entries, util 12.4800 %)

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

### sw05-p4  (18 entries, util 10.9200 %)

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

### sw05-p5  (23 entries, util 9.3600 %)

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

### sw06-p4  (24 entries, util 12.4800 %)

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

### sw06-p5  (14 entries, util 3.1200 %)

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

### sw07-p4  (23 entries, util 9.3600 %)

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

### sw07-p5  (18 entries, util 10.9200 %)

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

### sw08-p4  (12 entries, util 3.1200 %)

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

### sw08-p5  (23 entries, util 9.3600 %)

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

