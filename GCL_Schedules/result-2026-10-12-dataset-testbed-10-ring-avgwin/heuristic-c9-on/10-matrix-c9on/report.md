# Heuristic-enlarged GCL schedule (Problem 2: window enlargement)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Time-sensitive PCPs considered: [6, 7]
- Seeded from SMT run: **result/result-2026-10-12-dataset-testbed-10-ring-avgwin/smt-c9-on/10-fair-retimed-c9on**

## Admission (unchanged by this package -- it only widens windows)

SMT-fixed flows: **11**/11. This package never admits a flow itself; it banks slack for a later admission pass (`prob_3_admit`, Problem 3) to use.

## Opportunistic idle top-up (Step 7 -- see enlarge.py)

Total: **14364800 ns**, drawn from idle capacity on ports at or below utilisation 0.2, independent of any route's deadline-slack budget.

| port | queue | applied (ns) |
|---|---|---|
| S1-p0 | Q6 | 242560 |
| S1-p0 | Q7 | 313600 |
| S2-p0 | Q6 | 85120 |
| S2-p0 | Q7 | 541440 |
| S3-p0 | Q6 | 70400 |
| S3-p0 | Q7 | 471360 |
| sw01-p2 | Q6 | 253760 |
| sw01-p2 | Q7 | 321280 |
| sw01-p4 | Q7 | 735040 |
| sw01-p5 | Q6 | 334080 |
| sw01-p5 | Q7 | 275200 |
| sw02-p2 | Q6 | 255680 |
| sw02-p2 | Q7 | 267840 |
| sw02-p4 | Q6 | 91520 |
| sw02-p4 | Q7 | 555520 |
| sw02-p5 | Q6 | 704000 |
| sw03-p4 | Q7 | 689600 |
| sw03-p5 | Q7 | 728320 |
| sw04-p4 | Q6 | 655680 |
| sw04-p5 | Q6 | 97280 |
| sw04-p5 | Q7 | 547840 |
| sw05-p4 | Q7 | 721280 |
| sw05-p5 | Q7 | 697280 |
| sw06-p4 | Q6 | 102400 |
| sw06-p4 | Q7 | 540160 |
| sw06-p5 | Q6 | 669760 |
| sw07-p4 | Q7 | 704640 |
| sw07-p5 | Q7 | 714240 |
| sw08-p2 | Q6 | 88000 |
| sw08-p2 | Q7 | 495040 |
| sw08-p4 | Q6 | 683200 |
| sw08-p5 | Q7 | 711680 |

## Opportunistic window creation (Step 8 -- see enlarge.py)

**8** brand-new window(s) opened, **99840 ns** total, on ports at or below utilisation 0.2 whose TT queue had zero windows before this run.

| port | queue | size (ns) |
|---|---|---|
| sw03-p4 | Q6 | 12480 |
| sw03-p5 | Q6 | 12480 |
| sw04-p4 | Q7 | 12480 |
| sw05-p4 | Q6 | 12480 |
| sw05-p5 | Q6 | 12480 |
| sw06-p5 | Q7 | 12480 |
| sw07-p5 | Q6 | 12480 |
| sw08-p4 | Q7 | 12480 |

## Best-effort gap equalization (Step 9 -- see enlarge.py)

**8729280 ns** given back from Steps 7/8's growth so each port's leftover non-TAS gaps land close to equal, instead of one gap staying huge while a neighbour is squeezed to the bare 1-tick C10 minimum.

| port | given back (ns) |
|---|---|
| sw01-p4 | 599040 |
| sw02-p4 | 528320 |
| sw04-p5 | 527680 |
| sw06-p4 | 527040 |
| sw03-p5 | 499200 |
| sw05-p4 | 499200 |
| sw07-p5 | 499200 |
| sw02-p5 | 485120 |
| sw07-p4 | 438400 |
| sw08-p5 | 438400 |
| S2-p0 | 393280 |
| sw03-p4 | 387200 |
| sw05-p5 | 387200 |
| sw08-p2 | 338240 |
| S3-p0 | 336320 |
| S1-p0 | 307520 |
| sw01-p5 | 282240 |
| sw04-p4 | 262400 |
| sw06-p5 | 262400 |
| sw08-p4 | 262400 |
| sw01-p2 | 235520 |
| sw02-p2 | 232960 |

## Opportunistic overlay window creation (Step 10 -- see enlarge.py)

**44** new overlay window(s), **8843520 ns** total, carved out of already-open best-effort spans on ports at or below utilisation 0.2 -- best-effort stays reachable inside each one (gate mask keeps its BE bits set), so none of this is closed off from BE.

| port | queue | size (ns) |
|---|---|---|
| S1-p0 | Q6 | 74880 |
| S1-p0 | Q7 | 212160 |
| S2-p0 | Q6 | 193600 |
| S2-p0 | Q7 | 199680 |
| S3-p0 | Q6 | 124160 |
| S3-p0 | Q7 | 212160 |
| sw01-p2 | Q6 | 61440 |
| sw01-p2 | Q7 | 153600 |
| sw01-p4 | Q6 | 199680 |
| sw01-p4 | Q7 | 376320 |
| sw01-p5 | Q6 | 155520 |
| sw01-p5 | Q7 | 136320 |
| sw02-p2 | Q6 | 143680 |
| sw02-p2 | Q7 | 99840 |
| sw02-p4 | Q6 | 302080 |
| sw02-p4 | Q7 | 255360 |
| sw02-p5 | Q6 | 246720 |
| sw02-p5 | Q7 | 199680 |
| sw03-p4 | Q6 | 187520 |
| sw03-p4 | Q7 | 199680 |
| sw03-p5 | Q6 | 245760 |
| sw03-p5 | Q7 | 224640 |
| sw04-p4 | Q6 | 149760 |
| sw04-p4 | Q7 | 173120 |
| sw04-p5 | Q6 | 310400 |
| sw04-p5 | Q7 | 258880 |
| sw05-p4 | Q6 | 268800 |
| sw05-p4 | Q7 | 224640 |
| sw05-p5 | Q6 | 187520 |
| sw05-p5 | Q7 | 199680 |
| sw06-p4 | Q6 | 318720 |
| sw06-p4 | Q7 | 258240 |
| sw06-p5 | Q6 | 149760 |
| sw06-p5 | Q7 | 165440 |
| sw07-p4 | Q6 | 198720 |
| sw07-p4 | Q7 | 199680 |
| sw07-p5 | Q6 | 292800 |
| sw07-p5 | Q7 | 224640 |
| sw08-p2 | Q6 | 172160 |
| sw08-p2 | Q7 | 169600 |
| sw08-p4 | Q6 | 149760 |
| sw08-p4 | Q7 | 150080 |
| sw08-p5 | Q6 | 216960 |
| sw08-p5 | Q7 | 199680 |

## Candidate routes (P^cand = routes of the fixed flows above)

| route | PCPs carried | flows |
|---|---|---|
| S1->sw02->sw01->S3 | Q6 (2) | 2 |
| S1->sw02->sw04->sw06->sw08->S2 | Q6 (1), Q7 (1) | 2 |
| S2->sw08->sw06->sw04->sw02->S1 | Q6 (1) | 1 |
| S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 (2) | 2 |
| S3->sw01->sw02->S1 | Q6 (2), Q7 (1) | 3 |
| S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 (1) | 1 |

## Per-link enlargement accounting

| link | sharing eta | route-safe slack (ns) | link budget (ns) | final slack (ns) | applied (ns) |
|---|---|---|---|---|---|
| S1-p0 | 2 | Q6:70256, Q7:40126 | 110382 | Q6:70256, Q7:36629 | Q6:215040, Q7:427200 |
| S2-p0 | 2 | Q6:122941, Q7:33905 | 156846 | Q6:52534, Q7:33905 | Q6:242240, Q7:470400 |
| S3-p0 | 2 | Q6:135400, Q7:41453 | 176853 | Q6:104718, Q7:41453 | Q6:193280, Q7:494400 |
| sw01-p2 | 2 | Q6:38462, Q7:34115 | 72577 | Q6:26164, Q7:34115 | Q6:231040, Q7:383360 |
| sw02-p2 | 2 | Q6:94785, Q7:176007 | 270792 | Q6:94785, Q7:66834 | Q6:364480, Q7:330880 |
| sw08-p2 | 2 | Q6:98192, Q7:34115 | 132307 | Q6:32609, Q7:34115 | Q6:224000, Q7:428800 |
| sw01-p4 | 1 | Q6:0, Q7:7435 | 7435 | Q7:7435 | Q6:199680, Q7:519680 |
| sw01-p5 | 1 | Q6:33434, Q7:107209 | 140643 | Q6:33434, Q7:62579 | Q6:363520, Q7:351040 |
| sw02-p4 | 1 | Q6:66696, Q7:10869 | 77565 | Q6:46956, Q7:10869 | Q6:317440, Q7:416000 |
| sw02-p5 | 1 | Q6:13558, Q7:0 | 13558 | Q6:13558 | Q6:479040, Q7:199680 |
| sw03-p4 | 1 | Q6:0, Q7:11284 | 11284 | Q7:11284 | Q6:200000, Q7:513280 |
| sw03-p5 | 1 | Q6:0, Q7:6682 | 6682 | Q7:6682 | Q6:258240, Q7:460160 |
| sw04-p4 | 1 | Q6:58977, Q7:0 | 58977 | Q6:58977 | Q6:601920, Q7:185600 |
| sw04-p5 | 1 | Q6:59134, Q7:9391 | 68525 | Q6:41905, Q7:9391 | Q6:326400, Q7:411200 |
| sw05-p4 | 1 | Q6:0, Q7:6006 | 6006 | Q7:6006 | Q6:281280, Q7:452480 |
| sw05-p5 | 1 | Q6:0, Q7:9854 | 9854 | Q7:9854 | Q6:200000, Q7:519360 |
| sw06-p4 | 1 | Q6:52430, Q7:8114 | 60543 | Q6:37395, Q7:8114 | Q6:335360, Q7:402240 |
| sw06-p5 | 1 | Q6:52524, Q7:0 | 52524 | Q6:52524 | Q6:609600, Q7:177920 |
| sw07-p4 | 1 | Q6:0, Q7:8605 | 8605 | Q7:8605 | Q6:198720, Q7:474240 |
| sw07-p5 | 1 | Q6:0, Q7:5398 | 5398 | Q7:5398 | Q6:305280, Q7:444800 |
| sw08-p4 | 1 | Q6:46777, Q7:0 | 46777 | Q6:46777 | Q6:617280, Q7:162560 |
| sw08-p5 | 1 | Q6:0, Q7:7514 | 7514 | Q7:7514 | Q6:216960, Q7:480320 |

Total applied: **15686400 ns** across 22 port(s). Network total slack now banked: **15764800 ns**. GCL_size overflow: 0.

## Per-port GCL entries: before (SMT) vs. after (heuristic-enlarged)

| port | SMT entries | enlarged entries | GCL_size |
|---|---|---|---|
| sw01-p2 | 25 | 28 | 255 |
| sw01-p4 | 9 | 20 | 255 |
| sw01-p5 | 11 | 11 | 255 |
| sw02-p2 | 13 | 11 | 255 |
| sw02-p4 | 11 | 20 | 255 |
| sw02-p5 | 13 | 23 | 255 |
| sw03-p4 | 13 | 21 | 255 |
| sw03-p5 | 9 | 21 | 255 |
| sw04-p4 | 3 | 10 | 255 |
| sw04-p5 | 11 | 19 | 255 |
| sw05-p4 | 9 | 21 | 255 |
| sw05-p5 | 13 | 21 | 255 |
| sw06-p4 | 11 | 19 | 255 |
| sw06-p5 | 3 | 10 | 255 |
| sw07-p4 | 13 | 21 | 255 |
| sw07-p5 | 9 | 18 | 255 |
| sw08-p2 | 19 | 16 | 255 |
| sw08-p4 | 3 | 10 | 255 |
| sw08-p5 | 13 | 21 | 255 |

## Flows

| flow | route | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|
| s0(id=1 S3->S1) | S3->sw01->sw02->S1 | 6 | 24960 | 27920 | yes |
| s1(id=2 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | - | - | - | no |
| s2(id=3 S1->S3) | S1->sw02->sw01->S3 | 6 | 0 | 27920 | yes |
| s3(id=4 S1->S3) | S1->sw02->sw01->S3 | - | - | - | no |
| s4(id=5 S3->S1) | S3->sw01->sw02->S1 | 7 | 74880 | 31120 | yes |
| s5(id=6 S1->S3) | S1->sw02->sw01->S3 | - | - | - | no |
| s6(id=7 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 7 | 0 | 42960 | yes |
| s7(id=8 S1->S3) | S1->sw02->sw01->S3 | - | - | - | no |
| s8(id=9 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 7 | 0 | 50960 | yes |
| s9(id=10 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | 6 | 49920 | 43280 | yes |
| s10(id=11 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 7 | 24960 | 42960 | yes |
| s11(id=12 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 7 | 24960 | 45840 | yes |
| s12(id=13 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | - | - | - | no |
| s13(id=14 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | - | - | - | no |
| s14(id=15 S3->S1) | S3->sw01->sw02->S1 | 6 | 49920 | 26000 | yes |
| s15(id=16 S3->S1) | S3->sw01->sw02->S1 | - | - | - | no |
| s16(id=17 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 6 | 74880 | 43280 | yes |
| s17(id=18 S1->S3) | S1->sw02->sw01->S3 | 6 | 49920 | 30800 | yes |
| s18(id=19 S3->S1) | S3->sw01->sw02->S1 | - | - | - | no |
| s19(id=20 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | - | - | - | no |

## Per-hop windows (slack_ns > 0 means this window was enlarged)

| flow | egress port | queue | psi (ns) | delta (ns) |
|---|---|---|---|---|
| s0(id=1 S3->S1) | S3-p0 | Q6 | 24960 | 12480 |
| s0(id=1 S3->S1) | sw01-p5 | Q6 | 32640 | 12480 |
| s0(id=1 S3->S1) | sw02-p2 | Q6 | 40320 | 12480 |
| s2(id=3 S1->S3) | S1-p0 | Q6 | 0 | 12480 |
| s2(id=3 S1->S3) | sw02-p5 | Q6 | 7680 | 12480 |
| s2(id=3 S1->S3) | sw01-p2 | Q6 | 15360 | 12480 |
| s4(id=5 S3->S1) | S3-p0 | Q7 | 74880 | 12480 |
| s4(id=5 S3->S1) | sw01-p5 | Q7 | 82560 | 12480 |
| s4(id=5 S3->S1) | sw02-p2 | Q7 | 93440 | 12480 |
| s6(id=7 S2->S3) | S2-p0 | Q7 | 0 | 12480 |
| s6(id=7 S2->S3) | sw08-p5 | Q7 | 6080 | 12480 |
| s6(id=7 S2->S3) | sw07-p4 | Q7 | 12160 | 12480 |
| s6(id=7 S2->S3) | sw05-p5 | Q7 | 18240 | 12480 |
| s6(id=7 S2->S3) | sw03-p4 | Q7 | 24320 | 12480 |
| s6(id=7 S2->S3) | sw01-p2 | Q7 | 30400 | 12480 |
| s8(id=9 S3->S2) | S3-p0 | Q7 | 0 | 12480 |
| s8(id=9 S3->S2) | sw01-p4 | Q7 | 7680 | 12480 |
| s8(id=9 S3->S2) | sw03-p5 | Q7 | 15360 | 12480 |
| s8(id=9 S3->S2) | sw05-p4 | Q7 | 23040 | 12480 |
| s8(id=9 S3->S2) | sw07-p5 | Q7 | 30720 | 12480 |
| s8(id=9 S3->S2) | sw08-p2 | Q7 | 38400 | 12480 |
| s9(id=10 S2->S1) | S2-p0 | Q6 | 49920 | 12480 |
| s9(id=10 S2->S1) | sw08-p4 | Q6 | 57600 | 12480 |
| s9(id=10 S2->S1) | sw06-p5 | Q6 | 65280 | 12480 |
| s9(id=10 S2->S1) | sw04-p4 | Q6 | 72960 | 12480 |
| s9(id=10 S2->S1) | sw02-p2 | Q6 | 80640 | 12480 |
| s10(id=11 S2->S3) | S2-p0 | Q7 | 24960 | 12480 |
| s10(id=11 S2->S3) | sw08-p5 | Q7 | 31040 | 12480 |
| s10(id=11 S2->S3) | sw07-p4 | Q7 | 37120 | 12480 |
| s10(id=11 S2->S3) | sw05-p5 | Q7 | 43200 | 12480 |
| s10(id=11 S2->S3) | sw03-p4 | Q7 | 49280 | 12480 |
| s10(id=11 S2->S3) | sw01-p2 | Q7 | 55360 | 12480 |
| s11(id=12 S1->S2) | S1-p0 | Q7 | 24960 | 12480 |
| s11(id=12 S1->S2) | sw02-p4 | Q7 | 33280 | 12480 |
| s11(id=12 S1->S2) | sw04-p5 | Q7 | 41600 | 12480 |
| s11(id=12 S1->S2) | sw06-p4 | Q7 | 49920 | 12480 |
| s11(id=12 S1->S2) | sw08-p2 | Q7 | 58240 | 12480 |
| s14(id=15 S3->S1) | S3-p0 | Q6 | 49920 | 12480 |
| s14(id=15 S3->S1) | sw01-p5 | Q6 | 56640 | 12480 |
| s14(id=15 S3->S1) | sw02-p2 | Q6 | 63360 | 12480 |
| s16(id=17 S1->S2) | S1-p0 | Q6 | 74880 | 12480 |
| s16(id=17 S1->S2) | sw02-p4 | Q6 | 82560 | 12480 |
| s16(id=17 S1->S2) | sw04-p5 | Q6 | 90240 | 12480 |
| s16(id=17 S1->S2) | sw06-p4 | Q6 | 97920 | 12480 |
| s16(id=17 S1->S2) | sw08-p2 | Q6 | 105600 | 12480 |
| s17(id=18 S1->S3) | S1-p0 | Q6 | 49920 | 12480 |
| s17(id=18 S1->S3) | sw02-p5 | Q6 | 56000 | 12480 |
| s17(id=18 S1->S3) | sw01-p2 | Q6 | 68160 | 12480 |

## Constraint check

- C1-C7, C9: OK
- seed-integrity (no SMT-fixed flow's placement changed): OK

## GCL per egress port

### sw01-p2  (28 entries, util 18.7200 %)

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

### sw01-p4  (20 entries, util 6.2400 %)

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

### sw01-p5  (11 entries, util 7.8000 %)

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

### sw02-p2  (11 entries, util 9.3600 %)

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

### sw02-p4  (20 entries, util 7.8000 %)

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

### sw02-p5  (23 entries, util 9.3600 %)

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

### sw03-p4  (21 entries, util 9.3600 %)

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

### sw03-p5  (21 entries, util 6.2400 %)

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

### sw04-p4  (10 entries, util 1.5600 %)

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

### sw04-p5  (19 entries, util 7.8000 %)

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

### sw05-p4  (21 entries, util 6.2400 %)

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

### sw05-p5  (21 entries, util 9.3600 %)

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

### sw06-p4  (19 entries, util 7.8000 %)

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

### sw06-p5  (10 entries, util 1.5600 %)

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

### sw07-p4  (21 entries, util 9.3600 %)

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

### sw07-p5  (18 entries, util 6.2400 %)

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

### sw08-p2  (16 entries, util 14.0400 %)

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

### sw08-p4  (10 entries, util 1.5600 %)

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

### sw08-p5  (21 entries, util 9.3600 %)

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

