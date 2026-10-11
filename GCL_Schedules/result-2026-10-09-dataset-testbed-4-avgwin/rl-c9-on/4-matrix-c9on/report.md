# RL-enlarged GCL schedule (Problem 2: window enlargement)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Seeded from SMT run: **result/result-2026-10-09-dataset-testbed-4-avgwin/smt-c9-on/4-fair-retimed-c9on**

## Admission (unchanged) vs. capacity grown

Problem 2 never admits a flow into the schedule it exports -- it only widens windows. `admitted` below is exactly the SMT baseline, by construction; the capacity growth this run achieved is banked slack and per-port GCL entries, reported separately.

| | admitted | of total |
|---|---|---|
| SMT (fixed, never moved) | 11 | 11 |
| RL-enlarged (exported; grow-only, admits nothing new) | 11 | 20 |

During training, the policy's trial admissions (the reward signal that teaches it how much a window needs to grow) reached **6** of the 9 SMT-rejected flows -- none of those are kept in this export; that capacity stays as empty, banked slack for Problem 3 to fill. Total slack banked: 0 ns. GCL_size overflow: 0.

## Opportunistic idle top-up (deterministic post-pass)

**9544320 ns**, drawn from idle capacity on ports at or below utilisation 0.2, independent of what training happened to grow. Ported from prob_2_heuristic_enlarged's Step 7.

| port | queue | applied (ns) |
|---|---|---|
| S1-p0 | Q6 | 112640 |
| S1-p0 | Q7 | 550080 |
| S2-p0 | Q6 | 137600 |
| S2-p0 | Q7 | 487680 |
| S3-p0 | Q6 | 262720 |
| S3-p0 | Q7 | 350080 |
| sw01-p4 | Q6 | 117760 |
| sw01-p4 | Q7 | 490560 |
| sw02-p2 | Q6 | 261120 |
| sw02-p2 | Q7 | 409920 |
| sw02-p4 | Q6 | 112640 |
| sw02-p4 | Q7 | 545920 |
| sw03-p5 | Q6 | 118400 |
| sw03-p5 | Q7 | 485760 |
| sw04-p4 | Q6 | 261120 |
| sw04-p4 | Q7 | 414080 |
| sw04-p5 | Q6 | 112640 |
| sw04-p5 | Q7 | 541760 |
| sw05-p4 | Q6 | 119040 |
| sw05-p4 | Q7 | 480960 |
| sw06-p4 | Q6 | 112640 |
| sw06-p4 | Q7 | 537600 |
| sw06-p5 | Q6 | 261120 |
| sw06-p5 | Q7 | 418240 |
| sw07-p5 | Q6 | 128000 |
| sw07-p5 | Q7 | 459520 |
| sw08-p2 | Q6 | 140800 |
| sw08-p2 | Q7 | 430400 |
| sw08-p4 | Q6 | 261120 |
| sw08-p4 | Q7 | 422400 |

## Best-effort gap equalization (deterministic post-pass)

**5443200 ns** given back from the top-up/creation above so each port's leftover non-TAS gaps land close to equal. Ported from prob_2_heuristic_enlarged's Step 9.

| port | given back (ns) |
|---|---|---|
| sw02-p2 | 421760 |
| sw04-p4 | 421760 |
| sw06-p5 | 421760 |
| sw08-p4 | 421760 |
| sw05-p4 | 379200 |
| sw03-p5 | 378880 |
| sw01-p4 | 378560 |
| sw07-p5 | 362880 |
| S3-p0 | 360960 |
| S2-p0 | 336320 |
| sw04-p5 | 320320 |
| sw06-p4 | 320320 |
| sw02-p4 | 319360 |
| S1-p0 | 319360 |
| sw08-p2 | 280000 |

## Opportunistic overlay window creation (deterministic post-pass)

**30** new overlay window(s), **5330240 ns** total, carved out of already-open best-effort spans on ports at or below utilisation 0.2 -- best-effort stays reachable inside each one (gate mask keeps its BE bits set). Run once after training/finalize_grow_only(), not a trained action.

| port | queue | size (ns) |
|---|---|---|
| S1-p0 | Q6 | 62400 |
| S1-p0 | Q7 | 256960 |
| S2-p0 | Q6 | 124160 |
| S2-p0 | Q7 | 212160 |
| S3-p0 | Q6 | 161280 |
| S3-p0 | Q7 | 199680 |
| sw01-p4 | Q6 | 43520 |
| sw01-p4 | Q7 | 280960 |
| sw02-p2 | Q6 | 153920 |
| sw02-p2 | Q7 | 282880 |
| sw02-p4 | Q6 | 49920 |
| sw02-p4 | Q7 | 269440 |
| sw03-p5 | Q6 | 34560 |
| sw03-p5 | Q7 | 289920 |
| sw04-p4 | Q6 | 199680 |
| sw04-p4 | Q7 | 232960 |
| sw04-p5 | Q6 | 51200 |
| sw04-p5 | Q7 | 256960 |
| sw05-p4 | Q6 | 76800 |
| sw05-p4 | Q7 | 260480 |
| sw06-p4 | Q6 | 101120 |
| sw06-p4 | Q7 | 219520 |
| sw06-p5 | Q6 | 203840 |
| sw06-p5 | Q7 | 224640 |
| sw07-p5 | Q6 | 101120 |
| sw07-p5 | Q7 | 273600 |
| sw08-p2 | Q6 | 66560 |
| sw08-p2 | Q7 | 215680 |
| sw08-p4 | Q6 | 224640 |
| sw08-p4 | Q7 | 199680 |

## Per-port GCL entries: before (SMT) vs. after (RL-enlarged)

| port | SMT entries | RL-enlarged entries | GCL_size |
|---|---|---|---|
| sw01-p2 | 29 | 27 | 255 |
| sw01-p4 | 17 | 29 | 255 |
| sw02-p2 | 3 | 21 | 255 |
| sw02-p4 | 21 | 21 | 255 |
| sw03-p4 | 29 | 27 | 255 |
| sw03-p5 | 17 | 29 | 255 |
| sw04-p4 | 3 | 26 | 255 |
| sw04-p5 | 21 | 19 | 255 |
| sw05-p4 | 17 | 32 | 255 |
| sw05-p5 | 29 | 27 | 255 |
| sw06-p4 | 21 | 22 | 255 |
| sw06-p5 | 3 | 26 | 255 |
| sw07-p4 | 29 | 27 | 255 |
| sw07-p5 | 17 | 30 | 255 |
| sw08-p2 | 25 | 30 | 255 |
| sw08-p4 | 3 | 24 | 255 |
| sw08-p5 | 29 | 27 | 255 |

## Flows

| flow | route | fixed | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|---|
| s0(id=1 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | yes | 6 | 24960 | 33360 | yes |
| s1(id=2 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | no | None | None | None | no |
| s2(id=3 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | yes | 7 | 24960 | 33360 | yes |
| s3(id=4 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | no | None | None | None | no |
| s4(id=5 S3->S1) | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | no | None | None | None | no |
| s5(id=6 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | yes | 7 | 49920 | 46800 | yes |
| s6(id=7 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |
| s7(id=8 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | yes | 7 | 0 | 33360 | yes |
| s8(id=9 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | yes | 6 | 74880 | 45840 | yes |
| s9(id=10 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | yes | 6 | 49920 | 33360 | yes |
| s10(id=11 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | no | None | None | None | no |
| s11(id=12 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |
| s12(id=13 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | yes | 7 | 0 | 29200 | yes |
| s13(id=14 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | yes | 7 | 0 | 42000 | yes |
| s14(id=15 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | no | None | None | None | no |
| s15(id=16 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | no | None | None | None | no |
| s16(id=17 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | no | None | None | None | no |
| s17(id=18 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | yes | 7 | 74880 | 29200 | yes |
| s18(id=19 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | yes | 6 | 49920 | 34000 | yes |
| s19(id=20 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | yes | 7 | 24960 | 46160 | yes |

## Per-hop windows (slack_ns > 0 means this window was enlarged)

| flow | egress port | queue | psi (ns) | delta (ns) |
|---|---|---|---|---|
| s0(id=1 S3->S2) | S3-p0 | Q6 | 24960 | 12480 |
| s0(id=1 S3->S2) | sw01-p4 | Q6 | 29120 | 12480 |
| s0(id=1 S3->S2) | sw03-p5 | Q6 | 33280 | 12480 |
| s0(id=1 S3->S2) | sw05-p4 | Q6 | 37440 | 12480 |
| s0(id=1 S3->S2) | sw07-p5 | Q6 | 41600 | 12480 |
| s0(id=1 S3->S2) | sw08-p2 | Q6 | 45760 | 12480 |
| s2(id=3 S2->S3) | S2-p0 | Q7 | 24960 | 12480 |
| s2(id=3 S2->S3) | sw08-p5 | Q7 | 29120 | 12480 |
| s2(id=3 S2->S3) | sw07-p4 | Q7 | 33280 | 12480 |
| s2(id=3 S2->S3) | sw05-p5 | Q7 | 37440 | 12480 |
| s2(id=3 S2->S3) | sw03-p4 | Q7 | 41600 | 12480 |
| s2(id=3 S2->S3) | sw01-p2 | Q7 | 45760 | 12480 |
| s5(id=6 S1->S3) | S1-p0 | Q7 | 49920 | 12480 |
| s5(id=6 S1->S3) | sw02-p4 | Q7 | 54080 | 12480 |
| s5(id=6 S1->S3) | sw04-p5 | Q7 | 58240 | 12480 |
| s5(id=6 S1->S3) | sw06-p4 | Q7 | 62400 | 12480 |
| s5(id=6 S1->S3) | sw08-p5 | Q7 | 67520 | 12480 |
| s5(id=6 S1->S3) | sw07-p4 | Q7 | 71680 | 12480 |
| s5(id=6 S1->S3) | sw05-p5 | Q7 | 75840 | 12480 |
| s5(id=6 S1->S3) | sw03-p4 | Q7 | 80000 | 12480 |
| s5(id=6 S1->S3) | sw01-p2 | Q7 | 84160 | 12480 |
| s7(id=8 S2->S3) | S2-p0 | Q7 | 0 | 12480 |
| s7(id=8 S2->S3) | sw08-p5 | Q7 | 4160 | 12480 |
| s7(id=8 S2->S3) | sw07-p4 | Q7 | 8320 | 12480 |
| s7(id=8 S2->S3) | sw05-p5 | Q7 | 12480 | 12480 |
| s7(id=8 S2->S3) | sw03-p4 | Q7 | 16640 | 12480 |
| s7(id=8 S2->S3) | sw01-p2 | Q7 | 20800 | 12480 |
| s8(id=9 S1->S3) | S1-p0 | Q6 | 74880 | 12480 |
| s8(id=9 S1->S3) | sw02-p4 | Q6 | 79040 | 12480 |
| s8(id=9 S1->S3) | sw04-p5 | Q6 | 83200 | 12480 |
| s8(id=9 S1->S3) | sw06-p4 | Q6 | 87360 | 12480 |
| s8(id=9 S1->S3) | sw08-p5 | Q6 | 91520 | 12480 |
| s8(id=9 S1->S3) | sw07-p4 | Q6 | 95680 | 12480 |
| s8(id=9 S1->S3) | sw05-p5 | Q6 | 99840 | 12480 |
| s8(id=9 S1->S3) | sw03-p4 | Q6 | 104000 | 12480 |
| s8(id=9 S1->S3) | sw01-p2 | Q6 | 108160 | 12480 |
| s9(id=10 S3->S2) | S3-p0 | Q6 | 49920 | 12480 |
| s9(id=10 S3->S2) | sw01-p4 | Q6 | 54080 | 12480 |
| s9(id=10 S3->S2) | sw03-p5 | Q6 | 58240 | 12480 |
| s9(id=10 S3->S2) | sw05-p4 | Q6 | 62400 | 12480 |
| s9(id=10 S3->S2) | sw07-p5 | Q6 | 66560 | 12480 |
| s9(id=10 S3->S2) | sw08-p2 | Q6 | 70720 | 12480 |
| s12(id=13 S1->S2) | S1-p0 | Q7 | 0 | 12480 |
| s12(id=13 S1->S2) | sw02-p4 | Q7 | 4160 | 12480 |
| s12(id=13 S1->S2) | sw04-p5 | Q7 | 8320 | 12480 |
| s12(id=13 S1->S2) | sw06-p4 | Q7 | 12480 | 12480 |
| s12(id=13 S1->S2) | sw08-p2 | Q7 | 16640 | 12480 |
| s13(id=14 S3->S2) | S3-p0 | Q7 | 0 | 12480 |
| s13(id=14 S3->S2) | sw01-p4 | Q7 | 4480 | 12480 |
| s13(id=14 S3->S2) | sw03-p5 | Q7 | 8640 | 12480 |
| s13(id=14 S3->S2) | sw05-p4 | Q7 | 12800 | 12480 |
| s13(id=14 S3->S2) | sw07-p5 | Q7 | 25280 | 12480 |
| s13(id=14 S3->S2) | sw08-p2 | Q7 | 29440 | 12480 |
| s17(id=18 S2->S1) | S2-p0 | Q7 | 74880 | 12480 |
| s17(id=18 S2->S1) | sw08-p4 | Q7 | 79040 | 12480 |
| s17(id=18 S2->S1) | sw06-p5 | Q7 | 83200 | 12480 |
| s17(id=18 S2->S1) | sw04-p4 | Q7 | 87360 | 12480 |
| s17(id=18 S2->S1) | sw02-p2 | Q7 | 91520 | 12480 |
| s18(id=19 S2->S3) | S2-p0 | Q6 | 49920 | 12480 |
| s18(id=19 S2->S3) | sw08-p5 | Q6 | 54720 | 12480 |
| s18(id=19 S2->S3) | sw07-p4 | Q6 | 58880 | 12480 |
| s18(id=19 S2->S3) | sw05-p5 | Q6 | 63040 | 12480 |
| s18(id=19 S2->S3) | sw03-p4 | Q6 | 67200 | 12480 |
| s18(id=19 S2->S3) | sw01-p2 | Q6 | 71360 | 12480 |
| s19(id=20 S1->S3) | S1-p0 | Q7 | 24960 | 12480 |
| s19(id=20 S1->S3) | sw02-p4 | Q7 | 29120 | 12480 |
| s19(id=20 S1->S3) | sw04-p5 | Q7 | 33600 | 12480 |
| s19(id=20 S1->S3) | sw06-p4 | Q7 | 37760 | 12480 |
| s19(id=20 S1->S3) | sw08-p5 | Q7 | 41920 | 12480 |
| s19(id=20 S1->S3) | sw07-p4 | Q7 | 46080 | 12480 |
| s19(id=20 S1->S3) | sw05-p5 | Q7 | 50240 | 12480 |
| s19(id=20 S1->S3) | sw03-p4 | Q7 | 54400 | 12480 |
| s19(id=20 S1->S3) | sw01-p2 | Q7 | 58560 | 12480 |

## Metrics (training/evaluation signal, not the export)

| metric | value |
|---|---|
| trial-placed flow ratio (fixed + trial-admitted) | 0.850 |
| r1  same-queue window adjacency | 0.524 |
| r2  deadline-violation ratio | 0.000 |
| r3  supplier/receiver overlap | 0.997 |
| r4  mean e2e/deadline (admitted) | 0.131 |
| constraint violations | 0 |

## Constraint check

- C1-C7, C9: OK
- seed-integrity (no SMT-fixed flow's placement changed): OK

## GCL per egress port

### sw01-p2  (27 entries, util 21.8400 %)

```
sgs 20800 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 11520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 81920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 149760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 136960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 128960 0x3F # 00111111   BE
```

### sw01-p4  (29 entries, util 12.4800 %)

```
sgs 4480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 11520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 6720 0x3F # 00111111   BE
sgs 57280 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 23680 0x80 # 10000000   Q7
sgs 21760 0x7F # 01111111   Q6
sgs 28160 0xBF # 10111111   Q7
sgs 76480 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 11520 0x3F # 00111111   BE
sgs 76480 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
sgs 23680 0x80 # 10000000   Q7
sgs 21760 0x7F # 01111111   Q6
sgs 28160 0xBF # 10111111   Q7
sgs 72000 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (21 entries, util 1.5600 %)

```
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 29120 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 5760 0x3F # 00111111   BE
sgs 32000 0x40 # 01000000   Q6
sgs 58240 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 112640 0x80 # 10000000   Q7
sgs 58240 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 29120 0xBF # 10111111   Q7
sgs 71040 0x40 # 01000000   Q6
sgs 58240 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 83520 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p4  (21 entries, util 15.6000 %)

```
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 64000 0x40 # 01000000   Q6
sgs 61120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 113920 0x80 # 10000000   Q7
sgs 61120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 113920 0x80 # 10000000   Q7
sgs 61120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 109760 0x80 # 10000000   Q7
sgs 61120 0xBF # 10111111   Q7
```

### sw03-p4  (27 entries, util 21.8400 %)

```
sgs 16640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 11520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 81920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 149760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 136960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 133120 0x3F # 00111111   BE
```

### sw03-p5  (29 entries, util 12.4800 %)

```
sgs 8640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 11840 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 6400 0x3F # 00111111   BE
sgs 57280 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 24000 0x80 # 10000000   Q7
sgs 17280 0x7F # 01111111   Q6
sgs 32640 0xBF # 10111111   Q7
sgs 76160 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 11840 0x3F # 00111111   BE
sgs 76160 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
sgs 24000 0x80 # 10000000   Q7
sgs 17280 0x7F # 01111111   Q6
sgs 32640 0xBF # 10111111   Q7
sgs 67520 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p4  (26 entries, util 1.5600 %)

```
sgs 24960 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 5760 0x3F # 00111111   BE
sgs 32000 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 112640 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 71040 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 87680 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (19 entries, util 15.6000 %)

```
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0x7F # 01111111   Q6
sgs 37120 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 64000 0x40 # 01000000   Q6
sgs 61120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0x7F # 01111111   Q6
sgs 113600 0x80 # 10000000   Q7
sgs 61120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0x7F # 01111111   Q6
sgs 113600 0x80 # 10000000   Q7
sgs 61120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0x7F # 01111111   Q6
sgs 105280 0x80 # 10000000   Q7
sgs 61120 0xBF # 10111111   Q7
```

### sw05-p4  (32 entries, util 12.4800 %)

```
sgs 12800 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 6080 0x3F # 00111111   BE
sgs 57280 0x40 # 01000000   Q6
sgs 37120 0xBF # 10111111   Q7
sgs 12800 0x7F # 01111111   Q6
sgs 24320 0x80 # 10000000   Q7
sgs 12800 0x7F # 01111111   Q6
sgs 37120 0xBF # 10111111   Q7
sgs 75840 0x80 # 10000000   Q7
sgs 37120 0xBF # 10111111   Q7
sgs 12800 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12160 0x3F # 00111111   BE
sgs 75840 0x80 # 10000000   Q7
sgs 37120 0xBF # 10111111   Q7
sgs 12800 0x7F # 01111111   Q6
sgs 24320 0x80 # 10000000   Q7
sgs 12800 0x7F # 01111111   Q6
sgs 37120 0xBF # 10111111   Q7
sgs 63040 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p5  (27 entries, util 21.8400 %)

```
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 11520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 81920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 149760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 136960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 137280 0x3F # 00111111   BE
```

### sw06-p4  (22 entries, util 15.6000 %)

```
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0x7F # 01111111   Q6
sgs 37120 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 64000 0x40 # 01000000   Q6
sgs 48640 0xBF # 10111111   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0x7F # 01111111   Q6
sgs 113600 0x80 # 10000000   Q7
sgs 48640 0xBF # 10111111   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0x7F # 01111111   Q6
sgs 113600 0x80 # 10000000   Q7
sgs 48640 0xBF # 10111111   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0x7F # 01111111   Q6
sgs 101120 0x80 # 10000000   Q7
sgs 61120 0xBF # 10111111   Q7
```

### sw06-p5  (26 entries, util 1.5600 %)

```
sgs 20800 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 5760 0x3F # 00111111   BE
sgs 32000 0x40 # 01000000   Q6
sgs 16640 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 112640 0x80 # 10000000   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 71040 0x40 # 01000000   Q6
sgs 16640 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 91840 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (27 entries, util 21.8400 %)

```
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 11520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 81920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 149760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 136960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 141440 0x3F # 00111111   BE
```

### sw07-p5  (30 entries, util 12.4800 %)

```
sgs 25280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 3840 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 5760 0x3F # 00111111   BE
sgs 65600 0x40 # 01000000   Q6
sgs 24640 0xBF # 10111111   Q7
sgs 25280 0x7F # 01111111   Q6
sgs 16320 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
sgs 83840 0x80 # 10000000   Q7
sgs 24640 0xBF # 10111111   Q7
sgs 25280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 3840 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 83840 0x80 # 10000000   Q7
sgs 24640 0xBF # 10111111   Q7
sgs 25280 0x7F # 01111111   Q6
sgs 16320 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
sgs 58560 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p2  (30 entries, util 18.7200 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 25280 0x80 # 10000000   Q7
sgs 3840 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12800 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 5440 0x3F # 00111111   BE
sgs 66880 0x40 # 01000000   Q6
sgs 19200 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 43520 0x80 # 10000000   Q7
sgs 35840 0xBF # 10111111   Q7
sgs 84800 0x80 # 10000000   Q7
sgs 19200 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 25280 0x80 # 10000000   Q7
sgs 3840 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12800 0xBF # 10111111   Q7
sgs 84800 0x80 # 10000000   Q7
sgs 19200 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 43520 0x80 # 10000000   Q7
sgs 35840 0xBF # 10111111   Q7
sgs 68160 0x80 # 10000000   Q7
sgs 35840 0xBF # 10111111   Q7
```

### sw08-p4  (24 entries, util 1.5600 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 5760 0x3F # 00111111   BE
sgs 32000 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 112640 0x80 # 10000000   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 71040 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 96000 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (27 entries, util 21.8400 %)

```
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 11520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 81920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 149760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 136960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 145600 0x3F # 00111111   BE
```

