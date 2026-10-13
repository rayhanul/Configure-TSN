# RL-enlarged GCL schedule (Problem 2: window enlargement)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Seeded from SMT run: **result/result-2026-10-12-dataset-testbed-8-ring-avgwin/smt-c9-on/8-fair-retimed-c9on**

## Admission (unchanged) vs. capacity grown

Problem 2 never admits a flow into the schedule it exports -- it only widens windows. `admitted` below is exactly the SMT baseline, by construction; the capacity growth this run achieved is banked slack and per-port GCL entries, reported separately.

| | admitted | of total |
|---|---|---|
| SMT (fixed, never moved) | 10 | 10 |
| RL-enlarged (exported; grow-only, admits nothing new) | 10 | 20 |

During training, the policy's trial admissions (the reward signal that teaches it how much a window needs to grow) reached **9** of the 10 SMT-rejected flows -- none of those are kept in this export; that capacity stays as empty, banked slack for Problem 3 to fill. Total slack banked: 788800 ns. GCL_size overflow: 0.

## Opportunistic idle top-up (deterministic post-pass)

**13719680 ns**, drawn from idle capacity on ports at or below utilisation 0.2, independent of what training happened to grow. Ported from prob_2_heuristic_enlarged's Step 7.

| port | queue | applied (ns) |
|---|---|---|
| S1-p0 | Q6 | 100160 |
| S1-p0 | Q7 | 425280 |
| S2-p0 | Q6 | 125120 |
| S2-p0 | Q7 | 500160 |
| S3-p0 | Q6 | 350080 |
| S3-p0 | Q7 | 337600 |
| sw01-p2 | Q6 | 1920 |
| sw01-p2 | Q7 | 454400 |
| sw01-p4 | Q6 | 740480 |
| sw01-p5 | Q6 | 707200 |
| sw01-p5 | Q7 | 320 |
| sw02-p2 | Q6 | 623040 |
| sw02-p2 | Q7 | 29440 |
| sw02-p4 | Q6 | 8960 |
| sw02-p4 | Q7 | 587200 |
| sw02-p5 | Q6 | 318400 |
| sw02-p5 | Q7 | 286080 |
| sw03-p4 | Q6 | 29440 |
| sw03-p4 | Q7 | 484800 |
| sw03-p5 | Q6 | 730880 |
| sw04-p4 | Q6 | 641600 |
| sw04-p4 | Q7 | 48000 |
| sw04-p5 | Q6 | 17920 |
| sw04-p5 | Q7 | 574080 |
| sw05-p4 | Q6 | 721280 |
| sw05-p5 | Q6 | 29760 |
| sw05-p5 | Q7 | 497280 |
| sw06-p4 | Q6 | 26880 |
| sw06-p4 | Q7 | 560960 |
| sw06-p5 | Q6 | 655680 |
| sw06-p5 | Q7 | 39040 |
| sw07-p4 | Q6 | 24320 |
| sw07-p4 | Q7 | 524480 |
| sw07-p5 | Q6 | 711680 |
| sw08-p2 | Q6 | 292480 |
| sw08-p2 | Q7 | 264960 |
| sw08-p4 | Q6 | 662080 |
| sw08-p4 | Q7 | 45440 |
| sw08-p5 | Q6 | 18880 |
| sw08-p5 | Q7 | 521920 |

## Opportunistic exclusive window creation (deterministic post-pass)

**4** brand-new *exclusive* window(s) opened, **49920 ns** total, on ports at or below utilisation 0.2 whose TT queue had zero windows before this run. Ported from prob_2_heuristic_enlarged's Step 8.

| port | queue | size (ns) |
|---|---|---|
| sw01-p4 | Q7 | 12480 |
| sw03-p5 | Q7 | 12480 |
| sw05-p4 | Q7 | 12480 |
| sw07-p5 | Q7 | 12480 |

## Best-effort gap equalization (deterministic post-pass)

**8275520 ns** given back from the top-up/creation above so each port's leftover non-TAS gaps land close to equal. Ported from prob_2_heuristic_enlarged's Step 9.

| port | given back (ns) |
|---|---|---|
| sw03-p4 | 478400 |
| sw05-p5 | 478400 |
| sw07-p4 | 478400 |
| sw08-p5 | 478400 |
| sw06-p4 | 451840 |
| sw04-p5 | 445440 |
| sw02-p5 | 440960 |
| sw02-p4 | 439040 |
| sw08-p2 | 402560 |
| sw01-p4 | 400000 |
| sw03-p5 | 400000 |
| sw05-p4 | 400000 |
| sw07-p5 | 400000 |
| sw04-p4 | 357760 |
| sw08-p4 | 355200 |
| sw06-p5 | 348800 |
| S2-p0 | 321600 |
| S3-p0 | 283200 |
| sw01-p2 | 256960 |
| sw01-p5 | 251840 |
| S1-p0 | 209600 |
| sw02-p2 | 197120 |

## Opportunistic overlay window creation (deterministic post-pass)

**44** new overlay window(s), **8767360 ns** total, carved out of already-open best-effort spans on ports at or below utilisation 0.2 -- best-effort stays reachable inside each one (gate mask keeps its BE bits set). Run once after training/finalize_grow_only(), not a trained action.

| port | queue | size (ns) |
|---|---|---|
| S1-p0 | Q6 | 49920 |
| S1-p0 | Q7 | 159680 |
| S2-p0 | Q6 | 109440 |
| S2-p0 | Q7 | 212160 |
| S3-p0 | Q6 | 160320 |
| S3-p0 | Q7 | 135360 |
| sw01-p2 | Q6 | 136960 |
| sw01-p2 | Q7 | 131520 |
| sw01-p4 | Q6 | 221760 |
| sw01-p4 | Q7 | 200320 |
| sw01-p5 | Q6 | 158400 |
| sw01-p5 | Q7 | 99840 |
| sw02-p2 | Q6 | 95360 |
| sw02-p2 | Q7 | 120320 |
| sw02-p4 | Q6 | 219200 |
| sw02-p4 | Q7 | 219840 |
| sw02-p5 | Q6 | 159040 |
| sw02-p5 | Q7 | 288640 |
| sw03-p4 | Q6 | 256320 |
| sw03-p4 | Q7 | 252480 |
| sw03-p5 | Q6 | 225600 |
| sw03-p5 | Q7 | 206080 |
| sw04-p4 | Q6 | 215360 |
| sw04-p4 | Q7 | 202880 |
| sw04-p5 | Q6 | 259200 |
| sw04-p5 | Q7 | 199680 |
| sw05-p4 | Q6 | 244800 |
| sw05-p4 | Q7 | 196480 |
| sw05-p5 | Q6 | 246400 |
| sw05-p5 | Q7 | 257280 |
| sw06-p4 | Q6 | 222400 |
| sw06-p4 | Q7 | 249600 |
| sw06-p5 | Q6 | 210240 |
| sw06-p5 | Q7 | 193920 |
| sw07-p4 | Q6 | 269760 |
| sw07-p4 | Q7 | 228800 |
| sw07-p5 | Q6 | 237120 |
| sw07-p5 | Q7 | 213760 |
| sw08-p2 | Q6 | 125760 |
| sw08-p2 | Q7 | 299200 |
| sw08-p4 | Q6 | 184960 |
| sw08-p4 | Q7 | 212800 |
| sw08-p5 | Q6 | 223680 |
| sw08-p5 | Q7 | 254720 |

## Per-port GCL entries: before (SMT) vs. after (RL-enlarged)

| port | SMT entries | RL-enlarged entries | GCL_size |
|---|---|---|---|
| sw01-p2 | 25 | 36 | 255 |
| sw01-p4 | 1 | 13 | 255 |
| sw01-p5 | 11 | 16 | 255 |
| sw02-p2 | 15 | 19 | 255 |
| sw02-p4 | 9 | 21 | 255 |
| sw02-p5 | 15 | 24 | 255 |
| sw03-p4 | 11 | 19 | 255 |
| sw03-p5 | 1 | 12 | 255 |
| sw04-p4 | 5 | 13 | 255 |
| sw04-p5 | 9 | 24 | 255 |
| sw05-p4 | 1 | 12 | 255 |
| sw05-p5 | 11 | 19 | 255 |
| sw06-p4 | 9 | 28 | 255 |
| sw06-p5 | 5 | 13 | 255 |
| sw07-p4 | 11 | 21 | 255 |
| sw07-p5 | 1 | 14 | 255 |
| sw08-p2 | 9 | 25 | 255 |
| sw08-p4 | 5 | 14 | 255 |
| sw08-p5 | 11 | 18 | 255 |

## Flows

| flow | route | fixed | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|---|
| s0(id=1 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | no | None | None | None | no |
| s1(id=2 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | yes | 7 | 37440 | 40720 | yes |
| s2(id=3 S3->S1) | S3->sw01->sw02->S1 | no | None | None | None | no |
| s3(id=4 S1->S3) | S1->sw02->sw01->S3 | no | None | None | None | no |
| s4(id=5 S1->S3) | S1->sw02->sw01->S3 | yes | 6 | 87360 | 22800 | yes |
| s5(id=6 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | yes | 7 | 0 | 48080 | yes |
| s6(id=7 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |
| s7(id=8 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | no | None | None | None | no |
| s8(id=9 S3->S1) | S3->sw01->sw02->S1 | yes | 6 | 12480 | 22800 | yes |
| s9(id=10 S1->S3) | S1->sw02->sw01->S3 | yes | 6 | 12480 | 22800 | yes |
| s10(id=11 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | no | None | None | None | no |
| s11(id=12 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | yes | 6 | 62400 | 60560 | yes |
| s12(id=13 S3->S1) | S3->sw01->sw02->S1 | yes | 7 | 62400 | 28560 | yes |
| s13(id=14 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |
| s14(id=15 S3->S1) | S3->sw01->sw02->S1 | no | None | None | None | no |
| s15(id=16 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | no | None | None | None | no |
| s16(id=17 S1->S3) | S1->sw02->sw01->S3 | no | None | None | None | no |
| s17(id=18 S3->S1) | S3->sw01->sw02->S1 | yes | 6 | 37440 | 27920 | yes |
| s18(id=19 S1->S3) | S1->sw02->sw01->S3 | yes | 7 | 62400 | 26000 | yes |
| s19(id=20 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | yes | 7 | 37440 | 45840 | yes |

## Per-hop windows (slack_ns > 0 means this window was enlarged)

| flow | egress port | queue | psi (ns) | delta (ns) |
|---|---|---|---|---|
| s1(id=2 S2->S1) | S2-p0 | Q7 | 37440 | 12480 |
| s1(id=2 S2->S1) | sw08-p4 | Q7 | 42560 | 12480 |
| s1(id=2 S2->S1) | sw06-p5 | Q7 | 55360 | 12480 |
| s1(id=2 S2->S1) | sw04-p4 | Q7 | 60480 | 12480 |
| s1(id=2 S2->S1) | sw02-p2 | Q7 | 65600 | 12480 |
| s4(id=5 S1->S3) | S1-p0 | Q6 | 87360 | 12480 |
| s4(id=5 S1->S3) | sw02-p5 | Q6 | 92480 | 12480 |
| s4(id=5 S1->S3) | sw01-p2 | Q6 | 97600 | 12480 |
| s5(id=6 S2->S3) | S2-p0 | Q7 | 0 | 12480 |
| s5(id=6 S2->S3) | sw08-p5 | Q7 | 5120 | 12480 |
| s5(id=6 S2->S3) | sw07-p4 | Q7 | 20160 | 12480 |
| s5(id=6 S2->S3) | sw05-p5 | Q7 | 25280 | 12480 |
| s5(id=6 S2->S3) | sw03-p4 | Q7 | 30400 | 12480 |
| s5(id=6 S2->S3) | sw01-p2 | Q7 | 35520 | 12480 |
| s8(id=9 S3->S1) | S3-p0 | Q6 | 12480 | 12480 |
| s8(id=9 S3->S1) | sw01-p5 | Q6 | 17600 | 12480 |
| s8(id=9 S3->S1) | sw02-p2 | Q6 | 22720 | 12480 |
| s9(id=10 S1->S3) | S1-p0 | Q6 | 12480 | 12480 |
| s9(id=10 S1->S3) | sw02-p5 | Q6 | 17600 | 12480 |
| s9(id=10 S1->S3) | sw01-p2 | Q6 | 22720 | 12480 |
| s11(id=12 S2->S3) | S2-p0 | Q6 | 62400 | 12480 |
| s11(id=12 S2->S3) | sw08-p5 | Q6 | 70720 | 12480 |
| s11(id=12 S2->S3) | sw07-p4 | Q6 | 79040 | 12480 |
| s11(id=12 S2->S3) | sw05-p5 | Q6 | 87360 | 12480 |
| s11(id=12 S2->S3) | sw03-p4 | Q6 | 95680 | 12480 |
| s11(id=12 S2->S3) | sw01-p2 | Q6 | 110400 | 12480 |
| s12(id=13 S3->S1) | S3-p0 | Q7 | 62400 | 12480 |
| s12(id=13 S3->S1) | sw01-p5 | Q7 | 68480 | 12480 |
| s12(id=13 S3->S1) | sw02-p2 | Q7 | 78400 | 12480 |
| s17(id=18 S3->S1) | S3-p0 | Q6 | 37440 | 12480 |
| s17(id=18 S3->S1) | sw01-p5 | Q6 | 45120 | 12480 |
| s17(id=18 S3->S1) | sw02-p2 | Q6 | 52800 | 12480 |
| s18(id=19 S1->S3) | S1-p0 | Q7 | 62400 | 12480 |
| s18(id=19 S1->S3) | sw02-p5 | Q7 | 69120 | 12480 |
| s18(id=19 S1->S3) | sw01-p2 | Q7 | 75840 | 12480 |
| s19(id=20 S1->S2) | S1-p0 | Q7 | 37440 | 12480 |
| s19(id=20 S1->S2) | sw02-p4 | Q7 | 45760 | 12480 |
| s19(id=20 S1->S2) | sw04-p5 | Q7 | 54080 | 12480 |
| s19(id=20 S1->S2) | sw06-p4 | Q7 | 62400 | 12480 |
| s19(id=20 S1->S2) | sw08-p2 | Q7 | 70720 | 12480 |

## Metrics (training/evaluation signal, not the export)

| metric | value |
|---|---|
| trial-placed flow ratio (fixed + trial-admitted) | 0.950 |
| r1  same-queue window adjacency | 0.300 |
| r2  deadline-violation ratio | 0.000 |
| r3  supplier/receiver overlap | 0.990 |
| r4  mean e2e/deadline (admitted) | 0.156 |
| constraint violations | 0 |

## Constraint check

- C1-C7, C9: OK
- seed-integrity (no SMT-fixed flow's placement changed): OK

## GCL per egress port

### sw01-p2  (36 entries, util 18.7200 %)

```
sgs 22720 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 15360 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 9280 0x3F # 00111111   BE
sgs 25280 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 63680 0x80 # 10000000   Q7
sgs 13120 0xBF # 10111111   Q7
sgs 22720 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 51840 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 63680 0x80 # 10000000   Q7
sgs 13120 0xBF # 10111111   Q7
sgs 22720 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 15360 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 111040 0x80 # 10000000   Q7
sgs 13120 0xBF # 10111111   Q7
sgs 22720 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 51840 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 40960 0x80 # 10000000   Q7
sgs 35840 0xBF # 10111111   Q7
```

### sw01-p4  (13 entries, util 0.0000 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 22080 0x7F # 01111111   Q6
sgs 200000 0x40 # 01000000   Q6
sgs 15360 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 34560 0x7F # 01111111   Q6
sgs 165440 0x40 # 01000000   Q6
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p5  (16 entries, util 7.8000 %)

```
sgs 17600 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 15040 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 10880 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 231040 0x40 # 01000000   Q6
sgs 37760 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 17600 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 15040 0x7F # 01111111   Q6
sgs 249600 0x40 # 01000000   Q6
sgs 55360 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (19 entries, util 10.9200 %)

```
sgs 22720 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 17600 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 640 0x3F # 00111111   BE
sgs 266560 0x40 # 01000000   Q6
sgs 41920 0xBF # 10111111   Q7
sgs 22720 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 17600 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 28480 0xBF # 10111111   Q7
sgs 228800 0x40 # 01000000   Q6
sgs 14720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p4  (21 entries, util 6.2400 %)

```
sgs 6720 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 26560 0x7F # 01111111   Q6
sgs 77760 0x80 # 10000000   Q7
sgs 26560 0x7F # 01111111   Q6
sgs 56640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 26560 0x7F # 01111111   Q6
sgs 77760 0x80 # 10000000   Q7
sgs 26560 0x7F # 01111111   Q6
sgs 56640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 26560 0x7F # 01111111   Q6
sgs 77760 0x80 # 10000000   Q7
sgs 26560 0x7F # 01111111   Q6
sgs 56640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 26560 0x7F # 01111111   Q6
sgs 71040 0x80 # 10000000   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p5  (24 entries, util 10.9200 %)

```
sgs 17600 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 19840 0x7F # 01111111   Q6
sgs 19200 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 10880 0x3F # 00111111   BE
sgs 46080 0x40 # 01000000   Q6
sgs 61440 0xBF # 10111111   Q7
sgs 17600 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 19840 0x7F # 01111111   Q6
sgs 16000 0xBF # 10111111   Q7
sgs 72640 0x80 # 10000000   Q7
sgs 61440 0xBF # 10111111   Q7
sgs 17600 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 19840 0x7F # 01111111   Q6
sgs 19200 0xBF # 10111111   Q7
sgs 69440 0x80 # 10000000   Q7
sgs 61440 0xBF # 10111111   Q7
sgs 17600 0x7F # 01111111   Q6
sgs 103360 0x40 # 01000000   Q6
sgs 29120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (19 entries, util 7.8000 %)

```
sgs 30400 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 52800 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 29440 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
sgs 30400 0x7F # 01111111   Q6
sgs 94720 0x80 # 10000000   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 30400 0x7F # 01111111   Q6
sgs 94720 0x80 # 10000000   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 30400 0x7F # 01111111   Q6
sgs 64320 0x80 # 10000000   Q7
sgs 55360 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p5  (12 entries, util 0.0000 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 31680 0x7F # 01111111   Q6
sgs 200000 0x40 # 01000000   Q6
sgs 56000 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 44160 0x7F # 01111111   Q6
sgs 155840 0x40 # 01000000   Q6
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p4  (13 entries, util 3.1200 %)

```
sgs 60480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24000 0xBF # 10111111   Q7
sgs 208640 0x40 # 01000000   Q6
sgs 44480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 60480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24000 0xBF # 10111111   Q7
sgs 148160 0x40 # 01000000   Q6
sgs 55040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (24 entries, util 6.2400 %)

```
sgs 13440 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 28160 0x7F # 01111111   Q6
sgs 76160 0x80 # 10000000   Q7
sgs 19840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 13440 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 28160 0x7F # 01111111   Q6
sgs 76160 0x80 # 10000000   Q7
sgs 19840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 13440 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 28160 0x7F # 01111111   Q6
sgs 76160 0x80 # 10000000   Q7
sgs 19840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 13440 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 28160 0x7F # 01111111   Q6
sgs 62720 0x80 # 10000000   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (12 entries, util 0.0000 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 41280 0x7F # 01111111   Q6
sgs 200000 0x40 # 01000000   Q6
sgs 46400 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 53760 0x7F # 01111111   Q6
sgs 146240 0x40 # 01000000   Q6
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p5  (19 entries, util 7.8000 %)

```
sgs 25280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 49600 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 29760 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 57920 0xBF # 10111111   Q7
sgs 25280 0x7F # 01111111   Q6
sgs 94720 0x80 # 10000000   Q7
sgs 30080 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 25280 0x7F # 01111111   Q6
sgs 94720 0x80 # 10000000   Q7
sgs 30080 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 25280 0x7F # 01111111   Q6
sgs 69440 0x80 # 10000000   Q7
sgs 55360 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p4  (28 entries, util 6.2400 %)

```
sgs 20160 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 17280 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 74560 0x80 # 10000000   Q7
sgs 13120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 17280 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 74560 0x80 # 10000000   Q7
sgs 13120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 17280 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 74560 0x80 # 10000000   Q7
sgs 13120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 17280 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 54400 0x80 # 10000000   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (13 entries, util 3.1200 %)

```
sgs 55360 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 19520 0xBF # 10111111   Q7
sgs 213120 0x40 # 01000000   Q6
sgs 49600 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 55360 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 19520 0xBF # 10111111   Q7
sgs 157760 0x40 # 01000000   Q6
sgs 55040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (21 entries, util 7.8000 %)

```
sgs 20160 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 17280 0x7F # 01111111   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 24320 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 21760 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 94720 0x80 # 10000000   Q7
sgs 35200 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 94720 0x80 # 10000000   Q7
sgs 35200 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 74560 0x80 # 10000000   Q7
sgs 55360 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p5  (14 entries, util 0.0000 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 13440 0xBF # 10111111   Q7
sgs 200000 0x40 # 01000000   Q6
sgs 36800 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 13440 0xBF # 10111111   Q7
sgs 136640 0x40 # 01000000   Q6
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p2  (25 entries, util 6.2400 %)

```
sgs 26880 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 31360 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 2240 0x3F # 00111111   BE
sgs 73280 0x40 # 01000000   Q6
sgs 41280 0xBF # 10111111   Q7
sgs 26880 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 31360 0xBF # 10111111   Q7
sgs 88000 0x80 # 10000000   Q7
sgs 41280 0xBF # 10111111   Q7
sgs 26880 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 31360 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 2240 0x3F # 00111111   BE
sgs 73280 0x40 # 01000000   Q6
sgs 41280 0xBF # 10111111   Q7
sgs 26880 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 31360 0xBF # 10111111   Q7
sgs 61120 0x80 # 10000000   Q7
sgs 18240 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p4  (14 entries, util 3.1200 %)

```
sgs 42560 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 22720 0xBF # 10111111   Q7
sgs 209920 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 42560 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 22720 0xBF # 10111111   Q7
sgs 167360 0x40 # 01000000   Q6
sgs 55040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (18 entries, util 7.8000 %)

```
sgs 5120 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 32320 0x7F # 01111111   Q6
sgs 20800 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 18880 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 35520 0x7F # 01111111   Q6
sgs 55040 0xBF # 10111111   Q7
sgs 94720 0x80 # 10000000   Q7
sgs 50240 0x7F # 01111111   Q6
sgs 55040 0xBF # 10111111   Q7
sgs 94720 0x80 # 10000000   Q7
sgs 50240 0x7F # 01111111   Q6
sgs 55040 0xBF # 10111111   Q7
sgs 89600 0x80 # 10000000   Q7
sgs 55360 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

