# Heuristic-enlarged GCL schedule (Problem 2: window enlargement)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Time-sensitive PCPs considered: [6, 7]
- Seeded from SMT run: **result/result-2026-10-12-dataset-testbed-7-ring-avgwin/smt-c9-on/7-fair-retimed-c9on**

## Admission (unchanged by this package -- it only widens windows)

SMT-fixed flows: **11**/11. This package never admits a flow itself; it banks slack for a later admission pass (`prob_3_admit`, Problem 3) to use.

## Opportunistic idle top-up (Step 7 -- see enlarge.py)

Total: **13330880 ns**, drawn from idle capacity on ports at or below utilisation 0.2, independent of any route's deadline-slack budget.

| port | queue | applied (ns) |
|---|---|---|
| S1-p0 | Q6 | 572480 |
| S1-p0 | Q7 | 45440 |
| S2-p0 | Q6 | 289920 |
| S2-p0 | Q7 | 293760 |
| S3-p0 | Q6 | 543040 |
| S3-p0 | Q7 | 18880 |
| sw01-p2 | Q7 | 700480 |
| sw01-p4 | Q6 | 712960 |
| sw01-p5 | Q6 | 191040 |
| sw01-p5 | Q7 | 456640 |
| sw02-p2 | Q6 | 127680 |
| sw02-p2 | Q7 | 417600 |
| sw02-p4 | Q6 | 566400 |
| sw02-p4 | Q7 | 50880 |
| sw03-p4 | Q7 | 713280 |
| sw03-p5 | Q6 | 708480 |
| sw04-p4 | Q6 | 677440 |
| sw04-p5 | Q6 | 559680 |
| sw04-p5 | Q7 | 56000 |
| sw05-p4 | Q6 | 704000 |
| sw05-p5 | Q7 | 725760 |
| sw06-p4 | Q6 | 545280 |
| sw06-p4 | Q7 | 68480 |
| sw06-p5 | Q6 | 692800 |
| sw07-p4 | Q7 | 737280 |
| sw07-p5 | Q6 | 699520 |
| sw08-p4 | Q6 | 707200 |
| sw08-p5 | Q7 | 748480 |

## Opportunistic window creation (Step 8 -- see enlarge.py)

**13** brand-new window(s) opened, **162240 ns** total, on ports at or below utilisation 0.2 whose TT queue had zero windows before this run.

| port | queue | size (ns) |
|---|---|---|
| sw01-p2 | Q6 | 12480 |
| sw01-p4 | Q7 | 12480 |
| sw02-p5 | Q6 | 12480 |
| sw02-p5 | Q7 | 12480 |
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

**7578560 ns** given back from Steps 7/8's growth so each port's leftover non-TAS gaps land close to equal, instead of one gap staying huge while a neighbour is squeezed to the bare 1-tick C10 minimum.

| port | given back (ns) |
|---|---|
| sw08-p5 | 516480 |
| sw01-p4 | 499200 |
| sw03-p5 | 499200 |
| sw05-p4 | 499200 |
| sw07-p5 | 499200 |
| sw01-p5 | 414080 |
| S2-p0 | 393280 |
| sw01-p2 | 387200 |
| sw03-p4 | 387200 |
| sw05-p5 | 387200 |
| sw07-p4 | 387200 |
| sw02-p2 | 367680 |
| sw06-p4 | 309120 |
| sw04-p5 | 303360 |
| sw02-p4 | 301440 |
| S1-p0 | 299520 |
| S3-p0 | 299520 |
| sw04-p4 | 262400 |
| sw06-p5 | 262400 |
| sw08-p4 | 262400 |
| sw08-p2 | 41280 |

## Opportunistic overlay window creation (Step 10 -- see enlarge.py)

**42** new overlay window(s), **8265600 ns** total, carved out of already-open best-effort spans on ports at or below utilisation 0.2 -- best-effort stays reachable inside each one (gate mask keeps its BE bits set), so none of this is closed off from BE.

| port | queue | size (ns) |
|---|---|---|
| S1-p0 | Q6 | 74880 |
| S1-p0 | Q7 | 224640 |
| S2-p0 | Q6 | 192960 |
| S2-p0 | Q7 | 200320 |
| S3-p0 | Q6 | 74880 |
| S3-p0 | Q7 | 224640 |
| sw01-p2 | Q6 | 214080 |
| sw01-p2 | Q7 | 200320 |
| sw01-p4 | Q6 | 292160 |
| sw01-p4 | Q7 | 224640 |
| sw01-p5 | Q6 | 160640 |
| sw01-p5 | Q7 | 199680 |
| sw02-p2 | Q6 | 72960 |
| sw02-p2 | Q7 | 220800 |
| sw02-p4 | Q6 | 52480 |
| sw02-p4 | Q7 | 181440 |
| sw02-p5 | Q6 | 374400 |
| sw02-p5 | Q7 | 400640 |
| sw03-p4 | Q6 | 197440 |
| sw03-p4 | Q7 | 200320 |
| sw03-p5 | Q6 | 297280 |
| sw03-p5 | Q7 | 224640 |
| sw04-p4 | Q6 | 149760 |
| sw04-p4 | Q7 | 150080 |
| sw04-p5 | Q6 | 55040 |
| sw04-p5 | Q7 | 188160 |
| sw05-p4 | Q6 | 302400 |
| sw05-p4 | Q7 | 224640 |
| sw05-p5 | Q6 | 199360 |
| sw05-p5 | Q7 | 200320 |
| sw06-p4 | Q6 | 150720 |
| sw06-p4 | Q7 | 144960 |
| sw06-p5 | Q6 | 141440 |
| sw06-p5 | Q7 | 150080 |
| sw07-p4 | Q6 | 186880 |
| sw07-p4 | Q7 | 200320 |
| sw07-p5 | Q6 | 307520 |
| sw07-p5 | Q7 | 224640 |
| sw08-p4 | Q6 | 133120 |
| sw08-p4 | Q7 | 150080 |
| sw08-p5 | Q6 | 199680 |
| sw08-p5 | Q7 | 300160 |

## Candidate routes (P^cand = routes of the fixed flows above)

| route | PCPs carried | flows |
|---|---|---|
| S1->sw02->sw04->sw06->sw08->S2 | Q6 (3), Q7 (2) | 5 |
| S2->sw08->sw06->sw04->sw02->S1 | Q6 (1) | 1 |
| S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 (1) | 1 |
| S3->sw01->sw02->S1 | Q6 (1), Q7 (2) | 3 |
| S3->sw01->sw03->sw05->sw07->sw08->S2 | Q6 (1) | 1 |

## Per-link enlargement accounting

| link | sharing eta | route-safe slack (ns) | link budget (ns) | final slack (ns) | applied (ns) |
|---|---|---|---|---|---|
| S2-p0 | 2 | Q6:120416, Q7:106367 | 226783 | Q6:72687, Q7:106367 | Q6:365120, Q7:397440 |
| S3-p0 | 2 | Q6:32448, Q7:68159 | 100607 | Q6:32448, Q7:56097 | Q6:425600, Q7:224640 |
| sw02-p2 | 2 | Q6:107741, Q7:40648 | 148389 | Q6:91748, Q7:40648 | Q6:154880, Q7:448640 |
| sw08-p2 | 2 | Q6:52556, Q7:48439 | 100994 | Q6:52556, Q7:28364 | Q6:39360 |
| S1-p0 | 1 | Q6:15615, Q7:20157 | 35772 | Q6:15615, Q7:17160 | Q6:425600, Q7:224640 |
| sw01-p2 | 1 | Q6:0, Q7:33164 | 33164 | Q7:33164 | Q6:226560, Q7:546560 |
| sw01-p4 | 1 | Q6:7053, Q7:0 | 7053 | Q6:7053 | Q6:512960, Q7:237120 |
| sw01-p5 | 1 | Q6:47510, Q7:16591 | 64101 | Q6:31305, Q7:16591 | Q6:227200, Q7:414080 |
| sw02-p4 | 1 | Q6:13088, Q7:16614 | 29702 | Q6:13088, Q7:14124 | Q6:395200, Q7:181440 |
| sw03-p4 | 1 | Q6:0, Q7:28571 | 28571 | Q7:28571 | Q6:209920, Q7:554880 |
| sw03-p5 | 1 | Q6:6406, Q7:0 | 6406 | Q6:6406 | Q6:512960, Q7:237120 |
| sw04-p4 | 1 | Q6:60198, Q7:0 | 60198 | Q6:60198 | Q6:624960, Q7:162560 |
| sw04-p5 | 1 | Q6:10970, Q7:13694 | 24664 | Q6:10970, Q7:11626 | Q6:389760, Q7:188160 |
| sw05-p4 | 1 | Q6:5818, Q7:0 | 5818 | Q6:5818 | Q6:512960, Q7:237120 |
| sw05-p5 | 1 | Q6:0, Q7:24614 | 24614 | Q7:24614 | Q6:211840, Q7:563200 |
| sw06-p4 | 1 | Q6:9194, Q7:11287 | 20481 | Q6:9194, Q7:9569 | Q6:473600, Q7:144960 |
| sw06-p5 | 1 | Q6:53309, Q7:0 | 53309 | Q6:53309 | Q6:624960, Q7:162560 |
| sw07-p4 | 1 | Q6:0, Q7:21206 | 21206 | Q7:21206 | Q6:199360, Q7:571520 |
| sw07-p5 | 1 | Q6:5284, Q7:0 | 5284 | Q6:5284 | Q6:512960, Q7:237120 |
| sw08-p4 | 1 | Q6:47208, Q7:0 | 47208 | Q6:47208 | Q6:624960, Q7:162560 |
| sw08-p5 | 1 | Q6:0, Q7:18269 | 18269 | Q7:18269 | Q6:199680, Q7:550400 |

Total applied: **15117120 ns** across 22 port(s). Network total slack now banked: **15141440 ns**. GCL_size overflow: 0.

## Per-port GCL entries: before (SMT) vs. after (heuristic-enlarged)

| port | SMT entries | enlarged entries | GCL_size |
|---|---|---|---|
| sw01-p2 | 5 | 13 | 255 |
| sw01-p4 | 9 | 18 | 255 |
| sw01-p5 | 17 | 26 | 255 |
| sw02-p2 | 19 | 28 | 255 |
| sw02-p4 | 25 | 28 | 255 |
| sw02-p5 | 1 | 18 | 255 |
| sw03-p4 | 5 | 13 | 255 |
| sw03-p5 | 9 | 18 | 255 |
| sw04-p4 | 3 | 9 | 255 |
| sw04-p5 | 25 | 28 | 255 |
| sw05-p4 | 9 | 18 | 255 |
| sw05-p5 | 5 | 13 | 255 |
| sw06-p4 | 25 | 24 | 255 |
| sw06-p5 | 3 | 9 | 255 |
| sw07-p4 | 5 | 13 | 255 |
| sw07-p5 | 9 | 18 | 255 |
| sw08-p2 | 33 | 21 | 255 |
| sw08-p4 | 3 | 9 | 255 |
| sw08-p5 | 5 | 15 | 255 |

## Flows

| flow | route | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|
| s0(id=1 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 7 | 0 | 36880 | yes |
| s1(id=2 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | - | - | - | no |
| s2(id=3 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 7 | 0 | 54160 | yes |
| s3(id=4 S1->S3) | S1->sw02->sw01->S3 | - | - | - | no |
| s4(id=5 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 7 | 74880 | 36880 | yes |
| s5(id=6 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | - | - | - | no |
| s6(id=7 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | 6 | 24960 | 45840 | yes |
| s7(id=8 S3->S1) | S3->sw01->sw02->S1 | 7 | 49920 | 33680 | yes |
| s8(id=9 S3->S1) | S3->sw01->sw02->S1 | 7 | 0 | 22800 | yes |
| s9(id=10 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | - | - | - | no |
| s10(id=11 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | - | - | - | no |
| s11(id=12 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 6 | 24960 | 50960 | yes |
| s12(id=13 S1->S3) | S1->sw02->sw01->S3 | - | - | - | no |
| s13(id=14 S3->S1) | S3->sw01->sw02->S1 | - | - | - | no |
| s14(id=15 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 6 | 49920 | 39440 | yes |
| s15(id=16 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | - | - | - | no |
| s16(id=17 S1->S3) | S1->sw02->sw01->S3 | - | - | - | no |
| s17(id=18 S3->S1) | S3->sw01->sw02->S1 | 6 | 74880 | 26000 | yes |
| s18(id=19 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 6 | 99840 | 36880 | yes |
| s19(id=20 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 6 | 24960 | 38160 | yes |

## Per-hop windows (slack_ns > 0 means this window was enlarged)

| flow | egress port | queue | psi (ns) | delta (ns) |
|---|---|---|---|---|
| s0(id=1 S1->S2) | S1-p0 | Q7 | 0 | 12480 |
| s0(id=1 S1->S2) | sw02-p4 | Q7 | 6080 | 12480 |
| s0(id=1 S1->S2) | sw04-p5 | Q7 | 12160 | 12480 |
| s0(id=1 S1->S2) | sw06-p4 | Q7 | 18240 | 12480 |
| s0(id=1 S1->S2) | sw08-p2 | Q7 | 24320 | 12480 |
| s2(id=3 S2->S3) | S2-p0 | Q7 | 0 | 12480 |
| s2(id=3 S2->S3) | sw08-p5 | Q7 | 8320 | 12480 |
| s2(id=3 S2->S3) | sw07-p4 | Q7 | 16640 | 12480 |
| s2(id=3 S2->S3) | sw05-p5 | Q7 | 24960 | 12480 |
| s2(id=3 S2->S3) | sw03-p4 | Q7 | 33280 | 12480 |
| s2(id=3 S2->S3) | sw01-p2 | Q7 | 41600 | 12480 |
| s4(id=5 S1->S2) | S1-p0 | Q7 | 74880 | 12480 |
| s4(id=5 S1->S2) | sw02-p4 | Q7 | 80960 | 12480 |
| s4(id=5 S1->S2) | sw04-p5 | Q7 | 87040 | 12480 |
| s4(id=5 S1->S2) | sw06-p4 | Q7 | 93120 | 12480 |
| s4(id=5 S1->S2) | sw08-p2 | Q7 | 99200 | 12480 |
| s6(id=7 S2->S1) | S2-p0 | Q6 | 24960 | 12480 |
| s6(id=7 S2->S1) | sw08-p4 | Q6 | 33280 | 12480 |
| s6(id=7 S2->S1) | sw06-p5 | Q6 | 41600 | 12480 |
| s6(id=7 S2->S1) | sw04-p4 | Q6 | 49920 | 12480 |
| s6(id=7 S2->S1) | sw02-p2 | Q6 | 58240 | 12480 |
| s7(id=8 S3->S1) | S3-p0 | Q7 | 49920 | 12480 |
| s7(id=8 S3->S1) | sw01-p5 | Q7 | 58240 | 12480 |
| s7(id=8 S3->S1) | sw02-p2 | Q7 | 71040 | 12480 |
| s8(id=9 S3->S1) | S3-p0 | Q7 | 0 | 12480 |
| s8(id=9 S3->S1) | sw01-p5 | Q7 | 5120 | 12480 |
| s8(id=9 S3->S1) | sw02-p2 | Q7 | 10240 | 12480 |
| s11(id=12 S1->S2) | S1-p0 | Q6 | 24960 | 12480 |
| s11(id=12 S1->S2) | sw02-p4 | Q6 | 31680 | 12480 |
| s11(id=12 S1->S2) | sw04-p5 | Q6 | 38400 | 12480 |
| s11(id=12 S1->S2) | sw06-p4 | Q6 | 47040 | 12480 |
| s11(id=12 S1->S2) | sw08-p2 | Q6 | 63360 | 12480 |
| s14(id=15 S1->S2) | S1-p0 | Q6 | 49920 | 12480 |
| s14(id=15 S1->S2) | sw02-p4 | Q6 | 56640 | 12480 |
| s14(id=15 S1->S2) | sw04-p5 | Q6 | 63360 | 12480 |
| s14(id=15 S1->S2) | sw06-p4 | Q6 | 70080 | 12480 |
| s14(id=15 S1->S2) | sw08-p2 | Q6 | 76800 | 12480 |
| s17(id=18 S3->S1) | S3-p0 | Q6 | 74880 | 12480 |
| s17(id=18 S3->S1) | sw01-p5 | Q6 | 81600 | 12480 |
| s17(id=18 S3->S1) | sw02-p2 | Q6 | 88320 | 12480 |
| s18(id=19 S1->S2) | S1-p0 | Q6 | 99840 | 12480 |
| s18(id=19 S1->S2) | sw02-p4 | Q6 | 105920 | 12480 |
| s18(id=19 S1->S2) | sw04-p5 | Q6 | 112000 | 12480 |
| s18(id=19 S1->S2) | sw06-p4 | Q6 | 118080 | 12480 |
| s18(id=19 S1->S2) | sw08-p2 | Q6 | 124160 | 12480 |
| s19(id=20 S3->S2) | S3-p0 | Q6 | 24960 | 12480 |
| s19(id=20 S3->S2) | sw01-p4 | Q6 | 30080 | 12480 |
| s19(id=20 S3->S2) | sw03-p5 | Q6 | 35200 | 12480 |
| s19(id=20 S3->S2) | sw05-p4 | Q6 | 40320 | 12480 |
| s19(id=20 S3->S2) | sw07-p5 | Q6 | 45440 | 12480 |
| s19(id=20 S3->S2) | sw08-p2 | Q6 | 50560 | 12480 |

## Constraint check

- C1-C7, C9: OK
- seed-integrity (no SMT-fixed flow's placement changed): OK

## GCL per egress port

### sw01-p2  (13 entries, util 3.1200 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 29120 0x7F # 01111111   Q6
sgs 206400 0x80 # 10000000   Q7
sgs 1920 0x3F # 00111111   BE
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 164800 0x80 # 10000000   Q7
sgs 43520 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p4  (18 entries, util 6.2400 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 17600 0x7F # 01111111   Q6
sgs 75200 0x40 # 01000000   Q6
sgs 44800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 30080 0x7F # 01111111   Q6
sgs 75200 0x40 # 01000000   Q6
sgs 44800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 30080 0x7F # 01111111   Q6
sgs 75200 0x40 # 01000000   Q6
sgs 44800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 30080 0x7F # 01111111   Q6
sgs 45120 0x40 # 01000000   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p5  (26 entries, util 12.4800 %)

```
sgs 5120 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 32320 0x7F # 01111111   Q6
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 10880 0x3F # 00111111   BE
sgs 45760 0x40 # 01000000   Q6
sgs 22720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 5120 0x3F # 00111111   BE
sgs 122240 0x80 # 10000000   Q7
sgs 22720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 5120 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 32320 0x7F # 01111111   Q6
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 10880 0x3F # 00111111   BE
sgs 45760 0x40 # 01000000   Q6
sgs 22720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 5120 0x3F # 00111111   BE
sgs 117120 0x80 # 10000000   Q7
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (28 entries, util 14.0400 %)

```
sgs 10240 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 27200 0x7F # 01111111   Q6
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 4800 0x3F # 00111111   BE
sgs 53440 0x40 # 01000000   Q6
sgs 8320 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 10240 0x3F # 00111111   BE
sgs 131520 0x80 # 10000000   Q7
sgs 8320 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 10240 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 27200 0x7F # 01111111   Q6
sgs 21120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 4800 0x3F # 00111111   BE
sgs 53440 0x40 # 01000000   Q6
sgs 8320 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 10240 0x3F # 00111111   BE
sgs 121280 0x80 # 10000000   Q7
sgs 18560 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p4  (28 entries, util 18.7200 %)

```
sgs 6080 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 11840 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 50240 0x40 # 01000000   Q6
sgs 43840 0xBF # 10111111   Q7
sgs 6080 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0x7F # 01111111   Q6
sgs 124480 0x40 # 01000000   Q6
sgs 43840 0xBF # 10111111   Q7
sgs 6080 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 99520 0x40 # 01000000   Q6
sgs 43840 0xBF # 10111111   Q7
sgs 6080 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0x7F # 01111111   Q6
sgs 118400 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p5  (18 entries, util 0.0000 %)

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

### sw03-p4  (13 entries, util 3.1200 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 206400 0x80 # 10000000   Q7
sgs 10240 0x3F # 00111111   BE
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 173120 0x80 # 10000000   Q7
sgs 43520 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p5  (18 entries, util 6.2400 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 22720 0x7F # 01111111   Q6
sgs 75200 0x40 # 01000000   Q6
sgs 39680 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 35200 0x7F # 01111111   Q6
sgs 75200 0x40 # 01000000   Q6
sgs 39680 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 35200 0x7F # 01111111   Q6
sgs 75200 0x40 # 01000000   Q6
sgs 39680 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 35200 0x7F # 01111111   Q6
sgs 40000 0x40 # 01000000   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p4  (9 entries, util 1.5600 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 487680 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (28 entries, util 18.7200 %)

```
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13760 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 50240 0x40 # 01000000   Q6
sgs 37760 0xBF # 10111111   Q7
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13760 0x7F # 01111111   Q6
sgs 123840 0x40 # 01000000   Q6
sgs 37760 0xBF # 10111111   Q7
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13760 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 98880 0x40 # 01000000   Q6
sgs 37760 0xBF # 10111111   Q7
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13760 0x7F # 01111111   Q6
sgs 111680 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (18 entries, util 6.2400 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 27840 0x7F # 01111111   Q6
sgs 75200 0x40 # 01000000   Q6
sgs 34560 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 40320 0x7F # 01111111   Q6
sgs 75200 0x40 # 01000000   Q6
sgs 34560 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 40320 0x7F # 01111111   Q6
sgs 75200 0x40 # 01000000   Q6
sgs 34560 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 40320 0x7F # 01111111   Q6
sgs 34880 0x40 # 01000000   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p5  (13 entries, util 3.1200 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 206400 0x80 # 10000000   Q7
sgs 18560 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 181440 0x80 # 10000000   Q7
sgs 43520 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p4  (24 entries, util 18.7200 %)

```
sgs 18240 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 16320 0x7F # 01111111   Q6
sgs 35520 0x40 # 01000000   Q6
sgs 10560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 50240 0x40 # 01000000   Q6
sgs 31680 0xBF # 10111111   Q7
sgs 18240 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 16320 0x7F # 01111111   Q6
sgs 121280 0x40 # 01000000   Q6
sgs 31680 0xBF # 10111111   Q7
sgs 18240 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 16320 0x7F # 01111111   Q6
sgs 121280 0x40 # 01000000   Q6
sgs 31680 0xBF # 10111111   Q7
sgs 18240 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 16320 0x7F # 01111111   Q6
sgs 103040 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (9 entries, util 1.5600 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 496000 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (13 entries, util 3.1200 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 206400 0x80 # 10000000   Q7
sgs 26880 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 189760 0x80 # 10000000   Q7
sgs 43520 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p5  (18 entries, util 6.2400 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 32960 0x7F # 01111111   Q6
sgs 75200 0x40 # 01000000   Q6
sgs 29440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 45440 0x7F # 01111111   Q6
sgs 75200 0x40 # 01000000   Q6
sgs 29440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 45440 0x7F # 01111111   Q6
sgs 75200 0x40 # 01000000   Q6
sgs 29440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 45440 0x7F # 01111111   Q6
sgs 29760 0x40 # 01000000   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p2  (21 entries, util 24.9600 %)

```
sgs 24320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13760 0x3F # 00111111   BE
sgs 38720 0x40 # 01000000   Q6
sgs 9920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 38400 0x40 # 01000000   Q6
sgs 61760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13760 0x3F # 00111111   BE
sgs 29760 0x40 # 01000000   Q6
sgs 144000 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13760 0x3F # 00111111   BE
sgs 43200 0x40 # 01000000   Q6
sgs 130560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13760 0x3F # 00111111   BE
sgs 29760 0x40 # 01000000   Q6
sgs 119680 0x3F # 00111111   BE
```

### sw08-p4  (9 entries, util 1.5600 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 504320 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (15 entries, util 3.1200 %)

```
sgs 8320 0x3F # 00111111   BE
sgs 141760 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 8320 0x3F # 00111111   BE
sgs 133440 0x80 # 10000000   Q7
sgs 8320 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

