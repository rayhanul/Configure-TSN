# RL-enlarged GCL schedule (Problem 2: window enlargement)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Seeded from SMT run: **result/result-2026-10-13-dataset-testbed-12-tree-avgwin/smt-c9-on/12-fair-retimed-c9on**

## Admission (unchanged) vs. capacity grown

Problem 2 never admits a flow into the schedule it exports -- it only widens windows. `admitted` below is exactly the SMT baseline, by construction; the capacity growth this run achieved is banked slack and per-port GCL entries, reported separately.

| | admitted | of total |
|---|---|---|
| SMT (fixed, never moved) | 11 | 11 |
| RL-enlarged (exported; grow-only, admits nothing new) | 11 | 20 |

During training, the policy's trial admissions (the reward signal that teaches it how much a window needs to grow) reached **8** of the 9 SMT-rejected flows -- none of those are kept in this export; that capacity stays as empty, banked slack for Problem 3 to fill. Total slack banked: 111360 ns. GCL_size overflow: 0.

## Opportunistic idle top-up (deterministic post-pass)

**11963200 ns**, drawn from idle capacity on ports at or below utilisation 0.2, independent of what training happened to grow. Ported from prob_2_heuristic_enlarged's Step 7.

| port | queue | applied (ns) |
|---|---|---|
| S1-p0 | Q6 | 562880 |
| S2-p0 | Q6 | 637760 |
| S3-p0 | Q6 | 137600 |
| S3-p0 | Q7 | 525120 |
| sw01-p2 | Q6 | 436800 |
| sw01-p2 | Q7 | 55040 |
| sw01-p4 | Q6 | 82880 |
| sw01-p4 | Q7 | 574720 |
| sw02-p2 | Q6 | 261440 |
| sw02-p2 | Q7 | 411840 |
| sw02-p4 | Q6 | 551360 |
| sw02-p4 | Q7 | 1280 |
| sw03-p4 | Q6 | 501760 |
| sw03-p4 | Q7 | 640 |
| sw03-p5 | Q6 | 93760 |
| sw03-p5 | Q7 | 558720 |
| sw04-p4 | Q6 | 262080 |
| sw04-p4 | Q7 | 417920 |
| sw04-p5 | Q6 | 537920 |
| sw04-p5 | Q7 | 2560 |
| sw05-p4 | Q6 | 104640 |
| sw05-p4 | Q7 | 542720 |
| sw05-p5 | Q6 | 512000 |
| sw05-p5 | Q7 | 960 |
| sw06-p4 | Q6 | 526400 |
| sw06-p4 | Q7 | 3840 |
| sw06-p5 | Q6 | 260800 |
| sw06-p5 | Q7 | 425920 |
| sw07-p4 | Q6 | 522240 |
| sw07-p4 | Q7 | 3200 |
| sw07-p5 | Q6 | 115520 |
| sw07-p5 | Q7 | 526720 |
| sw08-p2 | Q6 | 416640 |
| sw08-p2 | Q7 | 158080 |
| sw08-p4 | Q6 | 259520 |
| sw08-p4 | Q7 | 433920 |
| sw08-p5 | Q6 | 532480 |
| sw08-p5 | Q7 | 3520 |

## Best-effort gap equalization (deterministic post-pass)

**6157440 ns** given back from the top-up/creation above so each port's leftover non-TAS gaps land close to equal. Ported from prob_2_heuristic_enlarged's Step 9.

| port | given back (ns) |
|---|---|---|
| sw02-p2 | 411520 |
| sw04-p4 | 409600 |
| sw06-p5 | 408640 |
| sw08-p4 | 407680 |
| sw07-p5 | 355200 |
| sw05-p4 | 347200 |
| sw03-p5 | 334400 |
| sw01-p4 | 321600 |
| sw01-p2 | 296320 |
| S2-p0 | 288640 |
| sw03-p4 | 273920 |
| sw05-p5 | 265600 |
| sw06-p4 | 261120 |
| sw04-p5 | 260800 |
| sw02-p4 | 260480 |
| S1-p0 | 260160 |
| sw07-p4 | 257280 |
| sw08-p2 | 251520 |
| sw08-p5 | 248960 |
| S3-p0 | 236800 |

## Opportunistic overlay window creation (deterministic post-pass)

**37** new overlay window(s), **6336320 ns** total, carved out of already-open best-effort spans on ports at or below utilisation 0.2 -- best-effort stays reachable inside each one (gate mask keeps its BE bits set). Run once after training/finalize_grow_only(), not a trained action.

| port | queue | size (ns) |
|---|---|---|
| S1-p0 | Q6 | 74880 |
| S1-p0 | Q7 | 185280 |
| S2-p0 | Q6 | 76480 |
| S2-p0 | Q7 | 212160 |
| S3-p0 | Q7 | 236800 |
| sw01-p2 | Q6 | 168640 |
| sw01-p2 | Q7 | 156800 |
| sw01-p4 | Q7 | 319680 |
| sw02-p2 | Q6 | 164480 |
| sw02-p2 | Q7 | 273280 |
| sw02-p4 | Q6 | 65920 |
| sw02-p4 | Q7 | 172800 |
| sw03-p4 | Q6 | 181760 |
| sw03-p4 | Q7 | 127680 |
| sw03-p5 | Q7 | 330560 |
| sw04-p4 | Q6 | 153280 |
| sw04-p4 | Q7 | 276160 |
| sw04-p5 | Q6 | 130880 |
| sw04-p5 | Q7 | 126720 |
| sw05-p4 | Q6 | 89600 |
| sw05-p4 | Q7 | 267200 |
| sw05-p5 | Q6 | 174720 |
| sw05-p5 | Q7 | 118720 |
| sw06-p4 | Q6 | 165120 |
| sw06-p4 | Q7 | 103680 |
| sw06-p5 | Q6 | 184000 |
| sw06-p5 | Q7 | 237120 |
| sw07-p4 | Q6 | 183680 |
| sw07-p4 | Q7 | 93760 |
| sw07-p5 | Q6 | 137600 |
| sw07-p5 | Q7 | 230400 |
| sw08-p2 | Q6 | 173440 |
| sw08-p2 | Q7 | 75520 |
| sw08-p4 | Q6 | 165440 |
| sw08-p4 | Q7 | 240640 |
| sw08-p5 | Q6 | 149440 |
| sw08-p5 | Q7 | 112000 |

## Per-port GCL entries: before (SMT) vs. after (RL-enlarged)

| port | SMT entries | RL-enlarged entries | GCL_size |
|---|---|---|---|
| sw01-p2 | 15 | 21 | 255 |
| sw01-p4 | 15 | 19 | 255 |
| sw02-p2 | 13 | 21 | 255 |
| sw02-p4 | 25 | 27 | 255 |
| sw03-p4 | 15 | 23 | 255 |
| sw03-p5 | 15 | 19 | 255 |
| sw04-p4 | 13 | 22 | 255 |
| sw04-p5 | 25 | 30 | 255 |
| sw05-p4 | 15 | 24 | 255 |
| sw05-p5 | 15 | 23 | 255 |
| sw06-p4 | 25 | 30 | 255 |
| sw06-p5 | 13 | 25 | 255 |
| sw07-p4 | 15 | 26 | 255 |
| sw07-p5 | 15 | 23 | 255 |
| sw08-p2 | 25 | 32 | 255 |
| sw08-p4 | 13 | 21 | 255 |
| sw08-p5 | 15 | 26 | 255 |

## Flows

| flow | route | fixed | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|---|
| s0(id=1 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | no | None | None | None | no |
| s1(id=2 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | yes | 6 | 0 | 50960 | yes |
| s2(id=3 S3->S1) | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | no | None | None | None | no |
| s3(id=4 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | yes | 6 | 74880 | 66320 | yes |
| s4(id=5 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | yes | 7 | 0 | 38160 | yes |
| s5(id=6 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |
| s6(id=7 S3->S1) | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | yes | 6 | 49920 | 79120 | yes |
| s7(id=8 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | yes | 7 | 0 | 39440 | yes |
| s8(id=9 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | yes | 6 | 24960 | 42960 | yes |
| s9(id=10 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |
| s10(id=11 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | yes | 7 | 37440 | 39440 | yes |
| s11(id=12 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | yes | 6 | 24960 | 79120 | yes |
| s12(id=13 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |
| s13(id=14 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | yes | 7 | 49920 | 36880 | yes |
| s14(id=15 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |
| s15(id=16 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | no | None | None | None | no |
| s16(id=17 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | no | None | None | None | no |
| s17(id=18 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | yes | 6 | 62400 | 54480 | yes |
| s18(id=19 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | yes | 6 | 99840 | 74000 | yes |
| s19(id=20 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |

## Per-hop windows (slack_ns > 0 means this window was enlarged)

| flow | egress port | queue | psi (ns) | delta (ns) |
|---|---|---|---|---|
| s1(id=2 S1->S2) | S1-p0 | Q6 | 0 | 12480 |
| s1(id=2 S1->S2) | sw02-p4 | Q6 | 7680 | 12480 |
| s1(id=2 S1->S2) | sw04-p5 | Q6 | 15360 | 12480 |
| s1(id=2 S1->S2) | sw06-p4 | Q6 | 23040 | 12480 |
| s1(id=2 S1->S2) | sw08-p2 | Q6 | 38400 | 12480 |
| s3(id=4 S1->S3) | S1-p0 | Q6 | 74880 | 12480 |
| s3(id=4 S1->S3) | sw02-p4 | Q6 | 81600 | 12480 |
| s3(id=4 S1->S3) | sw04-p5 | Q6 | 88320 | 12480 |
| s3(id=4 S1->S3) | sw06-p4 | Q6 | 95040 | 12480 |
| s3(id=4 S1->S3) | sw08-p5 | Q6 | 101760 | 12480 |
| s3(id=4 S1->S3) | sw07-p4 | Q6 | 108480 | 12480 |
| s3(id=4 S1->S3) | sw05-p5 | Q6 | 115200 | 12480 |
| s3(id=4 S1->S3) | sw03-p4 | Q6 | 121920 | 12480 |
| s3(id=4 S1->S3) | sw01-p2 | Q6 | 128640 | 12480 |
| s4(id=5 S3->S2) | S3-p0 | Q7 | 0 | 12480 |
| s4(id=5 S3->S2) | sw01-p4 | Q7 | 5120 | 12480 |
| s4(id=5 S3->S2) | sw03-p5 | Q7 | 10240 | 12480 |
| s4(id=5 S3->S2) | sw05-p4 | Q7 | 15360 | 12480 |
| s4(id=5 S3->S2) | sw07-p5 | Q7 | 20480 | 12480 |
| s4(id=5 S3->S2) | sw08-p2 | Q7 | 25600 | 12480 |
| s6(id=7 S3->S1) | S3-p0 | Q6 | 49920 | 12480 |
| s6(id=7 S3->S1) | sw01-p4 | Q6 | 58240 | 12480 |
| s6(id=7 S3->S1) | sw03-p5 | Q6 | 66560 | 12480 |
| s6(id=7 S3->S1) | sw05-p4 | Q6 | 74880 | 12480 |
| s6(id=7 S3->S1) | sw07-p5 | Q6 | 83200 | 12480 |
| s6(id=7 S3->S1) | sw08-p4 | Q6 | 91520 | 12480 |
| s6(id=7 S3->S1) | sw06-p5 | Q6 | 99840 | 12480 |
| s6(id=7 S3->S1) | sw04-p4 | Q6 | 108160 | 12480 |
| s6(id=7 S3->S1) | sw02-p2 | Q6 | 116480 | 12480 |
| s7(id=8 S2->S1) | S2-p0 | Q7 | 0 | 12480 |
| s7(id=8 S2->S1) | sw08-p4 | Q7 | 6720 | 12480 |
| s7(id=8 S2->S1) | sw06-p5 | Q7 | 13440 | 12480 |
| s7(id=8 S2->S1) | sw04-p4 | Q7 | 20160 | 12480 |
| s7(id=8 S2->S1) | sw02-p2 | Q7 | 26880 | 12480 |
| s8(id=9 S3->S2) | S3-p0 | Q6 | 24960 | 12480 |
| s8(id=9 S3->S2) | sw01-p4 | Q6 | 31040 | 12480 |
| s8(id=9 S3->S2) | sw03-p5 | Q6 | 37120 | 12480 |
| s8(id=9 S3->S2) | sw05-p4 | Q6 | 43200 | 12480 |
| s8(id=9 S3->S2) | sw07-p5 | Q6 | 49280 | 12480 |
| s8(id=9 S3->S2) | sw08-p2 | Q6 | 55360 | 12480 |
| s10(id=11 S2->S1) | S2-p0 | Q7 | 37440 | 12480 |
| s10(id=11 S2->S1) | sw08-p4 | Q7 | 44160 | 12480 |
| s10(id=11 S2->S1) | sw06-p5 | Q7 | 50880 | 12480 |
| s10(id=11 S2->S1) | sw04-p4 | Q7 | 57600 | 12480 |
| s10(id=11 S2->S1) | sw02-p2 | Q7 | 64320 | 12480 |
| s11(id=12 S1->S3) | S1-p0 | Q6 | 24960 | 12480 |
| s11(id=12 S1->S3) | sw02-p4 | Q6 | 33280 | 12480 |
| s11(id=12 S1->S3) | sw04-p5 | Q6 | 41600 | 12480 |
| s11(id=12 S1->S3) | sw06-p4 | Q6 | 49920 | 12480 |
| s11(id=12 S1->S3) | sw08-p5 | Q6 | 58240 | 12480 |
| s11(id=12 S1->S3) | sw07-p4 | Q6 | 66560 | 12480 |
| s11(id=12 S1->S3) | sw05-p5 | Q6 | 74880 | 12480 |
| s11(id=12 S1->S3) | sw03-p4 | Q6 | 83200 | 12480 |
| s11(id=12 S1->S3) | sw01-p2 | Q6 | 91520 | 12480 |
| s13(id=14 S1->S2) | S1-p0 | Q7 | 49920 | 12480 |
| s13(id=14 S1->S2) | sw02-p4 | Q7 | 56000 | 12480 |
| s13(id=14 S1->S2) | sw04-p5 | Q7 | 62080 | 12480 |
| s13(id=14 S1->S2) | sw06-p4 | Q7 | 68160 | 12480 |
| s13(id=14 S1->S2) | sw08-p2 | Q7 | 74240 | 12480 |
| s17(id=18 S2->S3) | S2-p0 | Q6 | 62400 | 12480 |
| s17(id=18 S2->S3) | sw08-p5 | Q6 | 71040 | 12480 |
| s17(id=18 S2->S3) | sw07-p4 | Q6 | 79360 | 12480 |
| s17(id=18 S2->S3) | sw05-p5 | Q6 | 87680 | 12480 |
| s17(id=18 S2->S3) | sw03-p4 | Q6 | 96000 | 12480 |
| s17(id=18 S2->S3) | sw01-p2 | Q6 | 104320 | 12480 |
| s18(id=19 S1->S3) | S1-p0 | Q6 | 99840 | 12480 |
| s18(id=19 S1->S3) | sw02-p4 | Q6 | 107520 | 12480 |
| s18(id=19 S1->S3) | sw04-p5 | Q6 | 115200 | 12480 |
| s18(id=19 S1->S3) | sw06-p4 | Q6 | 122880 | 12480 |
| s18(id=19 S1->S3) | sw08-p5 | Q6 | 130560 | 12480 |
| s18(id=19 S1->S3) | sw07-p4 | Q6 | 138240 | 12480 |
| s18(id=19 S1->S3) | sw05-p5 | Q6 | 145920 | 12480 |
| s18(id=19 S1->S3) | sw03-p4 | Q6 | 153600 | 12480 |
| s18(id=19 S1->S3) | sw01-p2 | Q6 | 161280 | 12480 |

## Metrics (training/evaluation signal, not the export)

| metric | value |
|---|---|
| trial-placed flow ratio (fixed + trial-admitted) | 0.950 |
| r1  same-queue window adjacency | 0.670 |
| r2  deadline-violation ratio | 0.000 |
| r3  supplier/receiver overlap | 0.998 |
| r4  mean e2e/deadline (admitted) | 0.169 |
| constraint violations | 0 |

## Constraint check

- C1-C7, C9: OK
- seed-integrity (no SMT-fixed flow's placement changed): OK

## GCL per egress port

### sw01-p2  (21 entries, util 10.9200 %)

```
sgs 42880 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 23680 0xBF # 10111111   Q7
sgs 62080 0x40 # 01000000   Q6
sgs 20160 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 1600 0x3F # 00111111   BE
sgs 25600 0x80 # 10000000   Q7
sgs 41920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 23680 0xBF # 10111111   Q7
sgs 121920 0x40 # 01000000   Q6
sgs 41920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 23680 0xBF # 10111111   Q7
sgs 121920 0x40 # 01000000   Q6
sgs 41920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 23680 0xBF # 10111111   Q7
sgs 79040 0x40 # 01000000   Q6
sgs 41920 0xBF # 10111111   Q7
```

### sw01-p4  (19 entries, util 10.9200 %)

```
sgs 5120 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 960 0x3F # 00111111   BE
sgs 24960 0x40 # 01000000   Q6
sgs 14720 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 20480 0xBF # 10111111   Q7
sgs 54720 0x80 # 10000000   Q7
sgs 59200 0xBF # 10111111   Q7
sgs 140800 0x80 # 10000000   Q7
sgs 59200 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 960 0x3F # 00111111   BE
sgs 24960 0x40 # 01000000   Q6
sgs 47680 0xBF # 10111111   Q7
sgs 54720 0x80 # 10000000   Q7
sgs 59200 0xBF # 10111111   Q7
sgs 135680 0x80 # 10000000   Q7
sgs 59200 0xBF # 10111111   Q7
```

### sw02-p2  (21 entries, util 9.3600 %)

```
sgs 26880 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 26560 0x7F # 01111111   Q6
sgs 30080 0x40 # 01000000   Q6
sgs 53440 0xBF # 10111111   Q7
sgs 26880 0x7F # 01111111   Q6
sgs 119680 0x80 # 10000000   Q7
sgs 53440 0xBF # 10111111   Q7
sgs 26880 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 38080 0xBF # 10111111   Q7
sgs 69120 0x40 # 01000000   Q6
sgs 53440 0xBF # 10111111   Q7
sgs 26880 0x7F # 01111111   Q6
sgs 92800 0x80 # 10000000   Q7
sgs 30400 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p4  (27 entries, util 18.7200 %)

```
sgs 7680 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 13120 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 10240 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 640 0x3F # 00111111   BE
sgs 24960 0x40 # 01000000   Q6
sgs 13440 0x7F # 01111111   Q6
sgs 56960 0x40 # 01000000   Q6
sgs 43200 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 13120 0x7F # 01111111   Q6
sgs 131200 0x40 # 01000000   Q6
sgs 43200 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 13120 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 10240 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 640 0x3F # 00111111   BE
sgs 95360 0x40 # 01000000   Q6
sgs 43200 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 13120 0x7F # 01111111   Q6
sgs 123520 0x40 # 01000000   Q6
sgs 43200 0xBF # 10111111   Q7
```

### sw03-p4  (23 entries, util 10.9200 %)

```
sgs 36800 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 21440 0xBF # 10111111   Q7
sgs 37760 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 19200 0x7F # 01111111   Q6
sgs 41280 0x40 # 01000000   Q6
sgs 41920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 21440 0xBF # 10111111   Q7
sgs 124160 0x40 # 01000000   Q6
sgs 41920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 21440 0xBF # 10111111   Q7
sgs 124160 0x40 # 01000000   Q6
sgs 41920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 21440 0xBF # 10111111   Q7
sgs 87360 0x40 # 01000000   Q6
sgs 41920 0xBF # 10111111   Q7
```

### sw03-p5  (19 entries, util 10.9200 %)

```
sgs 10240 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 1920 0x3F # 00111111   BE
sgs 24960 0x40 # 01000000   Q6
sgs 16960 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 23680 0xBF # 10111111   Q7
sgs 48320 0x80 # 10000000   Q7
sgs 59200 0xBF # 10111111   Q7
sgs 140800 0x80 # 10000000   Q7
sgs 59200 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 1920 0x3F # 00111111   BE
sgs 24960 0x40 # 01000000   Q6
sgs 53120 0xBF # 10111111   Q7
sgs 48320 0x80 # 10000000   Q7
sgs 59200 0xBF # 10111111   Q7
sgs 130560 0x80 # 10000000   Q7
sgs 59200 0xBF # 10111111   Q7
```

### sw04-p4  (22 entries, util 9.3600 %)

```
sgs 20160 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 25280 0xBF # 10111111   Q7
sgs 31680 0x40 # 01000000   Q6
sgs 60160 0xBF # 10111111   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 119680 0x80 # 10000000   Q7
sgs 60160 0xBF # 10111111   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 17280 0x7F # 01111111   Q6
sgs 20480 0xBF # 10111111   Q7
sgs 69440 0x40 # 01000000   Q6
sgs 60160 0xBF # 10111111   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 99520 0x80 # 10000000   Q7
sgs 30400 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (30 entries, util 18.7200 %)

```
sgs 15360 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 13760 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 8000 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 1280 0x3F # 00111111   BE
sgs 24960 0x40 # 01000000   Q6
sgs 14400 0x7F # 01111111   Q6
sgs 56960 0x40 # 01000000   Q6
sgs 27840 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 13760 0x7F # 01111111   Q6
sgs 130560 0x40 # 01000000   Q6
sgs 27840 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 13760 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 8000 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 1280 0x3F # 00111111   BE
sgs 96320 0x40 # 01000000   Q6
sgs 27840 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 13760 0x7F # 01111111   Q6
sgs 115200 0x40 # 01000000   Q6
sgs 43200 0xBF # 10111111   Q7
```

### sw05-p4  (24 entries, util 10.9200 %)

```
sgs 15360 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 2880 0x3F # 00111111   BE
sgs 24960 0x40 # 01000000   Q6
sgs 19200 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12800 0xBF # 10111111   Q7
sgs 14080 0x7F # 01111111   Q6
sgs 41920 0x80 # 10000000   Q7
sgs 43840 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 140800 0x80 # 10000000   Q7
sgs 43840 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 2880 0x3F # 00111111   BE
sgs 24960 0x40 # 01000000   Q6
sgs 44480 0xBF # 10111111   Q7
sgs 14080 0x7F # 01111111   Q6
sgs 41920 0x80 # 10000000   Q7
sgs 43840 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 125440 0x80 # 10000000   Q7
sgs 59200 0xBF # 10111111   Q7
```

### sw05-p5  (23 entries, util 10.9200 %)

```
sgs 30720 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 19200 0xBF # 10111111   Q7
sgs 37760 0x40 # 01000000   Q6
sgs 1600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 960 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 18240 0x7F # 01111111   Q6
sgs 42880 0x40 # 01000000   Q6
sgs 41920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 19200 0xBF # 10111111   Q7
sgs 126400 0x40 # 01000000   Q6
sgs 41920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 19200 0xBF # 10111111   Q7
sgs 126400 0x40 # 01000000   Q6
sgs 41920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 19200 0xBF # 10111111   Q7
sgs 95680 0x40 # 01000000   Q6
sgs 41920 0xBF # 10111111   Q7
```

### sw06-p4  (30 entries, util 18.7200 %)

```
sgs 23040 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 1920 0x3F # 00111111   BE
sgs 24960 0x40 # 01000000   Q6
sgs 15360 0x7F # 01111111   Q6
sgs 56960 0x40 # 01000000   Q6
sgs 20160 0xBF # 10111111   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0x7F # 01111111   Q6
sgs 129920 0x40 # 01000000   Q6
sgs 20160 0xBF # 10111111   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 1920 0x3F # 00111111   BE
sgs 97280 0x40 # 01000000   Q6
sgs 20160 0xBF # 10111111   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0x7F # 01111111   Q6
sgs 106880 0x40 # 01000000   Q6
sgs 43200 0xBF # 10111111   Q7
```

### sw06-p5  (25 entries, util 9.3600 %)

```
sgs 13440 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 960 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 23040 0xBF # 10111111   Q7
sgs 33280 0x40 # 01000000   Q6
sgs 16960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 13440 0x7F # 01111111   Q6
sgs 119680 0x80 # 10000000   Q7
sgs 16960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 13440 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24000 0x7F # 01111111   Q6
sgs 14400 0xBF # 10111111   Q7
sgs 68800 0x40 # 01000000   Q6
sgs 16960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 13440 0x7F # 01111111   Q6
sgs 106240 0x80 # 10000000   Q7
sgs 30400 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (26 entries, util 10.9200 %)

```
sgs 24640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 16960 0x7F # 01111111   Q6
sgs 37760 0x40 # 01000000   Q6
sgs 960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 3200 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 17280 0x7F # 01111111   Q6
sgs 44480 0x40 # 01000000   Q6
sgs 17280 0xBF # 10111111   Q7
sgs 24640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 16960 0x7F # 01111111   Q6
sgs 128640 0x40 # 01000000   Q6
sgs 17280 0xBF # 10111111   Q7
sgs 24640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 16960 0x7F # 01111111   Q6
sgs 128640 0x40 # 01000000   Q6
sgs 17280 0xBF # 10111111   Q7
sgs 24640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 16960 0x7F # 01111111   Q6
sgs 104000 0x40 # 01000000   Q6
sgs 41920 0xBF # 10111111   Q7
```

### sw07-p5  (23 entries, util 10.9200 %)

```
sgs 20480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 3840 0x3F # 00111111   BE
sgs 24960 0x40 # 01000000   Q6
sgs 21440 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 30080 0x7F # 01111111   Q6
sgs 35520 0x80 # 10000000   Q7
sgs 38720 0xBF # 10111111   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 140800 0x80 # 10000000   Q7
sgs 38720 0xBF # 10111111   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 3840 0x3F # 00111111   BE
sgs 29760 0x40 # 01000000   Q6
sgs 33600 0xBF # 10111111   Q7
sgs 25600 0x7F # 01111111   Q6
sgs 35520 0x80 # 10000000   Q7
sgs 38720 0xBF # 10111111   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 120320 0x80 # 10000000   Q7
sgs 59200 0xBF # 10111111   Q7
```

### sw08-p2  (32 entries, util 18.7200 %)

```
sgs 25600 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 29440 0x40 # 01000000   Q6
sgs 6400 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 2560 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 35520 0x7F # 01111111   Q6
sgs 50240 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 25600 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 149120 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 25600 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 29440 0x40 # 01000000   Q6
sgs 6400 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 2560 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 35520 0x7F # 01111111   Q6
sgs 50240 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 25600 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 123520 0x40 # 01000000   Q6
sgs 38080 0xBF # 10111111   Q7
```

### sw08-p4  (21 entries, util 9.3600 %)

```
sgs 6720 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 1600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0xBF # 10111111   Q7
sgs 34880 0x40 # 01000000   Q6
sgs 23680 0x7F # 01111111   Q6
sgs 56640 0xBF # 10111111   Q7
sgs 119680 0x80 # 10000000   Q7
sgs 23680 0x7F # 01111111   Q6
sgs 56640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 39040 0x7F # 01111111   Q6
sgs 68160 0x40 # 01000000   Q6
sgs 23680 0x7F # 01111111   Q6
sgs 56640 0xBF # 10111111   Q7
sgs 112960 0x80 # 10000000   Q7
sgs 30400 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (26 entries, util 10.9200 %)

```
sgs 18560 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 14720 0x7F # 01111111   Q6
sgs 37760 0x40 # 01000000   Q6
sgs 2240 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 3520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 16320 0x7F # 01111111   Q6
sgs 46080 0x40 # 01000000   Q6
sgs 23360 0xBF # 10111111   Q7
sgs 18560 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 14720 0x7F # 01111111   Q6
sgs 130880 0x40 # 01000000   Q6
sgs 23360 0xBF # 10111111   Q7
sgs 18560 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 14720 0x7F # 01111111   Q6
sgs 130880 0x40 # 01000000   Q6
sgs 23360 0xBF # 10111111   Q7
sgs 18560 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 14720 0x7F # 01111111   Q6
sgs 112320 0x40 # 01000000   Q6
sgs 41920 0xBF # 10111111   Q7
```

