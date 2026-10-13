# RL-enlarged GCL schedule (Problem 2: window enlargement)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Seeded from SMT run: **result/result-2026-10-13-dataset-testbed-13-tree-avgwin/smt-c9-on/13-fair-retimed-c9on**

## Admission (unchanged) vs. capacity grown

Problem 2 never admits a flow into the schedule it exports -- it only widens windows. `admitted` below is exactly the SMT baseline, by construction; the capacity growth this run achieved is banked slack and per-port GCL entries, reported separately.

| | admitted | of total |
|---|---|---|
| SMT (fixed, never moved) | 11 | 11 |
| RL-enlarged (exported; grow-only, admits nothing new) | 11 | 20 |

During training, the policy's trial admissions (the reward signal that teaches it how much a window needs to grow) reached **6** of the 9 SMT-rejected flows -- none of those are kept in this export; that capacity stays as empty, banked slack for Problem 3 to fill. Total slack banked: 188480 ns. GCL_size overflow: 0.

## Opportunistic idle top-up (deterministic post-pass)

**11501760 ns**, drawn from idle capacity on ports at or below utilisation 0.2, independent of what training happened to grow. Ported from prob_2_heuristic_enlarged's Step 7.

| port | queue | applied (ns) |
|---|---|---|
| S1-p0 | Q6 | 350080 |
| S1-p0 | Q7 | 300160 |
| S3-p0 | Q6 | 525120 |
| S3-p0 | Q7 | 125120 |
| sw01-p2 | Q6 | 451840 |
| sw01-p2 | Q7 | 89600 |
| sw01-p4 | Q6 | 487040 |
| sw01-p4 | Q7 | 125120 |
| sw02-p2 | Q6 | 302720 |
| sw02-p2 | Q7 | 308160 |
| sw02-p4 | Q6 | 429440 |
| sw02-p4 | Q7 | 214720 |
| sw03-p4 | Q6 | 454400 |
| sw03-p4 | Q7 | 92160 |
| sw03-p5 | Q6 | 479680 |
| sw03-p5 | Q7 | 125120 |
| sw04-p4 | Q6 | 312320 |
| sw04-p4 | Q7 | 305280 |
| sw04-p5 | Q6 | 415360 |
| sw04-p5 | Q7 | 210880 |
| sw05-p4 | Q6 | 482560 |
| sw05-p4 | Q7 | 125120 |
| sw05-p5 | Q6 | 456960 |
| sw05-p5 | Q7 | 94720 |
| sw06-p4 | Q6 | 379520 |
| sw06-p4 | Q7 | 248000 |
| sw06-p5 | Q6 | 327040 |
| sw06-p5 | Q7 | 297280 |
| sw07-p4 | Q6 | 459520 |
| sw07-p4 | Q7 | 97280 |
| sw07-p5 | Q6 | 485440 |
| sw07-p5 | Q7 | 125120 |
| sw08-p2 | Q6 | 598080 |
| sw08-p2 | Q7 | 27840 |
| sw08-p4 | Q6 | 336640 |
| sw08-p4 | Q7 | 294400 |
| sw08-p5 | Q6 | 462080 |
| sw08-p5 | Q7 | 99840 |

## Best-effort gap equalization (deterministic post-pass)

**7188160 ns** given back from the top-up/creation above so each port's leftover non-TAS gaps land close to equal. Ported from prob_2_heuristic_enlarged's Step 9.

| port | given back (ns) |
|---|---|---|
| sw06-p4 | 460480 |
| sw04-p5 | 441920 |
| S3-p0 | 418240 |
| sw01-p4 | 416000 |
| sw03-p5 | 413760 |
| sw05-p4 | 411520 |
| sw07-p5 | 409280 |
| sw02-p2 | 399360 |
| sw04-p4 | 397440 |
| sw06-p5 | 395520 |
| sw08-p4 | 393600 |
| sw01-p2 | 368960 |
| sw03-p4 | 367680 |
| sw05-p5 | 366400 |
| sw07-p4 | 365120 |
| sw08-p5 | 363840 |
| sw08-p2 | 282560 |
| sw02-p4 | 272640 |
| S1-p0 | 218880 |
| S2-p0 | 24960 |

## Opportunistic overlay window creation (deterministic post-pass)

**36** new overlay window(s), **7407040 ns** total, carved out of already-open best-effort spans on ports at or below utilisation 0.2 -- best-effort stays reachable inside each one (gate mask keeps its BE bits set). Run once after training/finalize_grow_only(), not a trained action.

| port | queue | size (ns) |
|---|---|---|
| S1-p0 | Q7 | 218880 |
| S3-p0 | Q6 | 206080 |
| S3-p0 | Q7 | 212160 |
| sw01-p2 | Q6 | 308480 |
| sw01-p2 | Q7 | 114240 |
| sw01-p4 | Q6 | 176640 |
| sw01-p4 | Q7 | 239360 |
| sw02-p2 | Q6 | 107520 |
| sw02-p2 | Q7 | 316160 |
| sw02-p4 | Q7 | 254400 |
| sw03-p4 | Q6 | 302080 |
| sw03-p4 | Q7 | 110720 |
| sw03-p5 | Q6 | 213760 |
| sw03-p5 | Q7 | 216640 |
| sw04-p4 | Q6 | 142080 |
| sw04-p4 | Q7 | 271680 |
| sw04-p5 | Q6 | 76160 |
| sw04-p5 | Q7 | 344320 |
| sw05-p4 | Q6 | 217600 |
| sw05-p4 | Q7 | 218880 |
| sw05-p5 | Q6 | 269440 |
| sw05-p5 | Q7 | 133440 |
| sw06-p4 | Q6 | 107520 |
| sw06-p4 | Q7 | 364480 |
| sw06-p5 | Q6 | 146560 |
| sw06-p5 | Q7 | 257280 |
| sw07-p4 | Q6 | 250880 |
| sw07-p4 | Q7 | 142080 |
| sw07-p5 | Q6 | 172160 |
| sw07-p5 | Q7 | 270400 |
| sw08-p2 | Q6 | 97280 |
| sw08-p2 | Q7 | 181760 |
| sw08-p4 | Q6 | 138240 |
| sw08-p4 | Q7 | 248960 |
| sw08-p5 | Q6 | 181440 |
| sw08-p5 | Q7 | 177280 |

## Per-port GCL entries: before (SMT) vs. after (RL-enlarged)

| port | SMT entries | RL-enlarged entries | GCL_size |
|---|---|---|---|
| sw01-p2 | 21 | 23 | 255 |
| sw01-p4 | 15 | 19 | 255 |
| sw02-p2 | 13 | 28 | 255 |
| sw02-p4 | 15 | 21 | 255 |
| sw03-p4 | 21 | 25 | 255 |
| sw03-p5 | 15 | 22 | 255 |
| sw04-p4 | 13 | 34 | 255 |
| sw04-p5 | 15 | 23 | 255 |
| sw05-p4 | 15 | 22 | 255 |
| sw05-p5 | 21 | 25 | 255 |
| sw06-p4 | 15 | 24 | 255 |
| sw06-p5 | 13 | 32 | 255 |
| sw07-p4 | 21 | 25 | 255 |
| sw07-p5 | 15 | 19 | 255 |
| sw08-p2 | 23 | 28 | 255 |
| sw08-p4 | 13 | 29 | 255 |
| sw08-p5 | 21 | 28 | 255 |

## Flows

| flow | route | fixed | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|---|
| s0(id=1 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | no | None | None | None | no |
| s1(id=2 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | no | None | None | None | no |
| s2(id=3 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | yes | 7 | 24960 | 74000 | yes |
| s3(id=4 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |
| s4(id=5 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | yes | 6 | 0 | 54160 | yes |
| s5(id=6 S3->S1) | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | no | None | None | None | no |
| s6(id=7 S3->S1) | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | no | None | None | None | no |
| s7(id=8 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | yes | 7 | 62400 | 54160 | yes |
| s8(id=9 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | yes | 6 | 37440 | 42960 | yes |
| s9(id=10 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | yes | 7 | 0 | 39440 | yes |
| s10(id=11 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |
| s11(id=12 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |
| s12(id=13 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | yes | 7 | 49920 | 45840 | yes |
| s13(id=14 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | yes | 7 | 0 | 36880 | yes |
| s14(id=15 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | yes | 7 | 49920 | 61840 | yes |
| s15(id=16 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |
| s16(id=17 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | yes | 6 | 99840 | 38160 | yes |
| s17(id=18 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | no | None | None | None | no |
| s18(id=19 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | yes | 6 | 24960 | 42960 | yes |
| s19(id=20 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | yes | 6 | 74880 | 49680 | yes |

## Per-hop windows (slack_ns > 0 means this window was enlarged)

| flow | egress port | queue | psi (ns) | delta (ns) |
|---|---|---|---|---|
| s2(id=3 S1->S3) | S1-p0 | Q7 | 24960 | 12480 |
| s2(id=3 S1->S3) | sw02-p4 | Q7 | 32640 | 12480 |
| s2(id=3 S1->S3) | sw04-p5 | Q7 | 40320 | 12480 |
| s2(id=3 S1->S3) | sw06-p4 | Q7 | 48000 | 12480 |
| s2(id=3 S1->S3) | sw08-p5 | Q7 | 55680 | 12480 |
| s2(id=3 S1->S3) | sw07-p4 | Q7 | 63360 | 12480 |
| s2(id=3 S1->S3) | sw05-p5 | Q7 | 71040 | 12480 |
| s2(id=3 S1->S3) | sw03-p4 | Q7 | 78720 | 12480 |
| s2(id=3 S1->S3) | sw01-p2 | Q7 | 86400 | 12480 |
| s4(id=5 S3->S2) | S3-p0 | Q6 | 0 | 12480 |
| s4(id=5 S3->S2) | sw01-p4 | Q6 | 8320 | 12480 |
| s4(id=5 S3->S2) | sw03-p5 | Q6 | 16640 | 12480 |
| s4(id=5 S3->S2) | sw05-p4 | Q6 | 24960 | 12480 |
| s4(id=5 S3->S2) | sw07-p5 | Q6 | 33280 | 12480 |
| s4(id=5 S3->S2) | sw08-p2 | Q6 | 41600 | 12480 |
| s7(id=8 S3->S2) | S3-p0 | Q7 | 62400 | 12480 |
| s7(id=8 S3->S2) | sw01-p4 | Q7 | 70720 | 12480 |
| s7(id=8 S3->S2) | sw03-p5 | Q7 | 79040 | 12480 |
| s7(id=8 S3->S2) | sw05-p4 | Q7 | 87360 | 12480 |
| s7(id=8 S3->S2) | sw07-p5 | Q7 | 95680 | 12480 |
| s7(id=8 S3->S2) | sw08-p2 | Q7 | 104000 | 12480 |
| s8(id=9 S3->S2) | S3-p0 | Q6 | 37440 | 12480 |
| s8(id=9 S3->S2) | sw01-p4 | Q6 | 43520 | 12480 |
| s8(id=9 S3->S2) | sw03-p5 | Q6 | 49600 | 12480 |
| s8(id=9 S3->S2) | sw05-p4 | Q6 | 55680 | 12480 |
| s8(id=9 S3->S2) | sw07-p5 | Q6 | 61760 | 12480 |
| s8(id=9 S3->S2) | sw08-p2 | Q6 | 67840 | 12480 |
| s9(id=10 S2->S1) | S2-p0 | Q7 | 0 | 12480 |
| s9(id=10 S2->S1) | sw08-p4 | Q7 | 6720 | 12480 |
| s9(id=10 S2->S1) | sw06-p5 | Q7 | 13440 | 12480 |
| s9(id=10 S2->S1) | sw04-p4 | Q7 | 20160 | 12480 |
| s9(id=10 S2->S1) | sw02-p2 | Q7 | 26880 | 12480 |
| s12(id=13 S2->S1) | S2-p0 | Q7 | 49920 | 12480 |
| s12(id=13 S2->S1) | sw08-p4 | Q7 | 58240 | 12480 |
| s12(id=13 S2->S1) | sw06-p5 | Q7 | 66560 | 12480 |
| s12(id=13 S2->S1) | sw04-p4 | Q7 | 74880 | 12480 |
| s12(id=13 S2->S1) | sw02-p2 | Q7 | 83200 | 12480 |
| s13(id=14 S1->S2) | S1-p0 | Q7 | 0 | 12480 |
| s13(id=14 S1->S2) | sw02-p4 | Q7 | 6080 | 12480 |
| s13(id=14 S1->S2) | sw04-p5 | Q7 | 12160 | 12480 |
| s13(id=14 S1->S2) | sw06-p4 | Q7 | 18240 | 12480 |
| s13(id=14 S1->S2) | sw08-p2 | Q7 | 24320 | 12480 |
| s14(id=15 S1->S3) | S1-p0 | Q7 | 49920 | 12480 |
| s14(id=15 S1->S3) | sw02-p4 | Q7 | 56960 | 12480 |
| s14(id=15 S1->S3) | sw04-p5 | Q7 | 62080 | 12480 |
| s14(id=15 S1->S3) | sw06-p4 | Q7 | 67200 | 12480 |
| s14(id=15 S1->S3) | sw08-p5 | Q7 | 72320 | 12480 |
| s14(id=15 S1->S3) | sw07-p4 | Q7 | 78720 | 12480 |
| s14(id=15 S1->S3) | sw05-p5 | Q7 | 83840 | 12480 |
| s14(id=15 S1->S3) | sw03-p4 | Q7 | 91520 | 12480 |
| s14(id=15 S1->S3) | sw01-p2 | Q7 | 99200 | 12480 |
| s16(id=17 S2->S3) | S2-p0 | Q6 | 99840 | 12480 |
| s16(id=17 S2->S3) | sw08-p5 | Q6 | 104960 | 12480 |
| s16(id=17 S2->S3) | sw07-p4 | Q6 | 110080 | 12480 |
| s16(id=17 S2->S3) | sw05-p5 | Q6 | 115200 | 12480 |
| s16(id=17 S2->S3) | sw03-p4 | Q6 | 120320 | 12480 |
| s16(id=17 S2->S3) | sw01-p2 | Q6 | 125440 | 12480 |
| s18(id=19 S2->S3) | S2-p0 | Q6 | 24960 | 12480 |
| s18(id=19 S2->S3) | sw08-p5 | Q6 | 31040 | 12480 |
| s18(id=19 S2->S3) | sw07-p4 | Q6 | 37120 | 12480 |
| s18(id=19 S2->S3) | sw05-p5 | Q6 | 43200 | 12480 |
| s18(id=19 S2->S3) | sw03-p4 | Q6 | 49280 | 12480 |
| s18(id=19 S2->S3) | sw01-p2 | Q6 | 55360 | 12480 |
| s19(id=20 S2->S3) | S2-p0 | Q6 | 74880 | 12480 |
| s19(id=20 S2->S3) | sw08-p5 | Q6 | 85120 | 12480 |
| s19(id=20 S2->S3) | sw07-p4 | Q6 | 91840 | 12480 |
| s19(id=20 S2->S3) | sw05-p5 | Q6 | 98560 | 12480 |
| s19(id=20 S2->S3) | sw03-p4 | Q6 | 105280 | 12480 |
| s19(id=20 S2->S3) | sw01-p2 | Q6 | 112000 | 12480 |

## Metrics (training/evaluation signal, not the export)

| metric | value |
|---|---|
| trial-placed flow ratio (fixed + trial-admitted) | 0.850 |
| r1  same-queue window adjacency | 0.391 |
| r2  deadline-violation ratio | 0.000 |
| r3  supplier/receiver overlap | 0.996 |
| r4  mean e2e/deadline (admitted) | 0.192 |
| constraint violations | 0 |

## Constraint check

- C1-C7, C9: OK
- seed-integrity (no SMT-fixed flow's placement changed): OK

## GCL per egress port

### sw01-p2  (23 entries, util 15.6000 %)

```
sgs 55360 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 18560 0xBF # 10111111   Q7
sgs 25280 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 25920 0x40 # 01000000   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 40320 0x80 # 10000000   Q7
sgs 48000 0x7F # 01111111   Q6
sgs 35840 0x40 # 01000000   Q6
sgs 48000 0x7F # 01111111   Q6
sgs 68160 0x40 # 01000000   Q6
sgs 48000 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 18560 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0x7F # 01111111   Q6
sgs 95360 0x40 # 01000000   Q6
sgs 48000 0x7F # 01111111   Q6
sgs 35840 0x40 # 01000000   Q6
sgs 48000 0x7F # 01111111   Q6
sgs 12800 0x40 # 01000000   Q6
sgs 48000 0xBF # 10111111   Q7
```

### sw01-p4  (19 entries, util 10.9200 %)

```
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 22720 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 14720 0xBF # 10111111   Q7
sgs 48640 0x80 # 10000000   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 58240 0xBF # 10111111   Q7
sgs 111040 0x40 # 01000000   Q6
sgs 30720 0x7F # 01111111   Q6
sgs 58240 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 22720 0x7F # 01111111   Q6
sgs 75840 0x40 # 01000000   Q6
sgs 30720 0x7F # 01111111   Q6
sgs 58240 0xBF # 10111111   Q7
sgs 102720 0x40 # 01000000   Q6
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (28 entries, util 9.3600 %)

```
sgs 26880 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 43840 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 1920 0x3F # 00111111   BE
sgs 52480 0x40 # 01000000   Q6
sgs 24640 0xBF # 10111111   Q7
sgs 26880 0x7F # 01111111   Q6
sgs 17280 0x80 # 10000000   Q7
sgs 51520 0xBF # 10111111   Q7
sgs 79680 0x40 # 01000000   Q6
sgs 24640 0xBF # 10111111   Q7
sgs 26880 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 43840 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 66880 0x80 # 10000000   Q7
sgs 24640 0xBF # 10111111   Q7
sgs 26880 0x7F # 01111111   Q6
sgs 17280 0x80 # 10000000   Q7
sgs 51520 0xBF # 10111111   Q7
sgs 52800 0x40 # 01000000   Q6
sgs 51520 0xBF # 10111111   Q7
```

### sw02-p4  (21 entries, util 10.9200 %)

```
sgs 6080 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 1600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 36800 0x80 # 10000000   Q7
sgs 35520 0xBF # 10111111   Q7
sgs 46400 0x40 # 01000000   Q6
sgs 54720 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 1600 0x3F # 00111111   BE
sgs 131200 0x40 # 01000000   Q6
sgs 54720 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 1600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 118720 0x80 # 10000000   Q7
sgs 54720 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 1600 0x3F # 00111111   BE
sgs 125120 0x40 # 01000000   Q6
sgs 54720 0xBF # 10111111   Q7
```

### sw03-p4  (25 entries, util 15.6000 %)

```
sgs 49280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 16960 0xBF # 10111111   Q7
sgs 25280 0x80 # 10000000   Q7
sgs 1280 0x3F # 00111111   BE
sgs 27520 0x40 # 01000000   Q6
sgs 27520 0x7F # 01111111   Q6
sgs 40960 0x80 # 10000000   Q7
sgs 48000 0x7F # 01111111   Q6
sgs 36480 0x40 # 01000000   Q6
sgs 14400 0xBF # 10111111   Q7
sgs 33600 0x7F # 01111111   Q6
sgs 67520 0x40 # 01000000   Q6
sgs 48000 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 16960 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 14080 0x7F # 01111111   Q6
sgs 96000 0x40 # 01000000   Q6
sgs 48000 0x7F # 01111111   Q6
sgs 36480 0x40 # 01000000   Q6
sgs 14400 0xBF # 10111111   Q7
sgs 33600 0x7F # 01111111   Q6
sgs 18240 0x40 # 01000000   Q6
sgs 48000 0xBF # 10111111   Q7
```

### sw03-p5  (22 entries, util 10.9200 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 20480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 16960 0xBF # 10111111   Q7
sgs 48640 0x80 # 10000000   Q7
sgs 22400 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 111040 0x40 # 01000000   Q6
sgs 22400 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 20480 0x7F # 01111111   Q6
sgs 78080 0x40 # 01000000   Q6
sgs 22400 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 94400 0x40 # 01000000   Q6
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p4  (34 entries, util 9.3600 %)

```
sgs 20160 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 17280 0x7F # 01111111   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 1920 0x3F # 00111111   BE
sgs 53440 0x40 # 01000000   Q6
sgs 31360 0xBF # 10111111   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 16320 0x80 # 10000000   Q7
sgs 13440 0x7F # 01111111   Q6
sgs 38080 0xBF # 10111111   Q7
sgs 80640 0x40 # 01000000   Q6
sgs 31360 0xBF # 10111111   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 17280 0x7F # 01111111   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 67840 0x80 # 10000000   Q7
sgs 31360 0xBF # 10111111   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 16320 0x80 # 10000000   Q7
sgs 13440 0x7F # 01111111   Q6
sgs 38080 0xBF # 10111111   Q7
sgs 60480 0x40 # 01000000   Q6
sgs 51520 0xBF # 10111111   Q7
```

### sw04-p5  (23 entries, util 10.9200 %)

```
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 15680 0x7F # 01111111   Q6
sgs 34240 0x80 # 10000000   Q7
sgs 12160 0x3F # 00111111   BE
sgs 66240 0x40 # 01000000   Q6
sgs 59200 0xBF # 10111111   Q7
sgs 15360 0x80 # 10000000   Q7
sgs 22400 0x7F # 01111111   Q6
sgs 36800 0xBF # 10111111   Q7
sgs 66240 0x40 # 01000000   Q6
sgs 59200 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 15680 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 33920 0xBF # 10111111   Q7
sgs 66240 0x40 # 01000000   Q6
sgs 59200 0xBF # 10111111   Q7
sgs 15360 0x80 # 10000000   Q7
sgs 22400 0x7F # 01111111   Q6
sgs 36800 0xBF # 10111111   Q7
sgs 54080 0x40 # 01000000   Q6
sgs 59200 0xBF # 10111111   Q7
```

### sw05-p4  (22 entries, util 10.9200 %)

```
sgs 24960 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 18240 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 19200 0xBF # 10111111   Q7
sgs 48640 0x80 # 10000000   Q7
sgs 14080 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 111040 0x40 # 01000000   Q6
sgs 14080 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 18240 0x7F # 01111111   Q6
sgs 80320 0x40 # 01000000   Q6
sgs 14080 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 86080 0x40 # 01000000   Q6
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p5  (25 entries, util 15.6000 %)

```
sgs 43200 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 15360 0xBF # 10111111   Q7
sgs 25280 0x80 # 10000000   Q7
sgs 2240 0x3F # 00111111   BE
sgs 29120 0x40 # 01000000   Q6
sgs 25920 0x7F # 01111111   Q6
sgs 41600 0x80 # 10000000   Q7
sgs 48000 0x7F # 01111111   Q6
sgs 37120 0x40 # 01000000   Q6
sgs 19840 0xBF # 10111111   Q7
sgs 28160 0x7F # 01111111   Q6
sgs 66880 0x40 # 01000000   Q6
sgs 48000 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 15360 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 15040 0xBF # 10111111   Q7
sgs 96640 0x40 # 01000000   Q6
sgs 48000 0x7F # 01111111   Q6
sgs 37120 0x40 # 01000000   Q6
sgs 19840 0xBF # 10111111   Q7
sgs 28160 0x7F # 01111111   Q6
sgs 23680 0x40 # 01000000   Q6
sgs 48000 0xBF # 10111111   Q7
```

### sw06-p4  (24 entries, util 10.9200 %)

```
sgs 18240 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 17280 0x7F # 01111111   Q6
sgs 31680 0x80 # 10000000   Q7
sgs 22400 0xBF # 10111111   Q7
sgs 56960 0x40 # 01000000   Q6
sgs 40960 0xBF # 10111111   Q7
sgs 18240 0x7F # 01111111   Q6
sgs 24640 0x80 # 10000000   Q7
sgs 59200 0xBF # 10111111   Q7
sgs 56960 0x40 # 01000000   Q6
sgs 40960 0xBF # 10111111   Q7
sgs 18240 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 17280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 41600 0xBF # 10111111   Q7
sgs 56960 0x40 # 01000000   Q6
sgs 40960 0xBF # 10111111   Q7
sgs 18240 0x7F # 01111111   Q6
sgs 24640 0x80 # 10000000   Q7
sgs 59200 0xBF # 10111111   Q7
sgs 38720 0x40 # 01000000   Q6
sgs 59200 0xBF # 10111111   Q7
```

### sw06-p5  (32 entries, util 9.3600 %)

```
sgs 13440 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24000 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 1600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 1920 0x3F # 00111111   BE
sgs 54400 0x40 # 01000000   Q6
sgs 38080 0xBF # 10111111   Q7
sgs 13440 0x7F # 01111111   Q6
sgs 14080 0x80 # 10000000   Q7
sgs 22400 0x7F # 01111111   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 82880 0x40 # 01000000   Q6
sgs 38080 0xBF # 10111111   Q7
sgs 13440 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24000 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 1600 0x3F # 00111111   BE
sgs 68800 0x80 # 10000000   Q7
sgs 38080 0xBF # 10111111   Q7
sgs 13440 0x7F # 01111111   Q6
sgs 14080 0x80 # 10000000   Q7
sgs 22400 0x7F # 01111111   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 69440 0x40 # 01000000   Q6
sgs 51520 0xBF # 10111111   Q7
```

### sw07-p4  (25 entries, util 15.6000 %)

```
sgs 37120 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 13760 0xBF # 10111111   Q7
sgs 27840 0x80 # 10000000   Q7
sgs 640 0x3F # 00111111   BE
sgs 30720 0x40 # 01000000   Q6
sgs 24320 0x7F # 01111111   Q6
sgs 42240 0x80 # 10000000   Q7
sgs 48000 0x7F # 01111111   Q6
sgs 37760 0x40 # 01000000   Q6
sgs 25280 0xBF # 10111111   Q7
sgs 22720 0x7F # 01111111   Q6
sgs 66240 0x40 # 01000000   Q6
sgs 48000 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 13760 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 16000 0xBF # 10111111   Q7
sgs 97280 0x40 # 01000000   Q6
sgs 48000 0x7F # 01111111   Q6
sgs 37760 0x40 # 01000000   Q6
sgs 25280 0xBF # 10111111   Q7
sgs 22720 0x7F # 01111111   Q6
sgs 29120 0x40 # 01000000   Q6
sgs 48000 0xBF # 10111111   Q7
```

### sw07-p5  (19 entries, util 10.9200 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 16000 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 21440 0xBF # 10111111   Q7
sgs 48640 0x80 # 10000000   Q7
sgs 55680 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 111040 0x40 # 01000000   Q6
sgs 55680 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 16000 0xBF # 10111111   Q7
sgs 82560 0x40 # 01000000   Q6
sgs 55680 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 77760 0x40 # 01000000   Q6
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p2  (28 entries, util 17.1600 %)

```
sgs 24320 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 4800 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 13760 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 23680 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 8640 0x3F # 00111111   BE
sgs 48320 0x40 # 01000000   Q6
sgs 26560 0xBF # 10111111   Q7
sgs 24320 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 4800 0x3F # 00111111   BE
sgs 131840 0x40 # 01000000   Q6
sgs 26560 0xBF # 10111111   Q7
sgs 24320 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 4800 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 13760 0xBF # 10111111   Q7
sgs 105600 0x40 # 01000000   Q6
sgs 26560 0xBF # 10111111   Q7
sgs 24320 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 4800 0x3F # 00111111   BE
sgs 107520 0x40 # 01000000   Q6
sgs 50880 0xBF # 10111111   Q7
```

### sw08-p4  (29 entries, util 9.3600 %)

```
sgs 6720 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 39040 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 1600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 1920 0x3F # 00111111   BE
sgs 55360 0x40 # 01000000   Q6
sgs 51520 0xBF # 10111111   Q7
sgs 13120 0x80 # 10000000   Q7
sgs 30080 0x7F # 01111111   Q6
sgs 21440 0xBF # 10111111   Q7
sgs 83840 0x40 # 01000000   Q6
sgs 51520 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 39040 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 1600 0x3F # 00111111   BE
sgs 69760 0x80 # 10000000   Q7
sgs 51520 0xBF # 10111111   Q7
sgs 13120 0x80 # 10000000   Q7
sgs 30080 0x7F # 01111111   Q6
sgs 21440 0xBF # 10111111   Q7
sgs 77120 0x40 # 01000000   Q6
sgs 51520 0xBF # 10111111   Q7
```

### sw08-p5  (28 entries, util 15.6000 %)

```
sgs 31040 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12160 0x3F # 00111111   BE
sgs 29120 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 32320 0x40 # 01000000   Q6
sgs 22720 0x7F # 01111111   Q6
sgs 42880 0x80 # 10000000   Q7
sgs 16960 0xBF # 10111111   Q7
sgs 31040 0x7F # 01111111   Q6
sgs 38400 0x40 # 01000000   Q6
sgs 30720 0xBF # 10111111   Q7
sgs 17280 0x7F # 01111111   Q6
sgs 65600 0x40 # 01000000   Q6
sgs 16960 0xBF # 10111111   Q7
sgs 31040 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 16960 0xBF # 10111111   Q7
sgs 97920 0x40 # 01000000   Q6
sgs 16960 0xBF # 10111111   Q7
sgs 31040 0x7F # 01111111   Q6
sgs 38400 0x40 # 01000000   Q6
sgs 30720 0xBF # 10111111   Q7
sgs 17280 0x7F # 01111111   Q6
sgs 34560 0x40 # 01000000   Q6
sgs 48000 0xBF # 10111111   Q7
```

