# Heuristic-enlarged GCL schedule (Problem 2: window enlargement)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Time-sensitive PCPs considered: [6, 7]
- Seeded from SMT run: **result/result-2026-10-09-dataset-testbed-4-avgwin/smt-c9-on/4-fair-retimed-c9on**

## Admission (unchanged by this package -- it only widens windows)

SMT-fixed flows: **11**/11. This package never admits a flow itself; it banks slack for a later admission pass (`prob_3_admit`, Problem 3) to use.

## Opportunistic idle top-up (Step 7 -- see enlarge.py)

Total: **9496320 ns**, drawn from idle capacity on ports at or below utilisation 0.2, independent of any route's deadline-slack budget.

| port | queue | applied (ns) |
|---|---|---|
| S1-p0 | Q6 | 88320 |
| S1-p0 | Q7 | 548480 |
| S2-p0 | Q6 | 125120 |
| S2-p0 | Q7 | 517760 |
| S3-p0 | Q6 | 260800 |
| S3-p0 | Q7 | 383040 |
| sw01-p4 | Q6 | 267200 |
| sw01-p4 | Q7 | 380160 |
| sw02-p2 | Q7 | 615680 |
| sw02-p4 | Q6 | 91520 |
| sw02-p4 | Q7 | 547520 |
| sw03-p5 | Q6 | 272320 |
| sw03-p5 | Q7 | 377920 |
| sw04-p4 | Q7 | 628480 |
| sw04-p5 | Q6 | 93760 |
| sw04-p5 | Q7 | 545600 |
| sw05-p4 | Q6 | 276480 |
| sw05-p4 | Q7 | 375360 |
| sw06-p4 | Q6 | 96000 |
| sw06-p4 | Q7 | 543360 |
| sw06-p5 | Q7 | 640320 |
| sw07-p5 | Q6 | 296640 |
| sw07-p5 | Q7 | 347840 |
| sw08-p2 | Q6 | 208640 |
| sw08-p2 | Q7 | 316800 |
| sw08-p4 | Q7 | 651200 |

## Opportunistic window creation (Step 8 -- see enlarge.py)

**4** brand-new window(s) opened, **49920 ns** total, on ports at or below utilisation 0.2 whose TT queue had zero windows before this run.

| port | queue | size (ns) |
|---|---|---|
| sw02-p2 | Q6 | 12480 |
| sw04-p4 | Q6 | 12480 |
| sw06-p5 | Q6 | 12480 |
| sw08-p4 | Q6 | 12480 |

## Best-effort gap equalization (Step 9 -- see enlarge.py)

**4735040 ns** given back from Steps 7/8's growth so each port's leftover non-TAS gaps land close to equal, instead of one gap staying huge while a neighbour is squeezed to the bare 1-tick C10 minimum.

| port | given back (ns) |
|---|---|
| S3-p0 | 360960 |
| sw01-p4 | 360320 |
| sw03-p5 | 360320 |
| sw05-p4 | 360320 |
| sw07-p5 | 343680 |
| S2-p0 | 336320 |
| sw04-p5 | 320320 |
| sw06-p4 | 320320 |
| sw02-p4 | 319360 |
| S1-p0 | 319360 |
| sw02-p2 | 262400 |
| sw04-p4 | 262400 |
| sw06-p5 | 262400 |
| sw08-p4 | 262400 |
| sw08-p2 | 233600 |
| sw01-p2 | 14720 |
| sw03-p4 | 12160 |
| sw05-p5 | 9280 |
| sw07-p4 | 7680 |
| sw08-p5 | 6720 |

## Opportunistic overlay window creation (Step 10 -- see enlarge.py)

**30** new overlay window(s), **4673920 ns** total, carved out of already-open best-effort spans on ports at or below utilisation 0.2 -- best-effort stays reachable inside each one (gate mask keeps its BE bits set), so none of this is closed off from BE.

| port | queue | size (ns) |
|---|---|---|
| S1-p0 | Q6 | 62400 |
| S1-p0 | Q7 | 212160 |
| S2-p0 | Q6 | 124160 |
| S2-p0 | Q7 | 212160 |
| S3-p0 | Q6 | 161280 |
| S3-p0 | Q7 | 199680 |
| sw01-p4 | Q6 | 97920 |
| sw01-p4 | Q7 | 199680 |
| sw02-p2 | Q6 | 149760 |
| sw02-p2 | Q7 | 191680 |
| sw02-p4 | Q6 | 49920 |
| sw02-p4 | Q7 | 212160 |
| sw03-p5 | Q6 | 85440 |
| sw03-p5 | Q7 | 199680 |
| sw04-p4 | Q6 | 149760 |
| sw04-p4 | Q7 | 187520 |
| sw04-p5 | Q6 | 51200 |
| sw04-p5 | Q7 | 212160 |
| sw05-p4 | Q6 | 124160 |
| sw05-p4 | Q7 | 224640 |
| sw06-p4 | Q6 | 101120 |
| sw06-p4 | Q7 | 208320 |
| sw06-p5 | Q6 | 149760 |
| sw06-p5 | Q7 | 183360 |
| sw07-p5 | Q6 | 128960 |
| sw07-p5 | Q7 | 224640 |
| sw08-p2 | Q6 | 66560 |
| sw08-p2 | Q7 | 174720 |
| sw08-p4 | Q6 | 149760 |
| sw08-p4 | Q7 | 179200 |

## Candidate routes (P^cand = routes of the fixed flows above)

| route | PCPs carried | flows |
|---|---|---|
| S1->sw02->sw04->sw06->sw08->S2 | Q7 (1) | 1 |
| S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | Q6 (1), Q7 (2) | 3 |
| S2->sw08->sw06->sw04->sw02->S1 | Q7 (1) | 1 |
| S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 (1), Q7 (2) | 3 |
| S3->sw01->sw03->sw05->sw07->sw08->S2 | Q6 (2), Q7 (1) | 3 |

## Per-link enlargement accounting

| link | sharing eta | route-safe slack (ns) | link budget (ns) | final slack (ns) | applied (ns) |
|---|---|---|---|---|---|
| S1-p0 | 2 | Q6:55224, Q7:14081 | 69305 | Q6:24390, Q7:14081 | Q6:113920, Q7:516480 |
| S2-p0 | 2 | Q6:44185, Q7:19854 | 64039 | Q6:25259, Q7:19854 | Q6:193280, Q7:494400 |
| sw01-p2 | 2 | Q6:56593, Q7:17718 | 74311 | Q6:33662, Q7:17718 | Q6:33280, Q7:3200 |
| sw02-p4 | 2 | Q6:47036, Q7:11170 | 58207 | Q6:21437, Q7:11170 | Q6:101440, Q7:512320 |
| sw03-p4 | 2 | Q6:46641, Q7:14056 | 60696 | Q6:28069, Q7:14056 | Q6:27520, Q7:1920 |
| sw04-p5 | 2 | Q6:40176, Q7:8862 | 49038 | Q6:18912, Q7:8862 | Q6:102720, Q7:507200 |
| sw05-p5 | 2 | Q6:38439, Q7:11150 | 49589 | Q6:23403, Q7:11150 | Q6:23040, Q7:1920 |
| sw06-p4 | 2 | Q6:34420, Q7:7030 | 41450 | Q6:16747, Q7:7030 | Q6:152640, Q7:499200 |
| sw07-p4 | 2 | Q6:31679, Q7:8846 | 40525 | Q6:19511, Q7:8846 | Q6:18880, Q7:1280 |
| sw08-p2 | 2 | Q6:97426, Q7:25120 | 122547 | Q6:83212, Q7:25120 | Q6:233600, Q7:407680 |
| sw08-p5 | 2 | Q6:26108, Q7:7724 | 33832 | Q6:15801, Q7:7724 | Q6:15360, Q7:1280 |
| S3-p0 | 1 | Q6:39535, Q7:17258 | 56793 | Q6:39535, Q7:17258 | Q6:280960, Q7:419200 |
| sw01-p4 | 1 | Q6:33729, Q7:15017 | 48746 | Q6:33729, Q7:15017 | Q6:218240, Q7:414720 |
| sw02-p2 | 1 | Q6:0, Q7:80606 | 80606 | Q7:80606 | Q6:162240, Q7:625280 |
| sw03-p5 | 1 | Q6:28776, Q7:13066 | 41842 | Q6:28776, Q7:13066 | Q6:205760, Q7:410560 |
| sw04-p4 | 1 | Q6:0, Q7:71954 | 71954 | Q7:71954 | Q6:162240, Q7:625280 |
| sw05-p4 | 1 | Q6:24550, Q7:11369 | 35919 | Q6:24550, Q7:11369 | Q6:244480, Q7:431360 |
| sw06-p5 | 1 | Q6:0, Q7:64230 | 64230 | Q7:64230 | Q6:162240, Q7:625280 |
| sw07-p5 | 1 | Q6:20945, Q7:9893 | 30837 | Q6:20945, Q7:9893 | Q6:265920, Q7:418880 |
| sw08-p4 | 1 | Q6:0, Q7:57336 | 57336 | Q7:57336 | Q6:162240, Q7:625280 |

Total applied: **10422720 ns** across 20 port(s). Network total slack now banked: **10451520 ns**. GCL_size overflow: 0.

## Per-port GCL entries: before (SMT) vs. after (heuristic-enlarged)

| port | SMT entries | enlarged entries | GCL_size |
|---|---|---|---|
| sw01-p2 | 29 | 25 | 255 |
| sw01-p4 | 17 | 24 | 255 |
| sw02-p2 | 3 | 10 | 255 |
| sw02-p4 | 21 | 28 | 255 |
| sw03-p4 | 29 | 25 | 255 |
| sw03-p5 | 17 | 24 | 255 |
| sw04-p4 | 3 | 10 | 255 |
| sw04-p5 | 21 | 26 | 255 |
| sw05-p4 | 17 | 24 | 255 |
| sw05-p5 | 29 | 25 | 255 |
| sw06-p4 | 21 | 23 | 255 |
| sw06-p5 | 3 | 10 | 255 |
| sw07-p4 | 29 | 25 | 255 |
| sw07-p5 | 17 | 24 | 255 |
| sw08-p2 | 25 | 20 | 255 |
| sw08-p4 | 3 | 10 | 255 |
| sw08-p5 | 29 | 25 | 255 |

## Flows

| flow | route | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|
| s0(id=1 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 6 | 24960 | 33360 | yes |
| s1(id=2 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | - | - | - | no |
| s2(id=3 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 7 | 24960 | 33360 | yes |
| s3(id=4 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | - | - | - | no |
| s4(id=5 S3->S1) | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | - | - | - | no |
| s5(id=6 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | 7 | 49920 | 46800 | yes |
| s6(id=7 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | - | - | - | no |
| s7(id=8 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 7 | 0 | 33360 | yes |
| s8(id=9 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | 6 | 74880 | 45840 | yes |
| s9(id=10 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 6 | 49920 | 33360 | yes |
| s10(id=11 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | - | - | - | no |
| s11(id=12 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | - | - | - | no |
| s12(id=13 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 7 | 0 | 29200 | yes |
| s13(id=14 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 7 | 0 | 42000 | yes |
| s14(id=15 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | - | - | - | no |
| s15(id=16 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | - | - | - | no |
| s16(id=17 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | - | - | - | no |
| s17(id=18 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | 7 | 74880 | 29200 | yes |
| s18(id=19 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 6 | 49920 | 34000 | yes |
| s19(id=20 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | 7 | 24960 | 46160 | yes |

## Per-hop windows (slack_ns > 0 means this window was enlarged)

| flow | egress port | queue | psi (ns) | delta (ns) |
|---|---|---|---|---|
| s0(id=1 S3->S2) | S3-p0 | Q6 | 24960 | 12480 |
| s0(id=1 S3->S2) | sw01-p4 | Q6 | 29120 | 12480 |
| s0(id=1 S3->S2) | sw03-p5 | Q6 | 33280 | 12480 |
| s0(id=1 S3->S2) | sw05-p4 | Q6 | 37440 | 12480 |
| s0(id=1 S3->S2) | sw07-p5 | Q6 | 41600 | 12480 |
| s0(id=1 S3->S2) | sw08-p2 | Q6 | 45760 | 12480 |
| s2(id=3 S2->S3) | S2-p0 | Q7 | 24960 | 12480 |
| s2(id=3 S2->S3) | sw08-p5 | Q7 | 29120 | 12480 |
| s2(id=3 S2->S3) | sw07-p4 | Q7 | 33280 | 12480 |
| s2(id=3 S2->S3) | sw05-p5 | Q7 | 37440 | 12480 |
| s2(id=3 S2->S3) | sw03-p4 | Q7 | 41600 | 12480 |
| s2(id=3 S2->S3) | sw01-p2 | Q7 | 45760 | 12480 |
| s5(id=6 S1->S3) | S1-p0 | Q7 | 49920 | 12480 |
| s5(id=6 S1->S3) | sw02-p4 | Q7 | 54080 | 12480 |
| s5(id=6 S1->S3) | sw04-p5 | Q7 | 58240 | 12480 |
| s5(id=6 S1->S3) | sw06-p4 | Q7 | 62400 | 12480 |
| s5(id=6 S1->S3) | sw08-p5 | Q7 | 67520 | 12480 |
| s5(id=6 S1->S3) | sw07-p4 | Q7 | 71680 | 12480 |
| s5(id=6 S1->S3) | sw05-p5 | Q7 | 75840 | 12480 |
| s5(id=6 S1->S3) | sw03-p4 | Q7 | 80000 | 12480 |
| s5(id=6 S1->S3) | sw01-p2 | Q7 | 84160 | 12480 |
| s7(id=8 S2->S3) | S2-p0 | Q7 | 0 | 12480 |
| s7(id=8 S2->S3) | sw08-p5 | Q7 | 4160 | 12480 |
| s7(id=8 S2->S3) | sw07-p4 | Q7 | 8320 | 12480 |
| s7(id=8 S2->S3) | sw05-p5 | Q7 | 12480 | 12480 |
| s7(id=8 S2->S3) | sw03-p4 | Q7 | 16640 | 12480 |
| s7(id=8 S2->S3) | sw01-p2 | Q7 | 20800 | 12480 |
| s8(id=9 S1->S3) | S1-p0 | Q6 | 74880 | 12480 |
| s8(id=9 S1->S3) | sw02-p4 | Q6 | 79040 | 12480 |
| s8(id=9 S1->S3) | sw04-p5 | Q6 | 83200 | 12480 |
| s8(id=9 S1->S3) | sw06-p4 | Q6 | 87360 | 12480 |
| s8(id=9 S1->S3) | sw08-p5 | Q6 | 91520 | 12480 |
| s8(id=9 S1->S3) | sw07-p4 | Q6 | 95680 | 12480 |
| s8(id=9 S1->S3) | sw05-p5 | Q6 | 99840 | 12480 |
| s8(id=9 S1->S3) | sw03-p4 | Q6 | 104000 | 12480 |
| s8(id=9 S1->S3) | sw01-p2 | Q6 | 108160 | 12480 |
| s9(id=10 S3->S2) | S3-p0 | Q6 | 49920 | 12480 |
| s9(id=10 S3->S2) | sw01-p4 | Q6 | 54080 | 12480 |
| s9(id=10 S3->S2) | sw03-p5 | Q6 | 58240 | 12480 |
| s9(id=10 S3->S2) | sw05-p4 | Q6 | 62400 | 12480 |
| s9(id=10 S3->S2) | sw07-p5 | Q6 | 66560 | 12480 |
| s9(id=10 S3->S2) | sw08-p2 | Q6 | 70720 | 12480 |
| s12(id=13 S1->S2) | S1-p0 | Q7 | 0 | 12480 |
| s12(id=13 S1->S2) | sw02-p4 | Q7 | 4160 | 12480 |
| s12(id=13 S1->S2) | sw04-p5 | Q7 | 8320 | 12480 |
| s12(id=13 S1->S2) | sw06-p4 | Q7 | 12480 | 12480 |
| s12(id=13 S1->S2) | sw08-p2 | Q7 | 16640 | 12480 |
| s13(id=14 S3->S2) | S3-p0 | Q7 | 0 | 12480 |
| s13(id=14 S3->S2) | sw01-p4 | Q7 | 4480 | 12480 |
| s13(id=14 S3->S2) | sw03-p5 | Q7 | 8640 | 12480 |
| s13(id=14 S3->S2) | sw05-p4 | Q7 | 12800 | 12480 |
| s13(id=14 S3->S2) | sw07-p5 | Q7 | 25280 | 12480 |
| s13(id=14 S3->S2) | sw08-p2 | Q7 | 29440 | 12480 |
| s17(id=18 S2->S1) | S2-p0 | Q7 | 74880 | 12480 |
| s17(id=18 S2->S1) | sw08-p4 | Q7 | 79040 | 12480 |
| s17(id=18 S2->S1) | sw06-p5 | Q7 | 83200 | 12480 |
| s17(id=18 S2->S1) | sw04-p4 | Q7 | 87360 | 12480 |
| s17(id=18 S2->S1) | sw02-p2 | Q7 | 91520 | 12480 |
| s18(id=19 S2->S3) | S2-p0 | Q6 | 49920 | 12480 |
| s18(id=19 S2->S3) | sw08-p5 | Q6 | 54720 | 12480 |
| s18(id=19 S2->S3) | sw07-p4 | Q6 | 58880 | 12480 |
| s18(id=19 S2->S3) | sw05-p5 | Q6 | 63040 | 12480 |
| s18(id=19 S2->S3) | sw03-p4 | Q6 | 67200 | 12480 |
| s18(id=19 S2->S3) | sw01-p2 | Q6 | 71360 | 12480 |
| s19(id=20 S1->S3) | S1-p0 | Q7 | 24960 | 12480 |
| s19(id=20 S1->S3) | sw02-p4 | Q7 | 29120 | 12480 |
| s19(id=20 S1->S3) | sw04-p5 | Q7 | 33600 | 12480 |
| s19(id=20 S1->S3) | sw06-p4 | Q7 | 37760 | 12480 |
| s19(id=20 S1->S3) | sw08-p5 | Q7 | 41920 | 12480 |
| s19(id=20 S1->S3) | sw07-p4 | Q7 | 46080 | 12480 |
| s19(id=20 S1->S3) | sw05-p5 | Q7 | 50240 | 12480 |
| s19(id=20 S1->S3) | sw03-p4 | Q7 | 54400 | 12480 |
| s19(id=20 S1->S3) | sw01-p2 | Q7 | 58560 | 12480 |

## Constraint check

- C1-C7, C9: OK
- seed-integrity (no SMT-fixed flow's placement changed): OK

## GCL per egress port

### sw01-p2  (25 entries, util 21.8400 %)

```
sgs 20800 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 11520 0x3F # 00111111   BE
sgs 34560 0x40 # 01000000   Q6
sgs 78080 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0x3F # 00111111   BE
sgs 14080 0x80 # 10000000   Q7
sgs 148160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 23680 0x40 # 01000000   Q6
sgs 125760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0x3F # 00111111   BE
sgs 14080 0x80 # 10000000   Q7
sgs 127360 0x3F # 00111111   BE
```

### sw01-p4  (24 entries, util 12.4800 %)

```
sgs 4480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 72640 0x40 # 01000000   Q6
sgs 23360 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 4480 0x3F # 00111111   BE
sgs 122240 0x80 # 10000000   Q7
sgs 23360 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 4480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 72640 0x40 # 01000000   Q6
sgs 23360 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 4480 0x3F # 00111111   BE
sgs 117760 0x80 # 10000000   Q7
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (10 entries, util 1.5600 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 446080 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p4  (28 entries, util 15.6000 %)

```
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 64000 0x40 # 01000000   Q6
sgs 7040 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 113920 0x80 # 10000000   Q7
sgs 7040 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 113920 0x80 # 10000000   Q7
sgs 7040 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 109760 0x80 # 10000000   Q7
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (25 entries, util 21.8400 %)

```
sgs 16640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 11520 0x3F # 00111111   BE
sgs 30720 0x40 # 01000000   Q6
sgs 81920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0x3F # 00111111   BE
sgs 13440 0x80 # 10000000   Q7
sgs 148800 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 21760 0x40 # 01000000   Q6
sgs 127680 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0x3F # 00111111   BE
sgs 13440 0x80 # 10000000   Q7
sgs 132160 0x3F # 00111111   BE
```

### sw03-p5  (24 entries, util 12.4800 %)

```
sgs 8640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 72640 0x40 # 01000000   Q6
sgs 19200 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 8640 0x3F # 00111111   BE
sgs 122240 0x80 # 10000000   Q7
sgs 19200 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 8640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 72640 0x40 # 01000000   Q6
sgs 19200 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 8640 0x3F # 00111111   BE
sgs 113600 0x80 # 10000000   Q7
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p4  (10 entries, util 1.5600 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 37440 0xBF # 10111111   Q7
sgs 450240 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (26 entries, util 15.6000 %)

```
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0x7F # 01111111   Q6
sgs 37120 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 64000 0x40 # 01000000   Q6
sgs 2880 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0x7F # 01111111   Q6
sgs 113600 0x80 # 10000000   Q7
sgs 2880 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0x7F # 01111111   Q6
sgs 113600 0x80 # 10000000   Q7
sgs 2880 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0x7F # 01111111   Q6
sgs 105280 0x80 # 10000000   Q7
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (24 entries, util 12.4800 %)

```
sgs 12800 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 72640 0x40 # 01000000   Q6
sgs 15040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 12800 0x7F # 01111111   Q6
sgs 122240 0x80 # 10000000   Q7
sgs 15040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 12800 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 72640 0x40 # 01000000   Q6
sgs 15040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 12800 0x7F # 01111111   Q6
sgs 109440 0x80 # 10000000   Q7
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p5  (25 entries, util 21.8400 %)

```
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 11520 0x3F # 00111111   BE
sgs 27840 0x40 # 01000000   Q6
sgs 84800 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0x3F # 00111111   BE
sgs 13440 0x80 # 10000000   Q7
sgs 148800 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 20160 0x40 # 01000000   Q6
sgs 129280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0x3F # 00111111   BE
sgs 13440 0x80 # 10000000   Q7
sgs 136320 0x3F # 00111111   BE
```

### sw06-p4  (23 entries, util 15.6000 %)

```
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0x7F # 01111111   Q6
sgs 37120 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 64000 0x40 # 01000000   Q6
sgs 48640 0xBF # 10111111   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0x7F # 01111111   Q6
sgs 113600 0x80 # 10000000   Q7
sgs 48640 0xBF # 10111111   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0x7F # 01111111   Q6
sgs 113600 0x80 # 10000000   Q7
sgs 48640 0xBF # 10111111   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0x7F # 01111111   Q6
sgs 101120 0x80 # 10000000   Q7
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (10 entries, util 1.5600 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 454400 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (25 entries, util 21.8400 %)

```
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 11520 0x3F # 00111111   BE
sgs 24960 0x40 # 01000000   Q6
sgs 87680 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0x3F # 00111111   BE
sgs 13120 0x80 # 10000000   Q7
sgs 149120 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 18880 0x40 # 01000000   Q6
sgs 130560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0x3F # 00111111   BE
sgs 13120 0x80 # 10000000   Q7
sgs 140800 0x3F # 00111111   BE
```

### sw07-p5  (24 entries, util 12.4800 %)

```
sgs 25280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 3840 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 80960 0x40 # 01000000   Q6
sgs 2560 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 25280 0x7F # 01111111   Q6
sgs 122240 0x80 # 10000000   Q7
sgs 2560 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 25280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 3840 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 80960 0x40 # 01000000   Q6
sgs 2560 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 25280 0x7F # 01111111   Q6
sgs 96960 0x80 # 10000000   Q7
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p2  (20 entries, util 18.7200 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 25280 0x80 # 10000000   Q7
sgs 3840 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 96000 0x40 # 01000000   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 150080 0x80 # 10000000   Q7
sgs 33280 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 25280 0x80 # 10000000   Q7
sgs 3840 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 96000 0x40 # 01000000   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 133440 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p4  (10 entries, util 1.5600 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 458560 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (25 entries, util 21.8400 %)

```
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 11520 0x3F # 00111111   BE
sgs 22720 0x40 # 01000000   Q6
sgs 89920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0x3F # 00111111   BE
sgs 13120 0x80 # 10000000   Q7
sgs 149120 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 17600 0x40 # 01000000   Q6
sgs 131840 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0x3F # 00111111   BE
sgs 13120 0x80 # 10000000   Q7
sgs 144960 0x3F # 00111111   BE
```

