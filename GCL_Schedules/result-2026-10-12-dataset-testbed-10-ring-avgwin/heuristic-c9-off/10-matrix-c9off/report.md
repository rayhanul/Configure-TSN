# Heuristic-enlarged GCL schedule (Problem 2: window enlargement)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Time-sensitive PCPs considered: [6, 7]
- Seeded from SMT run: **result/result-2026-10-12-dataset-testbed-10-ring-avgwin/smt-c9-off/10-t3600-c9off-minlat**

## Admission (unchanged by this package -- it only widens windows)

SMT-fixed flows: **11**/20. This package never admits a flow itself; it banks slack for a later admission pass (`prob_3_admit`, Problem 3) to use.

## Opportunistic idle top-up (Step 7 -- see enlarge.py)

Total: **14102720 ns**, drawn from idle capacity on ports at or below utilisation 0.2, independent of any route's deadline-slack budget.

| port | queue | applied (ns) |
|---|---|---|
| S1-p0 | Q6 | 501120 |
| S1-p0 | Q7 | 61120 |
| S2-p0 | Q6 | 266560 |
| S2-p0 | Q7 | 380480 |
| S3-p0 | Q7 | 647040 |
| sw01-p2 | Q6 | 360640 |
| sw01-p2 | Q7 | 200000 |
| sw01-p4 | Q7 | 728640 |
| sw01-p5 | Q7 | 648640 |
| sw02-p2 | Q6 | 236160 |
| sw02-p2 | Q7 | 241920 |
| sw02-p4 | Q6 | 550400 |
| sw02-p4 | Q7 | 84480 |
| sw02-p5 | Q6 | 695360 |
| sw03-p4 | Q6 | 320960 |
| sw03-p4 | Q7 | 306880 |
| sw03-p5 | Q7 | 712640 |
| sw04-p4 | Q6 | 629120 |
| sw04-p5 | Q6 | 534400 |
| sw04-p5 | Q7 | 90880 |
| sw05-p4 | Q7 | 696320 |
| sw05-p5 | Q6 | 322880 |
| sw05-p5 | Q7 | 324480 |
| sw06-p4 | Q6 | 518720 |
| sw06-p4 | Q7 | 96640 |
| sw06-p5 | Q6 | 652480 |
| sw07-p4 | Q6 | 324480 |
| sw07-p4 | Q7 | 341760 |
| sw07-p5 | Q7 | 680000 |
| sw08-p2 | Q6 | 463360 |
| sw08-p2 | Q7 | 117440 |
| sw08-p4 | Q6 | 675200 |
| sw08-p5 | Q6 | 312320 |
| sw08-p5 | Q7 | 379200 |

## Opportunistic window creation (Step 8 -- see enlarge.py)

**9** brand-new window(s) opened, **112320 ns** total, on ports at or below utilisation 0.2 whose TT queue had zero windows before this run.

| port | queue | size (ns) |
|---|---|---|
| sw01-p4 | Q6 | 12480 |
| sw01-p5 | Q6 | 12480 |
| sw02-p5 | Q7 | 12480 |
| sw03-p5 | Q6 | 12480 |
| sw04-p4 | Q7 | 12480 |
| sw05-p4 | Q6 | 12480 |
| sw06-p5 | Q7 | 12480 |
| sw07-p5 | Q6 | 12480 |
| sw08-p4 | Q7 | 12480 |

## Best-effort gap equalization (Step 9 -- see enlarge.py)

**8718080 ns** given back from Steps 7/8's growth so each port's leftover non-TAS gaps land close to equal, instead of one gap staying huge while a neighbour is squeezed to the bare 1-tick C10 minimum.

| port | given back (ns) |
|---|---|
| sw02-p4 | 528320 |
| sw04-p5 | 528320 |
| sw06-p4 | 517440 |
| sw01-p4 | 499200 |
| sw03-p5 | 499200 |
| sw05-p4 | 499200 |
| sw07-p5 | 495360 |
| sw08-p5 | 438400 |
| sw02-p5 | 437120 |
| sw03-p4 | 424960 |
| sw05-p5 | 424960 |
| sw07-p4 | 424960 |
| S2-p0 | 393280 |
| sw01-p2 | 375680 |
| S3-p0 | 336320 |
| sw08-p2 | 308160 |
| S1-p0 | 307520 |
| sw04-p4 | 262400 |
| sw06-p5 | 262400 |
| sw08-p4 | 262400 |
| sw01-p5 | 248000 |
| sw02-p2 | 244480 |

## Opportunistic overlay window creation (Step 10 -- see enlarge.py)

**44** new overlay window(s), **9338560 ns** total, carved out of already-open best-effort spans on ports at or below utilisation 0.2 -- best-effort stays reachable inside each one (gate mask keeps its BE bits set), so none of this is closed off from BE.

| port | queue | size (ns) |
|---|---|---|
| S1-p0 | Q6 | 74880 |
| S1-p0 | Q7 | 212160 |
| S2-p0 | Q6 | 193600 |
| S2-p0 | Q7 | 199680 |
| S3-p0 | Q6 | 124160 |
| S3-p0 | Q7 | 212160 |
| sw01-p2 | Q6 | 133120 |
| sw01-p2 | Q7 | 258560 |
| sw01-p4 | Q6 | 249600 |
| sw01-p4 | Q7 | 224640 |
| sw01-p5 | Q6 | 134400 |
| sw01-p5 | Q7 | 137280 |
| sw02-p2 | Q6 | 149760 |
| sw02-p2 | Q7 | 120000 |
| sw02-p4 | Q6 | 311040 |
| sw02-p4 | Q7 | 259520 |
| sw02-p5 | Q6 | 204160 |
| sw02-p5 | Q7 | 232960 |
| sw03-p4 | Q6 | 249600 |
| sw03-p4 | Q7 | 233600 |
| sw03-p5 | Q6 | 295360 |
| sw03-p5 | Q7 | 224640 |
| sw04-p4 | Q6 | 149760 |
| sw04-p4 | Q7 | 200000 |
| sw04-p5 | Q6 | 291840 |
| sw04-p5 | Q7 | 251520 |
| sw05-p4 | Q6 | 312000 |
| sw05-p4 | Q7 | 224640 |
| sw05-p5 | Q6 | 249600 |
| sw05-p5 | Q7 | 190080 |
| sw06-p4 | Q6 | 274240 |
| sw06-p4 | Q7 | 294400 |
| sw06-p5 | Q6 | 149760 |
| sw06-p5 | Q7 | 183360 |
| sw07-p4 | Q6 | 250240 |
| sw07-p4 | Q7 | 199680 |
| sw07-p5 | Q6 | 237120 |
| sw07-p5 | Q7 | 287360 |
| sw08-p2 | Q6 | 207040 |
| sw08-p2 | Q7 | 183040 |
| sw08-p4 | Q6 | 149760 |
| sw08-p4 | Q7 | 166720 |
| sw08-p5 | Q6 | 251840 |
| sw08-p5 | Q7 | 199680 |

## Candidate routes (P^cand = routes of the fixed flows above)

| route | PCPs carried | flows |
|---|---|---|
| S1->sw02->sw01->S3 | Q6 (2) | 2 |
| S1->sw02->sw04->sw06->sw08->S2 | Q6 (1), Q7 (1) | 2 |
| S2->sw08->sw06->sw04->sw02->S1 | Q6 (1) | 1 |
| S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 (1), Q7 (1) | 2 |
| S3->sw01->sw02->S1 | Q7 (3) | 3 |
| S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 (1) | 1 |

## Per-link enlargement accounting

| link | sharing eta | route-safe slack (ns) | link budget (ns) | final slack (ns) | applied (ns) |
|---|---|---|---|---|---|
| S1-p0 | 2 | Q6:48980, Q7:140253 | 189233 | Q6:48980, Q7:51786 | Q6:372480, Q7:269760 |
| S2-p0 | 2 | Q6:51607, Q7:19742 | 71349 | Q6:46329, Q7:19742 | Q6:315840, Q7:396800 |
| S3-p0 | 2 | Q6:0, Q7:40852 | 40852 | Q7:40852 | Q6:124160, Q7:563520 |
| sw01-p2 | 2 | Q6:39492, Q7:19864 | 59356 | Q6:39492, Q7:17031 | Q6:257920, Q7:375040 |
| sw02-p2 | 2 | Q6:157930, Q7:100174 | 258104 | Q6:88913, Q7:100174 | Q6:371200, Q7:320960 |
| sw08-p2 | 2 | Q6:12995, Q7:13432 | 26427 | Q6:10576, Q7:13432 | Q6:442560, Q7:243840 |
| sw01-p4 | 1 | Q6:0, Q7:4948 | 4948 | Q7:4948 | Q6:262080, Q7:458880 |
| sw01-p5 | 1 | Q6:0, Q7:47549 | 47549 | Q7:47549 | Q6:146880, Q7:585280 |
| sw02-p4 | 1 | Q6:7011, Q7:68767 | 75778 | Q6:7011, Q7:53826 | Q6:462720, Q7:274880 |
| sw02-p5 | 1 | Q6:13254, Q7:0 | 13254 | Q6:13254 | Q6:475520, Q7:245440 |
| sw03-p4 | 1 | Q6:21730, Q7:6571 | 28300 | Q6:17635, Q7:6571 | Q6:381440, Q7:328640 |
| sw03-p5 | 1 | Q6:0, Q7:4458 | 4458 | Q7:4458 | Q6:307840, Q7:442240 |
| sw04-p4 | 1 | Q6:58711, Q7:0 | 58711 | Q6:58711 | Q6:575040, Q7:212480 |
| sw04-p5 | 1 | Q6:6108, Q7:60429 | 66537 | Q6:6108, Q7:47381 | Q6:426880, Q7:266880 |
| sw05-p4 | 1 | Q6:0, Q7:4016 | 4016 | Q7:4016 | Q6:324480, Q7:425600 |
| sw05-p5 | 1 | Q6:19508, Q7:5738 | 25245 | Q6:15895, Q7:5738 | Q6:381440, Q7:301760 |
| sw06-p4 | 1 | Q6:5321, Q7:53103 | 58424 | Q6:5321, Q7:41707 | Q6:403520, Q7:309760 |
| sw06-p5 | 1 | Q6:51911, Q7:0 | 51911 | Q6:51911 | Q6:591680, Q7:195840 |
| sw07-p4 | 1 | Q6:17513, Q7:5010 | 22523 | Q6:14326, Q7:5010 | Q6:382080, Q7:328000 |
| sw07-p5 | 1 | Q6:0, Q7:3619 | 3619 | Q7:3619 | Q6:249600, Q7:475520 |
| sw08-p4 | 1 | Q6:45898, Q7:0 | 45898 | Q6:45898 | Q6:608320, Q7:179200 |
| sw08-p5 | 1 | Q6:15722, Q7:4375 | 20097 | Q6:12911, Q7:4375 | Q6:370240, Q7:351360 |

Total applied: **15785600 ns** across 22 port(s). Network total slack now banked: **15785600 ns**. GCL_size overflow: 0.

## Per-port GCL entries: before (SMT) vs. after (heuristic-enlarged)

| port | SMT entries | enlarged entries | GCL_size |
|---|---|---|---|
| sw01-p2 | 25 | 32 | 255 |
| sw01-p4 | 9 | 21 | 255 |
| sw01-p5 | 11 | 16 | 255 |
| sw02-p2 | 13 | 18 | 255 |
| sw02-p4 | 11 | 19 | 255 |
| sw02-p5 | 13 | 23 | 255 |
| sw03-p4 | 13 | 22 | 255 |
| sw03-p5 | 9 | 18 | 255 |
| sw04-p4 | 3 | 10 | 255 |
| sw04-p5 | 11 | 24 | 255 |
| sw05-p4 | 9 | 18 | 255 |
| sw05-p5 | 13 | 22 | 255 |
| sw06-p4 | 11 | 21 | 255 |
| sw06-p5 | 3 | 10 | 255 |
| sw07-p4 | 13 | 21 | 255 |
| sw07-p5 | 9 | 22 | 255 |
| sw08-p2 | 19 | 24 | 255 |
| sw08-p4 | 3 | 10 | 255 |
| sw08-p5 | 13 | 21 | 255 |

## Flows

| flow | route | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|
| s0(id=1 S3->S1) | S3->sw01->sw02->S1 | 7 | 24960 | 45840 | yes |
| s1(id=2 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | - | - | - | no |
| s2(id=3 S1->S3) | S1->sw02->sw01->S3 | 6 | 0 | 45840 | yes |
| s3(id=4 S1->S3) | S1->sw02->sw01->S3 | - | - | - | no |
| s4(id=5 S3->S1) | S3->sw01->sw02->S1 | 7 | 74880 | 45840 | yes |
| s5(id=6 S1->S3) | S1->sw02->sw01->S3 | - | - | - | no |
| s6(id=7 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 7 | 0 | 108560 | yes |
| s7(id=8 S1->S3) | S1->sw02->sw01->S3 | - | - | - | no |
| s8(id=9 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 7 | 0 | 95760 | yes |
| s9(id=10 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | 6 | 49920 | 83600 | yes |
| s10(id=11 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 6 | 24960 | 96400 | yes |
| s11(id=12 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 6 | 24960 | 83600 | yes |
| s12(id=13 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | - | - | - | no |
| s13(id=14 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | - | - | - | no |
| s14(id=15 S3->S1) | S3->sw01->sw02->S1 | 7 | 49920 | 45840 | yes |
| s15(id=16 S3->S1) | S3->sw01->sw02->S1 | - | - | - | no |
| s16(id=17 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 7 | 74880 | 79120 | yes |
| s17(id=18 S1->S3) | S1->sw02->sw01->S3 | 6 | 49920 | 45840 | yes |
| s18(id=19 S3->S1) | S3->sw01->sw02->S1 | - | - | - | no |
| s19(id=20 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | - | - | - | no |

## Per-hop windows (slack_ns > 0 means this window was enlarged)

| flow | egress port | queue | psi (ns) | delta (ns) |
|---|---|---|---|---|
| s0(id=1 S3->S1) | S3-p0 | Q7 | 24960 | 12480 |
| s0(id=1 S3->S1) | sw01-p5 | Q7 | 41600 | 12480 |
| s0(id=1 S3->S1) | sw02-p2 | Q7 | 58240 | 12480 |
| s2(id=3 S1->S3) | S1-p0 | Q6 | 0 | 12480 |
| s2(id=3 S1->S3) | sw02-p5 | Q6 | 16640 | 12480 |
| s2(id=3 S1->S3) | sw01-p2 | Q6 | 33280 | 12480 |
| s4(id=5 S3->S1) | S3-p0 | Q7 | 74880 | 12480 |
| s4(id=5 S3->S1) | sw01-p5 | Q7 | 91520 | 12480 |
| s4(id=5 S3->S1) | sw02-p2 | Q7 | 108160 | 12480 |
| s6(id=7 S2->S3) | S2-p0 | Q7 | 0 | 12480 |
| s6(id=7 S2->S3) | sw08-p5 | Q7 | 16640 | 12480 |
| s6(id=7 S2->S3) | sw07-p4 | Q7 | 40000 | 12480 |
| s6(id=7 S2->S3) | sw05-p5 | Q7 | 56640 | 12480 |
| s6(id=7 S2->S3) | sw03-p4 | Q7 | 73280 | 12480 |
| s6(id=7 S2->S3) | sw01-p2 | Q7 | 96000 | 12480 |
| s8(id=9 S3->S2) | S3-p0 | Q7 | 0 | 12480 |
| s8(id=9 S3->S2) | sw01-p4 | Q7 | 16640 | 12480 |
| s8(id=9 S3->S2) | sw03-p5 | Q7 | 33280 | 12480 |
| s8(id=9 S3->S2) | sw05-p4 | Q7 | 49920 | 12480 |
| s8(id=9 S3->S2) | sw07-p5 | Q7 | 66560 | 12480 |
| s8(id=9 S3->S2) | sw08-p2 | Q7 | 83200 | 12480 |
| s9(id=10 S2->S1) | S2-p0 | Q6 | 49920 | 12480 |
| s9(id=10 S2->S1) | sw08-p4 | Q6 | 66560 | 12480 |
| s9(id=10 S2->S1) | sw06-p5 | Q6 | 83200 | 12480 |
| s9(id=10 S2->S1) | sw04-p4 | Q6 | 99840 | 12480 |
| s9(id=10 S2->S1) | sw02-p2 | Q6 | 120960 | 12480 |
| s10(id=11 S2->S3) | S2-p0 | Q6 | 24960 | 12480 |
| s10(id=11 S2->S3) | sw08-p5 | Q6 | 41600 | 12480 |
| s10(id=11 S2->S3) | sw07-p4 | Q6 | 58240 | 12480 |
| s10(id=11 S2->S3) | sw05-p5 | Q6 | 74880 | 12480 |
| s10(id=11 S2->S3) | sw03-p4 | Q6 | 91520 | 12480 |
| s10(id=11 S2->S3) | sw01-p2 | Q6 | 108800 | 12480 |
| s11(id=12 S1->S2) | S1-p0 | Q6 | 24960 | 12480 |
| s11(id=12 S1->S2) | sw02-p4 | Q6 | 42240 | 12480 |
| s11(id=12 S1->S2) | sw04-p5 | Q6 | 58880 | 12480 |
| s11(id=12 S1->S2) | sw06-p4 | Q6 | 75520 | 12480 |
| s11(id=12 S1->S2) | sw08-p2 | Q6 | 96000 | 12480 |
| s14(id=15 S3->S1) | S3-p0 | Q7 | 49920 | 12480 |
| s14(id=15 S3->S1) | sw01-p5 | Q7 | 66560 | 12480 |
| s14(id=15 S3->S1) | sw02-p2 | Q7 | 83200 | 12480 |
| s16(id=17 S1->S2) | S1-p0 | Q7 | 74880 | 12480 |
| s16(id=17 S1->S2) | sw02-p4 | Q7 | 91520 | 12480 |
| s16(id=17 S1->S2) | sw04-p5 | Q7 | 108160 | 12480 |
| s16(id=17 S1->S2) | sw06-p4 | Q7 | 124800 | 12480 |
| s16(id=17 S1->S2) | sw08-p2 | Q7 | 141440 | 12480 |
| s17(id=18 S1->S3) | S1-p0 | Q6 | 49920 | 12480 |
| s17(id=18 S1->S3) | sw02-p5 | Q6 | 66560 | 12480 |
| s17(id=18 S1->S3) | sw01-p2 | Q6 | 83200 | 12480 |

## Constraint check

- C1-C7, C9: OK
- seed-integrity (no SMT-fixed flow's placement changed): OK

## GCL per egress port

### sw01-p2  (32 entries, util 18.7200 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 33280 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 74560 0x40 # 01000000   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12800 0x40 # 01000000   Q6
sgs 3840 0x3F # 00111111   BE
sgs 46080 0xBF # 10111111   Q7
sgs 87360 0x80 # 10000000   Q7
sgs 16640 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 33280 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 74560 0x40 # 01000000   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12800 0x40 # 01000000   Q6
sgs 3840 0x3F # 00111111   BE
sgs 46080 0xBF # 10111111   Q7
sgs 54080 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p4  (21 entries, util 6.2400 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 75200 0x80 # 10000000   Q7
sgs 8320 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 75200 0x80 # 10000000   Q7
sgs 8320 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 75200 0x80 # 10000000   Q7
sgs 8320 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 58560 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p5  (16 entries, util 7.8000 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 244800 0x80 # 10000000   Q7
sgs 13760 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 228160 0x80 # 10000000   Q7
sgs 5440 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (18 entries, util 9.3600 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 233920 0x40 # 01000000   Q6
sgs 45120 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 213440 0x80 # 10000000   Q7
sgs 3520 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p4  (19 entries, util 7.8000 %)

```
sgs 42240 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 36800 0xBF # 10111111   Q7
sgs 27840 0x80 # 10000000   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 42240 0x7F # 01111111   Q6
sgs 77120 0x40 # 01000000   Q6
sgs 30720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 42240 0x7F # 01111111   Q6
sgs 77120 0x40 # 01000000   Q6
sgs 30720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 42240 0x7F # 01111111   Q6
sgs 34880 0x40 # 01000000   Q6
sgs 23040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p5  (23 entries, util 9.3600 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 59520 0x40 # 01000000   Q6
sgs 24000 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 109440 0x40 # 01000000   Q6
sgs 24000 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 59520 0x40 # 01000000   Q6
sgs 24000 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 92800 0x40 # 01000000   Q6
sgs 40640 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (22 entries, util 9.3600 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 23360 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 5760 0x3F # 00111111   BE
sgs 78400 0x40 # 01000000   Q6
sgs 30080 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 23360 0xBF # 10111111   Q7
sgs 96640 0x80 # 10000000   Q7
sgs 30080 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 23360 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 5760 0x3F # 00111111   BE
sgs 78400 0x40 # 01000000   Q6
sgs 30080 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 23360 0xBF # 10111111   Q7
sgs 23360 0x80 # 10000000   Q7
sgs 3520 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p5  (18 entries, util 6.2400 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 75200 0x80 # 10000000   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 75200 0x80 # 10000000   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 75200 0x80 # 10000000   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 41920 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p4  (10 entries, util 1.5600 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 437760 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (24 entries, util 7.8000 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 8960 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 28800 0xBF # 10111111   Q7
sgs 8000 0x3F # 00111111   BE
sgs 27840 0x80 # 10000000   Q7
sgs 14080 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 8960 0x3F # 00111111   BE
sgs 77120 0x40 # 01000000   Q6
sgs 14080 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 8960 0x3F # 00111111   BE
sgs 77120 0x40 # 01000000   Q6
sgs 14080 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 8960 0x3F # 00111111   BE
sgs 18240 0x40 # 01000000   Q6
sgs 23040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (18 entries, util 6.2400 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 75200 0x80 # 10000000   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 75200 0x80 # 10000000   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 75200 0x80 # 10000000   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 25280 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p5  (22 entries, util 9.3600 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 6720 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 5760 0x3F # 00111111   BE
sgs 78400 0x40 # 01000000   Q6
sgs 46720 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 6720 0x3F # 00111111   BE
sgs 96640 0x80 # 10000000   Q7
sgs 46720 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 6720 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 5760 0x3F # 00111111   BE
sgs 78400 0x40 # 01000000   Q6
sgs 46720 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 6720 0x3F # 00111111   BE
sgs 40000 0x80 # 10000000   Q7
sgs 3520 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p4  (21 entries, util 7.8000 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 25600 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12160 0x3F # 00111111   BE
sgs 24640 0x7F # 01111111   Q6
sgs 27840 0x80 # 10000000   Q7
sgs 47360 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 25600 0xBF # 10111111   Q7
sgs 77120 0x40 # 01000000   Q6
sgs 47360 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 25600 0xBF # 10111111   Q7
sgs 77120 0x40 # 01000000   Q6
sgs 47360 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 25600 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12160 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (10 entries, util 1.5600 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 454400 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (21 entries, util 9.3600 %)

```
sgs 40000 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 5760 0x3F # 00111111   BE
sgs 78400 0x40 # 01000000   Q6
sgs 13440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 40000 0x7F # 01111111   Q6
sgs 96640 0x80 # 10000000   Q7
sgs 13440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 40000 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 5760 0x3F # 00111111   BE
sgs 78400 0x40 # 01000000   Q6
sgs 13440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 40000 0x7F # 01111111   Q6
sgs 56640 0x80 # 10000000   Q7
sgs 3520 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p5  (22 entries, util 6.2400 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 75200 0x80 # 10000000   Q7
sgs 8320 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 75200 0x80 # 10000000   Q7
sgs 8320 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 75200 0x80 # 10000000   Q7
sgs 8320 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 21120 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p2  (24 entries, util 14.0400 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 32960 0x7F # 01111111   Q6
sgs 73280 0x80 # 10000000   Q7
sgs 35200 0x7F # 01111111   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 118720 0x40 # 01000000   Q6
sgs 35200 0x7F # 01111111   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 118720 0x40 # 01000000   Q6
sgs 35200 0x7F # 01111111   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 35520 0x40 # 01000000   Q6
sgs 18560 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p4  (10 entries, util 1.5600 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 471040 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (21 entries, util 9.3600 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 71680 0x40 # 01000000   Q6
sgs 36800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 96640 0x80 # 10000000   Q7
sgs 36800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 71680 0x40 # 01000000   Q6
sgs 36800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 80000 0x80 # 10000000   Q7
sgs 3520 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

