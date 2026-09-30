# RL-enlarged GCL schedule (Problem 2: window enlargement)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 2000 ns
- Seeded from SMT run: **result/result-dataset-testbed/smt-c9-on/1-fair-retimed-c9on**

## Admission (unchanged) vs. capacity grown

Problem 2 never admits a flow into the schedule it exports -- it only widens windows. `admitted` below is exactly the SMT baseline, by construction; the capacity growth this run achieved is banked slack and per-port GCL entries, reported separately.

| | admitted | of total |
|---|---|---|
| SMT (fixed, never moved) | 10 | 10 |
| RL-enlarged (exported; grow-only, admits nothing new) | 10 | 20 |

During training, the policy's trial admissions (the reward signal that teaches it how much a window needs to grow) reached **10** of the 10 SMT-rejected flows -- none of those are kept in this export; that capacity stays as empty, banked slack for Problem 3 to fill. Total slack banked: 84160 ns. GCL_size overflow: 0.

## Opportunistic idle top-up (deterministic post-pass)

**15310080 ns**, drawn from idle capacity on ports at or below utilisation 0.2, independent of what training happened to grow. Ported from prob_2_heuristic_enlarged's Step 7.

| port | queue | applied (ns) |
|---|---|---|
| S1-p0 | Q7 | 787520 |
| S2-p0 | Q6 | 576640 |
| S2-p0 | Q7 | 190080 |
| S3-p0 | Q6 | 177600 |
| S3-p0 | Q7 | 555520 |
| sw01-p3 | Q6 | 390080 |
| sw01-p3 | Q7 | 384640 |
| sw01-p4 | Q6 | 368000 |
| sw01-p4 | Q7 | 383360 |
| sw01-p5 | Q7 | 765120 |
| sw02-p2 | Q6 | 181760 |
| sw02-p2 | Q7 | 555840 |
| sw02-p3 | Q7 | 790720 |
| sw02-p5 | Q7 | 788800 |
| sw03-p3 | Q6 | 390080 |
| sw03-p3 | Q7 | 386880 |
| sw03-p4 | Q6 | 364160 |
| sw03-p4 | Q7 | 381120 |
| sw05-p2 | Q7 | 786560 |
| sw05-p5 | Q6 | 566080 |
| sw05-p5 | Q7 | 194560 |
| sw06-p2 | Q6 | 364160 |
| sw06-p2 | Q7 | 378880 |
| sw06-p3 | Q6 | 390080 |
| sw06-p3 | Q7 | 389120 |
| sw07-p3 | Q6 | 570240 |
| sw07-p3 | Q7 | 194560 |
| sw07-p4 | Q7 | 784320 |
| sw08-p2 | Q6 | 19200 |
| sw08-p2 | Q7 | 704000 |
| sw08-p4 | Q6 | 390080 |
| sw08-p4 | Q7 | 391360 |
| sw08-p5 | Q6 | 574400 |
| sw08-p5 | Q7 | 194560 |

## Opportunistic exclusive window creation (deterministic post-pass)

**20** brand-new *exclusive* window(s) opened, **729600 ns** total, on ports at or below utilisation 0.2 whose TT queue had zero windows before this run. Ported from prob_2_heuristic_enlarged's Step 8.

| port | queue | size (ns) |
|---|---|---|
| sw02-p4 | Q6 | 36480 |
| sw02-p4 | Q7 | 36480 |
| sw03-p5 | Q6 | 36480 |
| sw03-p5 | Q7 | 36480 |
| sw04-p3 | Q6 | 36480 |
| sw04-p3 | Q7 | 36480 |
| sw04-p4 | Q6 | 36480 |
| sw04-p4 | Q7 | 36480 |
| sw04-p5 | Q6 | 36480 |
| sw04-p5 | Q7 | 36480 |
| sw05-p3 | Q6 | 36480 |
| sw05-p3 | Q7 | 36480 |
| sw05-p4 | Q6 | 36480 |
| sw05-p4 | Q7 | 36480 |
| sw06-p4 | Q6 | 36480 |
| sw06-p4 | Q7 | 36480 |
| sw06-p5 | Q6 | 36480 |
| sw06-p5 | Q7 | 36480 |
| sw07-p5 | Q6 | 36480 |
| sw07-p5 | Q7 | 36480 |

## Best-effort gap equalization (deterministic post-pass)

**6556160 ns** given back from the top-up/creation above so each port's leftover non-TAS gaps land close to equal. Ported from prob_2_heuristic_enlarged's Step 9.

| port | given back (ns) |
|---|---|---|
| sw02-p5 | 636160 |
| sw05-p2 | 636160 |
| sw07-p4 | 454400 |
| S1-p0 | 454400 |
| sw03-p3 | 318720 |
| sw06-p3 | 318720 |
| sw08-p4 | 318720 |
| sw05-p5 | 313600 |
| sw07-p3 | 313600 |
| sw08-p5 | 313600 |
| sw01-p4 | 284160 |
| sw03-p4 | 284160 |
| sw06-p2 | 284160 |
| sw01-p5 | 279040 |
| sw02-p3 | 266240 |
| sw01-p3 | 264960 |
| S2-p0 | 259840 |
| sw08-p2 | 239360 |
| S3-p0 | 166400 |
| sw02-p2 | 149760 |

## Opportunistic overlay window creation (deterministic post-pass)

**59** new overlay window(s), **13934080 ns** total, carved out of already-open best-effort spans on ports at or below utilisation 0.2 -- best-effort stays reachable inside each one (gate mask keeps its BE bits set). Run once after training/finalize_grow_only(), not a trained action.

| port | queue | size (ns) |
|---|---|---|
| S1-p0 | Q6 | 199680 |
| S1-p0 | Q7 | 254720 |
| S2-p0 | Q6 | 60160 |
| S2-p0 | Q7 | 199680 |
| S3-p0 | Q7 | 166400 |
| sw01-p3 | Q6 | 122880 |
| sw01-p3 | Q7 | 149760 |
| sw01-p4 | Q6 | 90880 |
| sw01-p4 | Q7 | 199680 |
| sw01-p5 | Q6 | 72640 |
| sw01-p5 | Q7 | 206400 |
| sw02-p2 | Q6 | 17920 |
| sw02-p2 | Q7 | 136320 |
| sw02-p3 | Q6 | 121600 |
| sw02-p3 | Q7 | 150080 |
| sw02-p4 | Q6 | 349440 |
| sw02-p4 | Q7 | 377600 |
| sw02-p5 | Q6 | 228800 |
| sw02-p5 | Q7 | 407360 |
| sw03-p3 | Q6 | 135360 |
| sw03-p3 | Q7 | 196480 |
| sw03-p4 | Q6 | 93120 |
| sw03-p4 | Q7 | 199680 |
| sw03-p5 | Q6 | 349440 |
| sw03-p5 | Q7 | 377600 |
| sw04-p3 | Q6 | 349440 |
| sw04-p3 | Q7 | 377600 |
| sw04-p4 | Q6 | 349440 |
| sw04-p4 | Q7 | 377600 |
| sw04-p5 | Q6 | 349440 |
| sw04-p5 | Q7 | 377600 |
| sw05-p2 | Q6 | 240000 |
| sw05-p2 | Q7 | 400640 |
| sw05-p3 | Q6 | 349440 |
| sw05-p3 | Q7 | 377600 |
| sw05-p4 | Q6 | 349440 |
| sw05-p4 | Q7 | 377600 |
| sw05-p5 | Q6 | 120640 |
| sw05-p5 | Q7 | 199680 |
| sw06-p2 | Q6 | 95360 |
| sw06-p2 | Q7 | 199680 |
| sw06-p3 | Q6 | 130880 |
| sw06-p3 | Q7 | 198720 |
| sw06-p4 | Q6 | 349440 |
| sw06-p4 | Q7 | 377600 |
| sw06-p5 | Q6 | 349440 |
| sw06-p5 | Q7 | 377600 |
| sw07-p3 | Q6 | 118400 |
| sw07-p3 | Q7 | 199680 |
| sw07-p4 | Q6 | 226560 |
| sw07-p4 | Q7 | 234560 |
| sw07-p5 | Q6 | 349440 |
| sw07-p5 | Q7 | 377600 |
| sw08-p2 | Q6 | 45760 |
| sw08-p2 | Q7 | 202560 |
| sw08-p4 | Q6 | 126400 |
| sw08-p4 | Q7 | 200960 |
| sw08-p5 | Q6 | 107200 |
| sw08-p5 | Q7 | 206400 |

## Per-port GCL entries: before (SMT) vs. after (RL-enlarged)

| port | SMT entries | RL-enlarged entries | GCL_size |
|---|---|---|---|
| sw01-p3 | 7 | 12 | 255 |
| sw01-p4 | 9 | 18 | 255 |
| sw01-p5 | 21 | 13 | 255 |
| sw02-p2 | 33 | 21 | 255 |
| sw02-p3 | 3 | 9 | 255 |
| sw02-p4 | 1 | 17 | 255 |
| sw02-p5 | 9 | 21 | 255 |
| sw03-p3 | 5 | 12 | 255 |
| sw03-p4 | 9 | 18 | 255 |
| sw03-p5 | 1 | 17 | 255 |
| sw04-p3 | 1 | 17 | 255 |
| sw04-p4 | 1 | 17 | 255 |
| sw04-p5 | 1 | 17 | 255 |
| sw05-p2 | 9 | 24 | 255 |
| sw05-p3 | 1 | 17 | 255 |
| sw05-p4 | 1 | 17 | 255 |
| sw05-p5 | 13 | 19 | 255 |
| sw06-p2 | 9 | 18 | 255 |
| sw06-p3 | 5 | 12 | 255 |
| sw06-p4 | 1 | 17 | 255 |
| sw06-p5 | 1 | 17 | 255 |
| sw07-p3 | 13 | 19 | 255 |
| sw07-p4 | 9 | 20 | 255 |
| sw07-p5 | 1 | 17 | 255 |
| sw08-p2 | 17 | 17 | 255 |
| sw08-p4 | 5 | 12 | 255 |
| sw08-p5 | 13 | 16 | 255 |

## Flows

| flow | route | fixed | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|---|
| s0(id=1 S3->S1) | S3->sw01->sw02->S1 | yes | 7 | 0 | 8640 | yes |
| s1(id=2 S2->S1) | S2->sw08->sw07->sw05->sw02->S1 | yes | 6 | 0 | 12480 | yes |
| s2(id=3 S3->S2) | S3->sw01->sw03->sw06->sw08->S2 | no | None | None | None | no |
| s3(id=4 S1->S3) | S1->sw02->sw01->S3 | no | None | None | None | no |
| s4(id=5 S2->S1) | S2->sw08->sw07->sw05->sw02->S1 | no | None | None | None | no |
| s5(id=6 S2->S1) | S2->sw08->sw07->sw05->sw02->S1 | yes | 7 | 5440 | 9920 | yes |
| s6(id=7 S2->S1) | S2->sw08->sw07->sw05->sw02->S1 | no | None | None | None | no |
| s7(id=8 S2->S3) | S2->sw08->sw06->sw03->sw01->S3 | yes | 7 | 12480 | 9920 | yes |
| s8(id=9 S3->S2) | S3->sw01->sw03->sw06->sw08->S2 | yes | 7 | 5120 | 13120 | yes |
| s9(id=10 S1->S3) | S1->sw02->sw01->S3 | yes | 7 | 6080 | 5440 | yes |
| s10(id=11 S3->S2) | S3->sw01->sw03->sw06->sw08->S2 | no | None | None | None | no |
| s11(id=12 S2->S1) | S2->sw08->sw07->sw05->sw02->S1 | no | None | None | None | no |
| s12(id=13 S1->S2) | S1->sw02->sw05->sw07->sw08->S2 | no | None | None | None | no |
| s13(id=14 S1->S2) | S1->sw02->sw05->sw07->sw08->S2 | yes | 7 | 0 | 9920 | yes |
| s14(id=15 S2->S3) | S2->sw08->sw06->sw03->sw01->S3 | no | None | None | None | no |
| s15(id=16 S3->S2) | S3->sw01->sw03->sw06->sw08->S2 | no | None | None | None | no |
| s16(id=17 S2->S3) | S2->sw08->sw06->sw03->sw01->S3 | yes | 6 | 14400 | 10880 | yes |
| s17(id=18 S3->S2) | S3->sw01->sw03->sw06->sw08->S2 | no | None | None | None | no |
| s18(id=19 S3->S1) | S3->sw01->sw02->S1 | yes | 7 | 14080 | 8640 | yes |
| s19(id=20 S3->S1) | S3->sw01->sw02->S1 | yes | 7 | 11200 | 6400 | yes |

## Per-hop windows (slack_ns > 0 means this window was enlarged)

| flow | egress port | queue | psi (ns) | delta (ns) |
|---|---|---|---|---|
| s0(id=1 S3->S1) | S3-p0 | Q7 | 0 | 4160 |
| s0(id=1 S3->S1) | sw01-p5 | Q7 | 2240 | 4160 |
| s0(id=1 S3->S1) | sw02-p2 | Q7 | 4480 | 4160 |
| s1(id=2 S2->S1) | S2-p0 | Q6 | 0 | 3520 |
| s1(id=2 S2->S1) | sw08-p5 | Q6 | 2240 | 3520 |
| s1(id=2 S2->S1) | sw07-p3 | Q6 | 4480 | 3520 |
| s1(id=2 S2->S1) | sw05-p5 | Q6 | 6720 | 3520 |
| s1(id=2 S2->S1) | sw02-p2 | Q6 | 8960 | 3520 |
| s5(id=6 S2->S1) | S2-p0 | Q7 | 5440 | 960 |
| s5(id=6 S2->S1) | sw08-p5 | Q7 | 7680 | 960 |
| s5(id=6 S2->S1) | sw07-p3 | Q7 | 9920 | 960 |
| s5(id=6 S2->S1) | sw05-p5 | Q7 | 12160 | 960 |
| s5(id=6 S2->S1) | sw02-p2 | Q7 | 14400 | 960 |
| s7(id=8 S2->S3) | S2-p0 | Q7 | 12480 | 960 |
| s7(id=8 S2->S3) | sw08-p4 | Q7 | 14720 | 960 |
| s7(id=8 S2->S3) | sw06-p3 | Q7 | 16960 | 960 |
| s7(id=8 S2->S3) | sw03-p3 | Q7 | 19200 | 960 |
| s7(id=8 S2->S3) | sw01-p3 | Q7 | 21440 | 960 |
| s8(id=9 S3->S2) | S3-p0 | Q7 | 5120 | 4160 |
| s8(id=9 S3->S2) | sw01-p4 | Q7 | 7360 | 4160 |
| s8(id=9 S3->S2) | sw03-p4 | Q7 | 9600 | 4160 |
| s8(id=9 S3->S2) | sw06-p2 | Q7 | 11840 | 4160 |
| s8(id=9 S3->S2) | sw08-p2 | Q7 | 14080 | 4160 |
| s9(id=10 S1->S3) | S1-p0 | Q7 | 6080 | 960 |
| s9(id=10 S1->S3) | sw02-p3 | Q7 | 8320 | 960 |
| s9(id=10 S1->S3) | sw01-p3 | Q7 | 10560 | 960 |
| s13(id=14 S1->S2) | S1-p0 | Q7 | 0 | 960 |
| s13(id=14 S1->S2) | sw02-p5 | Q7 | 2240 | 960 |
| s13(id=14 S1->S2) | sw05-p2 | Q7 | 4480 | 960 |
| s13(id=14 S1->S2) | sw07-p4 | Q7 | 6720 | 960 |
| s13(id=14 S1->S2) | sw08-p2 | Q7 | 8960 | 960 |
| s16(id=17 S2->S3) | S2-p0 | Q6 | 14400 | 1920 |
| s16(id=17 S2->S3) | sw08-p4 | Q6 | 16640 | 1920 |
| s16(id=17 S2->S3) | sw06-p3 | Q6 | 18880 | 1920 |
| s16(id=17 S2->S3) | sw03-p3 | Q6 | 21120 | 1920 |
| s16(id=17 S2->S3) | sw01-p3 | Q6 | 23360 | 1920 |
| s18(id=19 S3->S1) | S3-p0 | Q7 | 14080 | 4160 |
| s18(id=19 S3->S1) | sw01-p5 | Q7 | 16320 | 4160 |
| s18(id=19 S3->S1) | sw02-p2 | Q7 | 18560 | 4160 |
| s19(id=20 S3->S1) | S3-p0 | Q7 | 11200 | 1920 |
| s19(id=20 S3->S1) | sw01-p5 | Q7 | 13440 | 1920 |
| s19(id=20 S3->S1) | sw02-p2 | Q7 | 15680 | 1920 |

## Metrics (training/evaluation signal, not the export)

| metric | value |
|---|---|
| trial-placed flow ratio (fixed + trial-admitted) | 1.000 |
| r1  same-queue window adjacency | 0.579 |
| r2  deadline-violation ratio | 0.000 |
| r3  supplier/receiver overlap | 0.999 |
| r4  mean e2e/deadline (admitted) | 0.035 |
| constraint violations | 0 |

## Constraint check

- FAIL MINWIN S3-p0: TAS window at 13120 ns is 960 ns < 2633.6283185840707 ns
- FAIL MINWIN S3-p0: TAS window at 413120 ns is 960 ns < 2633.6283185840707 ns

## GCL per egress port

### sw01-p3  (12 entries, util 0.4800 %)

```
sgs 7680 0x7F # 01111111   Q6
sgs 2880 0x40 # 01000000   Q6
sgs 12800 0x80 # 10000000   Q7
sgs 259520 0x40 # 01000000   Q6
sgs 17280 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 252160 0x80 # 10000000   Q7
sgs 32640 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p4  (18 entries, util 2.0800 %)

```
sgs 6400 0x7F # 01111111   Q6
sgs 8960 0x80 # 10000000   Q7
sgs 120000 0x40 # 01000000   Q6
sgs 14720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 6400 0x7F # 01111111   Q6
sgs 128960 0x80 # 10000000   Q7
sgs 14720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 6400 0x7F # 01111111   Q6
sgs 8960 0x80 # 10000000   Q7
sgs 120000 0x40 # 01000000   Q6
sgs 14720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 6400 0x7F # 01111111   Q6
sgs 122560 0x80 # 10000000   Q7
sgs 21120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p5  (13 entries, util 4.0800 %)

```
sgs 2240 0x3F # 00111111   BE
sgs 130240 0x80 # 10000000   Q7
sgs 17600 0x7F # 01111111   Q6
sgs 52160 0xBF # 10111111   Q7
sgs 130240 0x80 # 10000000   Q7
sgs 17600 0x7F # 01111111   Q6
sgs 52160 0xBF # 10111111   Q7
sgs 130240 0x80 # 10000000   Q7
sgs 17600 0x7F # 01111111   Q6
sgs 52160 0xBF # 10111111   Q7
sgs 128000 0x80 # 10000000   Q7
sgs 19840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (21 entries, util 6.0800 %)

```
sgs 4480 0x7F # 01111111   Q6
sgs 4480 0x80 # 10000000   Q7
sgs 3520 0x40 # 01000000   Q6
sgs 15680 0x80 # 10000000   Q7
sgs 138880 0x40 # 01000000   Q6
sgs 32960 0xBF # 10111111   Q7
sgs 4480 0x7F # 01111111   Q6
sgs 4480 0x80 # 10000000   Q7
sgs 6720 0x40 # 01000000   Q6
sgs 151360 0x80 # 10000000   Q7
sgs 32960 0xBF # 10111111   Q7
sgs 4480 0x7F # 01111111   Q6
sgs 4480 0x80 # 10000000   Q7
sgs 3520 0x40 # 01000000   Q6
sgs 154560 0x80 # 10000000   Q7
sgs 32960 0xBF # 10111111   Q7
sgs 4480 0x7F # 01111111   Q6
sgs 4480 0x80 # 10000000   Q7
sgs 6720 0x40 # 01000000   Q6
sgs 146880 0x80 # 10000000   Q7
sgs 37440 0xBF # 10111111   Q7
```

### sw02-p3  (9 entries, util 0.1200 %)

```
sgs 5440 0x7F # 01111111   Q6
sgs 2880 0x40 # 01000000   Q6
sgs 525440 0x80 # 10000000   Q7
sgs 16320 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p4  (17 entries, util 0.0000 %)

```
sgs 36480 0x40 # 01000000   Q6
sgs 36480 0x80 # 10000000   Q7
sgs 27200 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p5  (21 entries, util 0.4800 %)

```
sgs 2240 0x3F # 00111111   BE
sgs 40960 0x80 # 10000000   Q7
sgs 6720 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 52160 0xBF # 10111111   Q7
sgs 40960 0x80 # 10000000   Q7
sgs 6720 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 52160 0xBF # 10111111   Q7
sgs 40960 0x80 # 10000000   Q7
sgs 6720 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 52160 0xBF # 10111111   Q7
sgs 38720 0x80 # 10000000   Q7
sgs 8960 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p3  (12 entries, util 0.3600 %)

```
sgs 13120 0x7F # 01111111   Q6
sgs 8000 0x80 # 10000000   Q7
sgs 232640 0x40 # 01000000   Q6
sgs 46400 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 13120 0x7F # 01111111   Q6
sgs 227520 0x80 # 10000000   Q7
sgs 9280 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (18 entries, util 2.0800 %)

```
sgs 8640 0x7F # 01111111   Q6
sgs 8960 0x80 # 10000000   Q7
sgs 120000 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 8640 0x7F # 01111111   Q6
sgs 128960 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 8640 0x7F # 01111111   Q6
sgs 8960 0x80 # 10000000   Q7
sgs 120000 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 8640 0x7F # 01111111   Q6
sgs 120320 0x80 # 10000000   Q7
sgs 21120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p5  (17 entries, util 0.0000 %)

```
sgs 36480 0x40 # 01000000   Q6
sgs 36480 0x80 # 10000000   Q7
sgs 27200 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p3  (17 entries, util 0.0000 %)

```
sgs 36480 0x40 # 01000000   Q6
sgs 36480 0x80 # 10000000   Q7
sgs 27200 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p4  (17 entries, util 0.0000 %)

```
sgs 36480 0x40 # 01000000   Q6
sgs 36480 0x80 # 10000000   Q7
sgs 27200 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (17 entries, util 0.0000 %)

```
sgs 36480 0x40 # 01000000   Q6
sgs 36480 0x80 # 10000000   Q7
sgs 27200 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p2  (24 entries, util 0.4800 %)

```
sgs 4480 0x7F # 01111111   Q6
sgs 40960 0x80 # 10000000   Q7
sgs 4480 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 4480 0x7F # 01111111   Q6
sgs 40960 0x80 # 10000000   Q7
sgs 4480 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 4480 0x7F # 01111111   Q6
sgs 40960 0x80 # 10000000   Q7
sgs 4480 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 4480 0x7F # 01111111   Q6
sgs 36480 0x80 # 10000000   Q7
sgs 8960 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p3  (17 entries, util 0.0000 %)

```
sgs 36480 0x40 # 01000000   Q6
sgs 36480 0x80 # 10000000   Q7
sgs 27200 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (17 entries, util 0.0000 %)

```
sgs 36480 0x40 # 01000000   Q6
sgs 36480 0x80 # 10000000   Q7
sgs 27200 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p5  (19 entries, util 2.0000 %)

```
sgs 6720 0x7F # 01111111   Q6
sgs 3520 0x40 # 01000000   Q6
sgs 15680 0x80 # 10000000   Q7
sgs 102400 0x40 # 01000000   Q6
sgs 21760 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 6720 0x7F # 01111111   Q6
sgs 121600 0x40 # 01000000   Q6
sgs 21760 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 6720 0x7F # 01111111   Q6
sgs 3520 0x40 # 01000000   Q6
sgs 118080 0x80 # 10000000   Q7
sgs 21760 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 6720 0x7F # 01111111   Q6
sgs 114880 0x40 # 01000000   Q6
sgs 28480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p2  (18 entries, util 2.0800 %)

```
sgs 10880 0x7F # 01111111   Q6
sgs 8960 0x80 # 10000000   Q7
sgs 120000 0x40 # 01000000   Q6
sgs 10240 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 10880 0x7F # 01111111   Q6
sgs 128960 0x80 # 10000000   Q7
sgs 10240 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 10880 0x7F # 01111111   Q6
sgs 8960 0x80 # 10000000   Q7
sgs 120000 0x40 # 01000000   Q6
sgs 10240 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 10880 0x7F # 01111111   Q6
sgs 118080 0x80 # 10000000   Q7
sgs 21120 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p3  (12 entries, util 0.3600 %)

```
sgs 10880 0x7F # 01111111   Q6
sgs 8000 0x80 # 10000000   Q7
sgs 232640 0x40 # 01000000   Q6
sgs 48640 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 10880 0x7F # 01111111   Q6
sgs 229760 0x80 # 10000000   Q7
sgs 9280 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p4  (17 entries, util 0.0000 %)

```
sgs 36480 0x40 # 01000000   Q6
sgs 36480 0x80 # 10000000   Q7
sgs 27200 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (17 entries, util 0.0000 %)

```
sgs 36480 0x40 # 01000000   Q6
sgs 36480 0x80 # 10000000   Q7
sgs 27200 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p3  (19 entries, util 2.0000 %)

```
sgs 4480 0x7F # 01111111   Q6
sgs 3520 0x40 # 01000000   Q6
sgs 13760 0x80 # 10000000   Q7
sgs 104320 0x40 # 01000000   Q6
sgs 24000 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 4480 0x7F # 01111111   Q6
sgs 121600 0x40 # 01000000   Q6
sgs 24000 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 4480 0x7F # 01111111   Q6
sgs 3520 0x40 # 01000000   Q6
sgs 118080 0x80 # 10000000   Q7
sgs 24000 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 4480 0x7F # 01111111   Q6
sgs 117120 0x40 # 01000000   Q6
sgs 28480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (20 entries, util 0.4800 %)

```
sgs 6720 0x7F # 01111111   Q6
sgs 86400 0x80 # 10000000   Q7
sgs 7040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 6720 0x7F # 01111111   Q6
sgs 86400 0x80 # 10000000   Q7
sgs 7040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 6720 0x7F # 01111111   Q6
sgs 86400 0x80 # 10000000   Q7
sgs 7040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 6720 0x7F # 01111111   Q6
sgs 79680 0x80 # 10000000   Q7
sgs 13760 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p5  (17 entries, util 0.0000 %)

```
sgs 36480 0x40 # 01000000   Q6
sgs 36480 0x80 # 10000000   Q7
sgs 27200 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p2  (17 entries, util 2.5600 %)

```
sgs 8960 0x7F # 01111111   Q6
sgs 13120 0x80 # 10000000   Q7
sgs 18560 0x40 # 01000000   Q6
sgs 108480 0x80 # 10000000   Q7
sgs 50880 0xBF # 10111111   Q7
sgs 8960 0x7F # 01111111   Q6
sgs 140160 0x80 # 10000000   Q7
sgs 50880 0xBF # 10111111   Q7
sgs 8960 0x7F # 01111111   Q6
sgs 13120 0x80 # 10000000   Q7
sgs 18560 0x40 # 01000000   Q6
sgs 108480 0x80 # 10000000   Q7
sgs 50880 0xBF # 10111111   Q7
sgs 8960 0x7F # 01111111   Q6
sgs 131200 0x80 # 10000000   Q7
sgs 9920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p4  (12 entries, util 0.3600 %)

```
sgs 8640 0x7F # 01111111   Q6
sgs 8000 0x80 # 10000000   Q7
sgs 232640 0x40 # 01000000   Q6
sgs 50880 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 8640 0x7F # 01111111   Q6
sgs 232000 0x80 # 10000000   Q7
sgs 9280 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (16 entries, util 2.0000 %)

```
sgs 2240 0x3F # 00111111   BE
sgs 3520 0x40 # 01000000   Q6
sgs 11840 0x80 # 10000000   Q7
sgs 106240 0x40 # 01000000   Q6
sgs 26240 0x7F # 01111111   Q6
sgs 52160 0xBF # 10111111   Q7
sgs 121600 0x40 # 01000000   Q6
sgs 26240 0x7F # 01111111   Q6
sgs 52160 0xBF # 10111111   Q7
sgs 3520 0x40 # 01000000   Q6
sgs 118080 0x80 # 10000000   Q7
sgs 26240 0x7F # 01111111   Q6
sgs 52160 0xBF # 10111111   Q7
sgs 119360 0x40 # 01000000   Q6
sgs 28480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

