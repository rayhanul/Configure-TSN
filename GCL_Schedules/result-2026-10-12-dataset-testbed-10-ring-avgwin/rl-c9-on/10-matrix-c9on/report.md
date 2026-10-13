# RL-enlarged GCL schedule (Problem 2: window enlargement)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Seeded from SMT run: **result/result-2026-10-12-dataset-testbed-10-ring-avgwin/smt-c9-on/10-fair-retimed-c9on**

## Admission (unchanged) vs. capacity grown

Problem 2 never admits a flow into the schedule it exports -- it only widens windows. `admitted` below is exactly the SMT baseline, by construction; the capacity growth this run achieved is banked slack and per-port GCL entries, reported separately.

| | admitted | of total |
|---|---|---|
| SMT (fixed, never moved) | 11 | 11 |
| RL-enlarged (exported; grow-only, admits nothing new) | 11 | 20 |

During training, the policy's trial admissions (the reward signal that teaches it how much a window needs to grow) reached **6** of the 9 SMT-rejected flows -- none of those are kept in this export; that capacity stays as empty, banked slack for Problem 3 to fill. Total slack banked: 120960 ns. GCL_size overflow: 0.

## Opportunistic idle top-up (deterministic post-pass)

**14515200 ns**, drawn from idle capacity on ports at or below utilisation 0.2, independent of what training happened to grow. Ported from prob_2_heuristic_enlarged's Step 7.

| port | queue | applied (ns) |
|---|---|---|
| S1-p0 | Q6 | 262720 |
| S1-p0 | Q7 | 350080 |
| S2-p0 | Q6 | 487680 |
| S2-p0 | Q7 | 150080 |
| S3-p0 | Q6 | 137600 |
| S3-p0 | Q7 | 500160 |
| sw01-p2 | Q6 | 405120 |
| sw01-p2 | Q7 | 34560 |
| sw01-p4 | Q6 | 164800 |
| sw01-p4 | Q7 | 540160 |
| sw01-p5 | Q6 | 367360 |
| sw01-p5 | Q7 | 303680 |
| sw02-p2 | Q6 | 56960 |
| sw02-p2 | Q7 | 586240 |
| sw02-p4 | Q6 | 138240 |
| sw02-p4 | Q7 | 566080 |
| sw02-p5 | Q6 | 223360 |
| sw02-p5 | Q7 | 444160 |
| sw03-p4 | Q6 | 517120 |
| sw03-p4 | Q7 | 133760 |
| sw03-p5 | Q6 | 167040 |
| sw03-p5 | Q7 | 530240 |
| sw04-p4 | Q6 | 14400 |
| sw04-p4 | Q7 | 675200 |
| sw04-p5 | Q6 | 138880 |
| sw04-p5 | Q7 | 557120 |
| sw05-p4 | Q6 | 169280 |
| sw05-p4 | Q7 | 520320 |
| sw05-p5 | Q6 | 532160 |
| sw05-p5 | Q7 | 124800 |
| sw06-p4 | Q6 | 139520 |
| sw06-p4 | Q7 | 548160 |
| sw06-p5 | Q6 | 9600 |
| sw06-p5 | Q7 | 687680 |
| sw07-p4 | Q6 | 547200 |
| sw07-p4 | Q7 | 115840 |
| sw07-p5 | Q6 | 171520 |
| sw07-p5 | Q7 | 510400 |
| sw08-p2 | Q6 | 178560 |
| sw08-p2 | Q7 | 433280 |
| sw08-p4 | Q6 | 4800 |
| sw08-p4 | Q7 | 700160 |
| sw08-p5 | Q6 | 562240 |
| sw08-p5 | Q7 | 106880 |

## Best-effort gap equalization (deterministic post-pass)

**8339200 ns** given back from the top-up/creation above so each port's leftover non-TAS gaps land close to equal. Ported from prob_2_heuristic_enlarged's Step 9.

| port | given back (ns) |
|---|---|---|
| sw02-p4 | 528320 |
| sw04-p5 | 527680 |
| sw06-p4 | 527040 |
| sw02-p5 | 487040 |
| sw01-p4 | 434880 |
| sw03-p5 | 432320 |
| sw05-p4 | 429760 |
| sw07-p5 | 427200 |
| sw04-p4 | 408000 |
| sw06-p5 | 403200 |
| sw08-p4 | 398400 |
| sw03-p4 | 397440 |
| sw05-p5 | 388480 |
| sw07-p4 | 379520 |
| sw08-p5 | 370560 |
| S3-p0 | 299520 |
| sw01-p5 | 282240 |
| sw08-p2 | 264000 |
| sw01-p2 | 263680 |
| S2-p0 | 249280 |
| sw02-p2 | 238080 |
| S1-p0 | 202560 |

## Opportunistic overlay window creation (deterministic post-pass)

**44** new overlay window(s), **8732480 ns** total, carved out of already-open best-effort spans on ports at or below utilisation 0.2 -- best-effort stays reachable inside each one (gate mask keeps its BE bits set). Run once after training/finalize_grow_only(), not a trained action.

| port | queue | size (ns) |
|---|---|---|
| S1-p0 | Q6 | 24960 |
| S1-p0 | Q7 | 177600 |
| S2-p0 | Q6 | 12480 |
| S2-p0 | Q7 | 236800 |
| S3-p0 | Q6 | 99840 |
| S3-p0 | Q7 | 199680 |
| sw01-p2 | Q6 | 61440 |
| sw01-p2 | Q7 | 182400 |
| sw01-p4 | Q6 | 199040 |
| sw01-p4 | Q7 | 235840 |
| sw01-p5 | Q6 | 155520 |
| sw01-p5 | Q7 | 136320 |
| sw02-p2 | Q6 | 121280 |
| sw02-p2 | Q7 | 130880 |
| sw02-p4 | Q6 | 302080 |
| sw02-p4 | Q7 | 259520 |
| sw02-p5 | Q6 | 147200 |
| sw02-p5 | Q7 | 339840 |
| sw03-p4 | Q6 | 164480 |
| sw03-p4 | Q7 | 257280 |
| sw03-p5 | Q6 | 234240 |
| sw03-p5 | Q7 | 213440 |
| sw04-p4 | Q6 | 243520 |
| sw04-p4 | Q7 | 237440 |
| sw04-p5 | Q6 | 310400 |
| sw04-p5 | Q7 | 258880 |
| sw05-p4 | Q6 | 238720 |
| sw05-p4 | Q7 | 214080 |
| sw05-p5 | Q6 | 152320 |
| sw05-p5 | Q7 | 254400 |
| sw06-p4 | Q6 | 318720 |
| sw06-p4 | Q7 | 258240 |
| sw06-p5 | Q6 | 256000 |
| sw06-p5 | Q7 | 202880 |
| sw07-p4 | Q6 | 111360 |
| sw07-p4 | Q7 | 247680 |
| sw07-p5 | Q6 | 206080 |
| sw07-p5 | Q7 | 251840 |
| sw08-p2 | Q6 | 153600 |
| sw08-p2 | Q7 | 118400 |
| sw08-p4 | Q6 | 254080 |
| sw08-p4 | Q7 | 197120 |
| sw08-p5 | Q6 | 106880 |
| sw08-p5 | Q7 | 247680 |

## Per-port GCL entries: before (SMT) vs. after (RL-enlarged)

| port | SMT entries | RL-enlarged entries | GCL_size |
|---|---|---|---|
| sw01-p2 | 25 | 40 | 255 |
| sw01-p4 | 9 | 19 | 255 |
| sw01-p5 | 11 | 11 | 255 |
| sw02-p2 | 13 | 11 | 255 |
| sw02-p4 | 11 | 19 | 255 |
| sw02-p5 | 13 | 24 | 255 |
| sw03-p4 | 13 | 27 | 255 |
| sw03-p5 | 9 | 22 | 255 |
| sw04-p4 | 3 | 14 | 255 |
| sw04-p5 | 11 | 19 | 255 |
| sw05-p4 | 9 | 22 | 255 |
| sw05-p5 | 13 | 27 | 255 |
| sw06-p4 | 11 | 19 | 255 |
| sw06-p5 | 3 | 14 | 255 |
| sw07-p4 | 13 | 22 | 255 |
| sw07-p5 | 9 | 22 | 255 |
| sw08-p2 | 19 | 18 | 255 |
| sw08-p4 | 3 | 14 | 255 |
| sw08-p5 | 13 | 22 | 255 |

## Flows

| flow | route | fixed | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|---|
| s0(id=1 S3->S1) | S3->sw01->sw02->S1 | yes | 6 | 24960 | 27920 | yes |
| s1(id=2 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | no | None | None | None | no |
| s2(id=3 S1->S3) | S1->sw02->sw01->S3 | yes | 6 | 0 | 27920 | yes |
| s3(id=4 S1->S3) | S1->sw02->sw01->S3 | no | None | None | None | no |
| s4(id=5 S3->S1) | S3->sw01->sw02->S1 | yes | 7 | 74880 | 31120 | yes |
| s5(id=6 S1->S3) | S1->sw02->sw01->S3 | no | None | None | None | no |
| s6(id=7 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | yes | 7 | 0 | 42960 | yes |
| s7(id=8 S1->S3) | S1->sw02->sw01->S3 | no | None | None | None | no |
| s8(id=9 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | yes | 7 | 0 | 50960 | yes |
| s9(id=10 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | yes | 6 | 49920 | 43280 | yes |
| s10(id=11 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | yes | 7 | 24960 | 42960 | yes |
| s11(id=12 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | yes | 7 | 24960 | 45840 | yes |
| s12(id=13 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | no | None | None | None | no |
| s13(id=14 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | no | None | None | None | no |
| s14(id=15 S3->S1) | S3->sw01->sw02->S1 | yes | 6 | 49920 | 26000 | yes |
| s15(id=16 S3->S1) | S3->sw01->sw02->S1 | no | None | None | None | no |
| s16(id=17 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | yes | 6 | 74880 | 43280 | yes |
| s17(id=18 S1->S3) | S1->sw02->sw01->S3 | yes | 6 | 49920 | 30800 | yes |
| s18(id=19 S3->S1) | S3->sw01->sw02->S1 | no | None | None | None | no |
| s19(id=20 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | no | None | None | None | no |

## Per-hop windows (slack_ns > 0 means this window was enlarged)

| flow | egress port | queue | psi (ns) | delta (ns) |
|---|---|---|---|---|
| s0(id=1 S3->S1) | S3-p0 | Q6 | 24960 | 12480 |
| s0(id=1 S3->S1) | sw01-p5 | Q6 | 32640 | 12480 |
| s0(id=1 S3->S1) | sw02-p2 | Q6 | 40320 | 12480 |
| s2(id=3 S1->S3) | S1-p0 | Q6 | 0 | 12480 |
| s2(id=3 S1->S3) | sw02-p5 | Q6 | 7680 | 12480 |
| s2(id=3 S1->S3) | sw01-p2 | Q6 | 15360 | 12480 |
| s4(id=5 S3->S1) | S3-p0 | Q7 | 74880 | 12480 |
| s4(id=5 S3->S1) | sw01-p5 | Q7 | 82560 | 12480 |
| s4(id=5 S3->S1) | sw02-p2 | Q7 | 93440 | 12480 |
| s6(id=7 S2->S3) | S2-p0 | Q7 | 0 | 12480 |
| s6(id=7 S2->S3) | sw08-p5 | Q7 | 6080 | 12480 |
| s6(id=7 S2->S3) | sw07-p4 | Q7 | 12160 | 12480 |
| s6(id=7 S2->S3) | sw05-p5 | Q7 | 18240 | 12480 |
| s6(id=7 S2->S3) | sw03-p4 | Q7 | 24320 | 12480 |
| s6(id=7 S2->S3) | sw01-p2 | Q7 | 30400 | 12480 |
| s8(id=9 S3->S2) | S3-p0 | Q7 | 0 | 12480 |
| s8(id=9 S3->S2) | sw01-p4 | Q7 | 7680 | 12480 |
| s8(id=9 S3->S2) | sw03-p5 | Q7 | 15360 | 12480 |
| s8(id=9 S3->S2) | sw05-p4 | Q7 | 23040 | 12480 |
| s8(id=9 S3->S2) | sw07-p5 | Q7 | 30720 | 12480 |
| s8(id=9 S3->S2) | sw08-p2 | Q7 | 38400 | 12480 |
| s9(id=10 S2->S1) | S2-p0 | Q6 | 49920 | 12480 |
| s9(id=10 S2->S1) | sw08-p4 | Q6 | 57600 | 12480 |
| s9(id=10 S2->S1) | sw06-p5 | Q6 | 65280 | 12480 |
| s9(id=10 S2->S1) | sw04-p4 | Q6 | 72960 | 12480 |
| s9(id=10 S2->S1) | sw02-p2 | Q6 | 80640 | 12480 |
| s10(id=11 S2->S3) | S2-p0 | Q7 | 24960 | 12480 |
| s10(id=11 S2->S3) | sw08-p5 | Q7 | 31040 | 12480 |
| s10(id=11 S2->S3) | sw07-p4 | Q7 | 37120 | 12480 |
| s10(id=11 S2->S3) | sw05-p5 | Q7 | 43200 | 12480 |
| s10(id=11 S2->S3) | sw03-p4 | Q7 | 49280 | 12480 |
| s10(id=11 S2->S3) | sw01-p2 | Q7 | 55360 | 12480 |
| s11(id=12 S1->S2) | S1-p0 | Q7 | 24960 | 12480 |
| s11(id=12 S1->S2) | sw02-p4 | Q7 | 33280 | 12480 |
| s11(id=12 S1->S2) | sw04-p5 | Q7 | 41600 | 12480 |
| s11(id=12 S1->S2) | sw06-p4 | Q7 | 49920 | 12480 |
| s11(id=12 S1->S2) | sw08-p2 | Q7 | 58240 | 12480 |
| s14(id=15 S3->S1) | S3-p0 | Q6 | 49920 | 12480 |
| s14(id=15 S3->S1) | sw01-p5 | Q6 | 56640 | 12480 |
| s14(id=15 S3->S1) | sw02-p2 | Q6 | 63360 | 12480 |
| s16(id=17 S1->S2) | S1-p0 | Q6 | 74880 | 12480 |
| s16(id=17 S1->S2) | sw02-p4 | Q6 | 82560 | 12480 |
| s16(id=17 S1->S2) | sw04-p5 | Q6 | 90240 | 12480 |
| s16(id=17 S1->S2) | sw06-p4 | Q6 | 97920 | 12480 |
| s16(id=17 S1->S2) | sw08-p2 | Q6 | 105600 | 12480 |
| s17(id=18 S1->S3) | S1-p0 | Q6 | 49920 | 12480 |
| s17(id=18 S1->S3) | sw02-p5 | Q6 | 56000 | 12480 |
| s17(id=18 S1->S3) | sw01-p2 | Q6 | 68160 | 12480 |

## Metrics (training/evaluation signal, not the export)

| metric | value |
|---|---|
| trial-placed flow ratio (fixed + trial-admitted) | 0.850 |
| r1  same-queue window adjacency | 0.352 |
| r2  deadline-violation ratio | 0.000 |
| r3  supplier/receiver overlap | 0.991 |
| r4  mean e2e/deadline (admitted) | 0.162 |
| constraint violations | 0 |

## Constraint check

- C1-C7, C9: OK
- seed-integrity (no SMT-fixed flow's placement changed): OK

## GCL per egress port

### sw01-p2  (40 entries, util 18.7200 %)

```
sgs 15360 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 2560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 9920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 2240 0x3F # 00111111   BE
sgs 76160 0x40 # 01000000   Q6
sgs 18560 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 2560 0x3F # 00111111   BE
sgs 40960 0x80 # 10000000   Q7
sgs 33920 0xBF # 10111111   Q7
sgs 76160 0x40 # 01000000   Q6
sgs 18560 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 2560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 9920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 2240 0x3F # 00111111   BE
sgs 76160 0x40 # 01000000   Q6
sgs 18560 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 2560 0x3F # 00111111   BE
sgs 40960 0x80 # 10000000   Q7
sgs 33920 0xBF # 10111111   Q7
sgs 60800 0x40 # 01000000   Q6
sgs 33920 0xBF # 10111111   Q7
```

### sw01-p4  (19 entries, util 6.2400 %)

```
sgs 7680 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 23360 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 13120 0xBF # 10111111   Q7
sgs 44800 0x80 # 10000000   Q7
sgs 36160 0x7F # 01111111   Q6
sgs 57600 0xBF # 10111111   Q7
sgs 106240 0x80 # 10000000   Q7
sgs 36160 0x7F # 01111111   Q6
sgs 57600 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 23360 0x7F # 01111111   Q6
sgs 70400 0x40 # 01000000   Q6
sgs 36160 0x7F # 01111111   Q6
sgs 57600 0xBF # 10111111   Q7
sgs 98560 0x80 # 10000000   Q7
sgs 43840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p5  (11 entries, util 7.8000 %)

```
sgs 32640 0x7F # 01111111   Q6
sgs 36480 0x40 # 01000000   Q6
sgs 13440 0xBF # 10111111   Q7
sgs 227200 0x80 # 10000000   Q7
sgs 40320 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 32640 0x7F # 01111111   Q6
sgs 244480 0x40 # 01000000   Q6
sgs 23040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (11 entries, util 9.3600 %)

```
sgs 40320 0x7F # 01111111   Q6
sgs 52800 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 256320 0x80 # 10000000   Q7
sgs 50240 0xBF # 10111111   Q7
sgs 40320 0x7F # 01111111   Q6
sgs 35520 0x40 # 01000000   Q6
sgs 30720 0xBF # 10111111   Q7
sgs 202880 0x80 # 10000000   Q7
sgs 40640 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p4  (19 entries, util 7.8000 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 36800 0xBF # 10111111   Q7
sgs 27840 0x40 # 01000000   Q6
sgs 39680 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 77120 0x80 # 10000000   Q7
sgs 39680 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 77120 0x80 # 10000000   Q7
sgs 39680 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 43840 0x80 # 10000000   Q7
sgs 23040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p5  (24 entries, util 9.3600 %)

```
sgs 7680 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 35840 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 13760 0xBF # 10111111   Q7
sgs 59520 0x80 # 10000000   Q7
sgs 65920 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 29760 0x7F # 01111111   Q6
sgs 32320 0xBF # 10111111   Q7
sgs 59520 0x80 # 10000000   Q7
sgs 65920 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 35840 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 13760 0xBF # 10111111   Q7
sgs 59520 0x80 # 10000000   Q7
sgs 65920 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 29760 0x7F # 01111111   Q6
sgs 32320 0xBF # 10111111   Q7
sgs 51840 0x80 # 10000000   Q7
sgs 16000 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (27 entries, util 9.3600 %)

```
sgs 24320 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 14720 0xBF # 10111111   Q7
sgs 81920 0x40 # 01000000   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 24320 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0x7F # 01111111   Q6
sgs 26560 0xBF # 10111111   Q7
sgs 81920 0x40 # 01000000   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 24320 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 14720 0xBF # 10111111   Q7
sgs 81920 0x40 # 01000000   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 24320 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0x7F # 01111111   Q6
sgs 26560 0xBF # 10111111   Q7
sgs 57600 0x40 # 01000000   Q6
sgs 16000 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p5  (22 entries, util 6.2400 %)

```
sgs 15360 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 21760 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 13760 0xBF # 10111111   Q7
sgs 45760 0x80 # 10000000   Q7
sgs 28480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 106240 0x80 # 10000000   Q7
sgs 28480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 21760 0x7F # 01111111   Q6
sgs 72000 0x40 # 01000000   Q6
sgs 28480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 90880 0x80 # 10000000   Q7
sgs 43840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p4  (14 entries, util 1.5600 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 23040 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0xBF # 10111111   Q7
sgs 203200 0x80 # 10000000   Q7
sgs 47040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 103360 0x80 # 10000000   Q7
sgs 46720 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (19 entries, util 7.8000 %)

```
sgs 41600 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 36160 0xBF # 10111111   Q7
sgs 28480 0x40 # 01000000   Q6
sgs 31360 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 77120 0x80 # 10000000   Q7
sgs 31360 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 77120 0x80 # 10000000   Q7
sgs 31360 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 35520 0x80 # 10000000   Q7
sgs 23040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (22 entries, util 6.2400 %)

```
sgs 23040 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0xBF # 10111111   Q7
sgs 46720 0x80 # 10000000   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 106240 0x80 # 10000000   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 73600 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 83200 0x80 # 10000000   Q7
sgs 43840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p5  (27 entries, util 9.3600 %)

```
sgs 18240 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 84160 0x40 # 01000000   Q6
sgs 47680 0xBF # 10111111   Q7
sgs 18240 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 19200 0x7F # 01111111   Q6
sgs 18240 0xBF # 10111111   Q7
sgs 84160 0x40 # 01000000   Q6
sgs 47680 0xBF # 10111111   Q7
sgs 18240 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 84160 0x40 # 01000000   Q6
sgs 47680 0xBF # 10111111   Q7
sgs 18240 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 19200 0x7F # 01111111   Q6
sgs 18240 0xBF # 10111111   Q7
sgs 65920 0x40 # 01000000   Q6
sgs 16000 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p4  (19 entries, util 7.8000 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 35520 0xBF # 10111111   Q7
sgs 29120 0x40 # 01000000   Q6
sgs 23040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 77120 0x80 # 10000000   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 77120 0x80 # 10000000   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 27200 0x80 # 10000000   Q7
sgs 23040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (14 entries, util 1.5600 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 15360 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 9600 0x3F # 00111111   BE
sgs 203200 0x80 # 10000000   Q7
sgs 59520 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 37440 0xBF # 10111111   Q7
sgs 115840 0x80 # 10000000   Q7
sgs 46720 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (22 entries, util 9.3600 %)

```
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 10240 0x3F # 00111111   BE
sgs 86400 0x40 # 01000000   Q6
sgs 65920 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 35200 0x7F # 01111111   Q6
sgs 86400 0x40 # 01000000   Q6
sgs 65920 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 10240 0x3F # 00111111   BE
sgs 86400 0x40 # 01000000   Q6
sgs 65920 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 35200 0x7F # 01111111   Q6
sgs 74240 0x40 # 01000000   Q6
sgs 16000 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p5  (22 entries, util 6.2400 %)

```
sgs 30720 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 18560 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 15040 0xBF # 10111111   Q7
sgs 47680 0x80 # 10000000   Q7
sgs 13120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 106240 0x80 # 10000000   Q7
sgs 13120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 18560 0xBF # 10111111   Q7
sgs 75200 0x40 # 01000000   Q6
sgs 13120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 75520 0x80 # 10000000   Q7
sgs 43840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p2  (18 entries, util 14.0400 %)

```
sgs 38400 0x7F # 01111111   Q6
sgs 32320 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 22400 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 960 0x3F # 00111111   BE
sgs 66560 0x80 # 10000000   Q7
sgs 14400 0xBF # 10111111   Q7
sgs 38400 0x7F # 01111111   Q6
sgs 147200 0x80 # 10000000   Q7
sgs 14400 0xBF # 10111111   Q7
sgs 38400 0x7F # 01111111   Q6
sgs 32320 0x80 # 10000000   Q7
sgs 114880 0x40 # 01000000   Q6
sgs 14400 0xBF # 10111111   Q7
sgs 38400 0x7F # 01111111   Q6
sgs 108800 0x80 # 10000000   Q7
sgs 52800 0xBF # 10111111   Q7
```

### sw08-p4  (14 entries, util 1.5600 %)

```
sgs 57600 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 4800 0x3F # 00111111   BE
sgs 203200 0x80 # 10000000   Q7
sgs 22080 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 128320 0x80 # 10000000   Q7
sgs 46720 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (22 entries, util 9.3600 %)

```
sgs 6080 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 8000 0x3F # 00111111   BE
sgs 88640 0x40 # 01000000   Q6
sgs 65920 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 32960 0x7F # 01111111   Q6
sgs 88640 0x40 # 01000000   Q6
sgs 65920 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 8000 0x3F # 00111111   BE
sgs 88640 0x40 # 01000000   Q6
sgs 65920 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 32960 0x7F # 01111111   Q6
sgs 82560 0x40 # 01000000   Q6
sgs 16000 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

