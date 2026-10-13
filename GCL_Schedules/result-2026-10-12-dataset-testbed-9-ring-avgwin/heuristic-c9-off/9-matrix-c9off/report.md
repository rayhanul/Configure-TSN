# Heuristic-enlarged GCL schedule (Problem 2: window enlargement)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Time-sensitive PCPs considered: [6, 7]
- Seeded from SMT run: **result/result-2026-10-12-dataset-testbed-9-ring-avgwin/smt-c9-off/9-t3600-c9off-minlat**

## Admission (unchanged by this package -- it only widens windows)

SMT-fixed flows: **11**/20. This package never admits a flow itself; it banks slack for a later admission pass (`prob_3_admit`, Problem 3) to use.

## Opportunistic idle top-up (Step 7 -- see enlarge.py)

Total: **13785920 ns**, drawn from idle capacity on ports at or below utilisation 0.2, independent of any route's deadline-slack budget.

| port | queue | applied (ns) |
|---|---|---|
| S1-p0 | Q6 | 525760 |
| S1-p0 | Q7 | 31680 |
| S2-p0 | Q7 | 535040 |
| S3-p0 | Q7 | 628480 |
| sw01-p2 | Q6 | 165760 |
| sw01-p2 | Q7 | 431040 |
| sw01-p4 | Q7 | 632640 |
| sw01-p5 | Q6 | 93120 |
| sw01-p5 | Q7 | 534400 |
| sw02-p2 | Q7 | 485440 |
| sw02-p4 | Q7 | 685440 |
| sw02-p5 | Q6 | 722240 |
| sw03-p4 | Q6 | 77760 |
| sw03-p4 | Q7 | 552640 |
| sw03-p5 | Q7 | 620480 |
| sw04-p4 | Q6 | 291840 |
| sw04-p4 | Q7 | 322240 |
| sw04-p5 | Q7 | 676800 |
| sw05-p4 | Q7 | 608000 |
| sw05-p5 | Q6 | 80960 |
| sw05-p5 | Q7 | 569920 |
| sw06-p4 | Q7 | 667200 |
| sw06-p5 | Q6 | 294400 |
| sw06-p5 | Q7 | 342400 |
| sw07-p4 | Q6 | 84160 |
| sw07-p4 | Q7 | 587200 |
| sw07-p5 | Q7 | 595200 |
| sw08-p2 | Q7 | 593280 |
| sw08-p4 | Q6 | 296960 |
| sw08-p4 | Q7 | 361920 |
| sw08-p5 | Q6 | 87040 |
| sw08-p5 | Q7 | 604480 |

## Opportunistic window creation (Step 8 -- see enlarge.py)

**9** brand-new window(s) opened, **112320 ns** total, on ports at or below utilisation 0.2 whose TT queue had zero windows before this run.

| port | queue | size (ns) |
|---|---|---|
| sw01-p4 | Q6 | 12480 |
| sw02-p4 | Q6 | 12480 |
| sw02-p5 | Q7 | 12480 |
| sw03-p5 | Q6 | 12480 |
| sw04-p5 | Q6 | 12480 |
| sw05-p4 | Q6 | 12480 |
| sw06-p4 | Q6 | 12480 |
| sw07-p5 | Q6 | 12480 |
| sw08-p2 | Q6 | 12480 |

## Best-effort gap equalization (Step 9 -- see enlarge.py)

**8043200 ns** given back from Steps 7/8's growth so each port's leftover non-TAS gaps land close to equal, instead of one gap staying huge while a neighbour is squeezed to the bare 1-tick C10 minimum.

| port | given back (ns) |
|---|---|
| sw05-p5 | 543680 |
| sw07-p4 | 543680 |
| sw08-p5 | 543680 |
| sw03-p4 | 541760 |
| S1-p0 | 504000 |
| sw02-p5 | 499200 |
| sw01-p2 | 480320 |
| sw01-p5 | 393280 |
| S3-p0 | 360960 |
| S2-p0 | 319360 |
| sw04-p4 | 308160 |
| sw06-p5 | 308160 |
| sw08-p4 | 308160 |
| sw02-p2 | 291840 |
| sw01-p4 | 262400 |
| sw02-p4 | 262400 |
| sw03-p5 | 262400 |
| sw04-p5 | 262400 |
| sw05-p4 | 262400 |
| sw06-p4 | 262400 |
| sw07-p5 | 262400 |
| sw08-p2 | 260160 |

## Opportunistic overlay window creation (Step 10 -- see enlarge.py)

**44** new overlay window(s), **8928960 ns** total, carved out of already-open best-effort spans on ports at or below utilisation 0.2 -- best-effort stays reachable inside each one (gate mask keeps its BE bits set), so none of this is closed off from BE.

| port | queue | size (ns) |
|---|---|---|
| S1-p0 | Q6 | 212160 |
| S1-p0 | Q7 | 291840 |
| S2-p0 | Q6 | 49920 |
| S2-p0 | Q7 | 224640 |
| S3-p0 | Q6 | 148800 |
| S3-p0 | Q7 | 224640 |
| sw01-p2 | Q6 | 201600 |
| sw01-p2 | Q7 | 282880 |
| sw01-p4 | Q6 | 149760 |
| sw01-p4 | Q7 | 200320 |
| sw01-p5 | Q6 | 155520 |
| sw01-p5 | Q7 | 212160 |
| sw02-p2 | Q6 | 216640 |
| sw02-p2 | Q7 | 91200 |
| sw02-p4 | Q6 | 141440 |
| sw02-p4 | Q7 | 150080 |
| sw02-p5 | Q6 | 249600 |
| sw02-p5 | Q7 | 224640 |
| sw03-p4 | Q6 | 290880 |
| sw03-p4 | Q7 | 304640 |
| sw03-p5 | Q6 | 170240 |
| sw03-p5 | Q7 | 200320 |
| sw04-p4 | Q6 | 187200 |
| sw04-p4 | Q7 | 195840 |
| sw04-p5 | Q6 | 149760 |
| sw04-p5 | Q7 | 150080 |
| sw05-p4 | Q6 | 186880 |
| sw05-p4 | Q7 | 200320 |
| sw05-p5 | Q6 | 333120 |
| sw05-p5 | Q7 | 260480 |
| sw06-p4 | Q6 | 149760 |
| sw06-p4 | Q7 | 175040 |
| sw06-p5 | Q6 | 197440 |
| sw06-p5 | Q7 | 147840 |
| sw07-p4 | Q6 | 291840 |
| sw07-p4 | Q7 | 272960 |
| sw07-p5 | Q6 | 199680 |
| sw07-p5 | Q7 | 200320 |
| sw08-p2 | Q6 | 176960 |
| sw08-p2 | Q7 | 162240 |
| sw08-p4 | Q6 | 180800 |
| sw08-p4 | Q7 | 168960 |
| sw08-p5 | Q6 | 283200 |
| sw08-p5 | Q7 | 264320 |

## Candidate routes (P^cand = routes of the fixed flows above)

| route | PCPs carried | flows |
|---|---|---|
| S1->sw02->sw01->S3 | Q6 (1) | 1 |
| S1->sw02->sw04->sw06->sw08->S2 | Q7 (1) | 1 |
| S2->sw08->sw06->sw04->sw02->S1 | Q6 (1), Q7 (2) | 3 |
| S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 (1), Q7 (1) | 2 |
| S3->sw01->sw02->S1 | Q6 (1), Q7 (2) | 3 |
| S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 (1) | 1 |

## Per-link enlargement accounting

| link | sharing eta | route-safe slack (ns) | link budget (ns) | final slack (ns) | applied (ns) |
|---|---|---|---|---|---|
| S1-p0 | 2 | Q6:49360, Q7:172048 | 221408 | Q6:49360, Q7:131123 | Q6:406080, Q7:331520 |
| S2-p0 | 2 | Q6:182719, Q7:40071 | 222790 | Q6:118681, Q7:40071 | Q6:76480, Q7:553920 |
| S3-p0 | 2 | Q6:205310, Q7:46968 | 252278 | Q6:89141, Q7:46968 | Q6:148800, Q7:551360 |
| sw01-p2 | 2 | Q6:49823, Q7:11038 | 60861 | Q6:46983, Q7:11038 | Q6:201600, Q7:456960 |
| sw02-p2 | 2 | Q6:179961, Q7:51997 | 231958 | Q6:97771, Q7:51997 | Q6:233600, Q7:386880 |
| sw08-p2 | 2 | Q6:0, Q7:90337 | 90337 | Q7:90337 | Q6:189440, Q7:585600 |
| sw01-p4 | 1 | Q6:0, Q7:51018 | 51018 | Q7:51018 | Q6:162240, Q7:621440 |
| sw01-p5 | 1 | Q6:74472, Q7:11605 | 86077 | Q6:44485, Q7:11605 | Q6:204160, Q7:453760 |
| sw02-p4 | 1 | Q6:0, Q7:60736 | 60736 | Q7:60736 | Q6:153920, Q7:633600 |
| sw02-p5 | 1 | Q6:11238, Q7:0 | 11238 | Q6:11238 | Q6:483840, Q7:237120 |
| sw03-p4 | 1 | Q6:46913, Q7:5892 | 52805 | Q6:35148, Q7:5892 | Q6:290880, Q7:433920 |
| sw03-p5 | 1 | Q6:0, Q7:46427 | 46427 | Q7:46427 | Q6:182720, Q7:604800 |
| sw04-p4 | 1 | Q6:45072, Q7:28093 | 73165 | Q6:20945, Q7:28093 | Q6:376960, Q7:360640 |
| sw04-p5 | 1 | Q6:0, Q7:52691 | 52691 | Q7:52691 | Q6:162240, Q7:616960 |
| sw05-p4 | 1 | Q6:0, Q7:42249 | 42249 | Q7:42249 | Q6:199360, Q7:588160 |
| sw05-p5 | 1 | Q6:42247, Q7:5239 | 47486 | Q6:31742, Q7:5239 | Q6:333120, Q7:404480 |
| sw06-p4 | 1 | Q6:0, Q7:45711 | 45711 | Q7:45711 | Q6:162240, Q7:625280 |
| sw06-p5 | 1 | Q6:39401, Q7:24634 | 64035 | Q6:18291, Q7:24634 | Q6:387200, Q7:329280 |
| sw07-p4 | 1 | Q6:38046, Q7:4658 | 42703 | Q6:28666, Q7:4658 | Q6:291840, Q7:433600 |
| sw07-p5 | 1 | Q6:0, Q7:38447 | 38447 | Q7:38447 | Q6:212160, Q7:571520 |
| sw08-p4 | 1 | Q6:34443, Q7:21601 | 56044 | Q6:15973, Q7:21601 | Q6:370560, Q7:367040 |
| sw08-p5 | 1 | Q6:34262, Q7:4141 | 38403 | Q6:25887, Q7:4141 | Q6:283200, Q7:441600 |

Total applied: **16102080 ns** across 22 port(s). Network total slack now banked: **16118720 ns**. GCL_size overflow: 0.

## Per-port GCL entries: before (SMT) vs. after (heuristic-enlarged)

| port | SMT entries | enlarged entries | GCL_size |
|---|---|---|---|
| sw01-p2 | 19 | 29 | 255 |
| sw01-p4 | 3 | 11 | 255 |
| sw01-p5 | 15 | 22 | 255 |
| sw02-p2 | 25 | 25 | 255 |
| sw02-p4 | 3 | 9 | 255 |
| sw02-p5 | 9 | 21 | 255 |
| sw03-p4 | 11 | 23 | 255 |
| sw03-p5 | 3 | 11 | 255 |
| sw04-p4 | 11 | 16 | 255 |
| sw04-p5 | 3 | 10 | 255 |
| sw05-p4 | 3 | 11 | 255 |
| sw05-p5 | 11 | 20 | 255 |
| sw06-p4 | 3 | 10 | 255 |
| sw06-p5 | 11 | 18 | 255 |
| sw07-p4 | 11 | 21 | 255 |
| sw07-p5 | 3 | 12 | 255 |
| sw08-p2 | 5 | 11 | 255 |
| sw08-p4 | 11 | 16 | 255 |
| sw08-p5 | 11 | 22 | 255 |

## Flows

| flow | route | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|
| s0(id=1 S3->S1) | S3->sw01->sw02->S1 | 6 | 62400 | 54480 | yes |
| s1(id=2 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | - | - | - | no |
| s2(id=3 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | - | - | - | no |
| s3(id=4 S3->S1) | S3->sw01->sw02->S1 | 7 | 37440 | 45840 | yes |
| s4(id=5 S1->S3) | S1->sw02->sw01->S3 | - | - | - | no |
| s5(id=6 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 7 | 0 | 95760 | yes |
| s6(id=7 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | 7 | 24960 | 79120 | yes |
| s7(id=8 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 6 | 74880 | 95760 | yes |
| s8(id=9 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 7 | 87360 | 95760 | yes |
| s9(id=10 S3->S1) | S3->sw01->sw02->S1 | 7 | 12480 | 45840 | yes |
| s10(id=11 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | - | - | - | no |
| s11(id=12 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 7 | 24960 | 79120 | yes |
| s12(id=13 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | - | - | - | no |
| s13(id=14 S1->S3) | S1->sw02->sw01->S3 | 6 | 0 | 45840 | yes |
| s14(id=15 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | - | - | - | no |
| s15(id=16 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | 7 | 49920 | 79760 | yes |
| s16(id=17 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | - | - | - | no |
| s17(id=18 S3->S1) | S3->sw01->sw02->S1 | - | - | - | no |
| s18(id=19 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | - | - | - | no |
| s19(id=20 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | 6 | 99840 | 79120 | yes |

## Per-hop windows (slack_ns > 0 means this window was enlarged)

| flow | egress port | queue | psi (ns) | delta (ns) |
|---|---|---|---|---|
| s0(id=1 S3->S1) | S3-p0 | Q6 | 62400 | 12480 |
| s0(id=1 S3->S1) | sw01-p5 | Q6 | 79040 | 12480 |
| s0(id=1 S3->S1) | sw02-p2 | Q6 | 104320 | 12480 |
| s3(id=4 S3->S1) | S3-p0 | Q7 | 37440 | 12480 |
| s3(id=4 S3->S1) | sw01-p5 | Q7 | 54080 | 12480 |
| s3(id=4 S3->S1) | sw02-p2 | Q7 | 70720 | 12480 |
| s5(id=6 S2->S3) | S2-p0 | Q7 | 0 | 12480 |
| s5(id=6 S2->S3) | sw08-p5 | Q7 | 16640 | 12480 |
| s5(id=6 S2->S3) | sw07-p4 | Q7 | 33280 | 12480 |
| s5(id=6 S2->S3) | sw05-p5 | Q7 | 49920 | 12480 |
| s5(id=6 S2->S3) | sw03-p4 | Q7 | 66560 | 12480 |
| s5(id=6 S2->S3) | sw01-p2 | Q7 | 83200 | 12480 |
| s6(id=7 S2->S1) | S2-p0 | Q7 | 24960 | 12480 |
| s6(id=7 S2->S1) | sw08-p4 | Q7 | 41600 | 12480 |
| s6(id=7 S2->S1) | sw06-p5 | Q7 | 58240 | 12480 |
| s6(id=7 S2->S1) | sw04-p4 | Q7 | 74880 | 12480 |
| s6(id=7 S2->S1) | sw02-p2 | Q7 | 91520 | 12480 |
| s7(id=8 S2->S3) | S2-p0 | Q6 | 74880 | 12480 |
| s7(id=8 S2->S3) | sw08-p5 | Q6 | 91520 | 12480 |
| s7(id=8 S2->S3) | sw07-p4 | Q6 | 108160 | 12480 |
| s7(id=8 S2->S3) | sw05-p5 | Q6 | 124800 | 12480 |
| s7(id=8 S2->S3) | sw03-p4 | Q6 | 141440 | 12480 |
| s7(id=8 S2->S3) | sw01-p2 | Q6 | 158080 | 12480 |
| s8(id=9 S3->S2) | S3-p0 | Q7 | 87360 | 12480 |
| s8(id=9 S3->S2) | sw01-p4 | Q7 | 104000 | 12480 |
| s8(id=9 S3->S2) | sw03-p5 | Q7 | 120640 | 12480 |
| s8(id=9 S3->S2) | sw05-p4 | Q7 | 137280 | 12480 |
| s8(id=9 S3->S2) | sw07-p5 | Q7 | 153920 | 12480 |
| s8(id=9 S3->S2) | sw08-p2 | Q7 | 170560 | 12480 |
| s9(id=10 S3->S1) | S3-p0 | Q7 | 12480 | 12480 |
| s9(id=10 S3->S1) | sw01-p5 | Q7 | 29120 | 12480 |
| s9(id=10 S3->S1) | sw02-p2 | Q7 | 45760 | 12480 |
| s11(id=12 S1->S2) | S1-p0 | Q7 | 24960 | 12480 |
| s11(id=12 S1->S2) | sw02-p4 | Q7 | 41600 | 12480 |
| s11(id=12 S1->S2) | sw04-p5 | Q7 | 58240 | 12480 |
| s11(id=12 S1->S2) | sw06-p4 | Q7 | 74880 | 12480 |
| s11(id=12 S1->S2) | sw08-p2 | Q7 | 91520 | 12480 |
| s13(id=14 S1->S3) | S1-p0 | Q6 | 0 | 12480 |
| s13(id=14 S1->S3) | sw02-p5 | Q6 | 16640 | 12480 |
| s13(id=14 S1->S3) | sw01-p2 | Q6 | 33280 | 12480 |
| s15(id=16 S2->S1) | S2-p0 | Q7 | 49920 | 12480 |
| s15(id=16 S2->S1) | sw08-p4 | Q7 | 66560 | 12480 |
| s15(id=16 S2->S1) | sw06-p5 | Q7 | 83200 | 12480 |
| s15(id=16 S2->S1) | sw04-p4 | Q7 | 99840 | 12480 |
| s15(id=16 S2->S1) | sw02-p2 | Q7 | 117120 | 12480 |
| s19(id=20 S2->S1) | S2-p0 | Q6 | 99840 | 12480 |
| s19(id=20 S2->S1) | sw08-p4 | Q6 | 116480 | 12480 |
| s19(id=20 S2->S1) | sw06-p5 | Q6 | 133120 | 12480 |
| s19(id=20 S2->S1) | sw04-p4 | Q6 | 149760 | 12480 |
| s19(id=20 S2->S1) | sw02-p2 | Q6 | 166400 | 12480 |

## Constraint check

- C1-C7, C9: OK
- seed-integrity (no SMT-fixed flow's placement changed): OK

## GCL per egress port

### sw01-p2  (29 entries, util 14.0400 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 33280 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 4480 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 8000 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 29440 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 33280 0xBF # 10111111   Q7
sgs 81600 0x80 # 10000000   Q7
sgs 35200 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 33280 0xBF # 10111111   Q7
sgs 81600 0x80 # 10000000   Q7
sgs 35200 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 33280 0xBF # 10111111   Q7
sgs 48320 0x80 # 10000000   Q7
sgs 18560 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p4  (11 entries, util 1.5600 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 3840 0x3F # 00111111   BE
sgs 433600 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p5  (22 entries, util 10.9200 %)

```
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 61120 0x40 # 01000000   Q6
sgs 9920 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 111040 0x80 # 10000000   Q7
sgs 9920 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 86080 0x80 # 10000000   Q7
sgs 9920 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 81920 0x80 # 10000000   Q7
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (25 entries, util 18.7200 %)

```
sgs 45760 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 33280 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 16320 0xBF # 10111111   Q7
sgs 29440 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 45760 0x7F # 01111111   Q6
sgs 150080 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 45760 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 33280 0x80 # 10000000   Q7
sgs 13120 0x7F # 01111111   Q6
sgs 78720 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 45760 0x7F # 01111111   Q6
sgs 104320 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p4  (9 entries, util 1.5600 %)

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

### sw02-p5  (21 entries, util 6.2400 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 75200 0x40 # 01000000   Q6
sgs 8320 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 75200 0x40 # 01000000   Q6
sgs 8320 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 75200 0x40 # 01000000   Q6
sgs 8320 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 58560 0x40 # 01000000   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (23 entries, util 7.8000 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 21120 0xBF # 10111111   Q7
sgs 41280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 46080 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 77120 0x80 # 10000000   Q7
sgs 6400 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 77120 0x80 # 10000000   Q7
sgs 6400 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 21120 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p5  (11 entries, util 1.5600 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 416960 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p4  (16 entries, util 7.8000 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 202240 0x40 # 01000000   Q6
sgs 48000 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 177280 0x80 # 10000000   Q7
sgs 23040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (10 entries, util 1.5600 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 8320 0x3F # 00111111   BE
sgs 479360 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (11 entries, util 1.5600 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 37120 0x7F # 01111111   Q6
sgs 400320 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p5  (20 entries, util 7.8000 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 37760 0xBF # 10111111   Q7
sgs 24640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12800 0x7F # 01111111   Q6
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

### sw06-p4  (10 entries, util 1.5600 %)

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

### sw06-p5  (18 entries, util 7.8000 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 4480 0x3F # 00111111   BE
sgs 32960 0x7F # 01111111   Q6
sgs 202240 0x40 # 01000000   Q6
sgs 14720 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 193920 0x80 # 10000000   Q7
sgs 23040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (21 entries, util 7.8000 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 50240 0xBF # 10111111   Q7
sgs 8000 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 29440 0x7F # 01111111   Q6
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

### sw07-p5  (12 entries, util 1.5600 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 3840 0x3F # 00111111   BE
sgs 383680 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p2  (11 entries, util 3.1200 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x7F # 01111111   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 46080 0x7F # 01111111   Q6
sgs 20480 0xBF # 10111111   Q7
sgs 435840 0x80 # 10000000   Q7
sgs 43520 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p4  (16 entries, util 7.8000 %)

```
sgs 41600 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 21120 0xBF # 10111111   Q7
sgs 16320 0x7F # 01111111   Q6
sgs 202240 0x40 # 01000000   Q6
sgs 31360 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0xBF # 10111111   Q7
sgs 210560 0x80 # 10000000   Q7
sgs 23040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (22 entries, util 7.8000 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 20800 0x7F # 01111111   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 46080 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 77120 0x80 # 10000000   Q7
sgs 6400 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 77120 0x80 # 10000000   Q7
sgs 6400 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 60480 0x80 # 10000000   Q7
sgs 23040 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

