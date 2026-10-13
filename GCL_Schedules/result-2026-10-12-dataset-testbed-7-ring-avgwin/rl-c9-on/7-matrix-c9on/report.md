# RL-enlarged GCL schedule (Problem 2: window enlargement)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Seeded from SMT run: **result/result-2026-10-12-dataset-testbed-7-ring-avgwin/smt-c9-on/7-fair-retimed-c9on**

## Admission (unchanged) vs. capacity grown

Problem 2 never admits a flow into the schedule it exports -- it only widens windows. `admitted` below is exactly the SMT baseline, by construction; the capacity growth this run achieved is banked slack and per-port GCL entries, reported separately.

| | admitted | of total |
|---|---|---|
| SMT (fixed, never moved) | 11 | 11 |
| RL-enlarged (exported; grow-only, admits nothing new) | 11 | 20 |

During training, the policy's trial admissions (the reward signal that teaches it how much a window needs to grow) reached **8** of the 9 SMT-rejected flows -- none of those are kept in this export; that capacity stays as empty, banked slack for Problem 3 to fill. Total slack banked: 513280 ns. GCL_size overflow: 0.

## Opportunistic idle top-up (deterministic post-pass)

**13545280 ns**, drawn from idle capacity on ports at or below utilisation 0.2, independent of what training happened to grow. Ported from prob_2_heuristic_enlarged's Step 7.

| port | queue | applied (ns) |
|---|---|---|
| S1-p0 | Q6 | 225280 |
| S1-p0 | Q7 | 350080 |
| S2-p0 | Q6 | 350080 |
| S2-p0 | Q7 | 375040 |
| S3-p0 | Q6 | 550400 |
| sw01-p2 | Q6 | 111680 |
| sw01-p2 | Q7 | 489920 |
| sw01-p4 | Q6 | 110080 |
| sw01-p4 | Q7 | 517760 |
| sw01-p5 | Q6 | 14720 |
| sw01-p5 | Q7 | 655360 |
| sw02-p2 | Q6 | 22080 |
| sw02-p2 | Q7 | 630400 |
| sw02-p4 | Q6 | 579200 |
| sw02-p4 | Q7 | 64960 |
| sw02-p5 | Q6 | 137280 |
| sw02-p5 | Q7 | 526080 |
| sw03-p4 | Q6 | 300800 |
| sw03-p4 | Q7 | 312000 |
| sw03-p5 | Q6 | 103040 |
| sw03-p5 | Q7 | 502400 |
| sw04-p4 | Q6 | 737600 |
| sw04-p5 | Q6 | 570560 |
| sw04-p5 | Q7 | 67520 |
| sw05-p4 | Q6 | 96000 |
| sw05-p4 | Q7 | 487040 |
| sw05-p5 | Q6 | 302080 |
| sw05-p5 | Q7 | 320320 |
| sw06-p4 | Q6 | 554240 |
| sw06-p4 | Q7 | 77760 |
| sw06-p5 | Q6 | 745920 |
| sw07-p4 | Q6 | 303360 |
| sw07-p4 | Q7 | 328640 |
| sw07-p5 | Q6 | 356480 |
| sw07-p5 | Q7 | 273280 |
| sw08-p4 | Q6 | 754240 |
| sw08-p5 | Q6 | 304640 |
| sw08-p5 | Q7 | 336960 |

## Opportunistic exclusive window creation (deterministic post-pass)

**3** brand-new *exclusive* window(s) opened, **37440 ns** total, on ports at or below utilisation 0.2 whose TT queue had zero windows before this run. Ported from prob_2_heuristic_enlarged's Step 8.

| port | queue | size (ns) |
|---|---|---|
| sw04-p4 | Q7 | 12480 |
| sw06-p5 | Q7 | 12480 |
| sw08-p4 | Q7 | 12480 |

## Best-effort gap equalization (deterministic post-pass)

**8175040 ns** given back from the top-up/creation above so each port's leftover non-TAS gaps land close to equal. Ported from prob_2_heuristic_enlarged's Step 9.

| port | given back (ns) |
|---|---|---|
| sw02-p5 | 541760 |
| sw07-p5 | 515840 |
| sw05-p4 | 505600 |
| sw03-p5 | 495360 |
| sw01-p4 | 485120 |
| sw01-p2 | 465280 |
| sw03-p4 | 461440 |
| sw05-p5 | 460160 |
| sw07-p4 | 458880 |
| sw08-p5 | 457600 |
| S2-p0 | 393280 |
| sw01-p5 | 371200 |
| sw02-p2 | 344640 |
| sw06-p4 | 309120 |
| sw04-p5 | 303360 |
| sw02-p4 | 301440 |
| S3-p0 | 299520 |
| sw04-p4 | 262400 |
| sw06-p5 | 262400 |
| sw08-p4 | 262400 |
| S1-p0 | 205760 |
| sw08-p2 | 12480 |

## Opportunistic overlay window creation (deterministic post-pass)

**42** new overlay window(s), **8448960 ns** total, carved out of already-open best-effort spans on ports at or below utilisation 0.2 -- best-effort stays reachable inside each one (gate mask keeps its BE bits set). Run once after training/finalize_grow_only(), not a trained action.

| port | queue | size (ns) |
|---|---|---|
| S1-p0 | Q6 | 49920 |
| S1-p0 | Q7 | 155840 |
| S2-p0 | Q6 | 192960 |
| S2-p0 | Q7 | 200320 |
| S3-p0 | Q6 | 74880 |
| S3-p0 | Q7 | 224640 |
| sw01-p2 | Q6 | 268480 |
| sw01-p2 | Q7 | 238080 |
| sw01-p4 | Q6 | 153600 |
| sw01-p4 | Q7 | 361600 |
| sw01-p5 | Q6 | 94720 |
| sw01-p5 | Q7 | 240000 |
| sw02-p2 | Q6 | 62720 |
| sw02-p2 | Q7 | 250240 |
| sw02-p4 | Q6 | 64960 |
| sw02-p4 | Q7 | 224640 |
| sw02-p5 | Q6 | 345280 |
| sw02-p5 | Q7 | 232960 |
| sw03-p4 | Q6 | 229760 |
| sw03-p4 | Q7 | 264960 |
| sw03-p5 | Q6 | 174080 |
| sw03-p5 | Q7 | 356480 |
| sw04-p4 | Q6 | 149760 |
| sw04-p4 | Q7 | 150080 |
| sw04-p5 | Q6 | 67520 |
| sw04-p5 | Q7 | 224640 |
| sw05-p4 | Q6 | 194560 |
| sw05-p4 | Q7 | 351360 |
| sw05-p5 | Q6 | 224320 |
| sw05-p5 | Q7 | 260800 |
| sw06-p4 | Q6 | 150720 |
| sw06-p4 | Q7 | 144960 |
| sw06-p5 | Q6 | 141440 |
| sw06-p5 | Q7 | 150080 |
| sw07-p4 | Q6 | 224320 |
| sw07-p4 | Q7 | 251200 |
| sw07-p5 | Q6 | 260160 |
| sw07-p5 | Q7 | 301120 |
| sw08-p4 | Q6 | 133120 |
| sw08-p4 | Q7 | 150080 |
| sw08-p5 | Q6 | 207680 |
| sw08-p5 | Q7 | 249920 |

## Per-port GCL entries: before (SMT) vs. after (RL-enlarged)

| port | SMT entries | RL-enlarged entries | GCL_size |
|---|---|---|---|
| sw01-p2 | 5 | 23 | 255 |
| sw01-p4 | 9 | 21 | 255 |
| sw01-p5 | 17 | 22 | 255 |
| sw02-p2 | 19 | 24 | 255 |
| sw02-p4 | 25 | 25 | 255 |
| sw02-p5 | 1 | 19 | 255 |
| sw03-p4 | 5 | 14 | 255 |
| sw03-p5 | 9 | 21 | 255 |
| sw04-p4 | 3 | 9 | 255 |
| sw04-p5 | 25 | 25 | 255 |
| sw05-p4 | 9 | 21 | 255 |
| sw05-p5 | 5 | 15 | 255 |
| sw06-p4 | 25 | 24 | 255 |
| sw06-p5 | 3 | 9 | 255 |
| sw07-p4 | 5 | 15 | 255 |
| sw07-p5 | 9 | 25 | 255 |
| sw08-p2 | 33 | 29 | 255 |
| sw08-p4 | 3 | 9 | 255 |
| sw08-p5 | 5 | 14 | 255 |

## Flows

| flow | route | fixed | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|---|
| s0(id=1 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | yes | 7 | 0 | 36880 | yes |
| s1(id=2 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | no | None | None | None | no |
| s2(id=3 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | yes | 7 | 0 | 54160 | yes |
| s3(id=4 S1->S3) | S1->sw02->sw01->S3 | no | None | None | None | no |
| s4(id=5 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | yes | 7 | 74880 | 36880 | yes |
| s5(id=6 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | no | None | None | None | no |
| s6(id=7 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | yes | 6 | 24960 | 45840 | yes |
| s7(id=8 S3->S1) | S3->sw01->sw02->S1 | yes | 7 | 49920 | 33680 | yes |
| s8(id=9 S3->S1) | S3->sw01->sw02->S1 | yes | 7 | 0 | 22800 | yes |
| s9(id=10 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | no | None | None | None | no |
| s10(id=11 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |
| s11(id=12 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | yes | 6 | 24960 | 50960 | yes |
| s12(id=13 S1->S3) | S1->sw02->sw01->S3 | no | None | None | None | no |
| s13(id=14 S3->S1) | S3->sw01->sw02->S1 | no | None | None | None | no |
| s14(id=15 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | yes | 6 | 49920 | 39440 | yes |
| s15(id=16 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |
| s16(id=17 S1->S3) | S1->sw02->sw01->S3 | no | None | None | None | no |
| s17(id=18 S3->S1) | S3->sw01->sw02->S1 | yes | 6 | 74880 | 26000 | yes |
| s18(id=19 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | yes | 6 | 99840 | 36880 | yes |
| s19(id=20 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | yes | 6 | 24960 | 38160 | yes |

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

## Metrics (training/evaluation signal, not the export)

| metric | value |
|---|---|
| trial-placed flow ratio (fixed + trial-admitted) | 0.950 |
| r1  same-queue window adjacency | 0.242 |
| r2  deadline-violation ratio | 0.000 |
| r3  supplier/receiver overlap | 0.991 |
| r4  mean e2e/deadline (admitted) | 0.156 |
| constraint violations | 0 |

## Constraint check

- C1-C7, C9: OK
- seed-integrity (no SMT-fixed flow's placement changed): OK

## GCL per egress port

### sw01-p2  (23 entries, util 3.1200 %)

```
sgs 41600 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 18560 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 15040 0xBF # 10111111   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 34560 0x40 # 01000000   Q6
sgs 32000 0xBF # 10111111   Q7
sgs 54080 0x7F # 01111111   Q6
sgs 101440 0x80 # 10000000   Q7
sgs 44480 0xBF # 10111111   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 46080 0xBF # 10111111   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 47360 0x80 # 10000000   Q7
sgs 32000 0xBF # 10111111   Q7
sgs 54080 0x7F # 01111111   Q6
sgs 59840 0x80 # 10000000   Q7
sgs 36160 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p4  (21 entries, util 6.2400 %)

```
sgs 30080 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 38080 0xBF # 10111111   Q7
sgs 66240 0x80 # 10000000   Q7
sgs 53120 0xBF # 10111111   Q7
sgs 30080 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 38080 0xBF # 10111111   Q7
sgs 66240 0x80 # 10000000   Q7
sgs 53120 0xBF # 10111111   Q7
sgs 30080 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 38080 0xBF # 10111111   Q7
sgs 66240 0x80 # 10000000   Q7
sgs 53120 0xBF # 10111111   Q7
sgs 30080 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 38080 0xBF # 10111111   Q7
sgs 36160 0x80 # 10000000   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p5  (22 entries, util 12.4800 %)

```
sgs 5120 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 40640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 10880 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 7360 0x3F # 00111111   BE
sgs 40320 0x80 # 10000000   Q7
sgs 63360 0xBF # 10111111   Q7
sgs 136640 0x80 # 10000000   Q7
sgs 63360 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 40640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 10880 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 7360 0x3F # 00111111   BE
sgs 40320 0x80 # 10000000   Q7
sgs 63360 0xBF # 10111111   Q7
sgs 131520 0x80 # 10000000   Q7
sgs 13440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (24 entries, util 14.0400 %)

```
sgs 10240 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 35520 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 4800 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 10880 0x3F # 00111111   BE
sgs 41280 0x80 # 10000000   Q7
sgs 57280 0xBF # 10111111   Q7
sgs 142720 0x80 # 10000000   Q7
sgs 57280 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 27200 0x7F # 01111111   Q6
sgs 21120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 4800 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 10880 0x3F # 00111111   BE
sgs 41280 0x80 # 10000000   Q7
sgs 57280 0xBF # 10111111   Q7
sgs 132480 0x80 # 10000000   Q7
sgs 57280 0xBF # 10111111   Q7
```

### sw02-p4  (25 entries, util 18.7200 %)

```
sgs 6080 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 11840 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 50240 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0x7F # 01111111   Q6
sgs 124480 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 99520 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0x7F # 01111111   Q6
sgs 118400 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p5  (19 entries, util 0.0000 %)

```
sgs 45760 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 9280 0x3F # 00111111   BE
sgs 45120 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 45760 0x7F # 01111111   Q6
sgs 66880 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 45760 0x7F # 01111111   Q6
sgs 66880 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 45760 0x7F # 01111111   Q6
sgs 21120 0x80 # 10000000   Q7
sgs 33280 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (14 entries, util 3.1200 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 54400 0xBF # 10111111   Q7
sgs 19840 0x7F # 01111111   Q6
sgs 119680 0x40 # 01000000   Q6
sgs 60480 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 173120 0x80 # 10000000   Q7
sgs 43520 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p5  (21 entries, util 6.2400 %)

```
sgs 35200 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 40640 0xBF # 10111111   Q7
sgs 63680 0x80 # 10000000   Q7
sgs 48000 0xBF # 10111111   Q7
sgs 35200 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 40640 0xBF # 10111111   Q7
sgs 63680 0x80 # 10000000   Q7
sgs 48000 0xBF # 10111111   Q7
sgs 35200 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 40640 0xBF # 10111111   Q7
sgs 63680 0x80 # 10000000   Q7
sgs 48000 0xBF # 10111111   Q7
sgs 35200 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 40640 0xBF # 10111111   Q7
sgs 28480 0x80 # 10000000   Q7
sgs 33280 0x7F # 01111111   Q6
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

### sw04-p5  (25 entries, util 18.7200 %)

```
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13760 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 50240 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 13760 0x7F # 01111111   Q6
sgs 123840 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 13760 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 98880 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 13760 0x7F # 01111111   Q6
sgs 111680 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (21 entries, util 6.2400 %)

```
sgs 40320 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 43200 0xBF # 10111111   Q7
sgs 61120 0x80 # 10000000   Q7
sgs 42880 0xBF # 10111111   Q7
sgs 40320 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 43200 0xBF # 10111111   Q7
sgs 61120 0x80 # 10000000   Q7
sgs 42880 0xBF # 10111111   Q7
sgs 40320 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 43200 0xBF # 10111111   Q7
sgs 61120 0x80 # 10000000   Q7
sgs 42880 0xBF # 10111111   Q7
sgs 40320 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 43200 0xBF # 10111111   Q7
sgs 20800 0x80 # 10000000   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p5  (15 entries, util 3.1200 %)

```
sgs 24960 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 60480 0xBF # 10111111   Q7
sgs 120960 0x40 # 01000000   Q6
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

### sw07-p4  (15 entries, util 3.1200 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 50880 0xBF # 10111111   Q7
sgs 122240 0x40 # 01000000   Q6
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

### sw07-p5  (25 entries, util 6.2400 %)

```
sgs 45440 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 45760 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 30080 0x7F # 01111111   Q6
sgs 31040 0x40 # 01000000   Q6
sgs 22720 0xBF # 10111111   Q7
sgs 45440 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 45760 0xBF # 10111111   Q7
sgs 73600 0x80 # 10000000   Q7
sgs 22720 0xBF # 10111111   Q7
sgs 45440 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 45760 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 30080 0x7F # 01111111   Q6
sgs 31040 0x40 # 01000000   Q6
sgs 22720 0xBF # 10111111   Q7
sgs 45440 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 45760 0xBF # 10111111   Q7
sgs 28160 0x80 # 10000000   Q7
sgs 18240 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p2  (29 entries, util 24.9600 %)

```
sgs 24320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13760 0x3F # 00111111   BE
sgs 38720 0x40 # 01000000   Q6
sgs 9920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 40640 0x40 # 01000000   Q6
sgs 59520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13760 0x3F # 00111111   BE
sgs 25280 0x40 # 01000000   Q6
sgs 35840 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 100160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13760 0x3F # 00111111   BE
sgs 38720 0x40 # 01000000   Q6
sgs 22400 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 28160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 59520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13760 0x3F # 00111111   BE
sgs 25280 0x40 # 01000000   Q6
sgs 35840 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 75840 0x3F # 00111111   BE
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

### sw08-p5  (14 entries, util 3.1200 %)

```
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 41280 0xBF # 10111111   Q7
sgs 123520 0x40 # 01000000   Q6
sgs 35200 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 58240 0xBF # 10111111   Q7
sgs 198080 0x80 # 10000000   Q7
sgs 43520 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

