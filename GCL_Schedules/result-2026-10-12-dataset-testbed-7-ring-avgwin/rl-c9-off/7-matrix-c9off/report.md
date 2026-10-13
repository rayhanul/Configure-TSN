# RL-enlarged GCL schedule (Problem 2: window enlargement)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Seeded from SMT run: **result/result-2026-10-12-dataset-testbed-7-ring-avgwin/smt-c9-off/7-t3600-c9off-minlat**

## Admission (unchanged) vs. capacity grown

Problem 2 never admits a flow into the schedule it exports -- it only widens windows. `admitted` below is exactly the SMT baseline, by construction; the capacity growth this run achieved is banked slack and per-port GCL entries, reported separately.

| | admitted | of total |
|---|---|---|
| SMT (fixed, never moved) | 11 | 20 |
| RL-enlarged (exported; grow-only, admits nothing new) | 11 | 20 |

During training, the policy's trial admissions (the reward signal that teaches it how much a window needs to grow) reached **7** of the 9 SMT-rejected flows -- none of those are kept in this export; that capacity stays as empty, banked slack for Problem 3 to fill. Total slack banked: 165120 ns. GCL_size overflow: 0.

## Opportunistic idle top-up (deterministic post-pass)

**13772800 ns**, drawn from idle capacity on ports at or below utilisation 0.2, independent of what training happened to grow. Ported from prob_2_heuristic_enlarged's Step 7.

| port | queue | applied (ns) |
|---|---|---|
| S1-p0 | Q6 | 350080 |
| S1-p0 | Q7 | 225280 |
| S2-p0 | Q6 | 375040 |
| S2-p0 | Q7 | 350080 |
| S3-p0 | Q6 | 550400 |
| S3-p0 | Q7 | 49920 |
| sw01-p2 | Q6 | 570560 |
| sw01-p2 | Q7 | 8960 |
| sw01-p4 | Q6 | 456320 |
| sw01-p4 | Q7 | 227200 |
| sw01-p5 | Q6 | 36480 |
| sw01-p5 | Q7 | 622080 |
| sw02-p2 | Q6 | 23680 |
| sw02-p2 | Q7 | 605760 |
| sw02-p4 | Q6 | 49920 |
| sw02-p4 | Q7 | 583680 |
| sw02-p5 | Q6 | 648320 |
| sw02-p5 | Q7 | 12480 |
| sw03-p4 | Q6 | 568320 |
| sw03-p4 | Q7 | 58560 |
| sw03-p5 | Q6 | 439680 |
| sw03-p5 | Q7 | 227200 |
| sw04-p4 | Q7 | 712640 |
| sw04-p5 | Q6 | 49920 |
| sw04-p5 | Q7 | 567040 |
| sw05-p4 | Q6 | 423040 |
| sw05-p4 | Q7 | 227200 |
| sw05-p5 | Q6 | 596480 |
| sw05-p5 | Q7 | 54720 |
| sw06-p4 | Q6 | 49920 |
| sw06-p4 | Q7 | 550400 |
| sw06-p5 | Q7 | 729280 |
| sw07-p4 | Q6 | 624640 |
| sw07-p4 | Q7 | 47040 |
| sw07-p5 | Q6 | 406400 |
| sw07-p5 | Q7 | 227200 |
| sw08-p4 | Q7 | 745920 |
| sw08-p5 | Q6 | 344000 |
| sw08-p5 | Q7 | 376960 |

## Opportunistic exclusive window creation (deterministic post-pass)

**3** brand-new *exclusive* window(s) opened, **37440 ns** total, on ports at or below utilisation 0.2 whose TT queue had zero windows before this run. Ported from prob_2_heuristic_enlarged's Step 8.

| port | queue | size (ns) |
|---|---|---|
| sw04-p4 | Q6 | 12480 |
| sw06-p5 | Q6 | 12480 |
| sw08-p4 | Q6 | 12480 |

## Best-effort gap equalization (deterministic post-pass)

**7560320 ns** given back from the top-up/creation above so each port's leftover non-TAS gaps land close to equal. Ported from prob_2_heuristic_enlarged's Step 9.

| port | given back (ns) |
|---|---|---|
| sw01-p4 | 550400 |
| sw03-p5 | 550400 |
| sw05-p4 | 550400 |
| sw07-p5 | 539520 |
| sw02-p5 | 473600 |
| sw03-p4 | 424960 |
| sw05-p5 | 413440 |
| sw07-p4 | 401920 |
| sw01-p5 | 364800 |
| sw02-p2 | 328000 |
| sw01-p2 | 321600 |
| sw06-p4 | 303360 |
| sw02-p4 | 299520 |
| sw04-p5 | 299520 |
| sw08-p5 | 289600 |
| sw04-p4 | 262400 |
| sw06-p5 | 262400 |
| sw08-p4 | 262400 |
| S2-p0 | 254080 |
| S1-p0 | 205760 |
| S3-p0 | 202240 |

## Opportunistic overlay window creation (deterministic post-pass)

**42** new overlay window(s), **8378560 ns** total, carved out of already-open best-effort spans on ports at or below utilisation 0.2 -- best-effort stays reachable inside each one (gate mask keeps its BE bits set). Run once after training/finalize_grow_only(), not a trained action.

| port | queue | size (ns) |
|---|---|---|
| S1-p0 | Q6 | 49920 |
| S1-p0 | Q7 | 155840 |
| S2-p0 | Q6 | 99840 |
| S2-p0 | Q7 | 154240 |
| S3-p0 | Q6 | 49920 |
| S3-p0 | Q7 | 152320 |
| sw01-p2 | Q6 | 181440 |
| sw01-p2 | Q7 | 209280 |
| sw01-p4 | Q6 | 300160 |
| sw01-p4 | Q7 | 291840 |
| sw01-p5 | Q6 | 121600 |
| sw01-p5 | Q7 | 249600 |
| sw02-p2 | Q6 | 146240 |
| sw02-p2 | Q7 | 204160 |
| sw02-p4 | Q6 | 128960 |
| sw02-p4 | Q7 | 187200 |
| sw02-p5 | Q6 | 262080 |
| sw02-p5 | Q7 | 271680 |
| sw03-p4 | Q6 | 261120 |
| sw03-p4 | Q7 | 230400 |
| sw03-p5 | Q6 | 353920 |
| sw03-p5 | Q7 | 254720 |
| sw04-p4 | Q6 | 149760 |
| sw04-p4 | Q7 | 175040 |
| sw04-p5 | Q6 | 158080 |
| sw04-p5 | Q7 | 174720 |
| sw05-p4 | Q6 | 353920 |
| sw05-p4 | Q7 | 271360 |
| sw05-p5 | Q6 | 232960 |
| sw05-p5 | Q7 | 230400 |
| sw06-p4 | Q6 | 212160 |
| sw06-p4 | Q7 | 132480 |
| sw06-p5 | Q6 | 158080 |
| sw06-p5 | Q7 | 150080 |
| sw07-p4 | Q6 | 166400 |
| sw07-p4 | Q7 | 268800 |
| sw07-p5 | Q6 | 337920 |
| sw07-p5 | Q7 | 293120 |
| sw08-p4 | Q6 | 141440 |
| sw08-p4 | Q7 | 150080 |
| sw08-p5 | Q6 | 163840 |
| sw08-p5 | Q7 | 141440 |

## Per-port GCL entries: before (SMT) vs. after (RL-enlarged)

| port | SMT entries | RL-enlarged entries | GCL_size |
|---|---|---|---|
| sw01-p2 | 5 | 28 | 255 |
| sw01-p4 | 9 | 22 | 255 |
| sw01-p5 | 17 | 27 | 255 |
| sw02-p2 | 19 | 26 | 255 |
| sw02-p4 | 25 | 28 | 255 |
| sw02-p5 | 1 | 22 | 255 |
| sw03-p4 | 5 | 17 | 255 |
| sw03-p5 | 9 | 19 | 255 |
| sw04-p4 | 3 | 10 | 255 |
| sw04-p5 | 25 | 28 | 255 |
| sw05-p4 | 9 | 23 | 255 |
| sw05-p5 | 5 | 15 | 255 |
| sw06-p4 | 25 | 23 | 255 |
| sw06-p5 | 3 | 9 | 255 |
| sw07-p4 | 5 | 14 | 255 |
| sw07-p5 | 9 | 23 | 255 |
| sw08-p2 | 33 | 31 | 255 |
| sw08-p4 | 3 | 9 | 255 |
| sw08-p5 | 5 | 16 | 255 |

## Flows

| flow | route | fixed | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|---|
| s0(id=1 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | yes | 6 | 0 | 79120 | yes |
| s1(id=2 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | no | None | None | None | no |
| s2(id=3 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | yes | 7 | 0 | 95760 | yes |
| s3(id=4 S1->S3) | S1->sw02->sw01->S3 | no | None | None | None | no |
| s4(id=5 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | yes | 7 | 74880 | 79120 | yes |
| s5(id=6 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | no | None | None | None | no |
| s6(id=7 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | yes | 7 | 24960 | 83600 | yes |
| s7(id=8 S3->S1) | S3->sw01->sw02->S1 | yes | 6 | 49920 | 45840 | yes |
| s8(id=9 S3->S1) | S3->sw01->sw02->S1 | yes | 7 | 0 | 45840 | yes |
| s9(id=10 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | no | None | None | None | no |
| s10(id=11 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |
| s11(id=12 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | yes | 7 | 24960 | 79120 | yes |
| s12(id=13 S1->S3) | S1->sw02->sw01->S3 | no | None | None | None | no |
| s13(id=14 S3->S1) | S3->sw01->sw02->S1 | no | None | None | None | no |
| s14(id=15 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | yes | 7 | 49920 | 83600 | yes |
| s15(id=16 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |
| s16(id=17 S1->S3) | S1->sw02->sw01->S3 | no | None | None | None | no |
| s17(id=18 S3->S1) | S3->sw01->sw02->S1 | yes | 6 | 74880 | 46480 | yes |
| s18(id=19 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | yes | 7 | 99840 | 79120 | yes |
| s19(id=20 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | yes | 6 | 24960 | 95760 | yes |

## Per-hop windows (slack_ns > 0 means this window was enlarged)

| flow | egress port | queue | psi (ns) | delta (ns) |
|---|---|---|---|---|
| s0(id=1 S1->S2) | S1-p0 | Q6 | 0 | 12480 |
| s0(id=1 S1->S2) | sw02-p4 | Q6 | 16640 | 12480 |
| s0(id=1 S1->S2) | sw04-p5 | Q6 | 33280 | 12480 |
| s0(id=1 S1->S2) | sw06-p4 | Q6 | 49920 | 12480 |
| s0(id=1 S1->S2) | sw08-p2 | Q6 | 66560 | 12480 |
| s2(id=3 S2->S3) | S2-p0 | Q7 | 0 | 12480 |
| s2(id=3 S2->S3) | sw08-p5 | Q7 | 16640 | 12480 |
| s2(id=3 S2->S3) | sw07-p4 | Q7 | 33280 | 12480 |
| s2(id=3 S2->S3) | sw05-p5 | Q7 | 49920 | 12480 |
| s2(id=3 S2->S3) | sw03-p4 | Q7 | 66560 | 12480 |
| s2(id=3 S2->S3) | sw01-p2 | Q7 | 83200 | 12480 |
| s4(id=5 S1->S2) | S1-p0 | Q7 | 74880 | 12480 |
| s4(id=5 S1->S2) | sw02-p4 | Q7 | 91520 | 12480 |
| s4(id=5 S1->S2) | sw04-p5 | Q7 | 108160 | 12480 |
| s4(id=5 S1->S2) | sw06-p4 | Q7 | 124800 | 12480 |
| s4(id=5 S1->S2) | sw08-p2 | Q7 | 141440 | 12480 |
| s6(id=7 S2->S1) | S2-p0 | Q7 | 24960 | 12480 |
| s6(id=7 S2->S1) | sw08-p4 | Q7 | 41600 | 12480 |
| s6(id=7 S2->S1) | sw06-p5 | Q7 | 58240 | 12480 |
| s6(id=7 S2->S1) | sw04-p4 | Q7 | 74880 | 12480 |
| s6(id=7 S2->S1) | sw02-p2 | Q7 | 96000 | 12480 |
| s7(id=8 S3->S1) | S3-p0 | Q6 | 49920 | 12480 |
| s7(id=8 S3->S1) | sw01-p5 | Q6 | 66560 | 12480 |
| s7(id=8 S3->S1) | sw02-p2 | Q6 | 83200 | 12480 |
| s8(id=9 S3->S1) | S3-p0 | Q7 | 0 | 12480 |
| s8(id=9 S3->S1) | sw01-p5 | Q7 | 16640 | 12480 |
| s8(id=9 S3->S1) | sw02-p2 | Q7 | 33280 | 12480 |
| s11(id=12 S1->S2) | S1-p0 | Q7 | 24960 | 12480 |
| s11(id=12 S1->S2) | sw02-p4 | Q7 | 41600 | 12480 |
| s11(id=12 S1->S2) | sw04-p5 | Q7 | 58240 | 12480 |
| s11(id=12 S1->S2) | sw06-p4 | Q7 | 74880 | 12480 |
| s11(id=12 S1->S2) | sw08-p2 | Q7 | 91520 | 12480 |
| s14(id=15 S1->S2) | S1-p0 | Q7 | 49920 | 12480 |
| s14(id=15 S1->S2) | sw02-p4 | Q7 | 66560 | 12480 |
| s14(id=15 S1->S2) | sw04-p5 | Q7 | 83200 | 12480 |
| s14(id=15 S1->S2) | sw06-p4 | Q7 | 103680 | 12480 |
| s14(id=15 S1->S2) | sw08-p2 | Q7 | 120960 | 12480 |
| s17(id=18 S3->S1) | S3-p0 | Q6 | 74880 | 12480 |
| s17(id=18 S3->S1) | sw01-p5 | Q6 | 92160 | 12480 |
| s17(id=18 S3->S1) | sw02-p2 | Q6 | 108800 | 12480 |
| s18(id=19 S1->S2) | S1-p0 | Q7 | 99840 | 12480 |
| s18(id=19 S1->S2) | sw02-p4 | Q7 | 116480 | 12480 |
| s18(id=19 S1->S2) | sw04-p5 | Q7 | 133120 | 12480 |
| s18(id=19 S1->S2) | sw06-p4 | Q7 | 149760 | 12480 |
| s18(id=19 S1->S2) | sw08-p2 | Q7 | 166400 | 12480 |
| s19(id=20 S3->S2) | S3-p0 | Q6 | 24960 | 12480 |
| s19(id=20 S3->S2) | sw01-p4 | Q6 | 41600 | 12480 |
| s19(id=20 S3->S2) | sw03-p5 | Q6 | 58240 | 12480 |
| s19(id=20 S3->S2) | sw05-p4 | Q6 | 74880 | 12480 |
| s19(id=20 S3->S2) | sw07-p5 | Q6 | 91520 | 12480 |
| s19(id=20 S3->S2) | sw08-p2 | Q6 | 108160 | 12480 |

## Metrics (training/evaluation signal, not the export)

| metric | value |
|---|---|
| trial-placed flow ratio (fixed + trial-admitted) | 0.900 |
| r1  same-queue window adjacency | 0.304 |
| r2  deadline-violation ratio | 0.000 |
| r3  supplier/receiver overlap | 0.991 |
| r4  mean e2e/deadline (admitted) | 0.228 |
| constraint violations | 0 |

## Constraint check

- C1-C7, C9: OK
- seed-integrity (no SMT-fixed flow's placement changed): OK

## GCL per egress port

### sw01-p2  (28 entries, util 3.1200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 960 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 4800 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 6720 0x3F # 00111111   BE
sgs 72960 0x40 # 01000000   Q6
sgs 17920 0x7F # 01111111   Q6
sgs 46400 0xBF # 10111111   Q7
sgs 122560 0x40 # 01000000   Q6
sgs 31040 0x7F # 01111111   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 50240 0x7F # 01111111   Q6
sgs 72960 0x40 # 01000000   Q6
sgs 17920 0x7F # 01111111   Q6
sgs 46400 0xBF # 10111111   Q7
sgs 39360 0x40 # 01000000   Q6
sgs 14400 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p4  (22 entries, util 6.2400 %)

```
sgs 41600 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 46080 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 19200 0x80 # 10000000   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 93120 0x40 # 01000000   Q6
sgs 15360 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 46080 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 19200 0x80 # 10000000   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 51520 0x40 # 01000000   Q6
sgs 56960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p5  (27 entries, util 12.4800 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 13120 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 5120 0x3F # 00111111   BE
sgs 43520 0x80 # 10000000   Q7
sgs 46720 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 136640 0x80 # 10000000   Q7
sgs 46720 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 13120 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 5120 0x3F # 00111111   BE
sgs 43520 0x80 # 10000000   Q7
sgs 46720 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 120000 0x80 # 10000000   Q7
sgs 13440 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (26 entries, util 14.0400 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 5120 0x3F # 00111111   BE
sgs 49600 0x80 # 10000000   Q7
sgs 24000 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 142720 0x80 # 10000000   Q7
sgs 24000 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 13120 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 5120 0x3F # 00111111   BE
sgs 49600 0x80 # 10000000   Q7
sgs 24000 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 109440 0x80 # 10000000   Q7
sgs 57280 0xBF # 10111111   Q7
```

### sw02-p4  (28 entries, util 18.7200 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 50240 0x80 # 10000000   Q7
sgs 33280 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 125120 0x80 # 10000000   Q7
sgs 33280 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 100160 0x80 # 10000000   Q7
sgs 33280 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 108480 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p5  (22 entries, util 0.0000 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 14400 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 44160 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 14400 0xBF # 10111111   Q7
sgs 85760 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 14400 0xBF # 10111111   Q7
sgs 85760 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 14400 0xBF # 10111111   Q7
sgs 21440 0x40 # 01000000   Q6
sgs 14400 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (17 entries, util 3.1200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 21120 0xBF # 10111111   Q7
sgs 36480 0x7F # 01111111   Q6
sgs 175040 0x40 # 01000000   Q6
sgs 38400 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 21120 0xBF # 10111111   Q7
sgs 36480 0x7F # 01111111   Q6
sgs 108480 0x40 # 01000000   Q6
sgs 55040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p5  (19 entries, util 6.2400 %)

```
sgs 58240 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 29440 0xBF # 10111111   Q7
sgs 32000 0x7F # 01111111   Q6
sgs 19200 0x80 # 10000000   Q7
sgs 48640 0xBF # 10111111   Q7
sgs 58240 0x7F # 01111111   Q6
sgs 93120 0x40 # 01000000   Q6
sgs 48640 0xBF # 10111111   Q7
sgs 58240 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 29440 0xBF # 10111111   Q7
sgs 32000 0x7F # 01111111   Q6
sgs 19200 0x80 # 10000000   Q7
sgs 48640 0xBF # 10111111   Q7
sgs 58240 0x7F # 01111111   Q6
sgs 34880 0x40 # 01000000   Q6
sgs 56960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p4  (10 entries, util 1.5600 %)

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

### sw04-p5  (28 entries, util 18.7200 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 50240 0x80 # 10000000   Q7
sgs 16640 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 125120 0x80 # 10000000   Q7
sgs 16640 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 100160 0x80 # 10000000   Q7
sgs 16640 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 91840 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (23 entries, util 6.2400 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12800 0xBF # 10111111   Q7
sgs 48640 0x7F # 01111111   Q6
sgs 19200 0x80 # 10000000   Q7
sgs 32000 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 93120 0x40 # 01000000   Q6
sgs 32000 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12800 0xBF # 10111111   Q7
sgs 48640 0x7F # 01111111   Q6
sgs 19200 0x80 # 10000000   Q7
sgs 32000 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 18240 0x40 # 01000000   Q6
sgs 56960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p5  (15 entries, util 3.1200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 37760 0xBF # 10111111   Q7
sgs 14080 0x7F # 01111111   Q6
sgs 180800 0x40 # 01000000   Q6
sgs 55040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 37760 0xBF # 10111111   Q7
sgs 14080 0x7F # 01111111   Q6
sgs 130880 0x40 # 01000000   Q6
sgs 55040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p4  (23 entries, util 18.7200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 16320 0xBF # 10111111   Q7
sgs 33600 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 50240 0x80 # 10000000   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 125120 0x80 # 10000000   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 16320 0xBF # 10111111   Q7
sgs 96320 0x80 # 10000000   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 75200 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (9 entries, util 1.5600 %)

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

### sw07-p4  (14 entries, util 3.1200 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 46080 0xBF # 10111111   Q7
sgs 186560 0x40 # 01000000   Q6
sgs 21760 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 46080 0xBF # 10111111   Q7
sgs 153280 0x40 # 01000000   Q6
sgs 55040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p5  (23 entries, util 6.2400 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 46080 0x7F # 01111111   Q6
sgs 15360 0xBF # 10111111   Q7
sgs 19200 0x80 # 10000000   Q7
sgs 15360 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 93120 0x40 # 01000000   Q6
sgs 15360 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 46080 0x7F # 01111111   Q6
sgs 15360 0xBF # 10111111   Q7
sgs 19200 0x80 # 10000000   Q7
sgs 15360 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 46080 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p2  (31 entries, util 24.9600 %)

```
sgs 66560 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 32960 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 28160 0x80 # 10000000   Q7
sgs 72000 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 145920 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 73600 0x80 # 10000000   Q7
sgs 72000 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 79360 0x3F # 00111111   BE
```

### sw08-p4  (9 entries, util 1.5600 %)

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

### sw08-p5  (16 entries, util 3.1200 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 960 0x3F # 00111111   BE
sgs 229760 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 226560 0x40 # 01000000   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

