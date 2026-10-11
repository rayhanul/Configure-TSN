# RL-enlarged GCL schedule (Problem 2: window enlargement)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Seeded from SMT run: **result/result-2026-10-10-dataset-testbed-4-saf/smt-c9-on/4-saf-retimed-c9on**

## Admission (unchanged) vs. capacity grown

Problem 2 never admits a flow into the schedule it exports -- it only widens windows. `admitted` below is exactly the SMT baseline, by construction; the capacity growth this run achieved is banked slack and per-port GCL entries, reported separately.

| | admitted | of total |
|---|---|---|
| SMT (fixed, never moved) | 11 | 11 |
| RL-enlarged (exported; grow-only, admits nothing new) | 11 | 20 |

During training, the policy's trial admissions (the reward signal that teaches it how much a window needs to grow) reached **6** of the 9 SMT-rejected flows -- none of those are kept in this export; that capacity stays as empty, banked slack for Problem 3 to fill. Total slack banked: 217600 ns. GCL_size overflow: 0.

## Opportunistic idle top-up (deterministic post-pass)

**9394560 ns**, drawn from idle capacity on ports at or below utilisation 0.2, independent of what training happened to grow. Ported from prob_2_heuristic_enlarged's Step 7.

| port | queue | applied (ns) |
|---|---|---|
| S1-p0 | Q6 | 525120 |
| S1-p0 | Q7 | 112640 |
| S2-p0 | Q6 | 250240 |
| S2-p0 | Q7 | 375040 |
| S3-p0 | Q6 | 662720 |
| sw01-p4 | Q6 | 646400 |
| sw01-p4 | Q7 | 1280 |
| sw02-p2 | Q6 | 3520 |
| sw02-p2 | Q7 | 620480 |
| sw02-p4 | Q6 | 513600 |
| sw02-p4 | Q7 | 113280 |
| sw03-p5 | Q6 | 630400 |
| sw03-p5 | Q7 | 2560 |
| sw04-p4 | Q6 | 3200 |
| sw04-p4 | Q7 | 626880 |
| sw04-p5 | Q6 | 502080 |
| sw04-p5 | Q7 | 113920 |
| sw05-p4 | Q6 | 620160 |
| sw05-p4 | Q7 | 3840 |
| sw06-p4 | Q6 | 490560 |
| sw06-p4 | Q7 | 114560 |
| sw06-p5 | Q6 | 2880 |
| sw06-p5 | Q7 | 635200 |
| sw07-p5 | Q6 | 609920 |
| sw07-p5 | Q7 | 5120 |
| sw08-p2 | Q6 | 562880 |
| sw08-p2 | Q7 | 1920 |
| sw08-p4 | Q6 | 640 |
| sw08-p4 | Q7 | 643520 |

## Best-effort gap equalization (deterministic post-pass)

**5393280 ns** given back from the top-up/creation above so each port's leftover non-TAS gaps land close to equal. Ported from prob_2_heuristic_enlarged's Step 9.

| port | given back (ns) |
|---|---|---|
| sw06-p5 | 505920 |
| sw04-p4 | 504000 |
| sw08-p4 | 504000 |
| sw02-p2 | 502080 |
| S3-p0 | 360960 |
| sw01-p4 | 359040 |
| sw03-p5 | 357760 |
| sw05-p4 | 356480 |
| sw07-p5 | 355200 |
| S2-p0 | 299520 |
| S1-p0 | 286400 |
| sw02-p4 | 278720 |
| sw04-p5 | 271040 |
| sw06-p4 | 263360 |
| sw08-p2 | 188800 |

## Opportunistic overlay window creation (deterministic post-pass)

**29** new overlay window(s), **5482560 ns** total, carved out of already-open best-effort spans on ports at or below utilisation 0.2 -- best-effort stays reachable inside each one (gate mask keeps its BE bits set). Run once after training/finalize_grow_only(), not a trained action.

| port | queue | size (ns) |
|---|---|---|
| S1-p0 | Q6 | 62400 |
| S1-p0 | Q7 | 224000 |
| S2-p0 | Q6 | 99840 |
| S2-p0 | Q7 | 199680 |
| S3-p0 | Q6 | 161280 |
| S3-p0 | Q7 | 199680 |
| sw01-p4 | Q6 | 85440 |
| sw01-p4 | Q7 | 252480 |
| sw02-p2 | Q6 | 243840 |
| sw02-p2 | Q7 | 299200 |
| sw02-p4 | Q7 | 238080 |
| sw03-p5 | Q6 | 95680 |
| sw03-p5 | Q7 | 261120 |
| sw04-p4 | Q6 | 194240 |
| sw04-p4 | Q7 | 343040 |
| sw04-p5 | Q6 | 61440 |
| sw04-p5 | Q7 | 193600 |
| sw05-p4 | Q6 | 128960 |
| sw05-p4 | Q7 | 238080 |
| sw06-p4 | Q6 | 92160 |
| sw06-p4 | Q7 | 172160 |
| sw06-p5 | Q6 | 221760 |
| sw06-p5 | Q7 | 309760 |
| sw07-p5 | Q6 | 162240 |
| sw07-p5 | Q7 | 215040 |
| sw08-p2 | Q6 | 122880 |
| sw08-p2 | Q7 | 80640 |
| sw08-p4 | Q6 | 247680 |
| sw08-p4 | Q7 | 276160 |

## Per-port GCL entries: before (SMT) vs. after (RL-enlarged)

| port | SMT entries | RL-enlarged entries | GCL_size |
|---|---|---|---|
| sw01-p2 | 29 | 19 | 255 |
| sw01-p4 | 17 | 21 | 255 |
| sw02-p2 | 3 | 20 | 255 |
| sw02-p4 | 21 | 13 | 255 |
| sw03-p4 | 29 | 19 | 255 |
| sw03-p5 | 17 | 21 | 255 |
| sw04-p4 | 3 | 19 | 255 |
| sw04-p5 | 21 | 16 | 255 |
| sw05-p4 | 17 | 21 | 255 |
| sw05-p5 | 29 | 19 | 255 |
| sw06-p4 | 21 | 16 | 255 |
| sw06-p5 | 3 | 22 | 255 |
| sw07-p4 | 29 | 19 | 255 |
| sw07-p5 | 17 | 21 | 255 |
| sw08-p2 | 25 | 20 | 255 |
| sw08-p4 | 3 | 24 | 255 |
| sw08-p5 | 29 | 19 | 255 |

## Flows

| flow | route | fixed | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|---|
| s0(id=1 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | yes | 7 | 24960 | 46160 | yes |
| s1(id=2 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | no | None | None | None | no |
| s2(id=3 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | yes | 7 | 24960 | 42000 | yes |
| s3(id=4 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | no | None | None | None | no |
| s4(id=5 S3->S1) | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | no | None | None | None | no |
| s5(id=6 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | yes | 6 | 49920 | 66960 | yes |
| s6(id=7 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |
| s7(id=8 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | yes | 7 | 0 | 54160 | yes |
| s8(id=9 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | yes | 7 | 74880 | 74000 | yes |
| s9(id=10 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | yes | 6 | 49920 | 50960 | yes |
| s10(id=11 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | no | None | None | None | no |
| s11(id=12 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |
| s12(id=13 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | yes | 6 | 0 | 43280 | yes |
| s13(id=14 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | yes | 6 | 0 | 56080 | yes |
| s14(id=15 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | no | None | None | None | no |
| s15(id=16 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | no | None | None | None | no |
| s16(id=17 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | no | None | None | None | no |
| s17(id=18 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | yes | 6 | 74880 | 39440 | yes |
| s18(id=19 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | yes | 6 | 49920 | 54160 | yes |
| s19(id=20 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | yes | 6 | 24960 | 54800 | yes |

## Per-hop windows (slack_ns > 0 means this window was enlarged)

| flow | egress port | queue | psi (ns) | delta (ns) |
|---|---|---|---|---|
| s0(id=1 S3->S2) | S3-p0 | Q7 | 24960 | 12480 |
| s0(id=1 S3->S2) | sw01-p4 | Q7 | 31680 | 12480 |
| s0(id=1 S3->S2) | sw03-p5 | Q7 | 38400 | 12480 |
| s0(id=1 S3->S2) | sw05-p4 | Q7 | 45120 | 12480 |
| s0(id=1 S3->S2) | sw07-p5 | Q7 | 51840 | 12480 |
| s0(id=1 S3->S2) | sw08-p2 | Q7 | 58560 | 12480 |
| s2(id=3 S2->S3) | S2-p0 | Q7 | 24960 | 12480 |
| s2(id=3 S2->S3) | sw08-p5 | Q7 | 30080 | 12480 |
| s2(id=3 S2->S3) | sw07-p4 | Q7 | 35200 | 12480 |
| s2(id=3 S2->S3) | sw05-p5 | Q7 | 40320 | 12480 |
| s2(id=3 S2->S3) | sw03-p4 | Q7 | 46080 | 12480 |
| s2(id=3 S2->S3) | sw01-p2 | Q7 | 54400 | 12480 |
| s5(id=6 S1->S3) | S1-p0 | Q6 | 49920 | 12480 |
| s5(id=6 S1->S3) | sw02-p4 | Q6 | 56640 | 12480 |
| s5(id=6 S1->S3) | sw04-p5 | Q6 | 63360 | 12480 |
| s5(id=6 S1->S3) | sw06-p4 | Q6 | 70080 | 12480 |
| s5(id=6 S1->S3) | sw08-p5 | Q6 | 76800 | 12480 |
| s5(id=6 S1->S3) | sw07-p4 | Q6 | 83520 | 12480 |
| s5(id=6 S1->S3) | sw05-p5 | Q6 | 90240 | 12480 |
| s5(id=6 S1->S3) | sw03-p4 | Q6 | 96960 | 12480 |
| s5(id=6 S1->S3) | sw01-p2 | Q6 | 104320 | 12480 |
| s7(id=8 S2->S3) | S2-p0 | Q7 | 0 | 12480 |
| s7(id=8 S2->S3) | sw08-p5 | Q7 | 8320 | 12480 |
| s7(id=8 S2->S3) | sw07-p4 | Q7 | 16640 | 12480 |
| s7(id=8 S2->S3) | sw05-p5 | Q7 | 24960 | 12480 |
| s7(id=8 S2->S3) | sw03-p4 | Q7 | 33280 | 12480 |
| s7(id=8 S2->S3) | sw01-p2 | Q7 | 41600 | 12480 |
| s8(id=9 S1->S3) | S1-p0 | Q7 | 74880 | 12480 |
| s8(id=9 S1->S3) | sw02-p4 | Q7 | 82560 | 12480 |
| s8(id=9 S1->S3) | sw04-p5 | Q7 | 90240 | 12480 |
| s8(id=9 S1->S3) | sw06-p4 | Q7 | 97920 | 12480 |
| s8(id=9 S1->S3) | sw08-p5 | Q7 | 105600 | 12480 |
| s8(id=9 S1->S3) | sw07-p4 | Q7 | 113280 | 12480 |
| s8(id=9 S1->S3) | sw05-p5 | Q7 | 120960 | 12480 |
| s8(id=9 S1->S3) | sw03-p4 | Q7 | 128640 | 12480 |
| s8(id=9 S1->S3) | sw01-p2 | Q7 | 136320 | 12480 |
| s9(id=10 S3->S2) | S3-p0 | Q6 | 49920 | 12480 |
| s9(id=10 S3->S2) | sw01-p4 | Q6 | 57600 | 12480 |
| s9(id=10 S3->S2) | sw03-p5 | Q6 | 65280 | 12480 |
| s9(id=10 S3->S2) | sw05-p4 | Q6 | 72960 | 12480 |
| s9(id=10 S3->S2) | sw07-p5 | Q6 | 80640 | 12480 |
| s9(id=10 S3->S2) | sw08-p2 | Q6 | 88320 | 12480 |
| s12(id=13 S1->S2) | S1-p0 | Q6 | 0 | 12480 |
| s12(id=13 S1->S2) | sw02-p4 | Q6 | 7680 | 12480 |
| s12(id=13 S1->S2) | sw04-p5 | Q6 | 15360 | 12480 |
| s12(id=13 S1->S2) | sw06-p4 | Q6 | 23040 | 12480 |
| s12(id=13 S1->S2) | sw08-p2 | Q6 | 30720 | 12480 |
| s13(id=14 S3->S2) | S3-p0 | Q6 | 0 | 12480 |
| s13(id=14 S3->S2) | sw01-p4 | Q6 | 8640 | 12480 |
| s13(id=14 S3->S2) | sw03-p5 | Q6 | 16960 | 12480 |
| s13(id=14 S3->S2) | sw05-p4 | Q6 | 25280 | 12480 |
| s13(id=14 S3->S2) | sw07-p5 | Q6 | 33600 | 12480 |
| s13(id=14 S3->S2) | sw08-p2 | Q6 | 43520 | 12480 |
| s17(id=18 S2->S1) | S2-p0 | Q6 | 74880 | 12480 |
| s17(id=18 S2->S1) | sw08-p4 | Q6 | 81600 | 12480 |
| s17(id=18 S2->S1) | sw06-p5 | Q6 | 88320 | 12480 |
| s17(id=18 S2->S1) | sw04-p4 | Q6 | 95040 | 12480 |
| s17(id=18 S2->S1) | sw02-p2 | Q6 | 101760 | 12480 |
| s18(id=19 S2->S3) | S2-p0 | Q6 | 49920 | 12480 |
| s18(id=19 S2->S3) | sw08-p5 | Q6 | 58240 | 12480 |
| s18(id=19 S2->S3) | sw07-p4 | Q6 | 66560 | 12480 |
| s18(id=19 S2->S3) | sw05-p5 | Q6 | 74880 | 12480 |
| s18(id=19 S2->S3) | sw03-p4 | Q6 | 83200 | 12480 |
| s18(id=19 S2->S3) | sw01-p2 | Q6 | 91520 | 12480 |
| s19(id=20 S1->S3) | S1-p0 | Q6 | 24960 | 12480 |
| s19(id=20 S1->S3) | sw02-p4 | Q6 | 30080 | 12480 |
| s19(id=20 S1->S3) | sw04-p5 | Q6 | 35200 | 12480 |
| s19(id=20 S1->S3) | sw06-p4 | Q6 | 40320 | 12480 |
| s19(id=20 S1->S3) | sw08-p5 | Q6 | 45440 | 12480 |
| s19(id=20 S1->S3) | sw07-p4 | Q6 | 50560 | 12480 |
| s19(id=20 S1->S3) | sw05-p5 | Q6 | 55680 | 12480 |
| s19(id=20 S1->S3) | sw03-p4 | Q6 | 62080 | 12480 |
| s19(id=20 S1->S3) | sw01-p2 | Q6 | 67200 | 12480 |

## Metrics (training/evaluation signal, not the export)

| metric | value |
|---|---|
| trial-placed flow ratio (fixed + trial-admitted) | 0.850 |
| r1  same-queue window adjacency | 0.582 |
| r2  deadline-violation ratio | 0.000 |
| r3  supplier/receiver overlap | 1.000 |
| r4  mean e2e/deadline (admitted) | 0.150 |
| constraint violations | 0 |

## Constraint check

- C1-C7, C9: OK
- seed-integrity (no SMT-fixed flow's placement changed): OK

## GCL per egress port

### sw01-p2  (19 entries, util 21.8400 %)

```
sgs 41600 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 49600 0x40 # 01000000   Q6
sgs 1920 0x3F # 00111111   BE
sgs 30080 0x80 # 10000000   Q7
sgs 92800 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 161920 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 36800 0x40 # 01000000   Q6
sgs 137600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 120320 0x3F # 00111111   BE
```

### sw01-p4  (21 entries, util 12.4800 %)

```
sgs 8640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 10560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13440 0xBF # 10111111   Q7
sgs 73280 0x40 # 01000000   Q6
sgs 19200 0x7F # 01111111   Q6
sgs 58560 0xBF # 10111111   Q7
sgs 122240 0x40 # 01000000   Q6
sgs 19200 0x7F # 01111111   Q6
sgs 58560 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 10560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13440 0xBF # 10111111   Q7
sgs 73280 0x40 # 01000000   Q6
sgs 19200 0x7F # 01111111   Q6
sgs 58560 0xBF # 10111111   Q7
sgs 113600 0x40 # 01000000   Q6
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (20 entries, util 1.5600 %)

```
sgs 44480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 44800 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 3520 0x3F # 00111111   BE
sgs 28480 0x80 # 10000000   Q7
sgs 53760 0xBF # 10111111   Q7
sgs 44480 0x7F # 01111111   Q6
sgs 101760 0x80 # 10000000   Q7
sgs 53760 0xBF # 10111111   Q7
sgs 44480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 43200 0xBF # 10111111   Q7
sgs 17600 0x7F # 01111111   Q6
sgs 28480 0x80 # 10000000   Q7
sgs 53760 0xBF # 10111111   Q7
sgs 44480 0x7F # 01111111   Q6
sgs 57280 0x80 # 10000000   Q7
sgs 48320 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p4  (13 entries, util 15.6000 %)

```
sgs 7680 0x3F # 00111111   BE
sgs 34880 0x40 # 01000000   Q6
sgs 14080 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 82240 0x80 # 10000000   Q7
sgs 56000 0xBF # 10111111   Q7
sgs 144000 0x40 # 01000000   Q6
sgs 56000 0xBF # 10111111   Q7
sgs 144000 0x40 # 01000000   Q6
sgs 56000 0xBF # 10111111   Q7
sgs 136320 0x40 # 01000000   Q6
sgs 56000 0xBF # 10111111   Q7
```

### sw03-p4  (19 entries, util 21.8400 %)

```
sgs 33280 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 3520 0x3F # 00111111   BE
sgs 47360 0x40 # 01000000   Q6
sgs 2240 0x3F # 00111111   BE
sgs 29440 0x80 # 10000000   Q7
sgs 92160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 16320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 158720 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 3520 0x3F # 00111111   BE
sgs 33600 0x40 # 01000000   Q6
sgs 137600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 16320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 125440 0x3F # 00111111   BE
```

### sw03-p5  (21 entries, util 12.4800 %)

```
sgs 16960 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 8960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 14400 0xBF # 10111111   Q7
sgs 73920 0x40 # 01000000   Q6
sgs 60800 0xBF # 10111111   Q7
sgs 16960 0x7F # 01111111   Q6
sgs 122240 0x40 # 01000000   Q6
sgs 60800 0xBF # 10111111   Q7
sgs 16960 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 8960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 14400 0xBF # 10111111   Q7
sgs 73920 0x40 # 01000000   Q6
sgs 60800 0xBF # 10111111   Q7
sgs 16960 0x7F # 01111111   Q6
sgs 105280 0x40 # 01000000   Q6
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p4  (19 entries, util 1.5600 %)

```
sgs 36480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 46080 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 3200 0x3F # 00111111   BE
sgs 27520 0x80 # 10000000   Q7
sgs 61760 0xBF # 10111111   Q7
sgs 36480 0x7F # 01111111   Q6
sgs 101760 0x80 # 10000000   Q7
sgs 61760 0xBF # 10111111   Q7
sgs 36480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 61760 0xBF # 10111111   Q7
sgs 27520 0x80 # 10000000   Q7
sgs 61760 0xBF # 10111111   Q7
sgs 36480 0x7F # 01111111   Q6
sgs 65280 0x80 # 10000000   Q7
sgs 48320 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (16 entries, util 15.6000 %)

```
sgs 15360 0x7F # 01111111   Q6
sgs 32320 0x40 # 01000000   Q6
sgs 15680 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 640 0x3F # 00111111   BE
sgs 82880 0x80 # 10000000   Q7
sgs 40640 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 144000 0x40 # 01000000   Q6
sgs 40640 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 144000 0x40 # 01000000   Q6
sgs 40640 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 128640 0x40 # 01000000   Q6
sgs 56000 0xBF # 10111111   Q7
```

### sw05-p4  (21 entries, util 12.4800 %)

```
sgs 25280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 7360 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 15360 0xBF # 10111111   Q7
sgs 74560 0x40 # 01000000   Q6
sgs 52480 0xBF # 10111111   Q7
sgs 25280 0x7F # 01111111   Q6
sgs 122240 0x40 # 01000000   Q6
sgs 52480 0xBF # 10111111   Q7
sgs 25280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 7360 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 15360 0xBF # 10111111   Q7
sgs 74560 0x40 # 01000000   Q6
sgs 52480 0xBF # 10111111   Q7
sgs 25280 0x7F # 01111111   Q6
sgs 96960 0x40 # 01000000   Q6
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p5  (19 entries, util 21.8400 %)

```
sgs 24960 0x3F # 00111111   BE
sgs 27840 0x80 # 10000000   Q7
sgs 2880 0x3F # 00111111   BE
sgs 47040 0x40 # 01000000   Q6
sgs 1920 0x3F # 00111111   BE
sgs 28800 0x80 # 10000000   Q7
sgs 91520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 18240 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 156800 0x3F # 00111111   BE
sgs 27840 0x80 # 10000000   Q7
sgs 2880 0x3F # 00111111   BE
sgs 31680 0x40 # 01000000   Q6
sgs 137600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 18240 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 131840 0x3F # 00111111   BE
```

### sw06-p4  (16 entries, util 15.6000 %)

```
sgs 23040 0x7F # 01111111   Q6
sgs 29760 0x40 # 01000000   Q6
sgs 17280 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 960 0x3F # 00111111   BE
sgs 83520 0x80 # 10000000   Q7
sgs 32960 0xBF # 10111111   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 144000 0x40 # 01000000   Q6
sgs 32960 0xBF # 10111111   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 144000 0x40 # 01000000   Q6
sgs 32960 0xBF # 10111111   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 120960 0x40 # 01000000   Q6
sgs 56000 0xBF # 10111111   Q7
```

### sw06-p5  (22 entries, util 1.5600 %)

```
sgs 28480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 47360 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 2880 0x3F # 00111111   BE
sgs 26560 0x80 # 10000000   Q7
sgs 19840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 28480 0x7F # 01111111   Q6
sgs 101760 0x80 # 10000000   Q7
sgs 19840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 28480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 62720 0xBF # 10111111   Q7
sgs 26560 0x80 # 10000000   Q7
sgs 19840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 28480 0x7F # 01111111   Q6
sgs 73280 0x80 # 10000000   Q7
sgs 48320 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (19 entries, util 21.8400 %)

```
sgs 16640 0x3F # 00111111   BE
sgs 31040 0x80 # 10000000   Q7
sgs 2880 0x3F # 00111111   BE
sgs 45440 0x40 # 01000000   Q6
sgs 1600 0x3F # 00111111   BE
sgs 28160 0x80 # 10000000   Q7
sgs 90880 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 21440 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 153600 0x3F # 00111111   BE
sgs 31040 0x80 # 10000000   Q7
sgs 2880 0x3F # 00111111   BE
sgs 28480 0x40 # 01000000   Q6
sgs 137600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 21440 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 136960 0x3F # 00111111   BE
```

### sw07-p5  (21 entries, util 12.4800 %)

```
sgs 33600 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 16320 0xBF # 10111111   Q7
sgs 75200 0x40 # 01000000   Q6
sgs 44160 0xBF # 10111111   Q7
sgs 33600 0x7F # 01111111   Q6
sgs 122240 0x40 # 01000000   Q6
sgs 44160 0xBF # 10111111   Q7
sgs 33600 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 16320 0xBF # 10111111   Q7
sgs 75200 0x40 # 01000000   Q6
sgs 44160 0xBF # 10111111   Q7
sgs 33600 0x7F # 01111111   Q6
sgs 88640 0x40 # 01000000   Q6
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p2  (20 entries, util 18.7200 %)

```
sgs 30720 0x7F # 01111111   Q6
sgs 25280 0x40 # 01000000   Q6
sgs 2560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 960 0x3F # 00111111   BE
sgs 115520 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 156800 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 25280 0x40 # 01000000   Q6
sgs 2560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 960 0x3F # 00111111   BE
sgs 115520 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 126080 0x40 # 01000000   Q6
sgs 43200 0xBF # 10111111   Q7
```

### sw08-p4  (24 entries, util 1.5600 %)

```
sgs 20480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 16960 0x7F # 01111111   Q6
sgs 31680 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 640 0x3F # 00111111   BE
sgs 27520 0x80 # 10000000   Q7
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 101760 0x80 # 10000000   Q7
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 16960 0x7F # 01111111   Q6
sgs 44800 0xBF # 10111111   Q7
sgs 27520 0x80 # 10000000   Q7
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 81280 0x80 # 10000000   Q7
sgs 48320 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (19 entries, util 21.8400 %)

```
sgs 8320 0x3F # 00111111   BE
sgs 34240 0x80 # 10000000   Q7
sgs 2880 0x3F # 00111111   BE
sgs 43840 0x40 # 01000000   Q6
sgs 1280 0x3F # 00111111   BE
sgs 27520 0x80 # 10000000   Q7
sgs 90240 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 24640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 150400 0x3F # 00111111   BE
sgs 34240 0x80 # 10000000   Q7
sgs 2880 0x3F # 00111111   BE
sgs 25280 0x40 # 01000000   Q6
sgs 137600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 24640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 142080 0x3F # 00111111   BE
```

