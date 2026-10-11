# RL-enlarged GCL schedule (Problem 2: window enlargement)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Seeded from SMT run: **result/result-2026-10-10-dataset-testbed-5-avgwin/smt-c9-off/5-t3600-c9off-minlat**

## Admission (unchanged) vs. capacity grown

Problem 2 never admits a flow into the schedule it exports -- it only widens windows. `admitted` below is exactly the SMT baseline, by construction; the capacity growth this run achieved is banked slack and per-port GCL entries, reported separately.

| | admitted | of total |
|---|---|---|
| SMT (fixed, never moved) | 10 | 20 |
| RL-enlarged (exported; grow-only, admits nothing new) | 10 | 20 |

During training, the policy's trial admissions (the reward signal that teaches it how much a window needs to grow) reached **9** of the 10 SMT-rejected flows -- none of those are kept in this export; that capacity stays as empty, banked slack for Problem 3 to fill. Total slack banked: 225600 ns. GCL_size overflow: 0.

## Opportunistic idle top-up (deterministic post-pass)

**10672960 ns**, drawn from idle capacity on ports at or below utilisation 0.2, independent of what training happened to grow. Ported from prob_2_heuristic_enlarged's Step 7.

| port | queue | applied (ns) |
|---|---|---|
| S1-p0 | Q6 | 475200 |
| S1-p0 | Q7 | 137600 |
| S2-p0 | Q6 | 137600 |
| S2-p0 | Q7 | 475200 |
| S3-p0 | Q7 | 625280 |
| sw01-p2 | Q6 | 176640 |
| sw01-p2 | Q7 | 262720 |
| sw01-p4 | Q6 | 45440 |
| sw01-p4 | Q7 | 563200 |
| sw02-p2 | Q6 | 575360 |
| sw02-p2 | Q7 | 33280 |
| sw02-p4 | Q6 | 378560 |
| sw02-p4 | Q7 | 217600 |
| sw03-p4 | Q6 | 194240 |
| sw03-p4 | Q7 | 259840 |
| sw03-p5 | Q6 | 146560 |
| sw03-p5 | Q7 | 402240 |
| sw04-p4 | Q6 | 592000 |
| sw04-p4 | Q7 | 33280 |
| sw04-p5 | Q6 | 360640 |
| sw04-p5 | Q7 | 218880 |
| sw05-p4 | Q6 | 146560 |
| sw05-p4 | Q7 | 385600 |
| sw05-p5 | Q6 | 211840 |
| sw05-p5 | Q7 | 256960 |
| sw06-p4 | Q6 | 342720 |
| sw06-p4 | Q7 | 220160 |
| sw06-p5 | Q6 | 608640 |
| sw06-p5 | Q7 | 33280 |
| sw07-p4 | Q6 | 229440 |
| sw07-p4 | Q7 | 254080 |
| sw07-p5 | Q6 | 146560 |
| sw07-p5 | Q7 | 368960 |
| sw08-p4 | Q6 | 625280 |
| sw08-p4 | Q7 | 33280 |
| sw08-p5 | Q6 | 247040 |
| sw08-p5 | Q7 | 251200 |

## Best-effort gap equalization (deterministic post-pass)

**5771840 ns** given back from the top-up/creation above so each port's leftover non-TAS gaps land close to equal. Ported from prob_2_heuristic_enlarged's Step 9.

| port | given back (ns) |
|---|---|---|
| sw08-p4 | 465280 |
| sw06-p5 | 456320 |
| sw04-p4 | 439680 |
| sw02-p2 | 423040 |
| sw03-p4 | 331840 |
| sw05-p5 | 331200 |
| sw07-p4 | 330560 |
| sw08-p5 | 329920 |
| sw01-p2 | 320960 |
| sw03-p5 | 288960 |
| sw05-p4 | 288960 |
| sw07-p5 | 288960 |
| sw01-p4 | 247360 |
| sw06-p4 | 221440 |
| sw04-p5 | 220800 |
| sw02-p4 | 220160 |
| S1-p0 | 199040 |
| S3-p0 | 189440 |
| S2-p0 | 177920 |

## Opportunistic overlay window creation (deterministic post-pass)

**36** new overlay window(s), **6287680 ns** total, carved out of already-open best-effort spans on ports at or below utilisation 0.2 -- best-effort stays reachable inside each one (gate mask keeps its BE bits set). Run once after training/finalize_grow_only(), not a trained action.

| port | queue | size (ns) |
|---|---|---|
| S1-p0 | Q6 | 24960 |
| S1-p0 | Q7 | 174080 |
| S2-p0 | Q7 | 177920 |
| S3-p0 | Q7 | 189440 |
| sw01-p2 | Q6 | 162240 |
| sw01-p2 | Q7 | 200640 |
| sw01-p4 | Q6 | 113920 |
| sw01-p4 | Q7 | 150080 |
| sw02-p2 | Q6 | 255040 |
| sw02-p2 | Q7 | 272000 |
| sw02-p4 | Q6 | 66560 |
| sw02-p4 | Q7 | 152960 |
| sw03-p4 | Q6 | 233920 |
| sw03-p4 | Q7 | 124800 |
| sw03-p5 | Q6 | 152640 |
| sw03-p5 | Q7 | 146240 |
| sw04-p4 | Q6 | 284800 |
| sw04-p4 | Q7 | 242240 |
| sw04-p5 | Q6 | 163840 |
| sw04-p5 | Q7 | 71680 |
| sw05-p4 | Q6 | 238400 |
| sw05-p4 | Q7 | 77120 |
| sw05-p5 | Q6 | 284800 |
| sw05-p5 | Q7 | 58240 |
| sw06-p4 | Q6 | 180480 |
| sw06-p4 | Q7 | 71040 |
| sw06-p5 | Q6 | 226240 |
| sw06-p5 | Q7 | 300800 |
| sw07-p4 | Q6 | 137600 |
| sw07-p4 | Q7 | 189760 |
| sw07-p5 | Q6 | 214720 |
| sw07-p5 | Q7 | 117440 |
| sw08-p4 | Q6 | 251520 |
| sw08-p4 | Q7 | 267840 |
| sw08-p5 | Q6 | 88640 |
| sw08-p5 | Q7 | 223040 |

## Per-port GCL entries: before (SMT) vs. after (RL-enlarged)

| port | SMT entries | RL-enlarged entries | GCL_size |
|---|---|---|---|
| sw01-p2 | 13 | 39 | 255 |
| sw01-p4 | 15 | 24 | 255 |
| sw02-p2 | 5 | 22 | 255 |
| sw02-p4 | 17 | 28 | 255 |
| sw03-p4 | 13 | 39 | 255 |
| sw03-p5 | 15 | 25 | 255 |
| sw04-p4 | 5 | 22 | 255 |
| sw04-p5 | 17 | 29 | 255 |
| sw05-p4 | 15 | 21 | 255 |
| sw05-p5 | 13 | 35 | 255 |
| sw06-p4 | 17 | 29 | 255 |
| sw06-p5 | 5 | 21 | 255 |
| sw07-p4 | 13 | 35 | 255 |
| sw07-p5 | 15 | 25 | 255 |
| sw08-p2 | 29 | 33 | 255 |
| sw08-p4 | 5 | 21 | 255 |
| sw08-p5 | 13 | 38 | 255 |

## Flows

| flow | route | fixed | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|---|
| s0(id=1 S3->S1) | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | no | None | None | None | no |
| s1(id=2 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | yes | 6 | 0 | 95760 | yes |
| s2(id=3 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | yes | 6 | 62400 | 84240 | yes |
| s3(id=4 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |
| s4(id=5 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | yes | 7 | 62400 | 95760 | yes |
| s5(id=6 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |
| s6(id=7 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | no | None | None | None | no |
| s7(id=8 S3->S1) | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | no | None | None | None | no |
| s8(id=9 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | yes | 7 | 37440 | 79120 | yes |
| s9(id=10 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | yes | 7 | 0 | 79120 | yes |
| s10(id=11 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |
| s11(id=12 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | yes | 7 | 12480 | 95760 | yes |
| s12(id=13 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | yes | 6 | 87360 | 145680 | yes |
| s13(id=14 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |
| s14(id=15 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |
| s15(id=16 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | yes | 7 | 62400 | 97040 | yes |
| s16(id=17 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | yes | 6 | 37440 | 83600 | yes |
| s17(id=18 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |
| s18(id=19 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | yes | 7 | 37440 | 96400 | yes |
| s19(id=20 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | no | None | None | None | no |

## Per-hop windows (slack_ns > 0 means this window was enlarged)

| flow | egress port | queue | psi (ns) | delta (ns) |
|---|---|---|---|---|
| s1(id=2 S2->S3) | S2-p0 | Q6 | 0 | 12480 |
| s1(id=2 S2->S3) | sw08-p5 | Q6 | 16640 | 12480 |
| s1(id=2 S2->S3) | sw07-p4 | Q6 | 33280 | 12480 |
| s1(id=2 S2->S3) | sw05-p5 | Q6 | 49920 | 12480 |
| s1(id=2 S2->S3) | sw03-p4 | Q6 | 66560 | 12480 |
| s1(id=2 S2->S3) | sw01-p2 | Q6 | 83200 | 12480 |
| s2(id=3 S1->S2) | S1-p0 | Q6 | 62400 | 12480 |
| s2(id=3 S1->S2) | sw02-p4 | Q6 | 82880 | 12480 |
| s2(id=3 S1->S2) | sw04-p5 | Q6 | 99520 | 12480 |
| s2(id=3 S1->S2) | sw06-p4 | Q6 | 116160 | 12480 |
| s2(id=3 S1->S2) | sw08-p2 | Q6 | 134080 | 12480 |
| s4(id=5 S2->S3) | S2-p0 | Q7 | 62400 | 12480 |
| s4(id=5 S2->S3) | sw08-p5 | Q7 | 79040 | 12480 |
| s4(id=5 S2->S3) | sw07-p4 | Q7 | 95680 | 12480 |
| s4(id=5 S2->S3) | sw05-p5 | Q7 | 112320 | 12480 |
| s4(id=5 S2->S3) | sw03-p4 | Q7 | 128960 | 12480 |
| s4(id=5 S2->S3) | sw01-p2 | Q7 | 145600 | 12480 |
| s8(id=9 S2->S1) | S2-p0 | Q7 | 37440 | 12480 |
| s8(id=9 S2->S1) | sw08-p4 | Q7 | 54080 | 12480 |
| s8(id=9 S2->S1) | sw06-p5 | Q7 | 70720 | 12480 |
| s8(id=9 S2->S1) | sw04-p4 | Q7 | 87360 | 12480 |
| s8(id=9 S2->S1) | sw02-p2 | Q7 | 104000 | 12480 |
| s9(id=10 S1->S2) | S1-p0 | Q7 | 0 | 12480 |
| s9(id=10 S1->S2) | sw02-p4 | Q7 | 16640 | 12480 |
| s9(id=10 S1->S2) | sw04-p5 | Q7 | 33280 | 12480 |
| s9(id=10 S1->S2) | sw06-p4 | Q7 | 49920 | 12480 |
| s9(id=10 S1->S2) | sw08-p2 | Q7 | 66560 | 12480 |
| s11(id=12 S3->S2) | S3-p0 | Q7 | 12480 | 12480 |
| s11(id=12 S3->S2) | sw01-p4 | Q7 | 29120 | 12480 |
| s11(id=12 S3->S2) | sw03-p5 | Q7 | 45760 | 12480 |
| s11(id=12 S3->S2) | sw05-p4 | Q7 | 62400 | 12480 |
| s11(id=12 S3->S2) | sw07-p5 | Q7 | 79040 | 12480 |
| s11(id=12 S3->S2) | sw08-p2 | Q7 | 95680 | 12480 |
| s12(id=13 S1->S3) | S1-p0 | Q6 | 87360 | 12480 |
| s12(id=13 S1->S3) | sw02-p4 | Q6 | 104000 | 12480 |
| s12(id=13 S1->S3) | sw04-p5 | Q6 | 120640 | 12480 |
| s12(id=13 S1->S3) | sw06-p4 | Q6 | 137280 | 12480 |
| s12(id=13 S1->S3) | sw08-p5 | Q6 | 153920 | 12480 |
| s12(id=13 S1->S3) | sw07-p4 | Q6 | 170560 | 12480 |
| s12(id=13 S1->S3) | sw05-p5 | Q6 | 187200 | 12480 |
| s12(id=13 S1->S3) | sw03-p4 | Q6 | 203840 | 12480 |
| s12(id=13 S1->S3) | sw01-p2 | Q6 | 220480 | 12480 |
| s15(id=16 S3->S2) | S3-p0 | Q7 | 62400 | 12480 |
| s15(id=16 S3->S2) | sw01-p4 | Q7 | 79040 | 12480 |
| s15(id=16 S3->S2) | sw03-p5 | Q7 | 95680 | 12480 |
| s15(id=16 S3->S2) | sw05-p4 | Q7 | 112320 | 12480 |
| s15(id=16 S3->S2) | sw07-p5 | Q7 | 128960 | 12480 |
| s15(id=16 S3->S2) | sw08-p2 | Q7 | 146880 | 12480 |
| s16(id=17 S1->S2) | S1-p0 | Q6 | 37440 | 12480 |
| s16(id=17 S1->S2) | sw02-p4 | Q6 | 56000 | 12480 |
| s16(id=17 S1->S2) | sw04-p5 | Q6 | 72640 | 12480 |
| s16(id=17 S1->S2) | sw06-p4 | Q6 | 89280 | 12480 |
| s16(id=17 S1->S2) | sw08-p2 | Q6 | 108480 | 12480 |
| s18(id=19 S3->S2) | S3-p0 | Q7 | 37440 | 12480 |
| s18(id=19 S3->S2) | sw01-p4 | Q7 | 54080 | 12480 |
| s18(id=19 S3->S2) | sw03-p5 | Q7 | 71360 | 12480 |
| s18(id=19 S3->S2) | sw05-p4 | Q7 | 88000 | 12480 |
| s18(id=19 S3->S2) | sw07-p5 | Q7 | 104640 | 12480 |
| s18(id=19 S3->S2) | sw08-p2 | Q7 | 121280 | 12480 |

## Metrics (training/evaluation signal, not the export)

| metric | value |
|---|---|
| trial-placed flow ratio (fixed + trial-admitted) | 0.950 |
| r1  same-queue window adjacency | 0.268 |
| r2  deadline-violation ratio | 0.000 |
| r3  supplier/receiver overlap | 0.996 |
| r4  mean e2e/deadline (admitted) | 0.333 |
| constraint violations | 0 |

## Constraint check

- C1-C7, C9: OK
- seed-integrity (no SMT-fixed flow's placement changed): OK

## GCL per egress port

### sw01-p2  (39 entries, util 9.3600 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 4800 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 20160 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 4800 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 10560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 22080 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 32000 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 31040 0x80 # 10000000   Q7
sgs 23360 0x7F # 01111111   Q6
sgs 12800 0xBF # 10111111   Q7
sgs 84160 0x40 # 01000000   Q6
sgs 36160 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 4800 0x3F # 00111111   BE
sgs 13760 0x40 # 01000000   Q6
sgs 23360 0x7F # 01111111   Q6
sgs 12800 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 10560 0x3F # 00111111   BE
sgs 61120 0x80 # 10000000   Q7
sgs 36160 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 31040 0x80 # 10000000   Q7
sgs 23360 0x7F # 01111111   Q6
sgs 12800 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 24640 0xBF # 10111111   Q7
```

### sw01-p4  (24 entries, util 10.9200 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 32320 0x80 # 10000000   Q7
sgs 47360 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 28800 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 140160 0x80 # 10000000   Q7
sgs 30720 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 115200 0x80 # 10000000   Q7
sgs 30720 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 123520 0x80 # 10000000   Q7
sgs 47360 0xBF # 10111111   Q7
```

### sw02-p2  (22 entries, util 3.1200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 54080 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 45440 0x40 # 01000000   Q6
sgs 21440 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 25280 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 32960 0x7F # 01111111   Q6
sgs 74240 0x40 # 01000000   Q6
sgs 42560 0x7F # 01111111   Q6
sgs 54080 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 103360 0x40 # 01000000   Q6
sgs 13440 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 32960 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 54400 0xBF # 10111111   Q7
```

### sw02-p4  (28 entries, util 12.4800 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 960 0x3F # 00111111   BE
sgs 33600 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 50880 0x80 # 10000000   Q7
sgs 26880 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 144000 0x40 # 01000000   Q6
sgs 26880 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 960 0x3F # 00111111   BE
sgs 103680 0x80 # 10000000   Q7
sgs 26880 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 127360 0x40 # 01000000   Q6
sgs 43520 0xBF # 10111111   Q7
```

### sw03-p4  (39 entries, util 9.3600 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 3840 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 21120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 4480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 10880 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 22080 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 30720 0x80 # 10000000   Q7
sgs 36160 0x7F # 01111111   Q6
sgs 84480 0x40 # 01000000   Q6
sgs 19520 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 3840 0x3F # 00111111   BE
sgs 14400 0x40 # 01000000   Q6
sgs 36160 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 10880 0x3F # 00111111   BE
sgs 61120 0x80 # 10000000   Q7
sgs 19520 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 30720 0x80 # 10000000   Q7
sgs 36160 0x7F # 01111111   Q6
sgs 17920 0x40 # 01000000   Q6
sgs 36160 0xBF # 10111111   Q7
```

### sw03-p5  (25 entries, util 10.9200 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0xBF # 10111111   Q7
sgs 36800 0x80 # 10000000   Q7
sgs 11520 0x3F # 00111111   BE
sgs 62720 0x40 # 01000000   Q6
sgs 17600 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 136640 0x80 # 10000000   Q7
sgs 17600 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 16320 0xBF # 10111111   Q7
sgs 19520 0x7F # 01111111   Q6
sgs 62720 0x40 # 01000000   Q6
sgs 17600 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 103360 0x80 # 10000000   Q7
sgs 50880 0xBF # 10111111   Q7
```

### sw04-p4  (22 entries, util 3.1200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 37440 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 45440 0x40 # 01000000   Q6
sgs 38080 0xBF # 10111111   Q7
sgs 58560 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 16320 0x7F # 01111111   Q6
sgs 74240 0x40 # 01000000   Q6
sgs 59200 0x7F # 01111111   Q6
sgs 37440 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 103360 0x40 # 01000000   Q6
sgs 30080 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 16320 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 21120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (29 entries, util 12.4800 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 14080 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 960 0x3F # 00111111   BE
sgs 33600 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 50880 0x80 # 10000000   Q7
sgs 43520 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 143680 0x40 # 01000000   Q6
sgs 43520 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 14080 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 960 0x3F # 00111111   BE
sgs 103680 0x80 # 10000000   Q7
sgs 43520 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 110400 0x40 # 01000000   Q6
sgs 43520 0xBF # 10111111   Q7
```

### sw05-p4  (21 entries, util 10.9200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0xBF # 10111111   Q7
sgs 36800 0x80 # 10000000   Q7
sgs 11520 0x3F # 00111111   BE
sgs 62720 0x40 # 01000000   Q6
sgs 50880 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 136640 0x80 # 10000000   Q7
sgs 50880 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 35840 0x7F # 01111111   Q6
sgs 62720 0x40 # 01000000   Q6
sgs 50880 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 86720 0x80 # 10000000   Q7
sgs 50880 0xBF # 10111111   Q7
```

### sw05-p5  (35 entries, util 9.3600 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 2880 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 22080 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 22080 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 32000 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 30400 0x80 # 10000000   Q7
sgs 36160 0x7F # 01111111   Q6
sgs 84800 0x40 # 01000000   Q6
sgs 36160 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 2880 0x3F # 00111111   BE
sgs 15040 0x40 # 01000000   Q6
sgs 36160 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 61120 0x80 # 10000000   Q7
sgs 36160 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 30400 0x80 # 10000000   Q7
sgs 36160 0x7F # 01111111   Q6
sgs 34880 0x40 # 01000000   Q6
sgs 36160 0xBF # 10111111   Q7
```

### sw06-p4  (29 entries, util 12.4800 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 13760 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 960 0x3F # 00111111   BE
sgs 33600 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 50880 0x80 # 10000000   Q7
sgs 43520 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 640 0x3F # 00111111   BE
sgs 143360 0x40 # 01000000   Q6
sgs 43520 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 13760 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 960 0x3F # 00111111   BE
sgs 103680 0x80 # 10000000   Q7
sgs 43520 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 640 0x3F # 00111111   BE
sgs 93440 0x40 # 01000000   Q6
sgs 43520 0xBF # 10111111   Q7
```

### sw06-p5  (21 entries, util 3.1200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 20800 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 16640 0xBF # 10111111   Q7
sgs 45440 0x40 # 01000000   Q6
sgs 54720 0xBF # 10111111   Q7
sgs 41920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 45440 0xBF # 10111111   Q7
sgs 74240 0x40 # 01000000   Q6
sgs 25920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 20800 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 16640 0xBF # 10111111   Q7
sgs 103360 0x40 # 01000000   Q6
sgs 46720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 37760 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (35 entries, util 9.3600 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 1920 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 23040 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 3840 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 11520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 22080 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 32000 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 30080 0x80 # 10000000   Q7
sgs 36160 0xBF # 10111111   Q7
sgs 85120 0x40 # 01000000   Q6
sgs 36160 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 1920 0x3F # 00111111   BE
sgs 15680 0x40 # 01000000   Q6
sgs 36160 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 11520 0x3F # 00111111   BE
sgs 61120 0x80 # 10000000   Q7
sgs 36160 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 30080 0x80 # 10000000   Q7
sgs 36160 0xBF # 10111111   Q7
sgs 51840 0x40 # 01000000   Q6
sgs 36160 0xBF # 10111111   Q7
```

### sw07-p5  (25 entries, util 10.9200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0x7F # 01111111   Q6
sgs 36800 0x80 # 10000000   Q7
sgs 11520 0x3F # 00111111   BE
sgs 62720 0x40 # 01000000   Q6
sgs 34240 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 136640 0x80 # 10000000   Q7
sgs 34240 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 35840 0x7F # 01111111   Q6
sgs 62720 0x40 # 01000000   Q6
sgs 34240 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 70080 0x80 # 10000000   Q7
sgs 50880 0xBF # 10111111   Q7
```

### sw08-p2  (33 entries, util 21.8400 %)

```
sgs 66560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 16640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 10240 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 84480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 16640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 158400 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 16640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 35840 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 84480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 16640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 91840 0x3F # 00111111   BE
```

### sw08-p4  (21 entries, util 3.1200 %)

```
sgs 54080 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 16640 0xBF # 10111111   Q7
sgs 45440 0x40 # 01000000   Q6
sgs 21440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 25280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 45440 0xBF # 10111111   Q7
sgs 74240 0x40 # 01000000   Q6
sgs 42560 0xBF # 10111111   Q7
sgs 54080 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 16640 0xBF # 10111111   Q7
sgs 103360 0x40 # 01000000   Q6
sgs 13440 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 20160 0x40 # 01000000   Q6
sgs 46720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (38 entries, util 9.3600 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 960 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 24000 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 3520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 11840 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 22080 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 15360 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 29760 0x80 # 10000000   Q7
sgs 36160 0xBF # 10111111   Q7
sgs 85440 0x40 # 01000000   Q6
sgs 19520 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 960 0x3F # 00111111   BE
sgs 16320 0x40 # 01000000   Q6
sgs 36160 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 11840 0x3F # 00111111   BE
sgs 61120 0x80 # 10000000   Q7
sgs 19520 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 29760 0x80 # 10000000   Q7
sgs 36160 0xBF # 10111111   Q7
sgs 68800 0x40 # 01000000   Q6
sgs 36160 0xBF # 10111111   Q7
```

