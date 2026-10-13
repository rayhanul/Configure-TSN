# Heuristic-enlarged GCL schedule (Problem 2: window enlargement)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Time-sensitive PCPs considered: [6, 7]
- Seeded from SMT run: **result/result-2026-10-12-dataset-testbed-9-ring-avgwin/smt-c9-on/9-fair-retimed-c9on**

## Admission (unchanged by this package -- it only widens windows)

SMT-fixed flows: **11**/11. This package never admits a flow itself; it banks slack for a later admission pass (`prob_3_admit`, Problem 3) to use.

## Opportunistic idle top-up (Step 7 -- see enlarge.py)

Total: **14470720 ns**, drawn from idle capacity on ports at or below utilisation 0.2, independent of any route's deadline-slack budget.

| port | queue | applied (ns) |
|---|---|---|
| S1-p0 | Q6 | 688000 |
| S2-p0 | Q6 | 620160 |
| S3-p0 | Q6 | 352640 |
| S3-p0 | Q7 | 156160 |
| sw01-p2 | Q6 | 649280 |
| sw01-p4 | Q7 | 641280 |
| sw01-p5 | Q6 | 522880 |
| sw01-p5 | Q7 | 136960 |
| sw02-p2 | Q6 | 537600 |
| sw02-p4 | Q6 | 687040 |
| sw02-p5 | Q6 | 723520 |
| sw03-p4 | Q6 | 708480 |
| sw03-p5 | Q7 | 637760 |
| sw04-p4 | Q6 | 668480 |
| sw04-p5 | Q6 | 689280 |
| sw05-p4 | Q7 | 633920 |
| sw05-p5 | Q6 | 714560 |
| sw06-p4 | Q6 | 690240 |
| sw06-p5 | Q6 | 677120 |
| sw07-p4 | Q6 | 720640 |
| sw07-p5 | Q7 | 629760 |
| sw08-p2 | Q7 | 573120 |
| sw08-p4 | Q6 | 685440 |
| sw08-p5 | Q6 | 726400 |

## Opportunistic window creation (Step 8 -- see enlarge.py)

**13** brand-new window(s) opened, **162240 ns** total, on ports at or below utilisation 0.2 whose TT queue had zero windows before this run.

| port | queue | size (ns) |
|---|---|---|
| sw01-p2 | Q7 | 12480 |
| sw01-p4 | Q6 | 12480 |
| sw02-p4 | Q7 | 12480 |
| sw03-p4 | Q7 | 12480 |
| sw03-p5 | Q6 | 12480 |
| sw04-p4 | Q7 | 12480 |
| sw04-p5 | Q7 | 12480 |
| sw05-p4 | Q6 | 12480 |
| sw05-p5 | Q7 | 12480 |
| sw06-p4 | Q7 | 12480 |
| sw06-p5 | Q7 | 12480 |
| sw07-p5 | Q6 | 12480 |
| sw08-p4 | Q7 | 12480 |

## Best-effort gap equalization (Step 9 -- see enlarge.py)

**7834880 ns** given back from Steps 7/8's growth so each port's leftover non-TAS gaps land close to equal, instead of one gap staying huge while a neighbour is squeezed to the bare 1-tick C10 minimum.

| port | given back (ns) |
|---|---|
| sw02-p5 | 599040 |
| sw07-p4 | 543680 |
| sw08-p5 | 543680 |
| S1-p0 | 504000 |
| sw03-p4 | 490880 |
| sw05-p5 | 490880 |
| sw01-p5 | 399680 |
| S3-p0 | 360960 |
| sw08-p2 | 325440 |
| S2-p0 | 319360 |
| sw01-p2 | 313280 |
| sw04-p4 | 288000 |
| sw06-p5 | 283840 |
| sw08-p4 | 279680 |
| sw01-p4 | 262400 |
| sw02-p4 | 262400 |
| sw03-p5 | 262400 |
| sw04-p5 | 262400 |
| sw05-p4 | 262400 |
| sw06-p4 | 262400 |
| sw07-p5 | 262400 |
| sw02-p2 | 255680 |

## Opportunistic overlay window creation (Step 10 -- see enlarge.py)

**44** new overlay window(s), **8198720 ns** total, carved out of already-open best-effort spans on ports at or below utilisation 0.2 -- best-effort stays reachable inside each one (gate mask keeps its BE bits set), so none of this is closed off from BE.

| port | queue | size (ns) |
|---|---|---|
| S1-p0 | Q6 | 212160 |
| S1-p0 | Q7 | 291840 |
| S2-p0 | Q6 | 49920 |
| S2-p0 | Q7 | 224640 |
| S3-p0 | Q6 | 148800 |
| S3-p0 | Q7 | 224640 |
| sw01-p2 | Q6 | 71680 |
| sw01-p2 | Q7 | 240320 |
| sw01-p4 | Q6 | 149760 |
| sw01-p4 | Q7 | 195840 |
| sw01-p5 | Q6 | 210880 |
| sw01-p5 | Q7 | 199680 |
| sw02-p2 | Q6 | 135360 |
| sw02-p2 | Q7 | 132800 |
| sw02-p4 | Q6 | 130880 |
| sw02-p4 | Q7 | 150080 |
| sw02-p5 | Q6 | 199680 |
| sw02-p5 | Q7 | 376320 |
| sw03-p4 | Q6 | 230080 |
| sw03-p4 | Q7 | 249920 |
| sw03-p5 | Q6 | 149760 |
| sw03-p5 | Q7 | 200320 |
| sw04-p4 | Q6 | 151040 |
| sw04-p4 | Q7 | 149120 |
| sw04-p5 | Q6 | 136960 |
| sw04-p5 | Q7 | 150080 |
| sw05-p4 | Q6 | 149760 |
| sw05-p4 | Q7 | 200320 |
| sw05-p5 | Q6 | 237760 |
| sw05-p5 | Q7 | 247680 |
| sw06-p4 | Q6 | 143040 |
| sw06-p4 | Q7 | 150080 |
| sw06-p5 | Q6 | 128000 |
| sw06-p5 | Q7 | 156800 |
| sw07-p4 | Q6 | 224320 |
| sw07-p4 | Q7 | 288640 |
| sw07-p5 | Q6 | 170240 |
| sw07-p5 | Q7 | 200320 |
| sw08-p2 | Q6 | 177920 |
| sw08-p2 | Q7 | 188480 |
| sw08-p4 | Q6 | 122880 |
| sw08-p4 | Q7 | 126720 |
| sw08-p5 | Q6 | 232000 |
| sw08-p5 | Q7 | 291200 |

## Candidate routes (P^cand = routes of the fixed flows above)

| route | PCPs carried | flows |
|---|---|---|
| S1->sw02->sw01->S3 | Q6 (1) | 1 |
| S1->sw02->sw04->sw06->sw08->S2 | Q6 (1) | 1 |
| S2->sw08->sw06->sw04->sw02->S1 | Q6 (3) | 3 |
| S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 (2) | 2 |
| S3->sw01->sw02->S1 | Q6 (2), Q7 (1) | 3 |
| S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 (1) | 1 |

## Per-link enlargement accounting

| link | sharing eta | route-safe slack (ns) | link budget (ns) | final slack (ns) | applied (ns) |
|---|---|---|---|---|---|
| S1-p0 | 2 | Q6:49703, Q7:0 | 49703 | Q6:49703 | Q6:445760, Q7:291840 |
| S2-p0 | 2 | Q6:55270, Q7:0 | 55270 | Q6:55270 | Q6:405760, Q7:224640 |
| S3-p0 | 2 | Q6:47389, Q7:140042 | 187432 | Q6:47389, Q7:131717 | Q6:355840, Q7:344320 |
| sw01-p2 | 2 | Q6:23208, Q7:0 | 23208 | Q6:23208 | Q6:430720, Q7:252800 |
| sw02-p2 | 2 | Q6:64575, Q7:90297 | 154872 | Q6:64575, Q7:26852 | Q6:502080, Q7:132800 |
| sw08-p2 | 2 | Q6:122359, Q7:85598 | 207957 | Q6:113052, Q7:85598 | Q6:177920, Q7:588800 |
| sw01-p4 | 1 | Q6:0, Q7:50769 | 50769 | Q7:50769 | Q6:162240, Q7:625280 |
| sw01-p5 | 1 | Q6:12427, Q7:29925 | 42352 | Q6:12427, Q7:20779 | Q6:438080, Q7:265280 |
| sw02-p4 | 1 | Q6:69505, Q7:0 | 69505 | Q6:69505 | Q6:624960, Q7:162560 |
| sw02-p5 | 1 | Q6:18911, Q7:0 | 18911 | Q6:18911 | Q6:343040, Q7:376320 |
| sw03-p4 | 1 | Q6:8684, Q7:0 | 8684 | Q6:8684 | Q6:456320, Q7:262400 |
| sw03-p5 | 1 | Q6:0, Q7:45814 | 45814 | Q7:45814 | Q6:162240, Q7:621440 |
| sw04-p4 | 1 | Q6:28960, Q7:0 | 28960 | Q6:28960 | Q6:560320, Q7:161600 |
| sw04-p5 | 1 | Q6:61332, Q7:0 | 61332 | Q6:61332 | Q6:624960, Q7:162560 |
| sw05-p4 | 1 | Q6:0, Q7:41343 | 41343 | Q7:41343 | Q6:162240, Q7:613120 |
| sw05-p5 | 1 | Q6:7751, Q7:0 | 7751 | Q6:7751 | Q6:469120, Q7:260160 |
| sw06-p4 | 1 | Q6:54119, Q7:0 | 54119 | Q6:54119 | Q6:624960, Q7:162560 |
| sw06-p5 | 1 | Q6:25316, Q7:0 | 25316 | Q6:25316 | Q6:546560, Q7:169280 |
| sw07-p4 | 1 | Q6:6918, Q7:0 | 6918 | Q6:6918 | Q6:408000, Q7:288640 |
| sw07-p5 | 1 | Q6:0, Q7:37308 | 37308 | Q7:37308 | Q6:182720, Q7:604800 |
| sw08-p4 | 1 | Q6:22131, Q7:0 | 22131 | Q6:22131 | Q6:550720, Q7:139200 |
| sw08-p5 | 1 | Q6:6174, Q7:0 | 6174 | Q6:6174 | Q6:420800, Q7:291200 |

Total applied: **16056960 ns** across 22 port(s). Network total slack now banked: **16068800 ns**. GCL_size overflow: 0.

## Per-port GCL entries: before (SMT) vs. after (heuristic-enlarged)

| port | SMT entries | enlarged entries | GCL_size |
|---|---|---|---|
| sw01-p2 | 19 | 17 | 255 |
| sw01-p4 | 3 | 10 | 255 |
| sw01-p5 | 15 | 24 | 255 |
| sw02-p2 | 25 | 23 | 255 |
| sw02-p4 | 3 | 9 | 255 |
| sw02-p5 | 9 | 20 | 255 |
| sw03-p4 | 11 | 22 | 255 |
| sw03-p5 | 3 | 11 | 255 |
| sw04-p4 | 11 | 17 | 255 |
| sw04-p5 | 3 | 9 | 255 |
| sw05-p4 | 3 | 11 | 255 |
| sw05-p5 | 11 | 21 | 255 |
| sw06-p4 | 3 | 9 | 255 |
| sw06-p5 | 11 | 19 | 255 |
| sw07-p4 | 11 | 22 | 255 |
| sw07-p5 | 3 | 11 | 255 |
| sw08-p2 | 5 | 11 | 255 |
| sw08-p4 | 11 | 17 | 255 |
| sw08-p5 | 11 | 23 | 255 |

## Flows

| flow | route | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|
| s0(id=1 S3->S1) | S3->sw01->sw02->S1 | 6 | 62400 | 24720 | yes |
| s1(id=2 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | - | - | - | no |
| s2(id=3 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | - | - | - | no |
| s3(id=4 S3->S1) | S3->sw01->sw02->S1 | 7 | 37440 | 33360 | yes |
| s4(id=5 S1->S3) | S1->sw02->sw01->S3 | - | - | - | no |
| s5(id=6 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 6 | 0 | 40720 | yes |
| s6(id=7 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | 6 | 24960 | 33040 | yes |
| s7(id=8 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 6 | 74880 | 50960 | yes |
| s8(id=9 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 7 | 87360 | 54160 | yes |
| s9(id=10 S3->S1) | S3->sw01->sw02->S1 | 6 | 12480 | 27920 | yes |
| s10(id=11 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | - | - | - | no |
| s11(id=12 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 6 | 24960 | 36880 | yes |
| s12(id=13 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | - | - | - | no |
| s13(id=14 S1->S3) | S1->sw02->sw01->S3 | 6 | 0 | 27920 | yes |
| s14(id=15 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | - | - | - | no |
| s15(id=16 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | 6 | 49920 | 50000 | yes |
| s16(id=17 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | - | - | - | no |
| s17(id=18 S3->S1) | S3->sw01->sw02->S1 | - | - | - | no |
| s18(id=19 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | - | - | - | no |
| s19(id=20 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | 6 | 99840 | 36880 | yes |

## Per-hop windows (slack_ns > 0 means this window was enlarged)

| flow | egress port | queue | psi (ns) | delta (ns) |
|---|---|---|---|---|
| s0(id=1 S3->S1) | S3-p0 | Q6 | 62400 | 12480 |
| s0(id=1 S3->S1) | sw01-p5 | Q6 | 68480 | 12480 |
| s0(id=1 S3->S1) | sw02-p2 | Q6 | 74560 | 12480 |
| s3(id=4 S3->S1) | S3-p0 | Q7 | 37440 | 12480 |
| s3(id=4 S3->S1) | sw01-p5 | Q7 | 53120 | 12480 |
| s3(id=4 S3->S1) | sw02-p2 | Q7 | 58240 | 12480 |
| s5(id=6 S2->S3) | S2-p0 | Q6 | 0 | 12480 |
| s5(id=6 S2->S3) | sw08-p5 | Q6 | 5120 | 12480 |
| s5(id=6 S2->S3) | sw07-p4 | Q6 | 10240 | 12480 |
| s5(id=6 S2->S3) | sw05-p5 | Q6 | 15360 | 12480 |
| s5(id=6 S2->S3) | sw03-p4 | Q6 | 20480 | 12480 |
| s5(id=6 S2->S3) | sw01-p2 | Q6 | 28160 | 12480 |
| s6(id=7 S2->S1) | S2-p0 | Q6 | 24960 | 12480 |
| s6(id=7 S2->S1) | sw08-p4 | Q6 | 30080 | 12480 |
| s6(id=7 S2->S1) | sw06-p5 | Q6 | 35200 | 12480 |
| s6(id=7 S2->S1) | sw04-p4 | Q6 | 40320 | 12480 |
| s6(id=7 S2->S1) | sw02-p2 | Q6 | 45440 | 12480 |
| s7(id=8 S2->S3) | S2-p0 | Q6 | 74880 | 12480 |
| s7(id=8 S2->S3) | sw08-p5 | Q6 | 82560 | 12480 |
| s7(id=8 S2->S3) | sw07-p4 | Q6 | 90240 | 12480 |
| s7(id=8 S2->S3) | sw05-p5 | Q6 | 97920 | 12480 |
| s7(id=8 S2->S3) | sw03-p4 | Q6 | 105600 | 12480 |
| s7(id=8 S2->S3) | sw01-p2 | Q6 | 113280 | 12480 |
| s8(id=9 S3->S2) | S3-p0 | Q7 | 87360 | 12480 |
| s8(id=9 S3->S2) | sw01-p4 | Q7 | 95680 | 12480 |
| s8(id=9 S3->S2) | sw03-p5 | Q7 | 104000 | 12480 |
| s8(id=9 S3->S2) | sw05-p4 | Q7 | 112320 | 12480 |
| s8(id=9 S3->S2) | sw07-p5 | Q7 | 120640 | 12480 |
| s8(id=9 S3->S2) | sw08-p2 | Q7 | 128960 | 12480 |
| s9(id=10 S3->S1) | S3-p0 | Q6 | 12480 | 12480 |
| s9(id=10 S3->S1) | sw01-p5 | Q6 | 20160 | 12480 |
| s9(id=10 S3->S1) | sw02-p2 | Q6 | 27840 | 12480 |
| s11(id=12 S1->S2) | S1-p0 | Q6 | 24960 | 12480 |
| s11(id=12 S1->S2) | sw02-p4 | Q6 | 31040 | 12480 |
| s11(id=12 S1->S2) | sw04-p5 | Q6 | 37120 | 12480 |
| s11(id=12 S1->S2) | sw06-p4 | Q6 | 43200 | 12480 |
| s11(id=12 S1->S2) | sw08-p2 | Q6 | 49280 | 12480 |
| s13(id=14 S1->S3) | S1-p0 | Q6 | 0 | 12480 |
| s13(id=14 S1->S3) | sw02-p5 | Q6 | 7680 | 12480 |
| s13(id=14 S1->S3) | sw01-p2 | Q6 | 15360 | 12480 |
| s15(id=16 S2->S1) | S2-p0 | Q6 | 49920 | 12480 |
| s15(id=16 S2->S1) | sw08-p4 | Q6 | 60800 | 12480 |
| s15(id=16 S2->S1) | sw06-p5 | Q6 | 69120 | 12480 |
| s15(id=16 S2->S1) | sw04-p4 | Q6 | 77440 | 12480 |
| s15(id=16 S2->S1) | sw02-p2 | Q6 | 87360 | 12480 |
| s19(id=20 S2->S1) | S2-p0 | Q6 | 99840 | 12480 |
| s19(id=20 S2->S1) | sw08-p4 | Q6 | 105920 | 12480 |
| s19(id=20 S2->S1) | sw06-p5 | Q6 | 112000 | 12480 |
| s19(id=20 S2->S1) | sw04-p4 | Q6 | 118080 | 12480 |
| s19(id=20 S2->S1) | sw02-p2 | Q6 | 124160 | 12480 |

## Constraint check

- C1-C7, C9: OK
- seed-integrity (no SMT-fixed flow's placement changed): OK

## GCL per egress port

### sw01-p2  (17 entries, util 14.0400 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 2880 0x3F # 00111111   BE
sgs 35520 0x40 # 01000000   Q6
sgs 49280 0xBF # 10111111   Q7
sgs 13120 0x7F # 01111111   Q6
sgs 39680 0x40 # 01000000   Q6
sgs 47040 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 137600 0x40 # 01000000   Q6
sgs 47040 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 137600 0x40 # 01000000   Q6
sgs 47040 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 122240 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p4  (10 entries, util 1.5600 %)

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

### sw01-p5  (24 entries, util 10.9200 %)

```
sgs 20160 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 17280 0x7F # 01111111   Q6
sgs 3200 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 2880 0x3F # 00111111   BE
sgs 62720 0x40 # 01000000   Q6
sgs 18880 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 111040 0x40 # 01000000   Q6
sgs 18880 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 17280 0x7F # 01111111   Q6
sgs 3200 0x3F # 00111111   BE
sgs 78080 0x80 # 10000000   Q7
sgs 18880 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 90880 0x40 # 01000000   Q6
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (23 entries, util 18.7200 %)

```
sgs 27840 0x7F # 01111111   Q6
sgs 30080 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 3840 0x3F # 00111111   BE
sgs 25280 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 24000 0x7F # 01111111   Q6
sgs 53760 0x40 # 01000000   Q6
sgs 22080 0xBF # 10111111   Q7
sgs 27840 0x7F # 01111111   Q6
sgs 150080 0x40 # 01000000   Q6
sgs 22080 0xBF # 10111111   Q7
sgs 27840 0x7F # 01111111   Q6
sgs 30080 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 16640 0xBF # 10111111   Q7
sgs 90560 0x40 # 01000000   Q6
sgs 22080 0xBF # 10111111   Q7
sgs 27840 0x7F # 01111111   Q6
sgs 122240 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p4  (9 entries, util 1.5600 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 18560 0x7F # 01111111   Q6
sgs 506560 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p5  (20 entries, util 6.2400 %)

```
sgs 7680 0x3F # 00111111   BE
sgs 50240 0x40 # 01000000   Q6
sgs 42240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 7680 0x3F # 00111111   BE
sgs 50240 0x40 # 01000000   Q6
sgs 42240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 7680 0x3F # 00111111   BE
sgs 50240 0x40 # 01000000   Q6
sgs 42240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 7680 0x3F # 00111111   BE
sgs 42560 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (22 entries, util 7.8000 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 8000 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 16960 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 5440 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 32000 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 94720 0x40 # 01000000   Q6
sgs 34880 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 94720 0x40 # 01000000   Q6
sgs 34880 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 74240 0x40 # 01000000   Q6
sgs 5440 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p5  (11 entries, util 1.5600 %)

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

### sw04-p4  (17 entries, util 7.8000 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 27840 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 24640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 10240 0x3F # 00111111   BE
sgs 17920 0x7F # 01111111   Q6
sgs 216960 0x40 # 01000000   Q6
sgs 15040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 40320 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 24640 0xBF # 10111111   Q7
sgs 217280 0x40 # 01000000   Q6
sgs 5440 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (9 entries, util 1.5600 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 24640 0x7F # 01111111   Q6
sgs 500480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (11 entries, util 1.5600 %)

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

### sw05-p5  (21 entries, util 7.8000 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 2880 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 22080 0x7F # 01111111   Q6
sgs 48000 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 39680 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 94720 0x40 # 01000000   Q6
sgs 40000 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 94720 0x40 # 01000000   Q6
sgs 40000 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 79360 0x40 # 01000000   Q6
sgs 5440 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p4  (9 entries, util 1.5600 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 494400 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (19 entries, util 7.8000 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 22720 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 2240 0x3F # 00111111   BE
sgs 19200 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 18560 0xBF # 10111111   Q7
sgs 11840 0x3F # 00111111   BE
sgs 217920 0x40 # 01000000   Q6
sgs 20160 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 35200 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 2240 0x3F # 00111111   BE
sgs 19200 0xBF # 10111111   Q7
sgs 225600 0x40 # 01000000   Q6
sgs 5440 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (22 entries, util 7.8000 %)

```
sgs 10240 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 27200 0x7F # 01111111   Q6
sgs 40320 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 47360 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 10240 0x3F # 00111111   BE
sgs 77120 0x40 # 01000000   Q6
sgs 12800 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 10240 0x3F # 00111111   BE
sgs 77120 0x40 # 01000000   Q6
sgs 12800 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 10240 0x3F # 00111111   BE
sgs 66880 0x40 # 01000000   Q6
sgs 23040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p5  (11 entries, util 1.5600 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 416960 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p2  (11 entries, util 3.1200 %)

```
sgs 49280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 38400 0xBF # 10111111   Q7
sgs 28800 0x7F # 01111111   Q6
sgs 412800 0x80 # 10000000   Q7
sgs 8320 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p4  (17 entries, util 7.8000 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 17600 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 18240 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 26880 0xBF # 10111111   Q7
sgs 5760 0x3F # 00111111   BE
sgs 218880 0x40 # 01000000   Q6
sgs 25280 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 30080 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 18240 0x3F # 00111111   BE
sgs 233920 0x40 # 01000000   Q6
sgs 5440 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (23 entries, util 7.8000 %)

```
sgs 5120 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 32320 0x7F # 01111111   Q6
sgs 32640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 5120 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 5120 0x3F # 00111111   BE
sgs 77120 0x40 # 01000000   Q6
sgs 17920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 5120 0x3F # 00111111   BE
sgs 77120 0x40 # 01000000   Q6
sgs 17920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 5120 0x3F # 00111111   BE
sgs 72000 0x40 # 01000000   Q6
sgs 23040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

