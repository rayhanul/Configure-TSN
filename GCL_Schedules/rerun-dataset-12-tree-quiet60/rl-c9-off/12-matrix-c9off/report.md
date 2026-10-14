# RL-enlarged GCL schedule (Problem 2: window enlargement)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Seeded from SMT run: **result/result-2026-10-13-dataset-testbed-12-tree-avgwin/smt-c9-off/12-t3600-c9off-minlat**

## Admission (unchanged) vs. capacity grown

Problem 2 never admits a flow into the schedule it exports -- it only widens windows. `admitted` below is exactly the SMT baseline, by construction; the capacity growth this run achieved is banked slack and per-port GCL entries, reported separately.

| | admitted | of total |
|---|---|---|
| SMT (fixed, never moved) | 11 | 20 |
| RL-enlarged (exported; grow-only, admits nothing new) | 11 | 20 |

During training, the policy's trial admissions (the reward signal that teaches it how much a window needs to grow) reached **4** of the 9 SMT-rejected flows -- none of those are kept in this export; that capacity stays as empty, banked slack for Problem 3 to fill. Total slack banked: 35840 ns. GCL_size overflow: 0.

## Opportunistic idle top-up (deterministic post-pass)

**12482240 ns**, drawn from idle capacity on ports at or below utilisation 0.2, independent of what training happened to grow. Ported from prob_2_heuristic_enlarged's Step 7.

| port | queue | applied (ns) |
|---|---|---|
| S1-p0 | Q6 | 87680 |
| S1-p0 | Q7 | 562560 |
| S2-p0 | Q6 | 287680 |
| S2-p0 | Q7 | 350080 |
| S3-p0 | Q6 | 137600 |
| S3-p0 | Q7 | 550080 |
| sw01-p2 | Q6 | 100800 |
| sw01-p2 | Q7 | 428800 |
| sw01-p4 | Q6 | 137600 |
| sw01-p4 | Q7 | 533440 |
| sw02-p2 | Q6 | 592000 |
| sw02-p2 | Q7 | 66560 |
| sw02-p4 | Q6 | 87680 |
| sw02-p4 | Q7 | 545920 |
| sw03-p4 | Q6 | 100800 |
| sw03-p4 | Q7 | 445440 |
| sw03-p5 | Q6 | 137600 |
| sw03-p5 | Q7 | 516800 |
| sw04-p4 | Q6 | 608640 |
| sw04-p4 | Q7 | 66560 |
| sw04-p5 | Q6 | 87680 |
| sw04-p5 | Q7 | 529280 |
| sw05-p4 | Q6 | 137600 |
| sw05-p4 | Q7 | 500160 |
| sw05-p5 | Q6 | 100800 |
| sw05-p5 | Q7 | 462080 |
| sw06-p4 | Q6 | 87680 |
| sw06-p4 | Q7 | 512640 |
| sw06-p5 | Q6 | 625280 |
| sw06-p5 | Q7 | 66560 |
| sw07-p4 | Q6 | 100800 |
| sw07-p4 | Q7 | 478720 |
| sw07-p5 | Q6 | 48960 |
| sw07-p5 | Q7 | 572160 |
| sw08-p2 | Q6 | 640 |
| sw08-p2 | Q7 | 522240 |
| sw08-p4 | Q6 | 641920 |
| sw08-p4 | Q7 | 66560 |
| sw08-p5 | Q6 | 100800 |
| sw08-p5 | Q7 | 495360 |

## Best-effort gap equalization (deterministic post-pass)

**7064320 ns** given back from the top-up/creation above so each port's leftover non-TAS gaps land close to equal. Ported from prob_2_heuristic_enlarged's Step 9.

| port | given back (ns) |
|---|---|---|
| sw02-p2 | 472640 |
| sw04-p4 | 472640 |
| sw06-p5 | 472640 |
| sw08-p4 | 472640 |
| sw05-p5 | 384320 |
| sw07-p4 | 384320 |
| sw08-p5 | 384320 |
| sw03-p4 | 382720 |
| sw01-p2 | 366080 |
| sw07-p5 | 358080 |
| sw01-p4 | 309120 |
| sw03-p5 | 309120 |
| sw05-p4 | 309120 |
| S3-p0 | 309120 |
| sw04-p5 | 300480 |
| sw06-p4 | 300480 |
| sw02-p4 | 299840 |
| S1-p0 | 299520 |
| sw08-p2 | 241920 |
| S2-p0 | 235200 |

## Opportunistic overlay window creation (deterministic post-pass)

**39** new overlay window(s), **7814400 ns** total, carved out of already-open best-effort spans on ports at or below utilisation 0.2 -- best-effort stays reachable inside each one (gate mask keeps its BE bits set). Run once after training/finalize_grow_only(), not a trained action.

| port | queue | size (ns) |
|---|---|---|
| S1-p0 | Q6 | 74880 |
| S1-p0 | Q7 | 224640 |
| S2-p0 | Q7 | 235200 |
| S3-p0 | Q6 | 109440 |
| S3-p0 | Q7 | 199680 |
| sw01-p2 | Q6 | 207360 |
| sw01-p2 | Q7 | 254080 |
| sw01-p4 | Q6 | 112640 |
| sw01-p4 | Q7 | 213120 |
| sw02-p2 | Q6 | 291200 |
| sw02-p2 | Q7 | 248000 |
| sw02-p4 | Q6 | 128960 |
| sw02-p4 | Q7 | 175360 |
| sw03-p4 | Q6 | 262080 |
| sw03-p4 | Q7 | 199360 |
| sw03-p5 | Q6 | 154240 |
| sw03-p5 | Q7 | 188160 |
| sw04-p4 | Q6 | 303360 |
| sw04-p4 | Q7 | 219200 |
| sw04-p5 | Q6 | 145600 |
| sw04-p5 | Q7 | 176000 |
| sw05-p4 | Q6 | 220800 |
| sw05-p4 | Q7 | 138240 |
| sw05-p5 | Q6 | 241920 |
| sw05-p5 | Q7 | 204480 |
| sw06-p4 | Q6 | 212160 |
| sw06-p4 | Q7 | 126080 |
| sw06-p5 | Q6 | 276480 |
| sw06-p5 | Q7 | 229440 |
| sw07-p4 | Q6 | 224960 |
| sw07-p4 | Q7 | 204800 |
| sw07-p5 | Q6 | 277440 |
| sw07-p5 | Q7 | 141440 |
| sw08-p2 | Q6 | 174720 |
| sw08-p2 | Q7 | 116480 |
| sw08-p4 | Q6 | 251520 |
| sw08-p4 | Q7 | 237760 |
| sw08-p5 | Q6 | 153600 |
| sw08-p5 | Q7 | 259520 |

## Per-port GCL entries: before (SMT) vs. after (RL-enlarged)

| port | SMT entries | RL-enlarged entries | GCL_size |
|---|---|---|---|
| sw01-p2 | 15 | 27 | 255 |
| sw01-p4 | 15 | 20 | 255 |
| sw02-p2 | 13 | 21 | 255 |
| sw02-p4 | 25 | 26 | 255 |
| sw03-p4 | 15 | 30 | 255 |
| sw03-p5 | 15 | 20 | 255 |
| sw04-p4 | 13 | 18 | 255 |
| sw04-p5 | 25 | 26 | 255 |
| sw05-p4 | 15 | 20 | 255 |
| sw05-p5 | 15 | 34 | 255 |
| sw06-p4 | 25 | 23 | 255 |
| sw06-p5 | 13 | 20 | 255 |
| sw07-p4 | 15 | 26 | 255 |
| sw07-p5 | 15 | 24 | 255 |
| sw08-p2 | 25 | 21 | 255 |
| sw08-p4 | 13 | 20 | 255 |
| sw08-p5 | 15 | 29 | 255 |

## Flows

| flow | route | fixed | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|---|
| s0(id=1 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | no | None | None | None | no |
| s1(id=2 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | yes | 7 | 0 | 79120 | yes |
| s2(id=3 S3->S1) | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | no | None | None | None | no |
| s3(id=4 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | yes | 7 | 74880 | 145680 | yes |
| s4(id=5 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | yes | 7 | 0 | 95760 | yes |
| s5(id=6 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |
| s6(id=7 S3->S1) | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | yes | 6 | 49920 | 145680 | yes |
| s7(id=8 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | yes | 6 | 0 | 79120 | yes |
| s8(id=9 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | yes | 6 | 24960 | 95760 | yes |
| s9(id=10 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |
| s10(id=11 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | yes | 7 | 37440 | 79120 | yes |
| s11(id=12 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | yes | 7 | 24960 | 146000 | yes |
| s12(id=13 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |
| s13(id=14 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | yes | 7 | 49920 | 83600 | yes |
| s14(id=15 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |
| s15(id=16 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | no | None | None | None | no |
| s16(id=17 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | no | None | None | None | no |
| s17(id=18 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | yes | 6 | 62400 | 95760 | yes |
| s18(id=19 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | yes | 6 | 99840 | 145680 | yes |
| s19(id=20 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |

## Per-hop windows (slack_ns > 0 means this window was enlarged)

| flow | egress port | queue | psi (ns) | delta (ns) |
|---|---|---|---|---|
| s1(id=2 S1->S2) | S1-p0 | Q7 | 0 | 12480 |
| s1(id=2 S1->S2) | sw02-p4 | Q7 | 16640 | 12480 |
| s1(id=2 S1->S2) | sw04-p5 | Q7 | 33280 | 12480 |
| s1(id=2 S1->S2) | sw06-p4 | Q7 | 49920 | 12480 |
| s1(id=2 S1->S2) | sw08-p2 | Q7 | 66560 | 12480 |
| s3(id=4 S1->S3) | S1-p0 | Q7 | 74880 | 12480 |
| s3(id=4 S1->S3) | sw02-p4 | Q7 | 91520 | 12480 |
| s3(id=4 S1->S3) | sw04-p5 | Q7 | 108160 | 12480 |
| s3(id=4 S1->S3) | sw06-p4 | Q7 | 124800 | 12480 |
| s3(id=4 S1->S3) | sw08-p5 | Q7 | 141440 | 12480 |
| s3(id=4 S1->S3) | sw07-p4 | Q7 | 158080 | 12480 |
| s3(id=4 S1->S3) | sw05-p5 | Q7 | 174720 | 12480 |
| s3(id=4 S1->S3) | sw03-p4 | Q7 | 191360 | 12480 |
| s3(id=4 S1->S3) | sw01-p2 | Q7 | 208000 | 12480 |
| s4(id=5 S3->S2) | S3-p0 | Q7 | 0 | 12480 |
| s4(id=5 S3->S2) | sw01-p4 | Q7 | 16640 | 12480 |
| s4(id=5 S3->S2) | sw03-p5 | Q7 | 33280 | 12480 |
| s4(id=5 S3->S2) | sw05-p4 | Q7 | 49920 | 12480 |
| s4(id=5 S3->S2) | sw07-p5 | Q7 | 66560 | 12480 |
| s4(id=5 S3->S2) | sw08-p2 | Q7 | 83200 | 12480 |
| s6(id=7 S3->S1) | S3-p0 | Q6 | 49920 | 12480 |
| s6(id=7 S3->S1) | sw01-p4 | Q6 | 66560 | 12480 |
| s6(id=7 S3->S1) | sw03-p5 | Q6 | 83200 | 12480 |
| s6(id=7 S3->S1) | sw05-p4 | Q6 | 99840 | 12480 |
| s6(id=7 S3->S1) | sw07-p5 | Q6 | 116480 | 12480 |
| s6(id=7 S3->S1) | sw08-p4 | Q6 | 133120 | 12480 |
| s6(id=7 S3->S1) | sw06-p5 | Q6 | 149760 | 12480 |
| s6(id=7 S3->S1) | sw04-p4 | Q6 | 166400 | 12480 |
| s6(id=7 S3->S1) | sw02-p2 | Q6 | 183040 | 12480 |
| s7(id=8 S2->S1) | S2-p0 | Q6 | 0 | 12480 |
| s7(id=8 S2->S1) | sw08-p4 | Q6 | 16640 | 12480 |
| s7(id=8 S2->S1) | sw06-p5 | Q6 | 33280 | 12480 |
| s7(id=8 S2->S1) | sw04-p4 | Q6 | 49920 | 12480 |
| s7(id=8 S2->S1) | sw02-p2 | Q6 | 66560 | 12480 |
| s8(id=9 S3->S2) | S3-p0 | Q6 | 24960 | 12480 |
| s8(id=9 S3->S2) | sw01-p4 | Q6 | 41600 | 12480 |
| s8(id=9 S3->S2) | sw03-p5 | Q6 | 58240 | 12480 |
| s8(id=9 S3->S2) | sw05-p4 | Q6 | 74880 | 12480 |
| s8(id=9 S3->S2) | sw07-p5 | Q6 | 91520 | 12480 |
| s8(id=9 S3->S2) | sw08-p2 | Q6 | 108160 | 12480 |
| s10(id=11 S2->S1) | S2-p0 | Q7 | 37440 | 12480 |
| s10(id=11 S2->S1) | sw08-p4 | Q7 | 54080 | 12480 |
| s10(id=11 S2->S1) | sw06-p5 | Q7 | 70720 | 12480 |
| s10(id=11 S2->S1) | sw04-p4 | Q7 | 87360 | 12480 |
| s10(id=11 S2->S1) | sw02-p2 | Q7 | 104000 | 12480 |
| s11(id=12 S1->S3) | S1-p0 | Q7 | 24960 | 12480 |
| s11(id=12 S1->S3) | sw02-p4 | Q7 | 41600 | 12480 |
| s11(id=12 S1->S3) | sw04-p5 | Q7 | 58560 | 12480 |
| s11(id=12 S1->S3) | sw06-p4 | Q7 | 75200 | 12480 |
| s11(id=12 S1->S3) | sw08-p5 | Q7 | 91840 | 12480 |
| s11(id=12 S1->S3) | sw07-p4 | Q7 | 108480 | 12480 |
| s11(id=12 S1->S3) | sw05-p5 | Q7 | 125120 | 12480 |
| s11(id=12 S1->S3) | sw03-p4 | Q7 | 141760 | 12480 |
| s11(id=12 S1->S3) | sw01-p2 | Q7 | 158400 | 12480 |
| s13(id=14 S1->S2) | S1-p0 | Q7 | 49920 | 12480 |
| s13(id=14 S1->S2) | sw02-p4 | Q7 | 66880 | 12480 |
| s13(id=14 S1->S2) | sw04-p5 | Q7 | 83520 | 12480 |
| s13(id=14 S1->S2) | sw06-p4 | Q7 | 100160 | 12480 |
| s13(id=14 S1->S2) | sw08-p2 | Q7 | 120960 | 12480 |
| s17(id=18 S2->S3) | S2-p0 | Q6 | 62400 | 12480 |
| s17(id=18 S2->S3) | sw08-p5 | Q6 | 79040 | 12480 |
| s17(id=18 S2->S3) | sw07-p4 | Q6 | 95680 | 12480 |
| s17(id=18 S2->S3) | sw05-p5 | Q6 | 112320 | 12480 |
| s17(id=18 S2->S3) | sw03-p4 | Q6 | 128960 | 12480 |
| s17(id=18 S2->S3) | sw01-p2 | Q6 | 145600 | 12480 |
| s18(id=19 S1->S3) | S1-p0 | Q6 | 99840 | 12480 |
| s18(id=19 S1->S3) | sw02-p4 | Q6 | 116480 | 12480 |
| s18(id=19 S1->S3) | sw04-p5 | Q6 | 133120 | 12480 |
| s18(id=19 S1->S3) | sw06-p4 | Q6 | 149760 | 12480 |
| s18(id=19 S1->S3) | sw08-p5 | Q6 | 166400 | 12480 |
| s18(id=19 S1->S3) | sw07-p4 | Q6 | 183040 | 12480 |
| s18(id=19 S1->S3) | sw05-p5 | Q6 | 199680 | 12480 |
| s18(id=19 S1->S3) | sw03-p4 | Q6 | 216320 | 12480 |
| s18(id=19 S1->S3) | sw01-p2 | Q6 | 232960 | 12480 |

## Metrics (training/evaluation signal, not the export)

| metric | value |
|---|---|
| trial-placed flow ratio (fixed + trial-admitted) | 0.750 |
| r1  same-queue window adjacency | 0.503 |
| r2  deadline-violation ratio | 0.000 |
| r3  supplier/receiver overlap | 0.999 |
| r4  mean e2e/deadline (admitted) | 0.291 |
| constraint violations | 0 |

## Constraint check

- C1-C7, C9: OK
- seed-integrity (no SMT-fixed flow's placement changed): OK

## GCL per egress port

### sw01-p2  (27 entries, util 10.9200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 45760 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 37120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 15360 0x40 # 01000000   Q6
sgs 47360 0xBF # 10111111   Q7
sgs 15360 0x80 # 10000000   Q7
sgs 47360 0x7F # 01111111   Q6
sgs 89920 0x80 # 10000000   Q7
sgs 47360 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 37760 0x7F # 01111111   Q6
sgs 89920 0x80 # 10000000   Q7
sgs 47360 0xBF # 10111111   Q7
sgs 15360 0x80 # 10000000   Q7
sgs 47360 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 29120 0xBF # 10111111   Q7
```

### sw01-p4  (20 entries, util 10.9200 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 79040 0x40 # 01000000   Q6
sgs 54400 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 128960 0x80 # 10000000   Q7
sgs 54400 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 91520 0x80 # 10000000   Q7
sgs 54400 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 112320 0x80 # 10000000   Q7
sgs 21120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (21 entries, util 9.3600 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 33600 0x7F # 01111111   Q6
sgs 32960 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 54400 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 96640 0x40 # 01000000   Q6
sgs 36800 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 96640 0x40 # 01000000   Q6
sgs 36800 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 30080 0x40 # 01000000   Q6
sgs 53440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p4  (26 entries, util 18.7200 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 37120 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 50240 0x40 # 01000000   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 125120 0x80 # 10000000   Q7
sgs 33280 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 99840 0x80 # 10000000   Q7
sgs 33280 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 108480 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (30 entries, util 10.9200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 37120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 15360 0x40 # 01000000   Q6
sgs 18240 0x7F # 01111111   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 15360 0x80 # 10000000   Q7
sgs 47360 0x7F # 01111111   Q6
sgs 89920 0x80 # 10000000   Q7
sgs 18240 0x7F # 01111111   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 37760 0x7F # 01111111   Q6
sgs 89920 0x80 # 10000000   Q7
sgs 18240 0x7F # 01111111   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 15360 0x80 # 10000000   Q7
sgs 47360 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 45760 0xBF # 10111111   Q7
```

### sw03-p5  (20 entries, util 10.9200 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 79040 0x40 # 01000000   Q6
sgs 37760 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 128960 0x80 # 10000000   Q7
sgs 37760 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 91520 0x80 # 10000000   Q7
sgs 37760 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 95680 0x80 # 10000000   Q7
sgs 21120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p4  (18 entries, util 9.3600 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 50240 0x7F # 01111111   Q6
sgs 16320 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 21120 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 96640 0x40 # 01000000   Q6
sgs 53440 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 96640 0x40 # 01000000   Q6
sgs 53440 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 46720 0x40 # 01000000   Q6
sgs 53440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (26 entries, util 18.7200 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 37120 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 50240 0x40 # 01000000   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 124800 0x80 # 10000000   Q7
sgs 16640 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 99840 0x80 # 10000000   Q7
sgs 16640 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 91520 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (20 entries, util 10.9200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 79040 0x40 # 01000000   Q6
sgs 21120 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 128960 0x80 # 10000000   Q7
sgs 21120 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 91520 0x80 # 10000000   Q7
sgs 21120 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 79040 0x80 # 10000000   Q7
sgs 21120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p5  (34 entries, util 10.9200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 24640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 15360 0x40 # 01000000   Q6
sgs 34880 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 15360 0x80 # 10000000   Q7
sgs 22400 0xBF # 10111111   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 89920 0x80 # 10000000   Q7
sgs 34880 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12800 0xBF # 10111111   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 89920 0x80 # 10000000   Q7
sgs 34880 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 15360 0x80 # 10000000   Q7
sgs 22400 0xBF # 10111111   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 27520 0x80 # 10000000   Q7
sgs 47360 0xBF # 10111111   Q7
```

### sw06-p4  (23 entries, util 18.7200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 37120 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 50240 0x40 # 01000000   Q6
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 124800 0x80 # 10000000   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 99840 0x80 # 10000000   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 74880 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (20 entries, util 9.3600 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 16960 0xBF # 10111111   Q7
sgs 49600 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 37760 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 96640 0x40 # 01000000   Q6
sgs 20160 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 96640 0x40 # 01000000   Q6
sgs 20160 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 63360 0x40 # 01000000   Q6
sgs 53440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (26 entries, util 10.9200 %)

```
sgs 45760 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 37120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 15360 0x40 # 01000000   Q6
sgs 47360 0x7F # 01111111   Q6
sgs 15360 0x80 # 10000000   Q7
sgs 47360 0xBF # 10111111   Q7
sgs 89920 0x80 # 10000000   Q7
sgs 47360 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 37760 0xBF # 10111111   Q7
sgs 89920 0x80 # 10000000   Q7
sgs 47360 0x7F # 01111111   Q6
sgs 15360 0x80 # 10000000   Q7
sgs 47360 0xBF # 10111111   Q7
sgs 44160 0x80 # 10000000   Q7
sgs 47360 0xBF # 10111111   Q7
```

### sw07-p5  (24 entries, util 10.9200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 60800 0x80 # 10000000   Q7
sgs 54400 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 128960 0x80 # 10000000   Q7
sgs 54400 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 30720 0x7F # 01111111   Q6
sgs 60800 0x80 # 10000000   Q7
sgs 54400 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 62400 0x80 # 10000000   Q7
sgs 21120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p2  (21 entries, util 18.7200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 29120 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 95680 0x80 # 10000000   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 150080 0x80 # 10000000   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 29120 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 95680 0x80 # 10000000   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 83520 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p4  (20 entries, util 9.3600 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 24960 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 33600 0xBF # 10111111   Q7
sgs 32960 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 54400 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 96640 0x40 # 01000000   Q6
sgs 36800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 96640 0x40 # 01000000   Q6
sgs 36800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 80000 0x40 # 01000000   Q6
sgs 53440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (29 entries, util 10.9200 %)

```
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 37120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 15360 0x40 # 01000000   Q6
sgs 18240 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 15360 0x80 # 10000000   Q7
sgs 47360 0xBF # 10111111   Q7
sgs 89920 0x80 # 10000000   Q7
sgs 18240 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 37760 0xBF # 10111111   Q7
sgs 89920 0x80 # 10000000   Q7
sgs 18240 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 15360 0x80 # 10000000   Q7
sgs 47360 0xBF # 10111111   Q7
sgs 60800 0x80 # 10000000   Q7
sgs 47360 0xBF # 10111111   Q7
```

