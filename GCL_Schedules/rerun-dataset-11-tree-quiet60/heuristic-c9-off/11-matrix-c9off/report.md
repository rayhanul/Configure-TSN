# Heuristic-enlarged GCL schedule (Problem 2: window enlargement)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Time-sensitive PCPs considered: [6, 7]
- Seeded from SMT run: **result/result-2026-10-13-dataset-testbed-11-tree-avgwin/smt-c9-off/11-t3600-c9off-minlat**

## Admission (unchanged by this package -- it only widens windows)

SMT-fixed flows: **10**/20. This package never admits a flow itself; it banks slack for a later admission pass (`prob_3_admit`, Problem 3) to use.

## Opportunistic idle top-up (Step 7 -- see enlarge.py)

Total: **12027840 ns**, drawn from idle capacity on ports at or below utilisation 0.2, independent of any route's deadline-slack budget.

| port | queue | applied (ns) |
|---|---|---|
| S1-p0 | Q6 | 386240 |
| S1-p0 | Q7 | 271680 |
| S2-p0 | Q7 | 702720 |
| S3-p0 | Q6 | 384640 |
| S3-p0 | Q7 | 244800 |
| sw01-p2 | Q7 | 577600 |
| sw01-p4 | Q6 | 370240 |
| sw01-p4 | Q7 | 246400 |
| sw02-p2 | Q7 | 626240 |
| sw02-p4 | Q6 | 371520 |
| sw02-p4 | Q7 | 276160 |
| sw03-p4 | Q7 | 600320 |
| sw03-p5 | Q6 | 355520 |
| sw03-p5 | Q7 | 249600 |
| sw04-p4 | Q7 | 647040 |
| sw04-p5 | Q6 | 356160 |
| sw04-p5 | Q7 | 279680 |
| sw05-p4 | Q6 | 340800 |
| sw05-p4 | Q7 | 252160 |
| sw05-p5 | Q7 | 622400 |
| sw06-p4 | Q6 | 341120 |
| sw06-p4 | Q7 | 282880 |
| sw06-p5 | Q7 | 666880 |
| sw07-p4 | Q7 | 644160 |
| sw07-p5 | Q6 | 325440 |
| sw07-p5 | Q7 | 254080 |
| sw08-p4 | Q7 | 686080 |
| sw08-p5 | Q7 | 665280 |

## Opportunistic window creation (Step 8 -- see enlarge.py)

**9** brand-new window(s) opened, **112320 ns** total, on ports at or below utilisation 0.2 whose TT queue had zero windows before this run.

| port | queue | size (ns) |
|---|---|---|
| sw01-p2 | Q6 | 12480 |
| sw02-p2 | Q6 | 12480 |
| sw03-p4 | Q6 | 12480 |
| sw04-p4 | Q6 | 12480 |
| sw05-p5 | Q6 | 12480 |
| sw06-p5 | Q6 | 12480 |
| sw07-p4 | Q6 | 12480 |
| sw08-p4 | Q6 | 12480 |
| sw08-p5 | Q6 | 12480 |

## Best-effort gap equalization (Step 9 -- see enlarge.py)

**6672320 ns** given back from Steps 7/8's growth so each port's leftover non-TAS gaps land close to equal, instead of one gap staying huge while a neighbour is squeezed to the bare 1-tick C10 minimum.

| port | given back (ns) |
|---|---|
| sw02-p2 | 470720 |
| sw04-p4 | 470720 |
| sw06-p5 | 470720 |
| sw08-p4 | 470720 |
| S2-p0 | 450880 |
| sw06-p4 | 371200 |
| sw02-p4 | 360960 |
| sw04-p5 | 360960 |
| S1-p0 | 360960 |
| sw01-p4 | 307520 |
| sw03-p5 | 307520 |
| sw05-p4 | 307520 |
| sw07-p5 | 307520 |
| S3-p0 | 307520 |
| sw01-p2 | 262400 |
| sw03-p4 | 262400 |
| sw05-p5 | 262400 |
| sw07-p4 | 262400 |
| sw08-p5 | 262400 |
| sw08-p2 | 34880 |

## Opportunistic overlay window creation (Step 10 -- see enlarge.py)

**38** new overlay window(s), **7271680 ns** total, carved out of already-open best-effort spans on ports at or below utilisation 0.2 -- best-effort stays reachable inside each one (gate mask keeps its BE bits set), so none of this is closed off from BE.

| port | queue | size (ns) |
|---|---|---|
| S1-p0 | Q6 | 161280 |
| S1-p0 | Q7 | 199680 |
| S2-p0 | Q6 | 224640 |
| S2-p0 | Q7 | 212160 |
| S3-p0 | Q6 | 74880 |
| S3-p0 | Q7 | 212160 |
| sw01-p2 | Q6 | 195200 |
| sw01-p2 | Q7 | 200320 |
| sw01-p4 | Q6 | 116480 |
| sw01-p4 | Q7 | 202560 |
| sw02-p2 | Q6 | 296000 |
| sw02-p2 | Q7 | 216000 |
| sw02-p4 | Q6 | 119360 |
| sw02-p4 | Q7 | 224640 |
| sw03-p4 | Q6 | 178560 |
| sw03-p4 | Q7 | 200320 |
| sw03-p5 | Q6 | 133120 |
| sw03-p5 | Q7 | 140160 |
| sw04-p4 | Q6 | 316160 |
| sw04-p4 | Q7 | 191680 |
| sw04-p5 | Q6 | 160960 |
| sw04-p5 | Q7 | 208320 |
| sw05-p4 | Q6 | 212160 |
| sw05-p4 | Q7 | 124800 |
| sw05-p5 | Q6 | 149760 |
| sw05-p5 | Q7 | 200320 |
| sw06-p4 | Q6 | 227520 |
| sw06-p4 | Q7 | 184000 |
| sw06-p5 | Q6 | 248960 |
| sw06-p5 | Q7 | 238400 |
| sw07-p4 | Q6 | 149760 |
| sw07-p4 | Q7 | 195840 |
| sw07-p5 | Q6 | 202560 |
| sw07-p5 | Q7 | 166400 |
| sw08-p4 | Q6 | 178240 |
| sw08-p4 | Q7 | 279360 |
| sw08-p5 | Q6 | 149760 |
| sw08-p5 | Q7 | 179200 |

## Candidate routes (P^cand = routes of the fixed flows above)

| route | PCPs carried | flows |
|---|---|---|
| S1->sw02->sw04->sw06->sw08->S2 | Q6 (1), Q7 (2) | 3 |
| S2->sw08->sw06->sw04->sw02->S1 | Q7 (2) | 2 |
| S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 (1) | 1 |
| S3->sw01->sw03->sw05->sw07->sw08->S2 | Q6 (2), Q7 (1) | 3 |
| S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q7 (1) | 1 |

## Per-link enlargement accounting

| link | sharing eta | route-safe slack (ns) | link budget (ns) | final slack (ns) | applied (ns) |
|---|---|---|---|---|---|
| S2-p0 | 2 | Q6:0, Q7:22602 | 22602 | Q7:22602 | Q6:224640, Q7:486400 |
| S3-p0 | 2 | Q6:15506, Q7:25177 | 40683 | Q6:15506, Q7:18229 | Q6:289920, Q7:352320 |
| sw01-p4 | 2 | Q6:13186, Q7:22685 | 35870 | Q6:13186, Q7:16587 | Q6:314880, Q7:342720 |
| sw02-p2 | 2 | Q6:0, Q7:19975 | 19975 | Q7:19975 | Q6:308480, Q7:391360 |
| sw03-p5 | 2 | Q6:11212, Q7:18461 | 29673 | Q6:11212, Q7:13399 | Q6:314880, Q7:280320 |
| sw04-p4 | 2 | Q6:0, Q7:15915 | 15915 | Q7:15915 | Q6:328640, Q7:383680 |
| sw05-p4 | 2 | Q6:9534, Q7:15058 | 24592 | Q6:9534, Q7:10851 | Q6:377280, Q7:264960 |
| sw06-p5 | 2 | Q6:0, Q7:12680 | 12680 | Q7:12680 | Q6:261440, Q7:447040 |
| sw07-p5 | 2 | Q6:8107, Q7:12312 | 20419 | Q6:8107, Q7:8813 | Q6:351040, Q7:306560 |
| sw08-p2 | 2 | Q6:11588, Q7:126021 | 137609 | Q6:11588, Q7:110930 | Q6:1920, Q7:85440 |
| sw08-p4 | 2 | Q6:0, Q7:10103 | 10103 | Q7:10103 | Q6:190720, Q7:504640 |
| S1-p0 | 1 | Q6:13916, Q7:28503 | 42420 | Q6:13916, Q7:28503 | Q6:380800, Q7:319360 |
| sw01-p2 | 1 | Q6:0, Q7:64532 | 64532 | Q7:64532 | Q6:207680, Q7:579840 |
| sw02-p4 | 1 | Q6:12144, Q7:24222 | 36366 | Q6:12144, Q7:24222 | Q6:322240, Q7:344320 |
| sw03-p4 | 1 | Q6:0, Q7:58422 | 58422 | Q7:58422 | Q6:191040, Q7:596480 |
| sw04-p5 | 1 | Q6:10598, Q7:20583 | 31181 | Q6:10598, Q7:20583 | Q6:347200, Q7:328000 |
| sw05-p5 | 1 | Q6:0, Q7:52892 | 52892 | Q7:52892 | Q6:162240, Q7:613120 |
| sw06-p4 | 1 | Q6:9249, Q7:17491 | 26739 | Q6:9249, Q7:17491 | Q6:397120, Q7:293440 |
| sw07-p4 | 1 | Q6:0, Q7:47884 | 47884 | Q7:47884 | Q6:162240, Q7:625280 |
| sw08-p5 | 1 | Q6:0, Q7:43351 | 43351 | Q7:43351 | Q6:162240, Q7:625280 |

Total applied: **13467200 ns** across 20 port(s). Network total slack now banked: **13483840 ns**. GCL_size overflow: 0.

## Per-port GCL entries: before (SMT) vs. after (heuristic-enlarged)

| port | SMT entries | enlarged entries | GCL_size |
|---|---|---|---|
| sw01-p2 | 3 | 11 | 255 |
| sw01-p4 | 23 | 27 | 255 |
| sw02-p2 | 15 | 27 | 255 |
| sw02-p4 | 17 | 24 | 255 |
| sw03-p4 | 3 | 11 | 255 |
| sw03-p5 | 23 | 27 | 255 |
| sw04-p4 | 15 | 24 | 255 |
| sw04-p5 | 17 | 21 | 255 |
| sw05-p4 | 23 | 27 | 255 |
| sw05-p5 | 3 | 11 | 255 |
| sw06-p4 | 17 | 23 | 255 |
| sw06-p5 | 15 | 23 | 255 |
| sw07-p4 | 3 | 10 | 255 |
| sw07-p5 | 23 | 28 | 255 |
| sw08-p2 | 35 | 27 | 255 |
| sw08-p4 | 15 | 26 | 255 |
| sw08-p5 | 3 | 10 | 255 |

## Flows

| flow | route | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|
| s0(id=1 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 6 | 0 | 79120 | yes |
| s1(id=2 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 6 | 0 | 95760 | yes |
| s2(id=3 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 7 | 24960 | 83600 | yes |
| s3(id=4 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | - | - | - | no |
| s4(id=5 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | 7 | 0 | 79120 | yes |
| s5(id=6 S3->S1) | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | - | - | - | no |
| s6(id=7 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | 7 | 37440 | 79120 | yes |
| s7(id=8 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 6 | 24960 | 96400 | yes |
| s8(id=9 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 7 | 74880 | 95760 | yes |
| s9(id=10 S3->S1) | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | 7 | 49920 | 145680 | yes |
| s10(id=11 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | - | - | - | no |
| s11(id=12 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | - | - | - | no |
| s12(id=13 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | - | - | - | no |
| s13(id=14 S3->S1) | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | - | - | - | no |
| s14(id=15 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | - | - | - | no |
| s15(id=16 S3->S1) | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | - | - | - | no |
| s16(id=17 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | - | - | - | no |
| s17(id=18 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 7 | 62400 | 95760 | yes |
| s18(id=19 S3->S1) | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | - | - | - | no |
| s19(id=20 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 7 | 49920 | 84240 | yes |

## Per-hop windows (slack_ns > 0 means this window was enlarged)

| flow | egress port | queue | psi (ns) | delta (ns) |
|---|---|---|---|---|
| s0(id=1 S1->S2) | S1-p0 | Q6 | 0 | 12480 |
| s0(id=1 S1->S2) | sw02-p4 | Q6 | 16640 | 12480 |
| s0(id=1 S1->S2) | sw04-p5 | Q6 | 33280 | 12480 |
| s0(id=1 S1->S2) | sw06-p4 | Q6 | 49920 | 12480 |
| s0(id=1 S1->S2) | sw08-p2 | Q6 | 66560 | 12480 |
| s1(id=2 S3->S2) | S3-p0 | Q6 | 0 | 12480 |
| s1(id=2 S3->S2) | sw01-p4 | Q6 | 16640 | 12480 |
| s1(id=2 S3->S2) | sw03-p5 | Q6 | 33280 | 12480 |
| s1(id=2 S3->S2) | sw05-p4 | Q6 | 49920 | 12480 |
| s1(id=2 S3->S2) | sw07-p5 | Q6 | 66560 | 12480 |
| s1(id=2 S3->S2) | sw08-p2 | Q6 | 83200 | 12480 |
| s2(id=3 S1->S2) | S1-p0 | Q7 | 24960 | 12480 |
| s2(id=3 S1->S2) | sw02-p4 | Q7 | 41600 | 12480 |
| s2(id=3 S1->S2) | sw04-p5 | Q7 | 58240 | 12480 |
| s2(id=3 S1->S2) | sw06-p4 | Q7 | 74880 | 12480 |
| s2(id=3 S1->S2) | sw08-p2 | Q7 | 96000 | 12480 |
| s4(id=5 S2->S1) | S2-p0 | Q7 | 0 | 12480 |
| s4(id=5 S2->S1) | sw08-p4 | Q7 | 16640 | 12480 |
| s4(id=5 S2->S1) | sw06-p5 | Q7 | 33280 | 12480 |
| s4(id=5 S2->S1) | sw04-p4 | Q7 | 49920 | 12480 |
| s4(id=5 S2->S1) | sw02-p2 | Q7 | 66560 | 12480 |
| s6(id=7 S2->S1) | S2-p0 | Q7 | 37440 | 12480 |
| s6(id=7 S2->S1) | sw08-p4 | Q7 | 54080 | 12480 |
| s6(id=7 S2->S1) | sw06-p5 | Q7 | 70720 | 12480 |
| s6(id=7 S2->S1) | sw04-p4 | Q7 | 87360 | 12480 |
| s6(id=7 S2->S1) | sw02-p2 | Q7 | 104000 | 12480 |
| s7(id=8 S3->S2) | S3-p0 | Q6 | 24960 | 12480 |
| s7(id=8 S3->S2) | sw01-p4 | Q6 | 41600 | 12480 |
| s7(id=8 S3->S2) | sw03-p5 | Q6 | 58240 | 12480 |
| s7(id=8 S3->S2) | sw05-p4 | Q6 | 74880 | 12480 |
| s7(id=8 S3->S2) | sw07-p5 | Q6 | 91520 | 12480 |
| s7(id=8 S3->S2) | sw08-p2 | Q6 | 108800 | 12480 |
| s8(id=9 S3->S2) | S3-p0 | Q7 | 74880 | 12480 |
| s8(id=9 S3->S2) | sw01-p4 | Q7 | 91520 | 12480 |
| s8(id=9 S3->S2) | sw03-p5 | Q7 | 108160 | 12480 |
| s8(id=9 S3->S2) | sw05-p4 | Q7 | 124800 | 12480 |
| s8(id=9 S3->S2) | sw07-p5 | Q7 | 141440 | 12480 |
| s8(id=9 S3->S2) | sw08-p2 | Q7 | 158080 | 12480 |
| s9(id=10 S3->S1) | S3-p0 | Q7 | 49920 | 12480 |
| s9(id=10 S3->S1) | sw01-p4 | Q7 | 66560 | 12480 |
| s9(id=10 S3->S1) | sw03-p5 | Q7 | 83200 | 12480 |
| s9(id=10 S3->S1) | sw05-p4 | Q7 | 99840 | 12480 |
| s9(id=10 S3->S1) | sw07-p5 | Q7 | 116480 | 12480 |
| s9(id=10 S3->S1) | sw08-p4 | Q7 | 133120 | 12480 |
| s9(id=10 S3->S1) | sw06-p5 | Q7 | 149760 | 12480 |
| s9(id=10 S3->S1) | sw04-p4 | Q7 | 166400 | 12480 |
| s9(id=10 S3->S1) | sw02-p2 | Q7 | 183040 | 12480 |
| s17(id=18 S2->S3) | S2-p0 | Q7 | 62400 | 12480 |
| s17(id=18 S2->S3) | sw08-p5 | Q7 | 79040 | 12480 |
| s17(id=18 S2->S3) | sw07-p4 | Q7 | 95680 | 12480 |
| s17(id=18 S2->S3) | sw05-p5 | Q7 | 112320 | 12480 |
| s17(id=18 S2->S3) | sw03-p4 | Q7 | 128960 | 12480 |
| s17(id=18 S2->S3) | sw01-p2 | Q7 | 145600 | 12480 |
| s19(id=20 S1->S2) | S1-p0 | Q7 | 49920 | 12480 |
| s19(id=20 S1->S2) | sw02-p4 | Q7 | 66560 | 12480 |
| s19(id=20 S1->S2) | sw04-p5 | Q7 | 83200 | 12480 |
| s19(id=20 S1->S2) | sw06-p4 | Q7 | 104960 | 12480 |
| s19(id=20 S1->S2) | sw08-p2 | Q7 | 121600 | 12480 |

## Constraint check

- C1-C7, C9: OK
- seed-integrity (no SMT-fixed flow's placement changed): OK

## GCL per egress port

### sw01-p2  (11 entries, util 1.5600 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 45440 0x7F # 01111111   Q6
sgs 392000 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p4  (27 entries, util 17.1600 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 70080 0x80 # 10000000   Q7
sgs 38400 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 120000 0x40 # 01000000   Q6
sgs 38400 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 95040 0x80 # 10000000   Q7
sgs 38400 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 103360 0x40 # 01000000   Q6
sgs 5120 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (27 entries, util 10.9200 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 21120 0xBF # 10111111   Q7
sgs 3840 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 33600 0x7F # 01111111   Q6
sgs 32960 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 4480 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 120960 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 37440 0x80 # 10000000   Q7
sgs 46080 0x7F # 01111111   Q6
sgs 32960 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 4480 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 54400 0x80 # 10000000   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p4  (24 entries, util 12.4800 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 72320 0x80 # 10000000   Q7
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 122240 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 72320 0x80 # 10000000   Q7
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 105600 0x40 # 01000000   Q6
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (11 entries, util 1.5600 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 28800 0x7F # 01111111   Q6
sgs 408640 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p5  (27 entries, util 17.1600 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 70080 0x80 # 10000000   Q7
sgs 21760 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 120000 0x40 # 01000000   Q6
sgs 21760 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 95040 0x80 # 10000000   Q7
sgs 21760 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 86720 0x40 # 01000000   Q6
sgs 5120 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p4  (24 entries, util 10.9200 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 16320 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 21120 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 120960 0x80 # 10000000   Q7
sgs 29120 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 37440 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16320 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 21120 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 71040 0x80 # 10000000   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (21 entries, util 12.4800 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 72320 0x80 # 10000000   Q7
sgs 44480 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 122240 0x40 # 01000000   Q6
sgs 44480 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 72320 0x80 # 10000000   Q7
sgs 44480 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 88960 0x40 # 01000000   Q6
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (27 entries, util 17.1600 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 70080 0x80 # 10000000   Q7
sgs 5120 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 120000 0x40 # 01000000   Q6
sgs 5120 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 95040 0x80 # 10000000   Q7
sgs 5120 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 70080 0x40 # 01000000   Q6
sgs 5120 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p5  (11 entries, util 1.5600 %)

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

### sw06-p4  (23 entries, util 12.4800 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 4800 0x3F # 00111111   BE
sgs 67200 0x80 # 10000000   Q7
sgs 27840 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 122240 0x40 # 01000000   Q6
sgs 27840 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 4800 0x3F # 00111111   BE
sgs 67200 0x80 # 10000000   Q7
sgs 27840 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 72320 0x40 # 01000000   Q6
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (23 entries, util 10.9200 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 20800 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 16960 0xBF # 10111111   Q7
sgs 49600 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 37760 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 120960 0x80 # 10000000   Q7
sgs 45760 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 37440 0x80 # 10000000   Q7
sgs 29440 0xBF # 10111111   Q7
sgs 49600 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 37760 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 87680 0x80 # 10000000   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (10 entries, util 1.5600 %)

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

### sw07-p5  (28 entries, util 17.1600 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 70080 0x80 # 10000000   Q7
sgs 38400 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 120000 0x40 # 01000000   Q6
sgs 38400 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 95040 0x80 # 10000000   Q7
sgs 38400 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 53440 0x40 # 01000000   Q6
sgs 5120 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p2  (27 entries, util 26.5200 %)

```
sgs 66560 0x3F # 00111111   BE
sgs 29120 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 24000 0x3F # 00111111   BE
sgs 75840 0x80 # 10000000   Q7
sgs 32640 0x3F # 00111111   BE
sgs 29120 0x40 # 01000000   Q6
sgs 13120 0x3F # 00111111   BE
sgs 13440 0x40 # 01000000   Q6
sgs 144320 0x3F # 00111111   BE
sgs 29120 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 34560 0x80 # 10000000   Q7
sgs 110400 0x3F # 00111111   BE
sgs 29120 0x40 # 01000000   Q6
sgs 13120 0x3F # 00111111   BE
sgs 13440 0x40 # 01000000   Q6
sgs 77760 0x3F # 00111111   BE
```

### sw08-p4  (26 entries, util 10.9200 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 33600 0xBF # 10111111   Q7
sgs 32960 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 4480 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 120960 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 37440 0x80 # 10000000   Q7
sgs 46080 0xBF # 10111111   Q7
sgs 32960 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 4480 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 104320 0x80 # 10000000   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (10 entries, util 1.5600 %)

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

