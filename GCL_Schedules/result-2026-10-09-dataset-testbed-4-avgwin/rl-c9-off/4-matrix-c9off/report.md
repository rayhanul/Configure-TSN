# RL-enlarged GCL schedule (Problem 2: window enlargement)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Seeded from SMT run: **result/result-2026-10-09-dataset-testbed-4-avgwin/smt-c9-off/4-t3600-c9off-minlat**

## Admission (unchanged) vs. capacity grown

Problem 2 never admits a flow into the schedule it exports -- it only widens windows. `admitted` below is exactly the SMT baseline, by construction; the capacity growth this run achieved is banked slack and per-port GCL entries, reported separately.

| | admitted | of total |
|---|---|---|
| SMT (fixed, never moved) | 11 | 20 |
| RL-enlarged (exported; grow-only, admits nothing new) | 11 | 20 |

During training, the policy's trial admissions (the reward signal that teaches it how much a window needs to grow) reached **7** of the 9 SMT-rejected flows -- none of those are kept in this export; that capacity stays as empty, banked slack for Problem 3 to fill. Total slack banked: 348160 ns. GCL_size overflow: 0.

## Opportunistic idle top-up (deterministic post-pass)

**8981120 ns**, drawn from idle capacity on ports at or below utilisation 0.2, independent of what training happened to grow. Ported from prob_2_heuristic_enlarged's Step 7.

| port | queue | applied (ns) |
|---|---|---|
| S1-p0 | Q6 | 487680 |
| S1-p0 | Q7 | 150080 |
| S2-p0 | Q6 | 112640 |
| S2-p0 | Q7 | 487680 |
| S3-p0 | Q6 | 525120 |
| S3-p0 | Q7 | 137600 |
| sw01-p4 | Q6 | 506560 |
| sw01-p4 | Q7 | 139520 |
| sw02-p2 | Q6 | 192000 |
| sw02-p2 | Q7 | 375040 |
| sw02-p4 | Q6 | 438080 |
| sw02-p4 | Q7 | 183040 |
| sw03-p5 | Q6 | 488000 |
| sw03-p5 | Q7 | 141440 |
| sw04-p4 | Q6 | 192000 |
| sw04-p4 | Q7 | 391680 |
| sw04-p5 | Q6 | 439680 |
| sw04-p5 | Q7 | 119680 |
| sw05-p4 | Q6 | 469440 |
| sw05-p4 | Q7 | 143360 |
| sw06-p4 | Q6 | 423040 |
| sw06-p4 | Q7 | 117760 |
| sw06-p5 | Q6 | 192000 |
| sw06-p5 | Q7 | 408320 |
| sw07-p5 | Q6 | 447040 |
| sw07-p5 | Q7 | 149120 |
| sw08-p2 | Q6 | 390720 |
| sw08-p2 | Q7 | 115840 |
| sw08-p4 | Q6 | 192000 |
| sw08-p4 | Q7 | 424960 |

## Best-effort gap equalization (deterministic post-pass)

**5247680 ns** given back from the top-up/creation above so each port's leftover non-TAS gaps land close to equal. Ported from prob_2_heuristic_enlarged's Step 9.

| port | given back (ns) |
|---|---|---|
| sw04-p4 | 561920 |
| sw06-p5 | 561920 |
| sw08-p4 | 561920 |
| sw02-p2 | 558080 |
| sw04-p5 | 345600 |
| sw06-p4 | 345600 |
| sw02-p4 | 287360 |
| sw08-p2 | 286720 |
| sw07-p5 | 269440 |
| sw05-p4 | 263680 |
| sw03-p5 | 261760 |
| sw01-p4 | 259840 |
| S3-p0 | 257920 |
| S1-p0 | 241920 |
| S2-p0 | 184000 |

## Opportunistic overlay window creation (deterministic post-pass)

**29** new overlay window(s), **5734080 ns** total, carved out of already-open best-effort spans on ports at or below utilisation 0.2 -- best-effort stays reachable inside each one (gate mask keeps its BE bits set). Run once after training/finalize_grow_only(), not a trained action.

| port | queue | size (ns) |
|---|---|---|
| S1-p0 | Q6 | 49920 |
| S1-p0 | Q7 | 192000 |
| S2-p0 | Q7 | 184000 |
| S3-p0 | Q6 | 24960 |
| S3-p0 | Q7 | 232960 |
| sw01-p4 | Q6 | 91520 |
| sw01-p4 | Q7 | 183040 |
| sw02-p2 | Q6 | 366720 |
| sw02-p2 | Q7 | 270400 |
| sw02-p4 | Q6 | 143360 |
| sw02-p4 | Q7 | 160640 |
| sw03-p5 | Q6 | 133120 |
| sw03-p5 | Q7 | 158080 |
| sw04-p4 | Q6 | 328000 |
| sw04-p4 | Q7 | 296320 |
| sw04-p5 | Q6 | 177600 |
| sw04-p5 | Q7 | 189760 |
| sw05-p4 | Q6 | 224640 |
| sw05-p4 | Q7 | 83200 |
| sw06-p4 | Q6 | 269760 |
| sw06-p4 | Q7 | 114240 |
| sw06-p5 | Q6 | 303360 |
| sw06-p5 | Q7 | 304320 |
| sw07-p5 | Q6 | 174720 |
| sw07-p5 | Q7 | 149760 |
| sw08-p2 | Q6 | 189120 |
| sw08-p2 | Q7 | 147520 |
| sw08-p4 | Q6 | 270400 |
| sw08-p4 | Q7 | 320640 |

## Per-port GCL entries: before (SMT) vs. after (RL-enlarged)

| port | SMT entries | RL-enlarged entries | GCL_size |
|---|---|---|---|
| sw01-p2 | 29 | 31 | 255 |
| sw01-p4 | 17 | 22 | 255 |
| sw02-p2 | 3 | 22 | 255 |
| sw02-p4 | 21 | 28 | 255 |
| sw03-p4 | 29 | 31 | 255 |
| sw03-p5 | 17 | 22 | 255 |
| sw04-p4 | 3 | 24 | 255 |
| sw04-p5 | 21 | 29 | 255 |
| sw05-p4 | 17 | 19 | 255 |
| sw05-p5 | 29 | 31 | 255 |
| sw06-p4 | 21 | 25 | 255 |
| sw06-p5 | 3 | 21 | 255 |
| sw07-p4 | 29 | 31 | 255 |
| sw07-p5 | 17 | 23 | 255 |
| sw08-p2 | 25 | 23 | 255 |
| sw08-p4 | 3 | 22 | 255 |
| sw08-p5 | 29 | 31 | 255 |

## Flows

| flow | route | fixed | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|---|
| s0(id=1 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | yes | 7 | 24960 | 95760 | yes |
| s1(id=2 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | no | None | None | None | no |
| s2(id=3 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | yes | 7 | 24960 | 95760 | yes |
| s3(id=4 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | no | None | None | None | no |
| s4(id=5 S3->S1) | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | no | None | None | None | no |
| s5(id=6 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | yes | 6 | 49920 | 145680 | yes |
| s6(id=7 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |
| s7(id=8 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | yes | 6 | 0 | 95760 | yes |
| s8(id=9 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | yes | 6 | 74880 | 145680 | yes |
| s9(id=10 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | yes | 7 | 49920 | 95760 | yes |
| s10(id=11 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | no | None | None | None | no |
| s11(id=12 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |
| s12(id=13 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | yes | 6 | 0 | 79120 | yes |
| s13(id=14 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | yes | 6 | 0 | 95760 | yes |
| s14(id=15 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | no | None | None | None | no |
| s15(id=16 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | no | None | None | None | no |
| s16(id=17 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | no | None | None | None | no |
| s17(id=18 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | yes | 6 | 74880 | 79120 | yes |
| s18(id=19 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | yes | 7 | 49920 | 95760 | yes |
| s19(id=20 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | yes | 6 | 24960 | 145680 | yes |

## Per-hop windows (slack_ns > 0 means this window was enlarged)

| flow | egress port | queue | psi (ns) | delta (ns) |
|---|---|---|---|---|
| s0(id=1 S3->S2) | S3-p0 | Q7 | 24960 | 12480 |
| s0(id=1 S3->S2) | sw01-p4 | Q7 | 41600 | 12480 |
| s0(id=1 S3->S2) | sw03-p5 | Q7 | 58240 | 12480 |
| s0(id=1 S3->S2) | sw05-p4 | Q7 | 74880 | 12480 |
| s0(id=1 S3->S2) | sw07-p5 | Q7 | 91520 | 12480 |
| s0(id=1 S3->S2) | sw08-p2 | Q7 | 108160 | 12480 |
| s2(id=3 S2->S3) | S2-p0 | Q7 | 24960 | 12480 |
| s2(id=3 S2->S3) | sw08-p5 | Q7 | 41600 | 12480 |
| s2(id=3 S2->S3) | sw07-p4 | Q7 | 58240 | 12480 |
| s2(id=3 S2->S3) | sw05-p5 | Q7 | 74880 | 12480 |
| s2(id=3 S2->S3) | sw03-p4 | Q7 | 91520 | 12480 |
| s2(id=3 S2->S3) | sw01-p2 | Q7 | 108160 | 12480 |
| s5(id=6 S1->S3) | S1-p0 | Q6 | 49920 | 12480 |
| s5(id=6 S1->S3) | sw02-p4 | Q6 | 66560 | 12480 |
| s5(id=6 S1->S3) | sw04-p5 | Q6 | 83200 | 12480 |
| s5(id=6 S1->S3) | sw06-p4 | Q6 | 99840 | 12480 |
| s5(id=6 S1->S3) | sw08-p5 | Q6 | 116480 | 12480 |
| s5(id=6 S1->S3) | sw07-p4 | Q6 | 133120 | 12480 |
| s5(id=6 S1->S3) | sw05-p5 | Q6 | 149760 | 12480 |
| s5(id=6 S1->S3) | sw03-p4 | Q6 | 166400 | 12480 |
| s5(id=6 S1->S3) | sw01-p2 | Q6 | 183040 | 12480 |
| s7(id=8 S2->S3) | S2-p0 | Q6 | 0 | 12480 |
| s7(id=8 S2->S3) | sw08-p5 | Q6 | 16640 | 12480 |
| s7(id=8 S2->S3) | sw07-p4 | Q6 | 33280 | 12480 |
| s7(id=8 S2->S3) | sw05-p5 | Q6 | 49920 | 12480 |
| s7(id=8 S2->S3) | sw03-p4 | Q6 | 66560 | 12480 |
| s7(id=8 S2->S3) | sw01-p2 | Q6 | 83200 | 12480 |
| s8(id=9 S1->S3) | S1-p0 | Q6 | 74880 | 12480 |
| s8(id=9 S1->S3) | sw02-p4 | Q6 | 91520 | 12480 |
| s8(id=9 S1->S3) | sw04-p5 | Q6 | 108160 | 12480 |
| s8(id=9 S1->S3) | sw06-p4 | Q6 | 124800 | 12480 |
| s8(id=9 S1->S3) | sw08-p5 | Q6 | 141440 | 12480 |
| s8(id=9 S1->S3) | sw07-p4 | Q6 | 158080 | 12480 |
| s8(id=9 S1->S3) | sw05-p5 | Q6 | 174720 | 12480 |
| s8(id=9 S1->S3) | sw03-p4 | Q6 | 191360 | 12480 |
| s8(id=9 S1->S3) | sw01-p2 | Q6 | 208000 | 12480 |
| s9(id=10 S3->S2) | S3-p0 | Q7 | 49920 | 12480 |
| s9(id=10 S3->S2) | sw01-p4 | Q7 | 66560 | 12480 |
| s9(id=10 S3->S2) | sw03-p5 | Q7 | 83200 | 12480 |
| s9(id=10 S3->S2) | sw05-p4 | Q7 | 99840 | 12480 |
| s9(id=10 S3->S2) | sw07-p5 | Q7 | 116480 | 12480 |
| s9(id=10 S3->S2) | sw08-p2 | Q7 | 133120 | 12480 |
| s12(id=13 S1->S2) | S1-p0 | Q6 | 0 | 12480 |
| s12(id=13 S1->S2) | sw02-p4 | Q6 | 16640 | 12480 |
| s12(id=13 S1->S2) | sw04-p5 | Q6 | 33280 | 12480 |
| s12(id=13 S1->S2) | sw06-p4 | Q6 | 49920 | 12480 |
| s12(id=13 S1->S2) | sw08-p2 | Q6 | 66560 | 12480 |
| s13(id=14 S3->S2) | S3-p0 | Q6 | 0 | 12480 |
| s13(id=14 S3->S2) | sw01-p4 | Q6 | 16640 | 12480 |
| s13(id=14 S3->S2) | sw03-p5 | Q6 | 33280 | 12480 |
| s13(id=14 S3->S2) | sw05-p4 | Q6 | 49920 | 12480 |
| s13(id=14 S3->S2) | sw07-p5 | Q6 | 66560 | 12480 |
| s13(id=14 S3->S2) | sw08-p2 | Q6 | 83200 | 12480 |
| s17(id=18 S2->S1) | S2-p0 | Q6 | 74880 | 12480 |
| s17(id=18 S2->S1) | sw08-p4 | Q6 | 91520 | 12480 |
| s17(id=18 S2->S1) | sw06-p5 | Q6 | 108160 | 12480 |
| s17(id=18 S2->S1) | sw04-p4 | Q6 | 124800 | 12480 |
| s17(id=18 S2->S1) | sw02-p2 | Q6 | 141440 | 12480 |
| s18(id=19 S2->S3) | S2-p0 | Q7 | 49920 | 12480 |
| s18(id=19 S2->S3) | sw08-p5 | Q7 | 66560 | 12480 |
| s18(id=19 S2->S3) | sw07-p4 | Q7 | 83200 | 12480 |
| s18(id=19 S2->S3) | sw05-p5 | Q7 | 99840 | 12480 |
| s18(id=19 S2->S3) | sw03-p4 | Q7 | 116480 | 12480 |
| s18(id=19 S2->S3) | sw01-p2 | Q7 | 133120 | 12480 |
| s19(id=20 S1->S3) | S1-p0 | Q6 | 24960 | 12480 |
| s19(id=20 S1->S3) | sw02-p4 | Q6 | 41600 | 12480 |
| s19(id=20 S1->S3) | sw04-p5 | Q6 | 58240 | 12480 |
| s19(id=20 S1->S3) | sw06-p4 | Q6 | 74880 | 12480 |
| s19(id=20 S1->S3) | sw08-p5 | Q6 | 91520 | 12480 |
| s19(id=20 S1->S3) | sw07-p4 | Q6 | 108160 | 12480 |
| s19(id=20 S1->S3) | sw05-p5 | Q6 | 124800 | 12480 |
| s19(id=20 S1->S3) | sw03-p4 | Q6 | 141440 | 12480 |
| s19(id=20 S1->S3) | sw01-p2 | Q6 | 158080 | 12480 |

## Metrics (training/evaluation signal, not the export)

| metric | value |
|---|---|
| trial-placed flow ratio (fixed + trial-admitted) | 0.900 |
| r1  same-queue window adjacency | 0.376 |
| r2  deadline-violation ratio | 0.000 |
| r3  supplier/receiver overlap | 0.997 |
| r4  mean e2e/deadline (admitted) | 0.301 |
| constraint violations | 0 |

## Constraint check

- C1-C7, C9: OK
- seed-integrity (no SMT-fixed flow's placement changed): OK

## GCL per egress port

### sw01-p2  (31 entries, util 21.8400 %)

```
sgs 83200 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 62720 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 1600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 48320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 112640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 112640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 62400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 29440 0x3F # 00111111   BE
```

### sw01-p4  (22 entries, util 12.4800 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 1920 0x3F # 00111111   BE
sgs 77440 0x40 # 01000000   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 141760 0x40 # 01000000   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 91840 0x80 # 10000000   Q7
sgs 41600 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 125120 0x40 # 01000000   Q6
sgs 58240 0xBF # 10111111   Q7
```

### sw02-p2  (22 entries, util 1.5600 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 25280 0x40 # 01000000   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 87680 0x80 # 10000000   Q7
sgs 33280 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 58560 0x7F # 01111111   Q6
sgs 20480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 16960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 58560 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p4  (28 entries, util 15.6000 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 31680 0x40 # 01000000   Q6
sgs 26880 0x7F # 01111111   Q6
sgs 21120 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 16320 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 127040 0x40 # 01000000   Q6
sgs 31360 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 114560 0x80 # 10000000   Q7
sgs 31360 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 110400 0x40 # 01000000   Q6
sgs 48000 0xBF # 10111111   Q7
```

### sw03-p4  (31 entries, util 21.8400 %)

```
sgs 66560 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 62720 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 1600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 48320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 112640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 112640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 62400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 46080 0x3F # 00111111   BE
```

### sw03-p5  (22 entries, util 12.4800 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 3840 0x3F # 00111111   BE
sgs 75520 0x40 # 01000000   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 141760 0x40 # 01000000   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 91840 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 108480 0x40 # 01000000   Q6
sgs 58240 0xBF # 10111111   Q7
```

### sw04-p4  (24 entries, util 1.5600 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0xBF # 10111111   Q7
sgs 24640 0x7F # 01111111   Q6
sgs 25280 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 87680 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0xBF # 10111111   Q7
sgs 53760 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 33600 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 25280 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (29 entries, util 15.6000 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 11520 0x3F # 00111111   BE
sgs 49280 0x80 # 10000000   Q7
sgs 18560 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 123200 0x40 # 01000000   Q6
sgs 18560 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 22080 0x40 # 01000000   Q6
sgs 19840 0xBF # 10111111   Q7
sgs 32000 0x7F # 01111111   Q6
sgs 49280 0x80 # 10000000   Q7
sgs 18560 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 89920 0x40 # 01000000   Q6
sgs 51840 0xBF # 10111111   Q7
```

### sw05-p4  (19 entries, util 12.4800 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 5760 0x3F # 00111111   BE
sgs 73600 0x40 # 01000000   Q6
sgs 58240 0x7F # 01111111   Q6
sgs 141760 0x40 # 01000000   Q6
sgs 58240 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 91840 0x80 # 10000000   Q7
sgs 58240 0x7F # 01111111   Q6
sgs 91840 0x40 # 01000000   Q6
sgs 58240 0xBF # 10111111   Q7
```

### sw05-p5  (31 entries, util 21.8400 %)

```
sgs 49920 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 62720 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 1600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 48320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 112640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 112640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 62400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 62720 0x3F # 00111111   BE
```

### sw06-p4  (25 entries, util 15.6000 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 11520 0x3F # 00111111   BE
sgs 49280 0x80 # 10000000   Q7
sgs 51840 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 123200 0x40 # 01000000   Q6
sgs 51840 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 22080 0x40 # 01000000   Q6
sgs 51840 0x7F # 01111111   Q6
sgs 49280 0x80 # 10000000   Q7
sgs 51840 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 73280 0x40 # 01000000   Q6
sgs 51840 0xBF # 10111111   Q7
```

### sw06-p5  (21 entries, util 1.5600 %)

```
sgs 45760 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
sgs 25280 0x40 # 01000000   Q6
sgs 16640 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 45760 0x7F # 01111111   Q6
sgs 87680 0x80 # 10000000   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 45760 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 41920 0xBF # 10111111   Q7
sgs 37120 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 45760 0x7F # 01111111   Q6
sgs 41920 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (31 entries, util 21.8400 %)

```
sgs 33280 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 62720 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 1600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 48320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 112640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 112640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 62400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 79360 0x3F # 00111111   BE
```

### sw07-p5  (23 entries, util 12.4800 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 11520 0x3F # 00111111   BE
sgs 67840 0x40 # 01000000   Q6
sgs 41600 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 141760 0x40 # 01000000   Q6
sgs 41600 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 91840 0x80 # 10000000   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 75200 0x40 # 01000000   Q6
sgs 58240 0xBF # 10111111   Q7
```

### sw08-p2  (23 entries, util 18.7200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 29120 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 34560 0xBF # 10111111   Q7
sgs 40000 0x40 # 01000000   Q6
sgs 29760 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 153600 0x40 # 01000000   Q6
sgs 29760 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 29120 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 87040 0x80 # 10000000   Q7
sgs 29760 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 87040 0x40 # 01000000   Q6
sgs 46400 0xBF # 10111111   Q7
```

### sw08-p4  (22 entries, util 1.5600 %)

```
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
sgs 25280 0x40 # 01000000   Q6
sgs 33280 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 87680 0x80 # 10000000   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 58560 0xBF # 10111111   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 16960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 58560 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (31 entries, util 21.8400 %)

```
sgs 16640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 62720 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 1600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 48320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 112640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 112640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 62400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 96000 0x3F # 00111111   BE
```

