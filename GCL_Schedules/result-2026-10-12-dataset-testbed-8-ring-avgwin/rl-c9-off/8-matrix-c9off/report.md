# RL-enlarged GCL schedule (Problem 2: window enlargement)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Seeded from SMT run: **result/result-2026-10-12-dataset-testbed-8-ring-avgwin/smt-c9-off/8-t3600-c9off-minlat**

## Admission (unchanged) vs. capacity grown

Problem 2 never admits a flow into the schedule it exports -- it only widens windows. `admitted` below is exactly the SMT baseline, by construction; the capacity growth this run achieved is banked slack and per-port GCL entries, reported separately.

| | admitted | of total |
|---|---|---|
| SMT (fixed, never moved) | 10 | 20 |
| RL-enlarged (exported; grow-only, admits nothing new) | 10 | 20 |

During training, the policy's trial admissions (the reward signal that teaches it how much a window needs to grow) reached **7** of the 10 SMT-rejected flows -- none of those are kept in this export; that capacity stays as empty, banked slack for Problem 3 to fill. Total slack banked: 318400 ns. GCL_size overflow: 0.

## Opportunistic idle top-up (deterministic post-pass)

**14081920 ns**, drawn from idle capacity on ports at or below utilisation 0.2, independent of what training happened to grow. Ported from prob_2_heuristic_enlarged's Step 7.

| port | queue | applied (ns) |
|---|---|---|
| S1-p0 | Q6 | 425280 |
| S1-p0 | Q7 | 137600 |
| S2-p0 | Q6 | 550080 |
| S2-p0 | Q7 | 125120 |
| S3-p0 | Q7 | 650240 |
| sw01-p2 | Q6 | 336960 |
| sw01-p2 | Q7 | 255040 |
| sw01-p4 | Q6 | 730560 |
| sw01-p5 | Q6 | 24960 |
| sw01-p5 | Q7 | 633600 |
| sw02-p2 | Q6 | 27520 |
| sw02-p2 | Q7 | 564480 |
| sw02-p4 | Q6 | 583680 |
| sw02-p5 | Q6 | 112640 |
| sw02-p5 | Q7 | 570880 |
| sw03-p4 | Q6 | 652800 |
| sw03-p4 | Q7 | 5760 |
| sw03-p5 | Q6 | 711040 |
| sw04-p4 | Q6 | 10880 |
| sw04-p4 | Q7 | 651520 |
| sw04-p5 | Q6 | 567040 |
| sw05-p4 | Q6 | 691520 |
| sw05-p5 | Q6 | 512640 |
| sw05-p5 | Q7 | 125120 |
| sw06-p4 | Q6 | 550400 |
| sw06-p5 | Q6 | 10880 |
| sw06-p5 | Q7 | 668160 |
| sw07-p4 | Q6 | 529280 |
| sw07-p4 | Q7 | 125120 |
| sw07-p5 | Q6 | 672000 |
| sw08-p2 | Q6 | 502400 |
| sw08-p4 | Q6 | 10880 |
| sw08-p4 | Q7 | 684800 |
| sw08-p5 | Q6 | 545920 |
| sw08-p5 | Q7 | 125120 |

## Opportunistic exclusive window creation (deterministic post-pass)

**4** brand-new *exclusive* window(s) opened, **49920 ns** total, on ports at or below utilisation 0.2 whose TT queue had zero windows before this run. Ported from prob_2_heuristic_enlarged's Step 8.

| port | queue | size (ns) |
|---|---|---|
| sw01-p4 | Q7 | 12480 |
| sw03-p5 | Q7 | 12480 |
| sw05-p4 | Q7 | 12480 |
| sw07-p5 | Q7 | 12480 |

## Best-effort gap equalization (deterministic post-pass)

**8555200 ns** given back from the top-up/creation above so each port's leftover non-TAS gaps land close to equal. Ported from prob_2_heuristic_enlarged's Step 9.

| port | given back (ns) |
|---|---|---|
| sw05-p5 | 541440 |
| sw07-p4 | 541440 |
| sw08-p5 | 541440 |
| sw03-p4 | 476800 |
| sw02-p5 | 443520 |
| sw02-p4 | 432640 |
| sw04-p5 | 432640 |
| sw06-p4 | 432640 |
| sw08-p2 | 432640 |
| sw01-p4 | 400000 |
| sw03-p5 | 400000 |
| sw05-p4 | 400000 |
| sw07-p5 | 400000 |
| S2-p0 | 321600 |
| sw04-p4 | 320640 |
| sw06-p5 | 320640 |
| sw08-p4 | 320640 |
| sw01-p2 | 316480 |
| sw01-p5 | 292480 |
| S3-p0 | 292480 |
| S1-p0 | 252480 |
| sw02-p2 | 242560 |

## Opportunistic overlay window creation (deterministic post-pass)

**44** new overlay window(s), **9399040 ns** total, carved out of already-open best-effort spans on ports at or below utilisation 0.2 -- best-effort stays reachable inside each one (gate mask keeps its BE bits set). Run once after training/finalize_grow_only(), not a trained action.

| port | queue | size (ns) |
|---|---|---|
| S1-p0 | Q6 | 49920 |
| S1-p0 | Q7 | 202560 |
| S2-p0 | Q6 | 109440 |
| S2-p0 | Q7 | 212160 |
| S3-p0 | Q6 | 92800 |
| S3-p0 | Q7 | 199680 |
| sw01-p2 | Q6 | 197440 |
| sw01-p2 | Q7 | 146240 |
| sw01-p4 | Q6 | 226240 |
| sw01-p4 | Q7 | 205760 |
| sw01-p5 | Q6 | 83520 |
| sw01-p5 | Q7 | 225600 |
| sw02-p2 | Q6 | 133120 |
| sw02-p2 | Q7 | 139840 |
| sw02-p4 | Q6 | 249600 |
| sw02-p4 | Q7 | 199680 |
| sw02-p5 | Q6 | 155520 |
| sw02-p5 | Q7 | 304960 |
| sw03-p4 | Q6 | 283840 |
| sw03-p4 | Q7 | 253760 |
| sw03-p5 | Q6 | 237120 |
| sw03-p5 | Q7 | 214400 |
| sw04-p4 | Q6 | 167040 |
| sw04-p4 | Q7 | 230400 |
| sw04-p5 | Q6 | 166400 |
| sw04-p5 | Q7 | 299520 |
| sw05-p4 | Q6 | 237120 |
| sw05-p4 | Q7 | 233920 |
| sw05-p5 | Q6 | 318720 |
| sw05-p5 | Q7 | 272640 |
| sw06-p4 | Q6 | 232960 |
| sw06-p4 | Q7 | 249600 |
| sw06-p5 | Q6 | 183680 |
| sw06-p5 | Q7 | 197120 |
| sw07-p4 | Q6 | 302080 |
| sw07-p4 | Q7 | 272640 |
| sw07-p5 | Q6 | 234240 |
| sw07-p5 | Q7 | 256320 |
| sw08-p2 | Q6 | 232960 |
| sw08-p2 | Q7 | 266240 |
| sw08-p4 | Q6 | 209280 |
| sw08-p4 | Q7 | 154880 |
| sw08-p5 | Q6 | 306240 |
| sw08-p5 | Q7 | 251840 |

## Per-port GCL entries: before (SMT) vs. after (RL-enlarged)

| port | SMT entries | RL-enlarged entries | GCL_size |
|---|---|---|---|
| sw01-p2 | 25 | 27 | 255 |
| sw01-p4 | 1 | 12 | 255 |
| sw01-p5 | 11 | 21 | 255 |
| sw02-p2 | 15 | 28 | 255 |
| sw02-p4 | 9 | 24 | 255 |
| sw02-p5 | 15 | 19 | 255 |
| sw03-p4 | 11 | 22 | 255 |
| sw03-p5 | 1 | 14 | 255 |
| sw04-p4 | 5 | 15 | 255 |
| sw04-p5 | 9 | 21 | 255 |
| sw05-p4 | 1 | 14 | 255 |
| sw05-p5 | 11 | 19 | 255 |
| sw06-p4 | 9 | 21 | 255 |
| sw06-p5 | 5 | 15 | 255 |
| sw07-p4 | 11 | 19 | 255 |
| sw07-p5 | 1 | 13 | 255 |
| sw08-p2 | 9 | 25 | 255 |
| sw08-p4 | 5 | 13 | 255 |
| sw08-p5 | 11 | 20 | 255 |

## Flows

| flow | route | fixed | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|---|
| s0(id=1 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | no | None | None | None | no |
| s1(id=2 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | yes | 6 | 37440 | 83600 | yes |
| s2(id=3 S3->S1) | S3->sw01->sw02->S1 | no | None | None | None | no |
| s3(id=4 S1->S3) | S1->sw02->sw01->S3 | no | None | None | None | no |
| s4(id=5 S1->S3) | S1->sw02->sw01->S3 | yes | 6 | 87360 | 45840 | yes |
| s5(id=6 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | yes | 6 | 0 | 95760 | yes |
| s6(id=7 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |
| s7(id=8 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | no | None | None | None | no |
| s8(id=9 S3->S1) | S3->sw01->sw02->S1 | yes | 6 | 12480 | 45840 | yes |
| s9(id=10 S1->S3) | S1->sw02->sw01->S3 | yes | 7 | 12480 | 45840 | yes |
| s10(id=11 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | no | None | None | None | no |
| s11(id=12 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | yes | 7 | 62400 | 95760 | yes |
| s12(id=13 S3->S1) | S3->sw01->sw02->S1 | yes | 7 | 62400 | 45840 | yes |
| s13(id=14 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |
| s14(id=15 S3->S1) | S3->sw01->sw02->S1 | no | None | None | None | no |
| s15(id=16 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | no | None | None | None | no |
| s16(id=17 S1->S3) | S1->sw02->sw01->S3 | no | None | None | None | no |
| s17(id=18 S3->S1) | S3->sw01->sw02->S1 | yes | 7 | 37440 | 45840 | yes |
| s18(id=19 S1->S3) | S1->sw02->sw01->S3 | yes | 7 | 62400 | 46160 | yes |
| s19(id=20 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | yes | 6 | 37440 | 79120 | yes |

## Per-hop windows (slack_ns > 0 means this window was enlarged)

| flow | egress port | queue | psi (ns) | delta (ns) |
|---|---|---|---|---|
| s1(id=2 S2->S1) | S2-p0 | Q6 | 37440 | 12480 |
| s1(id=2 S2->S1) | sw08-p4 | Q6 | 54400 | 12480 |
| s1(id=2 S2->S1) | sw06-p5 | Q6 | 71040 | 12480 |
| s1(id=2 S2->S1) | sw04-p4 | Q6 | 87680 | 12480 |
| s1(id=2 S2->S1) | sw02-p2 | Q6 | 108480 | 12480 |
| s4(id=5 S1->S3) | S1-p0 | Q6 | 87360 | 12480 |
| s4(id=5 S1->S3) | sw02-p5 | Q6 | 104000 | 12480 |
| s4(id=5 S1->S3) | sw01-p2 | Q6 | 120640 | 12480 |
| s5(id=6 S2->S3) | S2-p0 | Q6 | 0 | 12480 |
| s5(id=6 S2->S3) | sw08-p5 | Q6 | 16640 | 12480 |
| s5(id=6 S2->S3) | sw07-p4 | Q6 | 33280 | 12480 |
| s5(id=6 S2->S3) | sw05-p5 | Q6 | 49920 | 12480 |
| s5(id=6 S2->S3) | sw03-p4 | Q6 | 66560 | 12480 |
| s5(id=6 S2->S3) | sw01-p2 | Q6 | 83200 | 12480 |
| s8(id=9 S3->S1) | S3-p0 | Q6 | 12480 | 12480 |
| s8(id=9 S3->S1) | sw01-p5 | Q6 | 29120 | 12480 |
| s8(id=9 S3->S1) | sw02-p2 | Q6 | 45760 | 12480 |
| s9(id=10 S1->S3) | S1-p0 | Q7 | 12480 | 12480 |
| s9(id=10 S1->S3) | sw02-p5 | Q7 | 29120 | 12480 |
| s9(id=10 S1->S3) | sw01-p2 | Q7 | 45760 | 12480 |
| s11(id=12 S2->S3) | S2-p0 | Q7 | 62400 | 12480 |
| s11(id=12 S2->S3) | sw08-p5 | Q7 | 79040 | 12480 |
| s11(id=12 S2->S3) | sw07-p4 | Q7 | 95680 | 12480 |
| s11(id=12 S2->S3) | sw05-p5 | Q7 | 112320 | 12480 |
| s11(id=12 S2->S3) | sw03-p4 | Q7 | 128960 | 12480 |
| s11(id=12 S2->S3) | sw01-p2 | Q7 | 145600 | 12480 |
| s12(id=13 S3->S1) | S3-p0 | Q7 | 62400 | 12480 |
| s12(id=13 S3->S1) | sw01-p5 | Q7 | 79040 | 12480 |
| s12(id=13 S3->S1) | sw02-p2 | Q7 | 95680 | 12480 |
| s17(id=18 S3->S1) | S3-p0 | Q7 | 37440 | 12480 |
| s17(id=18 S3->S1) | sw01-p5 | Q7 | 54080 | 12480 |
| s17(id=18 S3->S1) | sw02-p2 | Q7 | 70720 | 12480 |
| s18(id=19 S1->S3) | S1-p0 | Q7 | 62400 | 12480 |
| s18(id=19 S1->S3) | sw02-p5 | Q7 | 79360 | 12480 |
| s18(id=19 S1->S3) | sw01-p2 | Q7 | 96000 | 12480 |
| s19(id=20 S1->S2) | S1-p0 | Q6 | 37440 | 12480 |
| s19(id=20 S1->S2) | sw02-p4 | Q6 | 54080 | 12480 |
| s19(id=20 S1->S2) | sw04-p5 | Q6 | 70720 | 12480 |
| s19(id=20 S1->S2) | sw06-p4 | Q6 | 87360 | 12480 |
| s19(id=20 S1->S2) | sw08-p2 | Q6 | 104000 | 12480 |

## Metrics (training/evaluation signal, not the export)

| metric | value |
|---|---|
| trial-placed flow ratio (fixed + trial-admitted) | 0.850 |
| r1  same-queue window adjacency | 0.245 |
| r2  deadline-violation ratio | 0.000 |
| r3  supplier/receiver overlap | 0.997 |
| r4  mean e2e/deadline (admitted) | 0.216 |
| constraint violations | 0 |

## Constraint check

- C1-C7, C9: OK
- seed-integrity (no SMT-fixed flow's placement changed): OK

## GCL per egress port

### sw01-p2  (27 entries, util 18.7200 %)

```
sgs 45760 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 5760 0x3F # 00111111   BE
sgs 35520 0x40 # 01000000   Q6
sgs 46400 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 116160 0x40 # 01000000   Q6
sgs 46400 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 103360 0x80 # 10000000   Q7
sgs 46400 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 70400 0x40 # 01000000   Q6
sgs 46400 0xBF # 10111111   Q7
```

### sw01-p4  (12 entries, util 0.0000 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 32000 0x7F # 01111111   Q6
sgs 200000 0x40 # 01000000   Q6
sgs 55680 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 44480 0x7F # 01111111   Q6
sgs 155520 0x40 # 01000000   Q6
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p5  (21 entries, util 7.8000 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 70720 0x80 # 10000000   Q7
sgs 50240 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 133120 0x80 # 10000000   Q7
sgs 50240 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 95680 0x80 # 10000000   Q7
sgs 50240 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 116480 0x80 # 10000000   Q7
sgs 16960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (28 entries, util 10.9200 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 1280 0x3F # 00111111   BE
sgs 63680 0x80 # 10000000   Q7
sgs 14080 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 152640 0x80 # 10000000   Q7
sgs 14080 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 1280 0x3F # 00111111   BE
sgs 63680 0x80 # 10000000   Q7
sgs 14080 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 119360 0x80 # 10000000   Q7
sgs 47360 0xBF # 10111111   Q7
```

### sw02-p4  (24 entries, util 6.2400 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 79360 0x40 # 01000000   Q6
sgs 16640 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 79360 0x40 # 01000000   Q6
sgs 16640 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 79360 0x40 # 01000000   Q6
sgs 16640 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 62720 0x40 # 01000000   Q6
sgs 33280 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p5  (19 entries, util 10.9200 %)

```
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 37760 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12160 0x3F # 00111111   BE
sgs 36160 0x40 # 01000000   Q6
sgs 59840 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 111040 0x80 # 10000000   Q7
sgs 59840 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 37760 0xBF # 10111111   Q7
sgs 60800 0x80 # 10000000   Q7
sgs 59840 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 81920 0x80 # 10000000   Q7
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (22 entries, util 7.8000 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 21120 0xBF # 10111111   Q7
sgs 28800 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 5760 0x3F # 00111111   BE
sgs 14080 0x40 # 01000000   Q6
sgs 38720 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 94720 0x40 # 01000000   Q6
sgs 38720 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 94720 0x40 # 01000000   Q6
sgs 38720 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 28160 0x40 # 01000000   Q6
sgs 55360 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p5  (14 entries, util 0.0000 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 14080 0xBF # 10111111   Q7
sgs 200000 0x40 # 01000000   Q6
sgs 36160 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 14080 0xBF # 10111111   Q7
sgs 136000 0x40 # 01000000   Q6
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p4  (15 entries, util 3.1200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 37760 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 5440 0x3F # 00111111   BE
sgs 227200 0x80 # 10000000   Q7
sgs 17280 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 37760 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 5440 0x3F # 00111111   BE
sgs 139520 0x80 # 10000000   Q7
sgs 55040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (21 entries, util 6.2400 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 79360 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 79360 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 79360 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 46080 0x40 # 01000000   Q6
sgs 33280 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (14 entries, util 0.0000 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 33600 0xBF # 10111111   Q7
sgs 200000 0x40 # 01000000   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 33600 0xBF # 10111111   Q7
sgs 116480 0x40 # 01000000   Q6
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p5  (19 entries, util 7.8000 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 14720 0x80 # 10000000   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 77120 0x40 # 01000000   Q6
sgs 23040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 77120 0x40 # 01000000   Q6
sgs 23040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 27200 0x40 # 01000000   Q6
sgs 23040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p4  (21 entries, util 6.2400 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 79360 0x40 # 01000000   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 79360 0x40 # 01000000   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 79360 0x40 # 01000000   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 29440 0x40 # 01000000   Q6
sgs 33280 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (15 entries, util 3.1200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 21120 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 5440 0x3F # 00111111   BE
sgs 227200 0x80 # 10000000   Q7
sgs 33920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 21120 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 5440 0x3F # 00111111   BE
sgs 156160 0x80 # 10000000   Q7
sgs 55040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (19 entries, util 7.8000 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 14720 0x80 # 10000000   Q7
sgs 39680 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 77120 0x40 # 01000000   Q6
sgs 39680 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 77120 0x40 # 01000000   Q6
sgs 39680 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 43840 0x40 # 01000000   Q6
sgs 23040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p5  (13 entries, util 0.0000 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 53120 0xBF # 10111111   Q7
sgs 200000 0x40 # 01000000   Q6
sgs 47040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 53120 0xBF # 10111111   Q7
sgs 96960 0x40 # 01000000   Q6
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p2  (25 entries, util 6.2400 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 79360 0x40 # 01000000   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 79360 0x40 # 01000000   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 79360 0x40 # 01000000   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 12800 0x40 # 01000000   Q6
sgs 33280 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p4  (13 entries, util 3.1200 %)

```
sgs 54400 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 5440 0x3F # 00111111   BE
sgs 227200 0x80 # 10000000   Q7
sgs 50560 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 54400 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 5440 0x3F # 00111111   BE
sgs 172800 0x80 # 10000000   Q7
sgs 55040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (20 entries, util 7.8000 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 14720 0x80 # 10000000   Q7
sgs 56320 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 77120 0x40 # 01000000   Q6
sgs 56320 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 77120 0x40 # 01000000   Q6
sgs 56320 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 60480 0x40 # 01000000   Q6
sgs 23040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

