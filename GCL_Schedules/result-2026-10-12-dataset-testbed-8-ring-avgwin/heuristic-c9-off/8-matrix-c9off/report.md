# Heuristic-enlarged GCL schedule (Problem 2: window enlargement)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Time-sensitive PCPs considered: [6, 7]
- Seeded from SMT run: **result/result-2026-10-12-dataset-testbed-8-ring-avgwin/smt-c9-off/8-t3600-c9off-minlat**

## Admission (unchanged by this package -- it only widens windows)

SMT-fixed flows: **10**/20. This package never admits a flow itself; it banks slack for a later admission pass (`prob_3_admit`, Problem 3) to use.

## Opportunistic idle top-up (Step 7 -- see enlarge.py)

Total: **11481600 ns**, drawn from idle capacity on ports at or below utilisation 0.2, independent of any route's deadline-slack budget.

| port | queue | applied (ns) |
|---|---|---|
| S1-p0 | Q6 | 393600 |
| S1-p0 | Q7 | 153920 |
| S2-p0 | Q6 | 563520 |
| S2-p0 | Q7 | 85440 |
| S3-p0 | Q7 | 648000 |
| sw01-p2 | Q6 | 242880 |
| sw01-p2 | Q7 | 295680 |
| sw01-p5 | Q7 | 645440 |
| sw02-p2 | Q6 | 536000 |
| sw02-p4 | Q6 | 687680 |
| sw02-p5 | Q6 | 30720 |
| sw02-p5 | Q7 | 557760 |
| sw03-p4 | Q6 | 539840 |
| sw03-p4 | Q7 | 83840 |
| sw04-p4 | Q6 | 664960 |
| sw04-p5 | Q6 | 672000 |
| sw05-p5 | Q6 | 557120 |
| sw05-p5 | Q7 | 87680 |
| sw06-p4 | Q6 | 656640 |
| sw06-p5 | Q6 | 684160 |
| sw07-p4 | Q6 | 574400 |
| sw07-p4 | Q7 | 90880 |
| sw08-p2 | Q6 | 640640 |
| sw08-p4 | Q6 | 703040 |
| sw08-p5 | Q6 | 591680 |
| sw08-p5 | Q7 | 94080 |

## Opportunistic window creation (Step 8 -- see enlarge.py)

**15** brand-new window(s) opened, **187200 ns** total, on ports at or below utilisation 0.2 whose TT queue had zero windows before this run.

| port | queue | size (ns) |
|---|---|---|
| sw01-p4 | Q6 | 12480 |
| sw01-p4 | Q7 | 12480 |
| sw02-p4 | Q7 | 12480 |
| sw03-p5 | Q6 | 12480 |
| sw03-p5 | Q7 | 12480 |
| sw04-p4 | Q7 | 12480 |
| sw04-p5 | Q7 | 12480 |
| sw05-p4 | Q6 | 12480 |
| sw05-p4 | Q7 | 12480 |
| sw06-p4 | Q7 | 12480 |
| sw06-p5 | Q7 | 12480 |
| sw07-p5 | Q6 | 12480 |
| sw07-p5 | Q7 | 12480 |
| sw08-p2 | Q7 | 12480 |
| sw08-p4 | Q7 | 12480 |

## Best-effort gap equalization (Step 9 -- see enlarge.py)

**7549760 ns** given back from Steps 7/8's growth so each port's leftover non-TAS gaps land close to equal, instead of one gap staying huge while a neighbour is squeezed to the bare 1-tick C10 minimum.

| port | given back (ns) |
|---|---|
| sw05-p5 | 541440 |
| sw07-p4 | 541440 |
| sw08-p5 | 541440 |
| sw03-p4 | 539520 |
| sw02-p4 | 499200 |
| sw04-p5 | 491200 |
| sw06-p4 | 474560 |
| sw08-p2 | 457920 |
| sw02-p5 | 443520 |
| S2-p0 | 418240 |
| sw04-p4 | 387200 |
| sw06-p5 | 387200 |
| sw08-p4 | 387200 |
| sw01-p2 | 324800 |
| S1-p0 | 307520 |
| sw01-p5 | 283200 |
| S3-p0 | 283200 |
| sw02-p2 | 240960 |

## Opportunistic overlay window creation (Step 10 -- see enlarge.py)

**44** new overlay window(s), **11185280 ns** total, carved out of already-open best-effort spans on ports at or below utilisation 0.2 -- best-effort stays reachable inside each one (gate mask keeps its BE bits set), so none of this is closed off from BE.

| port | queue | size (ns) |
|---|---|---|
| S1-p0 | Q6 | 99840 |
| S1-p0 | Q7 | 215040 |
| S2-p0 | Q6 | 206080 |
| S2-p0 | Q7 | 212160 |
| S3-p0 | Q6 | 149760 |
| S3-p0 | Q7 | 135360 |
| sw01-p2 | Q6 | 195520 |
| sw01-p2 | Q7 | 149760 |
| sw01-p4 | Q6 | 374400 |
| sw01-p4 | Q7 | 400640 |
| sw01-p5 | Q6 | 152000 |
| sw01-p5 | Q7 | 135360 |
| sw02-p2 | Q6 | 130560 |
| sw02-p2 | Q7 | 147520 |
| sw02-p4 | Q6 | 299520 |
| sw02-p4 | Q7 | 224640 |
| sw02-p5 | Q6 | 155520 |
| sw02-p5 | Q7 | 258560 |
| sw03-p4 | Q6 | 278400 |
| sw03-p4 | Q7 | 308480 |
| sw03-p5 | Q6 | 374400 |
| sw03-p5 | Q7 | 400640 |
| sw04-p4 | Q6 | 230720 |
| sw04-p4 | Q7 | 225600 |
| sw04-p5 | Q6 | 237120 |
| sw04-p5 | Q7 | 299840 |
| sw05-p4 | Q6 | 374400 |
| sw05-p4 | Q7 | 400640 |
| sw05-p5 | Q6 | 318720 |
| sw05-p5 | Q7 | 260480 |
| sw06-p4 | Q6 | 237120 |
| sw06-p4 | Q7 | 312000 |
| sw06-p5 | Q6 | 230720 |
| sw06-p5 | Q7 | 215040 |
| sw07-p4 | Q6 | 302080 |
| sw07-p4 | Q7 | 268480 |
| sw07-p5 | Q6 | 374400 |
| sw07-p5 | Q7 | 400640 |
| sw08-p2 | Q6 | 220800 |
| sw08-p2 | Q7 | 313280 |
| sw08-p4 | Q6 | 230720 |
| sw08-p4 | Q7 | 189440 |
| sw08-p5 | Q6 | 287040 |
| sw08-p5 | Q7 | 251840 |

## Candidate routes (P^cand = routes of the fixed flows above)

| route | PCPs carried | flows |
|---|---|---|
| S1->sw02->sw01->S3 | Q6 (1), Q7 (2) | 3 |
| S1->sw02->sw04->sw06->sw08->S2 | Q6 (1) | 1 |
| S2->sw08->sw06->sw04->sw02->S1 | Q6 (1) | 1 |
| S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 (1), Q7 (1) | 2 |
| S3->sw01->sw02->S1 | Q6 (1), Q7 (2) | 3 |

## Per-link enlargement accounting

| link | sharing eta | route-safe slack (ns) | link budget (ns) | final slack (ns) | applied (ns) |
|---|---|---|---|---|---|
| S1-p0 | 2 | Q6:56745, Q7:52882 | 109627 | Q6:56745, Q7:46234 | Q6:360000, Q7:297600 |
| S2-p0 | 2 | Q6:24102, Q7:82045 | 106148 | Q6:24102, Q7:39835 | Q6:464320, Q7:248320 |
| sw01-p2 | 2 | Q6:24718, Q7:43428 | 68146 | Q6:24718, Q7:41545 | Q6:350080, Q7:274880 |
| sw02-p2 | 2 | Q6:92845, Q7:161704 | 254549 | Q6:92845, Q7:125969 | Q6:556480, Q7:147520 |
| S3-p0 | 1 | Q6:60927, Q7:52292 | 113219 | Q6:49497, Q7:52292 | Q6:149760, Q7:577280 |
| sw01-p5 | 1 | Q6:46722, Q7:38084 | 84805 | Q6:38154, Q7:38084 | Q6:152000, Q7:560640 |
| sw02-p4 | 1 | Q6:8507, Q7:0 | 8507 | Q6:8507 | Q6:496320, Q7:237120 |
| sw02-p5 | 1 | Q6:122125, Q7:13200 | 135325 | Q6:82090, Q7:13200 | Q6:179200, Q7:474880 |
| sw03-p4 | 1 | Q6:6378, Q7:54413 | 60791 | Q6:6378, Q7:41387 | Q6:407680, Q7:310720 |
| sw04-p4 | 1 | Q6:22440, Q7:0 | 22440 | Q6:22440 | Q6:530880, Q7:238080 |
| sw04-p5 | 1 | Q6:7379, Q7:0 | 7379 | Q6:7379 | Q6:425280, Q7:312320 |
| sw05-p5 | 1 | Q6:5644, Q7:49297 | 54941 | Q6:5644, Q7:37684 | Q6:462720, Q7:262720 |
| sw06-p4 | 1 | Q6:6400, Q7:0 | 6400 | Q6:6400 | Q6:425280, Q7:324480 |
| sw06-p5 | 1 | Q6:19915, Q7:0 | 19915 | Q6:19915 | Q6:547520, Q7:227520 |
| sw07-p4 | 1 | Q6:4994, Q7:44663 | 49657 | Q6:4994, Q7:34310 | Q6:462720, Q7:270720 |
| sw08-p2 | 1 | Q6:5551, Q7:0 | 5551 | Q6:5551 | Q6:408960, Q7:325760 |
| sw08-p4 | 1 | Q6:17675, Q7:0 | 17675 | Q6:17675 | Q6:564160, Q7:201920 |
| sw08-p5 | 1 | Q6:4420, Q7:40464 | 44883 | Q6:4420, Q7:31236 | Q6:464320, Q7:254080 |

Total applied: **16154240 ns** across 22 port(s). Network total slack now banked: **16154240 ns**. GCL_size overflow: 0.

## Per-port GCL entries: before (SMT) vs. after (heuristic-enlarged)

| port | SMT entries | enlarged entries | GCL_size |
|---|---|---|---|
| sw01-p2 | 25 | 28 | 255 |
| sw01-p4 | 1 | 18 | 255 |
| sw01-p5 | 11 | 15 | 255 |
| sw02-p2 | 15 | 18 | 255 |
| sw02-p4 | 9 | 22 | 255 |
| sw02-p5 | 15 | 24 | 255 |
| sw03-p4 | 11 | 24 | 255 |
| sw03-p5 | 1 | 18 | 255 |
| sw04-p4 | 5 | 14 | 255 |
| sw04-p5 | 9 | 22 | 255 |
| sw05-p4 | 1 | 18 | 255 |
| sw05-p5 | 11 | 20 | 255 |
| sw06-p4 | 9 | 19 | 255 |
| sw06-p5 | 5 | 14 | 255 |
| sw07-p4 | 11 | 20 | 255 |
| sw07-p5 | 1 | 18 | 255 |
| sw08-p2 | 9 | 22 | 255 |
| sw08-p4 | 5 | 14 | 255 |
| sw08-p5 | 11 | 23 | 255 |

## Flows

| flow | route | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|
| s0(id=1 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | - | - | - | no |
| s1(id=2 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | 6 | 37440 | 83600 | yes |
| s2(id=3 S3->S1) | S3->sw01->sw02->S1 | - | - | - | no |
| s3(id=4 S1->S3) | S1->sw02->sw01->S3 | - | - | - | no |
| s4(id=5 S1->S3) | S1->sw02->sw01->S3 | 6 | 87360 | 45840 | yes |
| s5(id=6 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 6 | 0 | 95760 | yes |
| s6(id=7 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | - | - | - | no |
| s7(id=8 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | - | - | - | no |
| s8(id=9 S3->S1) | S3->sw01->sw02->S1 | 6 | 12480 | 45840 | yes |
| s9(id=10 S1->S3) | S1->sw02->sw01->S3 | 7 | 12480 | 45840 | yes |
| s10(id=11 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | - | - | - | no |
| s11(id=12 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 7 | 62400 | 95760 | yes |
| s12(id=13 S3->S1) | S3->sw01->sw02->S1 | 7 | 62400 | 45840 | yes |
| s13(id=14 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | - | - | - | no |
| s14(id=15 S3->S1) | S3->sw01->sw02->S1 | - | - | - | no |
| s15(id=16 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | - | - | - | no |
| s16(id=17 S1->S3) | S1->sw02->sw01->S3 | - | - | - | no |
| s17(id=18 S3->S1) | S3->sw01->sw02->S1 | 7 | 37440 | 45840 | yes |
| s18(id=19 S1->S3) | S1->sw02->sw01->S3 | 7 | 62400 | 46160 | yes |
| s19(id=20 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 6 | 37440 | 79120 | yes |

## Per-hop windows (slack_ns > 0 means this window was enlarged)

| flow | egress port | queue | psi (ns) | delta (ns) |
|---|---|---|---|---|
| s1(id=2 S2->S1) | S2-p0 | Q6 | 37440 | 12480 |
| s1(id=2 S2->S1) | sw08-p4 | Q6 | 54400 | 12480 |
| s1(id=2 S2->S1) | sw06-p5 | Q6 | 71040 | 12480 |
| s1(id=2 S2->S1) | sw04-p4 | Q6 | 87680 | 12480 |
| s1(id=2 S2->S1) | sw02-p2 | Q6 | 108480 | 12480 |
| s4(id=5 S1->S3) | S1-p0 | Q6 | 87360 | 12480 |
| s4(id=5 S1->S3) | sw02-p5 | Q6 | 104000 | 12480 |
| s4(id=5 S1->S3) | sw01-p2 | Q6 | 120640 | 12480 |
| s5(id=6 S2->S3) | S2-p0 | Q6 | 0 | 12480 |
| s5(id=6 S2->S3) | sw08-p5 | Q6 | 16640 | 12480 |
| s5(id=6 S2->S3) | sw07-p4 | Q6 | 33280 | 12480 |
| s5(id=6 S2->S3) | sw05-p5 | Q6 | 49920 | 12480 |
| s5(id=6 S2->S3) | sw03-p4 | Q6 | 66560 | 12480 |
| s5(id=6 S2->S3) | sw01-p2 | Q6 | 83200 | 12480 |
| s8(id=9 S3->S1) | S3-p0 | Q6 | 12480 | 12480 |
| s8(id=9 S3->S1) | sw01-p5 | Q6 | 29120 | 12480 |
| s8(id=9 S3->S1) | sw02-p2 | Q6 | 45760 | 12480 |
| s9(id=10 S1->S3) | S1-p0 | Q7 | 12480 | 12480 |
| s9(id=10 S1->S3) | sw02-p5 | Q7 | 29120 | 12480 |
| s9(id=10 S1->S3) | sw01-p2 | Q7 | 45760 | 12480 |
| s11(id=12 S2->S3) | S2-p0 | Q7 | 62400 | 12480 |
| s11(id=12 S2->S3) | sw08-p5 | Q7 | 79040 | 12480 |
| s11(id=12 S2->S3) | sw07-p4 | Q7 | 95680 | 12480 |
| s11(id=12 S2->S3) | sw05-p5 | Q7 | 112320 | 12480 |
| s11(id=12 S2->S3) | sw03-p4 | Q7 | 128960 | 12480 |
| s11(id=12 S2->S3) | sw01-p2 | Q7 | 145600 | 12480 |
| s12(id=13 S3->S1) | S3-p0 | Q7 | 62400 | 12480 |
| s12(id=13 S3->S1) | sw01-p5 | Q7 | 79040 | 12480 |
| s12(id=13 S3->S1) | sw02-p2 | Q7 | 95680 | 12480 |
| s17(id=18 S3->S1) | S3-p0 | Q7 | 37440 | 12480 |
| s17(id=18 S3->S1) | sw01-p5 | Q7 | 54080 | 12480 |
| s17(id=18 S3->S1) | sw02-p2 | Q7 | 70720 | 12480 |
| s18(id=19 S1->S3) | S1-p0 | Q7 | 62400 | 12480 |
| s18(id=19 S1->S3) | sw02-p5 | Q7 | 79360 | 12480 |
| s18(id=19 S1->S3) | sw01-p2 | Q7 | 96000 | 12480 |
| s19(id=20 S1->S2) | S1-p0 | Q6 | 37440 | 12480 |
| s19(id=20 S1->S2) | sw02-p4 | Q6 | 54080 | 12480 |
| s19(id=20 S1->S2) | sw04-p5 | Q6 | 70720 | 12480 |
| s19(id=20 S1->S2) | sw06-p4 | Q6 | 87360 | 12480 |
| s19(id=20 S1->S2) | sw08-p2 | Q6 | 104000 | 12480 |

## Constraint check

- C1-C7, C9: OK
- seed-integrity (no SMT-fixed flow's placement changed): OK

## GCL per egress port

### sw01-p2  (28 entries, util 18.7200 %)

```
sgs 45760 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 50240 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 45760 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 112640 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 45760 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 99840 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 45760 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 66880 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p4  (18 entries, util 0.0000 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p5  (15 entries, util 7.8000 %)

```
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 227200 0x80 # 10000000   Q7
sgs 43840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 223040 0x80 # 10000000   Q7
sgs 23040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (18 entries, util 10.9200 %)

```
sgs 45760 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 248320 0x40 # 01000000   Q6
sgs 43200 0xBF # 10111111   Q7
sgs 45760 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 16960 0xBF # 10111111   Q7
sgs 8320 0x3F # 00111111   BE
sgs 202560 0x40 # 01000000   Q6
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p4  (22 entries, util 6.2400 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 4160 0x3F # 00111111   BE
sgs 75200 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 4160 0x3F # 00111111   BE
sgs 75200 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 4160 0x3F # 00111111   BE
sgs 75200 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 4160 0x3F # 00111111   BE
sgs 21120 0x40 # 01000000   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p5  (24 entries, util 10.9200 %)

```
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 8320 0x3F # 00111111   BE
sgs 29440 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12160 0x3F # 00111111   BE
sgs 36160 0x40 # 01000000   Q6
sgs 9920 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 111040 0x80 # 10000000   Q7
sgs 9920 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 8320 0x3F # 00111111   BE
sgs 29440 0xBF # 10111111   Q7
sgs 60800 0x80 # 10000000   Q7
sgs 9920 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 81920 0x80 # 10000000   Q7
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (24 entries, util 7.8000 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 21120 0xBF # 10111111   Q7
sgs 28800 0x7F # 01111111   Q6
sgs 14720 0x80 # 10000000   Q7
sgs 6400 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 77120 0x40 # 01000000   Q6
sgs 6400 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 77120 0x40 # 01000000   Q6
sgs 6400 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 21120 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p5  (18 entries, util 0.0000 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p4  (14 entries, util 3.1200 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 37760 0xBF # 10111111   Q7
sgs 206400 0x40 # 01000000   Q6
sgs 6080 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 37760 0xBF # 10111111   Q7
sgs 118720 0x40 # 01000000   Q6
sgs 43520 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (22 entries, util 6.2400 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 20800 0xBF # 10111111   Q7
sgs 75200 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 20800 0xBF # 10111111   Q7
sgs 75200 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 20800 0xBF # 10111111   Q7
sgs 75200 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 20800 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 16960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (18 entries, util 0.0000 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p5  (20 entries, util 7.8000 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 37760 0xBF # 10111111   Q7
sgs 12160 0x3F # 00111111   BE
sgs 14720 0x80 # 10000000   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 77120 0x40 # 01000000   Q6
sgs 23040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 77120 0x40 # 01000000   Q6
sgs 23040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 27200 0x40 # 01000000   Q6
sgs 23040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p4  (19 entries, util 6.2400 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 37440 0xBF # 10111111   Q7
sgs 75200 0x40 # 01000000   Q6
sgs 37440 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 37440 0xBF # 10111111   Q7
sgs 75200 0x40 # 01000000   Q6
sgs 37440 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 37440 0xBF # 10111111   Q7
sgs 75200 0x40 # 01000000   Q6
sgs 37440 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 37440 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (14 entries, util 3.1200 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 21120 0xBF # 10111111   Q7
sgs 206400 0x40 # 01000000   Q6
sgs 22720 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 21120 0xBF # 10111111   Q7
sgs 135360 0x40 # 01000000   Q6
sgs 43520 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (20 entries, util 7.8000 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 45760 0xBF # 10111111   Q7
sgs 14720 0x80 # 10000000   Q7
sgs 39680 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 77120 0x40 # 01000000   Q6
sgs 39680 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 77120 0x40 # 01000000   Q6
sgs 39680 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 43840 0x40 # 01000000   Q6
sgs 23040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p5  (18 entries, util 0.0000 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p2  (22 entries, util 6.2400 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 3840 0x3F # 00111111   BE
sgs 75200 0x40 # 01000000   Q6
sgs 20800 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 3840 0x3F # 00111111   BE
sgs 75200 0x40 # 01000000   Q6
sgs 20800 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 3840 0x3F # 00111111   BE
sgs 75200 0x40 # 01000000   Q6
sgs 20800 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 3840 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 33600 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p4  (14 entries, util 3.1200 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 4480 0x3F # 00111111   BE
sgs 206400 0x40 # 01000000   Q6
sgs 39360 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 4480 0x3F # 00111111   BE
sgs 152000 0x40 # 01000000   Q6
sgs 43520 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (23 entries, util 7.8000 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 14720 0x80 # 10000000   Q7
sgs 6400 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 77120 0x40 # 01000000   Q6
sgs 6400 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 77120 0x40 # 01000000   Q6
sgs 6400 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 60480 0x40 # 01000000   Q6
sgs 23040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

