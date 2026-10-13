# RL-enlarged GCL schedule (Problem 2: window enlargement)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Seeded from SMT run: **result/result-2026-10-12-dataset-testbed-6-ring-avgwin/smt-c9-off/6-t3600-c9off-minlat**

## Admission (unchanged) vs. capacity grown

Problem 2 never admits a flow into the schedule it exports -- it only widens windows. `admitted` below is exactly the SMT baseline, by construction; the capacity growth this run achieved is banked slack and per-port GCL entries, reported separately.

| | admitted | of total |
|---|---|---|
| SMT (fixed, never moved) | 10 | 20 |
| RL-enlarged (exported; grow-only, admits nothing new) | 10 | 20 |

During training, the policy's trial admissions (the reward signal that teaches it how much a window needs to grow) reached **9** of the 10 SMT-rejected flows -- none of those are kept in this export; that capacity stays as empty, banked slack for Problem 3 to fill. Total slack banked: 677120 ns. GCL_size overflow: 0.

## Opportunistic idle top-up (deterministic post-pass)

**12198720 ns**, drawn from idle capacity on ports at or below utilisation 0.2, independent of what training happened to grow. Ported from prob_2_heuristic_enlarged's Step 7.

| port | queue | applied (ns) |
|---|---|---|
| S1-p0 | Q6 | 175040 |
| S1-p0 | Q7 | 525120 |
| S2-p0 | Q7 | 650240 |
| sw01-p2 | Q7 | 611200 |
| sw01-p4 | Q7 | 515520 |
| sw01-p5 | Q6 | 149760 |
| sw01-p5 | Q7 | 508800 |
| sw02-p4 | Q6 | 257920 |
| sw02-p4 | Q7 | 450560 |
| sw02-p5 | Q7 | 733440 |
| sw03-p4 | Q7 | 590400 |
| sw03-p5 | Q7 | 496960 |
| sw04-p4 | Q6 | 299520 |
| sw04-p4 | Q7 | 350720 |
| sw04-p5 | Q6 | 252160 |
| sw04-p5 | Q7 | 439680 |
| sw05-p4 | Q7 | 478400 |
| sw05-p5 | Q7 | 607040 |
| sw06-p4 | Q6 | 246400 |
| sw06-p4 | Q7 | 428800 |
| sw06-p5 | Q6 | 299520 |
| sw06-p5 | Q7 | 367360 |
| sw07-p4 | Q7 | 623680 |
| sw07-p5 | Q7 | 459840 |
| sw08-p2 | Q6 | 640 |
| sw08-p2 | Q7 | 356160 |
| sw08-p4 | Q6 | 299520 |
| sw08-p4 | Q7 | 384000 |
| sw08-p5 | Q7 | 640320 |

## Opportunistic exclusive window creation (deterministic post-pass)

**4** brand-new *exclusive* window(s) opened, **49920 ns** total, on ports at or below utilisation 0.2 whose TT queue had zero windows before this run. Ported from prob_2_heuristic_enlarged's Step 8.

| port | queue | size (ns) |
|---|---|---|
| sw03-p4 | Q6 | 12480 |
| sw05-p5 | Q6 | 12480 |
| sw07-p4 | Q6 | 12480 |
| sw08-p5 | Q6 | 12480 |

## Best-effort gap equalization (deterministic post-pass)

**7091200 ns** given back from the top-up/creation above so each port's leftover non-TAS gaps land close to equal. Ported from prob_2_heuristic_enlarged's Step 9.

| port | given back (ns) |
|---|---|---|
| sw06-p4 | 531200 |
| sw04-p5 | 525440 |
| sw02-p4 | 519680 |
| sw01-p5 | 419840 |
| sw03-p4 | 400000 |
| sw05-p5 | 400000 |
| sw07-p4 | 400000 |
| sw08-p5 | 400000 |
| sw04-p4 | 361280 |
| sw06-p5 | 361280 |
| sw08-p4 | 361280 |
| sw01-p2 | 352320 |
| S1-p0 | 327680 |
| sw08-p2 | 282240 |
| sw02-p5 | 262400 |
| S2-p0 | 240000 |
| sw01-p4 | 230400 |
| sw03-p5 | 230400 |
| sw05-p4 | 230400 |
| sw07-p5 | 230400 |
| S3-p0 | 24960 |

## Opportunistic overlay window creation (deterministic post-pass)

**40** new overlay window(s), **7893120 ns** total, carved out of already-open best-effort spans on ports at or below utilisation 0.2 -- best-effort stays reachable inside each one (gate mask keeps its BE bits set). Run once after training/finalize_grow_only(), not a trained action.

| port | queue | size (ns) |
|---|---|---|
| S1-p0 | Q6 | 128000 |
| S1-p0 | Q7 | 199680 |
| S2-p0 | Q6 | 24960 |
| S2-p0 | Q7 | 215040 |
| sw01-p2 | Q6 | 199040 |
| sw01-p2 | Q7 | 211520 |
| sw01-p4 | Q6 | 116480 |
| sw01-p4 | Q7 | 143040 |
| sw01-p5 | Q6 | 149760 |
| sw01-p5 | Q7 | 286720 |
| sw02-p4 | Q6 | 286080 |
| sw02-p4 | Q7 | 250240 |
| sw02-p5 | Q6 | 153920 |
| sw02-p5 | Q7 | 150080 |
| sw03-p4 | Q6 | 233280 |
| sw03-p4 | Q7 | 258240 |
| sw03-p5 | Q6 | 218560 |
| sw03-p5 | Q7 | 57600 |
| sw04-p4 | Q6 | 240000 |
| sw04-p4 | Q7 | 159040 |
| sw04-p5 | Q6 | 261120 |
| sw04-p5 | Q7 | 297600 |
| sw05-p4 | Q6 | 185280 |
| sw05-p4 | Q7 | 107520 |
| sw05-p5 | Q6 | 237120 |
| sw05-p5 | Q7 | 237760 |
| sw06-p4 | Q6 | 284800 |
| sw06-p4 | Q7 | 296320 |
| sw06-p5 | Q6 | 173440 |
| sw06-p5 | Q7 | 208960 |
| sw07-p4 | Q6 | 237120 |
| sw07-p4 | Q7 | 221120 |
| sw07-p5 | Q6 | 135360 |
| sw07-p5 | Q7 | 174080 |
| sw08-p2 | Q6 | 122880 |
| sw08-p2 | Q7 | 224000 |
| sw08-p4 | Q6 | 120000 |
| sw08-p4 | Q7 | 245760 |
| sw08-p5 | Q6 | 245440 |
| sw08-p5 | Q7 | 196160 |

## Per-port GCL entries: before (SMT) vs. after (RL-enlarged)

| port | SMT entries | RL-enlarged entries | GCL_size |
|---|---|---|---|
| sw01-p2 | 3 | 14 | 255 |
| sw01-p4 | 9 | 20 | 255 |
| sw01-p5 | 21 | 28 | 255 |
| sw02-p2 | 37 | 27 | 255 |
| sw02-p4 | 9 | 22 | 255 |
| sw02-p5 | 3 | 9 | 255 |
| sw03-p4 | 1 | 13 | 255 |
| sw03-p5 | 9 | 17 | 255 |
| sw04-p4 | 17 | 19 | 255 |
| sw04-p5 | 9 | 20 | 255 |
| sw05-p4 | 9 | 21 | 255 |
| sw05-p5 | 1 | 14 | 255 |
| sw06-p4 | 9 | 19 | 255 |
| sw06-p5 | 17 | 19 | 255 |
| sw07-p4 | 1 | 14 | 255 |
| sw07-p5 | 9 | 21 | 255 |
| sw08-p2 | 17 | 33 | 255 |
| sw08-p4 | 17 | 19 | 255 |
| sw08-p5 | 1 | 12 | 255 |

## Flows

| flow | route | fixed | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|---|
| s0(id=1 S3->S1) | S3->sw01->sw02->S1 | yes | 6 | 0 | 45840 | yes |
| s1(id=2 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | yes | 7 | 0 | 79120 | yes |
| s2(id=3 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | no | None | None | None | no |
| s3(id=4 S1->S3) | S1->sw02->sw01->S3 | yes | 6 | 24960 | 45840 | yes |
| s4(id=5 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | no | None | None | None | no |
| s5(id=6 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | yes | 6 | 24960 | 83600 | yes |
| s6(id=7 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | yes | 6 | 49920 | 84240 | yes |
| s7(id=8 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |
| s8(id=9 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | yes | 6 | 24960 | 95760 | yes |
| s9(id=10 S1->S3) | S1->sw02->sw01->S3 | no | None | None | None | no |
| s10(id=11 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | no | None | None | None | no |
| s11(id=12 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | yes | 6 | 74880 | 79120 | yes |
| s12(id=13 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | no | None | None | None | no |
| s13(id=14 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | yes | 7 | 0 | 79120 | yes |
| s14(id=15 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |
| s15(id=16 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | no | None | None | None | no |
| s16(id=17 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |
| s17(id=18 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | no | None | None | None | no |
| s18(id=19 S3->S1) | S3->sw01->sw02->S1 | yes | 7 | 74880 | 46480 | yes |
| s19(id=20 S3->S1) | S3->sw01->sw02->S1 | yes | 7 | 49920 | 45840 | yes |

## Per-hop windows (slack_ns > 0 means this window was enlarged)

| flow | egress port | queue | psi (ns) | delta (ns) |
|---|---|---|---|---|
| s0(id=1 S3->S1) | S3-p0 | Q6 | 0 | 12480 |
| s0(id=1 S3->S1) | sw01-p5 | Q6 | 16640 | 12480 |
| s0(id=1 S3->S1) | sw02-p2 | Q6 | 33280 | 12480 |
| s1(id=2 S2->S1) | S2-p0 | Q7 | 0 | 12480 |
| s1(id=2 S2->S1) | sw08-p4 | Q7 | 16640 | 12480 |
| s1(id=2 S2->S1) | sw06-p5 | Q7 | 33280 | 12480 |
| s1(id=2 S2->S1) | sw04-p4 | Q7 | 49920 | 12480 |
| s1(id=2 S2->S1) | sw02-p2 | Q7 | 66560 | 12480 |
| s3(id=4 S1->S3) | S1-p0 | Q6 | 24960 | 12480 |
| s3(id=4 S1->S3) | sw02-p5 | Q6 | 41600 | 12480 |
| s3(id=4 S1->S3) | sw01-p2 | Q6 | 58240 | 12480 |
| s5(id=6 S2->S1) | S2-p0 | Q6 | 24960 | 12480 |
| s5(id=6 S2->S1) | sw08-p4 | Q6 | 41920 | 12480 |
| s5(id=6 S2->S1) | sw06-p5 | Q6 | 58560 | 12480 |
| s5(id=6 S2->S1) | sw04-p4 | Q6 | 75200 | 12480 |
| s5(id=6 S2->S1) | sw02-p2 | Q6 | 96000 | 12480 |
| s6(id=7 S2->S1) | S2-p0 | Q6 | 49920 | 12480 |
| s6(id=7 S2->S1) | sw08-p4 | Q6 | 66560 | 12480 |
| s6(id=7 S2->S1) | sw06-p5 | Q6 | 83200 | 12480 |
| s6(id=7 S2->S1) | sw04-p4 | Q6 | 99840 | 12480 |
| s6(id=7 S2->S1) | sw02-p2 | Q6 | 121600 | 12480 |
| s8(id=9 S3->S2) | S3-p0 | Q6 | 24960 | 12480 |
| s8(id=9 S3->S2) | sw01-p4 | Q6 | 41600 | 12480 |
| s8(id=9 S3->S2) | sw03-p5 | Q6 | 58240 | 12480 |
| s8(id=9 S3->S2) | sw05-p4 | Q6 | 74880 | 12480 |
| s8(id=9 S3->S2) | sw07-p5 | Q6 | 91520 | 12480 |
| s8(id=9 S3->S2) | sw08-p2 | Q6 | 108160 | 12480 |
| s11(id=12 S2->S1) | S2-p0 | Q6 | 74880 | 12480 |
| s11(id=12 S2->S1) | sw08-p4 | Q6 | 91520 | 12480 |
| s11(id=12 S2->S1) | sw06-p5 | Q6 | 108160 | 12480 |
| s11(id=12 S2->S1) | sw04-p4 | Q6 | 124800 | 12480 |
| s11(id=12 S2->S1) | sw02-p2 | Q6 | 141440 | 12480 |
| s13(id=14 S1->S2) | S1-p0 | Q7 | 0 | 12480 |
| s13(id=14 S1->S2) | sw02-p4 | Q7 | 16640 | 12480 |
| s13(id=14 S1->S2) | sw04-p5 | Q7 | 33280 | 12480 |
| s13(id=14 S1->S2) | sw06-p4 | Q7 | 49920 | 12480 |
| s13(id=14 S1->S2) | sw08-p2 | Q7 | 66560 | 12480 |
| s18(id=19 S3->S1) | S3-p0 | Q7 | 74880 | 12480 |
| s18(id=19 S3->S1) | sw01-p5 | Q7 | 91840 | 12480 |
| s18(id=19 S3->S1) | sw02-p2 | Q7 | 108800 | 12480 |
| s19(id=20 S3->S1) | S3-p0 | Q7 | 49920 | 12480 |
| s19(id=20 S3->S1) | sw01-p5 | Q7 | 66560 | 12480 |
| s19(id=20 S3->S1) | sw02-p2 | Q7 | 83200 | 12480 |

## Metrics (training/evaluation signal, not the export)

| metric | value |
|---|---|
| trial-placed flow ratio (fixed + trial-admitted) | 0.950 |
| r1  same-queue window adjacency | 0.318 |
| r2  deadline-violation ratio | 0.000 |
| r3  supplier/receiver overlap | 0.997 |
| r4  mean e2e/deadline (admitted) | 0.242 |
| constraint violations | 0 |

## Constraint check

- C1-C7, C9: OK
- seed-integrity (no SMT-fixed flow's placement changed): OK

## GCL per egress port

### sw01-p2  (14 entries, util 1.5600 %)

```
sgs 58240 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 16960 0xBF # 10111111   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 242560 0x80 # 10000000   Q7
sgs 36800 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 121920 0x80 # 10000000   Q7
sgs 57600 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p4  (20 entries, util 6.2400 %)

```
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 117440 0x80 # 10000000   Q7
sgs 28480 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 117440 0x80 # 10000000   Q7
sgs 28480 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 117440 0x80 # 10000000   Q7
sgs 28480 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 88320 0x80 # 10000000   Q7
sgs 57600 0xBF # 10111111   Q7
```

### sw01-p5  (28 entries, util 15.6000 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 63680 0x80 # 10000000   Q7
sgs 44480 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 88960 0x80 # 10000000   Q7
sgs 44480 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 63680 0x80 # 10000000   Q7
sgs 44480 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 72320 0x80 # 10000000   Q7
sgs 61120 0xBF # 10111111   Q7
```

### sw02-p2  (27 entries, util 28.0800 %)

```
sgs 33280 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x3F # 00111111   BE
sgs 29120 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 32320 0x40 # 01000000   Q6
sgs 79360 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x3F # 00111111   BE
sgs 29120 0x80 # 10000000   Q7
sgs 137600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x3F # 00111111   BE
sgs 29120 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 112000 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x3F # 00111111   BE
sgs 29120 0x80 # 10000000   Q7
sgs 104320 0x3F # 00111111   BE
```

### sw02-p4  (22 entries, util 6.2400 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 25280 0xBF # 10111111   Q7
sgs 34560 0x40 # 01000000   Q6
sgs 40320 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 93120 0x80 # 10000000   Q7
sgs 40320 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 25280 0xBF # 10111111   Q7
sgs 34560 0x40 # 01000000   Q6
sgs 40320 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 76480 0x80 # 10000000   Q7
sgs 56960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p5  (9 entries, util 1.5600 %)

```
sgs 41600 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 483520 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (13 entries, util 0.0000 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 54080 0xBF # 10111111   Q7
sgs 200000 0x80 # 10000000   Q7
sgs 46080 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 54080 0xBF # 10111111   Q7
sgs 96000 0x80 # 10000000   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p5  (17 entries, util 6.2400 %)

```
sgs 45760 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 117440 0x80 # 10000000   Q7
sgs 57600 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 117440 0x80 # 10000000   Q7
sgs 57600 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 117440 0x80 # 10000000   Q7
sgs 57600 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 71680 0x80 # 10000000   Q7
sgs 57600 0xBF # 10111111   Q7
```

### sw04-p4  (19 entries, util 12.4800 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 37120 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 47360 0x40 # 01000000   Q6
sgs 27840 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 122240 0x80 # 10000000   Q7
sgs 27840 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 96960 0x40 # 01000000   Q6
sgs 27840 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 72320 0x80 # 10000000   Q7
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (20 entries, util 6.2400 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 48960 0xBF # 10111111   Q7
sgs 31680 0x40 # 01000000   Q6
sgs 23680 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 93120 0x80 # 10000000   Q7
sgs 23680 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 48960 0xBF # 10111111   Q7
sgs 31680 0x40 # 01000000   Q6
sgs 23680 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 59840 0x80 # 10000000   Q7
sgs 56960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (21 entries, util 6.2400 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 117440 0x80 # 10000000   Q7
sgs 45120 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 117440 0x80 # 10000000   Q7
sgs 45120 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 117440 0x80 # 10000000   Q7
sgs 45120 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 55040 0x80 # 10000000   Q7
sgs 57600 0xBF # 10111111   Q7
```

### sw05-p5  (14 entries, util 0.0000 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 37440 0xBF # 10111111   Q7
sgs 200000 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 37440 0xBF # 10111111   Q7
sgs 112640 0x80 # 10000000   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p4  (19 entries, util 6.2400 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 37760 0xBF # 10111111   Q7
sgs 14080 0x7F # 01111111   Q6
sgs 28800 0x40 # 01000000   Q6
sgs 56960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 93120 0x80 # 10000000   Q7
sgs 56960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 37760 0xBF # 10111111   Q7
sgs 14080 0x7F # 01111111   Q6
sgs 28800 0x40 # 01000000   Q6
sgs 56960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 43200 0x80 # 10000000   Q7
sgs 56960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (19 entries, util 12.4800 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 37120 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 47360 0x40 # 01000000   Q6
sgs 44480 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 122240 0x80 # 10000000   Q7
sgs 44480 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 96960 0x40 # 01000000   Q6
sgs 44480 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 88960 0x80 # 10000000   Q7
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (14 entries, util 0.0000 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 20800 0xBF # 10111111   Q7
sgs 200000 0x80 # 10000000   Q7
sgs 29440 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 20800 0xBF # 10111111   Q7
sgs 129280 0x80 # 10000000   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p5  (21 entries, util 6.2400 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 117440 0x80 # 10000000   Q7
sgs 28480 0x7F # 01111111   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 117440 0x80 # 10000000   Q7
sgs 28480 0x7F # 01111111   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 117440 0x80 # 10000000   Q7
sgs 28480 0x7F # 01111111   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 38400 0x80 # 10000000   Q7
sgs 57600 0xBF # 10111111   Q7
```

### sw08-p2  (33 entries, util 12.4800 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 29120 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 79040 0x80 # 10000000   Q7
sgs 24320 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 29120 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 104960 0x80 # 10000000   Q7
sgs 24320 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 29120 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 79040 0x80 # 10000000   Q7
sgs 24320 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 29120 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 38400 0x80 # 10000000   Q7
sgs 40960 0xBF # 10111111   Q7
```

### sw08-p4  (19 entries, util 12.4800 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0x7F # 01111111   Q6
sgs 37120 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 47360 0x40 # 01000000   Q6
sgs 61120 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 122240 0x80 # 10000000   Q7
sgs 61120 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0x7F # 01111111   Q6
sgs 96960 0x40 # 01000000   Q6
sgs 61120 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 105600 0x80 # 10000000   Q7
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (12 entries, util 0.0000 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 41600 0x7F # 01111111   Q6
sgs 200000 0x80 # 10000000   Q7
sgs 46080 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 54080 0x7F # 01111111   Q6
sgs 145920 0x80 # 10000000   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

