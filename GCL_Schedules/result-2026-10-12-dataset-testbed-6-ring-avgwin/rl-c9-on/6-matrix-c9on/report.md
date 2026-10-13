# RL-enlarged GCL schedule (Problem 2: window enlargement)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Seeded from SMT run: **result/result-2026-10-12-dataset-testbed-6-ring-avgwin/smt-c9-on/6-fair-retimed-c9on**

## Admission (unchanged) vs. capacity grown

Problem 2 never admits a flow into the schedule it exports -- it only widens windows. `admitted` below is exactly the SMT baseline, by construction; the capacity growth this run achieved is banked slack and per-port GCL entries, reported separately.

| | admitted | of total |
|---|---|---|
| SMT (fixed, never moved) | 10 | 10 |
| RL-enlarged (exported; grow-only, admits nothing new) | 10 | 20 |

During training, the policy's trial admissions (the reward signal that teaches it how much a window needs to grow) reached **9** of the 10 SMT-rejected flows -- none of those are kept in this export; that capacity stays as empty, banked slack for Problem 3 to fill. Total slack banked: 494720 ns. GCL_size overflow: 0.

## Opportunistic idle top-up (deterministic post-pass)

**12792960 ns**, drawn from idle capacity on ports at or below utilisation 0.2, independent of what training happened to grow. Ported from prob_2_heuristic_enlarged's Step 7.

| port | queue | applied (ns) |
|---|---|---|
| S1-p0 | Q6 | 150080 |
| S1-p0 | Q7 | 550080 |
| S2-p0 | Q6 | 500160 |
| S2-p0 | Q7 | 150080 |
| sw01-p2 | Q6 | 355520 |
| sw01-p2 | Q7 | 325120 |
| sw01-p4 | Q6 | 103040 |
| sw01-p4 | Q7 | 428160 |
| sw01-p5 | Q6 | 526080 |
| sw01-p5 | Q7 | 140800 |
| sw02-p4 | Q7 | 624640 |
| sw02-p5 | Q6 | 739200 |
| sw03-p4 | Q6 | 344000 |
| sw03-p4 | Q7 | 331840 |
| sw03-p5 | Q6 | 98560 |
| sw03-p5 | Q7 | 433280 |
| sw04-p4 | Q6 | 549120 |
| sw04-p4 | Q7 | 128000 |
| sw04-p5 | Q7 | 616320 |
| sw05-p4 | Q6 | 96640 |
| sw05-p4 | Q7 | 437120 |
| sw05-p5 | Q6 | 342400 |
| sw05-p5 | Q7 | 338560 |
| sw06-p4 | Q7 | 709760 |
| sw06-p5 | Q6 | 557760 |
| sw06-p5 | Q7 | 127040 |
| sw07-p4 | Q6 | 340800 |
| sw07-p4 | Q7 | 345280 |
| sw07-p5 | Q6 | 92160 |
| sw07-p5 | Q7 | 442240 |
| sw08-p2 | Q6 | 72640 |
| sw08-p2 | Q7 | 410880 |
| sw08-p4 | Q6 | 566400 |
| sw08-p4 | Q7 | 126080 |
| sw08-p5 | Q6 | 339200 |
| sw08-p5 | Q7 | 353920 |

## Opportunistic exclusive window creation (deterministic post-pass)

**2** brand-new *exclusive* window(s) opened, **24960 ns** total, on ports at or below utilisation 0.2 whose TT queue had zero windows before this run. Ported from prob_2_heuristic_enlarged's Step 8.

| port | queue | size (ns) |
|---|---|---|
| sw02-p5 | Q7 | 12480 |
| sw06-p4 | Q6 | 12480 |

## Best-effort gap equalization (deterministic post-pass)

**7877120 ns** given back from the top-up/creation above so each port's leftover non-TAS gaps land close to equal. Ported from prob_2_heuristic_enlarged's Step 9.

| port | given back (ns) |
|---|---|---|
| sw02-p4 | 599040 |
| sw04-p5 | 599040 |
| S1-p0 | 504000 |
| sw06-p4 | 476800 |
| sw08-p5 | 435840 |
| sw07-p4 | 434240 |
| sw05-p5 | 432640 |
| sw03-p4 | 431040 |
| sw01-p5 | 414720 |
| sw08-p2 | 380160 |
| sw01-p2 | 369280 |
| sw08-p4 | 355840 |
| sw06-p5 | 350720 |
| sw04-p4 | 345600 |
| sw07-p5 | 310080 |
| sw05-p4 | 298240 |
| sw03-p5 | 284480 |
| sw01-p4 | 272640 |
| S2-p0 | 270400 |
| sw02-p5 | 262400 |
| S3-p0 | 49920 |

## Opportunistic overlay window creation (deterministic post-pass)

**40** new overlay window(s), **8118720 ns** total, carved out of already-open best-effort spans on ports at or below utilisation 0.2 -- best-effort stays reachable inside each one (gate mask keeps its BE bits set). Run once after training/finalize_grow_only(), not a trained action.

| port | queue | size (ns) |
|---|---|---|
| S1-p0 | Q6 | 212160 |
| S1-p0 | Q7 | 291840 |
| S2-p0 | Q6 | 24960 |
| S2-p0 | Q7 | 245440 |
| sw01-p2 | Q6 | 199360 |
| sw01-p2 | Q7 | 208320 |
| sw01-p4 | Q6 | 70400 |
| sw01-p4 | Q7 | 205760 |
| sw01-p5 | Q6 | 140800 |
| sw01-p5 | Q7 | 273920 |
| sw02-p4 | Q6 | 199680 |
| sw02-p4 | Q7 | 399360 |
| sw02-p5 | Q6 | 131520 |
| sw02-p5 | Q7 | 150080 |
| sw03-p4 | Q6 | 249600 |
| sw03-p4 | Q7 | 249600 |
| sw03-p5 | Q6 | 90880 |
| sw03-p5 | Q7 | 190720 |
| sw04-p4 | Q6 | 120000 |
| sw04-p4 | Q7 | 231360 |
| sw04-p5 | Q6 | 199680 |
| sw04-p5 | Q7 | 399360 |
| sw05-p4 | Q6 | 131200 |
| sw05-p4 | Q7 | 155200 |
| sw05-p5 | Q6 | 270720 |
| sw05-p5 | Q7 | 222400 |
| sw06-p4 | Q6 | 219520 |
| sw06-p4 | Q7 | 257280 |
| sw06-p5 | Q6 | 126720 |
| sw06-p5 | Q7 | 215360 |
| sw07-p4 | Q6 | 255360 |
| sw07-p4 | Q7 | 231680 |
| sw07-p5 | Q6 | 160000 |
| sw07-p5 | Q7 | 183040 |
| sw08-p2 | Q6 | 194560 |
| sw08-p2 | Q7 | 204800 |
| sw08-p4 | Q6 | 88320 |
| sw08-p4 | Q7 | 236800 |
| sw08-p5 | Q6 | 240000 |
| sw08-p5 | Q7 | 240960 |

## Per-port GCL entries: before (SMT) vs. after (RL-enlarged)

| port | SMT entries | RL-enlarged entries | GCL_size |
|---|---|---|---|
| sw01-p2 | 3 | 14 | 255 |
| sw01-p4 | 9 | 30 | 255 |
| sw01-p5 | 21 | 21 | 255 |
| sw02-p2 | 37 | 29 | 255 |
| sw02-p4 | 9 | 17 | 255 |
| sw02-p5 | 3 | 9 | 255 |
| sw03-p4 | 1 | 15 | 255 |
| sw03-p5 | 9 | 26 | 255 |
| sw04-p4 | 17 | 15 | 255 |
| sw04-p5 | 9 | 17 | 255 |
| sw05-p4 | 9 | 31 | 255 |
| sw05-p5 | 1 | 13 | 255 |
| sw06-p4 | 9 | 23 | 255 |
| sw06-p5 | 17 | 18 | 255 |
| sw07-p4 | 1 | 13 | 255 |
| sw07-p5 | 9 | 27 | 255 |
| sw08-p2 | 17 | 34 | 255 |
| sw08-p4 | 17 | 15 | 255 |
| sw08-p5 | 1 | 13 | 255 |

## Flows

| flow | route | fixed | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|---|
| s0(id=1 S3->S1) | S3->sw01->sw02->S1 | yes | 7 | 0 | 29200 | yes |
| s1(id=2 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | yes | 6 | 0 | 43280 | yes |
| s2(id=3 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | no | None | None | None | no |
| s3(id=4 S1->S3) | S1->sw02->sw01->S3 | yes | 6 | 24960 | 26000 | yes |
| s4(id=5 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | no | None | None | None | no |
| s5(id=6 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | yes | 6 | 24960 | 33040 | yes |
| s6(id=7 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | yes | 7 | 49920 | 39440 | yes |
| s7(id=8 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |
| s8(id=9 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | yes | 6 | 24960 | 54160 | yes |
| s9(id=10 S1->S3) | S1->sw02->sw01->S3 | no | None | None | None | no |
| s10(id=11 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | no | None | None | None | no |
| s11(id=12 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | yes | 7 | 74880 | 42000 | yes |
| s12(id=13 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | no | None | None | None | no |
| s13(id=14 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | yes | 7 | 0 | 33040 | yes |
| s14(id=15 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |
| s15(id=16 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | no | None | None | None | no |
| s16(id=17 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |
| s17(id=18 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | no | None | None | None | no |
| s18(id=19 S3->S1) | S3->sw01->sw02->S1 | yes | 6 | 74880 | 29200 | yes |
| s19(id=20 S3->S1) | S3->sw01->sw02->S1 | yes | 6 | 49920 | 24720 | yes |

## Per-hop windows (slack_ns > 0 means this window was enlarged)

| flow | egress port | queue | psi (ns) | delta (ns) |
|---|---|---|---|---|
| s0(id=1 S3->S1) | S3-p0 | Q7 | 0 | 12480 |
| s0(id=1 S3->S1) | sw01-p5 | Q7 | 8320 | 12480 |
| s0(id=1 S3->S1) | sw02-p2 | Q7 | 16640 | 12480 |
| s1(id=2 S2->S1) | S2-p0 | Q6 | 0 | 12480 |
| s1(id=2 S2->S1) | sw08-p4 | Q6 | 7680 | 12480 |
| s1(id=2 S2->S1) | sw06-p5 | Q6 | 15360 | 12480 |
| s1(id=2 S2->S1) | sw04-p4 | Q6 | 23040 | 12480 |
| s1(id=2 S2->S1) | sw02-p2 | Q6 | 30720 | 12480 |
| s3(id=4 S1->S3) | S1-p0 | Q6 | 24960 | 12480 |
| s3(id=4 S1->S3) | sw02-p5 | Q6 | 31680 | 12480 |
| s3(id=4 S1->S3) | sw01-p2 | Q6 | 38400 | 12480 |
| s5(id=6 S2->S1) | S2-p0 | Q6 | 24960 | 12480 |
| s5(id=6 S2->S1) | sw08-p4 | Q6 | 30080 | 12480 |
| s5(id=6 S2->S1) | sw06-p5 | Q6 | 35200 | 12480 |
| s5(id=6 S2->S1) | sw04-p4 | Q6 | 40320 | 12480 |
| s5(id=6 S2->S1) | sw02-p2 | Q6 | 45440 | 12480 |
| s6(id=7 S2->S1) | S2-p0 | Q7 | 49920 | 12480 |
| s6(id=7 S2->S1) | sw08-p4 | Q7 | 56640 | 12480 |
| s6(id=7 S2->S1) | sw06-p5 | Q7 | 63360 | 12480 |
| s6(id=7 S2->S1) | sw04-p4 | Q7 | 70080 | 12480 |
| s6(id=7 S2->S1) | sw02-p2 | Q7 | 76800 | 12480 |
| s8(id=9 S3->S2) | S3-p0 | Q6 | 24960 | 12480 |
| s8(id=9 S3->S2) | sw01-p4 | Q6 | 33280 | 12480 |
| s8(id=9 S3->S2) | sw03-p5 | Q6 | 41600 | 12480 |
| s8(id=9 S3->S2) | sw05-p4 | Q6 | 49920 | 12480 |
| s8(id=9 S3->S2) | sw07-p5 | Q6 | 58240 | 12480 |
| s8(id=9 S3->S2) | sw08-p2 | Q6 | 66560 | 12480 |
| s11(id=12 S2->S1) | S2-p0 | Q7 | 74880 | 12480 |
| s11(id=12 S2->S1) | sw08-p4 | Q7 | 80000 | 12480 |
| s11(id=12 S2->S1) | sw06-p5 | Q7 | 85120 | 12480 |
| s11(id=12 S2->S1) | sw04-p4 | Q7 | 90240 | 12480 |
| s11(id=12 S2->S1) | sw02-p2 | Q7 | 104320 | 12480 |
| s13(id=14 S1->S2) | S1-p0 | Q7 | 0 | 12480 |
| s13(id=14 S1->S2) | sw02-p4 | Q7 | 5120 | 12480 |
| s13(id=14 S1->S2) | sw04-p5 | Q7 | 10240 | 12480 |
| s13(id=14 S1->S2) | sw06-p4 | Q7 | 15360 | 12480 |
| s13(id=14 S1->S2) | sw08-p2 | Q7 | 20480 | 12480 |
| s18(id=19 S3->S1) | S3-p0 | Q6 | 74880 | 12480 |
| s18(id=19 S3->S1) | sw01-p5 | Q6 | 83200 | 12480 |
| s18(id=19 S3->S1) | sw02-p2 | Q6 | 91520 | 12480 |
| s19(id=20 S3->S1) | S3-p0 | Q6 | 49920 | 12480 |
| s19(id=20 S3->S1) | sw01-p5 | Q6 | 56000 | 12480 |
| s19(id=20 S3->S1) | sw02-p2 | Q6 | 62080 | 12480 |

## Metrics (training/evaluation signal, not the export)

| metric | value |
|---|---|
| trial-placed flow ratio (fixed + trial-admitted) | 0.950 |
| r1  same-queue window adjacency | 0.357 |
| r2  deadline-violation ratio | 0.000 |
| r3  supplier/receiver overlap | 0.998 |
| r4  mean e2e/deadline (admitted) | 0.127 |
| constraint violations | 0 |

## Constraint check

- C1-C7, C9: OK
- seed-integrity (no SMT-fixed flow's placement changed): OK

## GCL per egress port

### sw01-p2  (14 entries, util 1.5600 %)

```
sgs 38400 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 29440 0x7F # 01111111   Q6
sgs 200640 0x40 # 01000000   Q6
sgs 31680 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 25920 0xBF # 10111111   Q7
sgs 166720 0x80 # 10000000   Q7
sgs 57600 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p4  (30 entries, util 6.2400 %)

```
sgs 17600 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 3200 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 44800 0xBF # 10111111   Q7
sgs 60800 0x40 # 01000000   Q6
sgs 35840 0xBF # 10111111   Q7
sgs 17600 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 3200 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 118080 0x80 # 10000000   Q7
sgs 35840 0xBF # 10111111   Q7
sgs 17600 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 3200 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 118080 0x80 # 10000000   Q7
sgs 35840 0xBF # 10111111   Q7
sgs 17600 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 3200 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 100480 0x80 # 10000000   Q7
sgs 53440 0xBF # 10111111   Q7
```

### sw01-p5  (21 entries, util 15.6000 %)

```
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 35200 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 14720 0xBF # 10111111   Q7
sgs 64000 0x40 # 01000000   Q6
sgs 61120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 35200 0x7F # 01111111   Q6
sgs 91200 0x40 # 01000000   Q6
sgs 61120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 35200 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 14720 0xBF # 10111111   Q7
sgs 64000 0x40 # 01000000   Q6
sgs 61120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 35200 0x7F # 01111111   Q6
sgs 82880 0x40 # 01000000   Q6
sgs 61120 0xBF # 10111111   Q7
```

### sw02-p2  (29 entries, util 28.0800 %)

```
sgs 16640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 1600 0x3F # 00111111   BE
sgs 43840 0x40 # 01000000   Q6
sgs 2240 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 2240 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 99840 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 1600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 18880 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 142080 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 1600 0x3F # 00111111   BE
sgs 43840 0x40 # 01000000   Q6
sgs 16960 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 112640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 1600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 18880 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 125440 0x3F # 00111111   BE
```

### sw02-p4  (17 entries, util 6.2400 %)

```
sgs 5120 0x3F # 00111111   BE
sgs 50240 0x80 # 10000000   Q7
sgs 44800 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 55040 0xBF # 10111111   Q7
sgs 50240 0x80 # 10000000   Q7
sgs 44800 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 55040 0xBF # 10111111   Q7
sgs 50240 0x80 # 10000000   Q7
sgs 44800 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 55040 0xBF # 10111111   Q7
sgs 45120 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p5  (9 entries, util 1.5600 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 19200 0x7F # 01111111   Q6
sgs 505920 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (15 entries, util 0.0000 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 18240 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 31040 0xBF # 10111111   Q7
sgs 156480 0x40 # 01000000   Q6
sgs 32000 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 18240 0xBF # 10111111   Q7
sgs 131840 0x80 # 10000000   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p5  (26 entries, util 6.2400 %)

```
sgs 22720 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 6400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 45120 0xBF # 10111111   Q7
sgs 57600 0x40 # 01000000   Q6
sgs 30720 0xBF # 10111111   Q7
sgs 22720 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 6400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 115200 0x80 # 10000000   Q7
sgs 30720 0xBF # 10111111   Q7
sgs 22720 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 6400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 115200 0x80 # 10000000   Q7
sgs 30720 0xBF # 10111111   Q7
sgs 22720 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 6400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 92480 0x80 # 10000000   Q7
sgs 53440 0xBF # 10111111   Q7
```

### sw04-p4  (15 entries, util 12.4800 %)

```
sgs 23040 0x7F # 01111111   Q6
sgs 29760 0x40 # 01000000   Q6
sgs 17280 0xBF # 10111111   Q7
sgs 75200 0x80 # 10000000   Q7
sgs 54720 0xBF # 10111111   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 122240 0x40 # 01000000   Q6
sgs 54720 0xBF # 10111111   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 122240 0x40 # 01000000   Q6
sgs 54720 0xBF # 10111111   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 99200 0x40 # 01000000   Q6
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (17 entries, util 6.2400 %)

```
sgs 10240 0x3F # 00111111   BE
sgs 50240 0x80 # 10000000   Q7
sgs 39680 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 60160 0xBF # 10111111   Q7
sgs 50240 0x80 # 10000000   Q7
sgs 39680 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 60160 0xBF # 10111111   Q7
sgs 50240 0x80 # 10000000   Q7
sgs 39680 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 60160 0xBF # 10111111   Q7
sgs 40000 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (31 entries, util 6.2400 %)

```
sgs 27840 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 9600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 19840 0x7F # 01111111   Q6
sgs 54400 0x40 # 01000000   Q6
sgs 25600 0xBF # 10111111   Q7
sgs 27840 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 9600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 111680 0x80 # 10000000   Q7
sgs 25600 0xBF # 10111111   Q7
sgs 27840 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 9600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 111680 0x80 # 10000000   Q7
sgs 25600 0xBF # 10111111   Q7
sgs 27840 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 9600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 83840 0x80 # 10000000   Q7
sgs 53440 0xBF # 10111111   Q7
```

### sw05-p5  (13 entries, util 0.0000 %)

```
sgs 60480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 32640 0xBF # 10111111   Q7
sgs 154880 0x40 # 01000000   Q6
sgs 39680 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 60480 0x7F # 01111111   Q6
sgs 139520 0x80 # 10000000   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p4  (23 entries, util 6.2400 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 2880 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 22080 0x7F # 01111111   Q6
sgs 28800 0xBF # 10111111   Q7
sgs 42880 0x80 # 10000000   Q7
sgs 28480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 106240 0x80 # 10000000   Q7
sgs 28480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 22080 0x7F # 01111111   Q6
sgs 28800 0xBF # 10111111   Q7
sgs 42880 0x80 # 10000000   Q7
sgs 28480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 90880 0x80 # 10000000   Q7
sgs 43840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (18 entries, util 12.4800 %)

```
sgs 15360 0x7F # 01111111   Q6
sgs 32320 0x40 # 01000000   Q6
sgs 15680 0xBF # 10111111   Q7
sgs 74240 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 122240 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 122240 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 106880 0x40 # 01000000   Q6
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (13 entries, util 0.0000 %)

```
sgs 52800 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 34240 0xBF # 10111111   Q7
sgs 153280 0x40 # 01000000   Q6
sgs 47360 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 52800 0x7F # 01111111   Q6
sgs 147200 0x80 # 10000000   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p5  (27 entries, util 6.2400 %)

```
sgs 32960 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 16960 0xBF # 10111111   Q7
sgs 28160 0x7F # 01111111   Q6
sgs 51200 0x40 # 01000000   Q6
sgs 20480 0xBF # 10111111   Q7
sgs 32960 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 108800 0x80 # 10000000   Q7
sgs 20480 0xBF # 10111111   Q7
sgs 32960 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 108800 0x80 # 10000000   Q7
sgs 20480 0xBF # 10111111   Q7
sgs 32960 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 75840 0x80 # 10000000   Q7
sgs 53440 0xBF # 10111111   Q7
```

### sw08-p2  (34 entries, util 12.4800 %)

```
sgs 20480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 16960 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 44800 0x7F # 01111111   Q6
sgs 33920 0x40 # 01000000   Q6
sgs 29440 0xBF # 10111111   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 16960 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 91200 0x80 # 10000000   Q7
sgs 29440 0xBF # 10111111   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 16960 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 91200 0x80 # 10000000   Q7
sgs 29440 0xBF # 10111111   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 16960 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 70720 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p4  (15 entries, util 12.4800 %)

```
sgs 7680 0x3F # 00111111   BE
sgs 34880 0x40 # 01000000   Q6
sgs 14080 0xBF # 10111111   Q7
sgs 73280 0x80 # 10000000   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 57600 0xBF # 10111111   Q7
sgs 122240 0x40 # 01000000   Q6
sgs 20160 0x7F # 01111111   Q6
sgs 57600 0xBF # 10111111   Q7
sgs 122240 0x40 # 01000000   Q6
sgs 20160 0x7F # 01111111   Q6
sgs 57600 0xBF # 10111111   Q7
sgs 114560 0x40 # 01000000   Q6
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (13 entries, util 0.0000 %)

```
sgs 45120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 35840 0xBF # 10111111   Q7
sgs 151680 0x40 # 01000000   Q6
sgs 55040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 45120 0x7F # 01111111   Q6
sgs 154880 0x80 # 10000000   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

