# Heuristic-enlarged GCL schedule (Problem 2: window enlargement)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Time-sensitive PCPs considered: [6, 7]
- Seeded from SMT run: **result/result-2026-10-10-dataset-testbed-5-avgwin/smt-c9-off/5-t3600-c9off-minlat**

## Admission (unchanged by this package -- it only widens windows)

SMT-fixed flows: **10**/20. This package never admits a flow itself; it banks slack for a later admission pass (`prob_3_admit`, Problem 3) to use.

## Opportunistic idle top-up (Step 7 -- see enlarge.py)

Total: **12170240 ns**, drawn from idle capacity on ports at or below utilisation 0.2, independent of any route's deadline-slack budget.

| port | queue | applied (ns) |
|---|---|---|
| S1-p0 | Q6 | 213760 |
| S1-p0 | Q7 | 408640 |
| S2-p0 | Q6 | 409280 |
| S2-p0 | Q7 | 148800 |
| S3-p0 | Q7 | 690240 |
| sw01-p2 | Q6 | 564800 |
| sw01-p2 | Q7 | 14720 |
| sw01-p4 | Q7 | 674880 |
| sw02-p2 | Q7 | 647360 |
| sw02-p4 | Q6 | 221760 |
| sw02-p4 | Q7 | 398400 |
| sw03-p4 | Q6 | 584000 |
| sw03-p4 | Q7 | 21440 |
| sw03-p5 | Q7 | 659200 |
| sw04-p4 | Q7 | 667200 |
| sw04-p5 | Q6 | 231680 |
| sw04-p5 | Q7 | 384000 |
| sw05-p4 | Q7 | 643520 |
| sw05-p5 | Q6 | 602560 |
| sw05-p5 | Q7 | 26880 |
| sw06-p4 | Q6 | 239360 |
| sw06-p4 | Q7 | 368960 |
| sw06-p5 | Q7 | 686720 |
| sw07-p4 | Q6 | 621120 |
| sw07-p4 | Q7 | 32000 |
| sw07-p5 | Q7 | 627840 |
| sw08-p4 | Q7 | 705920 |
| sw08-p5 | Q6 | 639040 |
| sw08-p5 | Q7 | 36160 |

## Opportunistic window creation (Step 8 -- see enlarge.py)

**9** brand-new window(s) opened, **112320 ns** total, on ports at or below utilisation 0.2 whose TT queue had zero windows before this run.

| port | queue | size (ns) |
|---|---|---|
| S3-p0 | Q6 | 12480 |
| sw01-p4 | Q6 | 12480 |
| sw02-p2 | Q6 | 12480 |
| sw03-p5 | Q6 | 12480 |
| sw04-p4 | Q6 | 12480 |
| sw05-p4 | Q6 | 12480 |
| sw06-p5 | Q6 | 12480 |
| sw07-p5 | Q6 | 12480 |
| sw08-p4 | Q6 | 12480 |

## Best-effort gap equalization (Step 9 -- see enlarge.py)

**7664960 ns** given back from Steps 7/8's growth so each port's leftover non-TAS gaps land close to equal, instead of one gap staying huge while a neighbour is squeezed to the bare 1-tick C10 minimum.

| port | given back (ns) |
|---|---|
| sw01-p2 | 472640 |
| sw03-p4 | 472640 |
| sw05-p5 | 472640 |
| sw07-p4 | 472640 |
| sw08-p5 | 472640 |
| S2-p0 | 418240 |
| sw02-p4 | 387840 |
| sw04-p5 | 387840 |
| sw06-p4 | 387840 |
| sw02-p2 | 387200 |
| sw04-p4 | 387200 |
| sw06-p5 | 387200 |
| sw08-p4 | 387200 |
| S1-p0 | 385920 |
| sw03-p5 | 354240 |
| sw05-p4 | 354240 |
| sw07-p5 | 354240 |
| sw01-p4 | 353600 |
| S3-p0 | 353600 |
| sw08-p2 | 15360 |

## Opportunistic overlay window creation (Step 10 -- see enlarge.py)

**38** new overlay window(s), **8171840 ns** total, carved out of already-open best-effort spans on ports at or below utilisation 0.2 -- best-effort stays reachable inside each one (gate mask keeps its BE bits set), so none of this is closed off from BE.

| port | queue | size (ns) |
|---|---|---|
| S1-p0 | Q6 | 161280 |
| S1-p0 | Q7 | 224640 |
| S2-p0 | Q6 | 206080 |
| S2-p0 | Q7 | 212160 |
| S3-p0 | Q6 | 141440 |
| S3-p0 | Q7 | 212160 |
| sw01-p2 | Q6 | 282560 |
| sw01-p2 | Q7 | 265280 |
| sw01-p4 | Q6 | 133120 |
| sw01-p4 | Q7 | 212160 |
| sw02-p2 | Q6 | 220480 |
| sw02-p2 | Q7 | 250560 |
| sw02-p4 | Q6 | 136000 |
| sw02-p4 | Q7 | 214080 |
| sw03-p4 | Q6 | 262080 |
| sw03-p4 | Q7 | 261120 |
| sw03-p5 | Q6 | 199680 |
| sw03-p5 | Q7 | 176000 |
| sw04-p4 | Q6 | 230720 |
| sw04-p4 | Q7 | 224960 |
| sw04-p5 | Q6 | 160960 |
| sw04-p5 | Q7 | 243200 |
| sw05-p4 | Q6 | 216320 |
| sw05-p4 | Q7 | 176000 |
| sw05-p5 | Q6 | 274880 |
| sw05-p5 | Q7 | 224640 |
| sw06-p4 | Q6 | 241920 |
| sw06-p4 | Q7 | 187200 |
| sw06-p5 | Q6 | 230720 |
| sw06-p5 | Q7 | 214720 |
| sw07-p4 | Q6 | 265280 |
| sw07-p4 | Q7 | 232960 |
| sw07-p5 | Q6 | 216320 |
| sw07-p5 | Q7 | 166400 |
| sw08-p4 | Q6 | 230720 |
| sw08-p4 | Q7 | 189760 |
| sw08-p5 | Q6 | 260800 |
| sw08-p5 | Q7 | 212480 |

## Candidate routes (P^cand = routes of the fixed flows above)

| route | PCPs carried | flows |
|---|---|---|
| S1->sw02->sw04->sw06->sw08->S2 | Q6 (2), Q7 (1) | 3 |
| S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | Q6 (1) | 1 |
| S2->sw08->sw06->sw04->sw02->S1 | Q7 (1) | 1 |
| S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 (1), Q7 (1) | 2 |
| S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 (3) | 3 |

## Per-link enlargement accounting

| link | sharing eta | route-safe slack (ns) | link budget (ns) | final slack (ns) | applied (ns) |
|---|---|---|---|---|---|
| S1-p0 | 2 | Q6:61718, Q7:19100 | 80818 | Q6:61718, Q7:16570 | Q6:256000, Q7:444160 |
| S2-p0 | 2 | Q6:15984, Q7:145983 | 161967 | Q6:15984, Q7:139119 | Q6:403200, Q7:309440 |
| sw01-p2 | 2 | Q6:14945, Q7:81185 | 96129 | Q6:14945, Q7:47767 | Q6:451840, Q7:265280 |
| sw02-p4 | 2 | Q6:49679, Q7:16082 | 65761 | Q6:49679, Q7:13971 | Q6:228800, Q7:416960 |
| sw03-p4 | 2 | Q6:12414, Q7:69378 | 81792 | Q6:12414, Q7:41223 | Q6:448000, Q7:261120 |
| sw04-p5 | 2 | Q6:39988, Q7:13541 | 53530 | Q6:39988, Q7:11781 | Q6:253760, Q7:429440 |
| sw05-p5 | 2 | Q6:10312, Q7:59289 | 69601 | Q6:10312, Q7:35573 | Q6:477440, Q7:224640 |
| sw06-p4 | 2 | Q6:32188, Q7:11401 | 43590 | Q6:32188, Q7:9934 | Q6:334720, Q7:356800 |
| sw07-p4 | 2 | Q6:8566, Q7:50667 | 59233 | Q6:8566, Q7:30693 | Q6:484480, Q7:232960 |
| sw08-p2 | 2 | Q6:29189, Q7:22355 | 51544 | Q6:12374, Q7:22355 | Q7:7680 |
| sw08-p5 | 2 | Q6:7115, Q7:43299 | 50414 | Q6:7115, Q7:26480 | Q6:496640, Q7:212480 |
| S3-p0 | 1 | Q6:0, Q7:10190 | 10190 | Q7:10190 | Q6:153920, Q7:558720 |
| sw01-p4 | 1 | Q6:0, Q7:8922 | 8922 | Q7:8922 | Q6:145600, Q7:542080 |
| sw02-p2 | 1 | Q6:0, Q7:23832 | 23832 | Q7:23832 | Q6:232960, Q7:534400 |
| sw03-p5 | 1 | Q6:0, Q7:7811 | 7811 | Q7:7811 | Q6:212160, Q7:488640 |
| sw04-p4 | 1 | Q6:0, Q7:20585 | 20585 | Q7:20585 | Q6:243200, Q7:525440 |
| sw05-p4 | 1 | Q6:0, Q7:6839 | 6839 | Q7:6839 | Q6:228800, Q7:472000 |
| sw06-p5 | 1 | Q6:0, Q7:17780 | 17780 | Q7:17780 | Q6:243200, Q7:531840 |
| sw07-p5 | 1 | Q6:0, Q7:5988 | 5988 | Q7:5988 | Q6:228800, Q7:445760 |
| sw08-p4 | 1 | Q6:0, Q7:15357 | 15357 | Q7:15357 | Q6:243200, Q7:523520 |

Total applied: **13550080 ns** across 20 port(s). Network total slack now banked: **13611520 ns**. GCL_size overflow: 0.

## Per-port GCL entries: before (SMT) vs. after (heuristic-enlarged)

| port | SMT entries | enlarged entries | GCL_size |
|---|---|---|---|
| sw01-p2 | 13 | 23 | 255 |
| sw01-p4 | 15 | 20 | 255 |
| sw02-p2 | 5 | 15 | 255 |
| sw02-p4 | 17 | 24 | 255 |
| sw03-p4 | 13 | 24 | 255 |
| sw03-p5 | 15 | 18 | 255 |
| sw04-p4 | 5 | 14 | 255 |
| sw04-p5 | 17 | 21 | 255 |
| sw05-p4 | 15 | 22 | 255 |
| sw05-p5 | 13 | 22 | 255 |
| sw06-p4 | 17 | 19 | 255 |
| sw06-p5 | 5 | 14 | 255 |
| sw07-p4 | 13 | 22 | 255 |
| sw07-p5 | 15 | 19 | 255 |
| sw08-p2 | 29 | 29 | 255 |
| sw08-p4 | 5 | 14 | 255 |
| sw08-p5 | 13 | 23 | 255 |

## Flows

| flow | route | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|
| s0(id=1 S3->S1) | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | - | - | - | no |
| s1(id=2 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 6 | 0 | 95760 | yes |
| s2(id=3 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 6 | 62400 | 84240 | yes |
| s3(id=4 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | - | - | - | no |
| s4(id=5 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 7 | 62400 | 95760 | yes |
| s5(id=6 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | - | - | - | no |
| s6(id=7 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | - | - | - | no |
| s7(id=8 S3->S1) | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | - | - | - | no |
| s8(id=9 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | 7 | 37440 | 79120 | yes |
| s9(id=10 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 7 | 0 | 79120 | yes |
| s10(id=11 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | - | - | - | no |
| s11(id=12 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 7 | 12480 | 95760 | yes |
| s12(id=13 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | 6 | 87360 | 145680 | yes |
| s13(id=14 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | - | - | - | no |
| s14(id=15 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | - | - | - | no |
| s15(id=16 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 7 | 62400 | 97040 | yes |
| s16(id=17 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 6 | 37440 | 83600 | yes |
| s17(id=18 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | - | - | - | no |
| s18(id=19 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 7 | 37440 | 96400 | yes |
| s19(id=20 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | - | - | - | no |

## Per-hop windows (slack_ns > 0 means this window was enlarged)

| flow | egress port | queue | psi (ns) | delta (ns) |
|---|---|---|---|---|
| s1(id=2 S2->S3) | S2-p0 | Q6 | 0 | 12480 |
| s1(id=2 S2->S3) | sw08-p5 | Q6 | 16640 | 12480 |
| s1(id=2 S2->S3) | sw07-p4 | Q6 | 33280 | 12480 |
| s1(id=2 S2->S3) | sw05-p5 | Q6 | 49920 | 12480 |
| s1(id=2 S2->S3) | sw03-p4 | Q6 | 66560 | 12480 |
| s1(id=2 S2->S3) | sw01-p2 | Q6 | 83200 | 12480 |
| s2(id=3 S1->S2) | S1-p0 | Q6 | 62400 | 12480 |
| s2(id=3 S1->S2) | sw02-p4 | Q6 | 82880 | 12480 |
| s2(id=3 S1->S2) | sw04-p5 | Q6 | 99520 | 12480 |
| s2(id=3 S1->S2) | sw06-p4 | Q6 | 116160 | 12480 |
| s2(id=3 S1->S2) | sw08-p2 | Q6 | 134080 | 12480 |
| s4(id=5 S2->S3) | S2-p0 | Q7 | 62400 | 12480 |
| s4(id=5 S2->S3) | sw08-p5 | Q7 | 79040 | 12480 |
| s4(id=5 S2->S3) | sw07-p4 | Q7 | 95680 | 12480 |
| s4(id=5 S2->S3) | sw05-p5 | Q7 | 112320 | 12480 |
| s4(id=5 S2->S3) | sw03-p4 | Q7 | 128960 | 12480 |
| s4(id=5 S2->S3) | sw01-p2 | Q7 | 145600 | 12480 |
| s8(id=9 S2->S1) | S2-p0 | Q7 | 37440 | 12480 |
| s8(id=9 S2->S1) | sw08-p4 | Q7 | 54080 | 12480 |
| s8(id=9 S2->S1) | sw06-p5 | Q7 | 70720 | 12480 |
| s8(id=9 S2->S1) | sw04-p4 | Q7 | 87360 | 12480 |
| s8(id=9 S2->S1) | sw02-p2 | Q7 | 104000 | 12480 |
| s9(id=10 S1->S2) | S1-p0 | Q7 | 0 | 12480 |
| s9(id=10 S1->S2) | sw02-p4 | Q7 | 16640 | 12480 |
| s9(id=10 S1->S2) | sw04-p5 | Q7 | 33280 | 12480 |
| s9(id=10 S1->S2) | sw06-p4 | Q7 | 49920 | 12480 |
| s9(id=10 S1->S2) | sw08-p2 | Q7 | 66560 | 12480 |
| s11(id=12 S3->S2) | S3-p0 | Q7 | 12480 | 12480 |
| s11(id=12 S3->S2) | sw01-p4 | Q7 | 29120 | 12480 |
| s11(id=12 S3->S2) | sw03-p5 | Q7 | 45760 | 12480 |
| s11(id=12 S3->S2) | sw05-p4 | Q7 | 62400 | 12480 |
| s11(id=12 S3->S2) | sw07-p5 | Q7 | 79040 | 12480 |
| s11(id=12 S3->S2) | sw08-p2 | Q7 | 95680 | 12480 |
| s12(id=13 S1->S3) | S1-p0 | Q6 | 87360 | 12480 |
| s12(id=13 S1->S3) | sw02-p4 | Q6 | 104000 | 12480 |
| s12(id=13 S1->S3) | sw04-p5 | Q6 | 120640 | 12480 |
| s12(id=13 S1->S3) | sw06-p4 | Q6 | 137280 | 12480 |
| s12(id=13 S1->S3) | sw08-p5 | Q6 | 153920 | 12480 |
| s12(id=13 S1->S3) | sw07-p4 | Q6 | 170560 | 12480 |
| s12(id=13 S1->S3) | sw05-p5 | Q6 | 187200 | 12480 |
| s12(id=13 S1->S3) | sw03-p4 | Q6 | 203840 | 12480 |
| s12(id=13 S1->S3) | sw01-p2 | Q6 | 220480 | 12480 |
| s15(id=16 S3->S2) | S3-p0 | Q7 | 62400 | 12480 |
| s15(id=16 S3->S2) | sw01-p4 | Q7 | 79040 | 12480 |
| s15(id=16 S3->S2) | sw03-p5 | Q7 | 95680 | 12480 |
| s15(id=16 S3->S2) | sw05-p4 | Q7 | 112320 | 12480 |
| s15(id=16 S3->S2) | sw07-p5 | Q7 | 128960 | 12480 |
| s15(id=16 S3->S2) | sw08-p2 | Q7 | 146880 | 12480 |
| s16(id=17 S1->S2) | S1-p0 | Q6 | 37440 | 12480 |
| s16(id=17 S1->S2) | sw02-p4 | Q6 | 56000 | 12480 |
| s16(id=17 S1->S2) | sw04-p5 | Q6 | 72640 | 12480 |
| s16(id=17 S1->S2) | sw06-p4 | Q6 | 89280 | 12480 |
| s16(id=17 S1->S2) | sw08-p2 | Q6 | 108480 | 12480 |
| s18(id=19 S3->S2) | S3-p0 | Q7 | 37440 | 12480 |
| s18(id=19 S3->S2) | sw01-p4 | Q7 | 54080 | 12480 |
| s18(id=19 S3->S2) | sw03-p5 | Q7 | 71360 | 12480 |
| s18(id=19 S3->S2) | sw05-p4 | Q7 | 88000 | 12480 |
| s18(id=19 S3->S2) | sw07-p5 | Q7 | 104640 | 12480 |
| s18(id=19 S3->S2) | sw08-p2 | Q7 | 121280 | 12480 |

## Constraint check

- C1-C7, C9: OK
- seed-integrity (no SMT-fixed flow's placement changed): OK

## GCL per egress port

### sw01-p2  (23 entries, util 9.3600 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 4480 0x3F # 00111111   BE
sgs 45440 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 41920 0xBF # 10111111   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 16960 0x7F # 01111111   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 96640 0x40 # 01000000   Q6
sgs 20160 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 96640 0x40 # 01000000   Q6
sgs 20160 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 13440 0x40 # 01000000   Q6
sgs 3520 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p4  (20 entries, util 10.9200 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 71040 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 120960 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 96000 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 91840 0x80 # 10000000   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (15 entries, util 3.1200 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 3840 0x3F # 00111111   BE
sgs 206400 0x80 # 10000000   Q7
sgs 39680 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 3840 0x3F # 00111111   BE
sgs 102400 0x80 # 10000000   Q7
sgs 43520 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p4  (24 entries, util 12.4800 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 6080 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0xBF # 10111111   Q7
sgs 56000 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 122240 0x80 # 10000000   Q7
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 6080 0x3F # 00111111   BE
sgs 82880 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 105600 0x80 # 10000000   Q7
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (24 entries, util 9.3600 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 21120 0xBF # 10111111   Q7
sgs 28800 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 8640 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 3840 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 33600 0x7F # 01111111   Q6
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

### sw03-p5  (18 entries, util 10.9200 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0xBF # 10111111   Q7
sgs 95360 0x80 # 10000000   Q7
sgs 33280 0xBF # 10111111   Q7
sgs 45760 0x7F # 01111111   Q6
sgs 120960 0x80 # 10000000   Q7
sgs 33280 0xBF # 10111111   Q7
sgs 45760 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0xBF # 10111111   Q7
sgs 95360 0x80 # 10000000   Q7
sgs 33280 0xBF # 10111111   Q7
sgs 45760 0x7F # 01111111   Q6
sgs 75200 0x80 # 10000000   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p4  (14 entries, util 3.1200 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 37440 0xBF # 10111111   Q7
sgs 206400 0x80 # 10000000   Q7
sgs 6400 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 37440 0xBF # 10111111   Q7
sgs 119040 0x80 # 10000000   Q7
sgs 43520 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (21 entries, util 12.4800 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 22720 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0xBF # 10111111   Q7
sgs 56000 0x40 # 01000000   Q6
sgs 44480 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 122240 0x80 # 10000000   Q7
sgs 44480 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 22720 0xBF # 10111111   Q7
sgs 82880 0x40 # 01000000   Q6
sgs 44480 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 88960 0x80 # 10000000   Q7
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (22 entries, util 10.9200 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0xBF # 10111111   Q7
sgs 95360 0x80 # 10000000   Q7
sgs 16640 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 120960 0x80 # 10000000   Q7
sgs 16640 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0xBF # 10111111   Q7
sgs 95360 0x80 # 10000000   Q7
sgs 16640 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 58560 0x80 # 10000000   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p5  (22 entries, util 9.3600 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 37760 0xBF # 10111111   Q7
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0x7F # 01111111   Q6
sgs 37120 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
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

### sw06-p4  (19 entries, util 12.4800 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 26880 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0x7F # 01111111   Q6
sgs 56000 0x40 # 01000000   Q6
sgs 27840 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 122240 0x80 # 10000000   Q7
sgs 27840 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 26880 0xBF # 10111111   Q7
sgs 82880 0x40 # 01000000   Q6
sgs 27840 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 72320 0x80 # 10000000   Q7
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (14 entries, util 3.1200 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 20800 0xBF # 10111111   Q7
sgs 206400 0x80 # 10000000   Q7
sgs 23040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 20800 0xBF # 10111111   Q7
sgs 135680 0x80 # 10000000   Q7
sgs 43520 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (22 entries, util 9.3600 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 45760 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 41920 0x7F # 01111111   Q6
sgs 20480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 16960 0xBF # 10111111   Q7
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

### sw07-p5  (19 entries, util 10.9200 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0x3F # 00111111   BE
sgs 95360 0x80 # 10000000   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 120960 0x80 # 10000000   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0x3F # 00111111   BE
sgs 95360 0x80 # 10000000   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 41920 0x80 # 10000000   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p2  (29 entries, util 21.8400 %)

```
sgs 66560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 16640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 14400 0x80 # 10000000   Q7
sgs 105280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 16640 0x3F # 00111111   BE
sgs 14400 0x80 # 10000000   Q7
sgs 156480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 16640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 14400 0x80 # 10000000   Q7
sgs 130880 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 16640 0x3F # 00111111   BE
sgs 14400 0x80 # 10000000   Q7
sgs 89920 0x3F # 00111111   BE
```

### sw08-p4  (14 entries, util 3.1200 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 4160 0x3F # 00111111   BE
sgs 206400 0x80 # 10000000   Q7
sgs 39680 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 4160 0x3F # 00111111   BE
sgs 152320 0x80 # 10000000   Q7
sgs 43520 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (23 entries, util 9.3600 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 8640 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 3840 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 33600 0xBF # 10111111   Q7
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

