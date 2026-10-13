# RL-enlarged GCL schedule (Problem 2: window enlargement)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Seeded from SMT run: **result/result-2026-10-13-dataset-testbed-13-tree-avgwin/smt-c9-off/13-t3600-c9off-minlat**

## Admission (unchanged) vs. capacity grown

Problem 2 never admits a flow into the schedule it exports -- it only widens windows. `admitted` below is exactly the SMT baseline, by construction; the capacity growth this run achieved is banked slack and per-port GCL entries, reported separately.

| | admitted | of total |
|---|---|---|
| SMT (fixed, never moved) | 11 | 20 |
| RL-enlarged (exported; grow-only, admits nothing new) | 11 | 20 |

During training, the policy's trial admissions (the reward signal that teaches it how much a window needs to grow) reached **5** of the 9 SMT-rejected flows -- none of those are kept in this export; that capacity stays as empty, banked slack for Problem 3 to fill. Total slack banked: 133120 ns. GCL_size overflow: 0.

## Opportunistic idle top-up (deterministic post-pass)

**11372800 ns**, drawn from idle capacity on ports at or below utilisation 0.2, independent of what training happened to grow. Ported from prob_2_heuristic_enlarged's Step 7.

| port | queue | applied (ns) |
|---|---|---|
| S1-p0 | Q6 | 537600 |
| S1-p0 | Q7 | 175040 |
| S3-p0 | Q6 | 275200 |
| S3-p0 | Q7 | 375040 |
| sw01-p2 | Q6 | 457600 |
| sw01-p2 | Q7 | 47040 |
| sw01-p4 | Q6 | 275200 |
| sw01-p4 | Q7 | 358400 |
| sw02-p2 | Q6 | 313280 |
| sw02-p2 | Q7 | 224640 |
| sw02-p4 | Q6 | 513600 |
| sw02-p4 | Q7 | 182400 |
| sw03-p4 | Q6 | 474240 |
| sw03-p4 | Q7 | 47040 |
| sw03-p5 | Q6 | 275200 |
| sw03-p5 | Q7 | 341760 |
| sw04-p4 | Q6 | 313280 |
| sw04-p4 | Q7 | 241280 |
| sw04-p5 | Q6 | 496960 |
| sw04-p5 | Q7 | 182400 |
| sw05-p4 | Q6 | 275200 |
| sw05-p4 | Q7 | 325120 |
| sw05-p5 | Q6 | 490880 |
| sw05-p5 | Q7 | 47040 |
| sw06-p4 | Q6 | 474240 |
| sw06-p4 | Q7 | 188480 |
| sw06-p5 | Q6 | 313280 |
| sw06-p5 | Q7 | 257920 |
| sw07-p4 | Q6 | 507520 |
| sw07-p4 | Q7 | 47040 |
| sw07-p5 | Q6 | 275200 |
| sw07-p5 | Q7 | 308480 |
| sw08-p2 | Q6 | 596160 |
| sw08-p4 | Q6 | 313280 |
| sw08-p4 | Q7 | 274560 |
| sw08-p5 | Q6 | 524160 |
| sw08-p5 | Q7 | 47040 |

## Opportunistic exclusive window creation (deterministic post-pass)

**1** brand-new *exclusive* window(s) opened, **12480 ns** total, on ports at or below utilisation 0.2 whose TT queue had zero windows before this run. Ported from prob_2_heuristic_enlarged's Step 8.

| port | queue | size (ns) |
|---|---|---|
| sw08-p2 | Q7 | 12480 |

## Best-effort gap equalization (deterministic post-pass)

**6165440 ns** given back from the top-up/creation above so each port's leftover non-TAS gaps land close to equal. Ported from prob_2_heuristic_enlarged's Step 9.

| port | given back (ns) |
|---|---|---|
| sw06-p5 | 508160 |
| sw08-p4 | 508160 |
| sw04-p4 | 506560 |
| sw02-p2 | 489920 |
| sw06-p4 | 406720 |
| sw02-p4 | 400640 |
| sw04-p5 | 400640 |
| S1-p0 | 393280 |
| sw08-p2 | 282560 |
| sw01-p4 | 243840 |
| sw03-p5 | 243840 |
| sw05-p4 | 243840 |
| sw07-p5 | 243840 |
| S3-p0 | 243840 |
| sw01-p2 | 209920 |
| sw03-p4 | 209920 |
| sw05-p5 | 209920 |
| sw07-p4 | 209920 |
| sw08-p5 | 209920 |

## Opportunistic overlay window creation (deterministic post-pass)

**38** new overlay window(s), **6878400 ns** total, carved out of already-open best-effort spans on ports at or below utilisation 0.2 -- best-effort stays reachable inside each one (gate mask keeps its BE bits set). Run once after training/finalize_grow_only(), not a trained action.

| port | queue | size (ns) |
|---|---|---|
| S1-p0 | Q6 | 193600 |
| S1-p0 | Q7 | 199680 |
| S3-p0 | Q6 | 24960 |
| S3-p0 | Q7 | 218880 |
| sw01-p2 | Q6 | 96000 |
| sw01-p2 | Q7 | 204480 |
| sw01-p4 | Q6 | 66560 |
| sw01-p4 | Q7 | 193920 |
| sw02-p2 | Q6 | 365440 |
| sw02-p2 | Q7 | 180160 |
| sw02-p4 | Q6 | 197760 |
| sw02-p4 | Q7 | 219520 |
| sw03-p4 | Q6 | 96000 |
| sw03-p4 | Q7 | 187840 |
| sw03-p5 | Q6 | 133120 |
| sw03-p5 | Q7 | 144000 |
| sw04-p4 | Q6 | 349440 |
| sw04-p4 | Q7 | 196160 |
| sw04-p5 | Q6 | 172160 |
| sw04-p5 | Q7 | 261760 |
| sw05-p4 | Q6 | 214080 |
| sw05-p4 | Q7 | 79680 |
| sw05-p5 | Q6 | 177600 |
| sw05-p5 | Q7 | 89600 |
| sw06-p4 | Q6 | 251840 |
| sw06-p4 | Q7 | 204800 |
| sw06-p5 | Q6 | 194560 |
| sw06-p5 | Q7 | 336000 |
| sw07-p4 | Q6 | 164800 |
| sw07-p4 | Q7 | 85760 |
| sw07-p5 | Q6 | 189120 |
| sw07-p5 | Q7 | 121280 |
| sw08-p2 | Q6 | 202560 |
| sw08-p2 | Q7 | 117440 |
| sw08-p4 | Q6 | 136960 |
| sw08-p4 | Q7 | 376960 |
| sw08-p5 | Q6 | 148160 |
| sw08-p5 | Q7 | 85760 |

## Per-port GCL entries: before (SMT) vs. after (RL-enlarged)

| port | SMT entries | RL-enlarged entries | GCL_size |
|---|---|---|---|
| sw01-p2 | 21 | 30 | 255 |
| sw01-p4 | 15 | 22 | 255 |
| sw02-p2 | 13 | 31 | 255 |
| sw02-p4 | 15 | 22 | 255 |
| sw03-p4 | 21 | 30 | 255 |
| sw03-p5 | 15 | 22 | 255 |
| sw04-p4 | 13 | 25 | 255 |
| sw04-p5 | 15 | 19 | 255 |
| sw05-p4 | 15 | 19 | 255 |
| sw05-p5 | 21 | 33 | 255 |
| sw06-p4 | 15 | 20 | 255 |
| sw06-p5 | 13 | 26 | 255 |
| sw07-p4 | 21 | 29 | 255 |
| sw07-p5 | 15 | 23 | 255 |
| sw08-p2 | 23 | 20 | 255 |
| sw08-p4 | 13 | 30 | 255 |
| sw08-p5 | 21 | 29 | 255 |

## Flows

| flow | route | fixed | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|---|
| s0(id=1 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | no | None | None | None | no |
| s1(id=2 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | no | None | None | None | no |
| s2(id=3 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | yes | 7 | 24960 | 145680 | yes |
| s3(id=4 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |
| s4(id=5 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | yes | 6 | 0 | 95760 | yes |
| s5(id=6 S3->S1) | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | no | None | None | None | no |
| s6(id=7 S3->S1) | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | no | None | None | None | no |
| s7(id=8 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | yes | 6 | 62400 | 95760 | yes |
| s8(id=9 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | yes | 6 | 37440 | 95760 | yes |
| s9(id=10 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | yes | 6 | 0 | 79120 | yes |
| s10(id=11 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |
| s11(id=12 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |
| s12(id=13 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | yes | 7 | 49920 | 79120 | yes |
| s13(id=14 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | yes | 6 | 0 | 79120 | yes |
| s14(id=15 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | yes | 6 | 49920 | 159120 | yes |
| s15(id=16 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |
| s16(id=17 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | yes | 7 | 99840 | 96400 | yes |
| s17(id=18 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | no | None | None | None | no |
| s18(id=19 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | yes | 6 | 24960 | 95760 | yes |
| s19(id=20 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | yes | 6 | 74880 | 108560 | yes |

## Per-hop windows (slack_ns > 0 means this window was enlarged)

| flow | egress port | queue | psi (ns) | delta (ns) |
|---|---|---|---|---|
| s2(id=3 S1->S3) | S1-p0 | Q7 | 24960 | 12480 |
| s2(id=3 S1->S3) | sw02-p4 | Q7 | 41600 | 12480 |
| s2(id=3 S1->S3) | sw04-p5 | Q7 | 58240 | 12480 |
| s2(id=3 S1->S3) | sw06-p4 | Q7 | 74880 | 12480 |
| s2(id=3 S1->S3) | sw08-p5 | Q7 | 91520 | 12480 |
| s2(id=3 S1->S3) | sw07-p4 | Q7 | 108160 | 12480 |
| s2(id=3 S1->S3) | sw05-p5 | Q7 | 124800 | 12480 |
| s2(id=3 S1->S3) | sw03-p4 | Q7 | 141440 | 12480 |
| s2(id=3 S1->S3) | sw01-p2 | Q7 | 158080 | 12480 |
| s4(id=5 S3->S2) | S3-p0 | Q6 | 0 | 12480 |
| s4(id=5 S3->S2) | sw01-p4 | Q6 | 16640 | 12480 |
| s4(id=5 S3->S2) | sw03-p5 | Q6 | 33280 | 12480 |
| s4(id=5 S3->S2) | sw05-p4 | Q6 | 49920 | 12480 |
| s4(id=5 S3->S2) | sw07-p5 | Q6 | 66560 | 12480 |
| s4(id=5 S3->S2) | sw08-p2 | Q6 | 83200 | 12480 |
| s7(id=8 S3->S2) | S3-p0 | Q6 | 62400 | 12480 |
| s7(id=8 S3->S2) | sw01-p4 | Q6 | 79040 | 12480 |
| s7(id=8 S3->S2) | sw03-p5 | Q6 | 95680 | 12480 |
| s7(id=8 S3->S2) | sw05-p4 | Q6 | 112320 | 12480 |
| s7(id=8 S3->S2) | sw07-p5 | Q6 | 128960 | 12480 |
| s7(id=8 S3->S2) | sw08-p2 | Q6 | 145600 | 12480 |
| s8(id=9 S3->S2) | S3-p0 | Q6 | 37440 | 12480 |
| s8(id=9 S3->S2) | sw01-p4 | Q6 | 54080 | 12480 |
| s8(id=9 S3->S2) | sw03-p5 | Q6 | 70720 | 12480 |
| s8(id=9 S3->S2) | sw05-p4 | Q6 | 87360 | 12480 |
| s8(id=9 S3->S2) | sw07-p5 | Q6 | 104000 | 12480 |
| s8(id=9 S3->S2) | sw08-p2 | Q6 | 120640 | 12480 |
| s9(id=10 S2->S1) | S2-p0 | Q6 | 0 | 12480 |
| s9(id=10 S2->S1) | sw08-p4 | Q6 | 16640 | 12480 |
| s9(id=10 S2->S1) | sw06-p5 | Q6 | 33280 | 12480 |
| s9(id=10 S2->S1) | sw04-p4 | Q6 | 49920 | 12480 |
| s9(id=10 S2->S1) | sw02-p2 | Q6 | 66560 | 12480 |
| s12(id=13 S2->S1) | S2-p0 | Q7 | 49920 | 12480 |
| s12(id=13 S2->S1) | sw08-p4 | Q7 | 66560 | 12480 |
| s12(id=13 S2->S1) | sw06-p5 | Q7 | 83200 | 12480 |
| s12(id=13 S2->S1) | sw04-p4 | Q7 | 99840 | 12480 |
| s12(id=13 S2->S1) | sw02-p2 | Q7 | 116480 | 12480 |
| s13(id=14 S1->S2) | S1-p0 | Q6 | 0 | 12480 |
| s13(id=14 S1->S2) | sw02-p4 | Q6 | 16640 | 12480 |
| s13(id=14 S1->S2) | sw04-p5 | Q6 | 33280 | 12480 |
| s13(id=14 S1->S2) | sw06-p4 | Q6 | 49920 | 12480 |
| s13(id=14 S1->S2) | sw08-p2 | Q6 | 66560 | 12480 |
| s14(id=15 S1->S3) | S1-p0 | Q6 | 49920 | 12480 |
| s14(id=15 S1->S3) | sw02-p4 | Q6 | 73920 | 12480 |
| s14(id=15 S1->S3) | sw04-p5 | Q6 | 90560 | 12480 |
| s14(id=15 S1->S3) | sw06-p4 | Q6 | 113280 | 12480 |
| s14(id=15 S1->S3) | sw08-p5 | Q6 | 129920 | 12480 |
| s14(id=15 S1->S3) | sw07-p4 | Q6 | 146560 | 12480 |
| s14(id=15 S1->S3) | sw05-p5 | Q6 | 163200 | 12480 |
| s14(id=15 S1->S3) | sw03-p4 | Q6 | 179840 | 12480 |
| s14(id=15 S1->S3) | sw01-p2 | Q6 | 196480 | 12480 |
| s16(id=17 S2->S3) | S2-p0 | Q7 | 99840 | 12480 |
| s16(id=17 S2->S3) | sw08-p5 | Q7 | 117120 | 12480 |
| s16(id=17 S2->S3) | sw07-p4 | Q7 | 133760 | 12480 |
| s16(id=17 S2->S3) | sw05-p5 | Q7 | 150400 | 12480 |
| s16(id=17 S2->S3) | sw03-p4 | Q7 | 167040 | 12480 |
| s16(id=17 S2->S3) | sw01-p2 | Q7 | 183680 | 12480 |
| s18(id=19 S2->S3) | S2-p0 | Q6 | 24960 | 12480 |
| s18(id=19 S2->S3) | sw08-p5 | Q6 | 41600 | 12480 |
| s18(id=19 S2->S3) | sw07-p4 | Q6 | 58240 | 12480 |
| s18(id=19 S2->S3) | sw05-p5 | Q6 | 74880 | 12480 |
| s18(id=19 S2->S3) | sw03-p4 | Q6 | 91520 | 12480 |
| s18(id=19 S2->S3) | sw01-p2 | Q6 | 108160 | 12480 |
| s19(id=20 S2->S3) | S2-p0 | Q6 | 74880 | 12480 |
| s19(id=20 S2->S3) | sw08-p5 | Q6 | 104320 | 12480 |
| s19(id=20 S2->S3) | sw07-p4 | Q6 | 120960 | 12480 |
| s19(id=20 S2->S3) | sw05-p5 | Q6 | 137600 | 12480 |
| s19(id=20 S2->S3) | sw03-p4 | Q6 | 154240 | 12480 |
| s19(id=20 S2->S3) | sw01-p2 | Q6 | 170880 | 12480 |

## Metrics (training/evaluation signal, not the export)

| metric | value |
|---|---|
| trial-placed flow ratio (fixed + trial-admitted) | 0.800 |
| r1  same-queue window adjacency | 0.203 |
| r2  deadline-violation ratio | 0.000 |
| r3  supplier/receiver overlap | 0.998 |
| r4  mean e2e/deadline (admitted) | 0.323 |
| constraint violations | 0 |

## Constraint check

- C1-C7, C9: OK
- seed-integrity (no SMT-fixed flow's placement changed): OK

## GCL per egress port

### sw01-p2  (30 entries, util 15.6000 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 45760 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 1920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 59520 0x40 # 01000000   Q6
sgs 39680 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 147840 0x40 # 01000000   Q6
sgs 39680 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 1920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 85120 0x40 # 01000000   Q6
sgs 39680 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 52160 0x40 # 01000000   Q6
sgs 39680 0xBF # 10111111   Q7
```

### sw01-p4  (22 entries, util 10.9200 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 82880 0x40 # 01000000   Q6
sgs 38080 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 132800 0x80 # 10000000   Q7
sgs 38080 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 107840 0x40 # 01000000   Q6
sgs 38080 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 116160 0x80 # 10000000   Q7
sgs 54720 0xBF # 10111111   Q7
```

### sw02-p2  (31 entries, util 9.3600 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 21120 0xBF # 10111111   Q7
sgs 16320 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 10880 0x3F # 00111111   BE
sgs 23360 0x80 # 10000000   Q7
sgs 43520 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 18880 0x40 # 01000000   Q6
sgs 14720 0xBF # 10111111   Q7
sgs 45440 0x7F # 01111111   Q6
sgs 60800 0x80 # 10000000   Q7
sgs 43520 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 21120 0xBF # 10111111   Q7
sgs 16320 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 46720 0x40 # 01000000   Q6
sgs 43520 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 18880 0x40 # 01000000   Q6
sgs 14720 0xBF # 10111111   Q7
sgs 45440 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 41920 0xBF # 10111111   Q7
```

### sw02-p4  (22 entries, util 10.9200 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 19840 0xBF # 10111111   Q7
sgs 53760 0x40 # 01000000   Q6
sgs 22400 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 111040 0x40 # 01000000   Q6
sgs 22400 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 86080 0x80 # 10000000   Q7
sgs 22400 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 94400 0x40 # 01000000   Q6
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (30 entries, util 15.6000 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 1920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 59520 0x40 # 01000000   Q6
sgs 39680 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 147840 0x40 # 01000000   Q6
sgs 39680 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 1920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 85120 0x40 # 01000000   Q6
sgs 39680 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 68800 0x40 # 01000000   Q6
sgs 39680 0xBF # 10111111   Q7
```

### sw03-p5  (22 entries, util 10.9200 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 82880 0x40 # 01000000   Q6
sgs 21440 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 132800 0x80 # 10000000   Q7
sgs 21440 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 107840 0x40 # 01000000   Q6
sgs 21440 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 99520 0x80 # 10000000   Q7
sgs 54720 0xBF # 10111111   Q7
```

### sw04-p4  (25 entries, util 9.3600 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 10880 0x3F # 00111111   BE
sgs 23360 0x80 # 10000000   Q7
sgs 60160 0x7F # 01111111   Q6
sgs 18880 0x40 # 01000000   Q6
sgs 31360 0xBF # 10111111   Q7
sgs 28800 0x7F # 01111111   Q6
sgs 60800 0x80 # 10000000   Q7
sgs 60160 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 46720 0x40 # 01000000   Q6
sgs 60160 0x7F # 01111111   Q6
sgs 18880 0x40 # 01000000   Q6
sgs 31360 0xBF # 10111111   Q7
sgs 28800 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 58560 0xBF # 10111111   Q7
```

### sw04-p5  (19 entries, util 10.9200 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 19840 0xBF # 10111111   Q7
sgs 53760 0x40 # 01000000   Q6
sgs 55680 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 111040 0x40 # 01000000   Q6
sgs 55680 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 86080 0x80 # 10000000   Q7
sgs 55680 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 77760 0x40 # 01000000   Q6
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (19 entries, util 10.9200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 82880 0x40 # 01000000   Q6
sgs 54720 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 132800 0x80 # 10000000   Q7
sgs 54720 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 107840 0x40 # 01000000   Q6
sgs 54720 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 82880 0x80 # 10000000   Q7
sgs 54720 0xBF # 10111111   Q7
```

### sw05-p5  (33 entries, util 15.6000 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 1920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 59520 0x40 # 01000000   Q6
sgs 27200 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 147840 0x40 # 01000000   Q6
sgs 27200 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 1920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 85120 0x40 # 01000000   Q6
sgs 27200 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 85440 0x40 # 01000000   Q6
sgs 39680 0xBF # 10111111   Q7
```

### sw06-p4  (20 entries, util 10.9200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 13120 0x7F # 01111111   Q6
sgs 47680 0x40 # 01000000   Q6
sgs 39040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 111040 0x40 # 01000000   Q6
sgs 39040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 86080 0x80 # 10000000   Q7
sgs 39040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 61120 0x40 # 01000000   Q6
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (26 entries, util 9.3600 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 10880 0x3F # 00111111   BE
sgs 23360 0x80 # 10000000   Q7
sgs 26880 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 18880 0x40 # 01000000   Q6
sgs 60160 0xBF # 10111111   Q7
sgs 60800 0x80 # 10000000   Q7
sgs 26880 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 46720 0x40 # 01000000   Q6
sgs 26880 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 18880 0x40 # 01000000   Q6
sgs 60160 0xBF # 10111111   Q7
sgs 27520 0x80 # 10000000   Q7
sgs 60160 0xBF # 10111111   Q7
```

### sw07-p4  (29 entries, util 15.6000 %)

```
sgs 45760 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 1920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 23040 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 59520 0x40 # 01000000   Q6
sgs 39680 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 147840 0x40 # 01000000   Q6
sgs 39680 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 1920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 23040 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 85120 0x40 # 01000000   Q6
sgs 39680 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 102080 0x40 # 01000000   Q6
sgs 39680 0xBF # 10111111   Q7
```

### sw07-p5  (23 entries, util 10.9200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 82880 0x40 # 01000000   Q6
sgs 38080 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 132800 0x80 # 10000000   Q7
sgs 38080 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 107840 0x40 # 01000000   Q6
sgs 38080 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 66240 0x80 # 10000000   Q7
sgs 54720 0xBF # 10111111   Q7
```

### sw08-p2  (20 entries, util 17.1600 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 29120 0x40 # 01000000   Q6
sgs 24960 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 70080 0x40 # 01000000   Q6
sgs 34240 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 149120 0x40 # 01000000   Q6
sgs 34240 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 29120 0x40 # 01000000   Q6
sgs 24960 0x7F # 01111111   Q6
sgs 95040 0x40 # 01000000   Q6
sgs 34240 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 82560 0x40 # 01000000   Q6
sgs 50880 0xBF # 10111111   Q7
```

### sw08-p4  (30 entries, util 9.3600 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 30720 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 10880 0x3F # 00111111   BE
sgs 23360 0x80 # 10000000   Q7
sgs 43520 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 18880 0x40 # 01000000   Q6
sgs 14400 0x7F # 01111111   Q6
sgs 45760 0xBF # 10111111   Q7
sgs 60800 0x80 # 10000000   Q7
sgs 43520 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 30720 0xBF # 10111111   Q7
sgs 46720 0x40 # 01000000   Q6
sgs 43520 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 18880 0x40 # 01000000   Q6
sgs 14400 0x7F # 01111111   Q6
sgs 45760 0xBF # 10111111   Q7
sgs 44160 0x80 # 10000000   Q7
sgs 60160 0xBF # 10111111   Q7
```

### sw08-p5  (29 entries, util 15.6000 %)

```
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 1920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 23040 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 59520 0x40 # 01000000   Q6
sgs 39680 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 147840 0x40 # 01000000   Q6
sgs 39680 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 1920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 23040 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 85120 0x40 # 01000000   Q6
sgs 39680 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 118720 0x40 # 01000000   Q6
sgs 39680 0xBF # 10111111   Q7
```

