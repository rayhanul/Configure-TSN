# RL-enlarged GCL schedule (Problem 2: window enlargement)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Seeded from SMT run: **result/result-2026-10-13-dataset-testbed-11-tree-avgwin/smt-c9-on/11-fair-retimed-c9on**

## Admission (unchanged) vs. capacity grown

Problem 2 never admits a flow into the schedule it exports -- it only widens windows. `admitted` below is exactly the SMT baseline, by construction; the capacity growth this run achieved is banked slack and per-port GCL entries, reported separately.

| | admitted | of total |
|---|---|---|
| SMT (fixed, never moved) | 10 | 10 |
| RL-enlarged (exported; grow-only, admits nothing new) | 10 | 20 |

During training, the policy's trial admissions (the reward signal that teaches it how much a window needs to grow) reached **7** of the 10 SMT-rejected flows -- none of those are kept in this export; that capacity stays as empty, banked slack for Problem 3 to fill. Total slack banked: 543680 ns. GCL_size overflow: 0.

## Opportunistic idle top-up (deterministic post-pass)

**11405440 ns**, drawn from idle capacity on ports at or below utilisation 0.2, independent of what training happened to grow. Ported from prob_2_heuristic_enlarged's Step 7.

| port | queue | applied (ns) |
|---|---|---|
| S1-p0 | Q6 | 287680 |
| S1-p0 | Q7 | 350080 |
| S2-p0 | Q6 | 375040 |
| S2-p0 | Q7 | 287680 |
| S3-p0 | Q6 | 100160 |
| S3-p0 | Q7 | 525120 |
| sw01-p2 | Q6 | 166400 |
| sw01-p2 | Q7 | 434240 |
| sw01-p4 | Q6 | 93760 |
| sw01-p4 | Q7 | 483840 |
| sw02-p2 | Q6 | 510080 |
| sw02-p2 | Q7 | 53760 |
| sw02-p4 | Q6 | 145280 |
| sw02-p4 | Q7 | 484160 |
| sw03-p4 | Q6 | 165440 |
| sw03-p4 | Q7 | 440320 |
| sw03-p5 | Q6 | 96960 |
| sw03-p5 | Q7 | 471360 |
| sw04-p4 | Q6 | 516480 |
| sw04-p4 | Q7 | 56640 |
| sw04-p5 | Q6 | 140480 |
| sw04-p5 | Q7 | 480640 |
| sw05-p4 | Q6 | 100160 |
| sw05-p4 | Q7 | 458880 |
| sw05-p5 | Q6 | 166400 |
| sw05-p5 | Q7 | 442560 |
| sw06-p4 | Q6 | 135680 |
| sw06-p4 | Q7 | 477120 |
| sw06-p5 | Q6 | 522880 |
| sw06-p5 | Q7 | 59520 |
| sw07-p4 | Q6 | 169280 |
| sw07-p4 | Q7 | 445760 |
| sw07-p5 | Q6 | 103360 |
| sw07-p5 | Q7 | 446400 |
| sw08-p4 | Q6 | 529280 |
| sw08-p4 | Q7 | 62400 |
| sw08-p5 | Q6 | 170240 |
| sw08-p5 | Q7 | 449920 |

## Best-effort gap equalization (deterministic post-pass)

**6953920 ns** given back from the top-up/creation above so each port's leftover non-TAS gaps land close to equal. Ported from prob_2_heuristic_enlarged's Step 9.

| port | given back (ns) |
|---|---|---|
| sw02-p2 | 454080 |
| sw04-p4 | 453440 |
| sw06-p5 | 452800 |
| sw08-p4 | 452160 |
| sw08-p5 | 417600 |
| sw07-p4 | 412800 |
| sw05-p5 | 408000 |
| sw03-p4 | 402240 |
| sw01-p2 | 392320 |
| sw02-p4 | 366720 |
| sw04-p5 | 361920 |
| S1-p0 | 360960 |
| sw06-p4 | 357120 |
| S2-p0 | 314240 |
| S3-p0 | 307520 |
| sw07-p5 | 260480 |
| sw05-p4 | 260160 |
| sw03-p5 | 259840 |
| sw01-p4 | 259520 |

## Opportunistic overlay window creation (deterministic post-pass)

**38** new overlay window(s), **7038080 ns** total, carved out of already-open best-effort spans on ports at or below utilisation 0.2 -- best-effort stays reachable inside each one (gate mask keeps its BE bits set). Run once after training/finalize_grow_only(), not a trained action.

| port | queue | size (ns) |
|---|---|---|
| S1-p0 | Q6 | 161280 |
| S1-p0 | Q7 | 199680 |
| S2-p0 | Q6 | 114560 |
| S2-p0 | Q7 | 199680 |
| S3-p0 | Q6 | 74880 |
| S3-p0 | Q7 | 232640 |
| sw01-p2 | Q6 | 201600 |
| sw01-p2 | Q7 | 243520 |
| sw01-p4 | Q6 | 61440 |
| sw01-p4 | Q7 | 142080 |
| sw02-p2 | Q6 | 186560 |
| sw02-p2 | Q7 | 291840 |
| sw02-p4 | Q6 | 66560 |
| sw02-p4 | Q7 | 282880 |
| sw03-p4 | Q6 | 181440 |
| sw03-p4 | Q7 | 265920 |
| sw03-p5 | Q6 | 92160 |
| sw03-p5 | Q7 | 119040 |
| sw04-p4 | Q6 | 188800 |
| sw04-p4 | Q7 | 282880 |
| sw04-p5 | Q6 | 122880 |
| sw04-p5 | Q7 | 243200 |
| sw05-p4 | Q6 | 138240 |
| sw05-p4 | Q7 | 96000 |
| sw05-p5 | Q6 | 177600 |
| sw05-p5 | Q7 | 267840 |
| sw06-p4 | Q6 | 124800 |
| sw06-p4 | Q7 | 249600 |
| sw06-p5 | Q6 | 170240 |
| sw06-p5 | Q7 | 282560 |
| sw07-p4 | Q6 | 172800 |
| sw07-p4 | Q7 | 267840 |
| sw07-p5 | Q6 | 198080 |
| sw07-p5 | Q7 | 47040 |
| sw08-p4 | Q6 | 186880 |
| sw08-p4 | Q7 | 265280 |
| sw08-p5 | Q6 | 138880 |
| sw08-p5 | Q7 | 298880 |

## Per-port GCL entries: before (SMT) vs. after (RL-enlarged)

| port | SMT entries | RL-enlarged entries | GCL_size |
|---|---|---|---|
| sw01-p2 | 3 | 24 | 255 |
| sw01-p4 | 23 | 18 | 255 |
| sw02-p2 | 15 | 24 | 255 |
| sw02-p4 | 17 | 29 | 255 |
| sw03-p4 | 3 | 23 | 255 |
| sw03-p5 | 23 | 18 | 255 |
| sw04-p4 | 15 | 23 | 255 |
| sw04-p5 | 17 | 32 | 255 |
| sw05-p4 | 23 | 18 | 255 |
| sw05-p5 | 3 | 21 | 255 |
| sw06-p4 | 17 | 30 | 255 |
| sw06-p5 | 15 | 21 | 255 |
| sw07-p4 | 3 | 23 | 255 |
| sw07-p5 | 23 | 15 | 255 |
| sw08-p2 | 35 | 25 | 255 |
| sw08-p4 | 15 | 21 | 255 |
| sw08-p5 | 3 | 23 | 255 |

## Flows

| flow | route | fixed | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|---|
| s0(id=1 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | yes | 7 | 0 | 45840 | yes |
| s1(id=2 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | yes | 7 | 0 | 58640 | yes |
| s2(id=3 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | yes | 6 | 24960 | 46480 | yes |
| s3(id=4 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |
| s4(id=5 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | yes | 6 | 0 | 36880 | yes |
| s5(id=6 S3->S1) | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | no | None | None | None | no |
| s6(id=7 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | yes | 6 | 37440 | 39440 | yes |
| s7(id=8 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | yes | 7 | 24960 | 59280 | yes |
| s8(id=9 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | yes | 6 | 74880 | 38160 | yes |
| s9(id=10 S3->S1) | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | yes | 7 | 49920 | 66320 | yes |
| s10(id=11 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |
| s11(id=12 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |
| s12(id=13 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |
| s13(id=14 S3->S1) | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | no | None | None | None | no |
| s14(id=15 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |
| s15(id=16 S3->S1) | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | no | None | None | None | no |
| s16(id=17 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | no | None | None | None | no |
| s17(id=18 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | yes | 7 | 62400 | 54160 | yes |
| s18(id=19 S3->S1) | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | no | None | None | None | no |
| s19(id=20 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | yes | 6 | 49920 | 47120 | yes |

## Per-hop windows (slack_ns > 0 means this window was enlarged)

| flow | egress port | queue | psi (ns) | delta (ns) |
|---|---|---|---|---|
| s0(id=1 S1->S2) | S1-p0 | Q7 | 0 | 12480 |
| s0(id=1 S1->S2) | sw02-p4 | Q7 | 8320 | 12480 |
| s0(id=1 S1->S2) | sw04-p5 | Q7 | 16640 | 12480 |
| s0(id=1 S1->S2) | sw06-p4 | Q7 | 24960 | 12480 |
| s0(id=1 S1->S2) | sw08-p2 | Q7 | 33280 | 12480 |
| s1(id=2 S3->S2) | S3-p0 | Q7 | 0 | 12480 |
| s1(id=2 S3->S2) | sw01-p4 | Q7 | 15360 | 12480 |
| s1(id=2 S3->S2) | sw03-p5 | Q7 | 23040 | 12480 |
| s1(id=2 S3->S2) | sw05-p4 | Q7 | 30720 | 12480 |
| s1(id=2 S3->S2) | sw07-p5 | Q7 | 38400 | 12480 |
| s1(id=2 S3->S2) | sw08-p2 | Q7 | 46080 | 12480 |
| s2(id=3 S1->S2) | S1-p0 | Q6 | 24960 | 12480 |
| s2(id=3 S1->S2) | sw02-p4 | Q6 | 33280 | 12480 |
| s2(id=3 S1->S2) | sw04-p5 | Q6 | 41600 | 12480 |
| s2(id=3 S1->S2) | sw06-p4 | Q6 | 49920 | 12480 |
| s2(id=3 S1->S2) | sw08-p2 | Q6 | 58880 | 12480 |
| s4(id=5 S2->S1) | S2-p0 | Q6 | 0 | 12480 |
| s4(id=5 S2->S1) | sw08-p4 | Q6 | 6080 | 12480 |
| s4(id=5 S2->S1) | sw06-p5 | Q6 | 12160 | 12480 |
| s4(id=5 S2->S1) | sw04-p4 | Q6 | 18240 | 12480 |
| s4(id=5 S2->S1) | sw02-p2 | Q6 | 24320 | 12480 |
| s6(id=7 S2->S1) | S2-p0 | Q6 | 37440 | 12480 |
| s6(id=7 S2->S1) | sw08-p4 | Q6 | 44160 | 12480 |
| s6(id=7 S2->S1) | sw06-p5 | Q6 | 50880 | 12480 |
| s6(id=7 S2->S1) | sw04-p4 | Q6 | 57600 | 12480 |
| s6(id=7 S2->S1) | sw02-p2 | Q6 | 64320 | 12480 |
| s7(id=8 S3->S2) | S3-p0 | Q7 | 24960 | 12480 |
| s7(id=8 S3->S2) | sw01-p4 | Q7 | 35200 | 12480 |
| s7(id=8 S3->S2) | sw03-p5 | Q7 | 43520 | 12480 |
| s7(id=8 S3->S2) | sw05-p4 | Q7 | 51840 | 12480 |
| s7(id=8 S3->S2) | sw07-p5 | Q7 | 60160 | 12480 |
| s7(id=8 S3->S2) | sw08-p2 | Q7 | 71680 | 12480 |
| s8(id=9 S3->S2) | S3-p0 | Q6 | 74880 | 12480 |
| s8(id=9 S3->S2) | sw01-p4 | Q6 | 80000 | 12480 |
| s8(id=9 S3->S2) | sw03-p5 | Q6 | 85120 | 12480 |
| s8(id=9 S3->S2) | sw05-p4 | Q6 | 90240 | 12480 |
| s8(id=9 S3->S2) | sw07-p5 | Q6 | 95360 | 12480 |
| s8(id=9 S3->S2) | sw08-p2 | Q6 | 100480 | 12480 |
| s9(id=10 S3->S1) | S3-p0 | Q7 | 49920 | 12480 |
| s9(id=10 S3->S1) | sw01-p4 | Q7 | 56640 | 12480 |
| s9(id=10 S3->S1) | sw03-p5 | Q7 | 63360 | 12480 |
| s9(id=10 S3->S1) | sw05-p4 | Q7 | 70080 | 12480 |
| s9(id=10 S3->S1) | sw07-p5 | Q7 | 76800 | 12480 |
| s9(id=10 S3->S1) | sw08-p4 | Q7 | 83520 | 12480 |
| s9(id=10 S3->S1) | sw06-p5 | Q7 | 90240 | 12480 |
| s9(id=10 S3->S1) | sw04-p4 | Q7 | 96960 | 12480 |
| s9(id=10 S3->S1) | sw02-p2 | Q7 | 103680 | 12480 |
| s17(id=18 S2->S3) | S2-p0 | Q7 | 62400 | 12480 |
| s17(id=18 S2->S3) | sw08-p5 | Q7 | 70720 | 12480 |
| s17(id=18 S2->S3) | sw07-p4 | Q7 | 79040 | 12480 |
| s17(id=18 S2->S3) | sw05-p5 | Q7 | 87360 | 12480 |
| s17(id=18 S2->S3) | sw03-p4 | Q7 | 95680 | 12480 |
| s17(id=18 S2->S3) | sw01-p2 | Q7 | 104000 | 12480 |
| s19(id=20 S1->S2) | S1-p0 | Q6 | 49920 | 12480 |
| s19(id=20 S1->S2) | sw02-p4 | Q6 | 58240 | 12480 |
| s19(id=20 S1->S2) | sw04-p5 | Q6 | 66560 | 12480 |
| s19(id=20 S1->S2) | sw06-p4 | Q6 | 74880 | 12480 |
| s19(id=20 S1->S2) | sw08-p2 | Q6 | 84480 | 12480 |

## Metrics (training/evaluation signal, not the export)

| metric | value |
|---|---|
| trial-placed flow ratio (fixed + trial-admitted) | 0.850 |
| r1  same-queue window adjacency | 0.506 |
| r2  deadline-violation ratio | 0.000 |
| r3  supplier/receiver overlap | 0.996 |
| r4  mean e2e/deadline (admitted) | 0.176 |
| constraint violations | 0 |

## Constraint check

- C1-C7, C9: OK
- seed-integrity (no SMT-fixed flow's placement changed): OK

## GCL per egress port

### sw01-p2  (24 entries, util 1.5600 %)

```
sgs 54080 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 24320 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 22720 0x7F # 01111111   Q6
sgs 98880 0x40 # 01000000   Q6
sgs 62080 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 58560 0x80 # 10000000   Q7
sgs 24640 0xBF # 10111111   Q7
sgs 54080 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 20480 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 121280 0x80 # 10000000   Q7
sgs 62080 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p4  (18 entries, util 17.1600 %)

```
sgs 15360 0x7F # 01111111   Q6
sgs 53760 0x80 # 10000000   Q7
sgs 10880 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 8960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 50240 0x40 # 01000000   Q6
sgs 31680 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 152960 0x80 # 10000000   Q7
sgs 31680 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 152960 0x80 # 10000000   Q7
sgs 31680 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 137600 0x80 # 10000000   Q7
sgs 47040 0xBF # 10111111   Q7
```

### sw02-p2  (24 entries, util 10.9200 %)

```
sgs 24320 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 13120 0x7F # 01111111   Q6
sgs 14400 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 26880 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 33920 0x7F # 01111111   Q6
sgs 23680 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 13760 0xBF # 10111111   Q7
sgs 24320 0x7F # 01111111   Q6
sgs 120960 0x40 # 01000000   Q6
sgs 54720 0xBF # 10111111   Q7
sgs 24320 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 13120 0x7F # 01111111   Q6
sgs 53760 0xBF # 10111111   Q7
sgs 41600 0x80 # 10000000   Q7
sgs 54720 0xBF # 10111111   Q7
sgs 24320 0x7F # 01111111   Q6
sgs 96640 0x40 # 01000000   Q6
sgs 29120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p4  (29 entries, util 12.4800 %)

```
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 640 0x3F # 00111111   BE
sgs 66240 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20800 0x80 # 10000000   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 79360 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 8320 0x3F # 00111111   BE
sgs 79360 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
sgs 20800 0x80 # 10000000   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 71040 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (23 entries, util 1.5600 %)

```
sgs 45760 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 24640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 24320 0x7F # 01111111   Q6
sgs 98560 0x40 # 01000000   Q6
sgs 18880 0x7F # 01111111   Q6
sgs 59840 0xBF # 10111111   Q7
sgs 57280 0x80 # 10000000   Q7
sgs 32960 0xBF # 10111111   Q7
sgs 45760 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 38720 0xBF # 10111111   Q7
sgs 121280 0x80 # 10000000   Q7
sgs 18880 0x7F # 01111111   Q6
sgs 59840 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p5  (18 entries, util 17.1600 %)

```
sgs 23040 0x7F # 01111111   Q6
sgs 52800 0x80 # 10000000   Q7
sgs 9280 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 3520 0x3F # 00111111   BE
sgs 50240 0x40 # 01000000   Q6
sgs 24000 0xBF # 10111111   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 152960 0x80 # 10000000   Q7
sgs 24000 0xBF # 10111111   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 152960 0x80 # 10000000   Q7
sgs 24000 0xBF # 10111111   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 129920 0x80 # 10000000   Q7
sgs 47040 0xBF # 10111111   Q7
```

### sw04-p4  (23 entries, util 10.9200 %)

```
sgs 18240 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 26880 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 26880 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 40640 0x7F # 01111111   Q6
sgs 16000 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 21440 0xBF # 10111111   Q7
sgs 18240 0x7F # 01111111   Q6
sgs 120960 0x40 # 01000000   Q6
sgs 60800 0xBF # 10111111   Q7
sgs 18240 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 19200 0x7F # 01111111   Q6
sgs 47040 0xBF # 10111111   Q7
sgs 42240 0x80 # 10000000   Q7
sgs 60800 0xBF # 10111111   Q7
sgs 18240 0x7F # 01111111   Q6
sgs 102720 0x40 # 01000000   Q6
sgs 29120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (32 entries, util 12.4800 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 5120 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 2240 0x3F # 00111111   BE
sgs 67840 0x40 # 01000000   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 17600 0x80 # 10000000   Q7
sgs 15680 0x7F # 01111111   Q6
sgs 34240 0xBF # 10111111   Q7
sgs 82560 0x80 # 10000000   Q7
sgs 33280 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 5120 0x3F # 00111111   BE
sgs 82560 0x80 # 10000000   Q7
sgs 33280 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 17600 0x80 # 10000000   Q7
sgs 15680 0x7F # 01111111   Q6
sgs 34240 0xBF # 10111111   Q7
sgs 65920 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (18 entries, util 17.1600 %)

```
sgs 30720 0x7F # 01111111   Q6
sgs 51840 0x80 # 10000000   Q7
sgs 7680 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 15360 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 2880 0x3F # 00111111   BE
sgs 50240 0x40 # 01000000   Q6
sgs 16320 0xBF # 10111111   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 152960 0x80 # 10000000   Q7
sgs 16320 0xBF # 10111111   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 152960 0x80 # 10000000   Q7
sgs 16320 0xBF # 10111111   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 122240 0x80 # 10000000   Q7
sgs 47040 0xBF # 10111111   Q7
```

### sw05-p5  (21 entries, util 1.5600 %)

```
sgs 37440 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 25920 0x7F # 01111111   Q6
sgs 100160 0x40 # 01000000   Q6
sgs 24000 0x7F # 01111111   Q6
sgs 54720 0xBF # 10111111   Q7
sgs 54080 0x80 # 10000000   Q7
sgs 41280 0xBF # 10111111   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 42240 0xBF # 10111111   Q7
sgs 121280 0x80 # 10000000   Q7
sgs 24000 0x7F # 01111111   Q6
sgs 54720 0xBF # 10111111   Q7
sgs 16640 0x80 # 10000000   Q7
sgs 28800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p4  (30 entries, util 12.4800 %)

```
sgs 24960 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 1920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 3840 0x3F # 00111111   BE
sgs 69440 0x40 # 01000000   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 14400 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
sgs 85760 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 1920 0x3F # 00111111   BE
sgs 85760 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 14400 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
sgs 60800 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (21 entries, util 10.9200 %)

```
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 26240 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 26880 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 55680 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 41280 0xBF # 10111111   Q7
sgs 120960 0x40 # 01000000   Q6
sgs 16960 0x7F # 01111111   Q6
sgs 62080 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 25280 0x7F # 01111111   Q6
sgs 40320 0xBF # 10111111   Q7
sgs 42880 0x80 # 10000000   Q7
sgs 16960 0x7F # 01111111   Q6
sgs 62080 0xBF # 10111111   Q7
sgs 108800 0x40 # 01000000   Q6
sgs 29120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (23 entries, util 1.5600 %)

```
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 24320 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 27520 0x7F # 01111111   Q6
sgs 101760 0x40 # 01000000   Q6
sgs 29120 0x7F # 01111111   Q6
sgs 49600 0xBF # 10111111   Q7
sgs 50880 0x80 # 10000000   Q7
sgs 49600 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 44800 0xBF # 10111111   Q7
sgs 121280 0x80 # 10000000   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 49600 0xBF # 10111111   Q7
sgs 21760 0x80 # 10000000   Q7
sgs 28800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p5  (15 entries, util 17.1600 %)

```
sgs 38400 0x7F # 01111111   Q6
sgs 50880 0x80 # 10000000   Q7
sgs 6080 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 18560 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 2240 0x3F # 00111111   BE
sgs 50240 0x40 # 01000000   Q6
sgs 47040 0x7F # 01111111   Q6
sgs 152960 0x80 # 10000000   Q7
sgs 47040 0x7F # 01111111   Q6
sgs 152960 0x80 # 10000000   Q7
sgs 47040 0x7F # 01111111   Q6
sgs 114560 0x80 # 10000000   Q7
sgs 47040 0xBF # 10111111   Q7
```

### sw08-p2  (25 entries, util 26.5200 %)

```
sgs 33280 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 28480 0x40 # 01000000   Q6
sgs 120320 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 13120 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 149120 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 136320 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 13120 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 115840 0x3F # 00111111   BE
```

### sw08-p4  (21 entries, util 10.9200 %)

```
sgs 6080 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 25600 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 26880 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 54720 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 42880 0xBF # 10111111   Q7
sgs 120960 0x40 # 01000000   Q6
sgs 23040 0x7F # 01111111   Q6
sgs 56000 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 31360 0x7F # 01111111   Q6
sgs 33600 0xBF # 10111111   Q7
sgs 43520 0x80 # 10000000   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 56000 0xBF # 10111111   Q7
sgs 114880 0x40 # 01000000   Q6
sgs 29120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (23 entries, util 1.5600 %)

```
sgs 20800 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 24640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 29120 0xBF # 10111111   Q7
sgs 103360 0x40 # 01000000   Q6
sgs 34240 0x7F # 01111111   Q6
sgs 44480 0xBF # 10111111   Q7
sgs 47680 0x80 # 10000000   Q7
sgs 57920 0xBF # 10111111   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 48320 0xBF # 10111111   Q7
sgs 121280 0x80 # 10000000   Q7
sgs 34240 0x7F # 01111111   Q6
sgs 44480 0xBF # 10111111   Q7
sgs 26880 0x80 # 10000000   Q7
sgs 28800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

