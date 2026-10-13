# RL-enlarged GCL schedule (Problem 2: window enlargement)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Seeded from SMT run: **result/result-2026-10-12-dataset-testbed-9-ring-avgwin/smt-c9-on/9-fair-retimed-c9on**

## Admission (unchanged) vs. capacity grown

Problem 2 never admits a flow into the schedule it exports -- it only widens windows. `admitted` below is exactly the SMT baseline, by construction; the capacity growth this run achieved is banked slack and per-port GCL entries, reported separately.

| | admitted | of total |
|---|---|---|
| SMT (fixed, never moved) | 11 | 11 |
| RL-enlarged (exported; grow-only, admits nothing new) | 11 | 20 |

During training, the policy's trial admissions (the reward signal that teaches it how much a window needs to grow) reached **7** of the 9 SMT-rejected flows -- none of those are kept in this export; that capacity stays as empty, banked slack for Problem 3 to fill. Total slack banked: 464320 ns. GCL_size overflow: 0.

## Opportunistic idle top-up (deterministic post-pass)

**14408960 ns**, drawn from idle capacity on ports at or below utilisation 0.2, independent of what training happened to grow. Ported from prob_2_heuristic_enlarged's Step 7.

| port | queue | applied (ns) |
|---|---|---|
| S1-p0 | Q6 | 537600 |
| S1-p0 | Q7 | 175040 |
| S2-p0 | Q6 | 237760 |
| S2-p0 | Q7 | 350080 |
| S3-p0 | Q6 | 375040 |
| S3-p0 | Q7 | 237760 |
| sw01-p2 | Q6 | 426240 |
| sw01-p2 | Q7 | 161600 |
| sw01-p4 | Q7 | 605120 |
| sw01-p5 | Q6 | 535040 |
| sw01-p5 | Q7 | 157440 |
| sw02-p2 | Q6 | 168000 |
| sw02-p2 | Q7 | 392000 |
| sw02-p4 | Q6 | 756480 |
| sw02-p5 | Q6 | 373120 |
| sw02-p5 | Q7 | 344320 |
| sw03-p4 | Q6 | 519680 |
| sw03-p4 | Q7 | 172480 |
| sw03-p5 | Q7 | 597440 |
| sw04-p4 | Q6 | 74880 |
| sw04-p4 | Q7 | 560000 |
| sw04-p5 | Q6 | 750400 |
| sw05-p4 | Q7 | 585920 |
| sw05-p5 | Q6 | 524160 |
| sw05-p5 | Q7 | 173120 |
| sw06-p4 | Q6 | 744320 |
| sw06-p5 | Q6 | 67840 |
| sw06-p5 | Q7 | 572160 |
| sw07-p4 | Q6 | 528640 |
| sw07-p4 | Q7 | 173760 |
| sw07-p5 | Q7 | 578240 |
| sw08-p2 | Q6 | 21760 |
| sw08-p2 | Q7 | 578880 |
| sw08-p4 | Q6 | 60800 |
| sw08-p4 | Q7 | 584320 |
| sw08-p5 | Q6 | 533120 |
| sw08-p5 | Q7 | 174400 |

## Opportunistic exclusive window creation (deterministic post-pass)

**5** brand-new *exclusive* window(s) opened, **62400 ns** total, on ports at or below utilisation 0.2 whose TT queue had zero windows before this run. Ported from prob_2_heuristic_enlarged's Step 8.

| port | queue | size (ns) |
|---|---|---|
| sw02-p4 | Q7 | 12480 |
| sw04-p5 | Q7 | 12480 |
| sw05-p4 | Q6 | 12480 |
| sw06-p4 | Q7 | 12480 |
| sw07-p5 | Q6 | 12480 |

## Best-effort gap equalization (deterministic post-pass)

**8401280 ns** given back from the top-up/creation above so each port's leftover non-TAS gaps land close to equal. Ported from prob_2_heuristic_enlarged's Step 9.

| port | given back (ns) |
|---|---|---|
| sw01-p4 | 568640 |
| sw03-p5 | 568640 |
| sw05-p4 | 512000 |
| sw07-p5 | 512000 |
| sw03-p4 | 460160 |
| sw05-p5 | 456000 |
| sw07-p4 | 451840 |
| sw08-p5 | 447680 |
| sw08-p2 | 440000 |
| sw02-p5 | 433280 |
| sw01-p5 | 399680 |
| S1-p0 | 368640 |
| sw04-p4 | 349120 |
| sw06-p5 | 344320 |
| sw08-p4 | 339520 |
| sw01-p2 | 288960 |
| sw02-p2 | 274240 |
| sw02-p4 | 262400 |
| sw04-p5 | 262400 |
| sw06-p4 | 262400 |
| S3-p0 | 237120 |
| S2-p0 | 162240 |

## Opportunistic overlay window creation (deterministic post-pass)

**43** new overlay window(s), **8548480 ns** total, carved out of already-open best-effort spans on ports at or below utilisation 0.2 -- best-effort stays reachable inside each one (gate mask keeps its BE bits set). Run once after training/finalize_grow_only(), not a trained action.

| port | queue | size (ns) |
|---|---|---|
| S1-p0 | Q6 | 168960 |
| S1-p0 | Q7 | 199680 |
| S2-p0 | Q7 | 162240 |
| S3-p0 | Q6 | 24960 |
| S3-p0 | Q7 | 212160 |
| sw01-p2 | Q6 | 74560 |
| sw01-p2 | Q7 | 227200 |
| sw01-p4 | Q6 | 223040 |
| sw01-p4 | Q7 | 345600 |
| sw01-p5 | Q6 | 217280 |
| sw01-p5 | Q7 | 199680 |
| sw02-p2 | Q6 | 135360 |
| sw02-p2 | Q7 | 124160 |
| sw02-p4 | Q6 | 130880 |
| sw02-p4 | Q7 | 150080 |
| sw02-p5 | Q6 | 204800 |
| sw02-p5 | Q7 | 222720 |
| sw03-p4 | Q6 | 223360 |
| sw03-p4 | Q7 | 257280 |
| sw03-p5 | Q6 | 208640 |
| sw03-p5 | Q7 | 360000 |
| sw04-p4 | Q6 | 133440 |
| sw04-p4 | Q7 | 223680 |
| sw04-p5 | Q6 | 136960 |
| sw04-p5 | Q7 | 150080 |
| sw05-p4 | Q6 | 237440 |
| sw05-p4 | Q7 | 274560 |
| sw05-p5 | Q6 | 243840 |
| sw05-p5 | Q7 | 227520 |
| sw06-p4 | Q6 | 143040 |
| sw06-p4 | Q7 | 150080 |
| sw06-p5 | Q6 | 139840 |
| sw06-p5 | Q7 | 205760 |
| sw07-p4 | Q6 | 194560 |
| sw07-p4 | Q7 | 257280 |
| sw07-p5 | Q6 | 249600 |
| sw07-p5 | Q7 | 262400 |
| sw08-p2 | Q6 | 233920 |
| sw08-p2 | Q7 | 230080 |
| sw08-p4 | Q6 | 146240 |
| sw08-p4 | Q7 | 187840 |
| sw08-p5 | Q6 | 206720 |
| sw08-p5 | Q7 | 240960 |

## Per-port GCL entries: before (SMT) vs. after (RL-enlarged)

| port | SMT entries | RL-enlarged entries | GCL_size |
|---|---|---|---|
| sw01-p2 | 19 | 19 | 255 |
| sw01-p4 | 3 | 19 | 255 |
| sw01-p5 | 15 | 22 | 255 |
| sw02-p2 | 25 | 29 | 255 |
| sw02-p4 | 3 | 9 | 255 |
| sw02-p5 | 9 | 17 | 255 |
| sw03-p4 | 11 | 24 | 255 |
| sw03-p5 | 3 | 19 | 255 |
| sw04-p4 | 11 | 25 | 255 |
| sw04-p5 | 3 | 9 | 255 |
| sw05-p4 | 3 | 21 | 255 |
| sw05-p5 | 11 | 22 | 255 |
| sw06-p4 | 3 | 9 | 255 |
| sw06-p5 | 11 | 25 | 255 |
| sw07-p4 | 11 | 19 | 255 |
| sw07-p5 | 3 | 22 | 255 |
| sw08-p2 | 5 | 21 | 255 |
| sw08-p4 | 11 | 25 | 255 |
| sw08-p5 | 11 | 19 | 255 |

## Flows

| flow | route | fixed | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|---|
| s0(id=1 S3->S1) | S3->sw01->sw02->S1 | yes | 6 | 62400 | 24720 | yes |
| s1(id=2 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | no | None | None | None | no |
| s2(id=3 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | no | None | None | None | no |
| s3(id=4 S3->S1) | S3->sw01->sw02->S1 | yes | 7 | 37440 | 33360 | yes |
| s4(id=5 S1->S3) | S1->sw02->sw01->S3 | no | None | None | None | no |
| s5(id=6 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | yes | 6 | 0 | 40720 | yes |
| s6(id=7 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | yes | 6 | 24960 | 33040 | yes |
| s7(id=8 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | yes | 6 | 74880 | 50960 | yes |
| s8(id=9 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | yes | 7 | 87360 | 54160 | yes |
| s9(id=10 S3->S1) | S3->sw01->sw02->S1 | yes | 6 | 12480 | 27920 | yes |
| s10(id=11 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | no | None | None | None | no |
| s11(id=12 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | yes | 6 | 24960 | 36880 | yes |
| s12(id=13 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |
| s13(id=14 S1->S3) | S1->sw02->sw01->S3 | yes | 6 | 0 | 27920 | yes |
| s14(id=15 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | no | None | None | None | no |
| s15(id=16 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | yes | 6 | 49920 | 50000 | yes |
| s16(id=17 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | no | None | None | None | no |
| s17(id=18 S3->S1) | S3->sw01->sw02->S1 | no | None | None | None | no |
| s18(id=19 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | no | None | None | None | no |
| s19(id=20 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | yes | 6 | 99840 | 36880 | yes |

## Per-hop windows (slack_ns > 0 means this window was enlarged)

| flow | egress port | queue | psi (ns) | delta (ns) |
|---|---|---|---|---|
| s0(id=1 S3->S1) | S3-p0 | Q6 | 62400 | 12480 |
| s0(id=1 S3->S1) | sw01-p5 | Q6 | 68480 | 12480 |
| s0(id=1 S3->S1) | sw02-p2 | Q6 | 74560 | 12480 |
| s3(id=4 S3->S1) | S3-p0 | Q7 | 37440 | 12480 |
| s3(id=4 S3->S1) | sw01-p5 | Q7 | 53120 | 12480 |
| s3(id=4 S3->S1) | sw02-p2 | Q7 | 58240 | 12480 |
| s5(id=6 S2->S3) | S2-p0 | Q6 | 0 | 12480 |
| s5(id=6 S2->S3) | sw08-p5 | Q6 | 5120 | 12480 |
| s5(id=6 S2->S3) | sw07-p4 | Q6 | 10240 | 12480 |
| s5(id=6 S2->S3) | sw05-p5 | Q6 | 15360 | 12480 |
| s5(id=6 S2->S3) | sw03-p4 | Q6 | 20480 | 12480 |
| s5(id=6 S2->S3) | sw01-p2 | Q6 | 28160 | 12480 |
| s6(id=7 S2->S1) | S2-p0 | Q6 | 24960 | 12480 |
| s6(id=7 S2->S1) | sw08-p4 | Q6 | 30080 | 12480 |
| s6(id=7 S2->S1) | sw06-p5 | Q6 | 35200 | 12480 |
| s6(id=7 S2->S1) | sw04-p4 | Q6 | 40320 | 12480 |
| s6(id=7 S2->S1) | sw02-p2 | Q6 | 45440 | 12480 |
| s7(id=8 S2->S3) | S2-p0 | Q6 | 74880 | 12480 |
| s7(id=8 S2->S3) | sw08-p5 | Q6 | 82560 | 12480 |
| s7(id=8 S2->S3) | sw07-p4 | Q6 | 90240 | 12480 |
| s7(id=8 S2->S3) | sw05-p5 | Q6 | 97920 | 12480 |
| s7(id=8 S2->S3) | sw03-p4 | Q6 | 105600 | 12480 |
| s7(id=8 S2->S3) | sw01-p2 | Q6 | 113280 | 12480 |
| s8(id=9 S3->S2) | S3-p0 | Q7 | 87360 | 12480 |
| s8(id=9 S3->S2) | sw01-p4 | Q7 | 95680 | 12480 |
| s8(id=9 S3->S2) | sw03-p5 | Q7 | 104000 | 12480 |
| s8(id=9 S3->S2) | sw05-p4 | Q7 | 112320 | 12480 |
| s8(id=9 S3->S2) | sw07-p5 | Q7 | 120640 | 12480 |
| s8(id=9 S3->S2) | sw08-p2 | Q7 | 128960 | 12480 |
| s9(id=10 S3->S1) | S3-p0 | Q6 | 12480 | 12480 |
| s9(id=10 S3->S1) | sw01-p5 | Q6 | 20160 | 12480 |
| s9(id=10 S3->S1) | sw02-p2 | Q6 | 27840 | 12480 |
| s11(id=12 S1->S2) | S1-p0 | Q6 | 24960 | 12480 |
| s11(id=12 S1->S2) | sw02-p4 | Q6 | 31040 | 12480 |
| s11(id=12 S1->S2) | sw04-p5 | Q6 | 37120 | 12480 |
| s11(id=12 S1->S2) | sw06-p4 | Q6 | 43200 | 12480 |
| s11(id=12 S1->S2) | sw08-p2 | Q6 | 49280 | 12480 |
| s13(id=14 S1->S3) | S1-p0 | Q6 | 0 | 12480 |
| s13(id=14 S1->S3) | sw02-p5 | Q6 | 7680 | 12480 |
| s13(id=14 S1->S3) | sw01-p2 | Q6 | 15360 | 12480 |
| s15(id=16 S2->S1) | S2-p0 | Q6 | 49920 | 12480 |
| s15(id=16 S2->S1) | sw08-p4 | Q6 | 60800 | 12480 |
| s15(id=16 S2->S1) | sw06-p5 | Q6 | 69120 | 12480 |
| s15(id=16 S2->S1) | sw04-p4 | Q6 | 77440 | 12480 |
| s15(id=16 S2->S1) | sw02-p2 | Q6 | 87360 | 12480 |
| s19(id=20 S2->S1) | S2-p0 | Q6 | 99840 | 12480 |
| s19(id=20 S2->S1) | sw08-p4 | Q6 | 105920 | 12480 |
| s19(id=20 S2->S1) | sw06-p5 | Q6 | 112000 | 12480 |
| s19(id=20 S2->S1) | sw04-p4 | Q6 | 118080 | 12480 |
| s19(id=20 S2->S1) | sw02-p2 | Q6 | 124160 | 12480 |

## Metrics (training/evaluation signal, not the export)

| metric | value |
|---|---|
| trial-placed flow ratio (fixed + trial-admitted) | 0.900 |
| r1  same-queue window adjacency | 0.473 |
| r2  deadline-violation ratio | 0.000 |
| r3  supplier/receiver overlap | 0.996 |
| r4  mean e2e/deadline (admitted) | 0.126 |
| constraint violations | 0 |

## Constraint check

- C1-C7, C9: OK
- seed-integrity (no SMT-fixed flow's placement changed): OK

## GCL per egress port

### sw01-p2  (19 entries, util 14.0400 %)

```
sgs 15360 0x7F # 01111111   Q6
sgs 25280 0x40 # 01000000   Q6
sgs 640 0x3F # 00111111   BE
sgs 14720 0x80 # 10000000   Q7
sgs 44160 0xBF # 10111111   Q7
sgs 13120 0x7F # 01111111   Q6
sgs 44800 0x40 # 01000000   Q6
sgs 41920 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 142720 0x40 # 01000000   Q6
sgs 41920 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 25280 0x40 # 01000000   Q6
sgs 640 0x3F # 00111111   BE
sgs 116800 0x80 # 10000000   Q7
sgs 41920 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 127360 0x40 # 01000000   Q6
sgs 57280 0xBF # 10111111   Q7
```

### sw01-p4  (19 entries, util 1.5600 %)

```
sgs 6080 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 31360 0x7F # 01111111   Q6
sgs 45760 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 41920 0x7F # 01111111   Q6
sgs 56000 0xBF # 10111111   Q7
sgs 68800 0x80 # 10000000   Q7
sgs 25280 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 56000 0xBF # 10111111   Q7
sgs 68800 0x80 # 10000000   Q7
sgs 25280 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 56000 0xBF # 10111111   Q7
sgs 62720 0x80 # 10000000   Q7
sgs 31360 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p5  (22 entries, util 10.9200 %)

```
sgs 20160 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 20480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 2880 0x3F # 00111111   BE
sgs 62720 0x40 # 01000000   Q6
sgs 18880 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 111040 0x40 # 01000000   Q6
sgs 18880 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 20480 0x7F # 01111111   Q6
sgs 78080 0x80 # 10000000   Q7
sgs 18880 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 90880 0x40 # 01000000   Q6
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (29 entries, util 18.7200 %)

```
sgs 27840 0x7F # 01111111   Q6
sgs 30080 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 3840 0x3F # 00111111   BE
sgs 25280 0x40 # 01000000   Q6
sgs 7360 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 4480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 8320 0x3F # 00111111   BE
sgs 47040 0x80 # 10000000   Q7
sgs 35840 0x7F # 01111111   Q6
sgs 43520 0x40 # 01000000   Q6
sgs 35840 0xBF # 10111111   Q7
sgs 84800 0x80 # 10000000   Q7
sgs 35840 0x7F # 01111111   Q6
sgs 30080 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 7360 0x3F # 00111111   BE
sgs 84800 0x80 # 10000000   Q7
sgs 35840 0x7F # 01111111   Q6
sgs 43520 0x40 # 01000000   Q6
sgs 35840 0xBF # 10111111   Q7
sgs 56960 0x80 # 10000000   Q7
sgs 35840 0xBF # 10111111   Q7
```

### sw02-p4  (9 entries, util 1.5600 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 18560 0x7F # 01111111   Q6
sgs 506560 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p5  (17 entries, util 6.2400 %)

```
sgs 7680 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 2880 0x3F # 00111111   BE
sgs 77760 0x80 # 10000000   Q7
sgs 49280 0x7F # 01111111   Q6
sgs 57600 0xBF # 10111111   Q7
sgs 93120 0x40 # 01000000   Q6
sgs 49280 0x7F # 01111111   Q6
sgs 57600 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 2880 0x3F # 00111111   BE
sgs 77760 0x80 # 10000000   Q7
sgs 49280 0x7F # 01111111   Q6
sgs 57600 0xBF # 10111111   Q7
sgs 85440 0x40 # 01000000   Q6
sgs 56960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (24 entries, util 7.8000 %)

```
sgs 20480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 16960 0x7F # 01111111   Q6
sgs 14400 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 28800 0xBF # 10111111   Q7
sgs 22720 0x40 # 01000000   Q6
sgs 21760 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 107840 0x40 # 01000000   Q6
sgs 21760 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 16960 0x7F # 01111111   Q6
sgs 14400 0xBF # 10111111   Q7
sgs 64000 0x80 # 10000000   Q7
sgs 21760 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 87360 0x40 # 01000000   Q6
sgs 42240 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p5  (19 entries, util 1.5600 %)

```
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0x7F # 01111111   Q6
sgs 54080 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 33600 0x7F # 01111111   Q6
sgs 62080 0xBF # 10111111   Q7
sgs 68800 0x80 # 10000000   Q7
sgs 19200 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 62080 0xBF # 10111111   Q7
sgs 68800 0x80 # 10000000   Q7
sgs 19200 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 62080 0xBF # 10111111   Q7
sgs 56640 0x80 # 10000000   Q7
sgs 31360 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p4  (25 entries, util 7.8000 %)

```
sgs 40320 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 24640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 8960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 6720 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 7680 0x3F # 00111111   BE
sgs 93760 0x80 # 10000000   Q7
sgs 17920 0x7F # 01111111   Q6
sgs 48960 0xBF # 10111111   Q7
sgs 74560 0x80 # 10000000   Q7
sgs 26560 0xBF # 10111111   Q7
sgs 40320 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 24640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 8960 0x3F # 00111111   BE
sgs 133120 0x80 # 10000000   Q7
sgs 17920 0x7F # 01111111   Q6
sgs 48960 0xBF # 10111111   Q7
sgs 34240 0x80 # 10000000   Q7
sgs 16960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (9 entries, util 1.5600 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 24640 0x7F # 01111111   Q6
sgs 500480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (21 entries, util 1.5600 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 19200 0x7F # 01111111   Q6
sgs 62400 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 18240 0x7F # 01111111   Q6
sgs 87680 0x80 # 10000000   Q7
sgs 44160 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 18240 0x7F # 01111111   Q6
sgs 87680 0x80 # 10000000   Q7
sgs 44160 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 18240 0x7F # 01111111   Q6
sgs 69440 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p5  (22 entries, util 7.8000 %)

```
sgs 15360 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 29760 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 27840 0xBF # 10111111   Q7
sgs 25280 0x40 # 01000000   Q6
sgs 26880 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 107840 0x40 # 01000000   Q6
sgs 26880 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 29760 0x7F # 01111111   Q6
sgs 65600 0x80 # 10000000   Q7
sgs 26880 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 92480 0x40 # 01000000   Q6
sgs 42240 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p4  (9 entries, util 1.5600 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 494400 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (25 entries, util 7.8000 %)

```
sgs 35200 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 21440 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 8960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 8960 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 7040 0x3F # 00111111   BE
sgs 92160 0x80 # 10000000   Q7
sgs 26240 0x7F # 01111111   Q6
sgs 40640 0xBF # 10111111   Q7
sgs 77760 0x80 # 10000000   Q7
sgs 31680 0xBF # 10111111   Q7
sgs 35200 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 21440 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 8960 0x3F # 00111111   BE
sgs 133120 0x80 # 10000000   Q7
sgs 26240 0x7F # 01111111   Q6
sgs 40640 0xBF # 10111111   Q7
sgs 42560 0x80 # 10000000   Q7
sgs 16960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (19 entries, util 7.8000 %)

```
sgs 10240 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 28160 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 26880 0xBF # 10111111   Q7
sgs 27840 0x40 # 01000000   Q6
sgs 32000 0x7F # 01111111   Q6
sgs 60160 0xBF # 10111111   Q7
sgs 107840 0x40 # 01000000   Q6
sgs 32000 0x7F # 01111111   Q6
sgs 60160 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 28160 0x7F # 01111111   Q6
sgs 67200 0x80 # 10000000   Q7
sgs 32000 0x7F # 01111111   Q6
sgs 60160 0xBF # 10111111   Q7
sgs 97600 0x40 # 01000000   Q6
sgs 42240 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p5  (22 entries, util 1.5600 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 11840 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 16960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 24320 0x7F # 01111111   Q6
sgs 87680 0x80 # 10000000   Q7
sgs 38080 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 24320 0x7F # 01111111   Q6
sgs 87680 0x80 # 10000000   Q7
sgs 38080 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 24320 0x7F # 01111111   Q6
sgs 63360 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p2  (21 entries, util 3.1200 %)

```
sgs 30400 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 6400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 21760 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 32960 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 58560 0xBF # 10111111   Q7
sgs 30400 0x7F # 01111111   Q6
sgs 103360 0x80 # 10000000   Q7
sgs 16320 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 30400 0x7F # 01111111   Q6
sgs 103360 0x80 # 10000000   Q7
sgs 16320 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 30400 0x7F # 01111111   Q6
sgs 72960 0x80 # 10000000   Q7
sgs 46720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p4  (25 entries, util 7.8000 %)

```
sgs 30080 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 18240 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 8960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 11200 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 6400 0x3F # 00111111   BE
sgs 90560 0x80 # 10000000   Q7
sgs 34560 0x7F # 01111111   Q6
sgs 32320 0xBF # 10111111   Q7
sgs 80960 0x80 # 10000000   Q7
sgs 36800 0xBF # 10111111   Q7
sgs 30080 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 18240 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 8960 0x3F # 00111111   BE
sgs 133120 0x80 # 10000000   Q7
sgs 34560 0x7F # 01111111   Q6
sgs 32320 0xBF # 10111111   Q7
sgs 50880 0x80 # 10000000   Q7
sgs 16960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (19 entries, util 7.8000 %)

```
sgs 5120 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 26560 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 25920 0xBF # 10111111   Q7
sgs 30400 0x40 # 01000000   Q6
sgs 37120 0x7F # 01111111   Q6
sgs 55040 0xBF # 10111111   Q7
sgs 107840 0x40 # 01000000   Q6
sgs 37120 0x7F # 01111111   Q6
sgs 55040 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 26560 0x7F # 01111111   Q6
sgs 68800 0x80 # 10000000   Q7
sgs 37120 0x7F # 01111111   Q6
sgs 55040 0xBF # 10111111   Q7
sgs 102720 0x40 # 01000000   Q6
sgs 42240 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

