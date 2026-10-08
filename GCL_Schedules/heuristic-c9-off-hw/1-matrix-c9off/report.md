# Heuristic-enlarged GCL schedule (Problem 2: window enlargement)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4000 ns
- Time-sensitive PCPs considered: [6, 7]
- Seeded from SMT run: **result/result-dataset-testbed-hw/smt-c9-off/1-t3600-c9off-minlat**

## Admission (unchanged by this package -- it only widens windows)

SMT-fixed flows: **10**/20. This package never admits a flow itself; it banks slack for a later admission pass (`prob_3_admit`, Problem 3) to use.

## Opportunistic idle top-up (Step 7 -- see enlarge.py)

Total: **14113600 ns**, drawn from idle capacity on ports at or below utilisation 0.2, independent of any route's deadline-slack budget.

| port | queue | applied (ns) |
|---|---|---|
| S1-p0 | Q6 | 747520 |
| S2-p0 | Q6 | 283840 |
| S2-p0 | Q7 | 249600 |
| S3-p0 | Q6 | 302400 |
| S3-p0 | Q7 | 325120 |
| sw01-p3 | Q6 | 309440 |
| sw01-p3 | Q7 | 268800 |
| sw01-p4 | Q6 | 759360 |
| sw01-p5 | Q6 | 325760 |
| sw01-p5 | Q7 | 384960 |
| sw02-p2 | Q6 | 283520 |
| sw02-p2 | Q7 | 342400 |
| sw02-p3 | Q6 | 666240 |
| sw02-p5 | Q6 | 769920 |
| sw03-p3 | Q6 | 338240 |
| sw03-p3 | Q7 | 330560 |
| sw03-p4 | Q6 | 752000 |
| sw05-p2 | Q6 | 764800 |
| sw05-p5 | Q6 | 752640 |
| sw06-p2 | Q6 | 744640 |
| sw06-p3 | Q6 | 350080 |
| sw06-p3 | Q7 | 339840 |
| sw07-p3 | Q6 | 761280 |
| sw07-p4 | Q6 | 759680 |
| sw08-p2 | Q6 | 721600 |
| sw08-p4 | Q6 | 362240 |
| sw08-p4 | Q7 | 347200 |
| sw08-p5 | Q6 | 769920 |

## Best-effort gap equalization (Step 9 -- see enlarge.py)

**8925440 ns** given back from Steps 7/8's growth so each port's leftover non-TAS gaps land close to equal, instead of one gap staying huge while a neighbour is squeezed to the bare 1-tick C10 minimum.

| port | given back (ns) |
|---|---|
| sw02-p5 | 631040 |
| sw05-p2 | 631040 |
| sw07-p4 | 631040 |
| sw01-p4 | 625920 |
| sw03-p4 | 625920 |
| sw06-p2 | 625920 |
| sw05-p5 | 529920 |
| sw07-p3 | 529920 |
| sw08-p5 | 529920 |
| S1-p0 | 526400 |
| sw02-p3 | 398720 |
| sw08-p2 | 381440 |
| sw08-p4 | 318080 |
| sw06-p3 | 317120 |
| sw03-p3 | 316160 |
| sw01-p5 | 314880 |
| sw01-p3 | 279360 |
| sw02-p2 | 259840 |
| S2-p0 | 230720 |
| S3-p0 | 222080 |

## Opportunistic overlay window creation (Step 10 -- see enlarge.py)

**59** new overlay window(s), **17192960 ns** total, carved out of already-open best-effort spans on ports at or below utilisation 0.2 -- best-effort stays reachable inside each one (gate mask keeps its BE bits set), so none of this is closed off from BE.

| port | queue | size (ns) |
|---|---|---|
| S1-p0 | Q6 | 199680 |
| S1-p0 | Q7 | 325120 |
| S2-p0 | Q6 | 106880 |
| S2-p0 | Q7 | 120000 |
| S3-p0 | Q7 | 198400 |
| sw01-p3 | Q6 | 166720 |
| sw01-p3 | Q7 | 130880 |
| sw01-p4 | Q6 | 266240 |
| sw01-p4 | Q7 | 374720 |
| sw01-p5 | Q6 | 117120 |
| sw01-p5 | Q7 | 199680 |
| sw02-p2 | Q6 | 99200 |
| sw02-p2 | Q7 | 174720 |
| sw02-p3 | Q6 | 210240 |
| sw02-p3 | Q7 | 200320 |
| sw02-p4 | Q6 | 399360 |
| sw02-p4 | Q7 | 400640 |
| sw02-p5 | Q6 | 234240 |
| sw02-p5 | Q7 | 400640 |
| sw03-p3 | Q6 | 170560 |
| sw03-p3 | Q7 | 176000 |
| sw03-p4 | Q6 | 299520 |
| sw03-p4 | Q7 | 349760 |
| sw03-p5 | Q6 | 399360 |
| sw03-p5 | Q7 | 400640 |
| sw04-p3 | Q6 | 399360 |
| sw04-p3 | Q7 | 400640 |
| sw04-p4 | Q6 | 399360 |
| sw04-p4 | Q7 | 400640 |
| sw04-p5 | Q6 | 399360 |
| sw04-p5 | Q7 | 400640 |
| sw05-p2 | Q6 | 261120 |
| sw05-p2 | Q7 | 383360 |
| sw05-p3 | Q6 | 399360 |
| sw05-p3 | Q7 | 400640 |
| sw05-p4 | Q6 | 399360 |
| sw05-p4 | Q7 | 400640 |
| sw05-p5 | Q6 | 262080 |
| sw05-p5 | Q7 | 291520 |
| sw06-p2 | Q6 | 332800 |
| sw06-p2 | Q7 | 324800 |
| sw06-p3 | Q6 | 155200 |
| sw06-p3 | Q7 | 183680 |
| sw06-p4 | Q6 | 399360 |
| sw06-p4 | Q7 | 400640 |
| sw06-p5 | Q6 | 399360 |
| sw06-p5 | Q7 | 400640 |
| sw07-p3 | Q6 | 248640 |
| sw07-p3 | Q7 | 298240 |
| sw07-p4 | Q6 | 288000 |
| sw07-p4 | Q7 | 363200 |
| sw07-p5 | Q6 | 399360 |
| sw07-p5 | Q7 | 400640 |
| sw08-p2 | Q6 | 208640 |
| sw08-p2 | Q7 | 199680 |
| sw08-p4 | Q6 | 139840 |
| sw08-p4 | Q7 | 191360 |
| sw08-p5 | Q6 | 240000 |
| sw08-p5 | Q7 | 300160 |

## Candidate routes (P^cand = routes of the fixed flows above)

| route | PCPs carried | flows |
|---|---|---|
| S1->sw02->sw01->S3 | Q6 (1) | 1 |
| S1->sw02->sw05->sw07->sw08->S2 | Q6 (1) | 1 |
| S2->sw08->sw06->sw03->sw01->S3 | Q6 (1), Q7 (2) | 3 |
| S2->sw08->sw07->sw05->sw02->S1 | Q6 (1) | 1 |
| S3->sw01->sw02->S1 | Q6 (1), Q7 (2) | 3 |
| S3->sw01->sw03->sw06->sw08->S2 | Q6 (1) | 1 |

## Per-link enlargement accounting

| link | sharing eta | route-safe slack (ns) | link budget (ns) | final slack (ns) | applied (ns) |
|---|---|---|---|---|---|
| S1-p0 | 2 | Q6:39881, Q7:0 | 39881 | Q6:39881 | Q6:460480, Q7:325120 |
| S2-p0 | 2 | Q6:111712, Q7:200347 | 312059 | Q6:111712, Q7:134261 | Q6:384960, Q7:390400 |
| S3-p0 | 2 | Q6:62442, Q7:67967 | 130409 | Q6:62442, Q7:58421 | Q6:255360, Q7:469120 |
| sw01-p3 | 2 | Q6:66471, Q7:147851 | 214322 | Q6:66471, Q7:122256 | Q6:393920, Q7:391040 |
| sw02-p2 | 2 | Q6:90126, Q7:41830 | 131956 | Q6:75826, Q7:41830 | Q6:339200, Q7:417920 |
| sw08-p2 | 2 | Q6:24834, Q7:0 | 24834 | Q6:24834 | Q6:573440, Q7:199680 |
| sw01-p4 | 1 | Q6:9231, Q7:0 | 9231 | Q6:9231 | Q6:408640, Q7:374720 |
| sw01-p5 | 1 | Q6:46157, Q7:16980 | 63137 | Q6:28849, Q7:16980 | Q6:332800, Q7:425600 |
| sw02-p3 | 1 | Q6:119492, Q7:0 | 119492 | Q6:119492 | Q6:597120, Q7:200320 |
| sw02-p5 | 1 | Q6:13408, Q7:0 | 13408 | Q6:13408 | Q6:386240, Q7:400640 |
| sw03-p3 | 1 | Q6:27069, Q7:67243 | 94312 | Q6:27069, Q7:60709 | Q6:377920, Q7:408640 |
| sw03-p4 | 1 | Q6:8099, Q7:0 | 8099 | Q6:8099 | Q6:433600, Q7:349760 |
| sw05-p2 | 1 | Q6:11710, Q7:0 | 11710 | Q6:11710 | Q6:406400, Q7:383360 |
| sw05-p5 | 1 | Q6:18778, Q7:0 | 18778 | Q6:18778 | Q6:503360, Q7:291520 |
| sw06-p2 | 1 | Q6:7106, Q7:0 | 7106 | Q6:7106 | Q6:458560, Q7:324800 |
| sw06-p3 | 1 | Q6:23163, Q7:56497 | 79659 | Q6:23163, Q7:50942 | Q6:370240, Q7:415360 |
| sw07-p3 | 1 | Q6:16688, Q7:0 | 16688 | Q6:16688 | Q6:496640, Q7:298240 |
| sw07-p4 | 1 | Q6:10226, Q7:0 | 10226 | Q6:10226 | Q6:426560, Q7:363200 |
| sw08-p4 | 1 | Q6:19820, Q7:47468 | 67288 | Q6:19820, Q7:42746 | Q6:362560, Q7:422080 |
| sw08-p5 | 1 | Q6:14831, Q7:0 | 14831 | Q6:14831 | Q6:494720, Q7:300160 |

Total applied: **23614400 ns** across 30 port(s). Network total slack now banked: **23627520 ns**. GCL_size overflow: 0.

## Per-port GCL entries: before (SMT) vs. after (heuristic-enlarged)

| port | SMT entries | enlarged entries | GCL_size |
|---|---|---|---|
| sw01-p3 | 11 | 13 | 255 |
| sw01-p4 | 9 | 21 | 255 |
| sw01-p5 | 21 | 28 | 255 |
| sw02-p2 | 25 | 23 | 255 |
| sw02-p3 | 3 | 10 | 255 |
| sw02-p4 | 1 | 16 | 255 |
| sw02-p5 | 9 | 24 | 255 |
| sw03-p3 | 9 | 13 | 255 |
| sw03-p4 | 9 | 21 | 255 |
| sw03-p5 | 1 | 16 | 255 |
| sw04-p3 | 1 | 16 | 255 |
| sw04-p4 | 1 | 16 | 255 |
| sw04-p5 | 1 | 16 | 255 |
| sw05-p2 | 9 | 21 | 255 |
| sw05-p3 | 1 | 16 | 255 |
| sw05-p4 | 1 | 16 | 255 |
| sw05-p5 | 5 | 15 | 255 |
| sw06-p2 | 9 | 21 | 255 |
| sw06-p3 | 9 | 13 | 255 |
| sw06-p4 | 1 | 16 | 255 |
| sw06-p5 | 1 | 16 | 255 |
| sw07-p3 | 5 | 15 | 255 |
| sw07-p4 | 9 | 21 | 255 |
| sw07-p5 | 1 | 16 | 255 |
| sw08-p2 | 17 | 24 | 255 |
| sw08-p4 | 9 | 13 | 255 |
| sw08-p5 | 5 | 16 | 255 |

## Flows

| flow | route | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|
| s0(id=1 S3->S1) | S3->sw01->sw02->S1 | 7 | 0 | 20800 | yes |
| s1(id=2 S2->S1) | S2->sw08->sw07->sw05->sw02->S1 | - | - | - | no |
| s2(id=3 S3->S2) | S3->sw01->sw03->sw06->sw08->S2 | - | - | - | no |
| s3(id=4 S1->S3) | S1->sw02->sw01->S3 | 6 | 5120 | 16000 | yes |
| s4(id=5 S2->S1) | S2->sw08->sw07->sw05->sw02->S1 | 6 | 3520 | 29440 | yes |
| s5(id=6 S2->S1) | S2->sw08->sw07->sw05->sw02->S1 | - | - | - | no |
| s6(id=7 S2->S1) | S2->sw08->sw07->sw05->sw02->S1 | - | - | - | no |
| s7(id=8 S2->S3) | S2->sw08->sw06->sw03->sw01->S3 | 7 | 14720 | 31040 | yes |
| s8(id=9 S3->S2) | S3->sw01->sw03->sw06->sw08->S2 | 6 | 6720 | 37440 | yes |
| s9(id=10 S1->S3) | S1->sw02->sw01->S3 | - | - | - | no |
| s10(id=11 S3->S2) | S3->sw01->sw03->sw06->sw08->S2 | - | - | - | no |
| s11(id=12 S2->S1) | S2->sw08->sw07->sw05->sw02->S1 | - | - | - | no |
| s12(id=13 S1->S2) | S1->sw02->sw05->sw07->sw08->S2 | - | - | - | no |
| s13(id=14 S1->S2) | S1->sw02->sw05->sw07->sw08->S2 | 6 | 0 | 29440 | yes |
| s14(id=15 S2->S3) | S2->sw08->sw06->sw03->sw01->S3 | 6 | 8640 | 34240 | yes |
| s15(id=16 S3->S2) | S3->sw01->sw03->sw06->sw08->S2 | - | - | - | no |
| s16(id=17 S2->S3) | S2->sw08->sw06->sw03->sw01->S3 | 7 | 19840 | 29440 | yes |
| s17(id=18 S3->S2) | S3->sw01->sw03->sw06->sw08->S2 | - | - | - | no |
| s18(id=19 S3->S1) | S3->sw01->sw02->S1 | 6 | 18560 | 20800 | yes |
| s19(id=20 S3->S1) | S3->sw01->sw02->S1 | 7 | 13440 | 16000 | yes |

## Per-hop windows (slack_ns > 0 means this window was enlarged)

| flow | egress port | queue | psi (ns) | delta (ns) |
|---|---|---|---|---|
| s0(id=1 S3->S1) | S3-p0 | Q7 | 0 | 4160 |
| s0(id=1 S3->S1) | sw01-p5 | Q7 | 8320 | 4160 |
| s0(id=1 S3->S1) | sw02-p2 | Q7 | 16640 | 4160 |
| s3(id=4 S1->S3) | S1-p0 | Q6 | 5120 | 2560 |
| s3(id=4 S1->S3) | sw02-p3 | Q6 | 11840 | 2560 |
| s3(id=4 S1->S3) | sw01-p3 | Q6 | 18560 | 2560 |
| s4(id=5 S2->S1) | S2-p0 | Q6 | 3520 | 2560 |
| s4(id=5 S2->S1) | sw08-p5 | Q6 | 10240 | 2560 |
| s4(id=5 S2->S1) | sw07-p3 | Q6 | 16960 | 2560 |
| s4(id=5 S2->S1) | sw05-p5 | Q6 | 23680 | 2560 |
| s4(id=5 S2->S1) | sw02-p2 | Q6 | 30400 | 2560 |
| s7(id=8 S2->S3) | S2-p0 | Q7 | 14720 | 2560 |
| s7(id=8 S2->S3) | sw08-p4 | Q7 | 21440 | 2560 |
| s7(id=8 S2->S3) | sw06-p3 | Q7 | 28160 | 2560 |
| s7(id=8 S2->S3) | sw03-p3 | Q7 | 35520 | 2560 |
| s7(id=8 S2->S3) | sw01-p3 | Q7 | 43200 | 2560 |
| s8(id=9 S3->S2) | S3-p0 | Q6 | 6720 | 4160 |
| s8(id=9 S3->S2) | sw01-p4 | Q6 | 15040 | 4160 |
| s8(id=9 S3->S2) | sw03-p4 | Q6 | 23360 | 4160 |
| s8(id=9 S3->S2) | sw06-p2 | Q6 | 31680 | 4160 |
| s8(id=9 S3->S2) | sw08-p2 | Q6 | 40000 | 4160 |
| s13(id=14 S1->S2) | S1-p0 | Q6 | 0 | 2560 |
| s13(id=14 S1->S2) | sw02-p5 | Q6 | 6720 | 2560 |
| s13(id=14 S1->S2) | sw05-p2 | Q6 | 13440 | 2560 |
| s13(id=14 S1->S2) | sw07-p4 | Q6 | 20160 | 2560 |
| s13(id=14 S1->S2) | sw08-p2 | Q6 | 26880 | 2560 |
| s14(id=15 S2->S3) | S2-p0 | Q6 | 8640 | 3520 |
| s14(id=15 S2->S3) | sw08-p4 | Q6 | 16320 | 3520 |
| s14(id=15 S2->S3) | sw06-p3 | Q6 | 24000 | 3520 |
| s14(id=15 S2->S3) | sw03-p3 | Q6 | 31680 | 3520 |
| s14(id=15 S2->S3) | sw01-p3 | Q6 | 39360 | 3520 |
| s16(id=17 S2->S3) | S2-p0 | Q7 | 19840 | 2560 |
| s16(id=17 S2->S3) | sw08-p4 | Q7 | 26560 | 2560 |
| s16(id=17 S2->S3) | sw06-p3 | Q7 | 33280 | 2560 |
| s16(id=17 S2->S3) | sw03-p3 | Q7 | 40000 | 2560 |
| s16(id=17 S2->S3) | sw01-p3 | Q7 | 46720 | 2560 |
| s18(id=19 S3->S1) | S3-p0 | Q6 | 18560 | 4160 |
| s18(id=19 S3->S1) | sw01-p5 | Q6 | 26880 | 4160 |
| s18(id=19 S3->S1) | sw02-p2 | Q6 | 35200 | 4160 |
| s19(id=20 S3->S1) | S3-p0 | Q7 | 13440 | 2560 |
| s19(id=20 S3->S1) | sw01-p5 | Q7 | 20160 | 2560 |
| s19(id=20 S3->S1) | sw02-p2 | Q7 | 26880 | 2560 |

## Constraint check

- C1-C7, C9: OK
- seed-integrity (no SMT-fixed flow's placement changed): OK

## GCL per egress port

### sw01-p3  (13 entries, util 1.8400 %)

```
sgs 18560 0x7F # 01111111   Q6
sgs 3520 0x40 # 01000000   Q6
sgs 17280 0x7F # 01111111   Q6
sgs 3520 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 265280 0x80 # 10000000   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 39360 0x7F # 01111111   Q6
sgs 229760 0x40 # 01000000   Q6
sgs 31040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p4  (21 entries, util 2.0800 %)

```
sgs 15040 0x7F # 01111111   Q6
sgs 43520 0x40 # 01000000   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 15040 0x7F # 01111111   Q6
sgs 43520 0x40 # 01000000   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 15040 0x7F # 01111111   Q6
sgs 43520 0x40 # 01000000   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 15040 0x7F # 01111111   Q6
sgs 28480 0x40 # 01000000   Q6
sgs 6400 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p5  (28 entries, util 4.4000 %)

```
sgs 8320 0x7F # 01111111   Q6
sgs 4160 0x80 # 10000000   Q7
sgs 7680 0x7F # 01111111   Q6
sgs 3520 0x80 # 10000000   Q7
sgs 3200 0x3F # 00111111   BE
sgs 112000 0x40 # 01000000   Q6
sgs 11200 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 8320 0x7F # 01111111   Q6
sgs 4160 0x80 # 10000000   Q7
sgs 7680 0x7F # 01111111   Q6
sgs 118720 0x80 # 10000000   Q7
sgs 11200 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 8320 0x7F # 01111111   Q6
sgs 4160 0x80 # 10000000   Q7
sgs 7680 0x7F # 01111111   Q6
sgs 3520 0x80 # 10000000   Q7
sgs 3200 0x3F # 00111111   BE
sgs 112000 0x40 # 01000000   Q6
sgs 11200 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 8320 0x7F # 01111111   Q6
sgs 4160 0x80 # 10000000   Q7
sgs 7680 0x7F # 01111111   Q6
sgs 110400 0x80 # 10000000   Q7
sgs 19520 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (23 entries, util 5.0400 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 4160 0x80 # 10000000   Q7
sgs 6080 0x7F # 01111111   Q6
sgs 3520 0x80 # 10000000   Q7
sgs 128000 0x40 # 01000000   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 4160 0x80 # 10000000   Q7
sgs 6080 0x7F # 01111111   Q6
sgs 131520 0x80 # 10000000   Q7
sgs 41600 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 4160 0x80 # 10000000   Q7
sgs 6080 0x7F # 01111111   Q6
sgs 3520 0x80 # 10000000   Q7
sgs 128000 0x40 # 01000000   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 4160 0x80 # 10000000   Q7
sgs 6080 0x7F # 01111111   Q6
sgs 114880 0x80 # 10000000   Q7
sgs 8320 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p3  (10 entries, util 0.3200 %)

```
sgs 11840 0x7F # 01111111   Q6
sgs 389440 0x40 # 01000000   Q6
sgs 48640 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p4  (16 entries, util 0.0000 %)

```
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
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p5  (24 entries, util 1.2800 %)

```
sgs 6720 0x7F # 01111111   Q6
sgs 42240 0x40 # 01000000   Q6
sgs 960 0x3F # 00111111   BE
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 6720 0x7F # 01111111   Q6
sgs 42240 0x40 # 01000000   Q6
sgs 960 0x3F # 00111111   BE
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 6720 0x7F # 01111111   Q6
sgs 42240 0x40 # 01000000   Q6
sgs 960 0x3F # 00111111   BE
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 6720 0x7F # 01111111   Q6
sgs 35520 0x40 # 01000000   Q6
sgs 7680 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p3  (13 entries, util 1.5200 %)

```
sgs 31680 0x7F # 01111111   Q6
sgs 3520 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 238720 0x80 # 10000000   Q7
sgs 25920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 31680 0x7F # 01111111   Q6
sgs 210880 0x40 # 01000000   Q6
sgs 7360 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (21 entries, util 2.0800 %)

```
sgs 23360 0x7F # 01111111   Q6
sgs 43520 0x40 # 01000000   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 23360 0x7F # 01111111   Q6
sgs 43520 0x40 # 01000000   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 23360 0x7F # 01111111   Q6
sgs 43520 0x40 # 01000000   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 23360 0x7F # 01111111   Q6
sgs 20160 0x40 # 01000000   Q6
sgs 6400 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p5  (16 entries, util 0.0000 %)

```
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
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p3  (16 entries, util 0.0000 %)

```
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
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p4  (16 entries, util 0.0000 %)

```
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
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (16 entries, util 0.0000 %)

```
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
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p2  (21 entries, util 1.2800 %)

```
sgs 13440 0x7F # 01111111   Q6
sgs 42240 0x40 # 01000000   Q6
sgs 44480 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 13440 0x7F # 01111111   Q6
sgs 42240 0x40 # 01000000   Q6
sgs 44480 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 13440 0x7F # 01111111   Q6
sgs 42240 0x40 # 01000000   Q6
sgs 44480 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 13440 0x7F # 01111111   Q6
sgs 28800 0x40 # 01000000   Q6
sgs 7680 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p3  (16 entries, util 0.0000 %)

```
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
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (16 entries, util 0.0000 %)

```
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
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p5  (15 entries, util 0.6400 %)

```
sgs 23680 0x7F # 01111111   Q6
sgs 135040 0x40 # 01000000   Q6
sgs 41280 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 23680 0x7F # 01111111   Q6
sgs 111360 0x40 # 01000000   Q6
sgs 15040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p2  (21 entries, util 2.0800 %)

```
sgs 31680 0x7F # 01111111   Q6
sgs 43520 0x40 # 01000000   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 31680 0x7F # 01111111   Q6
sgs 43520 0x40 # 01000000   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 31680 0x7F # 01111111   Q6
sgs 43520 0x40 # 01000000   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 31680 0x7F # 01111111   Q6
sgs 11840 0x40 # 01000000   Q6
sgs 6400 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p3  (13 entries, util 1.5200 %)

```
sgs 24000 0x7F # 01111111   Q6
sgs 3520 0x40 # 01000000   Q6
sgs 640 0x3F # 00111111   BE
sgs 238400 0x80 # 10000000   Q7
sgs 33600 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 24000 0x7F # 01111111   Q6
sgs 218560 0x40 # 01000000   Q6
sgs 7360 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p4  (16 entries, util 0.0000 %)

```
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
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (16 entries, util 0.0000 %)

```
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
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p3  (15 entries, util 0.6400 %)

```
sgs 16960 0x7F # 01111111   Q6
sgs 135040 0x40 # 01000000   Q6
sgs 48000 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16960 0x7F # 01111111   Q6
sgs 118080 0x40 # 01000000   Q6
sgs 15040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (21 entries, util 1.2800 %)

```
sgs 20160 0x7F # 01111111   Q6
sgs 42240 0x40 # 01000000   Q6
sgs 37760 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 42240 0x40 # 01000000   Q6
sgs 37760 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 42240 0x40 # 01000000   Q6
sgs 37760 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 22080 0x40 # 01000000   Q6
sgs 7680 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p5  (16 entries, util 0.0000 %)

```
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
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p2  (24 entries, util 3.3600 %)

```
sgs 26880 0x7F # 01111111   Q6
sgs 3520 0x40 # 01000000   Q6
sgs 9600 0x7F # 01111111   Q6
sgs 101120 0x40 # 01000000   Q6
sgs 8960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 26880 0x7F # 01111111   Q6
sgs 3520 0x40 # 01000000   Q6
sgs 9600 0x7F # 01111111   Q6
sgs 101120 0x40 # 01000000   Q6
sgs 8960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 26880 0x7F # 01111111   Q6
sgs 3520 0x40 # 01000000   Q6
sgs 9600 0x7F # 01111111   Q6
sgs 101120 0x40 # 01000000   Q6
sgs 8960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 26880 0x7F # 01111111   Q6
sgs 3520 0x40 # 01000000   Q6
sgs 9600 0x7F # 01111111   Q6
sgs 74240 0x40 # 01000000   Q6
sgs 35840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p4  (13 entries, util 1.5200 %)

```
sgs 16320 0x7F # 01111111   Q6
sgs 3520 0x40 # 01000000   Q6
sgs 1600 0x3F # 00111111   BE
sgs 237440 0x80 # 10000000   Q7
sgs 41280 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16320 0x7F # 01111111   Q6
sgs 226240 0x40 # 01000000   Q6
sgs 7360 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (16 entries, util 0.6400 %)

```
sgs 10240 0x7F # 01111111   Q6
sgs 135040 0x40 # 01000000   Q6
sgs 4800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 10240 0x7F # 01111111   Q6
sgs 124800 0x40 # 01000000   Q6
sgs 15040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

