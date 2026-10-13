# Heuristic-enlarged GCL schedule (Problem 2: window enlargement)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Time-sensitive PCPs considered: [6, 7]
- Seeded from SMT run: **result/result-2026-10-12-dataset-testbed-6-ring-avgwin/smt-c9-off/6-t3600-c9off-minlat**

## Admission (unchanged by this package -- it only widens windows)

SMT-fixed flows: **10**/20. This package never admits a flow itself; it banks slack for a later admission pass (`prob_3_admit`, Problem 3) to use.

## Opportunistic idle top-up (Step 7 -- see enlarge.py)

Total: **10495040 ns**, drawn from idle capacity on ports at or below utilisation 0.2, independent of any route's deadline-slack budget.

| port | queue | applied (ns) |
|---|---|---|
| S1-p0 | Q7 | 541440 |
| S2-p0 | Q6 | 263360 |
| S2-p0 | Q7 | 391360 |
| sw01-p2 | Q6 | 637760 |
| sw01-p4 | Q6 | 703680 |
| sw01-p5 | Q6 | 141120 |
| sw01-p5 | Q7 | 497600 |
| sw02-p4 | Q7 | 724800 |
| sw02-p5 | Q6 | 677120 |
| sw03-p5 | Q6 | 687360 |
| sw04-p4 | Q6 | 267840 |
| sw04-p4 | Q7 | 343360 |
| sw04-p5 | Q7 | 709440 |
| sw05-p4 | Q6 | 671360 |
| sw06-p4 | Q7 | 693760 |
| sw06-p5 | Q6 | 272320 |
| sw06-p5 | Q7 | 360960 |
| sw07-p5 | Q6 | 655040 |
| sw08-p2 | Q6 | 507840 |
| sw08-p2 | Q7 | 92800 |
| sw08-p4 | Q6 | 276160 |
| sw08-p4 | Q7 | 378560 |

## Opportunistic window creation (Step 8 -- see enlarge.py)

**17** brand-new window(s) opened, **212160 ns** total, on ports at or below utilisation 0.2 whose TT queue had zero windows before this run.

| port | queue | size (ns) |
|---|---|---|
| sw01-p2 | Q7 | 12480 |
| sw01-p4 | Q7 | 12480 |
| sw02-p4 | Q6 | 12480 |
| sw02-p5 | Q7 | 12480 |
| sw03-p4 | Q6 | 12480 |
| sw03-p4 | Q7 | 12480 |
| sw03-p5 | Q7 | 12480 |
| sw04-p5 | Q6 | 12480 |
| sw05-p4 | Q7 | 12480 |
| sw05-p5 | Q6 | 12480 |
| sw05-p5 | Q7 | 12480 |
| sw06-p4 | Q6 | 12480 |
| sw07-p4 | Q6 | 12480 |
| sw07-p4 | Q7 | 12480 |
| sw07-p5 | Q7 | 12480 |
| sw08-p5 | Q6 | 12480 |
| sw08-p5 | Q7 | 12480 |

## Best-effort gap equalization (Step 9 -- see enlarge.py)

**6888320 ns** given back from Steps 7/8's growth so each port's leftover non-TAS gaps land close to equal, instead of one gap staying huge while a neighbour is squeezed to the bare 1-tick C10 minimum.

| port | given back (ns) |
|---|---|
| S1-p0 | 504000 |
| sw01-p4 | 499200 |
| sw02-p4 | 499200 |
| sw03-p5 | 499200 |
| sw04-p5 | 499200 |
| sw06-p4 | 499200 |
| sw05-p4 | 487040 |
| sw07-p5 | 470400 |
| sw08-p2 | 427520 |
| sw01-p5 | 419840 |
| sw04-p4 | 361280 |
| sw06-p5 | 361280 |
| sw08-p4 | 361280 |
| S2-p0 | 360960 |
| sw01-p2 | 262400 |
| sw02-p5 | 262400 |
| sw02-p2 | 58880 |
| S3-p0 | 55040 |

## Opportunistic overlay window creation (Step 10 -- see enlarge.py)

**40** new overlay window(s), **10155520 ns** total, carved out of already-open best-effort spans on ports at or below utilisation 0.2 -- best-effort stays reachable inside each one (gate mask keeps its BE bits set), so none of this is closed off from BE.

| port | queue | size (ns) |
|---|---|---|
| S1-p0 | Q6 | 212160 |
| S1-p0 | Q7 | 291840 |
| S2-p0 | Q6 | 148800 |
| S2-p0 | Q7 | 212160 |
| sw01-p2 | Q6 | 149760 |
| sw01-p2 | Q7 | 150080 |
| sw01-p4 | Q6 | 303680 |
| sw01-p4 | Q7 | 224640 |
| sw01-p5 | Q6 | 149760 |
| sw01-p5 | Q7 | 275520 |
| sw02-p4 | Q6 | 249600 |
| sw02-p4 | Q7 | 224640 |
| sw02-p5 | Q6 | 141440 |
| sw02-p5 | Q7 | 150080 |
| sw03-p4 | Q6 | 374400 |
| sw03-p4 | Q7 | 400640 |
| sw03-p5 | Q6 | 287040 |
| sw03-p5 | Q7 | 224640 |
| sw04-p4 | Q6 | 240000 |
| sw04-p4 | Q7 | 159040 |
| sw04-p5 | Q6 | 295360 |
| sw04-p5 | Q7 | 224640 |
| sw05-p4 | Q6 | 237120 |
| sw05-p4 | Q7 | 312320 |
| sw05-p5 | Q6 | 374400 |
| sw05-p5 | Q7 | 400640 |
| sw06-p4 | Q6 | 312000 |
| sw06-p4 | Q7 | 224640 |
| sw06-p5 | Q6 | 160960 |
| sw06-p5 | Q7 | 183360 |
| sw07-p4 | Q6 | 374400 |
| sw07-p4 | Q7 | 400640 |
| sw07-p5 | Q6 | 233280 |
| sw07-p5 | Q7 | 316160 |
| sw08-p2 | Q6 | 227520 |
| sw08-p2 | Q7 | 200960 |
| sw08-p4 | Q6 | 120000 |
| sw08-p4 | Q7 | 212160 |
| sw08-p5 | Q6 | 374400 |
| sw08-p5 | Q7 | 400640 |

## Candidate routes (P^cand = routes of the fixed flows above)

| route | PCPs carried | flows |
|---|---|---|
| S1->sw02->sw01->S3 | Q6 (1) | 1 |
| S1->sw02->sw04->sw06->sw08->S2 | Q7 (1) | 1 |
| S2->sw08->sw06->sw04->sw02->S1 | Q6 (3), Q7 (1) | 4 |
| S3->sw01->sw02->S1 | Q6 (1), Q7 (2) | 3 |
| S3->sw01->sw03->sw05->sw07->sw08->S2 | Q6 (1) | 1 |

## Per-link enlargement accounting

| link | sharing eta | route-safe slack (ns) | link budget (ns) | final slack (ns) | applied (ns) |
|---|---|---|---|---|---|
| S1-p0 | 2 | Q6:382506, Q7:33743 | 416250 | Q6:262104, Q7:33743 | Q6:251840, Q7:485760 |
| S3-p0 | 2 | Q6:45092, Q7:42758 | 87850 | Q6:45092, Q7:28255 | Q7:17920 |
| sw02-p2 | 2 | Q6:51901, Q7:56023 | 107925 | Q6:47298, Q7:56023 | Q6:5760, Q7:38400 |
| sw08-p2 | 2 | Q6:9541, Q7:25159 | 34700 | Q6:9541, Q7:23847 | Q6:433600, Q7:200960 |
| S2-p0 | 1 | Q6:37014, Q7:8700 | 45714 | Q6:37014, Q7:8700 | Q6:268480, Q7:431680 |
| sw01-p2 | 1 | Q6:91576, Q7:0 | 91576 | Q6:91576 | Q6:616640, Q7:162560 |
| sw01-p4 | 1 | Q6:5037, Q7:0 | 5037 | Q6:5037 | Q6:512960, Q7:237120 |
| sw01-p5 | 1 | Q6:11142, Q7:11359 | 22500 | Q6:8896, Q7:11359 | Q6:149760, Q7:514240 |
| sw02-p4 | 1 | Q6:0, Q7:8927 | 8927 | Q7:8927 | Q6:262080, Q7:458880 |
| sw02-p5 | 1 | Q6:69012, Q7:0 | 69012 | Q6:69012 | Q6:624960, Q7:162560 |
| sw03-p5 | 1 | Q6:4525, Q7:0 | 4525 | Q6:4525 | Q6:479680, Q7:237120 |
| sw04-p4 | 1 | Q6:31834, Q7:7533 | 39367 | Q6:31834, Q7:7533 | Q6:359360, Q7:328640 |
| sw04-p5 | 1 | Q6:0, Q7:7641 | 7641 | Q7:7641 | Q6:307840, Q7:442240 |
| sw05-p4 | 1 | Q6:4066, Q7:0 | 4066 | Q6:4066 | Q6:425280, Q7:324800 |
| sw06-p4 | 1 | Q6:0, Q7:6541 | 6541 | Q7:6541 | Q6:324480, Q7:425600 |
| sw06-p5 | 1 | Q6:27380, Q7:6522 | 33902 | Q6:27380, Q7:6522 | Q6:280320, Q7:369600 |
| sw07-p5 | 1 | Q6:3653, Q7:0 | 3653 | Q6:3653 | Q6:421440, Q7:328640 |
| sw08-p4 | 1 | Q6:23548, Q7:5647 | 29195 | Q6:23548, Q7:5647 | Q6:239360, Q7:415040 |

Total applied: **14745600 ns** across 22 port(s). Network total slack now banked: **14806080 ns**. GCL_size overflow: 0.

## Per-port GCL entries: before (SMT) vs. after (heuristic-enlarged)

| port | SMT entries | enlarged entries | GCL_size |
|---|---|---|---|
| sw01-p2 | 3 | 10 | 255 |
| sw01-p4 | 9 | 18 | 255 |
| sw01-p5 | 21 | 29 | 255 |
| sw02-p2 | 37 | 27 | 255 |
| sw02-p4 | 9 | 21 | 255 |
| sw02-p5 | 3 | 9 | 255 |
| sw03-p4 | 1 | 18 | 255 |
| sw03-p5 | 9 | 22 | 255 |
| sw04-p4 | 17 | 19 | 255 |
| sw04-p5 | 9 | 18 | 255 |
| sw05-p4 | 9 | 19 | 255 |
| sw05-p5 | 1 | 18 | 255 |
| sw06-p4 | 9 | 18 | 255 |
| sw06-p5 | 17 | 19 | 255 |
| sw07-p4 | 1 | 18 | 255 |
| sw07-p5 | 9 | 18 | 255 |
| sw08-p2 | 17 | 29 | 255 |
| sw08-p4 | 17 | 22 | 255 |
| sw08-p5 | 1 | 18 | 255 |

## Flows

| flow | route | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|
| s0(id=1 S3->S1) | S3->sw01->sw02->S1 | 6 | 0 | 45840 | yes |
| s1(id=2 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | 7 | 0 | 79120 | yes |
| s2(id=3 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | - | - | - | no |
| s3(id=4 S1->S3) | S1->sw02->sw01->S3 | 6 | 24960 | 45840 | yes |
| s4(id=5 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | - | - | - | no |
| s5(id=6 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | 6 | 24960 | 83600 | yes |
| s6(id=7 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | 6 | 49920 | 84240 | yes |
| s7(id=8 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | - | - | - | no |
| s8(id=9 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 6 | 24960 | 95760 | yes |
| s9(id=10 S1->S3) | S1->sw02->sw01->S3 | - | - | - | no |
| s10(id=11 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | - | - | - | no |
| s11(id=12 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | 6 | 74880 | 79120 | yes |
| s12(id=13 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | - | - | - | no |
| s13(id=14 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 7 | 0 | 79120 | yes |
| s14(id=15 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | - | - | - | no |
| s15(id=16 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | - | - | - | no |
| s16(id=17 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | - | - | - | no |
| s17(id=18 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | - | - | - | no |
| s18(id=19 S3->S1) | S3->sw01->sw02->S1 | 7 | 74880 | 46480 | yes |
| s19(id=20 S3->S1) | S3->sw01->sw02->S1 | 7 | 49920 | 45840 | yes |

## Per-hop windows (slack_ns > 0 means this window was enlarged)

| flow | egress port | queue | psi (ns) | delta (ns) |
|---|---|---|---|---|
| s0(id=1 S3->S1) | S3-p0 | Q6 | 0 | 12480 |
| s0(id=1 S3->S1) | sw01-p5 | Q6 | 16640 | 12480 |
| s0(id=1 S3->S1) | sw02-p2 | Q6 | 33280 | 12480 |
| s1(id=2 S2->S1) | S2-p0 | Q7 | 0 | 12480 |
| s1(id=2 S2->S1) | sw08-p4 | Q7 | 16640 | 12480 |
| s1(id=2 S2->S1) | sw06-p5 | Q7 | 33280 | 12480 |
| s1(id=2 S2->S1) | sw04-p4 | Q7 | 49920 | 12480 |
| s1(id=2 S2->S1) | sw02-p2 | Q7 | 66560 | 12480 |
| s3(id=4 S1->S3) | S1-p0 | Q6 | 24960 | 12480 |
| s3(id=4 S1->S3) | sw02-p5 | Q6 | 41600 | 12480 |
| s3(id=4 S1->S3) | sw01-p2 | Q6 | 58240 | 12480 |
| s5(id=6 S2->S1) | S2-p0 | Q6 | 24960 | 12480 |
| s5(id=6 S2->S1) | sw08-p4 | Q6 | 41920 | 12480 |
| s5(id=6 S2->S1) | sw06-p5 | Q6 | 58560 | 12480 |
| s5(id=6 S2->S1) | sw04-p4 | Q6 | 75200 | 12480 |
| s5(id=6 S2->S1) | sw02-p2 | Q6 | 96000 | 12480 |
| s6(id=7 S2->S1) | S2-p0 | Q6 | 49920 | 12480 |
| s6(id=7 S2->S1) | sw08-p4 | Q6 | 66560 | 12480 |
| s6(id=7 S2->S1) | sw06-p5 | Q6 | 83200 | 12480 |
| s6(id=7 S2->S1) | sw04-p4 | Q6 | 99840 | 12480 |
| s6(id=7 S2->S1) | sw02-p2 | Q6 | 121600 | 12480 |
| s8(id=9 S3->S2) | S3-p0 | Q6 | 24960 | 12480 |
| s8(id=9 S3->S2) | sw01-p4 | Q6 | 41600 | 12480 |
| s8(id=9 S3->S2) | sw03-p5 | Q6 | 58240 | 12480 |
| s8(id=9 S3->S2) | sw05-p4 | Q6 | 74880 | 12480 |
| s8(id=9 S3->S2) | sw07-p5 | Q6 | 91520 | 12480 |
| s8(id=9 S3->S2) | sw08-p2 | Q6 | 108160 | 12480 |
| s11(id=12 S2->S1) | S2-p0 | Q6 | 74880 | 12480 |
| s11(id=12 S2->S1) | sw08-p4 | Q6 | 91520 | 12480 |
| s11(id=12 S2->S1) | sw06-p5 | Q6 | 108160 | 12480 |
| s11(id=12 S2->S1) | sw04-p4 | Q6 | 124800 | 12480 |
| s11(id=12 S2->S1) | sw02-p2 | Q6 | 141440 | 12480 |
| s13(id=14 S1->S2) | S1-p0 | Q7 | 0 | 12480 |
| s13(id=14 S1->S2) | sw02-p4 | Q7 | 16640 | 12480 |
| s13(id=14 S1->S2) | sw04-p5 | Q7 | 33280 | 12480 |
| s13(id=14 S1->S2) | sw06-p4 | Q7 | 49920 | 12480 |
| s13(id=14 S1->S2) | sw08-p2 | Q7 | 66560 | 12480 |
| s18(id=19 S3->S1) | S3-p0 | Q7 | 74880 | 12480 |
| s18(id=19 S3->S1) | sw01-p5 | Q7 | 91840 | 12480 |
| s18(id=19 S3->S1) | sw02-p2 | Q7 | 108800 | 12480 |
| s19(id=20 S3->S1) | S3-p0 | Q7 | 49920 | 12480 |
| s19(id=20 S3->S1) | sw01-p5 | Q7 | 66560 | 12480 |
| s19(id=20 S3->S1) | sw02-p2 | Q7 | 83200 | 12480 |

## Constraint check

- C1-C7, C9: OK
- seed-integrity (no SMT-fixed flow's placement changed): OK

## GCL per egress port

### sw01-p2  (10 entries, util 1.5600 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 8320 0x3F # 00111111   BE
sgs 479360 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p4  (18 entries, util 6.2400 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 75200 0x40 # 01000000   Q6
sgs 33280 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 75200 0x40 # 01000000   Q6
sgs 33280 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 75200 0x40 # 01000000   Q6
sgs 33280 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 41600 0x7F # 01111111   Q6
sgs 33600 0x40 # 01000000   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p5  (29 entries, util 15.6000 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 63680 0x80 # 10000000   Q7
sgs 44480 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 88960 0x80 # 10000000   Q7
sgs 44480 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 63680 0x80 # 10000000   Q7
sgs 44480 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 72320 0x80 # 10000000   Q7
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (27 entries, util 28.0800 %)

```
sgs 33280 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x3F # 00111111   BE
sgs 29120 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 38080 0x40 # 01000000   Q6
sgs 73600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x3F # 00111111   BE
sgs 56640 0x80 # 10000000   Q7
sgs 110080 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x3F # 00111111   BE
sgs 29120 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 17920 0x80 # 10000000   Q7
sgs 106560 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 20800 0x3F # 00111111   BE
sgs 34560 0x80 # 10000000   Q7
sgs 98880 0x3F # 00111111   BE
```

### sw02-p4  (21 entries, util 6.2400 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 75200 0x80 # 10000000   Q7
sgs 8320 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 75200 0x80 # 10000000   Q7
sgs 8320 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 75200 0x80 # 10000000   Q7
sgs 8320 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 58560 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p5  (9 entries, util 1.5600 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 496000 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (18 entries, util 0.0000 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0x7F # 01111111   Q6
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
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p5  (22 entries, util 6.2400 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 8320 0x3F # 00111111   BE
sgs 75200 0x40 # 01000000   Q6
sgs 16640 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 8320 0x3F # 00111111   BE
sgs 75200 0x40 # 01000000   Q6
sgs 16640 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 8320 0x3F # 00111111   BE
sgs 75200 0x40 # 01000000   Q6
sgs 16640 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 8320 0x3F # 00111111   BE
sgs 16960 0x40 # 01000000   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p4  (19 entries, util 12.4800 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 37120 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 47360 0x40 # 01000000   Q6
sgs 27840 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 122240 0x80 # 10000000   Q7
sgs 27840 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0xBF # 10111111   Q7
sgs 96960 0x40 # 01000000   Q6
sgs 27840 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 72320 0x80 # 10000000   Q7
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (18 entries, util 6.2400 %)

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

### sw05-p4  (19 entries, util 6.2400 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 75200 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 75200 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 75200 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 12800 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p5  (18 entries, util 0.0000 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0x7F # 01111111   Q6
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
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p4  (18 entries, util 6.2400 %)

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

### sw06-p5  (19 entries, util 12.4800 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0x3F # 00111111   BE
sgs 37120 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 47360 0x40 # 01000000   Q6
sgs 44480 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 122240 0x80 # 10000000   Q7
sgs 44480 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0x3F # 00111111   BE
sgs 96960 0x40 # 01000000   Q6
sgs 44480 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 88960 0x80 # 10000000   Q7
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (18 entries, util 0.0000 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0x7F # 01111111   Q6
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
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p5  (18 entries, util 6.2400 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 75200 0x40 # 01000000   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 75200 0x40 # 01000000   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 75200 0x40 # 01000000   Q6
sgs 33280 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 41600 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 46080 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p2  (29 entries, util 12.4800 %)

```
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 21120 0xBF # 10111111   Q7
sgs 8000 0x3F # 00111111   BE
sgs 80640 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 21120 0xBF # 10111111   Q7
sgs 8000 0x3F # 00111111   BE
sgs 80640 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 21120 0xBF # 10111111   Q7
sgs 8000 0x3F # 00111111   BE
sgs 80640 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 21120 0xBF # 10111111   Q7
sgs 8000 0x3F # 00111111   BE
sgs 14080 0x40 # 01000000   Q6
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p4  (22 entries, util 12.4800 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0x7F # 01111111   Q6
sgs 37120 0x40 # 01000000   Q6
sgs 12480 0xBF # 10111111   Q7
sgs 47360 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 122240 0x80 # 10000000   Q7
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0x7F # 01111111   Q6
sgs 96960 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 105600 0x80 # 10000000   Q7
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (18 entries, util 0.0000 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0x7F # 01111111   Q6
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
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

