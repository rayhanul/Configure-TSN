# Heuristic-enlarged GCL schedule (Problem 2: window enlargement)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Time-sensitive PCPs considered: [6, 7]
- Seeded from SMT run: **result/result-2026-10-09-dataset-testbed-4-avgwin/smt-c9-off/4-t3600-c9off-minlat**

## Admission (unchanged by this package -- it only widens windows)

SMT-fixed flows: **11**/20. This package never admits a flow itself; it banks slack for a later admission pass (`prob_3_admit`, Problem 3) to use.

## Opportunistic idle top-up (Step 7 -- see enlarge.py)

Total: **9308800 ns**, drawn from idle capacity on ports at or below utilisation 0.2, independent of any route's deadline-slack budget.

| port | queue | applied (ns) |
|---|---|---|
| S1-p0 | Q6 | 670080 |
| S2-p0 | Q6 | 501120 |
| S2-p0 | Q7 | 135360 |
| S3-p0 | Q6 | 389120 |
| S3-p0 | Q7 | 267520 |
| sw01-p4 | Q6 | 374080 |
| sw01-p4 | Q7 | 272320 |
| sw02-p2 | Q6 | 568320 |
| sw02-p4 | Q6 | 654400 |
| sw03-p5 | Q6 | 358400 |
| sw03-p5 | Q7 | 276480 |
| sw04-p4 | Q6 | 593280 |
| sw04-p5 | Q6 | 638720 |
| sw05-p4 | Q6 | 343040 |
| sw05-p4 | Q7 | 280000 |
| sw06-p4 | Q6 | 622720 |
| sw06-p5 | Q6 | 617600 |
| sw07-p5 | Q6 | 327360 |
| sw07-p5 | Q7 | 282880 |
| sw08-p2 | Q6 | 297280 |
| sw08-p2 | Q7 | 197440 |
| sw08-p4 | Q6 | 641280 |

## Opportunistic window creation (Step 8 -- see enlarge.py)

**7** brand-new window(s) opened, **87360 ns** total, on ports at or below utilisation 0.2 whose TT queue had zero windows before this run.

| port | queue | size (ns) |
|---|---|---|
| sw02-p2 | Q7 | 12480 |
| sw02-p4 | Q7 | 12480 |
| sw04-p4 | Q7 | 12480 |
| sw04-p5 | Q7 | 12480 |
| sw06-p4 | Q7 | 12480 |
| sw06-p5 | Q7 | 12480 |
| sw08-p4 | Q7 | 12480 |

## Best-effort gap equalization (Step 9 -- see enlarge.py)

**4814080 ns** given back from Steps 7/8's growth so each port's leftover non-TAS gaps land close to equal, instead of one gap staying huge while a neighbour is squeezed to the bare 1-tick C10 minimum.

| port | given back (ns) |
|---|---|
| sw01-p4 | 360960 |
| sw03-p5 | 360960 |
| sw05-p4 | 360960 |
| sw07-p5 | 360960 |
| S3-p0 | 360960 |
| S2-p0 | 336320 |
| S1-p0 | 319360 |
| sw02-p4 | 298880 |
| sw04-p5 | 298880 |
| sw06-p4 | 298880 |
| sw08-p2 | 266240 |
| sw02-p2 | 262400 |
| sw04-p4 | 262400 |
| sw06-p5 | 262400 |
| sw08-p4 | 262400 |
| sw01-p2 | 39680 |
| sw03-p4 | 32320 |
| sw05-p5 | 26240 |
| sw07-p4 | 23360 |
| sw08-p5 | 19520 |

## Opportunistic overlay window creation (Step 10 -- see enlarge.py)

**30** new overlay window(s), **5094720 ns** total, carved out of already-open best-effort spans on ports at or below utilisation 0.2 -- best-effort stays reachable inside each one (gate mask keeps its BE bits set), so none of this is closed off from BE.

| port | queue | size (ns) |
|---|---|---|
| S1-p0 | Q6 | 62400 |
| S1-p0 | Q7 | 212160 |
| S2-p0 | Q6 | 124160 |
| S2-p0 | Q7 | 212160 |
| S3-p0 | Q6 | 161280 |
| S3-p0 | Q7 | 199680 |
| sw01-p4 | Q6 | 119360 |
| sw01-p4 | Q7 | 224640 |
| sw02-p2 | Q6 | 191040 |
| sw02-p2 | Q7 | 200320 |
| sw02-p4 | Q6 | 99840 |
| sw02-p4 | Q7 | 192960 |
| sw03-p5 | Q6 | 160960 |
| sw03-p5 | Q7 | 208320 |
| sw04-p4 | Q6 | 174400 |
| sw04-p4 | Q7 | 200320 |
| sw04-p5 | Q6 | 120640 |
| sw04-p5 | Q7 | 130560 |
| sw05-p4 | Q6 | 227520 |
| sw05-p4 | Q7 | 183360 |
| sw06-p4 | Q6 | 199680 |
| sw06-p4 | Q7 | 112320 |
| sw06-p5 | Q6 | 149760 |
| sw06-p5 | Q7 | 200320 |
| sw07-p5 | Q6 | 252480 |
| sw07-p5 | Q7 | 141440 |
| sw08-p2 | Q6 | 174720 |
| sw08-p2 | Q7 | 116480 |
| sw08-p4 | Q6 | 149760 |
| sw08-p4 | Q7 | 191680 |

## Candidate routes (P^cand = routes of the fixed flows above)

| route | PCPs carried | flows |
|---|---|---|
| S1->sw02->sw04->sw06->sw08->S2 | Q6 (1) | 1 |
| S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | Q6 (3) | 3 |
| S2->sw08->sw06->sw04->sw02->S1 | Q6 (1) | 1 |
| S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 (1), Q7 (2) | 3 |
| S3->sw01->sw03->sw05->sw07->sw08->S2 | Q6 (1), Q7 (2) | 3 |

## Per-link enlargement accounting

| link | sharing eta | route-safe slack (ns) | link budget (ns) | final slack (ns) | applied (ns) |
|---|---|---|---|---|---|
| S1-p0 | 2 | Q6:5263, Q7:0 | 5263 | Q6:5263 | Q6:418240, Q7:212160 |
| S2-p0 | 2 | Q6:11665, Q7:41801 | 53467 | Q6:11665, Q7:39984 | Q6:406400, Q7:281280 |
| sw01-p2 | 2 | Q6:6009, Q7:45276 | 51285 | Q6:6009, Q7:35830 | Q6:1600 |
| sw02-p4 | 2 | Q6:4171, Q7:0 | 4171 | Q6:4171 | Q6:459520, Q7:205440 |
| sw03-p4 | 2 | Q6:4762, Q7:37465 | 42227 | Q6:4762, Q7:29882 | Q6:1920 |
| sw04-p5 | 2 | Q6:3305, Q7:0 | 3305 | Q6:3305 | Q6:463680, Q7:143040 |
| sw05-p5 | 2 | Q6:3774, Q7:31002 | 34776 | Q6:3774, Q7:24917 | Q6:1920 |
| sw06-p4 | 2 | Q6:2619, Q7:0 | 2619 | Q6:2619 | Q6:526080, Q7:124800 |
| sw07-p4 | 2 | Q6:2991, Q7:25653 | 28644 | Q6:2991, Q7:20773 | - |
| sw08-p2 | 2 | Q6:19625, Q7:80845 | 100470 | Q6:19625, Q7:69527 | Q6:350080, Q7:258560 |
| sw08-p5 | 2 | Q6:2625, Q7:21227 | 23852 | Q6:2625, Q7:17015 | - |
| S3-p0 | 1 | Q6:10989, Q7:32807 | 43796 | Q6:10989, Q7:32807 | Q6:380800, Q7:319360 |
| sw01-p4 | 1 | Q6:9562, Q7:27989 | 37551 | Q6:9562, Q7:27989 | Q6:322240, Q7:344320 |
| sw02-p2 | 1 | Q6:78041, Q7:0 | 78041 | Q6:78041 | Q6:574720, Q7:212800 |
| sw03-p5 | 1 | Q6:8320, Q7:23879 | 32199 | Q6:8320, Q7:23879 | Q6:347200, Q7:328000 |
| sw04-p4 | 1 | Q6:69453, Q7:0 | 69453 | Q6:69453 | Q6:574720, Q7:212800 |
| sw05-p4 | 1 | Q6:7240, Q7:20372 | 27612 | Q6:7240, Q7:20372 | Q6:397120, Q7:303040 |
| sw06-p5 | 1 | Q6:61811, Q7:0 | 61811 | Q6:61811 | Q6:566720, Q7:212800 |
| sw07-p5 | 1 | Q6:6299, Q7:17380 | 23680 | Q6:6299, Q7:17380 | Q6:405440, Q7:261120 |
| sw08-p4 | 1 | Q6:55009, Q7:0 | 55009 | Q6:55009 | Q6:583360, Q7:204160 |

Total applied: **10405440 ns** across 18 port(s). Network total slack now banked: **10422080 ns**. GCL_size overflow: 0.

## Per-port GCL entries: before (SMT) vs. after (heuristic-enlarged)

| port | SMT entries | enlarged entries | GCL_size |
|---|---|---|---|
| sw01-p2 | 29 | 29 | 255 |
| sw01-p4 | 17 | 24 | 255 |
| sw02-p2 | 3 | 11 | 255 |
| sw02-p4 | 21 | 26 | 255 |
| sw03-p4 | 29 | 29 | 255 |
| sw03-p5 | 17 | 21 | 255 |
| sw04-p4 | 3 | 11 | 255 |
| sw04-p5 | 21 | 26 | 255 |
| sw05-p4 | 17 | 21 | 255 |
| sw05-p5 | 29 | 29 | 255 |
| sw06-p4 | 21 | 26 | 255 |
| sw06-p5 | 3 | 11 | 255 |
| sw07-p4 | 29 | 29 | 255 |
| sw07-p5 | 17 | 25 | 255 |
| sw08-p2 | 25 | 21 | 255 |
| sw08-p4 | 3 | 10 | 255 |
| sw08-p5 | 29 | 29 | 255 |

## Flows

| flow | route | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|
| s0(id=1 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 7 | 24960 | 95760 | yes |
| s1(id=2 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | - | - | - | no |
| s2(id=3 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 7 | 24960 | 95760 | yes |
| s3(id=4 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | - | - | - | no |
| s4(id=5 S3->S1) | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | - | - | - | no |
| s5(id=6 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | 6 | 49920 | 145680 | yes |
| s6(id=7 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | - | - | - | no |
| s7(id=8 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 6 | 0 | 95760 | yes |
| s8(id=9 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | 6 | 74880 | 145680 | yes |
| s9(id=10 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 7 | 49920 | 95760 | yes |
| s10(id=11 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | - | - | - | no |
| s11(id=12 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | - | - | - | no |
| s12(id=13 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 6 | 0 | 79120 | yes |
| s13(id=14 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 6 | 0 | 95760 | yes |
| s14(id=15 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | - | - | - | no |
| s15(id=16 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | - | - | - | no |
| s16(id=17 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | - | - | - | no |
| s17(id=18 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | 6 | 74880 | 79120 | yes |
| s18(id=19 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 7 | 49920 | 95760 | yes |
| s19(id=20 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | 6 | 24960 | 145680 | yes |

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

## Constraint check

- C1-C7, C9: OK
- seed-integrity (no SMT-fixed flow's placement changed): OK

## GCL per egress port

### sw01-p2  (29 entries, util 21.8400 %)

```
sgs 83200 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12800 0x40 # 01000000   Q6
sgs 62400 0x3F # 00111111   BE
sgs 12800 0x40 # 01000000   Q6
sgs 62080 0x3F # 00111111   BE
sgs 12800 0x40 # 01000000   Q6
sgs 112320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12800 0x40 # 01000000   Q6
sgs 112320 0x3F # 00111111   BE
sgs 12800 0x40 # 01000000   Q6
sgs 62080 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 29440 0x3F # 00111111   BE
```

### sw01-p4  (24 entries, util 12.4800 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 72320 0x80 # 10000000   Q7
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 122240 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 72320 0x80 # 10000000   Q7
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 105600 0x40 # 01000000   Q6
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (11 entries, util 1.5600 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 41280 0x7F # 01111111   Q6
sgs 396160 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p4  (26 entries, util 15.6000 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 69120 0x40 # 01000000   Q6
sgs 39360 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 119040 0x40 # 01000000   Q6
sgs 39360 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 119040 0x40 # 01000000   Q6
sgs 39360 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 102400 0x40 # 01000000   Q6
sgs 6080 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (29 entries, util 21.8400 %)

```
sgs 66560 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12800 0x40 # 01000000   Q6
sgs 62400 0x3F # 00111111   BE
sgs 12800 0x40 # 01000000   Q6
sgs 62080 0x3F # 00111111   BE
sgs 12800 0x40 # 01000000   Q6
sgs 112320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12800 0x40 # 01000000   Q6
sgs 112320 0x3F # 00111111   BE
sgs 12800 0x40 # 01000000   Q6
sgs 62080 0x3F # 00111111   BE
sgs 12800 0x40 # 01000000   Q6
sgs 45760 0x3F # 00111111   BE
```

### sw03-p5  (21 entries, util 12.4800 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 72320 0x80 # 10000000   Q7
sgs 44480 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 122240 0x40 # 01000000   Q6
sgs 44480 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 72320 0x80 # 10000000   Q7
sgs 44480 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 88960 0x40 # 01000000   Q6
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p4  (11 entries, util 1.5600 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 24640 0x7F # 01111111   Q6
sgs 412800 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (26 entries, util 15.6000 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 69120 0x40 # 01000000   Q6
sgs 22720 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 119040 0x40 # 01000000   Q6
sgs 22720 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 119040 0x40 # 01000000   Q6
sgs 22720 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 85760 0x40 # 01000000   Q6
sgs 6080 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (21 entries, util 12.4800 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 72320 0x80 # 10000000   Q7
sgs 27840 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 122240 0x40 # 01000000   Q6
sgs 27840 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 72320 0x80 # 10000000   Q7
sgs 27840 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 72320 0x40 # 01000000   Q6
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p5  (29 entries, util 21.8400 %)

```
sgs 49920 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12800 0x40 # 01000000   Q6
sgs 62400 0x3F # 00111111   BE
sgs 12800 0x40 # 01000000   Q6
sgs 62080 0x3F # 00111111   BE
sgs 12800 0x40 # 01000000   Q6
sgs 112320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12800 0x40 # 01000000   Q6
sgs 112320 0x3F # 00111111   BE
sgs 12800 0x40 # 01000000   Q6
sgs 62080 0x3F # 00111111   BE
sgs 12800 0x40 # 01000000   Q6
sgs 62400 0x3F # 00111111   BE
```

### sw06-p4  (26 entries, util 15.6000 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 69120 0x40 # 01000000   Q6
sgs 6080 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 119040 0x40 # 01000000   Q6
sgs 6080 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 119040 0x40 # 01000000   Q6
sgs 6080 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 69120 0x40 # 01000000   Q6
sgs 6080 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (11 entries, util 1.5600 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 8000 0x3F # 00111111   BE
sgs 429440 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (29 entries, util 21.8400 %)

```
sgs 33280 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 62720 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 62400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 112640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 112640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 62400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 79360 0x3F # 00111111   BE
```

### sw07-p5  (25 entries, util 12.4800 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 72320 0x80 # 10000000   Q7
sgs 11200 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 122240 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 72320 0x80 # 10000000   Q7
sgs 11200 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 55680 0x40 # 01000000   Q6
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p2  (21 entries, util 18.7200 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 29120 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 83520 0x80 # 10000000   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 150080 0x40 # 01000000   Q6
sgs 33280 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 29120 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 83520 0x80 # 10000000   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 83520 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p4  (10 entries, util 1.5600 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 446080 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (29 entries, util 21.8400 %)

```
sgs 16640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 62720 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 62400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 112640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 112640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 62400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 96000 0x3F # 00111111   BE
```

