# RL-enlarged GCL schedule (Problem 2: window enlargement)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Seeded from SMT run: **result/result-2026-10-12-dataset-testbed-10-ring-avgwin/smt-c9-off/10-t3600-c9off-minlat**

## Admission (unchanged) vs. capacity grown

Problem 2 never admits a flow into the schedule it exports -- it only widens windows. `admitted` below is exactly the SMT baseline, by construction; the capacity growth this run achieved is banked slack and per-port GCL entries, reported separately.

| | admitted | of total |
|---|---|---|
| SMT (fixed, never moved) | 11 | 20 |
| RL-enlarged (exported; grow-only, admits nothing new) | 11 | 20 |

During training, the policy's trial admissions (the reward signal that teaches it how much a window needs to grow) reached **8** of the 9 SMT-rejected flows -- none of those are kept in this export; that capacity stays as empty, banked slack for Problem 3 to fill. Total slack banked: 501120 ns. GCL_size overflow: 0.

## Opportunistic idle top-up (deterministic post-pass)

**13790400 ns**, drawn from idle capacity on ports at or below utilisation 0.2, independent of what training happened to grow. Ported from prob_2_heuristic_enlarged's Step 7.

| port | queue | applied (ns) |
|---|---|---|
| S1-p0 | Q6 | 462720 |
| S1-p0 | Q7 | 112640 |
| S2-p0 | Q6 | 137600 |
| S2-p0 | Q7 | 550080 |
| S3-p0 | Q6 | 450240 |
| S3-p0 | Q7 | 137600 |
| sw01-p2 | Q6 | 113920 |
| sw01-p2 | Q7 | 390720 |
| sw01-p4 | Q7 | 602880 |
| sw01-p5 | Q6 | 435520 |
| sw01-p5 | Q7 | 210560 |
| sw02-p2 | Q6 | 416320 |
| sw02-p2 | Q7 | 136640 |
| sw02-p4 | Q6 | 557120 |
| sw02-p4 | Q7 | 138240 |
| sw02-p5 | Q6 | 160640 |
| sw02-p5 | Q7 | 435520 |
| sw03-p4 | Q6 | 338560 |
| sw03-p4 | Q7 | 313280 |
| sw03-p5 | Q7 | 584320 |
| sw04-p4 | Q6 | 5760 |
| sw04-p4 | Q7 | 656960 |
| sw04-p5 | Q6 | 540480 |
| sw04-p5 | Q7 | 138240 |
| sw05-p4 | Q7 | 565760 |
| sw05-p5 | Q6 | 338560 |
| sw05-p5 | Q7 | 329920 |
| sw06-p4 | Q6 | 523840 |
| sw06-p4 | Q7 | 138240 |
| sw06-p5 | Q6 | 5760 |
| sw06-p5 | Q7 | 673600 |
| sw07-p4 | Q6 | 338560 |
| sw07-p4 | Q7 | 346560 |
| sw07-p5 | Q7 | 547200 |
| sw08-p2 | Q6 | 290560 |
| sw08-p2 | Q7 | 248320 |
| sw08-p4 | Q6 | 375040 |
| sw08-p4 | Q7 | 333440 |
| sw08-p5 | Q6 | 325120 |
| sw08-p5 | Q7 | 383360 |

## Opportunistic exclusive window creation (deterministic post-pass)

**4** brand-new *exclusive* window(s) opened, **49920 ns** total, on ports at or below utilisation 0.2 whose TT queue had zero windows before this run. Ported from prob_2_heuristic_enlarged's Step 8.

| port | queue | size (ns) |
|---|---|---|
| sw01-p4 | Q6 | 12480 |
| sw03-p5 | Q6 | 12480 |
| sw05-p4 | Q6 | 12480 |
| sw07-p5 | Q6 | 12480 |

## Best-effort gap equalization (deterministic post-pass)

**8576000 ns** given back from the top-up/creation above so each port's leftover non-TAS gaps land close to equal. Ported from prob_2_heuristic_enlarged's Step 9.

| port | given back (ns) |
|---|---|---|
| sw02-p4 | 528320 |
| sw04-p5 | 528320 |
| sw06-p4 | 517440 |
| sw01-p4 | 499200 |
| sw03-p5 | 499200 |
| sw05-p4 | 499200 |
| sw07-p5 | 495360 |
| sw08-p5 | 438400 |
| sw03-p4 | 424960 |
| sw05-p5 | 424960 |
| sw07-p4 | 424960 |
| sw04-p4 | 399360 |
| sw06-p5 | 399360 |
| sw08-p4 | 393600 |
| sw01-p5 | 328000 |
| sw02-p5 | 313600 |
| S2-p0 | 309120 |
| sw01-p2 | 267520 |
| sw08-p2 | 263040 |
| sw02-p2 | 262080 |
| S3-p0 | 220480 |
| S1-p0 | 139520 |

## Opportunistic overlay window creation (deterministic post-pass)

**43** new overlay window(s), **9412160 ns** total, carved out of already-open best-effort spans on ports at or below utilisation 0.2 -- best-effort stays reachable inside each one (gate mask keeps its BE bits set). Run once after training/finalize_grow_only(), not a trained action.

| port | queue | size (ns) |
|---|---|---|
| S1-p0 | Q7 | 139520 |
| S2-p0 | Q6 | 109440 |
| S2-p0 | Q7 | 199680 |
| S3-p0 | Q6 | 24960 |
| S3-p0 | Q7 | 195520 |
| sw01-p2 | Q6 | 140800 |
| sw01-p2 | Q7 | 157440 |
| sw01-p4 | Q6 | 274560 |
| sw01-p4 | Q7 | 224640 |
| sw01-p5 | Q6 | 156480 |
| sw01-p5 | Q7 | 200640 |
| sw02-p2 | Q6 | 225280 |
| sw02-p2 | Q7 | 80640 |
| sw02-p4 | Q6 | 311040 |
| sw02-p4 | Q7 | 259520 |
| sw02-p5 | Q6 | 66560 |
| sw02-p5 | Q7 | 263680 |
| sw03-p4 | Q6 | 253120 |
| sw03-p4 | Q7 | 233600 |
| sw03-p5 | Q6 | 295360 |
| sw03-p5 | Q7 | 224640 |
| sw04-p4 | Q6 | 243200 |
| sw04-p4 | Q7 | 250240 |
| sw04-p5 | Q6 | 327680 |
| sw04-p5 | Q7 | 259520 |
| sw05-p4 | Q6 | 312000 |
| sw05-p4 | Q7 | 224640 |
| sw05-p5 | Q6 | 280000 |
| sw05-p5 | Q7 | 190080 |
| sw06-p4 | Q6 | 298560 |
| sw06-p4 | Q7 | 294400 |
| sw06-p5 | Q6 | 241920 |
| sw06-p5 | Q7 | 234880 |
| sw07-p4 | Q6 | 253760 |
| sw07-p4 | Q7 | 199680 |
| sw07-p5 | Q6 | 237120 |
| sw07-p5 | Q7 | 312320 |
| sw08-p2 | Q6 | 121920 |
| sw08-p2 | Q7 | 190400 |
| sw08-p4 | Q6 | 254720 |
| sw08-p4 | Q7 | 192960 |
| sw08-p5 | Q6 | 255360 |
| sw08-p5 | Q7 | 199680 |

## Per-port GCL entries: before (SMT) vs. after (RL-enlarged)

| port | SMT entries | RL-enlarged entries | GCL_size |
|---|---|---|---|
| sw01-p2 | 25 | 31 | 255 |
| sw01-p4 | 9 | 18 | 255 |
| sw01-p5 | 11 | 23 | 255 |
| sw02-p2 | 13 | 23 | 255 |
| sw02-p4 | 11 | 19 | 255 |
| sw02-p5 | 13 | 22 | 255 |
| sw03-p4 | 13 | 21 | 255 |
| sw03-p5 | 9 | 18 | 255 |
| sw04-p4 | 3 | 15 | 255 |
| sw04-p5 | 11 | 19 | 255 |
| sw05-p4 | 9 | 18 | 255 |
| sw05-p5 | 13 | 17 | 255 |
| sw06-p4 | 11 | 19 | 255 |
| sw06-p5 | 3 | 14 | 255 |
| sw07-p4 | 13 | 20 | 255 |
| sw07-p5 | 9 | 19 | 255 |
| sw08-p2 | 19 | 25 | 255 |
| sw08-p4 | 3 | 12 | 255 |
| sw08-p5 | 13 | 20 | 255 |

## Flows

| flow | route | fixed | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|---|
| s0(id=1 S3->S1) | S3->sw01->sw02->S1 | yes | 7 | 24960 | 45840 | yes |
| s1(id=2 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | no | None | None | None | no |
| s2(id=3 S1->S3) | S1->sw02->sw01->S3 | yes | 6 | 0 | 45840 | yes |
| s3(id=4 S1->S3) | S1->sw02->sw01->S3 | no | None | None | None | no |
| s4(id=5 S3->S1) | S3->sw01->sw02->S1 | yes | 7 | 74880 | 45840 | yes |
| s5(id=6 S1->S3) | S1->sw02->sw01->S3 | no | None | None | None | no |
| s6(id=7 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | yes | 7 | 0 | 108560 | yes |
| s7(id=8 S1->S3) | S1->sw02->sw01->S3 | no | None | None | None | no |
| s8(id=9 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | yes | 7 | 0 | 95760 | yes |
| s9(id=10 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | yes | 6 | 49920 | 83600 | yes |
| s10(id=11 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | yes | 6 | 24960 | 96400 | yes |
| s11(id=12 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | yes | 6 | 24960 | 83600 | yes |
| s12(id=13 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | no | None | None | None | no |
| s13(id=14 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | no | None | None | None | no |
| s14(id=15 S3->S1) | S3->sw01->sw02->S1 | yes | 7 | 49920 | 45840 | yes |
| s15(id=16 S3->S1) | S3->sw01->sw02->S1 | no | None | None | None | no |
| s16(id=17 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | yes | 7 | 74880 | 79120 | yes |
| s17(id=18 S1->S3) | S1->sw02->sw01->S3 | yes | 6 | 49920 | 45840 | yes |
| s18(id=19 S3->S1) | S3->sw01->sw02->S1 | no | None | None | None | no |
| s19(id=20 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |

## Per-hop windows (slack_ns > 0 means this window was enlarged)

| flow | egress port | queue | psi (ns) | delta (ns) |
|---|---|---|---|---|
| s0(id=1 S3->S1) | S3-p0 | Q7 | 24960 | 12480 |
| s0(id=1 S3->S1) | sw01-p5 | Q7 | 41600 | 12480 |
| s0(id=1 S3->S1) | sw02-p2 | Q7 | 58240 | 12480 |
| s2(id=3 S1->S3) | S1-p0 | Q6 | 0 | 12480 |
| s2(id=3 S1->S3) | sw02-p5 | Q6 | 16640 | 12480 |
| s2(id=3 S1->S3) | sw01-p2 | Q6 | 33280 | 12480 |
| s4(id=5 S3->S1) | S3-p0 | Q7 | 74880 | 12480 |
| s4(id=5 S3->S1) | sw01-p5 | Q7 | 91520 | 12480 |
| s4(id=5 S3->S1) | sw02-p2 | Q7 | 108160 | 12480 |
| s6(id=7 S2->S3) | S2-p0 | Q7 | 0 | 12480 |
| s6(id=7 S2->S3) | sw08-p5 | Q7 | 16640 | 12480 |
| s6(id=7 S2->S3) | sw07-p4 | Q7 | 40000 | 12480 |
| s6(id=7 S2->S3) | sw05-p5 | Q7 | 56640 | 12480 |
| s6(id=7 S2->S3) | sw03-p4 | Q7 | 73280 | 12480 |
| s6(id=7 S2->S3) | sw01-p2 | Q7 | 96000 | 12480 |
| s8(id=9 S3->S2) | S3-p0 | Q7 | 0 | 12480 |
| s8(id=9 S3->S2) | sw01-p4 | Q7 | 16640 | 12480 |
| s8(id=9 S3->S2) | sw03-p5 | Q7 | 33280 | 12480 |
| s8(id=9 S3->S2) | sw05-p4 | Q7 | 49920 | 12480 |
| s8(id=9 S3->S2) | sw07-p5 | Q7 | 66560 | 12480 |
| s8(id=9 S3->S2) | sw08-p2 | Q7 | 83200 | 12480 |
| s9(id=10 S2->S1) | S2-p0 | Q6 | 49920 | 12480 |
| s9(id=10 S2->S1) | sw08-p4 | Q6 | 66560 | 12480 |
| s9(id=10 S2->S1) | sw06-p5 | Q6 | 83200 | 12480 |
| s9(id=10 S2->S1) | sw04-p4 | Q6 | 99840 | 12480 |
| s9(id=10 S2->S1) | sw02-p2 | Q6 | 120960 | 12480 |
| s10(id=11 S2->S3) | S2-p0 | Q6 | 24960 | 12480 |
| s10(id=11 S2->S3) | sw08-p5 | Q6 | 41600 | 12480 |
| s10(id=11 S2->S3) | sw07-p4 | Q6 | 58240 | 12480 |
| s10(id=11 S2->S3) | sw05-p5 | Q6 | 74880 | 12480 |
| s10(id=11 S2->S3) | sw03-p4 | Q6 | 91520 | 12480 |
| s10(id=11 S2->S3) | sw01-p2 | Q6 | 108800 | 12480 |
| s11(id=12 S1->S2) | S1-p0 | Q6 | 24960 | 12480 |
| s11(id=12 S1->S2) | sw02-p4 | Q6 | 42240 | 12480 |
| s11(id=12 S1->S2) | sw04-p5 | Q6 | 58880 | 12480 |
| s11(id=12 S1->S2) | sw06-p4 | Q6 | 75520 | 12480 |
| s11(id=12 S1->S2) | sw08-p2 | Q6 | 96000 | 12480 |
| s14(id=15 S3->S1) | S3-p0 | Q7 | 49920 | 12480 |
| s14(id=15 S3->S1) | sw01-p5 | Q7 | 66560 | 12480 |
| s14(id=15 S3->S1) | sw02-p2 | Q7 | 83200 | 12480 |
| s16(id=17 S1->S2) | S1-p0 | Q7 | 74880 | 12480 |
| s16(id=17 S1->S2) | sw02-p4 | Q7 | 91520 | 12480 |
| s16(id=17 S1->S2) | sw04-p5 | Q7 | 108160 | 12480 |
| s16(id=17 S1->S2) | sw06-p4 | Q7 | 124800 | 12480 |
| s16(id=17 S1->S2) | sw08-p2 | Q7 | 141440 | 12480 |
| s17(id=18 S1->S3) | S1-p0 | Q6 | 49920 | 12480 |
| s17(id=18 S1->S3) | sw02-p5 | Q6 | 66560 | 12480 |
| s17(id=18 S1->S3) | sw01-p2 | Q6 | 83200 | 12480 |

## Metrics (training/evaluation signal, not the export)

| metric | value |
|---|---|
| trial-placed flow ratio (fixed + trial-admitted) | 0.950 |
| r1  same-queue window adjacency | 0.387 |
| r2  deadline-violation ratio | 0.000 |
| r3  supplier/receiver overlap | 0.995 |
| r4  mean e2e/deadline (admitted) | 0.208 |
| constraint violations | 0 |

## Constraint check

- C1-C7, C9: OK
- seed-integrity (no SMT-fixed flow's placement changed): OK

## GCL per egress port

### sw01-p2  (31 entries, util 18.7200 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 1280 0x3F # 00111111   BE
sgs 74880 0x80 # 10000000   Q7
sgs 35840 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0x80 # 10000000   Q7
sgs 35840 0xBF # 10111111   Q7
sgs 101440 0x80 # 10000000   Q7
sgs 35840 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 88640 0x40 # 01000000   Q6
sgs 35840 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0x80 # 10000000   Q7
sgs 35840 0xBF # 10111111   Q7
sgs 68160 0x80 # 10000000   Q7
sgs 35840 0xBF # 10111111   Q7
```

### sw01-p4  (18 entries, util 6.2400 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 75200 0x80 # 10000000   Q7
sgs 58240 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 75200 0x80 # 10000000   Q7
sgs 58240 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 75200 0x80 # 10000000   Q7
sgs 58240 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 58560 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p5  (23 entries, util 7.8000 %)

```
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 35200 0x40 # 01000000   Q6
sgs 37760 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 133120 0x40 # 01000000   Q6
sgs 37760 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 95680 0x80 # 10000000   Q7
sgs 37760 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 104000 0x40 # 01000000   Q6
sgs 16960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (23 entries, util 9.3600 %)

```
sgs 45760 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 1280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 42560 0x40 # 01000000   Q6
sgs 55680 0x7F # 01111111   Q6
sgs 144320 0x40 # 01000000   Q6
sgs 55680 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 106880 0x80 # 10000000   Q7
sgs 55680 0x7F # 01111111   Q6
sgs 98560 0x40 # 01000000   Q6
sgs 55680 0xBF # 10111111   Q7
```

### sw02-p4  (19 entries, util 7.8000 %)

```
sgs 42240 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 36800 0xBF # 10111111   Q7
sgs 27840 0x80 # 10000000   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 42240 0x7F # 01111111   Q6
sgs 77120 0x40 # 01000000   Q6
sgs 30720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 42240 0x7F # 01111111   Q6
sgs 77120 0x40 # 01000000   Q6
sgs 30720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 42240 0x7F # 01111111   Q6
sgs 34880 0x40 # 01000000   Q6
sgs 23040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p5  (22 entries, util 9.3600 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 23040 0xBF # 10111111   Q7
sgs 54400 0x80 # 10000000   Q7
sgs 43520 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 127360 0x80 # 10000000   Q7
sgs 43520 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 89920 0x40 # 01000000   Q6
sgs 43520 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 110720 0x80 # 10000000   Q7
sgs 60160 0xBF # 10111111   Q7
```

### sw03-p4  (21 entries, util 9.3600 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 23360 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 5760 0x3F # 00111111   BE
sgs 78400 0x40 # 01000000   Q6
sgs 30080 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 23360 0xBF # 10111111   Q7
sgs 96640 0x80 # 10000000   Q7
sgs 30080 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 23360 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 5760 0x3F # 00111111   BE
sgs 78400 0x40 # 01000000   Q6
sgs 30080 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 23360 0xBF # 10111111   Q7
sgs 23360 0x80 # 10000000   Q7
sgs 53440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p5  (18 entries, util 6.2400 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 75200 0x80 # 10000000   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 75200 0x80 # 10000000   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 75200 0x80 # 10000000   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 41920 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p4  (15 entries, util 1.5600 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 203200 0x80 # 10000000   Q7
sgs 28800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 17920 0x7F # 01111111   Q6
sgs 85120 0x80 # 10000000   Q7
sgs 46720 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (19 entries, util 7.8000 %)

```
sgs 58880 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 36800 0xBF # 10111111   Q7
sgs 27840 0x80 # 10000000   Q7
sgs 14080 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 58880 0x7F # 01111111   Q6
sgs 77120 0x40 # 01000000   Q6
sgs 14080 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 58880 0x7F # 01111111   Q6
sgs 77120 0x40 # 01000000   Q6
sgs 14080 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 58880 0x7F # 01111111   Q6
sgs 18240 0x40 # 01000000   Q6
sgs 23040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (18 entries, util 6.2400 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 75200 0x80 # 10000000   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 75200 0x80 # 10000000   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 75200 0x80 # 10000000   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 25280 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p5  (17 entries, util 9.3600 %)

```
sgs 56640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 5760 0x3F # 00111111   BE
sgs 78400 0x40 # 01000000   Q6
sgs 46720 0xBF # 10111111   Q7
sgs 56640 0x7F # 01111111   Q6
sgs 96640 0x80 # 10000000   Q7
sgs 46720 0xBF # 10111111   Q7
sgs 56640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 5760 0x3F # 00111111   BE
sgs 78400 0x40 # 01000000   Q6
sgs 46720 0xBF # 10111111   Q7
sgs 56640 0x7F # 01111111   Q6
sgs 40000 0x80 # 10000000   Q7
sgs 53440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p4  (19 entries, util 7.8000 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 25600 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 36800 0x7F # 01111111   Q6
sgs 27840 0x80 # 10000000   Q7
sgs 47360 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 25600 0xBF # 10111111   Q7
sgs 77120 0x40 # 01000000   Q6
sgs 47360 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 25600 0xBF # 10111111   Q7
sgs 77120 0x40 # 01000000   Q6
sgs 47360 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 25600 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 62080 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (14 entries, util 1.5600 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 203200 0x80 # 10000000   Q7
sgs 45440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 51520 0xBF # 10111111   Q7
sgs 101760 0x80 # 10000000   Q7
sgs 46720 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (20 entries, util 9.3600 %)

```
sgs 40000 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 5760 0x3F # 00111111   BE
sgs 78400 0x40 # 01000000   Q6
sgs 13440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 40000 0x7F # 01111111   Q6
sgs 96640 0x80 # 10000000   Q7
sgs 13440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 40000 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 5760 0x3F # 00111111   BE
sgs 78400 0x40 # 01000000   Q6
sgs 13440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 40000 0x7F # 01111111   Q6
sgs 56640 0x80 # 10000000   Q7
sgs 53440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p5  (19 entries, util 6.2400 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 75200 0x80 # 10000000   Q7
sgs 58240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 75200 0x80 # 10000000   Q7
sgs 58240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 75200 0x80 # 10000000   Q7
sgs 58240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 21120 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p2  (25 entries, util 14.0400 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12160 0x3F # 00111111   BE
sgs 105280 0x80 # 10000000   Q7
sgs 24000 0x7F # 01111111   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 129920 0x40 # 01000000   Q6
sgs 24000 0x7F # 01111111   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12160 0x3F # 00111111   BE
sgs 105280 0x80 # 10000000   Q7
sgs 24000 0x7F # 01111111   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 46720 0x40 # 01000000   Q6
sgs 57280 0xBF # 10111111   Q7
```

### sw08-p4  (12 entries, util 1.5600 %)

```
sgs 54080 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 190720 0x40 # 01000000   Q6
sgs 42880 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 54080 0x7F # 01111111   Q6
sgs 149120 0x80 # 10000000   Q7
sgs 46720 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (20 entries, util 9.3600 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 71680 0x40 # 01000000   Q6
sgs 36800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 96640 0x80 # 10000000   Q7
sgs 36800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 71680 0x40 # 01000000   Q6
sgs 36800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 80000 0x80 # 10000000   Q7
sgs 53440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

