# Heuristic-enlarged GCL schedule (Problem 2: window enlargement)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Time-sensitive PCPs considered: [6, 7]
- Seeded from SMT run: **result/result-2026-10-12-dataset-testbed-8-ring-avgwin/smt-c9-on/8-fair-retimed-c9on**

## Admission (unchanged by this package -- it only widens windows)

SMT-fixed flows: **10**/10. This package never admits a flow itself; it banks slack for a later admission pass (`prob_3_admit`, Problem 3) to use.

## Opportunistic idle top-up (Step 7 -- see enlarge.py)

Total: **11659520 ns**, drawn from idle capacity on ports at or below utilisation 0.2, independent of any route's deadline-slack budget.

| port | queue | applied (ns) |
|---|---|---|
| S1-p0 | Q6 | 119680 |
| S1-p0 | Q7 | 412800 |
| S2-p0 | Q6 | 85760 |
| S2-p0 | Q7 | 554560 |
| S3-p0 | Q6 | 332800 |
| S3-p0 | Q7 | 257280 |
| sw01-p2 | Q6 | 59200 |
| sw01-p2 | Q7 | 487040 |
| sw01-p5 | Q6 | 343360 |
| sw01-p5 | Q7 | 272320 |
| sw02-p2 | Q7 | 561920 |
| sw02-p4 | Q7 | 694400 |
| sw02-p5 | Q6 | 533120 |
| sw02-p5 | Q7 | 110400 |
| sw03-p4 | Q6 | 81600 |
| sw03-p4 | Q7 | 576320 |
| sw04-p4 | Q7 | 688000 |
| sw04-p5 | Q7 | 687360 |
| sw05-p5 | Q6 | 88640 |
| sw05-p5 | Q7 | 579200 |
| sw06-p4 | Q7 | 680000 |
| sw06-p5 | Q7 | 696320 |
| sw07-p4 | Q6 | 95040 |
| sw07-p4 | Q7 | 582080 |
| sw08-p2 | Q7 | 672640 |
| sw08-p4 | Q7 | 711680 |
| sw08-p5 | Q6 | 91520 |
| sw08-p5 | Q7 | 604480 |

## Opportunistic window creation (Step 8 -- see enlarge.py)

**15** brand-new window(s) opened, **187200 ns** total, on ports at or below utilisation 0.2 whose TT queue had zero windows before this run.

| port | queue | size (ns) |
|---|---|---|
| sw01-p4 | Q6 | 12480 |
| sw01-p4 | Q7 | 12480 |
| sw02-p4 | Q6 | 12480 |
| sw03-p5 | Q6 | 12480 |
| sw03-p5 | Q7 | 12480 |
| sw04-p4 | Q6 | 12480 |
| sw04-p5 | Q6 | 12480 |
| sw05-p4 | Q6 | 12480 |
| sw05-p4 | Q7 | 12480 |
| sw06-p4 | Q6 | 12480 |
| sw06-p5 | Q6 | 12480 |
| sw07-p5 | Q6 | 12480 |
| sw07-p5 | Q7 | 12480 |
| sw08-p2 | Q6 | 12480 |
| sw08-p4 | Q6 | 12480 |

## Best-effort gap equalization (Step 9 -- see enlarge.py)

**7537600 ns** given back from Steps 7/8's growth so each port's leftover non-TAS gaps land close to equal, instead of one gap staying huge while a neighbour is squeezed to the bare 1-tick C10 minimum.

| port | given back (ns) |
|---|---|
| sw03-p4 | 543680 |
| sw08-p5 | 543680 |
| sw05-p5 | 541120 |
| sw07-p4 | 537920 |
| sw02-p4 | 499200 |
| sw04-p5 | 499200 |
| sw06-p4 | 499200 |
| sw08-p2 | 491200 |
| sw02-p5 | 444800 |
| S2-p0 | 418240 |
| sw04-p4 | 387200 |
| sw06-p5 | 387200 |
| sw08-p4 | 387200 |
| S1-p0 | 307520 |
| sw01-p5 | 286720 |
| S3-p0 | 283200 |
| sw01-p2 | 266240 |
| sw02-p2 | 214080 |

## Opportunistic overlay window creation (Step 10 -- see enlarge.py)

**44** new overlay window(s), **10953600 ns** total, carved out of already-open best-effort spans on ports at or below utilisation 0.2 -- best-effort stays reachable inside each one (gate mask keeps its BE bits set), so none of this is closed off from BE.

| port | queue | size (ns) |
|---|---|---|
| S1-p0 | Q6 | 99840 |
| S1-p0 | Q7 | 215040 |
| S2-p0 | Q6 | 206080 |
| S2-p0 | Q7 | 212160 |
| S3-p0 | Q6 | 149760 |
| S3-p0 | Q7 | 135360 |
| sw01-p2 | Q6 | 90880 |
| sw01-p2 | Q7 | 183360 |
| sw01-p4 | Q6 | 374400 |
| sw01-p4 | Q7 | 400640 |
| sw01-p5 | Q6 | 165120 |
| sw01-p5 | Q7 | 122880 |
| sw02-p2 | Q6 | 130240 |
| sw02-p2 | Q7 | 99840 |
| sw02-p4 | Q6 | 307840 |
| sw02-p4 | Q7 | 224640 |
| sw02-p5 | Q6 | 213440 |
| sw02-p5 | Q7 | 238080 |
| sw03-p4 | Q6 | 298560 |
| sw03-p4 | Q7 | 268480 |
| sw03-p5 | Q6 | 374400 |
| sw03-p5 | Q7 | 400640 |
| sw04-p4 | Q6 | 230720 |
| sw04-p4 | Q7 | 183360 |
| sw04-p5 | Q6 | 299520 |
| sw04-p5 | Q7 | 224640 |
| sw05-p4 | Q6 | 374400 |
| sw05-p4 | Q7 | 400640 |
| sw05-p5 | Q6 | 294080 |
| sw05-p5 | Q7 | 260160 |
| sw06-p4 | Q6 | 274560 |
| sw06-p4 | Q7 | 274560 |
| sw06-p5 | Q6 | 230720 |
| sw06-p5 | Q7 | 188480 |
| sw07-p4 | Q6 | 297600 |
| sw07-p4 | Q7 | 251840 |
| sw07-p5 | Q6 | 374400 |
| sw07-p5 | Q7 | 400640 |
| sw08-p2 | Q6 | 237120 |
| sw08-p2 | Q7 | 299840 |
| sw08-p4 | Q6 | 216000 |
| sw08-p4 | Q7 | 200320 |
| sw08-p5 | Q6 | 232000 |
| sw08-p5 | Q7 | 296320 |

## Candidate routes (P^cand = routes of the fixed flows above)

| route | PCPs carried | flows |
|---|---|---|
| S1->sw02->sw01->S3 | Q6 (2), Q7 (1) | 3 |
| S1->sw02->sw04->sw06->sw08->S2 | Q7 (1) | 1 |
| S2->sw08->sw06->sw04->sw02->S1 | Q7 (1) | 1 |
| S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 (1), Q7 (1) | 2 |
| S3->sw01->sw02->S1 | Q6 (2), Q7 (1) | 3 |

## Per-link enlargement accounting

| link | sharing eta | route-safe slack (ns) | link budget (ns) | final slack (ns) | applied (ns) |
|---|---|---|---|---|---|
| S1-p0 | 2 | Q6:60324, Q7:74960 | 135283 | Q6:42894, Q7:74960 | Q6:157440, Q7:500160 |
| S2-p0 | 2 | Q6:89528, Q7:33271 | 122799 | Q6:39537, Q7:33271 | Q6:242240, Q7:470400 |
| sw01-p2 | 2 | Q6:50527, Q7:39290 | 89817 | Q6:42550, Q7:39290 | Q6:140800, Q7:494720 |
| sw02-p2 | 2 | Q6:169886, Q7:92312 | 262199 | Q6:165044, Q7:92312 | Q6:130240, Q7:575680 |
| S3-p0 | 1 | Q6:54937, Q7:146219 | 201156 | Q6:54937, Q7:80370 | Q6:376960, Q7:350080 |
| sw01-p5 | 1 | Q6:40011, Q7:114737 | 154748 | Q6:40011, Q7:64617 | Q6:384640, Q7:336640 |
| sw02-p4 | 1 | Q6:0, Q7:10172 | 10172 | Q7:10172 | Q6:320320, Q7:429760 |
| sw02-p5 | 1 | Q6:15079, Q7:49608 | 64687 | Q6:15079, Q7:36756 | Q6:416640, Q7:285120 |
| sw03-p4 | 1 | Q6:57234, Q7:8925 | 66159 | Q6:40745, Q7:8925 | Q6:298560, Q7:432000 |
| sw04-p4 | 1 | Q6:0, Q7:26649 | 26649 | Q7:26649 | Q6:243200, Q7:510720 |
| sw04-p5 | 1 | Q6:0, Q7:8866 | 8866 | Q7:8866 | Q6:312000, Q7:421440 |
| sw05-p5 | 1 | Q6:51769, Q7:7921 | 59690 | Q6:37028, Q7:7921 | Q6:296640, Q7:428800 |
| sw06-p4 | 1 | Q6:0, Q7:7727 | 7727 | Q7:7727 | Q6:287040, Q7:463040 |
| sw06-p5 | 1 | Q6:0, Q7:23611 | 23611 | Q7:23611 | Q6:243200, Q7:520960 |
| sw07-p4 | 1 | Q6:46826, Q7:7030 | 53856 | Q6:33648, Q7:7030 | Q6:303360, Q7:425600 |
| sw08-p2 | 1 | Q6:0, Q7:6735 | 6735 | Q7:6735 | Q6:249600, Q7:488000 |
| sw08-p4 | 1 | Q6:0, Q7:20918 | 20918 | Q7:20918 | Q6:228480, Q7:545600 |
| sw08-p5 | 1 | Q6:42354, Q7:6240 | 48594 | Q6:30576, Q7:6240 | Q6:232000, Q7:485120 |

Total applied: **16227200 ns** across 22 port(s). Network total slack now banked: **16227840 ns**. GCL_size overflow: 0.

## Per-port GCL entries: before (SMT) vs. after (heuristic-enlarged)

| port | SMT entries | enlarged entries | GCL_size |
|---|---|---|---|
| sw01-p2 | 25 | 28 | 255 |
| sw01-p4 | 1 | 18 | 255 |
| sw01-p5 | 11 | 16 | 255 |
| sw02-p2 | 15 | 18 | 255 |
| sw02-p4 | 9 | 18 | 255 |
| sw02-p5 | 15 | 24 | 255 |
| sw03-p4 | 11 | 20 | 255 |
| sw03-p5 | 1 | 18 | 255 |
| sw04-p4 | 5 | 14 | 255 |
| sw04-p5 | 9 | 22 | 255 |
| sw05-p4 | 1 | 18 | 255 |
| sw05-p5 | 11 | 20 | 255 |
| sw06-p4 | 9 | 22 | 255 |
| sw06-p5 | 5 | 14 | 255 |
| sw07-p4 | 11 | 23 | 255 |
| sw07-p5 | 1 | 18 | 255 |
| sw08-p2 | 9 | 22 | 255 |
| sw08-p4 | 5 | 13 | 255 |
| sw08-p5 | 11 | 23 | 255 |

## Flows

| flow | route | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|
| s0(id=1 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | - | - | - | no |
| s1(id=2 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | 7 | 37440 | 40720 | yes |
| s2(id=3 S3->S1) | S3->sw01->sw02->S1 | - | - | - | no |
| s3(id=4 S1->S3) | S1->sw02->sw01->S3 | - | - | - | no |
| s4(id=5 S1->S3) | S1->sw02->sw01->S3 | 6 | 87360 | 22800 | yes |
| s5(id=6 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 7 | 0 | 48080 | yes |
| s6(id=7 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | - | - | - | no |
| s7(id=8 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | - | - | - | no |
| s8(id=9 S3->S1) | S3->sw01->sw02->S1 | 6 | 12480 | 22800 | yes |
| s9(id=10 S1->S3) | S1->sw02->sw01->S3 | 6 | 12480 | 22800 | yes |
| s10(id=11 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | - | - | - | no |
| s11(id=12 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 6 | 62400 | 60560 | yes |
| s12(id=13 S3->S1) | S3->sw01->sw02->S1 | 7 | 62400 | 28560 | yes |
| s13(id=14 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | - | - | - | no |
| s14(id=15 S3->S1) | S3->sw01->sw02->S1 | - | - | - | no |
| s15(id=16 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | - | - | - | no |
| s16(id=17 S1->S3) | S1->sw02->sw01->S3 | - | - | - | no |
| s17(id=18 S3->S1) | S3->sw01->sw02->S1 | 6 | 37440 | 27920 | yes |
| s18(id=19 S1->S3) | S1->sw02->sw01->S3 | 7 | 62400 | 26000 | yes |
| s19(id=20 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 7 | 37440 | 45840 | yes |

## Per-hop windows (slack_ns > 0 means this window was enlarged)

| flow | egress port | queue | psi (ns) | delta (ns) |
|---|---|---|---|---|
| s1(id=2 S2->S1) | S2-p0 | Q7 | 37440 | 12480 |
| s1(id=2 S2->S1) | sw08-p4 | Q7 | 42560 | 12480 |
| s1(id=2 S2->S1) | sw06-p5 | Q7 | 55360 | 12480 |
| s1(id=2 S2->S1) | sw04-p4 | Q7 | 60480 | 12480 |
| s1(id=2 S2->S1) | sw02-p2 | Q7 | 65600 | 12480 |
| s4(id=5 S1->S3) | S1-p0 | Q6 | 87360 | 12480 |
| s4(id=5 S1->S3) | sw02-p5 | Q6 | 92480 | 12480 |
| s4(id=5 S1->S3) | sw01-p2 | Q6 | 97600 | 12480 |
| s5(id=6 S2->S3) | S2-p0 | Q7 | 0 | 12480 |
| s5(id=6 S2->S3) | sw08-p5 | Q7 | 5120 | 12480 |
| s5(id=6 S2->S3) | sw07-p4 | Q7 | 20160 | 12480 |
| s5(id=6 S2->S3) | sw05-p5 | Q7 | 25280 | 12480 |
| s5(id=6 S2->S3) | sw03-p4 | Q7 | 30400 | 12480 |
| s5(id=6 S2->S3) | sw01-p2 | Q7 | 35520 | 12480 |
| s8(id=9 S3->S1) | S3-p0 | Q6 | 12480 | 12480 |
| s8(id=9 S3->S1) | sw01-p5 | Q6 | 17600 | 12480 |
| s8(id=9 S3->S1) | sw02-p2 | Q6 | 22720 | 12480 |
| s9(id=10 S1->S3) | S1-p0 | Q6 | 12480 | 12480 |
| s9(id=10 S1->S3) | sw02-p5 | Q6 | 17600 | 12480 |
| s9(id=10 S1->S3) | sw01-p2 | Q6 | 22720 | 12480 |
| s11(id=12 S2->S3) | S2-p0 | Q6 | 62400 | 12480 |
| s11(id=12 S2->S3) | sw08-p5 | Q6 | 70720 | 12480 |
| s11(id=12 S2->S3) | sw07-p4 | Q6 | 79040 | 12480 |
| s11(id=12 S2->S3) | sw05-p5 | Q6 | 87360 | 12480 |
| s11(id=12 S2->S3) | sw03-p4 | Q6 | 95680 | 12480 |
| s11(id=12 S2->S3) | sw01-p2 | Q6 | 110400 | 12480 |
| s12(id=13 S3->S1) | S3-p0 | Q7 | 62400 | 12480 |
| s12(id=13 S3->S1) | sw01-p5 | Q7 | 68480 | 12480 |
| s12(id=13 S3->S1) | sw02-p2 | Q7 | 78400 | 12480 |
| s17(id=18 S3->S1) | S3-p0 | Q6 | 37440 | 12480 |
| s17(id=18 S3->S1) | sw01-p5 | Q6 | 45120 | 12480 |
| s17(id=18 S3->S1) | sw02-p2 | Q6 | 52800 | 12480 |
| s18(id=19 S1->S3) | S1-p0 | Q7 | 62400 | 12480 |
| s18(id=19 S1->S3) | sw02-p5 | Q7 | 69120 | 12480 |
| s18(id=19 S1->S3) | sw01-p2 | Q7 | 75840 | 12480 |
| s19(id=20 S1->S2) | S1-p0 | Q7 | 37440 | 12480 |
| s19(id=20 S1->S2) | sw02-p4 | Q7 | 45760 | 12480 |
| s19(id=20 S1->S2) | sw04-p5 | Q7 | 54080 | 12480 |
| s19(id=20 S1->S2) | sw06-p4 | Q7 | 62400 | 12480 |
| s19(id=20 S1->S2) | sw08-p2 | Q7 | 70720 | 12480 |

## Constraint check

- C1-C7, C9: OK
- seed-integrity (no SMT-fixed flow's placement changed): OK

## GCL per egress port

### sw01-p2  (28 entries, util 18.7200 %)

```
sgs 22720 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 1920 0x3F # 00111111   BE
sgs 25920 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 9280 0x3F # 00111111   BE
sgs 75200 0x40 # 01000000   Q6
sgs 27200 0xBF # 10111111   Q7
sgs 22720 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 137280 0x80 # 10000000   Q7
sgs 27200 0xBF # 10111111   Q7
sgs 22720 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 1920 0x3F # 00111111   BE
sgs 25920 0xBF # 10111111   Q7
sgs 96960 0x80 # 10000000   Q7
sgs 27200 0xBF # 10111111   Q7
sgs 22720 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 114560 0x80 # 10000000   Q7
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

### sw01-p5  (16 entries, util 7.8000 %)

```
sgs 17600 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 15040 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 10880 0x3F # 00111111   BE
sgs 226240 0x80 # 10000000   Q7
sgs 5440 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 17600 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 15040 0x7F # 01111111   Q6
sgs 232000 0x40 # 01000000   Q6
sgs 23040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (18 entries, util 10.9200 %)

```
sgs 22720 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 14720 0x7F # 01111111   Q6
sgs 2880 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 268160 0x80 # 10000000   Q7
sgs 16320 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 22720 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 14720 0x7F # 01111111   Q6
sgs 2880 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 245440 0x80 # 10000000   Q7
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p4  (18 entries, util 6.2400 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 33280 0x7F # 01111111   Q6
sgs 75200 0x80 # 10000000   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 45760 0x7F # 01111111   Q6
sgs 75200 0x80 # 10000000   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 45760 0x7F # 01111111   Q6
sgs 75200 0x80 # 10000000   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 45760 0x7F # 01111111   Q6
sgs 29440 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p5  (24 entries, util 10.9200 %)

```
sgs 17600 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 19840 0x7F # 01111111   Q6
sgs 19200 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 10880 0x3F # 00111111   BE
sgs 36160 0x40 # 01000000   Q6
sgs 21440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 17600 0x7F # 01111111   Q6
sgs 111040 0x40 # 01000000   Q6
sgs 21440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 17600 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 19840 0x7F # 01111111   Q6
sgs 19200 0xBF # 10111111   Q7
sgs 59520 0x80 # 10000000   Q7
sgs 21440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 17600 0x7F # 01111111   Q6
sgs 93440 0x40 # 01000000   Q6
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (20 entries, util 7.8000 %)

```
sgs 30400 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 7040 0x3F # 00111111   BE
sgs 45760 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 41920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 30400 0x7F # 01111111   Q6
sgs 77120 0x80 # 10000000   Q7
sgs 42560 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 30400 0x7F # 01111111   Q6
sgs 77120 0x80 # 10000000   Q7
sgs 42560 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 30400 0x7F # 01111111   Q6
sgs 46720 0x80 # 10000000   Q7
sgs 23040 0xBF # 10111111   Q7
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
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 10560 0x3F # 00111111   BE
sgs 206400 0x80 # 10000000   Q7
sgs 33280 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 10560 0x3F # 00111111   BE
sgs 145920 0x80 # 10000000   Q7
sgs 43520 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (22 entries, util 6.2400 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 4160 0x3F # 00111111   BE
sgs 75200 0x80 # 10000000   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 4160 0x3F # 00111111   BE
sgs 75200 0x80 # 10000000   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 4160 0x3F # 00111111   BE
sgs 75200 0x80 # 10000000   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 4160 0x3F # 00111111   BE
sgs 21120 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
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
sgs 25280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12160 0x3F # 00111111   BE
sgs 37440 0xBF # 10111111   Q7
sgs 15040 0x40 # 01000000   Q6
sgs 47680 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 25280 0x7F # 01111111   Q6
sgs 77120 0x80 # 10000000   Q7
sgs 47680 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 25280 0x7F # 01111111   Q6
sgs 77120 0x80 # 10000000   Q7
sgs 47680 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 25280 0x7F # 01111111   Q6
sgs 51840 0x80 # 10000000   Q7
sgs 23040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p4  (22 entries, util 6.2400 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 75200 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 75200 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 75200 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12800 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (14 entries, util 3.1200 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 5440 0x3F # 00111111   BE
sgs 206400 0x80 # 10000000   Q7
sgs 38400 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 5440 0x3F # 00111111   BE
sgs 151040 0x80 # 10000000   Q7
sgs 43520 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (23 entries, util 7.8000 %)

```
sgs 20160 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 17280 0x7F # 01111111   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 18240 0x40 # 01000000   Q6
sgs 2880 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 77120 0x80 # 10000000   Q7
sgs 2880 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 77120 0x80 # 10000000   Q7
sgs 2880 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 56960 0x80 # 10000000   Q7
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
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 20800 0xBF # 10111111   Q7
sgs 75200 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 20800 0xBF # 10111111   Q7
sgs 75200 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 20800 0xBF # 10111111   Q7
sgs 75200 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 20800 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 16960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p4  (13 entries, util 3.1200 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 30080 0x7F # 01111111   Q6
sgs 206400 0x80 # 10000000   Q7
sgs 960 0x3F # 00111111   BE
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 42560 0x7F # 01111111   Q6
sgs 163840 0x80 # 10000000   Q7
sgs 43520 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (23 entries, util 7.8000 %)

```
sgs 5120 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 32320 0x7F # 01111111   Q6
sgs 20800 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 16960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 5120 0x3F # 00111111   BE
sgs 77120 0x80 # 10000000   Q7
sgs 17920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 5120 0x3F # 00111111   BE
sgs 77120 0x80 # 10000000   Q7
sgs 17920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 5120 0x3F # 00111111   BE
sgs 72000 0x80 # 10000000   Q7
sgs 23040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

