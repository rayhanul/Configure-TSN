# Heuristic-enlarged GCL schedule (Problem 2: window enlargement)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Time-sensitive PCPs considered: [6, 7]
- Seeded from SMT run: **result/result-2026-10-12-dataset-testbed-7-ring-avgwin/smt-c9-off/7-t3600-c9off-minlat**

## Admission (unchanged by this package -- it only widens windows)

SMT-fixed flows: **11**/20. This package never admits a flow itself; it banks slack for a later admission pass (`prob_3_admit`, Problem 3) to use.

## Opportunistic idle top-up (Step 7 -- see enlarge.py)

Total: **13086080 ns**, drawn from idle capacity on ports at or below utilisation 0.2, independent of any route's deadline-slack budget.

| port | queue | applied (ns) |
|---|---|---|
| S1-p0 | Q6 | 40640 |
| S1-p0 | Q7 | 585600 |
| S2-p0 | Q7 | 653760 |
| S3-p0 | Q6 | 573440 |
| S3-p0 | Q7 | 16000 |
| sw01-p2 | Q7 | 666880 |
| sw01-p4 | Q6 | 704000 |
| sw01-p5 | Q6 | 200960 |
| sw01-p5 | Q7 | 419520 |
| sw02-p2 | Q6 | 146880 |
| sw02-p2 | Q7 | 377920 |
| sw02-p4 | Q6 | 41920 |
| sw02-p4 | Q7 | 571520 |
| sw03-p4 | Q7 | 686720 |
| sw03-p5 | Q6 | 688000 |
| sw04-p4 | Q7 | 651200 |
| sw04-p5 | Q6 | 43200 |
| sw04-p5 | Q7 | 557120 |
| sw05-p4 | Q6 | 671680 |
| sw05-p5 | Q7 | 706240 |
| sw06-p4 | Q6 | 44160 |
| sw06-p4 | Q7 | 542080 |
| sw06-p5 | Q7 | 674560 |
| sw07-p4 | Q7 | 725440 |
| sw07-p5 | Q6 | 655360 |
| sw08-p4 | Q7 | 697280 |
| sw08-p5 | Q7 | 744000 |

## Opportunistic window creation (Step 8 -- see enlarge.py)

**14** brand-new window(s) opened, **174720 ns** total, on ports at or below utilisation 0.2 whose TT queue had zero windows before this run.

| port | queue | size (ns) |
|---|---|---|
| sw01-p2 | Q6 | 12480 |
| sw01-p4 | Q7 | 12480 |
| sw02-p5 | Q6 | 12480 |
| sw02-p5 | Q7 | 12480 |
| sw03-p4 | Q6 | 12480 |
| sw03-p5 | Q7 | 12480 |
| sw04-p4 | Q6 | 12480 |
| sw05-p4 | Q7 | 12480 |
| sw05-p5 | Q6 | 12480 |
| sw06-p5 | Q6 | 12480 |
| sw07-p4 | Q6 | 12480 |
| sw07-p5 | Q7 | 12480 |
| sw08-p4 | Q6 | 12480 |
| sw08-p5 | Q6 | 12480 |

## Best-effort gap equalization (Step 9 -- see enlarge.py)

**7395840 ns** given back from Steps 7/8's growth so each port's leftover non-TAS gaps land close to equal, instead of one gap staying huge while a neighbour is squeezed to the bare 1-tick C10 minimum.

| port | given back (ns) |
|---|---|
| sw01-p4 | 499200 |
| sw03-p5 | 499200 |
| sw05-p4 | 487040 |
| sw07-p5 | 470400 |
| sw01-p5 | 412160 |
| S2-p0 | 393280 |
| sw01-p2 | 387200 |
| sw03-p4 | 387200 |
| sw05-p5 | 387200 |
| sw07-p4 | 387200 |
| sw08-p5 | 387200 |
| sw02-p2 | 362560 |
| sw06-p4 | 303360 |
| sw02-p4 | 299520 |
| sw04-p5 | 299520 |
| S1-p0 | 299520 |
| S3-p0 | 299520 |
| sw04-p4 | 262400 |
| sw06-p5 | 262400 |
| sw08-p4 | 262400 |
| sw08-p2 | 47360 |

## Opportunistic overlay window creation (Step 10 -- see enlarge.py)

**42** new overlay window(s), **8613760 ns** total, carved out of already-open best-effort spans on ports at or below utilisation 0.2 -- best-effort stays reachable inside each one (gate mask keeps its BE bits set), so none of this is closed off from BE.

| port | queue | size (ns) |
|---|---|---|
| S1-p0 | Q6 | 74880 |
| S1-p0 | Q7 | 224640 |
| S2-p0 | Q6 | 192960 |
| S2-p0 | Q7 | 200320 |
| S3-p0 | Q6 | 74880 |
| S3-p0 | Q7 | 224640 |
| sw01-p2 | Q6 | 230720 |
| sw01-p2 | Q7 | 216640 |
| sw01-p4 | Q6 | 303680 |
| sw01-p4 | Q7 | 224640 |
| sw01-p5 | Q6 | 136000 |
| sw01-p5 | Q7 | 259200 |
| sw02-p2 | Q6 | 151680 |
| sw02-p2 | Q7 | 222080 |
| sw02-p4 | Q6 | 128960 |
| sw02-p4 | Q7 | 187200 |
| sw02-p5 | Q6 | 374400 |
| sw02-p5 | Q7 | 400640 |
| sw03-p4 | Q6 | 230720 |
| sw03-p4 | Q7 | 210560 |
| sw03-p5 | Q6 | 287040 |
| sw03-p5 | Q7 | 224640 |
| sw04-p4 | Q6 | 149760 |
| sw04-p4 | Q7 | 175040 |
| sw04-p5 | Q6 | 145600 |
| sw04-p5 | Q7 | 124800 |
| sw05-p4 | Q6 | 237120 |
| sw05-p4 | Q7 | 312320 |
| sw05-p5 | Q6 | 230720 |
| sw05-p5 | Q7 | 193920 |
| sw06-p4 | Q6 | 212160 |
| sw06-p4 | Q7 | 125440 |
| sw06-p5 | Q6 | 149760 |
| sw06-p5 | Q7 | 150080 |
| sw07-p4 | Q6 | 197440 |
| sw07-p4 | Q7 | 200320 |
| sw07-p5 | Q6 | 233280 |
| sw07-p5 | Q7 | 316160 |
| sw08-p4 | Q6 | 141440 |
| sw08-p4 | Q7 | 150080 |
| sw08-p5 | Q6 | 186880 |
| sw08-p5 | Q7 | 200320 |

## Candidate routes (P^cand = routes of the fixed flows above)

| route | PCPs carried | flows |
|---|---|---|
| S1->sw02->sw04->sw06->sw08->S2 | Q6 (1), Q7 (4) | 5 |
| S2->sw08->sw06->sw04->sw02->S1 | Q7 (1) | 1 |
| S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 (1) | 1 |
| S3->sw01->sw02->S1 | Q6 (2), Q7 (1) | 3 |
| S3->sw01->sw03->sw05->sw07->sw08->S2 | Q6 (1) | 1 |

## Per-link enlargement accounting

| link | sharing eta | route-safe slack (ns) | link budget (ns) | final slack (ns) | applied (ns) |
|---|---|---|---|---|---|
| S2-p0 | 2 | Q6:0, Q7:108940 | 108940 | Q7:108940 | Q6:192960, Q7:569600 |
| S3-p0 | 2 | Q6:27029, Q7:56157 | 83187 | Q6:27029, Q7:34038 | Q6:425600, Q7:224640 |
| sw02-p2 | 2 | Q6:101278, Q7:39224 | 140502 | Q6:90725, Q7:39224 | Q6:238720, Q7:426880 |
| sw08-p2 | 2 | Q6:28509, Q7:35895 | 64404 | Q6:28509, Q7:34374 | Q6:7040, Q7:8320 |
| S1-p0 | 1 | Q6:14258, Q7:14937 | 29195 | Q6:9432, Q7:14937 | Q6:74880, Q7:575360 |
| sw01-p2 | 1 | Q6:0, Q7:25074 | 25074 | Q7:25074 | Q6:243200, Q7:521280 |
| sw01-p4 | 1 | Q6:4523, Q7:0 | 4523 | Q6:4523 | Q6:512960, Q7:237120 |
| sw01-p5 | 1 | Q6:49442, Q7:13842 | 63283 | Q6:49442, Q7:13842 | Q6:204480, Q7:462080 |
| sw02-p4 | 1 | Q6:12057, Q7:12312 | 24369 | Q6:8010, Q7:12312 | Q6:128960, Q7:521280 |
| sw03-p4 | 1 | Q6:0, Q7:21855 | 21855 | Q7:21855 | Q6:243200, Q7:531840 |
| sw03-p5 | 1 | Q6:4103, Q7:0 | 4103 | Q6:4103 | Q6:479680, Q7:237120 |
| sw04-p4 | 1 | Q6:0, Q7:61466 | 61466 | Q7:61466 | Q6:162240, Q7:625280 |
| sw04-p5 | 1 | Q6:10196, Q7:10148 | 20344 | Q6:6803, Q7:10148 | Q6:145600, Q7:442240 |
| sw05-p4 | 1 | Q6:3722, Q7:0 | 3722 | Q6:3722 | Q6:425280, Q7:324800 |
| sw05-p5 | 1 | Q6:0, Q7:19049 | 19049 | Q7:19049 | Q6:243200, Q7:531840 |
| sw06-p4 | 1 | Q6:8622, Q7:8364 | 16986 | Q6:5777, Q7:8364 | Q6:212160, Q7:422400 |
| sw06-p5 | 1 | Q6:0, Q7:54817 | 54817 | Q7:54817 | Q6:162240, Q7:616960 |
| sw07-p4 | 1 | Q6:0, Q7:16603 | 16603 | Q7:16603 | Q6:209920, Q7:554880 |
| sw07-p5 | 1 | Q6:3376, Q7:0 | 3376 | Q6:3376 | Q6:421440, Q7:328640 |
| sw08-p4 | 1 | Q6:0, Q7:48888 | 48888 | Q7:48888 | Q6:153920, Q7:633600 |
| sw08-p5 | 1 | Q6:0, Q7:14472 | 14472 | Q7:14472 | Q6:199360, Q7:571520 |

Total applied: **15254720 ns** across 22 port(s). Network total slack now banked: **15271360 ns**. GCL_size overflow: 0.

## Per-port GCL entries: before (SMT) vs. after (heuristic-enlarged)

| port | SMT entries | enlarged entries | GCL_size |
|---|---|---|---|
| sw01-p2 | 5 | 14 | 255 |
| sw01-p4 | 9 | 18 | 255 |
| sw01-p5 | 17 | 26 | 255 |
| sw02-p2 | 19 | 25 | 255 |
| sw02-p4 | 25 | 28 | 255 |
| sw02-p5 | 1 | 18 | 255 |
| sw03-p4 | 5 | 14 | 255 |
| sw03-p5 | 9 | 22 | 255 |
| sw04-p4 | 3 | 10 | 255 |
| sw04-p5 | 25 | 28 | 255 |
| sw05-p4 | 9 | 19 | 255 |
| sw05-p5 | 5 | 12 | 255 |
| sw06-p4 | 25 | 25 | 255 |
| sw06-p5 | 3 | 10 | 255 |
| sw07-p4 | 5 | 13 | 255 |
| sw07-p5 | 9 | 18 | 255 |
| sw08-p2 | 33 | 31 | 255 |
| sw08-p4 | 3 | 9 | 255 |
| sw08-p5 | 5 | 13 | 255 |

## Flows

| flow | route | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|
| s0(id=1 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 6 | 0 | 79120 | yes |
| s1(id=2 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | - | - | - | no |
| s2(id=3 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 7 | 0 | 95760 | yes |
| s3(id=4 S1->S3) | S1->sw02->sw01->S3 | - | - | - | no |
| s4(id=5 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 7 | 74880 | 79120 | yes |
| s5(id=6 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | - | - | - | no |
| s6(id=7 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | 7 | 24960 | 83600 | yes |
| s7(id=8 S3->S1) | S3->sw01->sw02->S1 | 6 | 49920 | 45840 | yes |
| s8(id=9 S3->S1) | S3->sw01->sw02->S1 | 7 | 0 | 45840 | yes |
| s9(id=10 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | - | - | - | no |
| s10(id=11 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | - | - | - | no |
| s11(id=12 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 7 | 24960 | 79120 | yes |
| s12(id=13 S1->S3) | S1->sw02->sw01->S3 | - | - | - | no |
| s13(id=14 S3->S1) | S3->sw01->sw02->S1 | - | - | - | no |
| s14(id=15 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 7 | 49920 | 83600 | yes |
| s15(id=16 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | - | - | - | no |
| s16(id=17 S1->S3) | S1->sw02->sw01->S3 | - | - | - | no |
| s17(id=18 S3->S1) | S3->sw01->sw02->S1 | 6 | 74880 | 46480 | yes |
| s18(id=19 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 7 | 99840 | 79120 | yes |
| s19(id=20 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 6 | 24960 | 95760 | yes |

## Per-hop windows (slack_ns > 0 means this window was enlarged)

| flow | egress port | queue | psi (ns) | delta (ns) |
|---|---|---|---|---|
| s0(id=1 S1->S2) | S1-p0 | Q6 | 0 | 12480 |
| s0(id=1 S1->S2) | sw02-p4 | Q6 | 16640 | 12480 |
| s0(id=1 S1->S2) | sw04-p5 | Q6 | 33280 | 12480 |
| s0(id=1 S1->S2) | sw06-p4 | Q6 | 49920 | 12480 |
| s0(id=1 S1->S2) | sw08-p2 | Q6 | 66560 | 12480 |
| s2(id=3 S2->S3) | S2-p0 | Q7 | 0 | 12480 |
| s2(id=3 S2->S3) | sw08-p5 | Q7 | 16640 | 12480 |
| s2(id=3 S2->S3) | sw07-p4 | Q7 | 33280 | 12480 |
| s2(id=3 S2->S3) | sw05-p5 | Q7 | 49920 | 12480 |
| s2(id=3 S2->S3) | sw03-p4 | Q7 | 66560 | 12480 |
| s2(id=3 S2->S3) | sw01-p2 | Q7 | 83200 | 12480 |
| s4(id=5 S1->S2) | S1-p0 | Q7 | 74880 | 12480 |
| s4(id=5 S1->S2) | sw02-p4 | Q7 | 91520 | 12480 |
| s4(id=5 S1->S2) | sw04-p5 | Q7 | 108160 | 12480 |
| s4(id=5 S1->S2) | sw06-p4 | Q7 | 124800 | 12480 |
| s4(id=5 S1->S2) | sw08-p2 | Q7 | 141440 | 12480 |
| s6(id=7 S2->S1) | S2-p0 | Q7 | 24960 | 12480 |
| s6(id=7 S2->S1) | sw08-p4 | Q7 | 41600 | 12480 |
| s6(id=7 S2->S1) | sw06-p5 | Q7 | 58240 | 12480 |
| s6(id=7 S2->S1) | sw04-p4 | Q7 | 74880 | 12480 |
| s6(id=7 S2->S1) | sw02-p2 | Q7 | 96000 | 12480 |
| s7(id=8 S3->S1) | S3-p0 | Q6 | 49920 | 12480 |
| s7(id=8 S3->S1) | sw01-p5 | Q6 | 66560 | 12480 |
| s7(id=8 S3->S1) | sw02-p2 | Q6 | 83200 | 12480 |
| s8(id=9 S3->S1) | S3-p0 | Q7 | 0 | 12480 |
| s8(id=9 S3->S1) | sw01-p5 | Q7 | 16640 | 12480 |
| s8(id=9 S3->S1) | sw02-p2 | Q7 | 33280 | 12480 |
| s11(id=12 S1->S2) | S1-p0 | Q7 | 24960 | 12480 |
| s11(id=12 S1->S2) | sw02-p4 | Q7 | 41600 | 12480 |
| s11(id=12 S1->S2) | sw04-p5 | Q7 | 58240 | 12480 |
| s11(id=12 S1->S2) | sw06-p4 | Q7 | 74880 | 12480 |
| s11(id=12 S1->S2) | sw08-p2 | Q7 | 91520 | 12480 |
| s14(id=15 S1->S2) | S1-p0 | Q7 | 49920 | 12480 |
| s14(id=15 S1->S2) | sw02-p4 | Q7 | 66560 | 12480 |
| s14(id=15 S1->S2) | sw04-p5 | Q7 | 83200 | 12480 |
| s14(id=15 S1->S2) | sw06-p4 | Q7 | 103680 | 12480 |
| s14(id=15 S1->S2) | sw08-p2 | Q7 | 120960 | 12480 |
| s17(id=18 S3->S1) | S3-p0 | Q6 | 74880 | 12480 |
| s17(id=18 S3->S1) | sw01-p5 | Q6 | 92160 | 12480 |
| s17(id=18 S3->S1) | sw02-p2 | Q6 | 108800 | 12480 |
| s18(id=19 S1->S2) | S1-p0 | Q7 | 99840 | 12480 |
| s18(id=19 S1->S2) | sw02-p4 | Q7 | 116480 | 12480 |
| s18(id=19 S1->S2) | sw04-p5 | Q7 | 133120 | 12480 |
| s18(id=19 S1->S2) | sw06-p4 | Q7 | 149760 | 12480 |
| s18(id=19 S1->S2) | sw08-p2 | Q7 | 166400 | 12480 |
| s19(id=20 S3->S2) | S3-p0 | Q6 | 24960 | 12480 |
| s19(id=20 S3->S2) | sw01-p4 | Q6 | 41600 | 12480 |
| s19(id=20 S3->S2) | sw03-p5 | Q6 | 58240 | 12480 |
| s19(id=20 S3->S2) | sw05-p4 | Q6 | 74880 | 12480 |
| s19(id=20 S3->S2) | sw07-p5 | Q6 | 91520 | 12480 |
| s19(id=20 S3->S2) | sw08-p2 | Q6 | 108160 | 12480 |

## Constraint check

- C1-C7, C9: OK
- seed-integrity (no SMT-fixed flow's placement changed): OK

## GCL per egress port

### sw01-p2  (14 entries, util 3.1200 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 206400 0x80 # 10000000   Q7
sgs 10560 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 123200 0x80 # 10000000   Q7
sgs 43520 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p4  (18 entries, util 6.2400 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 75200 0x40 # 01000000   Q6
sgs 33280 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 75200 0x40 # 01000000   Q6
sgs 33280 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 75200 0x40 # 01000000   Q6
sgs 33280 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 33600 0x40 # 01000000   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p5  (26 entries, util 12.4800 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 13120 0xBF # 10111111   Q7
sgs 46720 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 122240 0x80 # 10000000   Q7
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 13120 0xBF # 10111111   Q7
sgs 46720 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 105600 0x80 # 10000000   Q7
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (25 entries, util 14.0400 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 33280 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 56000 0x40 # 01000000   Q6
sgs 35200 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 131520 0x80 # 10000000   Q7
sgs 35200 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 33280 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 13120 0x3F # 00111111   BE
sgs 56000 0x40 # 01000000   Q6
sgs 35200 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 98240 0x80 # 10000000   Q7
sgs 18560 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p4  (28 entries, util 18.7200 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 50240 0x80 # 10000000   Q7
sgs 33280 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 125120 0x80 # 10000000   Q7
sgs 33280 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 100160 0x80 # 10000000   Q7
sgs 33280 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 108480 0x80 # 10000000   Q7
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

### sw03-p4  (14 entries, util 3.1200 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 206400 0x80 # 10000000   Q7
sgs 27200 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 139840 0x80 # 10000000   Q7
sgs 43520 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p5  (22 entries, util 6.2400 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 8320 0x3F # 00111111   BE
sgs 75200 0x40 # 01000000   Q6
sgs 16640 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 8320 0x3F # 00111111   BE
sgs 75200 0x40 # 01000000   Q6
sgs 16640 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 8320 0x3F # 00111111   BE
sgs 75200 0x40 # 01000000   Q6
sgs 16640 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 8320 0x3F # 00111111   BE
sgs 16960 0x40 # 01000000   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p4  (10 entries, util 1.5600 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 462720 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (28 entries, util 18.7200 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 50240 0x80 # 10000000   Q7
sgs 16640 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 125120 0x80 # 10000000   Q7
sgs 16640 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 100160 0x80 # 10000000   Q7
sgs 16640 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 91840 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (19 entries, util 6.2400 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 75200 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 75200 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 75200 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12800 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p5  (12 entries, util 3.1200 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 206400 0x80 # 10000000   Q7
sgs 43840 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 156480 0x80 # 10000000   Q7
sgs 43520 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p4  (25 entries, util 18.7200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 3520 0x3F # 00111111   BE
sgs 33600 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 50240 0x80 # 10000000   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 125120 0x80 # 10000000   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 3520 0x3F # 00111111   BE
sgs 96320 0x80 # 10000000   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 75200 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (10 entries, util 1.5600 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 8320 0x3F # 00111111   BE
sgs 479360 0x80 # 10000000   Q7
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

### sw07-p5  (18 entries, util 6.2400 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 75200 0x40 # 01000000   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 75200 0x40 # 01000000   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 75200 0x40 # 01000000   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 46080 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p2  (31 entries, util 24.9600 %)

```
sgs 66560 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 32960 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 16640 0x80 # 10000000   Q7
sgs 83520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 16000 0x40 # 01000000   Q6
sgs 142400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 16640 0x80 # 10000000   Q7
sgs 128960 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 16000 0x40 # 01000000   Q6
sgs 75840 0x3F # 00111111   BE
```

### sw08-p4  (9 entries, util 1.5600 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 29120 0x7F # 01111111   Q6
sgs 496000 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (13 entries, util 3.1200 %)

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

