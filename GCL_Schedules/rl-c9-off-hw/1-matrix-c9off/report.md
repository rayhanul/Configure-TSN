# RL-enlarged GCL schedule (Problem 2: window enlargement)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4000 ns
- Seeded from SMT run: **result/result-dataset-testbed-hw/smt-c9-off/1-t3600-c9off-minlat**

## Admission (unchanged) vs. capacity grown

Problem 2 never admits a flow into the schedule it exports -- it only widens windows. `admitted` below is exactly the SMT baseline, by construction; the capacity growth this run achieved is banked slack and per-port GCL entries, reported separately.

| | admitted | of total |
|---|---|---|
| SMT (fixed, never moved) | 10 | 20 |
| RL-enlarged (exported; grow-only, admits nothing new) | 10 | 20 |

During training, the policy's trial admissions (the reward signal that teaches it how much a window needs to grow) reached **9** of the 10 SMT-rejected flows -- none of those are kept in this export; that capacity stays as empty, banked slack for Problem 3 to fill. Total slack banked: 29440 ns. GCL_size overflow: 0.

## Opportunistic idle top-up (deterministic post-pass)

**15059840 ns**, drawn from idle capacity on ports at or below utilisation 0.2, independent of what training happened to grow. Ported from prob_2_heuristic_enlarged's Step 7.

| port | queue | applied (ns) |
|---|---|---|
| S1-p0 | Q6 | 394880 |
| S1-p0 | Q7 | 384640 |
| S2-p0 | Q6 | 192960 |
| S2-p0 | Q7 | 570560 |
| S3-p0 | Q6 | 177280 |
| S3-p0 | Q7 | 541120 |
| sw01-p3 | Q6 | 357440 |
| sw01-p3 | Q7 | 406720 |
| sw01-p4 | Q6 | 197120 |
| sw01-p4 | Q7 | 545600 |
| sw01-p5 | Q6 | 354560 |
| sw01-p5 | Q7 | 401920 |
| sw02-p2 | Q6 | 5760 |
| sw02-p2 | Q7 | 697600 |
| sw02-p3 | Q7 | 783040 |
| sw02-p5 | Q6 | 388160 |
| sw02-p5 | Q7 | 389760 |
| sw03-p3 | Q6 | 365120 |
| sw03-p3 | Q7 | 391040 |
| sw03-p4 | Q6 | 201920 |
| sw03-p4 | Q7 | 534080 |
| sw05-p2 | Q6 | 381440 |
| sw05-p2 | Q7 | 389760 |
| sw05-p5 | Q6 | 4480 |
| sw05-p5 | Q7 | 747520 |
| sw06-p2 | Q6 | 208320 |
| sw06-p2 | Q7 | 520640 |
| sw06-p3 | Q6 | 373120 |
| sw06-p3 | Q7 | 390720 |
| sw07-p3 | Q6 | 2560 |
| sw07-p3 | Q7 | 756160 |
| sw07-p4 | Q6 | 374720 |
| sw07-p4 | Q7 | 389760 |
| sw08-p2 | Q6 | 197760 |
| sw08-p2 | Q7 | 504640 |
| sw08-p4 | Q6 | 381760 |
| sw08-p4 | Q7 | 389760 |
| sw08-p5 | Q6 | 640 |
| sw08-p5 | Q7 | 764800 |

## Opportunistic exclusive window creation (deterministic post-pass)

**20** brand-new *exclusive* window(s) opened, **729600 ns** total, on ports at or below utilisation 0.2 whose TT queue had zero windows before this run. Ported from prob_2_heuristic_enlarged's Step 8.

| port | queue | size (ns) |
|---|---|---|
| sw02-p4 | Q6 | 36480 |
| sw02-p4 | Q7 | 36480 |
| sw03-p5 | Q6 | 36480 |
| sw03-p5 | Q7 | 36480 |
| sw04-p3 | Q6 | 36480 |
| sw04-p3 | Q7 | 36480 |
| sw04-p4 | Q6 | 36480 |
| sw04-p4 | Q7 | 36480 |
| sw04-p5 | Q6 | 36480 |
| sw04-p5 | Q7 | 36480 |
| sw05-p3 | Q6 | 36480 |
| sw05-p3 | Q7 | 36480 |
| sw05-p4 | Q6 | 36480 |
| sw05-p4 | Q7 | 36480 |
| sw06-p4 | Q6 | 36480 |
| sw06-p4 | Q7 | 36480 |
| sw06-p5 | Q6 | 36480 |
| sw06-p5 | Q7 | 36480 |
| sw07-p5 | Q6 | 36480 |
| sw07-p5 | Q7 | 36480 |

## Best-effort gap equalization (deterministic post-pass)

**5808000 ns** given back from the top-up/creation above so each port's leftover non-TAS gaps land close to equal. Ported from prob_2_heuristic_enlarged's Step 9.

| port | given back (ns) |
|---|---|---|
| sw02-p5 | 450560 |
| sw05-p2 | 450560 |
| sw07-p4 | 450560 |
| sw05-p5 | 353280 |
| sw07-p3 | 353280 |
| sw08-p5 | 353280 |
| S1-p0 | 349440 |
| sw03-p3 | 314880 |
| sw06-p3 | 314880 |
| sw08-p4 | 314880 |
| S2-p0 | 284160 |
| sw01-p5 | 277760 |
| sw02-p3 | 265600 |
| sw01-p3 | 224000 |
| sw01-p4 | 195840 |
| sw03-p4 | 195840 |
| sw06-p2 | 195840 |
| sw02-p2 | 177920 |
| sw08-p2 | 171520 |
| S3-p0 | 113920 |

## Opportunistic overlay window creation (deterministic post-pass)

**59** new overlay window(s), **13366400 ns** total, carved out of already-open best-effort spans on ports at or below utilisation 0.2 -- best-effort stays reachable inside each one (gate mask keeps its BE bits set). Run once after training/finalize_grow_only(), not a trained action.

| port | queue | size (ns) |
|---|---|---|
| S1-p0 | Q6 | 149760 |
| S1-p0 | Q7 | 198720 |
| S2-p0 | Q6 | 84480 |
| S2-p0 | Q7 | 199680 |
| S3-p0 | Q7 | 113920 |
| sw01-p3 | Q6 | 129600 |
| sw01-p3 | Q7 | 112000 |
| sw01-p4 | Q6 | 43520 |
| sw01-p4 | Q7 | 163200 |
| sw01-p5 | Q6 | 86400 |
| sw01-p5 | Q7 | 199680 |
| sw02-p2 | Q6 | 66560 |
| sw02-p2 | Q7 | 128000 |
| sw02-p3 | Q6 | 126400 |
| sw02-p3 | Q7 | 150080 |
| sw02-p4 | Q6 | 349440 |
| sw02-p4 | Q7 | 377600 |
| sw02-p5 | Q6 | 224640 |
| sw02-p5 | Q7 | 230720 |
| sw03-p3 | Q6 | 170560 |
| sw03-p3 | Q7 | 176000 |
| sw03-p4 | Q6 | 70400 |
| sw03-p4 | Q7 | 143040 |
| sw03-p5 | Q6 | 349440 |
| sw03-p5 | Q7 | 377600 |
| sw04-p3 | Q6 | 349440 |
| sw04-p3 | Q7 | 377600 |
| sw04-p4 | Q6 | 349440 |
| sw04-p4 | Q7 | 377600 |
| sw04-p5 | Q6 | 349440 |
| sw04-p5 | Q7 | 377600 |
| sw05-p2 | Q6 | 249600 |
| sw05-p2 | Q7 | 212480 |
| sw05-p3 | Q6 | 349440 |
| sw05-p3 | Q7 | 377600 |
| sw05-p4 | Q6 | 349440 |
| sw05-p4 | Q7 | 377600 |
| sw05-p5 | Q6 | 177280 |
| sw05-p5 | Q7 | 199680 |
| sw06-p2 | Q6 | 98560 |
| sw06-p2 | Q7 | 121920 |
| sw06-p3 | Q6 | 155200 |
| sw06-p3 | Q7 | 183680 |
| sw06-p4 | Q6 | 349440 |
| sw06-p4 | Q7 | 377600 |
| sw06-p5 | Q6 | 349440 |
| sw06-p5 | Q7 | 377600 |
| sw07-p3 | Q6 | 170560 |
| sw07-p3 | Q7 | 199680 |
| sw07-p4 | Q6 | 256320 |
| sw07-p4 | Q7 | 212480 |
| sw07-p5 | Q6 | 349440 |
| sw07-p5 | Q7 | 377600 |
| sw08-p2 | Q6 | 107520 |
| sw08-p2 | Q7 | 90880 |
| sw08-p4 | Q6 | 139840 |
| sw08-p4 | Q7 | 191360 |
| sw08-p5 | Q6 | 161920 |
| sw08-p5 | Q7 | 199680 |

## Per-port GCL entries: before (SMT) vs. after (RL-enlarged)

| port | SMT entries | RL-enlarged entries | GCL_size |
|---|---|---|---|
| sw01-p3 | 11 | 12 | 255 |
| sw01-p4 | 9 | 19 | 255 |
| sw01-p5 | 21 | 18 | 255 |
| sw02-p2 | 25 | 18 | 255 |
| sw02-p3 | 3 | 9 | 255 |
| sw02-p4 | 1 | 17 | 255 |
| sw02-p5 | 9 | 22 | 255 |
| sw03-p3 | 9 | 12 | 255 |
| sw03-p4 | 9 | 19 | 255 |
| sw03-p5 | 1 | 17 | 255 |
| sw04-p3 | 1 | 17 | 255 |
| sw04-p4 | 1 | 17 | 255 |
| sw04-p5 | 1 | 17 | 255 |
| sw05-p2 | 9 | 19 | 255 |
| sw05-p3 | 1 | 17 | 255 |
| sw05-p4 | 1 | 17 | 255 |
| sw05-p5 | 5 | 20 | 255 |
| sw06-p2 | 9 | 19 | 255 |
| sw06-p3 | 9 | 12 | 255 |
| sw06-p4 | 1 | 17 | 255 |
| sw06-p5 | 1 | 17 | 255 |
| sw07-p3 | 5 | 20 | 255 |
| sw07-p4 | 9 | 19 | 255 |
| sw07-p5 | 1 | 17 | 255 |
| sw08-p2 | 17 | 23 | 255 |
| sw08-p4 | 9 | 12 | 255 |
| sw08-p5 | 5 | 20 | 255 |

## Flows

| flow | route | fixed | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|---|
| s0(id=1 S3->S1) | S3->sw01->sw02->S1 | yes | 7 | 0 | 20800 | yes |
| s1(id=2 S2->S1) | S2->sw08->sw07->sw05->sw02->S1 | no | None | None | None | no |
| s2(id=3 S3->S2) | S3->sw01->sw03->sw06->sw08->S2 | no | None | None | None | no |
| s3(id=4 S1->S3) | S1->sw02->sw01->S3 | yes | 6 | 5120 | 16000 | yes |
| s4(id=5 S2->S1) | S2->sw08->sw07->sw05->sw02->S1 | yes | 6 | 3520 | 29440 | yes |
| s5(id=6 S2->S1) | S2->sw08->sw07->sw05->sw02->S1 | no | None | None | None | no |
| s6(id=7 S2->S1) | S2->sw08->sw07->sw05->sw02->S1 | no | None | None | None | no |
| s7(id=8 S2->S3) | S2->sw08->sw06->sw03->sw01->S3 | yes | 7 | 14720 | 31040 | yes |
| s8(id=9 S3->S2) | S3->sw01->sw03->sw06->sw08->S2 | yes | 6 | 6720 | 37440 | yes |
| s9(id=10 S1->S3) | S1->sw02->sw01->S3 | no | None | None | None | no |
| s10(id=11 S3->S2) | S3->sw01->sw03->sw06->sw08->S2 | no | None | None | None | no |
| s11(id=12 S2->S1) | S2->sw08->sw07->sw05->sw02->S1 | no | None | None | None | no |
| s12(id=13 S1->S2) | S1->sw02->sw05->sw07->sw08->S2 | no | None | None | None | no |
| s13(id=14 S1->S2) | S1->sw02->sw05->sw07->sw08->S2 | yes | 6 | 0 | 29440 | yes |
| s14(id=15 S2->S3) | S2->sw08->sw06->sw03->sw01->S3 | yes | 6 | 8640 | 34240 | yes |
| s15(id=16 S3->S2) | S3->sw01->sw03->sw06->sw08->S2 | no | None | None | None | no |
| s16(id=17 S2->S3) | S2->sw08->sw06->sw03->sw01->S3 | yes | 7 | 19840 | 29440 | yes |
| s17(id=18 S3->S2) | S3->sw01->sw03->sw06->sw08->S2 | no | None | None | None | no |
| s18(id=19 S3->S1) | S3->sw01->sw02->S1 | yes | 6 | 18560 | 20800 | yes |
| s19(id=20 S3->S1) | S3->sw01->sw02->S1 | yes | 7 | 13440 | 16000 | yes |

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

## Metrics (training/evaluation signal, not the export)

| metric | value |
|---|---|
| trial-placed flow ratio (fixed + trial-admitted) | 0.950 |
| r1  same-queue window adjacency | 0.338 |
| r2  deadline-violation ratio | 0.000 |
| r3  supplier/receiver overlap | 0.998 |
| r4  mean e2e/deadline (admitted) | 0.089 |
| constraint violations | 0 |

## Constraint check

- FAIL MINWIN S1-p0: TAS window at 0 ns is 2560 ns < 3243.4951456310678 ns
- FAIL MINWIN S1-p0: TAS window at 2560 ns is 2560 ns < 3243.4951456310678 ns

## GCL per egress port

### sw01-p3  (12 entries, util 1.8400 %)

```
sgs 17600 0x7F # 01111111   Q6
sgs 3520 0x40 # 01000000   Q6
sgs 18240 0x80 # 10000000   Q7
sgs 3840 0x40 # 01000000   Q6
sgs 284160 0x80 # 10000000   Q7
sgs 22720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 39360 0x7F # 01111111   Q6
sgs 248640 0x40 # 01000000   Q6
sgs 12160 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p4  (19 entries, util 2.0800 %)

```
sgs 10880 0x7F # 01111111   Q6
sgs 8640 0x40 # 01000000   Q6
sgs 4160 0x80 # 10000000   Q7
sgs 7360 0x40 # 01000000   Q6
sgs 130880 0x80 # 10000000   Q7
sgs 38080 0xBF # 10111111   Q7
sgs 10880 0x7F # 01111111   Q6
sgs 8640 0x40 # 01000000   Q6
sgs 142400 0x80 # 10000000   Q7
sgs 38080 0xBF # 10111111   Q7
sgs 10880 0x7F # 01111111   Q6
sgs 8640 0x40 # 01000000   Q6
sgs 4160 0x80 # 10000000   Q7
sgs 138240 0x40 # 01000000   Q6
sgs 38080 0xBF # 10111111   Q7
sgs 10880 0x7F # 01111111   Q6
sgs 8640 0x40 # 01000000   Q6
sgs 131520 0x80 # 10000000   Q7
sgs 48960 0xBF # 10111111   Q7
```

### sw01-p5  (18 entries, util 4.4000 %)

```
sgs 8320 0x7F # 01111111   Q6
sgs 18560 0x80 # 10000000   Q7
sgs 112000 0x40 # 01000000   Q6
sgs 11200 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 8320 0x7F # 01111111   Q6
sgs 130560 0x80 # 10000000   Q7
sgs 11200 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 8320 0x7F # 01111111   Q6
sgs 18560 0x80 # 10000000   Q7
sgs 112000 0x40 # 01000000   Q6
sgs 11200 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 8320 0x7F # 01111111   Q6
sgs 122240 0x80 # 10000000   Q7
sgs 19520 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (18 entries, util 5.0400 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 13760 0x80 # 10000000   Q7
sgs 9280 0x40 # 01000000   Q6
sgs 5120 0x80 # 10000000   Q7
sgs 3520 0x40 # 01000000   Q6
sgs 123840 0x80 # 10000000   Q7
sgs 27840 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 155520 0x80 # 10000000   Q7
sgs 27840 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 13760 0x80 # 10000000   Q7
sgs 9280 0x40 # 01000000   Q6
sgs 132480 0x80 # 10000000   Q7
sgs 27840 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 138880 0x80 # 10000000   Q7
sgs 44480 0xBF # 10111111   Q7
```

### sw02-p3  (9 entries, util 0.3200 %)

```
sgs 10880 0x7F # 01111111   Q6
sgs 3520 0x40 # 01000000   Q6
sgs 520000 0x80 # 10000000   Q7
sgs 15680 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p4  (17 entries, util 0.0000 %)

```
sgs 36480 0x40 # 01000000   Q6
sgs 36480 0x80 # 10000000   Q7
sgs 27200 0xBF # 10111111   Q7
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

### sw02-p5  (22 entries, util 1.2800 %)

```
sgs 5760 0x7F # 01111111   Q6
sgs 3520 0x40 # 01000000   Q6
sgs 84800 0x80 # 10000000   Q7
sgs 6080 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 6720 0x7F # 01111111   Q6
sgs 87360 0x40 # 01000000   Q6
sgs 6080 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 5760 0x7F # 01111111   Q6
sgs 3520 0x40 # 01000000   Q6
sgs 84800 0x80 # 10000000   Q7
sgs 6080 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 6720 0x7F # 01111111   Q6
sgs 80640 0x40 # 01000000   Q6
sgs 12800 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p3  (12 entries, util 1.5200 %)

```
sgs 31680 0x7F # 01111111   Q6
sgs 3840 0x40 # 01000000   Q6
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

### sw03-p4  (19 entries, util 2.0800 %)

```
sgs 17600 0x7F # 01111111   Q6
sgs 9920 0x40 # 01000000   Q6
sgs 3840 0x80 # 10000000   Q7
sgs 8000 0x40 # 01000000   Q6
sgs 129280 0x80 # 10000000   Q7
sgs 31360 0xBF # 10111111   Q7
sgs 17600 0x7F # 01111111   Q6
sgs 9920 0x40 # 01000000   Q6
sgs 141120 0x80 # 10000000   Q7
sgs 31360 0xBF # 10111111   Q7
sgs 17600 0x7F # 01111111   Q6
sgs 9920 0x40 # 01000000   Q6
sgs 3840 0x80 # 10000000   Q7
sgs 137280 0x40 # 01000000   Q6
sgs 31360 0xBF # 10111111   Q7
sgs 17600 0x7F # 01111111   Q6
sgs 9920 0x40 # 01000000   Q6
sgs 123520 0x80 # 10000000   Q7
sgs 48960 0xBF # 10111111   Q7
```

### sw03-p5  (17 entries, util 0.0000 %)

```
sgs 36480 0x40 # 01000000   Q6
sgs 36480 0x80 # 10000000   Q7
sgs 27200 0xBF # 10111111   Q7
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

### sw04-p3  (17 entries, util 0.0000 %)

```
sgs 36480 0x40 # 01000000   Q6
sgs 36480 0x80 # 10000000   Q7
sgs 27200 0xBF # 10111111   Q7
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

### sw04-p4  (17 entries, util 0.0000 %)

```
sgs 36480 0x40 # 01000000   Q6
sgs 36480 0x80 # 10000000   Q7
sgs 27200 0xBF # 10111111   Q7
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

### sw04-p5  (17 entries, util 0.0000 %)

```
sgs 36480 0x40 # 01000000   Q6
sgs 36480 0x80 # 10000000   Q7
sgs 27200 0xBF # 10111111   Q7
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

### sw05-p2  (19 entries, util 1.2800 %)

```
sgs 12480 0x7F # 01111111   Q6
sgs 3520 0x40 # 01000000   Q6
sgs 84800 0x80 # 10000000   Q7
sgs 49280 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 13440 0x7F # 01111111   Q6
sgs 87360 0x40 # 01000000   Q6
sgs 49280 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 3520 0x40 # 01000000   Q6
sgs 84800 0x80 # 10000000   Q7
sgs 49280 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 13440 0x7F # 01111111   Q6
sgs 73920 0x40 # 01000000   Q6
sgs 12800 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p3  (17 entries, util 0.0000 %)

```
sgs 36480 0x40 # 01000000   Q6
sgs 36480 0x80 # 10000000   Q7
sgs 27200 0xBF # 10111111   Q7
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

### sw05-p4  (17 entries, util 0.0000 %)

```
sgs 36480 0x40 # 01000000   Q6
sgs 36480 0x80 # 10000000   Q7
sgs 27200 0xBF # 10111111   Q7
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

### sw05-p5  (20 entries, util 0.6400 %)

```
sgs 23680 0x7F # 01111111   Q6
sgs 4480 0x40 # 01000000   Q6
sgs 9920 0x80 # 10000000   Q7
sgs 3520 0x40 # 01000000   Q6
sgs 98240 0x80 # 10000000   Q7
sgs 10240 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 28160 0x7F # 01111111   Q6
sgs 107200 0x80 # 10000000   Q7
sgs 14720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 23680 0x7F # 01111111   Q6
sgs 4480 0x40 # 01000000   Q6
sgs 111680 0x80 # 10000000   Q7
sgs 10240 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 28160 0x7F # 01111111   Q6
sgs 83520 0x80 # 10000000   Q7
sgs 38400 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p2  (19 entries, util 2.0800 %)

```
sgs 24640 0x7F # 01111111   Q6
sgs 11520 0x40 # 01000000   Q6
sgs 3520 0x80 # 10000000   Q7
sgs 8000 0x40 # 01000000   Q6
sgs 128000 0x80 # 10000000   Q7
sgs 24320 0xBF # 10111111   Q7
sgs 24640 0x7F # 01111111   Q6
sgs 11520 0x40 # 01000000   Q6
sgs 139520 0x80 # 10000000   Q7
sgs 24320 0xBF # 10111111   Q7
sgs 24640 0x7F # 01111111   Q6
sgs 11520 0x40 # 01000000   Q6
sgs 3520 0x80 # 10000000   Q7
sgs 136000 0x40 # 01000000   Q6
sgs 24320 0xBF # 10111111   Q7
sgs 24640 0x7F # 01111111   Q6
sgs 11520 0x40 # 01000000   Q6
sgs 114880 0x80 # 10000000   Q7
sgs 48960 0xBF # 10111111   Q7
```

### sw06-p3  (12 entries, util 1.5200 %)

```
sgs 24000 0x7F # 01111111   Q6
sgs 4160 0x40 # 01000000   Q6
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

### sw06-p4  (17 entries, util 0.0000 %)

```
sgs 36480 0x40 # 01000000   Q6
sgs 36480 0x80 # 10000000   Q7
sgs 27200 0xBF # 10111111   Q7
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

### sw06-p5  (17 entries, util 0.0000 %)

```
sgs 36480 0x40 # 01000000   Q6
sgs 36480 0x80 # 10000000   Q7
sgs 27200 0xBF # 10111111   Q7
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

### sw07-p3  (20 entries, util 0.6400 %)

```
sgs 16960 0x7F # 01111111   Q6
sgs 3520 0x40 # 01000000   Q6
sgs 8960 0x80 # 10000000   Q7
sgs 3520 0x40 # 01000000   Q6
sgs 99200 0x80 # 10000000   Q7
sgs 17920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 108160 0x80 # 10000000   Q7
sgs 21440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16960 0x7F # 01111111   Q6
sgs 3520 0x40 # 01000000   Q6
sgs 111680 0x80 # 10000000   Q7
sgs 17920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 91200 0x80 # 10000000   Q7
sgs 38400 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (19 entries, util 1.2800 %)

```
sgs 19200 0x7F # 01111111   Q6
sgs 3520 0x40 # 01000000   Q6
sgs 84800 0x80 # 10000000   Q7
sgs 42560 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 87360 0x40 # 01000000   Q6
sgs 42560 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 19200 0x7F # 01111111   Q6
sgs 3520 0x40 # 01000000   Q6
sgs 84800 0x80 # 10000000   Q7
sgs 42560 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 67200 0x40 # 01000000   Q6
sgs 12800 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p5  (17 entries, util 0.0000 %)

```
sgs 36480 0x40 # 01000000   Q6
sgs 36480 0x80 # 10000000   Q7
sgs 27200 0xBF # 10111111   Q7
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

### sw08-p2  (23 entries, util 3.3600 %)

```
sgs 26880 0x7F # 01111111   Q6
sgs 8320 0x40 # 01000000   Q6
sgs 4800 0x80 # 10000000   Q7
sgs 4160 0x40 # 01000000   Q6
sgs 3520 0x80 # 10000000   Q7
sgs 8320 0x40 # 01000000   Q6
sgs 128000 0x80 # 10000000   Q7
sgs 16000 0xBF # 10111111   Q7
sgs 26880 0x7F # 01111111   Q6
sgs 17280 0x40 # 01000000   Q6
sgs 139840 0x80 # 10000000   Q7
sgs 16000 0xBF # 10111111   Q7
sgs 26880 0x7F # 01111111   Q6
sgs 8320 0x40 # 01000000   Q6
sgs 4800 0x80 # 10000000   Q7
sgs 4160 0x40 # 01000000   Q6
sgs 3520 0x80 # 10000000   Q7
sgs 136320 0x40 # 01000000   Q6
sgs 16000 0xBF # 10111111   Q7
sgs 26880 0x7F # 01111111   Q6
sgs 17280 0x40 # 01000000   Q6
sgs 112960 0x80 # 10000000   Q7
sgs 42880 0xBF # 10111111   Q7
```

### sw08-p4  (12 entries, util 1.5200 %)

```
sgs 16320 0x7F # 01111111   Q6
sgs 5120 0x40 # 01000000   Q6
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

### sw08-p5  (20 entries, util 0.6400 %)

```
sgs 9280 0x7F # 01111111   Q6
sgs 3520 0x40 # 01000000   Q6
sgs 8000 0x80 # 10000000   Q7
sgs 3520 0x40 # 01000000   Q6
sgs 100160 0x80 # 10000000   Q7
sgs 25600 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 12800 0x7F # 01111111   Q6
sgs 109120 0x80 # 10000000   Q7
sgs 28160 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 9280 0x7F # 01111111   Q6
sgs 3520 0x40 # 01000000   Q6
sgs 111680 0x80 # 10000000   Q7
sgs 25600 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 12800 0x7F # 01111111   Q6
sgs 98880 0x80 # 10000000   Q7
sgs 38400 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

