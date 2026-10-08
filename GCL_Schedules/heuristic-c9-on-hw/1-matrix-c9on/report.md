# Heuristic-enlarged GCL schedule (Problem 2: window enlargement)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4000 ns
- Time-sensitive PCPs considered: [6, 7]
- Seeded from SMT run: **result/result-dataset-testbed-hw/smt-c9-on/1-fair-retimed-c9on**

## Admission (unchanged by this package -- it only widens windows)

SMT-fixed flows: **10**/10. This package never admits a flow itself; it banks slack for a later admission pass (`prob_3_admit`, Problem 3) to use.

## Opportunistic idle top-up (Step 7 -- see enlarge.py)

Total: **14211840 ns**, drawn from idle capacity on ports at or below utilisation 0.2, independent of any route's deadline-slack budget.

| port | queue | applied (ns) |
|---|---|---|
| S1-p0 | Q6 | 544320 |
| S1-p0 | Q7 | 114560 |
| S2-p0 | Q6 | 305600 |
| S2-p0 | Q7 | 314240 |
| S3-p0 | Q6 | 311680 |
| S3-p0 | Q7 | 306560 |
| sw01-p3 | Q6 | 264640 |
| sw01-p3 | Q7 | 298240 |
| sw01-p4 | Q7 | 762560 |
| sw01-p5 | Q6 | 379840 |
| sw01-p5 | Q7 | 354240 |
| sw02-p2 | Q6 | 344000 |
| sw02-p2 | Q7 | 346240 |
| sw02-p3 | Q7 | 692800 |
| sw02-p5 | Q6 | 772160 |
| sw03-p3 | Q6 | 317440 |
| sw03-p3 | Q7 | 346880 |
| sw03-p4 | Q7 | 759680 |
| sw05-p2 | Q6 | 769920 |
| sw05-p5 | Q6 | 752320 |
| sw06-p2 | Q7 | 756480 |
| sw06-p3 | Q6 | 328000 |
| sw06-p3 | Q7 | 355840 |
| sw07-p3 | Q6 | 759360 |
| sw07-p4 | Q6 | 767680 |
| sw08-p2 | Q7 | 719680 |
| sw08-p4 | Q6 | 336640 |
| sw08-p4 | Q7 | 364160 |
| sw08-p5 | Q6 | 766080 |

## Best-effort gap equalization (Step 9 -- see enlarge.py)

**8916480 ns** given back from Steps 7/8's growth so each port's leftover non-TAS gaps land close to equal, instead of one gap staying huge while a neighbour is squeezed to the bare 1-tick C10 minimum.

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
| sw08-p2 | 355840 |
| sw01-p5 | 320640 |
| sw03-p3 | 319040 |
| sw06-p3 | 319040 |
| sw08-p4 | 319040 |
| sw01-p3 | 274240 |
| sw02-p2 | 270080 |
| S2-p0 | 230720 |
| S3-p0 | 222080 |

## Opportunistic overlay window creation (Step 10 -- see enlarge.py)

**59** new overlay window(s), **17060480 ns** total, carved out of already-open best-effort spans on ports at or below utilisation 0.2 -- best-effort stays reachable inside each one (gate mask keeps its BE bits set), so none of this is closed off from BE.

| port | queue | size (ns) |
|---|---|---|
| S1-p0 | Q6 | 199680 |
| S1-p0 | Q7 | 325120 |
| S2-p0 | Q6 | 106880 |
| S2-p0 | Q7 | 120000 |
| S3-p0 | Q7 | 198400 |
| sw01-p3 | Q6 | 146880 |
| sw01-p3 | Q7 | 136640 |
| sw01-p4 | Q6 | 249600 |
| sw01-p4 | Q7 | 387200 |
| sw01-p5 | Q6 | 124480 |
| sw01-p5 | Q7 | 199680 |
| sw02-p2 | Q6 | 76800 |
| sw02-p2 | Q7 | 199680 |
| sw02-p3 | Q6 | 207680 |
| sw02-p3 | Q7 | 200320 |
| sw02-p4 | Q6 | 399360 |
| sw02-p4 | Q7 | 400640 |
| sw02-p5 | Q6 | 234560 |
| sw02-p5 | Q7 | 400640 |
| sw03-p3 | Q6 | 149440 |
| sw03-p3 | Q7 | 186560 |
| sw03-p4 | Q6 | 266240 |
| sw03-p4 | Q7 | 374720 |
| sw03-p5 | Q6 | 399360 |
| sw03-p5 | Q7 | 400640 |
| sw04-p3 | Q6 | 399360 |
| sw04-p3 | Q7 | 400640 |
| sw04-p4 | Q6 | 399360 |
| sw04-p4 | Q7 | 400640 |
| sw04-p5 | Q6 | 399360 |
| sw04-p5 | Q7 | 400640 |
| sw05-p2 | Q6 | 240640 |
| sw05-p2 | Q7 | 398720 |
| sw05-p3 | Q6 | 399360 |
| sw05-p3 | Q7 | 400640 |
| sw05-p4 | Q6 | 399360 |
| sw05-p4 | Q7 | 400640 |
| sw05-p5 | Q6 | 246720 |
| sw05-p5 | Q7 | 299200 |
| sw06-p2 | Q6 | 282880 |
| sw06-p2 | Q7 | 362240 |
| sw06-p3 | Q6 | 141120 |
| sw06-p3 | Q7 | 190720 |
| sw06-p4 | Q6 | 399360 |
| sw06-p4 | Q7 | 400640 |
| sw06-p5 | Q6 | 399360 |
| sw06-p5 | Q7 | 400640 |
| sw07-p3 | Q6 | 238400 |
| sw07-p3 | Q7 | 300160 |
| sw07-p4 | Q6 | 257280 |
| sw07-p4 | Q7 | 386240 |
| sw07-p5 | Q6 | 399360 |
| sw07-p5 | Q7 | 400640 |
| sw08-p2 | Q6 | 160000 |
| sw08-p2 | Q7 | 199680 |
| sw08-p4 | Q6 | 132800 |
| sw08-p4 | Q7 | 194880 |
| sw08-p5 | Q6 | 237440 |
| sw08-p5 | Q7 | 300160 |

## Candidate routes (P^cand = routes of the fixed flows above)

| route | PCPs carried | flows |
|---|---|---|
| S1->sw02->sw01->S3 | Q7 (1) | 1 |
| S1->sw02->sw05->sw07->sw08->S2 | Q6 (1) | 1 |
| S2->sw08->sw06->sw03->sw01->S3 | Q6 (2), Q7 (1) | 3 |
| S2->sw08->sw07->sw05->sw02->S1 | Q6 (1) | 1 |
| S3->sw01->sw02->S1 | Q6 (2), Q7 (1) | 3 |
| S3->sw01->sw03->sw06->sw08->S2 | Q7 (1) | 1 |

## Per-link enlargement accounting

| link | sharing eta | route-safe slack (ns) | link budget (ns) | final slack (ns) | applied (ns) |
|---|---|---|---|---|---|
| S1-p0 | 2 | Q6:50765, Q7:176535 | 227300 | Q6:50765, Q7:77920 | Q6:399360, Q7:386240 |
| S2-p0 | 2 | Q6:83293, Q7:92608 | 175900 | Q6:83293, Q7:76205 | Q6:379200, Q7:396160 |
| S3-p0 | 2 | Q6:67969, Q7:76819 | 144788 | Q6:53241, Q7:76819 | Q6:255360, Q7:469120 |
| sw01-p3 | 2 | Q6:154238, Q7:84866 | 239104 | Q6:124428, Q7:84866 | Q6:403200, Q7:377920 |
| sw02-p2 | 2 | Q6:47706, Q7:32251 | 79957 | Q6:47706, Q7:13695 | Q6:315520, Q7:442240 |
| sw08-p2 | 2 | Q6:36939, Q7:20317 | 57257 | Q6:30234, Q7:20317 | Q6:163840, Q7:596480 |
| sw01-p4 | 1 | Q6:0, Q7:10200 | 10200 | Q7:10200 | Q6:249600, Q7:533760 |
| sw01-p5 | 1 | Q6:17134, Q7:16762 | 33896 | Q6:17134, Q7:9708 | Q6:340160, Q7:424000 |
| sw02-p3 | 1 | Q6:0, Q7:95382 | 95382 | Q7:95382 | Q6:207680, Q7:589760 |
| sw02-p5 | 1 | Q6:13503, Q7:0 | 13503 | Q6:13503 | Q6:389120, Q7:400640 |
| sw03-p3 | 1 | Q6:78924, Q7:31079 | 110002 | Q6:71363, Q7:31079 | Q6:379200, Q7:404480 |
| sw03-p4 | 1 | Q6:0, Q7:8932 | 8932 | Q7:8932 | Q6:266240, Q7:517120 |
| sw05-p2 | 1 | Q6:11545, Q7:0 | 11545 | Q6:11545 | Q6:391040, Q7:398720 |
| sw05-p5 | 1 | Q6:26805, Q7:0 | 26805 | Q6:26805 | Q6:495680, Q7:299200 |
| sw06-p2 | 1 | Q6:0, Q7:7822 | 7822 | Q7:7822 | Q6:282880, Q7:500480 |
| sw06-p3 | 1 | Q6:67458, Q7:26306 | 93764 | Q6:61036, Q7:26306 | Q6:370880, Q7:412800 |
| sw07-p3 | 1 | Q6:23929, Q7:0 | 23929 | Q6:23929 | Q6:491520, Q7:300160 |
| sw07-p4 | 1 | Q6:9870, Q7:0 | 9870 | Q6:9870 | Q6:403520, Q7:386240 |
| sw08-p4 | 1 | Q6:57658, Q7:22266 | 79924 | Q6:52204, Q7:22266 | Q6:362560, Q7:421120 |
| sw08-p5 | 1 | Q6:21361, Q7:0 | 21361 | Q6:21361 | Q6:494720, Q7:300160 |

Total applied: **23598080 ns** across 30 port(s). Network total slack now banked: **23617600 ns**. GCL_size overflow: 0.

## Per-port GCL entries: before (SMT) vs. after (heuristic-enlarged)

| port | SMT entries | enlarged entries | GCL_size |
|---|---|---|---|
| sw01-p3 | 11 | 14 | 255 |
| sw01-p4 | 9 | 21 | 255 |
| sw01-p5 | 21 | 28 | 255 |
| sw02-p2 | 25 | 27 | 255 |
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
| sw07-p3 | 5 | 16 | 255 |
| sw07-p4 | 9 | 21 | 255 |
| sw07-p5 | 1 | 16 | 255 |
| sw08-p2 | 17 | 24 | 255 |
| sw08-p4 | 9 | 13 | 255 |
| sw08-p5 | 5 | 16 | 255 |

## Flows

| flow | route | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|
| s0(id=1 S3->S1) | S3->sw01->sw02->S1 | 6 | 0 | 12480 | yes |
| s1(id=2 S2->S1) | S2->sw08->sw07->sw05->sw02->S1 | - | - | - | no |
| s2(id=3 S3->S2) | S3->sw01->sw03->sw06->sw08->S2 | - | - | - | no |
| s3(id=4 S1->S3) | S1->sw02->sw01->S3 | 7 | 5120 | 10880 | yes |
| s4(id=5 S2->S1) | S2->sw08->sw07->sw05->sw02->S1 | 6 | 3520 | 19200 | yes |
| s5(id=6 S2->S1) | S2->sw08->sw07->sw05->sw02->S1 | - | - | - | no |
| s6(id=7 S2->S1) | S2->sw08->sw07->sw05->sw02->S1 | - | - | - | no |
| s7(id=8 S2->S3) | S2->sw08->sw06->sw03->sw01->S3 | 6 | 14720 | 19200 | yes |
| s8(id=9 S3->S2) | S3->sw01->sw03->sw06->sw08->S2 | 7 | 6720 | 20800 | yes |
| s9(id=10 S1->S3) | S1->sw02->sw01->S3 | - | - | - | no |
| s10(id=11 S3->S2) | S3->sw01->sw03->sw06->sw08->S2 | - | - | - | no |
| s11(id=12 S2->S1) | S2->sw08->sw07->sw05->sw02->S1 | - | - | - | no |
| s12(id=13 S1->S2) | S1->sw02->sw05->sw07->sw08->S2 | - | - | - | no |
| s13(id=14 S1->S2) | S1->sw02->sw05->sw07->sw08->S2 | 6 | 0 | 19200 | yes |
| s14(id=15 S2->S3) | S2->sw08->sw06->sw03->sw01->S3 | 7 | 8640 | 20160 | yes |
| s15(id=16 S3->S2) | S3->sw01->sw03->sw06->sw08->S2 | - | - | - | no |
| s16(id=17 S2->S3) | S2->sw08->sw06->sw03->sw01->S3 | 6 | 19840 | 19200 | yes |
| s17(id=18 S3->S2) | S3->sw01->sw03->sw06->sw08->S2 | - | - | - | no |
| s18(id=19 S3->S1) | S3->sw01->sw02->S1 | 6 | 18560 | 12480 | yes |
| s19(id=20 S3->S1) | S3->sw01->sw02->S1 | 7 | 13440 | 12160 | yes |

## Per-hop windows (slack_ns > 0 means this window was enlarged)

| flow | egress port | queue | psi (ns) | delta (ns) |
|---|---|---|---|---|
| s0(id=1 S3->S1) | S3-p0 | Q6 | 0 | 4160 |
| s0(id=1 S3->S1) | sw01-p5 | Q6 | 4160 | 4160 |
| s0(id=1 S3->S1) | sw02-p2 | Q6 | 8320 | 4160 |
| s3(id=4 S1->S3) | S1-p0 | Q7 | 5120 | 2560 |
| s3(id=4 S1->S3) | sw02-p3 | Q7 | 9280 | 2560 |
| s3(id=4 S1->S3) | sw01-p3 | Q7 | 13440 | 2560 |
| s4(id=5 S2->S1) | S2-p0 | Q6 | 3520 | 2560 |
| s4(id=5 S2->S1) | sw08-p5 | Q6 | 7680 | 2560 |
| s4(id=5 S2->S1) | sw07-p3 | Q6 | 11840 | 2560 |
| s4(id=5 S2->S1) | sw05-p5 | Q6 | 16000 | 2560 |
| s4(id=5 S2->S1) | sw02-p2 | Q6 | 20160 | 2560 |
| s7(id=8 S2->S3) | S2-p0 | Q6 | 14720 | 2560 |
| s7(id=8 S2->S3) | sw08-p4 | Q6 | 18880 | 2560 |
| s7(id=8 S2->S3) | sw06-p3 | Q6 | 23040 | 2560 |
| s7(id=8 S2->S3) | sw03-p3 | Q6 | 27200 | 2560 |
| s7(id=8 S2->S3) | sw01-p3 | Q6 | 31360 | 2560 |
| s8(id=9 S3->S2) | S3-p0 | Q7 | 6720 | 4160 |
| s8(id=9 S3->S2) | sw01-p4 | Q7 | 10880 | 4160 |
| s8(id=9 S3->S2) | sw03-p4 | Q7 | 15040 | 4160 |
| s8(id=9 S3->S2) | sw06-p2 | Q7 | 19200 | 4160 |
| s8(id=9 S3->S2) | sw08-p2 | Q7 | 23360 | 4160 |
| s13(id=14 S1->S2) | S1-p0 | Q6 | 0 | 2560 |
| s13(id=14 S1->S2) | sw02-p5 | Q6 | 4160 | 2560 |
| s13(id=14 S1->S2) | sw05-p2 | Q6 | 8320 | 2560 |
| s13(id=14 S1->S2) | sw07-p4 | Q6 | 12480 | 2560 |
| s13(id=14 S1->S2) | sw08-p2 | Q6 | 16640 | 2560 |
| s14(id=15 S2->S3) | S2-p0 | Q7 | 8640 | 3520 |
| s14(id=15 S2->S3) | sw08-p4 | Q7 | 12800 | 3520 |
| s14(id=15 S2->S3) | sw06-p3 | Q7 | 16960 | 3520 |
| s14(id=15 S2->S3) | sw03-p3 | Q7 | 21120 | 3520 |
| s14(id=15 S2->S3) | sw01-p3 | Q7 | 25280 | 3520 |
| s16(id=17 S2->S3) | S2-p0 | Q6 | 19840 | 2560 |
| s16(id=17 S2->S3) | sw08-p4 | Q6 | 24000 | 2560 |
| s16(id=17 S2->S3) | sw06-p3 | Q6 | 28160 | 2560 |
| s16(id=17 S2->S3) | sw03-p3 | Q6 | 32320 | 2560 |
| s16(id=17 S2->S3) | sw01-p3 | Q6 | 36480 | 2560 |
| s18(id=19 S3->S1) | S3-p0 | Q6 | 18560 | 4160 |
| s18(id=19 S3->S1) | sw01-p5 | Q6 | 22720 | 4160 |
| s18(id=19 S3->S1) | sw02-p2 | Q6 | 26880 | 4160 |
| s19(id=20 S3->S1) | S3-p0 | Q7 | 13440 | 2560 |
| s19(id=20 S3->S1) | sw01-p5 | Q7 | 18880 | 2560 |
| s19(id=20 S3->S1) | sw02-p2 | Q7 | 23040 | 2560 |

## Constraint check

- C1-C7, C9: OK
- seed-integrity (no SMT-fixed flow's placement changed): OK

## GCL per egress port

### sw01-p3  (14 entries, util 1.8400 %)

```
sgs 13440 0x7F # 01111111   Q6
sgs 3520 0x80 # 10000000   Q7
sgs 8320 0x7F # 01111111   Q6
sgs 3520 0x80 # 10000000   Q7
sgs 2560 0x3F # 00111111   BE
sgs 263040 0x40 # 01000000   Q6
sgs 5760 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 25280 0x7F # 01111111   Q6
sgs 243840 0x80 # 10000000   Q7
sgs 31040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p4  (21 entries, util 2.0800 %)

```
sgs 10880 0x7F # 01111111   Q6
sgs 43520 0x80 # 10000000   Q7
sgs 45760 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 10880 0x7F # 01111111   Q6
sgs 43520 0x80 # 10000000   Q7
sgs 45760 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 10880 0x7F # 01111111   Q6
sgs 43520 0x80 # 10000000   Q7
sgs 45760 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 10880 0x7F # 01111111   Q6
sgs 32640 0x80 # 10000000   Q7
sgs 6400 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p5  (28 entries, util 4.4000 %)

```
sgs 4160 0x7F # 01111111   Q6
sgs 4160 0x40 # 01000000   Q6
sgs 10560 0x7F # 01111111   Q6
sgs 3520 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 112000 0x40 # 01000000   Q6
sgs 15360 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 4160 0x7F # 01111111   Q6
sgs 4160 0x40 # 01000000   Q6
sgs 10560 0x7F # 01111111   Q6
sgs 115840 0x80 # 10000000   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 4160 0x7F # 01111111   Q6
sgs 4160 0x40 # 01000000   Q6
sgs 10560 0x7F # 01111111   Q6
sgs 3520 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 112000 0x40 # 01000000   Q6
sgs 15360 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 4160 0x7F # 01111111   Q6
sgs 4160 0x40 # 01000000   Q6
sgs 10560 0x7F # 01111111   Q6
sgs 111680 0x80 # 10000000   Q7
sgs 19520 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (27 entries, util 5.0400 %)

```
sgs 8320 0x7F # 01111111   Q6
sgs 4160 0x40 # 01000000   Q6
sgs 7040 0x7F # 01111111   Q6
sgs 3520 0x40 # 01000000   Q6
sgs 3520 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 123200 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 8320 0x7F # 01111111   Q6
sgs 4160 0x40 # 01000000   Q6
sgs 10560 0x7F # 01111111   Q6
sgs 127040 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
sgs 8320 0x7F # 01111111   Q6
sgs 4160 0x40 # 01000000   Q6
sgs 7040 0x7F # 01111111   Q6
sgs 3520 0x40 # 01000000   Q6
sgs 3520 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 123200 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 8320 0x7F # 01111111   Q6
sgs 4160 0x40 # 01000000   Q6
sgs 10560 0x7F # 01111111   Q6
sgs 118720 0x80 # 10000000   Q7
sgs 8320 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p3  (10 entries, util 0.3200 %)

```
sgs 9280 0x7F # 01111111   Q6
sgs 392000 0x80 # 10000000   Q7
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
sgs 4160 0x7F # 01111111   Q6
sgs 42240 0x40 # 01000000   Q6
sgs 3520 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 4160 0x7F # 01111111   Q6
sgs 42240 0x40 # 01000000   Q6
sgs 3520 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 4160 0x7F # 01111111   Q6
sgs 42240 0x40 # 01000000   Q6
sgs 3520 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 4160 0x7F # 01111111   Q6
sgs 38080 0x40 # 01000000   Q6
sgs 7680 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p3  (13 entries, util 1.5200 %)

```
sgs 21120 0x7F # 01111111   Q6
sgs 3520 0x80 # 10000000   Q7
sgs 2560 0x3F # 00111111   BE
sgs 236480 0x40 # 01000000   Q6
sgs 36480 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 21120 0x7F # 01111111   Q6
sgs 221440 0x80 # 10000000   Q7
sgs 7360 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (21 entries, util 2.0800 %)

```
sgs 15040 0x7F # 01111111   Q6
sgs 43520 0x80 # 10000000   Q7
sgs 41600 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 15040 0x7F # 01111111   Q6
sgs 43520 0x80 # 10000000   Q7
sgs 41600 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 15040 0x7F # 01111111   Q6
sgs 43520 0x80 # 10000000   Q7
sgs 41600 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 15040 0x7F # 01111111   Q6
sgs 28480 0x80 # 10000000   Q7
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
sgs 8320 0x7F # 01111111   Q6
sgs 42240 0x40 # 01000000   Q6
sgs 49600 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 8320 0x7F # 01111111   Q6
sgs 42240 0x40 # 01000000   Q6
sgs 49600 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 8320 0x7F # 01111111   Q6
sgs 42240 0x40 # 01000000   Q6
sgs 49600 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 8320 0x7F # 01111111   Q6
sgs 33920 0x40 # 01000000   Q6
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
sgs 16000 0x7F # 01111111   Q6
sgs 135040 0x40 # 01000000   Q6
sgs 48960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16000 0x7F # 01111111   Q6
sgs 119040 0x40 # 01000000   Q6
sgs 15040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p2  (21 entries, util 2.0800 %)

```
sgs 19200 0x7F # 01111111   Q6
sgs 43520 0x80 # 10000000   Q7
sgs 37440 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 19200 0x7F # 01111111   Q6
sgs 43520 0x80 # 10000000   Q7
sgs 37440 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 19200 0x7F # 01111111   Q6
sgs 43520 0x80 # 10000000   Q7
sgs 37440 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 19200 0x7F # 01111111   Q6
sgs 24320 0x80 # 10000000   Q7
sgs 6400 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p3  (13 entries, util 1.5200 %)

```
sgs 16960 0x7F # 01111111   Q6
sgs 3520 0x80 # 10000000   Q7
sgs 2560 0x3F # 00111111   BE
sgs 236480 0x40 # 01000000   Q6
sgs 40640 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16960 0x7F # 01111111   Q6
sgs 225600 0x80 # 10000000   Q7
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

### sw07-p3  (16 entries, util 0.6400 %)

```
sgs 11840 0x7F # 01111111   Q6
sgs 135040 0x40 # 01000000   Q6
sgs 3200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 11840 0x7F # 01111111   Q6
sgs 123200 0x40 # 01000000   Q6
sgs 15040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (21 entries, util 1.2800 %)

```
sgs 12480 0x7F # 01111111   Q6
sgs 42240 0x40 # 01000000   Q6
sgs 45440 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 42240 0x40 # 01000000   Q6
sgs 45440 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 42240 0x40 # 01000000   Q6
sgs 45440 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 29760 0x40 # 01000000   Q6
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
sgs 16640 0x7F # 01111111   Q6
sgs 3520 0x40 # 01000000   Q6
sgs 3200 0x3F # 00111111   BE
sgs 107520 0x80 # 10000000   Q7
sgs 19200 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 3520 0x40 # 01000000   Q6
sgs 3200 0x3F # 00111111   BE
sgs 107520 0x80 # 10000000   Q7
sgs 19200 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 3520 0x40 # 01000000   Q6
sgs 3200 0x3F # 00111111   BE
sgs 107520 0x80 # 10000000   Q7
sgs 19200 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 3520 0x40 # 01000000   Q6
sgs 3200 0x3F # 00111111   BE
sgs 90880 0x80 # 10000000   Q7
sgs 35840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p4  (13 entries, util 1.5200 %)

```
sgs 12800 0x7F # 01111111   Q6
sgs 3520 0x80 # 10000000   Q7
sgs 2560 0x3F # 00111111   BE
sgs 236480 0x40 # 01000000   Q6
sgs 44800 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 12800 0x7F # 01111111   Q6
sgs 229760 0x80 # 10000000   Q7
sgs 7360 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (16 entries, util 0.6400 %)

```
sgs 7680 0x7F # 01111111   Q6
sgs 135040 0x40 # 01000000   Q6
sgs 7360 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 7680 0x7F # 01111111   Q6
sgs 127360 0x40 # 01000000   Q6
sgs 15040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

