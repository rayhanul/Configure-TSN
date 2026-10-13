# Heuristic-enlarged GCL schedule (Problem 2: window enlargement)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Time-sensitive PCPs considered: [6, 7]
- Seeded from SMT run: **result/result-2026-10-13-dataset-testbed-13-tree-avgwin/smt-c9-off/13-t3600-c9off-minlat**

## Admission (unchanged by this package -- it only widens windows)

SMT-fixed flows: **11**/20. This package never admits a flow itself; it banks slack for a later admission pass (`prob_3_admit`, Problem 3) to use.

## Opportunistic idle top-up (Step 7 -- see enlarge.py)

Total: **12144640 ns**, drawn from idle capacity on ports at or below utilisation 0.2, independent of any route's deadline-slack budget.

| port | queue | applied (ns) |
|---|---|---|
| S1-p0 | Q6 | 517120 |
| S1-p0 | Q7 | 158720 |
| S3-p0 | Q6 | 701120 |
| sw01-p2 | Q6 | 552960 |
| sw01-p4 | Q6 | 686080 |
| sw02-p2 | Q6 | 370880 |
| sw02-p2 | Q7 | 254080 |
| sw02-p4 | Q6 | 496640 |
| sw02-p4 | Q7 | 169600 |
| sw03-p4 | Q6 | 571520 |
| sw03-p5 | Q6 | 670720 |
| sw04-p4 | Q6 | 389120 |
| sw04-p4 | Q7 | 256960 |
| sw04-p5 | Q6 | 482880 |
| sw04-p5 | Q7 | 172160 |
| sw05-p4 | Q6 | 655360 |
| sw05-p5 | Q6 | 590080 |
| sw06-p4 | Q6 | 462720 |
| sw06-p4 | Q7 | 180480 |
| sw06-p5 | Q6 | 407040 |
| sw06-p5 | Q7 | 259520 |
| sw07-p4 | Q6 | 608320 |
| sw07-p5 | Q6 | 639680 |
| sw08-p2 | Q6 | 577920 |
| sw08-p4 | Q6 | 424960 |
| sw08-p4 | Q7 | 261760 |
| sw08-p5 | Q6 | 626240 |

## Opportunistic window creation (Step 8 -- see enlarge.py)

**5** brand-new window(s) opened, **62400 ns** total, on ports at or below utilisation 0.2 whose TT queue had zero windows before this run.

| port | queue | size (ns) |
|---|---|---|
| sw01-p4 | Q7 | 12480 |
| sw03-p5 | Q7 | 12480 |
| sw05-p4 | Q7 | 12480 |
| sw07-p5 | Q7 | 12480 |
| sw08-p2 | Q7 | 12480 |

## Best-effort gap equalization (Step 9 -- see enlarge.py)

**7432960 ns** given back from Steps 7/8's growth so each port's leftover non-TAS gaps land close to equal, instead of one gap staying huge while a neighbour is squeezed to the bare 1-tick C10 minimum.

| port | given back (ns) |
|---|---|
| sw02-p2 | 488320 |
| sw04-p4 | 488320 |
| sw06-p5 | 488320 |
| sw08-p4 | 488320 |
| S3-p0 | 418240 |
| sw06-p4 | 406720 |
| sw02-p4 | 400640 |
| sw04-p5 | 400640 |
| S1-p0 | 393280 |
| sw01-p4 | 378560 |
| sw03-p5 | 378560 |
| sw05-p4 | 378560 |
| sw07-p5 | 378560 |
| sw01-p2 | 320640 |
| sw03-p4 | 320640 |
| sw05-p5 | 320640 |
| sw07-p4 | 320640 |
| sw08-p5 | 320640 |
| sw08-p2 | 282560 |
| S2-p0 | 60160 |

## Opportunistic overlay window creation (Step 10 -- see enlarge.py)

**38** new overlay window(s), **7864320 ns** total, carved out of already-open best-effort spans on ports at or below utilisation 0.2 -- best-effort stays reachable inside each one (gate mask keeps its BE bits set), so none of this is closed off from BE.

| port | queue | size (ns) |
|---|---|---|
| S1-p0 | Q6 | 193600 |
| S1-p0 | Q7 | 199680 |
| S3-p0 | Q6 | 206080 |
| S3-p0 | Q7 | 212160 |
| sw01-p2 | Q6 | 108800 |
| sw01-p2 | Q7 | 250880 |
| sw01-p4 | Q6 | 158080 |
| sw01-p4 | Q7 | 212160 |
| sw02-p2 | Q6 | 282240 |
| sw02-p2 | Q7 | 269120 |
| sw02-p4 | Q6 | 197760 |
| sw02-p4 | Q7 | 219520 |
| sw03-p4 | Q6 | 183360 |
| sw03-p4 | Q7 | 216320 |
| sw03-p5 | Q6 | 149760 |
| sw03-p5 | Q7 | 241280 |
| sw04-p4 | Q6 | 249600 |
| sw04-p4 | Q7 | 274560 |
| sw04-p5 | Q6 | 172160 |
| sw04-p5 | Q7 | 219520 |
| sw05-p4 | Q6 | 216320 |
| sw05-p4 | Q7 | 187200 |
| sw05-p5 | Q6 | 207680 |
| sw05-p5 | Q7 | 175360 |
| sw06-p4 | Q6 | 251840 |
| sw06-p4 | Q7 | 204800 |
| sw06-p5 | Q6 | 243520 |
| sw06-p5 | Q7 | 266240 |
| sw07-p4 | Q6 | 199680 |
| sw07-p4 | Q7 | 108800 |
| sw07-p5 | Q6 | 228800 |
| sw07-p5 | Q7 | 196160 |
| sw08-p2 | Q6 | 193600 |
| sw08-p2 | Q7 | 116480 |
| sw08-p4 | Q6 | 268480 |
| sw08-p4 | Q7 | 232960 |
| sw08-p5 | Q6 | 166400 |
| sw08-p5 | Q7 | 183360 |

## Candidate routes (P^cand = routes of the fixed flows above)

| route | PCPs carried | flows |
|---|---|---|
| S1->sw02->sw04->sw06->sw08->S2 | Q6 (1) | 1 |
| S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | Q6 (1), Q7 (1) | 2 |
| S2->sw08->sw06->sw04->sw02->S1 | Q6 (1), Q7 (1) | 2 |
| S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 (2), Q7 (1) | 3 |
| S3->sw01->sw03->sw05->sw07->sw08->S2 | Q6 (3) | 3 |

## Per-link enlargement accounting

| link | sharing eta | route-safe slack (ns) | link budget (ns) | final slack (ns) | applied (ns) |
|---|---|---|---|---|---|
| S1-p0 | 2 | Q6:20536, Q7:21525 | 42061 | Q6:20536, Q7:16578 | Q6:439360, Q7:273280 |
| S2-p0 | 2 | Q6:20791, Q7:120107 | 140898 | Q6:20791, Q7:87740 | Q6:5760, Q7:42240 |
| sw01-p2 | 2 | Q6:13361, Q7:30797 | 44158 | Q6:13361, Q7:24350 | Q6:355200, Q7:250880 |
| sw02-p4 | 2 | Q6:17047, Q7:17097 | 34144 | Q6:17047, Q7:13100 | Q6:419520, Q7:293120 |
| sw03-p4 | 2 | Q6:11222, Q7:24461 | 35683 | Q6:11222, Q7:19182 | Q6:446400, Q7:216320 |
| sw04-p5 | 2 | Q6:14151, Q7:13579 | 27730 | Q6:14151, Q7:10351 | Q6:377280, Q7:293120 |
| sw05-p5 | 2 | Q6:9425, Q7:19428 | 28853 | Q6:9425, Q7:15110 | Q6:487360, Q7:175360 |
| sw06-p4 | 2 | Q6:11747, Q7:10786 | 22533 | Q6:11747, Q7:8180 | Q6:434240, Q7:278400 |
| sw07-p4 | 2 | Q6:7916, Q7:15431 | 23347 | Q6:7916, Q7:11901 | Q6:496000, Q7:108800 |
| sw08-p2 | 2 | Q6:18393, Q7:0 | 18393 | Q6:18393 | Q6:507200, Q7:128960 |
| sw08-p5 | 2 | Q6:6649, Q7:13390 | 20039 | Q6:6649, Q7:10377 | Q6:479360, Q7:183360 |
| S3-p0 | 1 | Q6:11669, Q7:0 | 11669 | Q6:11669 | Q6:500480, Q7:212160 |
| sw01-p4 | 1 | Q6:10083, Q7:0 | 10083 | Q6:10083 | Q6:475520, Q7:224640 |
| sw02-p2 | 1 | Q6:12757, Q7:28091 | 40847 | Q6:12757, Q7:21406 | Q6:384000, Q7:337600 |
| sw03-p5 | 1 | Q6:8712, Q7:0 | 8712 | Q6:8712 | Q6:450560, Q7:253760 |
| sw04-p4 | 1 | Q6:11131, Q7:24160 | 35291 | Q6:11131, Q7:18367 | Q6:368000, Q7:343040 |
| sw05-p4 | 1 | Q6:7528, Q7:0 | 7528 | Q6:7528 | Q6:500480, Q7:199680 |
| sw06-p5 | 1 | Q6:9712, Q7:20780 | 30492 | Q6:9712, Q7:15760 | Q6:378560, Q7:334720 |
| sw07-p5 | 1 | Q6:6505, Q7:0 | 6505 | Q6:6505 | Q6:496320, Q7:208640 |
| sw08-p4 | 1 | Q6:8474, Q7:17873 | 26347 | Q6:8474, Q7:13523 | Q6:420160, Q7:301440 |

Total applied: **13081280 ns** across 20 port(s). Network total slack now banked: **13097920 ns**. GCL_size overflow: 0.

## Per-port GCL entries: before (SMT) vs. after (heuristic-enlarged)

| port | SMT entries | enlarged entries | GCL_size |
|---|---|---|---|
| sw01-p2 | 21 | 32 | 255 |
| sw01-p4 | 15 | 25 | 255 |
| sw02-p2 | 13 | 24 | 255 |
| sw02-p4 | 15 | 22 | 255 |
| sw03-p4 | 21 | 26 | 255 |
| sw03-p5 | 15 | 22 | 255 |
| sw04-p4 | 13 | 21 | 255 |
| sw04-p5 | 15 | 22 | 255 |
| sw05-p4 | 15 | 20 | 255 |
| sw05-p5 | 21 | 28 | 255 |
| sw06-p4 | 15 | 20 | 255 |
| sw06-p5 | 13 | 23 | 255 |
| sw07-p4 | 21 | 31 | 255 |
| sw07-p5 | 15 | 26 | 255 |
| sw08-p2 | 23 | 23 | 255 |
| sw08-p4 | 13 | 23 | 255 |
| sw08-p5 | 21 | 25 | 255 |

## Flows

| flow | route | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|
| s0(id=1 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | - | - | - | no |
| s1(id=2 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | - | - | - | no |
| s2(id=3 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | 7 | 24960 | 145680 | yes |
| s3(id=4 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | - | - | - | no |
| s4(id=5 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 6 | 0 | 95760 | yes |
| s5(id=6 S3->S1) | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | - | - | - | no |
| s6(id=7 S3->S1) | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | - | - | - | no |
| s7(id=8 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 6 | 62400 | 95760 | yes |
| s8(id=9 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 6 | 37440 | 95760 | yes |
| s9(id=10 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | 6 | 0 | 79120 | yes |
| s10(id=11 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | - | - | - | no |
| s11(id=12 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | - | - | - | no |
| s12(id=13 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | 7 | 49920 | 79120 | yes |
| s13(id=14 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 6 | 0 | 79120 | yes |
| s14(id=15 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | 6 | 49920 | 159120 | yes |
| s15(id=16 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | - | - | - | no |
| s16(id=17 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 7 | 99840 | 96400 | yes |
| s17(id=18 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | - | - | - | no |
| s18(id=19 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 6 | 24960 | 95760 | yes |
| s19(id=20 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 6 | 74880 | 108560 | yes |

## Per-hop windows (slack_ns > 0 means this window was enlarged)

| flow | egress port | queue | psi (ns) | delta (ns) |
|---|---|---|---|---|
| s2(id=3 S1->S3) | S1-p0 | Q7 | 24960 | 12480 |
| s2(id=3 S1->S3) | sw02-p4 | Q7 | 41600 | 12480 |
| s2(id=3 S1->S3) | sw04-p5 | Q7 | 58240 | 12480 |
| s2(id=3 S1->S3) | sw06-p4 | Q7 | 74880 | 12480 |
| s2(id=3 S1->S3) | sw08-p5 | Q7 | 91520 | 12480 |
| s2(id=3 S1->S3) | sw07-p4 | Q7 | 108160 | 12480 |
| s2(id=3 S1->S3) | sw05-p5 | Q7 | 124800 | 12480 |
| s2(id=3 S1->S3) | sw03-p4 | Q7 | 141440 | 12480 |
| s2(id=3 S1->S3) | sw01-p2 | Q7 | 158080 | 12480 |
| s4(id=5 S3->S2) | S3-p0 | Q6 | 0 | 12480 |
| s4(id=5 S3->S2) | sw01-p4 | Q6 | 16640 | 12480 |
| s4(id=5 S3->S2) | sw03-p5 | Q6 | 33280 | 12480 |
| s4(id=5 S3->S2) | sw05-p4 | Q6 | 49920 | 12480 |
| s4(id=5 S3->S2) | sw07-p5 | Q6 | 66560 | 12480 |
| s4(id=5 S3->S2) | sw08-p2 | Q6 | 83200 | 12480 |
| s7(id=8 S3->S2) | S3-p0 | Q6 | 62400 | 12480 |
| s7(id=8 S3->S2) | sw01-p4 | Q6 | 79040 | 12480 |
| s7(id=8 S3->S2) | sw03-p5 | Q6 | 95680 | 12480 |
| s7(id=8 S3->S2) | sw05-p4 | Q6 | 112320 | 12480 |
| s7(id=8 S3->S2) | sw07-p5 | Q6 | 128960 | 12480 |
| s7(id=8 S3->S2) | sw08-p2 | Q6 | 145600 | 12480 |
| s8(id=9 S3->S2) | S3-p0 | Q6 | 37440 | 12480 |
| s8(id=9 S3->S2) | sw01-p4 | Q6 | 54080 | 12480 |
| s8(id=9 S3->S2) | sw03-p5 | Q6 | 70720 | 12480 |
| s8(id=9 S3->S2) | sw05-p4 | Q6 | 87360 | 12480 |
| s8(id=9 S3->S2) | sw07-p5 | Q6 | 104000 | 12480 |
| s8(id=9 S3->S2) | sw08-p2 | Q6 | 120640 | 12480 |
| s9(id=10 S2->S1) | S2-p0 | Q6 | 0 | 12480 |
| s9(id=10 S2->S1) | sw08-p4 | Q6 | 16640 | 12480 |
| s9(id=10 S2->S1) | sw06-p5 | Q6 | 33280 | 12480 |
| s9(id=10 S2->S1) | sw04-p4 | Q6 | 49920 | 12480 |
| s9(id=10 S2->S1) | sw02-p2 | Q6 | 66560 | 12480 |
| s12(id=13 S2->S1) | S2-p0 | Q7 | 49920 | 12480 |
| s12(id=13 S2->S1) | sw08-p4 | Q7 | 66560 | 12480 |
| s12(id=13 S2->S1) | sw06-p5 | Q7 | 83200 | 12480 |
| s12(id=13 S2->S1) | sw04-p4 | Q7 | 99840 | 12480 |
| s12(id=13 S2->S1) | sw02-p2 | Q7 | 116480 | 12480 |
| s13(id=14 S1->S2) | S1-p0 | Q6 | 0 | 12480 |
| s13(id=14 S1->S2) | sw02-p4 | Q6 | 16640 | 12480 |
| s13(id=14 S1->S2) | sw04-p5 | Q6 | 33280 | 12480 |
| s13(id=14 S1->S2) | sw06-p4 | Q6 | 49920 | 12480 |
| s13(id=14 S1->S2) | sw08-p2 | Q6 | 66560 | 12480 |
| s14(id=15 S1->S3) | S1-p0 | Q6 | 49920 | 12480 |
| s14(id=15 S1->S3) | sw02-p4 | Q6 | 73920 | 12480 |
| s14(id=15 S1->S3) | sw04-p5 | Q6 | 90560 | 12480 |
| s14(id=15 S1->S3) | sw06-p4 | Q6 | 113280 | 12480 |
| s14(id=15 S1->S3) | sw08-p5 | Q6 | 129920 | 12480 |
| s14(id=15 S1->S3) | sw07-p4 | Q6 | 146560 | 12480 |
| s14(id=15 S1->S3) | sw05-p5 | Q6 | 163200 | 12480 |
| s14(id=15 S1->S3) | sw03-p4 | Q6 | 179840 | 12480 |
| s14(id=15 S1->S3) | sw01-p2 | Q6 | 196480 | 12480 |
| s16(id=17 S2->S3) | S2-p0 | Q7 | 99840 | 12480 |
| s16(id=17 S2->S3) | sw08-p5 | Q7 | 117120 | 12480 |
| s16(id=17 S2->S3) | sw07-p4 | Q7 | 133760 | 12480 |
| s16(id=17 S2->S3) | sw05-p5 | Q7 | 150400 | 12480 |
| s16(id=17 S2->S3) | sw03-p4 | Q7 | 167040 | 12480 |
| s16(id=17 S2->S3) | sw01-p2 | Q7 | 183680 | 12480 |
| s18(id=19 S2->S3) | S2-p0 | Q6 | 24960 | 12480 |
| s18(id=19 S2->S3) | sw08-p5 | Q6 | 41600 | 12480 |
| s18(id=19 S2->S3) | sw07-p4 | Q6 | 58240 | 12480 |
| s18(id=19 S2->S3) | sw05-p5 | Q6 | 74880 | 12480 |
| s18(id=19 S2->S3) | sw03-p4 | Q6 | 91520 | 12480 |
| s18(id=19 S2->S3) | sw01-p2 | Q6 | 108160 | 12480 |
| s19(id=20 S2->S3) | S2-p0 | Q6 | 74880 | 12480 |
| s19(id=20 S2->S3) | sw08-p5 | Q6 | 104320 | 12480 |
| s19(id=20 S2->S3) | sw07-p4 | Q6 | 120960 | 12480 |
| s19(id=20 S2->S3) | sw05-p5 | Q6 | 137600 | 12480 |
| s19(id=20 S2->S3) | sw03-p4 | Q6 | 154240 | 12480 |
| s19(id=20 S2->S3) | sw01-p2 | Q6 | 170880 | 12480 |

## Constraint check

- C1-C7, C9: OK
- seed-integrity (no SMT-fixed flow's placement changed): OK

## GCL per egress port

### sw01-p2  (32 entries, util 15.6000 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 8000 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 29440 0x7F # 01111111   Q6
sgs 8000 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 50560 0x40 # 01000000   Q6
sgs 2880 0x3F # 00111111   BE
sgs 50240 0xBF # 10111111   Q7
sgs 8000 0x3F # 00111111   BE
sgs 138880 0x40 # 01000000   Q6
sgs 2880 0x3F # 00111111   BE
sgs 50240 0xBF # 10111111   Q7
sgs 8000 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 29440 0x7F # 01111111   Q6
sgs 8000 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 76160 0x40 # 01000000   Q6
sgs 2880 0x3F # 00111111   BE
sgs 50240 0xBF # 10111111   Q7
sgs 8000 0x3F # 00111111   BE
sgs 30720 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p4  (25 entries, util 10.9200 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 58560 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 120960 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 4160 0x3F # 00111111   BE
sgs 83520 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 104320 0x40 # 01000000   Q6
sgs 29120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (24 entries, util 9.3600 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 21120 0xBF # 10111111   Q7
sgs 16320 0x7F # 01111111   Q6
sgs 46720 0x80 # 10000000   Q7
sgs 36800 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 96640 0x40 # 01000000   Q6
sgs 36800 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 21120 0xBF # 10111111   Q7
sgs 16320 0x7F # 01111111   Q6
sgs 46720 0x80 # 10000000   Q7
sgs 36800 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 30080 0x40 # 01000000   Q6
sgs 3520 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p4  (22 entries, util 10.9200 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 19840 0xBF # 10111111   Q7
sgs 53760 0x40 # 01000000   Q6
sgs 22400 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 111040 0x40 # 01000000   Q6
sgs 22400 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 86080 0x80 # 10000000   Q7
sgs 22400 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 94400 0x40 # 01000000   Q6
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (26 entries, util 15.6000 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 50560 0x40 # 01000000   Q6
sgs 19520 0x7F # 01111111   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 138880 0x40 # 01000000   Q6
sgs 19520 0x7F # 01111111   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 76160 0x40 # 01000000   Q6
sgs 19520 0x7F # 01111111   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 47360 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p5  (22 entries, util 10.9200 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 20800 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 58560 0x40 # 01000000   Q6
sgs 45760 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 120960 0x40 # 01000000   Q6
sgs 45760 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 20800 0xBF # 10111111   Q7
sgs 83520 0x40 # 01000000   Q6
sgs 45760 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 87680 0x40 # 01000000   Q6
sgs 29120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p4  (21 entries, util 9.3600 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0xBF # 10111111   Q7
sgs 46720 0x80 # 10000000   Q7
sgs 3520 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 96640 0x40 # 01000000   Q6
sgs 3520 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0xBF # 10111111   Q7
sgs 46720 0x80 # 10000000   Q7
sgs 3520 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 46720 0x40 # 01000000   Q6
sgs 3520 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (22 entries, util 10.9200 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 19840 0xBF # 10111111   Q7
sgs 53760 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 111040 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 86080 0x80 # 10000000   Q7
sgs 5760 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 77760 0x40 # 01000000   Q6
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (20 entries, util 10.9200 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 58560 0x40 # 01000000   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 120960 0x40 # 01000000   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 83520 0x40 # 01000000   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 71040 0x40 # 01000000   Q6
sgs 29120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p5  (28 entries, util 15.6000 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12800 0xBF # 10111111   Q7
sgs 24640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 50560 0x40 # 01000000   Q6
sgs 36160 0x7F # 01111111   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 138880 0x40 # 01000000   Q6
sgs 36160 0x7F # 01111111   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12800 0xBF # 10111111   Q7
sgs 24640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 76160 0x40 # 01000000   Q6
sgs 36160 0x7F # 01111111   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 64000 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p4  (20 entries, util 10.9200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 13120 0x7F # 01111111   Q6
sgs 47680 0x40 # 01000000   Q6
sgs 39040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 111040 0x40 # 01000000   Q6
sgs 39040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 86080 0x80 # 10000000   Q7
sgs 39040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 61120 0x40 # 01000000   Q6
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (23 entries, util 9.3600 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 33280 0xBF # 10111111   Q7
sgs 46720 0x80 # 10000000   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 96640 0x40 # 01000000   Q6
sgs 20160 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 33280 0xBF # 10111111   Q7
sgs 46720 0x80 # 10000000   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 63360 0x40 # 01000000   Q6
sgs 3520 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (31 entries, util 15.6000 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 29440 0xBF # 10111111   Q7
sgs 8000 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 50560 0x40 # 01000000   Q6
sgs 2880 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 8320 0x3F # 00111111   BE
sgs 138880 0x40 # 01000000   Q6
sgs 2880 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 29440 0xBF # 10111111   Q7
sgs 8000 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 76160 0x40 # 01000000   Q6
sgs 2880 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 8320 0x3F # 00111111   BE
sgs 80640 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p5  (26 entries, util 10.9200 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 21120 0xBF # 10111111   Q7
sgs 3840 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 58560 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 120960 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 21120 0xBF # 10111111   Q7
sgs 3840 0x3F # 00111111   BE
sgs 83520 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 54400 0x40 # 01000000   Q6
sgs 29120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p2  (23 entries, util 17.1600 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 29120 0x40 # 01000000   Q6
sgs 4480 0x3F # 00111111   BE
sgs 20480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 70080 0x40 # 01000000   Q6
sgs 34240 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 149120 0x40 # 01000000   Q6
sgs 34240 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 29120 0x40 # 01000000   Q6
sgs 4480 0x3F # 00111111   BE
sgs 20480 0x7F # 01111111   Q6
sgs 95040 0x40 # 01000000   Q6
sgs 34240 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 82560 0x40 # 01000000   Q6
sgs 960 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p4  (23 entries, util 9.3600 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 46720 0x80 # 10000000   Q7
sgs 36800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 96640 0x40 # 01000000   Q6
sgs 36800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 46720 0x80 # 10000000   Q7
sgs 36800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 80000 0x40 # 01000000   Q6
sgs 3520 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (25 entries, util 15.6000 %)

```
sgs 41600 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 50560 0x40 # 01000000   Q6
sgs 19520 0xBF # 10111111   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 138880 0x40 # 01000000   Q6
sgs 19520 0xBF # 10111111   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 76160 0x40 # 01000000   Q6
sgs 19520 0xBF # 10111111   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 97280 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

