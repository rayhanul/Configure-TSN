# Heuristic-enlarged GCL schedule (Problem 2: window enlargement)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Time-sensitive PCPs considered: [6, 7]
- Seeded from SMT run: **result/result-2026-10-13-dataset-testbed-13-tree-avgwin/smt-c9-on/13-fair-retimed-c9on**

## Admission (unchanged by this package -- it only widens windows)

SMT-fixed flows: **11**/11. This package never admits a flow itself; it banks slack for a later admission pass (`prob_3_admit`, Problem 3) to use.

## Opportunistic idle top-up (Step 7 -- see enlarge.py)

Total: **12348800 ns**, drawn from idle capacity on ports at or below utilisation 0.2, independent of any route's deadline-slack budget.

| port | queue | applied (ns) |
|---|---|---|
| S1-p0 | Q7 | 680320 |
| S3-p0 | Q6 | 571840 |
| S3-p0 | Q7 | 81280 |
| sw01-p2 | Q6 | 584640 |
| sw01-p4 | Q6 | 566080 |
| sw01-p4 | Q7 | 85440 |
| sw02-p2 | Q7 | 683520 |
| sw02-p4 | Q7 | 680640 |
| sw03-p4 | Q6 | 592320 |
| sw03-p5 | Q6 | 559680 |
| sw03-p5 | Q7 | 89280 |
| sw04-p4 | Q7 | 692480 |
| sw04-p5 | Q7 | 679680 |
| sw05-p4 | Q6 | 552960 |
| sw05-p4 | Q7 | 92800 |
| sw05-p5 | Q6 | 599680 |
| sw05-p5 | Q7 | 1600 |
| sw06-p4 | Q7 | 677760 |
| sw06-p5 | Q7 | 701120 |
| sw07-p4 | Q6 | 606080 |
| sw07-p4 | Q7 | 6720 |
| sw07-p5 | Q6 | 545920 |
| sw07-p5 | Q7 | 95680 |
| sw08-p2 | Q6 | 472640 |
| sw08-p2 | Q7 | 116800 |
| sw08-p4 | Q7 | 709440 |
| sw08-p5 | Q6 | 612480 |
| sw08-p5 | Q7 | 9920 |

## Opportunistic window creation (Step 8 -- see enlarge.py)

**4** brand-new window(s) opened, **49920 ns** total, on ports at or below utilisation 0.2 whose TT queue had zero windows before this run.

| port | queue | size (ns) |
|---|---|---|
| sw02-p2 | Q6 | 12480 |
| sw04-p4 | Q6 | 12480 |
| sw06-p4 | Q6 | 12480 |
| sw06-p5 | Q6 | 12480 |

## Best-effort gap equalization (Step 9 -- see enlarge.py)

**7287680 ns** given back from Steps 7/8's growth so each port's leftover non-TAS gaps land close to equal, instead of one gap staying huge while a neighbour is squeezed to the bare 1-tick C10 minimum.

| port | given back (ns) |
|---|---|
| sw08-p4 | 491520 |
| sw02-p2 | 449920 |
| sw04-p4 | 446720 |
| sw06-p5 | 443520 |
| S3-p0 | 418240 |
| sw01-p4 | 416000 |
| sw03-p5 | 413760 |
| sw05-p4 | 411520 |
| sw07-p5 | 409280 |
| sw04-p5 | 396480 |
| sw02-p4 | 395840 |
| S1-p0 | 393280 |
| sw06-p4 | 357440 |
| sw08-p5 | 297600 |
| sw07-p4 | 297280 |
| sw05-p5 | 296960 |
| sw03-p4 | 296640 |
| sw01-p2 | 296320 |
| sw08-p2 | 290560 |
| S2-p0 | 68800 |

## Opportunistic overlay window creation (Step 10 -- see enlarge.py)

**38** new overlay window(s), **7041600 ns** total, carved out of already-open best-effort spans on ports at or below utilisation 0.2 -- best-effort stays reachable inside each one (gate mask keeps its BE bits set), so none of this is closed off from BE.

| port | queue | size (ns) |
|---|---|---|
| S1-p0 | Q6 | 193600 |
| S1-p0 | Q7 | 199680 |
| S3-p0 | Q6 | 206080 |
| S3-p0 | Q7 | 212160 |
| sw01-p2 | Q6 | 199680 |
| sw01-p2 | Q7 | 87040 |
| sw01-p4 | Q6 | 176640 |
| sw01-p4 | Q7 | 214400 |
| sw02-p2 | Q6 | 176960 |
| sw02-p2 | Q7 | 266240 |
| sw02-p4 | Q6 | 166080 |
| sw02-p4 | Q7 | 199680 |
| sw03-p4 | Q6 | 197120 |
| sw03-p4 | Q7 | 83840 |
| sw03-p5 | Q6 | 213760 |
| sw03-p5 | Q7 | 216640 |
| sw04-p4 | Q6 | 197120 |
| sw04-p4 | Q7 | 249600 |
| sw04-p5 | Q6 | 151040 |
| sw04-p5 | Q7 | 199680 |
| sw05-p4 | Q6 | 206080 |
| sw05-p4 | Q7 | 218880 |
| sw05-p5 | Q6 | 172800 |
| sw05-p5 | Q7 | 149440 |
| sw06-p4 | Q6 | 118400 |
| sw06-p4 | Q7 | 199680 |
| sw06-p5 | Q6 | 210560 |
| sw06-p5 | Q7 | 232960 |
| sw07-p4 | Q6 | 148480 |
| sw07-p4 | Q7 | 164800 |
| sw07-p5 | Q6 | 172160 |
| sw07-p5 | Q7 | 221120 |
| sw08-p2 | Q6 | 97280 |
| sw08-p2 | Q7 | 189440 |
| sw08-p4 | Q6 | 251520 |
| sw08-p4 | Q7 | 199680 |
| sw08-p5 | Q6 | 124160 |
| sw08-p5 | Q7 | 157120 |

## Candidate routes (P^cand = routes of the fixed flows above)

| route | PCPs carried | flows |
|---|---|---|
| S1->sw02->sw04->sw06->sw08->S2 | Q7 (1) | 1 |
| S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | Q7 (2) | 2 |
| S2->sw08->sw06->sw04->sw02->S1 | Q7 (2) | 2 |
| S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 (3) | 3 |
| S3->sw01->sw03->sw05->sw07->sw08->S2 | Q6 (2), Q7 (1) | 3 |

## Per-link enlargement accounting

| link | sharing eta | route-safe slack (ns) | link budget (ns) | final slack (ns) | applied (ns) |
|---|---|---|---|---|---|
| S1-p0 | 2 | Q6:0, Q7:32546 | 32546 | Q7:32546 | Q6:193600, Q7:519040 |
| S2-p0 | 2 | Q6:26807, Q7:63179 | 89987 | Q6:26807, Q7:56452 | Q6:14080 |
| sw01-p2 | 2 | Q6:21600, Q7:30540 | 52141 | Q6:21600, Q7:24827 | Q6:523200, Q7:87040 |
| sw02-p4 | 2 | Q6:0, Q7:26052 | 26052 | Q7:26052 | Q6:166080, Q7:510400 |
| sw03-p4 | 2 | Q6:18018, Q7:24651 | 42668 | Q6:18018, Q7:19967 | Q6:526400, Q7:83840 |
| sw04-p5 | 2 | Q6:0, Q7:20854 | 20854 | Q7:20854 | Q6:151040, Q7:503680 |
| sw05-p5 | 2 | Q6:15029, Q7:19915 | 34944 | Q6:15029, Q7:16074 | Q6:507840, Q7:149440 |
| sw06-p4 | 2 | Q6:0, Q7:16693 | 16693 | Q7:16693 | Q6:130880, Q7:536640 |
| sw07-p4 | 2 | Q6:12537, Q7:16105 | 28642 | Q6:12537, Q7:12955 | Q6:489280, Q7:164800 |
| sw08-p2 | 2 | Q6:38731, Q7:13524 | 52255 | Q6:38731, Q7:10524 | Q6:392320, Q7:242240 |
| sw08-p5 | 2 | Q6:10457, Q7:14429 | 24886 | Q6:10457, Q7:11698 | Q6:470720, Q7:157120 |
| S3-p0 | 1 | Q6:15733, Q7:79961 | 95694 | Q6:15733, Q7:43886 | Q6:464320, Q7:248320 |
| sw01-p4 | 1 | Q6:13422, Q7:71230 | 84652 | Q6:13422, Q7:39732 | Q6:428800, Q7:250560 |
| sw02-p2 | 1 | Q6:0, Q7:14766 | 14766 | Q7:14766 | Q6:189440, Q7:514560 |
| sw03-p5 | 1 | Q6:11450, Q7:63453 | 74903 | Q6:11450, Q7:35964 | Q6:459840, Q7:252800 |
| sw04-p4 | 1 | Q6:0, Q7:12527 | 12527 | Q7:12527 | Q6:209600, Q7:507840 |
| sw05-p4 | 1 | Q6:9768, Q7:56524 | 66293 | Q6:9768, Q7:32546 | Q6:446080, Q7:255040 |
| sw06-p5 | 1 | Q6:0, Q7:10627 | 10627 | Q7:10627 | Q6:223040, Q7:501120 |
| sw07-p5 | 1 | Q6:8334, Q7:50353 | 58686 | Q6:8334, Q7:29446 | Q6:406080, Q7:257280 |
| sw08-p4 | 1 | Q6:0, Q7:9016 | 9016 | Q7:9016 | Q6:251520, Q7:426560 |

Total applied: **12812480 ns** across 20 port(s). Network total slack now banked: **12869120 ns**. GCL_size overflow: 0.

## Per-port GCL entries: before (SMT) vs. after (heuristic-enlarged)

| port | SMT entries | enlarged entries | GCL_size |
|---|---|---|---|
| sw01-p2 | 21 | 25 | 255 |
| sw01-p4 | 15 | 22 | 255 |
| sw02-p2 | 13 | 23 | 255 |
| sw02-p4 | 15 | 20 | 255 |
| sw03-p4 | 21 | 21 | 255 |
| sw03-p5 | 15 | 22 | 255 |
| sw04-p4 | 13 | 23 | 255 |
| sw04-p5 | 15 | 20 | 255 |
| sw05-p4 | 15 | 24 | 255 |
| sw05-p5 | 21 | 21 | 255 |
| sw06-p4 | 15 | 21 | 255 |
| sw06-p5 | 13 | 23 | 255 |
| sw07-p4 | 21 | 23 | 255 |
| sw07-p5 | 15 | 22 | 255 |
| sw08-p2 | 23 | 28 | 255 |
| sw08-p4 | 13 | 23 | 255 |
| sw08-p5 | 21 | 21 | 255 |

## Flows

| flow | route | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|
| s0(id=1 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | - | - | - | no |
| s1(id=2 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | - | - | - | no |
| s2(id=3 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | 7 | 24960 | 74000 | yes |
| s3(id=4 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | - | - | - | no |
| s4(id=5 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 6 | 0 | 54160 | yes |
| s5(id=6 S3->S1) | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | - | - | - | no |
| s6(id=7 S3->S1) | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | - | - | - | no |
| s7(id=8 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 7 | 62400 | 54160 | yes |
| s8(id=9 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 6 | 37440 | 42960 | yes |
| s9(id=10 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | 7 | 0 | 39440 | yes |
| s10(id=11 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | - | - | - | no |
| s11(id=12 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | - | - | - | no |
| s12(id=13 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | 7 | 49920 | 45840 | yes |
| s13(id=14 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 7 | 0 | 36880 | yes |
| s14(id=15 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | 7 | 49920 | 61840 | yes |
| s15(id=16 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | - | - | - | no |
| s16(id=17 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 6 | 99840 | 38160 | yes |
| s17(id=18 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | - | - | - | no |
| s18(id=19 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 6 | 24960 | 42960 | yes |
| s19(id=20 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 6 | 74880 | 49680 | yes |

## Per-hop windows (slack_ns > 0 means this window was enlarged)

| flow | egress port | queue | psi (ns) | delta (ns) |
|---|---|---|---|---|
| s2(id=3 S1->S3) | S1-p0 | Q7 | 24960 | 12480 |
| s2(id=3 S1->S3) | sw02-p4 | Q7 | 32640 | 12480 |
| s2(id=3 S1->S3) | sw04-p5 | Q7 | 40320 | 12480 |
| s2(id=3 S1->S3) | sw06-p4 | Q7 | 48000 | 12480 |
| s2(id=3 S1->S3) | sw08-p5 | Q7 | 55680 | 12480 |
| s2(id=3 S1->S3) | sw07-p4 | Q7 | 63360 | 12480 |
| s2(id=3 S1->S3) | sw05-p5 | Q7 | 71040 | 12480 |
| s2(id=3 S1->S3) | sw03-p4 | Q7 | 78720 | 12480 |
| s2(id=3 S1->S3) | sw01-p2 | Q7 | 86400 | 12480 |
| s4(id=5 S3->S2) | S3-p0 | Q6 | 0 | 12480 |
| s4(id=5 S3->S2) | sw01-p4 | Q6 | 8320 | 12480 |
| s4(id=5 S3->S2) | sw03-p5 | Q6 | 16640 | 12480 |
| s4(id=5 S3->S2) | sw05-p4 | Q6 | 24960 | 12480 |
| s4(id=5 S3->S2) | sw07-p5 | Q6 | 33280 | 12480 |
| s4(id=5 S3->S2) | sw08-p2 | Q6 | 41600 | 12480 |
| s7(id=8 S3->S2) | S3-p0 | Q7 | 62400 | 12480 |
| s7(id=8 S3->S2) | sw01-p4 | Q7 | 70720 | 12480 |
| s7(id=8 S3->S2) | sw03-p5 | Q7 | 79040 | 12480 |
| s7(id=8 S3->S2) | sw05-p4 | Q7 | 87360 | 12480 |
| s7(id=8 S3->S2) | sw07-p5 | Q7 | 95680 | 12480 |
| s7(id=8 S3->S2) | sw08-p2 | Q7 | 104000 | 12480 |
| s8(id=9 S3->S2) | S3-p0 | Q6 | 37440 | 12480 |
| s8(id=9 S3->S2) | sw01-p4 | Q6 | 43520 | 12480 |
| s8(id=9 S3->S2) | sw03-p5 | Q6 | 49600 | 12480 |
| s8(id=9 S3->S2) | sw05-p4 | Q6 | 55680 | 12480 |
| s8(id=9 S3->S2) | sw07-p5 | Q6 | 61760 | 12480 |
| s8(id=9 S3->S2) | sw08-p2 | Q6 | 67840 | 12480 |
| s9(id=10 S2->S1) | S2-p0 | Q7 | 0 | 12480 |
| s9(id=10 S2->S1) | sw08-p4 | Q7 | 6720 | 12480 |
| s9(id=10 S2->S1) | sw06-p5 | Q7 | 13440 | 12480 |
| s9(id=10 S2->S1) | sw04-p4 | Q7 | 20160 | 12480 |
| s9(id=10 S2->S1) | sw02-p2 | Q7 | 26880 | 12480 |
| s12(id=13 S2->S1) | S2-p0 | Q7 | 49920 | 12480 |
| s12(id=13 S2->S1) | sw08-p4 | Q7 | 58240 | 12480 |
| s12(id=13 S2->S1) | sw06-p5 | Q7 | 66560 | 12480 |
| s12(id=13 S2->S1) | sw04-p4 | Q7 | 74880 | 12480 |
| s12(id=13 S2->S1) | sw02-p2 | Q7 | 83200 | 12480 |
| s13(id=14 S1->S2) | S1-p0 | Q7 | 0 | 12480 |
| s13(id=14 S1->S2) | sw02-p4 | Q7 | 6080 | 12480 |
| s13(id=14 S1->S2) | sw04-p5 | Q7 | 12160 | 12480 |
| s13(id=14 S1->S2) | sw06-p4 | Q7 | 18240 | 12480 |
| s13(id=14 S1->S2) | sw08-p2 | Q7 | 24320 | 12480 |
| s14(id=15 S1->S3) | S1-p0 | Q7 | 49920 | 12480 |
| s14(id=15 S1->S3) | sw02-p4 | Q7 | 56960 | 12480 |
| s14(id=15 S1->S3) | sw04-p5 | Q7 | 62080 | 12480 |
| s14(id=15 S1->S3) | sw06-p4 | Q7 | 67200 | 12480 |
| s14(id=15 S1->S3) | sw08-p5 | Q7 | 72320 | 12480 |
| s14(id=15 S1->S3) | sw07-p4 | Q7 | 78720 | 12480 |
| s14(id=15 S1->S3) | sw05-p5 | Q7 | 83840 | 12480 |
| s14(id=15 S1->S3) | sw03-p4 | Q7 | 91520 | 12480 |
| s14(id=15 S1->S3) | sw01-p2 | Q7 | 99200 | 12480 |
| s16(id=17 S2->S3) | S2-p0 | Q6 | 99840 | 12480 |
| s16(id=17 S2->S3) | sw08-p5 | Q6 | 104960 | 12480 |
| s16(id=17 S2->S3) | sw07-p4 | Q6 | 110080 | 12480 |
| s16(id=17 S2->S3) | sw05-p5 | Q6 | 115200 | 12480 |
| s16(id=17 S2->S3) | sw03-p4 | Q6 | 120320 | 12480 |
| s16(id=17 S2->S3) | sw01-p2 | Q6 | 125440 | 12480 |
| s18(id=19 S2->S3) | S2-p0 | Q6 | 24960 | 12480 |
| s18(id=19 S2->S3) | sw08-p5 | Q6 | 31040 | 12480 |
| s18(id=19 S2->S3) | sw07-p4 | Q6 | 37120 | 12480 |
| s18(id=19 S2->S3) | sw05-p5 | Q6 | 43200 | 12480 |
| s18(id=19 S2->S3) | sw03-p4 | Q6 | 49280 | 12480 |
| s18(id=19 S2->S3) | sw01-p2 | Q6 | 55360 | 12480 |
| s19(id=20 S2->S3) | S2-p0 | Q6 | 74880 | 12480 |
| s19(id=20 S2->S3) | sw08-p5 | Q6 | 85120 | 12480 |
| s19(id=20 S2->S3) | sw07-p4 | Q6 | 91840 | 12480 |
| s19(id=20 S2->S3) | sw05-p5 | Q6 | 98560 | 12480 |
| s19(id=20 S2->S3) | sw03-p4 | Q6 | 105280 | 12480 |
| s19(id=20 S2->S3) | sw01-p2 | Q6 | 112000 | 12480 |

## Constraint check

- C1-C7, C9: OK
- seed-integrity (no SMT-fixed flow's placement changed): OK

## GCL per egress port

### sw01-p2  (25 entries, util 15.6000 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 5440 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 18560 0xBF # 10111111   Q7
sgs 25280 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 82240 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 5440 0x3F # 00111111   BE
sgs 138880 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 5440 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 18560 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0x3F # 00111111   BE
sgs 82240 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 5440 0x3F # 00111111   BE
sgs 83520 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p4  (22 entries, util 10.9200 %)

```
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 22720 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 14720 0xBF # 10111111   Q7
sgs 48640 0x80 # 10000000   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 8320 0x3F # 00111111   BE
sgs 111040 0x40 # 01000000   Q6
sgs 30720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 22720 0x7F # 01111111   Q6
sgs 75840 0x40 # 01000000   Q6
sgs 30720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 8320 0x3F # 00111111   BE
sgs 102720 0x40 # 01000000   Q6
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (23 entries, util 9.3600 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 10560 0x3F # 00111111   BE
sgs 33280 0xBF # 10111111   Q7
sgs 53120 0x80 # 10000000   Q7
sgs 13760 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 26880 0x7F # 01111111   Q6
sgs 109440 0x80 # 10000000   Q7
sgs 13760 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 26880 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 10560 0x3F # 00111111   BE
sgs 33280 0xBF # 10111111   Q7
sgs 53120 0x80 # 10000000   Q7
sgs 13760 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 26880 0x7F # 01111111   Q6
sgs 82560 0x80 # 10000000   Q7
sgs 40640 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p4  (20 entries, util 10.9200 %)

```
sgs 6080 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 14080 0x7F # 01111111   Q6
sgs 84480 0x80 # 10000000   Q7
sgs 32960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 6080 0x3F # 00111111   BE
sgs 111040 0x80 # 10000000   Q7
sgs 32960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 6080 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 14080 0x7F # 01111111   Q6
sgs 84480 0x80 # 10000000   Q7
sgs 32960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 6080 0x3F # 00111111   BE
sgs 104960 0x80 # 10000000   Q7
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (21 entries, util 15.6000 %)

```
sgs 49280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 16960 0xBF # 10111111   Q7
sgs 25280 0x80 # 10000000   Q7
sgs 1280 0x3F # 00111111   BE
sgs 82880 0x40 # 01000000   Q6
sgs 11840 0x3F # 00111111   BE
sgs 49280 0x7F # 01111111   Q6
sgs 138880 0x40 # 01000000   Q6
sgs 11840 0x3F # 00111111   BE
sgs 49280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 16960 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 14080 0x3F # 00111111   BE
sgs 82880 0x40 # 01000000   Q6
sgs 11840 0x3F # 00111111   BE
sgs 49280 0x7F # 01111111   Q6
sgs 89600 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p5  (22 entries, util 10.9200 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 20480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 16960 0xBF # 10111111   Q7
sgs 48640 0x80 # 10000000   Q7
sgs 22400 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 111040 0x40 # 01000000   Q6
sgs 22400 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 20480 0x7F # 01111111   Q6
sgs 78080 0x40 # 01000000   Q6
sgs 22400 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 94400 0x40 # 01000000   Q6
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p4  (23 entries, util 9.3600 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 7680 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 17280 0x7F # 01111111   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 54720 0x80 # 10000000   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 109440 0x80 # 10000000   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 17280 0x7F # 01111111   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 54720 0x80 # 10000000   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 89280 0x80 # 10000000   Q7
sgs 40640 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (20 entries, util 10.9200 %)

```
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 15680 0x7F # 01111111   Q6
sgs 82880 0x80 # 10000000   Q7
sgs 26880 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 12160 0x3F # 00111111   BE
sgs 111040 0x80 # 10000000   Q7
sgs 26880 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 15680 0x7F # 01111111   Q6
sgs 82880 0x80 # 10000000   Q7
sgs 26880 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 12160 0x3F # 00111111   BE
sgs 98880 0x80 # 10000000   Q7
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (24 entries, util 10.9200 %)

```
sgs 24960 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 5760 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 19200 0xBF # 10111111   Q7
sgs 48640 0x80 # 10000000   Q7
sgs 14080 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 111040 0x40 # 01000000   Q6
sgs 14080 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 5760 0x3F # 00111111   BE
sgs 80320 0x40 # 01000000   Q6
sgs 14080 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 86080 0x40 # 01000000   Q6
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p5  (21 entries, util 15.6000 %)

```
sgs 43200 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 15360 0xBF # 10111111   Q7
sgs 25280 0x80 # 10000000   Q7
sgs 2240 0x3F # 00111111   BE
sgs 83520 0x40 # 01000000   Q6
sgs 17920 0xBF # 10111111   Q7
sgs 43200 0x7F # 01111111   Q6
sgs 138880 0x40 # 01000000   Q6
sgs 17920 0xBF # 10111111   Q7
sgs 43200 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 15360 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 15040 0xBF # 10111111   Q7
sgs 83520 0x40 # 01000000   Q6
sgs 17920 0xBF # 10111111   Q7
sgs 43200 0x7F # 01111111   Q6
sgs 95680 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p4  (21 entries, util 10.9200 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 17280 0x7F # 01111111   Q6
sgs 91200 0x80 # 10000000   Q7
sgs 10880 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 18240 0x7F # 01111111   Q6
sgs 120960 0x80 # 10000000   Q7
sgs 10880 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 18240 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 17280 0x7F # 01111111   Q6
sgs 91200 0x80 # 10000000   Q7
sgs 10880 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 18240 0x7F # 01111111   Q6
sgs 102720 0x80 # 10000000   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (23 entries, util 9.3600 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 24000 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 56320 0x80 # 10000000   Q7
sgs 27200 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 13440 0x7F # 01111111   Q6
sgs 109440 0x80 # 10000000   Q7
sgs 27200 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 13440 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24000 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 56320 0x80 # 10000000   Q7
sgs 27200 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 13440 0x7F # 01111111   Q6
sgs 96000 0x80 # 10000000   Q7
sgs 40640 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (23 entries, util 15.6000 %)

```
sgs 37120 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 13440 0xBF # 10111111   Q7
sgs 27840 0x80 # 10000000   Q7
sgs 640 0x3F # 00111111   BE
sgs 84160 0x40 # 01000000   Q6
sgs 24000 0xBF # 10111111   Q7
sgs 37120 0x7F # 01111111   Q6
sgs 138880 0x40 # 01000000   Q6
sgs 24000 0xBF # 10111111   Q7
sgs 37120 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 13440 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 16000 0xBF # 10111111   Q7
sgs 84160 0x40 # 01000000   Q6
sgs 24000 0xBF # 10111111   Q7
sgs 37120 0x7F # 01111111   Q6
sgs 101760 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p5  (22 entries, util 10.9200 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 16000 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 21440 0xBF # 10111111   Q7
sgs 48640 0x80 # 10000000   Q7
sgs 5760 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 111040 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 16000 0x3F # 00111111   BE
sgs 82560 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 77760 0x40 # 01000000   Q6
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p2  (28 entries, util 17.1600 %)

```
sgs 24320 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 4800 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 13760 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 19840 0xBF # 10111111   Q7
sgs 3840 0x3F # 00111111   BE
sgs 65280 0x80 # 10000000   Q7
sgs 30720 0xBF # 10111111   Q7
sgs 24320 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 4800 0x3F # 00111111   BE
sgs 127680 0x40 # 01000000   Q6
sgs 30720 0xBF # 10111111   Q7
sgs 24320 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 4800 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 13760 0xBF # 10111111   Q7
sgs 101440 0x40 # 01000000   Q6
sgs 30720 0xBF # 10111111   Q7
sgs 24320 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 4800 0x3F # 00111111   BE
sgs 103360 0x40 # 01000000   Q6
sgs 5120 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p4  (23 entries, util 9.3600 %)

```
sgs 6720 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 8320 0x3F # 00111111   BE
sgs 45120 0x80 # 10000000   Q7
sgs 46720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 6720 0x3F # 00111111   BE
sgs 96640 0x80 # 10000000   Q7
sgs 46720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 6720 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 8320 0x3F # 00111111   BE
sgs 45120 0x80 # 10000000   Q7
sgs 46720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 6720 0x3F # 00111111   BE
sgs 89920 0x80 # 10000000   Q7
sgs 3520 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (21 entries, util 15.6000 %)

```
sgs 31040 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12160 0x3F # 00111111   BE
sgs 29120 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 84800 0x40 # 01000000   Q6
sgs 30080 0xBF # 10111111   Q7
sgs 31040 0x7F # 01111111   Q6
sgs 138880 0x40 # 01000000   Q6
sgs 30080 0xBF # 10111111   Q7
sgs 31040 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 16960 0xBF # 10111111   Q7
sgs 84800 0x40 # 01000000   Q6
sgs 30080 0xBF # 10111111   Q7
sgs 31040 0x7F # 01111111   Q6
sgs 107840 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

