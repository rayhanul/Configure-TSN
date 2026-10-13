# RL-enlarged GCL schedule (Problem 2: window enlargement)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Seeded from SMT run: **result/result-2026-10-12-dataset-testbed-9-ring-avgwin/smt-c9-off/9-t3600-c9off-minlat**

## Admission (unchanged) vs. capacity grown

Problem 2 never admits a flow into the schedule it exports -- it only widens windows. `admitted` below is exactly the SMT baseline, by construction; the capacity growth this run achieved is banked slack and per-port GCL entries, reported separately.

| | admitted | of total |
|---|---|---|
| SMT (fixed, never moved) | 11 | 20 |
| RL-enlarged (exported; grow-only, admits nothing new) | 11 | 20 |

During training, the policy's trial admissions (the reward signal that teaches it how much a window needs to grow) reached **8** of the 9 SMT-rejected flows -- none of those are kept in this export; that capacity stays as empty, banked slack for Problem 3 to fill. Total slack banked: 442560 ns. GCL_size overflow: 0.

## Opportunistic idle top-up (deterministic post-pass)

**13836800 ns**, drawn from idle capacity on ports at or below utilisation 0.2, independent of what training happened to grow. Ported from prob_2_heuristic_enlarged's Step 7.

| port | queue | applied (ns) |
|---|---|---|
| S1-p0 | Q6 | 375040 |
| S1-p0 | Q7 | 337600 |
| S2-p0 | Q6 | 437760 |
| S2-p0 | Q7 | 150080 |
| S3-p0 | Q6 | 462720 |
| S3-p0 | Q7 | 100160 |
| sw01-p2 | Q6 | 262720 |
| sw01-p2 | Q7 | 341760 |
| sw01-p4 | Q6 | 496000 |
| sw01-p4 | Q7 | 100160 |
| sw01-p5 | Q6 | 458560 |
| sw01-p5 | Q7 | 175040 |
| sw02-p2 | Q6 | 440320 |
| sw02-p2 | Q7 | 51840 |
| sw02-p4 | Q7 | 745920 |
| sw02-p5 | Q6 | 358400 |
| sw02-p5 | Q7 | 350080 |
| sw03-p4 | Q6 | 287680 |
| sw03-p4 | Q7 | 358400 |
| sw03-p5 | Q6 | 479360 |
| sw03-p5 | Q7 | 100160 |
| sw04-p4 | Q6 | 552320 |
| sw04-p4 | Q7 | 48000 |
| sw04-p5 | Q7 | 729280 |
| sw05-p4 | Q6 | 462720 |
| sw05-p4 | Q7 | 100480 |
| sw05-p5 | Q6 | 287680 |
| sw05-p5 | Q7 | 375040 |
| sw06-p4 | Q7 | 712640 |
| sw06-p5 | Q6 | 429440 |
| sw06-p5 | Q7 | 175040 |
| sw07-p4 | Q6 | 287680 |
| sw07-p4 | Q7 | 391680 |
| sw07-p5 | Q6 | 446080 |
| sw07-p5 | Q7 | 100800 |
| sw08-p2 | Q6 | 429440 |
| sw08-p2 | Q7 | 121600 |
| sw08-p4 | Q6 | 446080 |
| sw08-p4 | Q7 | 175040 |
| sw08-p5 | Q6 | 287680 |
| sw08-p5 | Q7 | 408320 |

## Opportunistic exclusive window creation (deterministic post-pass)

**3** brand-new *exclusive* window(s) opened, **37440 ns** total, on ports at or below utilisation 0.2 whose TT queue had zero windows before this run. Ported from prob_2_heuristic_enlarged's Step 8.

| port | queue | size (ns) |
|---|---|---|
| sw02-p4 | Q6 | 12480 |
| sw04-p5 | Q6 | 12480 |
| sw06-p4 | Q6 | 12480 |

## Best-effort gap equalization (deterministic post-pass)

**8313920 ns** given back from the top-up/creation above so each port's leftover non-TAS gaps land close to equal. Ported from prob_2_heuristic_enlarged's Step 9.

| port | given back (ns) |
|---|---|---|
| sw01-p4 | 568640 |
| sw03-p5 | 568640 |
| sw05-p4 | 568640 |
| sw07-p5 | 557760 |
| sw08-p2 | 469440 |
| sw03-p4 | 443520 |
| sw05-p5 | 443520 |
| sw07-p4 | 443520 |
| sw08-p5 | 443520 |
| sw02-p5 | 427520 |
| sw01-p2 | 395520 |
| S1-p0 | 368640 |
| sw06-p5 | 356800 |
| sw08-p4 | 356800 |
| sw04-p4 | 313280 |
| sw02-p4 | 262400 |
| sw04-p5 | 262400 |
| sw06-p4 | 262400 |
| sw01-p5 | 249280 |
| sw02-p2 | 229760 |
| S2-p0 | 162240 |
| S3-p0 | 159680 |

## Opportunistic overlay window creation (deterministic post-pass)

**42** new overlay window(s), **9086720 ns** total, carved out of already-open best-effort spans on ports at or below utilisation 0.2 -- best-effort stays reachable inside each one (gate mask keeps its BE bits set). Run once after training/finalize_grow_only(), not a trained action.

| port | queue | size (ns) |
|---|---|---|
| S1-p0 | Q6 | 168960 |
| S1-p0 | Q7 | 199680 |
| S2-p0 | Q7 | 162240 |
| S3-p0 | Q7 | 159680 |
| sw01-p2 | Q6 | 208000 |
| sw01-p2 | Q7 | 220800 |
| sw01-p4 | Q6 | 270720 |
| sw01-p4 | Q7 | 314560 |
| sw01-p5 | Q6 | 116480 |
| sw01-p5 | Q7 | 161920 |
| sw02-p2 | Q6 | 206080 |
| sw02-p2 | Q7 | 29440 |
| sw02-p4 | Q6 | 141440 |
| sw02-p4 | Q7 | 150080 |
| sw02-p5 | Q6 | 244480 |
| sw02-p5 | Q7 | 199680 |
| sw03-p4 | Q6 | 266880 |
| sw03-p4 | Q7 | 243200 |
| sw03-p5 | Q6 | 316480 |
| sw03-p5 | Q7 | 285440 |
| sw04-p4 | Q6 | 152960 |
| sw04-p4 | Q7 | 211200 |
| sw04-p5 | Q6 | 158080 |
| sw04-p5 | Q7 | 150080 |
| sw05-p4 | Q6 | 350080 |
| sw05-p4 | Q7 | 268800 |
| sw05-p5 | Q6 | 266880 |
| sw05-p5 | Q7 | 226560 |
| sw06-p4 | Q6 | 149760 |
| sw06-p4 | Q7 | 175040 |
| sw06-p5 | Q6 | 244160 |
| sw06-p5 | Q7 | 158400 |
| sw07-p4 | Q6 | 175360 |
| sw07-p4 | Q7 | 301440 |
| sw07-p5 | Q6 | 331520 |
| sw07-p5 | Q7 | 293440 |
| sw08-p2 | Q6 | 285440 |
| sw08-p2 | Q7 | 275200 |
| sw08-p4 | Q6 | 156480 |
| sw08-p4 | Q7 | 229440 |
| sw08-p5 | Q6 | 235520 |
| sw08-p5 | Q7 | 224640 |

## Per-port GCL entries: before (SMT) vs. after (RL-enlarged)

| port | SMT entries | RL-enlarged entries | GCL_size |
|---|---|---|---|
| sw01-p2 | 19 | 28 | 255 |
| sw01-p4 | 3 | 22 | 255 |
| sw01-p5 | 15 | 20 | 255 |
| sw02-p2 | 25 | 32 | 255 |
| sw02-p4 | 3 | 9 | 255 |
| sw02-p5 | 9 | 18 | 255 |
| sw03-p4 | 11 | 23 | 255 |
| sw03-p5 | 3 | 20 | 255 |
| sw04-p4 | 11 | 25 | 255 |
| sw04-p5 | 3 | 9 | 255 |
| sw05-p4 | 3 | 19 | 255 |
| sw05-p5 | 11 | 19 | 255 |
| sw06-p4 | 3 | 10 | 255 |
| sw06-p5 | 11 | 21 | 255 |
| sw07-p4 | 11 | 19 | 255 |
| sw07-p5 | 3 | 23 | 255 |
| sw08-p2 | 5 | 19 | 255 |
| sw08-p4 | 11 | 22 | 255 |
| sw08-p5 | 11 | 22 | 255 |

## Flows

| flow | route | fixed | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|---|
| s0(id=1 S3->S1) | S3->sw01->sw02->S1 | yes | 6 | 62400 | 54480 | yes |
| s1(id=2 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | no | None | None | None | no |
| s2(id=3 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | no | None | None | None | no |
| s3(id=4 S3->S1) | S3->sw01->sw02->S1 | yes | 7 | 37440 | 45840 | yes |
| s4(id=5 S1->S3) | S1->sw02->sw01->S3 | no | None | None | None | no |
| s5(id=6 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | yes | 7 | 0 | 95760 | yes |
| s6(id=7 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | yes | 7 | 24960 | 79120 | yes |
| s7(id=8 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | yes | 6 | 74880 | 95760 | yes |
| s8(id=9 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | yes | 7 | 87360 | 95760 | yes |
| s9(id=10 S3->S1) | S3->sw01->sw02->S1 | yes | 7 | 12480 | 45840 | yes |
| s10(id=11 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | no | None | None | None | no |
| s11(id=12 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | yes | 7 | 24960 | 79120 | yes |
| s12(id=13 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |
| s13(id=14 S1->S3) | S1->sw02->sw01->S3 | yes | 6 | 0 | 45840 | yes |
| s14(id=15 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | no | None | None | None | no |
| s15(id=16 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | yes | 7 | 49920 | 79760 | yes |
| s16(id=17 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | no | None | None | None | no |
| s17(id=18 S3->S1) | S3->sw01->sw02->S1 | no | None | None | None | no |
| s18(id=19 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | no | None | None | None | no |
| s19(id=20 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | yes | 6 | 99840 | 79120 | yes |

## Per-hop windows (slack_ns > 0 means this window was enlarged)

| flow | egress port | queue | psi (ns) | delta (ns) |
|---|---|---|---|---|
| s0(id=1 S3->S1) | S3-p0 | Q6 | 62400 | 12480 |
| s0(id=1 S3->S1) | sw01-p5 | Q6 | 79040 | 12480 |
| s0(id=1 S3->S1) | sw02-p2 | Q6 | 104320 | 12480 |
| s3(id=4 S3->S1) | S3-p0 | Q7 | 37440 | 12480 |
| s3(id=4 S3->S1) | sw01-p5 | Q7 | 54080 | 12480 |
| s3(id=4 S3->S1) | sw02-p2 | Q7 | 70720 | 12480 |
| s5(id=6 S2->S3) | S2-p0 | Q7 | 0 | 12480 |
| s5(id=6 S2->S3) | sw08-p5 | Q7 | 16640 | 12480 |
| s5(id=6 S2->S3) | sw07-p4 | Q7 | 33280 | 12480 |
| s5(id=6 S2->S3) | sw05-p5 | Q7 | 49920 | 12480 |
| s5(id=6 S2->S3) | sw03-p4 | Q7 | 66560 | 12480 |
| s5(id=6 S2->S3) | sw01-p2 | Q7 | 83200 | 12480 |
| s6(id=7 S2->S1) | S2-p0 | Q7 | 24960 | 12480 |
| s6(id=7 S2->S1) | sw08-p4 | Q7 | 41600 | 12480 |
| s6(id=7 S2->S1) | sw06-p5 | Q7 | 58240 | 12480 |
| s6(id=7 S2->S1) | sw04-p4 | Q7 | 74880 | 12480 |
| s6(id=7 S2->S1) | sw02-p2 | Q7 | 91520 | 12480 |
| s7(id=8 S2->S3) | S2-p0 | Q6 | 74880 | 12480 |
| s7(id=8 S2->S3) | sw08-p5 | Q6 | 91520 | 12480 |
| s7(id=8 S2->S3) | sw07-p4 | Q6 | 108160 | 12480 |
| s7(id=8 S2->S3) | sw05-p5 | Q6 | 124800 | 12480 |
| s7(id=8 S2->S3) | sw03-p4 | Q6 | 141440 | 12480 |
| s7(id=8 S2->S3) | sw01-p2 | Q6 | 158080 | 12480 |
| s8(id=9 S3->S2) | S3-p0 | Q7 | 87360 | 12480 |
| s8(id=9 S3->S2) | sw01-p4 | Q7 | 104000 | 12480 |
| s8(id=9 S3->S2) | sw03-p5 | Q7 | 120640 | 12480 |
| s8(id=9 S3->S2) | sw05-p4 | Q7 | 137280 | 12480 |
| s8(id=9 S3->S2) | sw07-p5 | Q7 | 153920 | 12480 |
| s8(id=9 S3->S2) | sw08-p2 | Q7 | 170560 | 12480 |
| s9(id=10 S3->S1) | S3-p0 | Q7 | 12480 | 12480 |
| s9(id=10 S3->S1) | sw01-p5 | Q7 | 29120 | 12480 |
| s9(id=10 S3->S1) | sw02-p2 | Q7 | 45760 | 12480 |
| s11(id=12 S1->S2) | S1-p0 | Q7 | 24960 | 12480 |
| s11(id=12 S1->S2) | sw02-p4 | Q7 | 41600 | 12480 |
| s11(id=12 S1->S2) | sw04-p5 | Q7 | 58240 | 12480 |
| s11(id=12 S1->S2) | sw06-p4 | Q7 | 74880 | 12480 |
| s11(id=12 S1->S2) | sw08-p2 | Q7 | 91520 | 12480 |
| s13(id=14 S1->S3) | S1-p0 | Q6 | 0 | 12480 |
| s13(id=14 S1->S3) | sw02-p5 | Q6 | 16640 | 12480 |
| s13(id=14 S1->S3) | sw01-p2 | Q6 | 33280 | 12480 |
| s15(id=16 S2->S1) | S2-p0 | Q7 | 49920 | 12480 |
| s15(id=16 S2->S1) | sw08-p4 | Q7 | 66560 | 12480 |
| s15(id=16 S2->S1) | sw06-p5 | Q7 | 83200 | 12480 |
| s15(id=16 S2->S1) | sw04-p4 | Q7 | 99840 | 12480 |
| s15(id=16 S2->S1) | sw02-p2 | Q7 | 117120 | 12480 |
| s19(id=20 S2->S1) | S2-p0 | Q6 | 99840 | 12480 |
| s19(id=20 S2->S1) | sw08-p4 | Q6 | 116480 | 12480 |
| s19(id=20 S2->S1) | sw06-p5 | Q6 | 133120 | 12480 |
| s19(id=20 S2->S1) | sw04-p4 | Q6 | 149760 | 12480 |
| s19(id=20 S2->S1) | sw02-p2 | Q6 | 166400 | 12480 |

## Metrics (training/evaluation signal, not the export)

| metric | value |
|---|---|
| trial-placed flow ratio (fixed + trial-admitted) | 0.950 |
| r1  same-queue window adjacency | 0.359 |
| r2  deadline-violation ratio | 0.000 |
| r3  supplier/receiver overlap | 0.994 |
| r4  mean e2e/deadline (admitted) | 0.225 |
| constraint violations | 0 |

## Constraint check

- C1-C7, C9: OK
- seed-integrity (no SMT-fixed flow's placement changed): OK

## GCL per egress port

### sw01-p2  (28 entries, util 14.0400 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 24960 0x7F # 01111111   Q6
sgs 26240 0x40 # 01000000   Q6
sgs 15680 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0xBF # 10111111   Q7
sgs 101120 0x80 # 10000000   Q7
sgs 15680 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 63680 0x40 # 01000000   Q6
sgs 15680 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0xBF # 10111111   Q7
sgs 67840 0x80 # 10000000   Q7
sgs 48960 0xBF # 10111111   Q7
```

### sw01-p4  (22 entries, util 1.5600 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 54080 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 33600 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 68800 0x40 # 01000000   Q6
sgs 14720 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 68800 0x40 # 01000000   Q6
sgs 14720 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 52160 0x40 # 01000000   Q6
sgs 31360 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p5  (20 entries, util 10.9200 %)

```
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 90880 0x40 # 01000000   Q6
sgs 30080 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 128320 0x40 # 01000000   Q6
sgs 30080 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 115840 0x80 # 10000000   Q7
sgs 30080 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 99200 0x40 # 01000000   Q6
sgs 59200 0xBF # 10111111   Q7
```

### sw02-p2  (32 entries, util 18.7200 %)

```
sgs 45760 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 33280 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 10880 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 49920 0x40 # 01000000   Q6
sgs 29440 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 52800 0x40 # 01000000   Q6
sgs 29440 0x7F # 01111111   Q6
sgs 75840 0x40 # 01000000   Q6
sgs 29440 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 33280 0x80 # 10000000   Q7
sgs 13120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 10880 0x3F # 00111111   BE
sgs 75840 0x40 # 01000000   Q6
sgs 29440 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 52800 0x40 # 01000000   Q6
sgs 29440 0x7F # 01111111   Q6
sgs 30080 0x40 # 01000000   Q6
sgs 29440 0xBF # 10111111   Q7
```

### sw02-p4  (9 entries, util 1.5600 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 29120 0x7F # 01111111   Q6
sgs 496000 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p5  (18 entries, util 6.2400 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 80640 0x80 # 10000000   Q7
sgs 40320 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 93120 0x40 # 01000000   Q6
sgs 40320 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 80640 0x80 # 10000000   Q7
sgs 40320 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 76480 0x40 # 01000000   Q6
sgs 56960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (23 entries, util 7.8000 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 24960 0x7F # 01111111   Q6
sgs 32960 0x40 # 01000000   Q6
sgs 25600 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 107840 0x80 # 10000000   Q7
sgs 25600 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 70400 0x40 # 01000000   Q6
sgs 25600 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 41280 0x80 # 10000000   Q7
sgs 42240 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p5  (20 entries, util 1.5600 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 54400 0xBF # 10111111   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 16960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 68800 0x40 # 01000000   Q6
sgs 48000 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 68800 0x40 # 01000000   Q6
sgs 48000 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 35520 0x40 # 01000000   Q6
sgs 31360 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p4  (25 entries, util 7.8000 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 11520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 107200 0x40 # 01000000   Q6
sgs 43200 0xBF # 10111111   Q7
sgs 23680 0x7F # 01111111   Q6
sgs 84160 0x40 # 01000000   Q6
sgs 41920 0x7F # 01111111   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 11520 0x3F # 00111111   BE
sgs 133120 0x40 # 01000000   Q6
sgs 43200 0xBF # 10111111   Q7
sgs 23680 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 13760 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (9 entries, util 1.5600 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 45760 0x7F # 01111111   Q6
sgs 479360 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (19 entries, util 1.5600 %)

```
sgs 50240 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0xBF # 10111111   Q7
sgs 37120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 50240 0xBF # 10111111   Q7
sgs 50240 0x7F # 01111111   Q6
sgs 68800 0x40 # 01000000   Q6
sgs 31040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 50240 0x7F # 01111111   Q6
sgs 68800 0x40 # 01000000   Q6
sgs 31040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 50240 0x7F # 01111111   Q6
sgs 18560 0x40 # 01000000   Q6
sgs 31360 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p5  (19 entries, util 7.8000 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 24960 0x7F # 01111111   Q6
sgs 32960 0x40 # 01000000   Q6
sgs 42240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 107840 0x80 # 10000000   Q7
sgs 42240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 70400 0x40 # 01000000   Q6
sgs 42240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 57920 0x80 # 10000000   Q7
sgs 42240 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p4  (10 entries, util 1.5600 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 462720 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (21 entries, util 7.8000 %)

```
sgs 45760 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 39040 0x40 # 01000000   Q6
sgs 27840 0xBF # 10111111   Q7
sgs 45760 0x7F # 01111111   Q6
sgs 126400 0x40 # 01000000   Q6
sgs 27840 0xBF # 10111111   Q7
sgs 45760 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 88960 0x80 # 10000000   Q7
sgs 27840 0xBF # 10111111   Q7
sgs 45760 0x7F # 01111111   Q6
sgs 80640 0x40 # 01000000   Q6
sgs 23680 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (19 entries, util 7.8000 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 32960 0x40 # 01000000   Q6
sgs 58880 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 107840 0x80 # 10000000   Q7
sgs 58880 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 70400 0x40 # 01000000   Q6
sgs 58880 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 74560 0x80 # 10000000   Q7
sgs 42240 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p5  (23 entries, util 1.5600 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 17280 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 20480 0xBF # 10111111   Q7
sgs 53760 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 33600 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 17280 0xBF # 10111111   Q7
sgs 68800 0x40 # 01000000   Q6
sgs 14080 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 17280 0xBF # 10111111   Q7
sgs 68800 0x40 # 01000000   Q6
sgs 14080 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 17280 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 20480 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p2  (19 entries, util 3.1200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 33280 0x7F # 01111111   Q6
sgs 20480 0xBF # 10111111   Q7
sgs 23040 0x80 # 10000000   Q7
sgs 56320 0x7F # 01111111   Q6
sgs 54400 0xBF # 10111111   Q7
sgs 89280 0x40 # 01000000   Q6
sgs 56320 0x7F # 01111111   Q6
sgs 54400 0xBF # 10111111   Q7
sgs 89280 0x40 # 01000000   Q6
sgs 56320 0x7F # 01111111   Q6
sgs 54400 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 33280 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p4  (22 entries, util 7.8000 %)

```
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 21120 0xBF # 10111111   Q7
sgs 16320 0x7F # 01111111   Q6
sgs 39040 0x40 # 01000000   Q6
sgs 44480 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 126400 0x40 # 01000000   Q6
sgs 44480 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 88960 0x80 # 10000000   Q7
sgs 44480 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 97280 0x40 # 01000000   Q6
sgs 23680 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (22 entries, util 7.8000 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 32960 0x40 # 01000000   Q6
sgs 25600 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 107840 0x80 # 10000000   Q7
sgs 25600 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 70400 0x40 # 01000000   Q6
sgs 25600 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 91200 0x80 # 10000000   Q7
sgs 42240 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

