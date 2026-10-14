# Heuristic-enlarged GCL schedule (Problem 2: window enlargement)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Time-sensitive PCPs considered: [6, 7]
- Seeded from SMT run: **result/result-2026-10-13-dataset-testbed-11-tree-avgwin/smt-c9-on/11-fair-retimed-c9on**

## Admission (unchanged by this package -- it only widens windows)

SMT-fixed flows: **10**/10. This package never admits a flow itself; it banks slack for a later admission pass (`prob_3_admit`, Problem 3) to use.

## Opportunistic idle top-up (Step 7 -- see enlarge.py)

Total: **12086400 ns**, drawn from idle capacity on ports at or below utilisation 0.2, independent of any route's deadline-slack budget.

| port | queue | applied (ns) |
|---|---|---|
| S1-p0 | Q6 | 268480 |
| S1-p0 | Q7 | 382400 |
| S2-p0 | Q6 | 567680 |
| S3-p0 | Q6 | 81280 |
| S3-p0 | Q7 | 528640 |
| sw01-p2 | Q7 | 623680 |
| sw01-p4 | Q6 | 94720 |
| sw01-p4 | Q7 | 506240 |
| sw02-p2 | Q6 | 446080 |
| sw02-p2 | Q7 | 200000 |
| sw02-p4 | Q6 | 273280 |
| sw02-p4 | Q7 | 376320 |
| sw03-p4 | Q7 | 639680 |
| sw03-p5 | Q6 | 100160 |
| sw03-p5 | Q7 | 498880 |
| sw04-p4 | Q6 | 456000 |
| sw04-p4 | Q7 | 203200 |
| sw04-p5 | Q6 | 277440 |
| sw04-p5 | Q7 | 369920 |
| sw05-p4 | Q6 | 105280 |
| sw05-p4 | Q7 | 490880 |
| sw05-p5 | Q7 | 654720 |
| sw06-p4 | Q6 | 280640 |
| sw06-p4 | Q7 | 363200 |
| sw06-p5 | Q6 | 464960 |
| sw06-p5 | Q7 | 206080 |
| sw07-p4 | Q7 | 668800 |
| sw07-p5 | Q6 | 110400 |
| sw07-p5 | Q7 | 482880 |
| sw08-p4 | Q6 | 473280 |
| sw08-p4 | Q7 | 208960 |
| sw08-p5 | Q7 | 682240 |

## Opportunistic window creation (Step 8 -- see enlarge.py)

**5** brand-new window(s) opened, **62400 ns** total, on ports at or below utilisation 0.2 whose TT queue had zero windows before this run.

| port | queue | size (ns) |
|---|---|---|
| sw01-p2 | Q6 | 12480 |
| sw03-p4 | Q6 | 12480 |
| sw05-p5 | Q6 | 12480 |
| sw07-p4 | Q6 | 12480 |
| sw08-p5 | Q6 | 12480 |

## Best-effort gap equalization (Step 9 -- see enlarge.py)

**6537920 ns** given back from Steps 7/8's growth so each port's leftover non-TAS gaps land close to equal, instead of one gap staying huge while a neighbour is squeezed to the bare 1-tick C10 minimum.

| port | given back (ns) |
|---|---|
| sw02-p2 | 477120 |
| sw04-p4 | 475840 |
| sw06-p5 | 474560 |
| sw08-p4 | 473280 |
| S2-p0 | 450880 |
| sw02-p4 | 360960 |
| sw04-p5 | 360960 |
| sw06-p4 | 360960 |
| S1-p0 | 360960 |
| S3-p0 | 307520 |
| sw01-p4 | 278400 |
| sw03-p5 | 276160 |
| sw05-p4 | 273920 |
| sw07-p5 | 271680 |
| sw01-p2 | 262400 |
| sw03-p4 | 262400 |
| sw05-p5 | 262400 |
| sw07-p4 | 262400 |
| sw08-p5 | 262400 |
| sw08-p2 | 22720 |

## Opportunistic overlay window creation (Step 10 -- see enlarge.py)

**38** new overlay window(s), **6640320 ns** total, carved out of already-open best-effort spans on ports at or below utilisation 0.2 -- best-effort stays reachable inside each one (gate mask keeps its BE bits set), so none of this is closed off from BE.

| port | queue | size (ns) |
|---|---|---|
| S1-p0 | Q6 | 161280 |
| S1-p0 | Q7 | 199680 |
| S2-p0 | Q6 | 224640 |
| S2-p0 | Q7 | 212160 |
| S3-p0 | Q6 | 74880 |
| S3-p0 | Q7 | 212160 |
| sw01-p2 | Q6 | 149760 |
| sw01-p2 | Q7 | 200320 |
| sw01-p4 | Q6 | 61440 |
| sw01-p4 | Q7 | 168960 |
| sw02-p2 | Q6 | 206720 |
| sw02-p2 | Q7 | 287680 |
| sw02-p4 | Q6 | 111360 |
| sw02-p4 | Q7 | 199680 |
| sw03-p4 | Q6 | 149760 |
| sw03-p4 | Q7 | 195840 |
| sw03-p5 | Q6 | 92160 |
| sw03-p5 | Q7 | 145920 |
| sw04-p4 | Q6 | 212800 |
| sw04-p4 | Q7 | 273600 |
| sw04-p5 | Q6 | 119360 |
| sw04-p5 | Q7 | 224640 |
| sw05-p4 | Q6 | 122880 |
| sw05-p4 | Q7 | 122880 |
| sw05-p5 | Q6 | 149760 |
| sw05-p5 | Q7 | 187520 |
| sw06-p4 | Q6 | 152640 |
| sw06-p4 | Q7 | 224640 |
| sw06-p5 | Q6 | 170240 |
| sw06-p5 | Q7 | 266880 |
| sw07-p4 | Q6 | 149760 |
| sw07-p4 | Q7 | 179200 |
| sw07-p5 | Q6 | 153600 |
| sw07-p5 | Q7 | 99840 |
| sw08-p4 | Q6 | 194880 |
| sw08-p4 | Q7 | 260160 |
| sw08-p5 | Q6 | 149760 |
| sw08-p5 | Q7 | 170880 |

## Candidate routes (P^cand = routes of the fixed flows above)

| route | PCPs carried | flows |
|---|---|---|
| S1->sw02->sw04->sw06->sw08->S2 | Q6 (2), Q7 (1) | 3 |
| S2->sw08->sw06->sw04->sw02->S1 | Q6 (2) | 2 |
| S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 (1) | 1 |
| S3->sw01->sw03->sw05->sw07->sw08->S2 | Q6 (1), Q7 (2) | 3 |
| S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q7 (1) | 1 |

## Per-link enlargement accounting

| link | sharing eta | route-safe slack (ns) | link budget (ns) | final slack (ns) | applied (ns) |
|---|---|---|---|---|---|
| S2-p0 | 2 | Q6:32399, Q7:273164 | 305563 | Q6:32399, Q7:204501 | Q6:477120, Q7:233920 |
| S3-p0 | 2 | Q6:91797, Q7:21736 | 113533 | Q6:31496, Q7:21736 | Q6:132480, Q7:509760 |
| sw01-p4 | 2 | Q6:80736, Q7:18379 | 99114 | Q6:28286, Q7:18379 | Q6:129280, Q7:470080 |
| sw02-p2 | 2 | Q6:26189, Q7:19993 | 46183 | Q6:26189, Q7:16381 | Q6:379520, Q7:326080 |
| sw03-p5 | 2 | Q6:71008, Q7:15540 | 86547 | Q6:25400, Q7:15540 | Q6:162560, Q7:439040 |
| sw04-p4 | 2 | Q6:20942, Q7:17573 | 38516 | Q6:20942, Q7:14506 | Q6:391680, Q7:313280 |
| sw05-p4 | 2 | Q6:62452, Q7:13140 | 75591 | Q6:22807, Q7:13140 | Q6:195840, Q7:408000 |
| sw06-p5 | 2 | Q6:16747, Q7:15481 | 32228 | Q6:16747, Q7:12879 | Q6:355200, Q7:307840 |
| sw07-p5 | 2 | Q6:54927, Q7:11110 | 66037 | Q6:20477, Q7:11110 | Q6:229120, Q7:376960 |
| sw08-p2 | 2 | Q6:140836, Q7:13846 | 154682 | Q6:123043, Q7:13846 | Q6:112000, Q7:1920 |
| sw08-p4 | 2 | Q6:13392, Q7:13670 | 27062 | Q6:13392, Q7:11464 | Q6:385920, Q7:302400 |
| S1-p0 | 1 | Q6:31854, Q7:17867 | 49721 | Q6:31854, Q7:17867 | Q6:280960, Q7:419200 |
| sw01-p2 | 1 | Q6:0, Q7:59912 | 59912 | Q7:59912 | Q6:162240, Q7:621440 |
| sw02-p4 | 1 | Q6:27069, Q7:15592 | 42660 | Q6:27069, Q7:15592 | Q6:231040, Q7:410880 |
| sw03-p4 | 1 | Q6:0, Q7:52318 | 52318 | Q7:52318 | Q6:162240, Q7:625280 |
| sw04-p5 | 1 | Q6:23003, Q7:13606 | 36609 | Q6:23003, Q7:13606 | Q6:239040, Q7:427520 |
| sw05-p5 | 1 | Q6:0, Q7:45687 | 45687 | Q7:45687 | Q6:162240, Q7:625280 |
| sw06-p4 | 1 | Q6:19547, Q7:11874 | 31421 | Q6:19547, Q7:11874 | Q6:272320, Q7:419200 |
| sw07-p4 | 1 | Q6:0, Q7:39896 | 39896 | Q7:39896 | Q6:162240, Q7:625280 |
| sw08-p5 | 1 | Q6:0, Q7:34839 | 34839 | Q7:34839 | Q6:162240, Q7:625280 |

Total applied: **13273920 ns** across 20 port(s). Network total slack now banked: **13464320 ns**. GCL_size overflow: 0.

## Per-port GCL entries: before (SMT) vs. after (heuristic-enlarged)

| port | SMT entries | enlarged entries | GCL_size |
|---|---|---|---|
| sw01-p2 | 3 | 11 | 255 |
| sw01-p4 | 23 | 15 | 255 |
| sw02-p2 | 15 | 26 | 255 |
| sw02-p4 | 17 | 24 | 255 |
| sw03-p4 | 3 | 10 | 255 |
| sw03-p5 | 23 | 15 | 255 |
| sw04-p4 | 15 | 24 | 255 |
| sw04-p5 | 17 | 24 | 255 |
| sw05-p4 | 23 | 15 | 255 |
| sw05-p5 | 3 | 10 | 255 |
| sw06-p4 | 17 | 24 | 255 |
| sw06-p5 | 15 | 24 | 255 |
| sw07-p4 | 3 | 10 | 255 |
| sw07-p5 | 23 | 15 | 255 |
| sw08-p2 | 35 | 25 | 255 |
| sw08-p4 | 15 | 23 | 255 |
| sw08-p5 | 3 | 10 | 255 |

## Flows

| flow | route | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|
| s0(id=1 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 7 | 0 | 45840 | yes |
| s1(id=2 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 7 | 0 | 58640 | yes |
| s2(id=3 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 6 | 24960 | 46480 | yes |
| s3(id=4 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | - | - | - | no |
| s4(id=5 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | 6 | 0 | 36880 | yes |
| s5(id=6 S3->S1) | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | - | - | - | no |
| s6(id=7 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | 6 | 37440 | 39440 | yes |
| s7(id=8 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 7 | 24960 | 59280 | yes |
| s8(id=9 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 6 | 74880 | 38160 | yes |
| s9(id=10 S3->S1) | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | 7 | 49920 | 66320 | yes |
| s10(id=11 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | - | - | - | no |
| s11(id=12 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | - | - | - | no |
| s12(id=13 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | - | - | - | no |
| s13(id=14 S3->S1) | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | - | - | - | no |
| s14(id=15 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | - | - | - | no |
| s15(id=16 S3->S1) | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | - | - | - | no |
| s16(id=17 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | - | - | - | no |
| s17(id=18 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 7 | 62400 | 54160 | yes |
| s18(id=19 S3->S1) | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | - | - | - | no |
| s19(id=20 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 6 | 49920 | 47120 | yes |

## Per-hop windows (slack_ns > 0 means this window was enlarged)

| flow | egress port | queue | psi (ns) | delta (ns) |
|---|---|---|---|---|
| s0(id=1 S1->S2) | S1-p0 | Q7 | 0 | 12480 |
| s0(id=1 S1->S2) | sw02-p4 | Q7 | 8320 | 12480 |
| s0(id=1 S1->S2) | sw04-p5 | Q7 | 16640 | 12480 |
| s0(id=1 S1->S2) | sw06-p4 | Q7 | 24960 | 12480 |
| s0(id=1 S1->S2) | sw08-p2 | Q7 | 33280 | 12480 |
| s1(id=2 S3->S2) | S3-p0 | Q7 | 0 | 12480 |
| s1(id=2 S3->S2) | sw01-p4 | Q7 | 15360 | 12480 |
| s1(id=2 S3->S2) | sw03-p5 | Q7 | 23040 | 12480 |
| s1(id=2 S3->S2) | sw05-p4 | Q7 | 30720 | 12480 |
| s1(id=2 S3->S2) | sw07-p5 | Q7 | 38400 | 12480 |
| s1(id=2 S3->S2) | sw08-p2 | Q7 | 46080 | 12480 |
| s2(id=3 S1->S2) | S1-p0 | Q6 | 24960 | 12480 |
| s2(id=3 S1->S2) | sw02-p4 | Q6 | 33280 | 12480 |
| s2(id=3 S1->S2) | sw04-p5 | Q6 | 41600 | 12480 |
| s2(id=3 S1->S2) | sw06-p4 | Q6 | 49920 | 12480 |
| s2(id=3 S1->S2) | sw08-p2 | Q6 | 58880 | 12480 |
| s4(id=5 S2->S1) | S2-p0 | Q6 | 0 | 12480 |
| s4(id=5 S2->S1) | sw08-p4 | Q6 | 6080 | 12480 |
| s4(id=5 S2->S1) | sw06-p5 | Q6 | 12160 | 12480 |
| s4(id=5 S2->S1) | sw04-p4 | Q6 | 18240 | 12480 |
| s4(id=5 S2->S1) | sw02-p2 | Q6 | 24320 | 12480 |
| s6(id=7 S2->S1) | S2-p0 | Q6 | 37440 | 12480 |
| s6(id=7 S2->S1) | sw08-p4 | Q6 | 44160 | 12480 |
| s6(id=7 S2->S1) | sw06-p5 | Q6 | 50880 | 12480 |
| s6(id=7 S2->S1) | sw04-p4 | Q6 | 57600 | 12480 |
| s6(id=7 S2->S1) | sw02-p2 | Q6 | 64320 | 12480 |
| s7(id=8 S3->S2) | S3-p0 | Q7 | 24960 | 12480 |
| s7(id=8 S3->S2) | sw01-p4 | Q7 | 35200 | 12480 |
| s7(id=8 S3->S2) | sw03-p5 | Q7 | 43520 | 12480 |
| s7(id=8 S3->S2) | sw05-p4 | Q7 | 51840 | 12480 |
| s7(id=8 S3->S2) | sw07-p5 | Q7 | 60160 | 12480 |
| s7(id=8 S3->S2) | sw08-p2 | Q7 | 71680 | 12480 |
| s8(id=9 S3->S2) | S3-p0 | Q6 | 74880 | 12480 |
| s8(id=9 S3->S2) | sw01-p4 | Q6 | 80000 | 12480 |
| s8(id=9 S3->S2) | sw03-p5 | Q6 | 85120 | 12480 |
| s8(id=9 S3->S2) | sw05-p4 | Q6 | 90240 | 12480 |
| s8(id=9 S3->S2) | sw07-p5 | Q6 | 95360 | 12480 |
| s8(id=9 S3->S2) | sw08-p2 | Q6 | 100480 | 12480 |
| s9(id=10 S3->S1) | S3-p0 | Q7 | 49920 | 12480 |
| s9(id=10 S3->S1) | sw01-p4 | Q7 | 56640 | 12480 |
| s9(id=10 S3->S1) | sw03-p5 | Q7 | 63360 | 12480 |
| s9(id=10 S3->S1) | sw05-p4 | Q7 | 70080 | 12480 |
| s9(id=10 S3->S1) | sw07-p5 | Q7 | 76800 | 12480 |
| s9(id=10 S3->S1) | sw08-p4 | Q7 | 83520 | 12480 |
| s9(id=10 S3->S1) | sw06-p5 | Q7 | 90240 | 12480 |
| s9(id=10 S3->S1) | sw04-p4 | Q7 | 96960 | 12480 |
| s9(id=10 S3->S1) | sw02-p2 | Q7 | 103680 | 12480 |
| s17(id=18 S2->S3) | S2-p0 | Q7 | 62400 | 12480 |
| s17(id=18 S2->S3) | sw08-p5 | Q7 | 70720 | 12480 |
| s17(id=18 S2->S3) | sw07-p4 | Q7 | 79040 | 12480 |
| s17(id=18 S2->S3) | sw05-p5 | Q7 | 87360 | 12480 |
| s17(id=18 S2->S3) | sw03-p4 | Q7 | 95680 | 12480 |
| s17(id=18 S2->S3) | sw01-p2 | Q7 | 104000 | 12480 |
| s19(id=20 S1->S2) | S1-p0 | Q6 | 49920 | 12480 |
| s19(id=20 S1->S2) | sw02-p4 | Q6 | 58240 | 12480 |
| s19(id=20 S1->S2) | sw04-p5 | Q6 | 66560 | 12480 |
| s19(id=20 S1->S2) | sw06-p4 | Q6 | 74880 | 12480 |
| s19(id=20 S1->S2) | sw08-p2 | Q6 | 84480 | 12480 |

## Constraint check

- C1-C7, C9: OK
- seed-integrity (no SMT-fixed flow's placement changed): OK

## GCL per egress port

### sw01-p2  (11 entries, util 1.5600 %)

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

### sw01-p4  (15 entries, util 17.1600 %)

```
sgs 15360 0x7F # 01111111   Q6
sgs 53760 0x80 # 10000000   Q7
sgs 10880 0x3F # 00111111   BE
sgs 80320 0x40 # 01000000   Q6
sgs 39680 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 144960 0x80 # 10000000   Q7
sgs 39680 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 144960 0x80 # 10000000   Q7
sgs 39680 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 129600 0x80 # 10000000   Q7
sgs 5120 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (26 entries, util 10.9200 %)

```
sgs 24320 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 13120 0x7F # 01111111   Q6
sgs 14400 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 23360 0xBF # 10111111   Q7
sgs 3520 0x3F # 00111111   BE
sgs 31680 0x80 # 10000000   Q7
sgs 14720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 24320 0x7F # 01111111   Q6
sgs 111040 0x40 # 01000000   Q6
sgs 14720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 24320 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 13120 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 3520 0x3F # 00111111   BE
sgs 31680 0x80 # 10000000   Q7
sgs 14720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 24320 0x7F # 01111111   Q6
sgs 86720 0x40 # 01000000   Q6
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p4  (24 entries, util 12.4800 %)

```
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 72320 0x40 # 01000000   Q6
sgs 19520 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 8320 0x3F # 00111111   BE
sgs 122240 0x80 # 10000000   Q7
sgs 19520 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 72320 0x40 # 01000000   Q6
sgs 19520 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 8320 0x3F # 00111111   BE
sgs 113920 0x80 # 10000000   Q7
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (10 entries, util 1.5600 %)

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

### sw03-p5  (15 entries, util 17.1600 %)

```
sgs 23040 0x7F # 01111111   Q6
sgs 52800 0x80 # 10000000   Q7
sgs 9280 0x3F # 00111111   BE
sgs 82880 0x40 # 01000000   Q6
sgs 32000 0xBF # 10111111   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 144960 0x80 # 10000000   Q7
sgs 32000 0xBF # 10111111   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 144960 0x80 # 10000000   Q7
sgs 32000 0xBF # 10111111   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 121920 0x80 # 10000000   Q7
sgs 5120 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p4  (24 entries, util 10.9200 %)

```
sgs 18240 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 19200 0x7F # 01111111   Q6
sgs 7680 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 26880 0xBF # 10111111   Q7
sgs 32320 0x80 # 10000000   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 18240 0x7F # 01111111   Q6
sgs 111040 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 18240 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 19200 0x7F # 01111111   Q6
sgs 47040 0xBF # 10111111   Q7
sgs 32320 0x80 # 10000000   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 18240 0x7F # 01111111   Q6
sgs 92800 0x40 # 01000000   Q6
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (24 entries, util 12.4800 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 72320 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 122240 0x80 # 10000000   Q7
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 72320 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 105600 0x80 # 10000000   Q7
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (15 entries, util 17.1600 %)

```
sgs 30720 0x7F # 01111111   Q6
sgs 51840 0x80 # 10000000   Q7
sgs 7680 0x3F # 00111111   BE
sgs 85440 0x40 # 01000000   Q6
sgs 24320 0xBF # 10111111   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 144960 0x80 # 10000000   Q7
sgs 24320 0xBF # 10111111   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 144960 0x80 # 10000000   Q7
sgs 24320 0xBF # 10111111   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 114240 0x80 # 10000000   Q7
sgs 5120 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p5  (10 entries, util 1.5600 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 37440 0xBF # 10111111   Q7
sgs 450240 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p4  (24 entries, util 12.4800 %)

```
sgs 24960 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 72320 0x40 # 01000000   Q6
sgs 2880 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 122240 0x80 # 10000000   Q7
sgs 2880 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 72320 0x40 # 01000000   Q6
sgs 2880 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 97280 0x80 # 10000000   Q7
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (24 entries, util 10.9200 %)

```
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 25280 0x7F # 01111111   Q6
sgs 960 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 26880 0xBF # 10111111   Q7
sgs 32960 0x80 # 10000000   Q7
sgs 26880 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 12160 0x3F # 00111111   BE
sgs 111040 0x40 # 01000000   Q6
sgs 26880 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 25280 0x7F # 01111111   Q6
sgs 40320 0xBF # 10111111   Q7
sgs 32960 0x80 # 10000000   Q7
sgs 26880 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 12160 0x3F # 00111111   BE
sgs 98880 0x40 # 01000000   Q6
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (10 entries, util 1.5600 %)

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

### sw07-p5  (15 entries, util 17.1600 %)

```
sgs 38400 0x7F # 01111111   Q6
sgs 50880 0x80 # 10000000   Q7
sgs 6080 0x3F # 00111111   BE
sgs 88000 0x40 # 01000000   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 38400 0x7F # 01111111   Q6
sgs 144960 0x80 # 10000000   Q7
sgs 16640 0xBF # 10111111   Q7
sgs 38400 0x7F # 01111111   Q6
sgs 144960 0x80 # 10000000   Q7
sgs 16640 0xBF # 10111111   Q7
sgs 38400 0x7F # 01111111   Q6
sgs 106560 0x80 # 10000000   Q7
sgs 5120 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p2  (25 entries, util 26.5200 %)

```
sgs 33280 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 116160 0x40 # 01000000   Q6
sgs 32640 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 13120 0x3F # 00111111   BE
sgs 13440 0x80 # 10000000   Q7
sgs 148160 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 36800 0x40 # 01000000   Q6
sgs 112000 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 13120 0x3F # 00111111   BE
sgs 13440 0x80 # 10000000   Q7
sgs 114880 0x3F # 00111111   BE
```

### sw08-p4  (23 entries, util 10.9200 %)

```
sgs 6080 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 25600 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 26880 0xBF # 10111111   Q7
sgs 33600 0x80 # 10000000   Q7
sgs 32960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 6080 0x3F # 00111111   BE
sgs 111040 0x40 # 01000000   Q6
sgs 32960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 6080 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 31360 0x7F # 01111111   Q6
sgs 33600 0xBF # 10111111   Q7
sgs 33600 0x80 # 10000000   Q7
sgs 32960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 6080 0x3F # 00111111   BE
sgs 104960 0x40 # 01000000   Q6
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (10 entries, util 1.5600 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 20800 0xBF # 10111111   Q7
sgs 466880 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

