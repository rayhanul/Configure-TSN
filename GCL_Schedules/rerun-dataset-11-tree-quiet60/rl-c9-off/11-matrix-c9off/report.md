# RL-enlarged GCL schedule (Problem 2: window enlargement)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Seeded from SMT run: **result/result-2026-10-13-dataset-testbed-11-tree-avgwin/smt-c9-off/11-t3600-c9off-minlat**

## Admission (unchanged) vs. capacity grown

Problem 2 never admits a flow into the schedule it exports -- it only widens windows. `admitted` below is exactly the SMT baseline, by construction; the capacity growth this run achieved is banked slack and per-port GCL entries, reported separately.

| | admitted | of total |
|---|---|---|
| SMT (fixed, never moved) | 10 | 20 |
| RL-enlarged (exported; grow-only, admits nothing new) | 10 | 20 |

During training, the policy's trial admissions (the reward signal that teaches it how much a window needs to grow) reached **8** of the 10 SMT-rejected flows -- none of those are kept in this export; that capacity stays as empty, banked slack for Problem 3 to fill. Total slack banked: 332480 ns. GCL_size overflow: 0.

## Opportunistic idle top-up (deterministic post-pass)

**11177600 ns**, drawn from idle capacity on ports at or below utilisation 0.2, independent of what training happened to grow. Ported from prob_2_heuristic_enlarged's Step 7.

| port | queue | applied (ns) |
|---|---|---|
| S1-p0 | Q6 | 525120 |
| S1-p0 | Q7 | 137600 |
| S2-p0 | Q6 | 162560 |
| S2-p0 | Q7 | 500160 |
| S3-p0 | Q6 | 575360 |
| sw01-p2 | Q6 | 611200 |
| sw01-p2 | Q7 | 5760 |
| sw01-p4 | Q6 | 528000 |
| sw01-p4 | Q7 | 30720 |
| sw02-p2 | Q6 | 59520 |
| sw02-p2 | Q7 | 424960 |
| sw02-p4 | Q6 | 477760 |
| sw02-p4 | Q7 | 168320 |
| sw03-p4 | Q6 | 627840 |
| sw03-p4 | Q7 | 5760 |
| sw03-p5 | Q6 | 511360 |
| sw03-p5 | Q7 | 30720 |
| sw04-p4 | Q6 | 59520 |
| sw04-p4 | Q7 | 441600 |
| sw04-p5 | Q6 | 438080 |
| sw04-p5 | Q7 | 191360 |
| sw05-p4 | Q6 | 494720 |
| sw05-p4 | Q7 | 30720 |
| sw05-p5 | Q6 | 644480 |
| sw05-p5 | Q7 | 5760 |
| sw06-p4 | Q6 | 540800 |
| sw06-p4 | Q7 | 36480 |
| sw06-p5 | Q6 | 59520 |
| sw06-p5 | Q7 | 458240 |
| sw07-p4 | Q6 | 661120 |
| sw07-p4 | Q7 | 5760 |
| sw07-p5 | Q6 | 478080 |
| sw07-p5 | Q7 | 30720 |
| sw08-p4 | Q6 | 59520 |
| sw08-p4 | Q7 | 474880 |
| sw08-p5 | Q6 | 677760 |
| sw08-p5 | Q7 | 5760 |

## Best-effort gap equalization (deterministic post-pass)

**5871360 ns** given back from the top-up/creation above so each port's leftover non-TAS gaps land close to equal. Ported from prob_2_heuristic_enlarged's Step 9.

| port | given back (ns) |
|---|---|---|
| sw04-p4 | 487680 |
| sw06-p5 | 487680 |
| sw08-p4 | 487680 |
| sw02-p2 | 474880 |
| sw06-p4 | 314880 |
| S2-p0 | 314240 |
| sw04-p5 | 311680 |
| sw01-p2 | 300160 |
| sw03-p4 | 300160 |
| sw05-p5 | 300160 |
| sw07-p4 | 300160 |
| sw08-p5 | 300160 |
| sw02-p4 | 288640 |
| S1-p0 | 257920 |
| sw01-p4 | 195200 |
| sw03-p5 | 195200 |
| sw05-p4 | 195200 |
| sw07-p5 | 195200 |
| S3-p0 | 164480 |

## Opportunistic overlay window creation (deterministic post-pass)

**38** new overlay window(s), **6585920 ns** total, carved out of already-open best-effort spans on ports at or below utilisation 0.2 -- best-effort stays reachable inside each one (gate mask keeps its BE bits set). Run once after training/finalize_grow_only(), not a trained action.

| port | queue | size (ns) |
|---|---|---|
| S1-p0 | Q6 | 24960 |
| S1-p0 | Q7 | 232960 |
| S2-p0 | Q6 | 114560 |
| S2-p0 | Q7 | 199680 |
| S3-p0 | Q6 | 24960 |
| S3-p0 | Q7 | 139520 |
| sw01-p2 | Q6 | 224960 |
| sw01-p2 | Q7 | 165120 |
| sw01-p4 | Q6 | 97280 |
| sw01-p4 | Q7 | 114560 |
| sw02-p2 | Q6 | 350080 |
| sw02-p2 | Q7 | 191360 |
| sw02-p4 | Q6 | 91520 |
| sw02-p4 | Q7 | 213760 |
| sw03-p4 | Q6 | 205760 |
| sw03-p4 | Q7 | 167680 |
| sw03-p5 | Q6 | 168640 |
| sw03-p5 | Q7 | 59840 |
| sw04-p4 | Q6 | 338880 |
| sw04-p4 | Q7 | 198720 |
| sw04-p5 | Q6 | 186880 |
| sw04-p5 | Q7 | 158080 |
| sw05-p4 | Q6 | 167360 |
| sw05-p4 | Q7 | 77760 |
| sw05-p5 | Q6 | 164160 |
| sw05-p5 | Q7 | 192640 |
| sw06-p4 | Q6 | 213120 |
| sw06-p4 | Q7 | 150400 |
| sw06-p5 | Q6 | 212800 |
| sw06-p5 | Q7 | 308160 |
| sw07-p4 | Q6 | 163520 |
| sw07-p4 | Q7 | 176640 |
| sw07-p5 | Q6 | 129600 |
| sw07-p5 | Q7 | 132160 |
| sw08-p4 | Q6 | 149440 |
| sw08-p4 | Q7 | 354880 |
| sw08-p5 | Q6 | 166080 |
| sw08-p5 | Q7 | 157440 |

## Per-port GCL entries: before (SMT) vs. after (RL-enlarged)

| port | SMT entries | RL-enlarged entries | GCL_size |
|---|---|---|---|
| sw01-p2 | 3 | 17 | 255 |
| sw01-p4 | 23 | 29 | 255 |
| sw02-p2 | 15 | 28 | 255 |
| sw02-p4 | 17 | 22 | 255 |
| sw03-p4 | 3 | 18 | 255 |
| sw03-p5 | 23 | 26 | 255 |
| sw04-p4 | 15 | 27 | 255 |
| sw04-p5 | 17 | 22 | 255 |
| sw05-p4 | 23 | 27 | 255 |
| sw05-p5 | 3 | 18 | 255 |
| sw06-p4 | 17 | 25 | 255 |
| sw06-p5 | 15 | 26 | 255 |
| sw07-p4 | 3 | 16 | 255 |
| sw07-p5 | 23 | 30 | 255 |
| sw08-p2 | 35 | 31 | 255 |
| sw08-p4 | 15 | 27 | 255 |
| sw08-p5 | 3 | 17 | 255 |

## Flows

| flow | route | fixed | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|---|
| s0(id=1 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | yes | 6 | 0 | 79120 | yes |
| s1(id=2 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | yes | 6 | 0 | 95760 | yes |
| s2(id=3 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | yes | 7 | 24960 | 83600 | yes |
| s3(id=4 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |
| s4(id=5 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | yes | 7 | 0 | 79120 | yes |
| s5(id=6 S3->S1) | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | no | None | None | None | no |
| s6(id=7 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | yes | 7 | 37440 | 79120 | yes |
| s7(id=8 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | yes | 6 | 24960 | 96400 | yes |
| s8(id=9 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | yes | 7 | 74880 | 95760 | yes |
| s9(id=10 S3->S1) | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | yes | 7 | 49920 | 145680 | yes |
| s10(id=11 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |
| s11(id=12 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |
| s12(id=13 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |
| s13(id=14 S3->S1) | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | no | None | None | None | no |
| s14(id=15 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |
| s15(id=16 S3->S1) | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | no | None | None | None | no |
| s16(id=17 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | no | None | None | None | no |
| s17(id=18 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | yes | 7 | 62400 | 95760 | yes |
| s18(id=19 S3->S1) | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | no | None | None | None | no |
| s19(id=20 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | yes | 7 | 49920 | 84240 | yes |

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

## Metrics (training/evaluation signal, not the export)

| metric | value |
|---|---|
| trial-placed flow ratio (fixed + trial-admitted) | 0.900 |
| r1  same-queue window adjacency | 0.328 |
| r2  deadline-violation ratio | 0.000 |
| r3  supplier/receiver overlap | 0.997 |
| r4  mean e2e/deadline (admitted) | 0.297 |
| constraint violations | 0 |

## Constraint check

- C1-C7, C9: OK
- seed-integrity (no SMT-fixed flow's placement changed): OK

## GCL per egress port

### sw01-p2  (17 entries, util 1.5600 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 45760 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 24960 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 5760 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 23680 0xBF # 10111111   Q7
sgs 49280 0x7F # 01111111   Q6
sgs 148160 0x40 # 01000000   Q6
sgs 52480 0x7F # 01111111   Q6
sgs 45760 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 193600 0x40 # 01000000   Q6
sgs 48320 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p4  (29 entries, util 17.1600 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 47040 0x40 # 01000000   Q6
sgs 18240 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 140160 0x40 # 01000000   Q6
sgs 18240 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 102720 0x40 # 01000000   Q6
sgs 18240 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 123520 0x40 # 01000000   Q6
sgs 34880 0xBF # 10111111   Q7
```

### sw02-p2  (28 entries, util 10.9200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 24320 0x80 # 10000000   Q7
sgs 21760 0x7F # 01111111   Q6
sgs 32960 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 16320 0x40 # 01000000   Q6
sgs 38080 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 24320 0x80 # 10000000   Q7
sgs 54720 0x7F # 01111111   Q6
sgs 66240 0x80 # 10000000   Q7
sgs 38080 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 24320 0x80 # 10000000   Q7
sgs 54720 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 16320 0x40 # 01000000   Q6
sgs 38080 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 24320 0x80 # 10000000   Q7
sgs 54720 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 41920 0xBF # 10111111   Q7
```

### sw02-p4  (22 entries, util 12.4800 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 30720 0xBF # 10111111   Q7
sgs 48640 0x40 # 01000000   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 141760 0x40 # 01000000   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 91840 0x80 # 10000000   Q7
sgs 41600 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 125120 0x40 # 01000000   Q6
sgs 58240 0xBF # 10111111   Q7
```

### sw03-p4  (18 entries, util 1.5600 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 24960 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 5760 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 40320 0xBF # 10111111   Q7
sgs 32640 0x7F # 01111111   Q6
sgs 148160 0x40 # 01000000   Q6
sgs 19200 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 210240 0x40 # 01000000   Q6
sgs 48320 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p5  (26 entries, util 17.1600 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 47040 0x40 # 01000000   Q6
sgs 34880 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 140160 0x40 # 01000000   Q6
sgs 34880 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 102720 0x40 # 01000000   Q6
sgs 34880 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 106880 0x40 # 01000000   Q6
sgs 34880 0xBF # 10111111   Q7
```

### sw04-p4  (27 entries, util 10.9200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 24320 0x80 # 10000000   Q7
sgs 38400 0x7F # 01111111   Q6
sgs 16320 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 16320 0x40 # 01000000   Q6
sgs 54720 0x7F # 01111111   Q6
sgs 24320 0x80 # 10000000   Q7
sgs 25920 0xBF # 10111111   Q7
sgs 28800 0x7F # 01111111   Q6
sgs 66240 0x80 # 10000000   Q7
sgs 54720 0x7F # 01111111   Q6
sgs 24320 0x80 # 10000000   Q7
sgs 25920 0xBF # 10111111   Q7
sgs 28800 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 16320 0x40 # 01000000   Q6
sgs 54720 0x7F # 01111111   Q6
sgs 24320 0x80 # 10000000   Q7
sgs 25920 0xBF # 10111111   Q7
sgs 28800 0x7F # 01111111   Q6
sgs 16320 0x80 # 10000000   Q7
sgs 54720 0xBF # 10111111   Q7
```

### sw04-p5  (22 entries, util 12.4800 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 53760 0x7F # 01111111   Q6
sgs 25600 0x40 # 01000000   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 141760 0x40 # 01000000   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 91840 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 108480 0x40 # 01000000   Q6
sgs 58240 0xBF # 10111111   Q7
```

### sw05-p4  (27 entries, util 17.1600 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0x7F # 01111111   Q6
sgs 17920 0xBF # 10111111   Q7
sgs 47040 0x40 # 01000000   Q6
sgs 34880 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 140160 0x40 # 01000000   Q6
sgs 34880 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 102720 0x40 # 01000000   Q6
sgs 34880 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 90240 0x40 # 01000000   Q6
sgs 34880 0xBF # 10111111   Q7
```

### sw05-p5  (18 entries, util 1.5600 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 5760 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 56960 0xBF # 10111111   Q7
sgs 16000 0x7F # 01111111   Q6
sgs 148160 0x40 # 01000000   Q6
sgs 35840 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 226880 0x40 # 01000000   Q6
sgs 48320 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p4  (25 entries, util 12.4800 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 17600 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 640 0x3F # 00111111   BE
sgs 68480 0x40 # 01000000   Q6
sgs 13440 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 136640 0x40 # 01000000   Q6
sgs 13440 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 17600 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 640 0x3F # 00111111   BE
sgs 68480 0x40 # 01000000   Q6
sgs 13440 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 86720 0x40 # 01000000   Q6
sgs 13440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (26 entries, util 10.9200 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 24320 0x80 # 10000000   Q7
sgs 54720 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 16320 0x40 # 01000000   Q6
sgs 21440 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 24320 0x80 # 10000000   Q7
sgs 54720 0xBF # 10111111   Q7
sgs 66240 0x80 # 10000000   Q7
sgs 21440 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 24320 0x80 # 10000000   Q7
sgs 54720 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 16320 0x40 # 01000000   Q6
sgs 21440 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 24320 0x80 # 10000000   Q7
sgs 54720 0xBF # 10111111   Q7
sgs 32960 0x80 # 10000000   Q7
sgs 54720 0xBF # 10111111   Q7
```

### sw07-p4  (16 entries, util 1.5600 %)

```
sgs 45760 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 5760 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 23680 0x7F # 01111111   Q6
sgs 49280 0xBF # 10111111   Q7
sgs 148160 0x40 # 01000000   Q6
sgs 52480 0xBF # 10111111   Q7
sgs 45760 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 243520 0x40 # 01000000   Q6
sgs 48320 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p5  (30 entries, util 17.1600 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 30720 0xBF # 10111111   Q7
sgs 47040 0x40 # 01000000   Q6
sgs 18240 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 140160 0x40 # 01000000   Q6
sgs 18240 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 102720 0x40 # 01000000   Q6
sgs 18240 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 73600 0x40 # 01000000   Q6
sgs 34880 0xBF # 10111111   Q7
```

### sw08-p2  (31 entries, util 26.5200 %)

```
sgs 66560 0x3F # 00111111   BE
sgs 29120 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 10880 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 96000 0x3F # 00111111   BE
sgs 29120 0x40 # 01000000   Q6
sgs 13120 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 145280 0x3F # 00111111   BE
sgs 29120 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 119360 0x3F # 00111111   BE
sgs 29120 0x40 # 01000000   Q6
sgs 13120 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 78720 0x3F # 00111111   BE
```

### sw08-p4  (27 entries, util 10.9200 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 24320 0x80 # 10000000   Q7
sgs 21760 0xBF # 10111111   Q7
sgs 32960 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 16320 0x40 # 01000000   Q6
sgs 38080 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 24320 0x80 # 10000000   Q7
sgs 54720 0xBF # 10111111   Q7
sgs 66240 0x80 # 10000000   Q7
sgs 38080 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 24320 0x80 # 10000000   Q7
sgs 54720 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 16320 0x40 # 01000000   Q6
sgs 38080 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 24320 0x80 # 10000000   Q7
sgs 54720 0xBF # 10111111   Q7
sgs 49600 0x80 # 10000000   Q7
sgs 54720 0xBF # 10111111   Q7
```

### sw08-p5  (17 entries, util 1.5600 %)

```
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 5760 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 40320 0x7F # 01111111   Q6
sgs 32640 0xBF # 10111111   Q7
sgs 148160 0x40 # 01000000   Q6
sgs 19200 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 260160 0x40 # 01000000   Q6
sgs 48320 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

