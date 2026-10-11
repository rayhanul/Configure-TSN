# RL-enlarged GCL schedule (Problem 2: window enlargement)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Seeded from SMT run: **result/result-2026-10-10-dataset-testbed-5-avgwin/smt-c9-on/5-fair-retimed-c9on**

## Admission (unchanged) vs. capacity grown

Problem 2 never admits a flow into the schedule it exports -- it only widens windows. `admitted` below is exactly the SMT baseline, by construction; the capacity growth this run achieved is banked slack and per-port GCL entries, reported separately.

| | admitted | of total |
|---|---|---|
| SMT (fixed, never moved) | 10 | 10 |
| RL-enlarged (exported; grow-only, admits nothing new) | 10 | 20 |

During training, the policy's trial admissions (the reward signal that teaches it how much a window needs to grow) reached **9** of the 10 SMT-rejected flows -- none of those are kept in this export; that capacity stays as empty, banked slack for Problem 3 to fill. Total slack banked: 330880 ns. GCL_size overflow: 0.

## Opportunistic idle top-up (deterministic post-pass)

**10933120 ns**, drawn from idle capacity on ports at or below utilisation 0.2, independent of what training happened to grow. Ported from prob_2_heuristic_enlarged's Step 7.

| port | queue | applied (ns) |
|---|---|---|
| S1-p0 | Q6 | 512640 |
| S1-p0 | Q7 | 100160 |
| S2-p0 | Q6 | 487680 |
| S2-p0 | Q7 | 125120 |
| S3-p0 | Q6 | 625280 |
| sw01-p2 | Q6 | 377280 |
| sw01-p2 | Q7 | 93120 |
| sw01-p4 | Q6 | 536640 |
| sw01-p4 | Q7 | 80320 |
| sw02-p2 | Q6 | 9600 |
| sw02-p2 | Q7 | 632320 |
| sw02-p4 | Q6 | 429440 |
| sw02-p4 | Q7 | 145280 |
| sw03-p4 | Q6 | 386880 |
| sw03-p4 | Q7 | 88960 |
| sw03-p5 | Q6 | 528000 |
| sw03-p5 | Q7 | 80640 |
| sw04-p4 | Q6 | 8960 |
| sw04-p4 | Q7 | 641280 |
| sw04-p5 | Q6 | 419840 |
| sw04-p5 | Q7 | 145600 |
| sw05-p4 | Q6 | 383680 |
| sw05-p4 | Q7 | 197440 |
| sw05-p5 | Q6 | 398400 |
| sw05-p5 | Q7 | 82880 |
| sw06-p4 | Q6 | 414080 |
| sw06-p4 | Q7 | 144000 |
| sw06-p5 | Q6 | 8320 |
| sw06-p5 | Q7 | 650240 |
| sw07-p4 | Q6 | 409920 |
| sw07-p4 | Q7 | 76800 |
| sw07-p5 | Q6 | 379200 |
| sw07-p5 | Q7 | 197760 |
| sw08-p4 | Q6 | 7680 |
| sw08-p4 | Q7 | 659200 |
| sw08-p5 | Q6 | 431360 |
| sw08-p5 | Q7 | 37120 |

## Best-effort gap equalization (deterministic post-pass)

**6483200 ns** given back from the top-up/creation above so each port's leftover non-TAS gaps land close to equal. Ported from prob_2_heuristic_enlarged's Step 9.

| port | given back (ns) |
|---|---|---|
| sw08-p4 | 461440 |
| sw06-p5 | 459520 |
| sw04-p4 | 457600 |
| sw02-p2 | 455680 |
| sw02-p4 | 398080 |
| sw04-p5 | 396160 |
| sw06-p4 | 396160 |
| sw01-p2 | 361600 |
| sw03-p4 | 359680 |
| sw05-p5 | 356480 |
| sw07-p4 | 353280 |
| S1-p0 | 315840 |
| sw08-p5 | 304320 |
| sw07-p5 | 265920 |
| sw05-p4 | 262080 |
| sw01-p4 | 238080 |
| sw03-p5 | 235840 |
| S2-p0 | 216000 |
| S3-p0 | 189440 |

## Opportunistic overlay window creation (deterministic post-pass)

**36** new overlay window(s), **6629120 ns** total, carved out of already-open best-effort spans on ports at or below utilisation 0.2 -- best-effort stays reachable inside each one (gate mask keeps its BE bits set). Run once after training/finalize_grow_only(), not a trained action.

| port | queue | size (ns) |
|---|---|---|
| S1-p0 | Q6 | 103680 |
| S1-p0 | Q7 | 212160 |
| S2-p0 | Q7 | 216000 |
| S3-p0 | Q7 | 189440 |
| sw01-p2 | Q6 | 158080 |
| sw01-p2 | Q7 | 188480 |
| sw01-p4 | Q6 | 17280 |
| sw01-p4 | Q7 | 208640 |
| sw02-p2 | Q6 | 323200 |
| sw02-p2 | Q7 | 193600 |
| sw02-p4 | Q6 | 153920 |
| sw02-p4 | Q7 | 234240 |
| sw03-p4 | Q6 | 149760 |
| sw03-p4 | Q7 | 191040 |
| sw03-p5 | Q6 | 89920 |
| sw03-p5 | Q7 | 152640 |
| sw04-p4 | Q6 | 308480 |
| sw04-p4 | Q7 | 202560 |
| sw04-p5 | Q6 | 234880 |
| sw04-p5 | Q7 | 170560 |
| sw05-p4 | Q6 | 99840 |
| sw05-p4 | Q7 | 178560 |
| sw05-p5 | Q6 | 112640 |
| sw05-p5 | Q7 | 220160 |
| sw06-p4 | Q6 | 253120 |
| sw06-p4 | Q7 | 163200 |
| sw06-p5 | Q6 | 302400 |
| sw06-p5 | Q7 | 202880 |
| sw07-p4 | Q6 | 89920 |
| sw07-p4 | Q7 | 236160 |
| sw07-p5 | Q6 | 133120 |
| sw07-p5 | Q7 | 155520 |
| sw08-p4 | Q6 | 304000 |
| sw08-p4 | Q7 | 195520 |
| sw08-p5 | Q6 | 111040 |
| sw08-p5 | Q7 | 172480 |

## Per-port GCL entries: before (SMT) vs. after (RL-enlarged)

| port | SMT entries | RL-enlarged entries | GCL_size |
|---|---|---|---|
| sw01-p2 | 13 | 35 | 255 |
| sw01-p4 | 15 | 24 | 255 |
| sw02-p2 | 5 | 21 | 255 |
| sw02-p4 | 17 | 21 | 255 |
| sw03-p4 | 13 | 35 | 255 |
| sw03-p5 | 15 | 25 | 255 |
| sw04-p4 | 5 | 23 | 255 |
| sw04-p5 | 17 | 23 | 255 |
| sw05-p4 | 15 | 24 | 255 |
| sw05-p5 | 13 | 39 | 255 |
| sw06-p4 | 17 | 25 | 255 |
| sw06-p5 | 5 | 22 | 255 |
| sw07-p4 | 13 | 40 | 255 |
| sw07-p5 | 15 | 24 | 255 |
| sw08-p2 | 29 | 21 | 255 |
| sw08-p4 | 5 | 20 | 255 |
| sw08-p5 | 13 | 38 | 255 |

## Flows

| flow | route | fixed | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|---|
| s0(id=1 S3->S1) | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | no | None | None | None | no |
| s1(id=2 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | yes | 7 | 0 | 46160 | yes |
| s2(id=3 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | yes | 7 | 62400 | 56720 | yes |
| s3(id=4 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |
| s4(id=5 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | yes | 7 | 62400 | 38160 | yes |
| s5(id=6 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |
| s6(id=7 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | no | None | None | None | no |
| s7(id=8 S3->S1) | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | no | None | None | None | no |
| s8(id=9 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | yes | 6 | 37440 | 45840 | yes |
| s9(id=10 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | yes | 6 | 0 | 45840 | yes |
| s10(id=11 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |
| s11(id=12 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | yes | 6 | 12480 | 54160 | yes |
| s12(id=13 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | yes | 7 | 87360 | 74000 | yes |
| s13(id=14 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |
| s14(id=15 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |
| s15(id=16 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | yes | 6 | 62400 | 43920 | yes |
| s16(id=17 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | yes | 7 | 37440 | 43280 | yes |
| s17(id=18 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |
| s18(id=19 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | yes | 6 | 37440 | 56080 | yes |
| s19(id=20 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | no | None | None | None | no |

## Per-hop windows (slack_ns > 0 means this window was enlarged)

| flow | egress port | queue | psi (ns) | delta (ns) |
|---|---|---|---|---|
| s1(id=2 S2->S3) | S2-p0 | Q7 | 0 | 12480 |
| s1(id=2 S2->S3) | sw08-p5 | Q7 | 6720 | 12480 |
| s1(id=2 S2->S3) | sw07-p4 | Q7 | 13440 | 12480 |
| s1(id=2 S2->S3) | sw05-p5 | Q7 | 20160 | 12480 |
| s1(id=2 S2->S3) | sw03-p4 | Q7 | 26880 | 12480 |
| s1(id=2 S2->S3) | sw01-p2 | Q7 | 33600 | 12480 |
| s2(id=3 S1->S2) | S1-p0 | Q7 | 62400 | 12480 |
| s2(id=3 S1->S2) | sw02-p4 | Q7 | 67520 | 12480 |
| s2(id=3 S1->S2) | sw04-p5 | Q7 | 72640 | 12480 |
| s2(id=3 S1->S2) | sw06-p4 | Q7 | 77760 | 12480 |
| s2(id=3 S1->S2) | sw08-p2 | Q7 | 106560 | 12480 |
| s4(id=5 S2->S3) | S2-p0 | Q7 | 62400 | 12480 |
| s4(id=5 S2->S3) | sw08-p5 | Q7 | 67520 | 12480 |
| s4(id=5 S2->S3) | sw07-p4 | Q7 | 72640 | 12480 |
| s4(id=5 S2->S3) | sw05-p5 | Q7 | 77760 | 12480 |
| s4(id=5 S2->S3) | sw03-p4 | Q7 | 82880 | 12480 |
| s4(id=5 S2->S3) | sw01-p2 | Q7 | 88000 | 12480 |
| s8(id=9 S2->S1) | S2-p0 | Q6 | 37440 | 12480 |
| s8(id=9 S2->S1) | sw08-p4 | Q6 | 45760 | 12480 |
| s8(id=9 S2->S1) | sw06-p5 | Q6 | 54080 | 12480 |
| s8(id=9 S2->S1) | sw04-p4 | Q6 | 62400 | 12480 |
| s8(id=9 S2->S1) | sw02-p2 | Q6 | 70720 | 12480 |
| s9(id=10 S1->S2) | S1-p0 | Q6 | 0 | 12480 |
| s9(id=10 S1->S2) | sw02-p4 | Q6 | 8320 | 12480 |
| s9(id=10 S1->S2) | sw04-p5 | Q6 | 16640 | 12480 |
| s9(id=10 S1->S2) | sw06-p4 | Q6 | 24960 | 12480 |
| s9(id=10 S1->S2) | sw08-p2 | Q6 | 33280 | 12480 |
| s11(id=12 S3->S2) | S3-p0 | Q6 | 12480 | 12480 |
| s11(id=12 S3->S2) | sw01-p4 | Q6 | 20800 | 12480 |
| s11(id=12 S3->S2) | sw03-p5 | Q6 | 29120 | 12480 |
| s11(id=12 S3->S2) | sw05-p4 | Q6 | 37440 | 12480 |
| s11(id=12 S3->S2) | sw07-p5 | Q6 | 45760 | 12480 |
| s11(id=12 S3->S2) | sw08-p2 | Q6 | 54080 | 12480 |
| s12(id=13 S1->S3) | S1-p0 | Q7 | 87360 | 12480 |
| s12(id=13 S1->S3) | sw02-p4 | Q7 | 95040 | 12480 |
| s12(id=13 S1->S3) | sw04-p5 | Q7 | 102720 | 12480 |
| s12(id=13 S1->S3) | sw06-p4 | Q7 | 110400 | 12480 |
| s12(id=13 S1->S3) | sw08-p5 | Q7 | 118080 | 12480 |
| s12(id=13 S1->S3) | sw07-p4 | Q7 | 125760 | 12480 |
| s12(id=13 S1->S3) | sw05-p5 | Q7 | 133440 | 12480 |
| s12(id=13 S1->S3) | sw03-p4 | Q7 | 141120 | 12480 |
| s12(id=13 S1->S3) | sw01-p2 | Q7 | 148800 | 12480 |
| s15(id=16 S3->S2) | S3-p0 | Q6 | 62400 | 12480 |
| s15(id=16 S3->S2) | sw01-p4 | Q6 | 68480 | 12480 |
| s15(id=16 S3->S2) | sw03-p5 | Q6 | 74560 | 12480 |
| s15(id=16 S3->S2) | sw05-p4 | Q6 | 80640 | 12480 |
| s15(id=16 S3->S2) | sw07-p5 | Q6 | 87680 | 12480 |
| s15(id=16 S3->S2) | sw08-p2 | Q6 | 93760 | 12480 |
| s16(id=17 S1->S2) | S1-p0 | Q7 | 37440 | 12480 |
| s16(id=17 S1->S2) | sw02-p4 | Q7 | 45120 | 12480 |
| s16(id=17 S1->S2) | sw04-p5 | Q7 | 52800 | 12480 |
| s16(id=17 S1->S2) | sw06-p4 | Q7 | 60480 | 12480 |
| s16(id=17 S1->S2) | sw08-p2 | Q7 | 68160 | 12480 |
| s18(id=19 S3->S2) | S3-p0 | Q6 | 37440 | 12480 |
| s18(id=19 S3->S2) | sw01-p4 | Q6 | 47680 | 12480 |
| s18(id=19 S3->S2) | sw03-p5 | Q6 | 56000 | 12480 |
| s18(id=19 S3->S2) | sw05-p4 | Q6 | 64320 | 12480 |
| s18(id=19 S3->S2) | sw07-p5 | Q6 | 72640 | 12480 |
| s18(id=19 S3->S2) | sw08-p2 | Q6 | 80960 | 12480 |

## Metrics (training/evaluation signal, not the export)

| metric | value |
|---|---|
| trial-placed flow ratio (fixed + trial-admitted) | 0.950 |
| r1  same-queue window adjacency | 0.348 |
| r2  deadline-violation ratio | 0.000 |
| r3  supplier/receiver overlap | 0.993 |
| r4  mean e2e/deadline (admitted) | 0.215 |
| constraint violations | 0 |

## Constraint check

- C1-C7, C9: OK
- seed-integrity (no SMT-fixed flow's placement changed): OK

## GCL per egress port

### sw01-p2  (35 entries, util 9.3600 %)

```
sgs 33600 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 8000 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 33600 0x80 # 10000000   Q7
sgs 1600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 16000 0x7F # 01111111   Q6
sgs 30720 0x80 # 10000000   Q7
sgs 22400 0xBF # 10111111   Q7
sgs 13760 0x40 # 01000000   Q6
sgs 36160 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 8000 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 35520 0xBF # 10111111   Q7
sgs 95360 0x40 # 01000000   Q6
sgs 36160 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 8000 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 22720 0xBF # 10111111   Q7
sgs 45440 0x40 # 01000000   Q6
sgs 36160 0xBF # 10111111   Q7
sgs 13760 0x40 # 01000000   Q6
sgs 36160 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 8000 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 35520 0xBF # 10111111   Q7
sgs 61760 0x40 # 01000000   Q6
sgs 36160 0xBF # 10111111   Q7
```

### sw01-p4  (24 entries, util 10.9200 %)

```
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 960 0x3F # 00111111   BE
sgs 33280 0x40 # 01000000   Q6
sgs 19200 0xBF # 10111111   Q7
sgs 17280 0x7F # 01111111   Q6
sgs 43520 0x80 # 10000000   Q7
sgs 47360 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 140160 0x40 # 01000000   Q6
sgs 47360 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 960 0x3F # 00111111   BE
sgs 113280 0x40 # 01000000   Q6
sgs 47360 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 131840 0x40 # 01000000   Q6
sgs 47360 0xBF # 10111111   Q7
```

### sw02-p2  (21 entries, util 3.1200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 20800 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 4800 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 59520 0x7F # 01111111   Q6
sgs 31360 0x80 # 10000000   Q7
sgs 58560 0x7F # 01111111   Q6
sgs 38080 0xBF # 10111111   Q7
sgs 86080 0x80 # 10000000   Q7
sgs 25920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 20800 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 4800 0x3F # 00111111   BE
sgs 103360 0x80 # 10000000   Q7
sgs 58560 0x7F # 01111111   Q6
sgs 38080 0xBF # 10111111   Q7
sgs 15360 0x80 # 10000000   Q7
sgs 46720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p4  (21 entries, util 12.4800 %)

```
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 24320 0x7F # 01111111   Q6
sgs 34880 0x80 # 10000000   Q7
sgs 15040 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 42240 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 46080 0xBF # 10111111   Q7
sgs 136640 0x40 # 01000000   Q6
sgs 63360 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 24320 0x7F # 01111111   Q6
sgs 41280 0x80 # 10000000   Q7
sgs 13760 0xBF # 10111111   Q7
sgs 49600 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 46080 0xBF # 10111111   Q7
sgs 128320 0x40 # 01000000   Q6
sgs 13440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (35 entries, util 9.3600 %)

```
sgs 26880 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 6400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 1600 0x3F # 00111111   BE
sgs 35520 0x80 # 10000000   Q7
sgs 1600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0x7F # 01111111   Q6
sgs 29760 0x80 # 10000000   Q7
sgs 21760 0xBF # 10111111   Q7
sgs 15360 0x40 # 01000000   Q6
sgs 36160 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 6400 0x3F # 00111111   BE
sgs 15040 0x40 # 01000000   Q6
sgs 36160 0xBF # 10111111   Q7
sgs 93760 0x40 # 01000000   Q6
sgs 36160 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 6400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 1600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 24640 0xBF # 10111111   Q7
sgs 42240 0x40 # 01000000   Q6
sgs 36160 0xBF # 10111111   Q7
sgs 15360 0x40 # 01000000   Q6
sgs 36160 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 6400 0x3F # 00111111   BE
sgs 15040 0x40 # 01000000   Q6
sgs 36160 0xBF # 10111111   Q7
sgs 66880 0x40 # 01000000   Q6
sgs 36160 0xBF # 10111111   Q7
```

### sw03-p5  (25 entries, util 10.9200 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 1920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 31040 0x40 # 01000000   Q6
sgs 13120 0xBF # 10111111   Q7
sgs 23360 0x7F # 01111111   Q6
sgs 45760 0x80 # 10000000   Q7
sgs 30720 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 140160 0x40 # 01000000   Q6
sgs 30720 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 1920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 113280 0x40 # 01000000   Q6
sgs 30720 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 123520 0x40 # 01000000   Q6
sgs 47360 0xBF # 10111111   Q7
```

### sw04-p4  (23 entries, util 3.1200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 4480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 62080 0x7F # 01111111   Q6
sgs 28800 0x80 # 10000000   Q7
sgs 17280 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 29440 0xBF # 10111111   Q7
sgs 86400 0x80 # 10000000   Q7
sgs 34240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 4480 0x3F # 00111111   BE
sgs 103360 0x80 # 10000000   Q7
sgs 17280 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 29440 0xBF # 10111111   Q7
sgs 24000 0x80 # 10000000   Q7
sgs 46720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (23 entries, util 12.4800 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 23680 0x7F # 01111111   Q6
sgs 32320 0x80 # 10000000   Q7
sgs 17600 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 44160 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 28160 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 136640 0x40 # 01000000   Q6
sgs 46720 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 23680 0x7F # 01111111   Q6
sgs 43200 0x80 # 10000000   Q7
sgs 63360 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 28160 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 120000 0x40 # 01000000   Q6
sgs 13440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (24 entries, util 10.9200 %)

```
sgs 24960 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0xBF # 10111111   Q7
sgs 28800 0x40 # 01000000   Q6
sgs 4800 0x3F # 00111111   BE
sgs 76160 0x80 # 10000000   Q7
sgs 25920 0xBF # 10111111   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 136640 0x40 # 01000000   Q6
sgs 25920 0xBF # 10111111   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 21120 0xBF # 10111111   Q7
sgs 76160 0x80 # 10000000   Q7
sgs 25920 0xBF # 10111111   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 111680 0x40 # 01000000   Q6
sgs 50880 0xBF # 10111111   Q7
```

### sw05-p5  (39 entries, util 9.3600 %)

```
sgs 20160 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 4800 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 3840 0x3F # 00111111   BE
sgs 36480 0x80 # 10000000   Q7
sgs 1600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12800 0x7F # 01111111   Q6
sgs 28800 0x80 # 10000000   Q7
sgs 21120 0xBF # 10111111   Q7
sgs 16960 0x40 # 01000000   Q6
sgs 16000 0xBF # 10111111   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 4800 0x3F # 00111111   BE
sgs 18240 0x40 # 01000000   Q6
sgs 36160 0xBF # 10111111   Q7
sgs 92160 0x40 # 01000000   Q6
sgs 16000 0xBF # 10111111   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 4800 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 3840 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 25600 0xBF # 10111111   Q7
sgs 39040 0x40 # 01000000   Q6
sgs 19200 0x7F # 01111111   Q6
sgs 16960 0xBF # 10111111   Q7
sgs 16960 0x40 # 01000000   Q6
sgs 16000 0xBF # 10111111   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 4800 0x3F # 00111111   BE
sgs 18240 0x40 # 01000000   Q6
sgs 36160 0xBF # 10111111   Q7
sgs 72000 0x40 # 01000000   Q6
sgs 36160 0xBF # 10111111   Q7
```

### sw06-p4  (25 entries, util 12.4800 %)

```
sgs 24960 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 23040 0x7F # 01111111   Q6
sgs 29760 0x80 # 10000000   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 27200 0x7F # 01111111   Q6
sgs 16960 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 20480 0xBF # 10111111   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 136640 0x40 # 01000000   Q6
sgs 38400 0xBF # 10111111   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 23040 0x7F # 01111111   Q6
sgs 43200 0x80 # 10000000   Q7
sgs 46400 0x7F # 01111111   Q6
sgs 16960 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 20480 0xBF # 10111111   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 111680 0x40 # 01000000   Q6
sgs 13440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (22 entries, util 3.1200 %)

```
sgs 54080 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 16960 0xBF # 10111111   Q7
sgs 47680 0x7F # 01111111   Q6
sgs 26240 0x80 # 10000000   Q7
sgs 25920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 20800 0xBF # 10111111   Q7
sgs 86720 0x80 # 10000000   Q7
sgs 42560 0xBF # 10111111   Q7
sgs 54080 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 103360 0x80 # 10000000   Q7
sgs 25920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 20800 0xBF # 10111111   Q7
sgs 32640 0x80 # 10000000   Q7
sgs 46720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (40 entries, util 9.3600 %)

```
sgs 13440 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 3200 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 6080 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 1600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 27840 0x80 # 10000000   Q7
sgs 20480 0xBF # 10111111   Q7
sgs 18560 0x40 # 01000000   Q6
sgs 22720 0xBF # 10111111   Q7
sgs 13440 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 3200 0x3F # 00111111   BE
sgs 21440 0x40 # 01000000   Q6
sgs 36160 0xBF # 10111111   Q7
sgs 90560 0x40 # 01000000   Q6
sgs 22720 0xBF # 10111111   Q7
sgs 13440 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 3200 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 6080 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 26560 0xBF # 10111111   Q7
sgs 35840 0x40 # 01000000   Q6
sgs 36160 0x7F # 01111111   Q6
sgs 18560 0x40 # 01000000   Q6
sgs 22720 0xBF # 10111111   Q7
sgs 13440 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 3200 0x3F # 00111111   BE
sgs 21440 0x40 # 01000000   Q6
sgs 36160 0xBF # 10111111   Q7
sgs 77120 0x40 # 01000000   Q6
sgs 36160 0xBF # 10111111   Q7
```

### sw07-p5  (24 entries, util 10.9200 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0xBF # 10111111   Q7
sgs 27520 0x40 # 01000000   Q6
sgs 8000 0x3F # 00111111   BE
sgs 74240 0x80 # 10000000   Q7
sgs 17600 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 136640 0x40 # 01000000   Q6
sgs 17600 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 23040 0xBF # 10111111   Q7
sgs 74240 0x80 # 10000000   Q7
sgs 17600 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 103360 0x40 # 01000000   Q6
sgs 50880 0xBF # 10111111   Q7
```

### sw08-p2  (21 entries, util 21.8400 %)

```
sgs 33280 0x3F # 00111111   BE
sgs 33280 0x40 # 01000000   Q6
sgs 1600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 25280 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 101440 0x3F # 00111111   BE
sgs 33280 0x40 # 01000000   Q6
sgs 166720 0x3F # 00111111   BE
sgs 33280 0x40 # 01000000   Q6
sgs 1600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 25920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 101440 0x3F # 00111111   BE
sgs 33280 0x40 # 01000000   Q6
sgs 133440 0x3F # 00111111   BE
```

### sw08-p4  (20 entries, util 3.1200 %)

```
sgs 45760 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 3840 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 25600 0xBF # 10111111   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 23680 0x80 # 10000000   Q7
sgs 34560 0xBF # 10111111   Q7
sgs 62080 0x7F # 01111111   Q6
sgs 87040 0x80 # 10000000   Q7
sgs 50880 0xBF # 10111111   Q7
sgs 45760 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 3840 0x3F # 00111111   BE
sgs 103360 0x80 # 10000000   Q7
sgs 34560 0xBF # 10111111   Q7
sgs 62080 0x7F # 01111111   Q6
sgs 41280 0x80 # 10000000   Q7
sgs 46720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (38 entries, util 9.3600 %)

```
sgs 6720 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 1600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 4480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 20160 0xBF # 10111111   Q7
sgs 17920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 19840 0x7F # 01111111   Q6
sgs 18240 0x40 # 01000000   Q6
sgs 38080 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 1600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 17600 0x7F # 01111111   Q6
sgs 117760 0x40 # 01000000   Q6
sgs 38080 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 1600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 4480 0x3F # 00111111   BE
sgs 61440 0x40 # 01000000   Q6
sgs 38080 0x7F # 01111111   Q6
sgs 18240 0x40 # 01000000   Q6
sgs 38080 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 1600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 17600 0x7F # 01111111   Q6
sgs 111040 0x40 # 01000000   Q6
sgs 38080 0xBF # 10111111   Q7
```

