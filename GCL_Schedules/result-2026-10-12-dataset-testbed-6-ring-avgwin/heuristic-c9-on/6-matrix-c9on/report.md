# Heuristic-enlarged GCL schedule (Problem 2: window enlargement)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Time-sensitive PCPs considered: [6, 7]
- Seeded from SMT run: **result/result-2026-10-12-dataset-testbed-6-ring-avgwin/smt-c9-on/6-fair-retimed-c9on**

## Admission (unchanged by this package -- it only widens windows)

SMT-fixed flows: **10**/10. This package never admits a flow itself; it banks slack for a later admission pass (`prob_3_admit`, Problem 3) to use.

## Opportunistic idle top-up (Step 7 -- see enlarge.py)

Total: **10603200 ns**, drawn from idle capacity on ports at or below utilisation 0.2, independent of any route's deadline-slack budget.

| port | queue | applied (ns) |
|---|---|---|
| S1-p0 | Q7 | 528640 |
| S2-p0 | Q6 | 561600 |
| S2-p0 | Q7 | 53760 |
| sw01-p2 | Q6 | 655360 |
| sw01-p4 | Q6 | 709120 |
| sw01-p5 | Q6 | 514240 |
| sw01-p5 | Q7 | 130880 |
| sw02-p4 | Q7 | 732800 |
| sw02-p5 | Q6 | 685120 |
| sw03-p5 | Q6 | 701760 |
| sw04-p4 | Q6 | 537600 |
| sw04-p4 | Q7 | 65600 |
| sw04-p5 | Q7 | 729600 |
| sw05-p4 | Q6 | 694080 |
| sw06-p4 | Q7 | 725760 |
| sw06-p5 | Q6 | 547840 |
| sw06-p5 | Q7 | 72640 |
| sw07-p5 | Q6 | 686400 |
| sw08-p2 | Q6 | 531840 |
| sw08-p2 | Q7 | 101760 |
| sw08-p4 | Q6 | 558080 |
| sw08-p4 | Q7 | 78720 |

## Opportunistic window creation (Step 8 -- see enlarge.py)

**15** brand-new window(s) opened, **187200 ns** total, on ports at or below utilisation 0.2 whose TT queue had zero windows before this run.

| port | queue | size (ns) |
|---|---|---|
| sw01-p2 | Q7 | 12480 |
| sw01-p4 | Q7 | 12480 |
| sw02-p5 | Q7 | 12480 |
| sw03-p4 | Q6 | 12480 |
| sw03-p4 | Q7 | 12480 |
| sw03-p5 | Q7 | 12480 |
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

**7103040 ns** given back from Steps 7/8's growth so each port's leftover non-TAS gaps land close to equal, instead of one gap staying huge while a neighbour is squeezed to the bare 1-tick C10 minimum.

| port | given back (ns) |
|---|---|
| sw02-p4 | 599040 |
| sw04-p5 | 599040 |
| S1-p0 | 504000 |
| sw01-p4 | 499200 |
| sw03-p5 | 499200 |
| sw05-p4 | 499200 |
| sw06-p4 | 499200 |
| sw07-p5 | 499200 |
| sw08-p2 | 445440 |
| sw01-p5 | 414720 |
| S2-p0 | 360960 |
| sw08-p4 | 355840 |
| sw06-p5 | 350720 |
| sw04-p4 | 345600 |
| sw01-p2 | 262400 |
| sw02-p5 | 262400 |
| S3-p0 | 54400 |
| sw02-p2 | 52480 |

## Opportunistic overlay window creation (Step 10 -- see enlarge.py)

**40** new overlay window(s), **10008320 ns** total, carved out of already-open best-effort spans on ports at or below utilisation 0.2 -- best-effort stays reachable inside each one (gate mask keeps its BE bits set), so none of this is closed off from BE.

| port | queue | size (ns) |
|---|---|---|
| S1-p0 | Q6 | 212160 |
| S1-p0 | Q7 | 291840 |
| S2-p0 | Q6 | 148800 |
| S2-p0 | Q7 | 212160 |
| sw01-p2 | Q6 | 138240 |
| sw01-p2 | Q7 | 150080 |
| sw01-p4 | Q6 | 295360 |
| sw01-p4 | Q7 | 224640 |
| sw01-p5 | Q6 | 116480 |
| sw01-p5 | Q7 | 229120 |
| sw02-p4 | Q6 | 199680 |
| sw02-p4 | Q7 | 384000 |
| sw02-p5 | Q6 | 131520 |
| sw02-p5 | Q7 | 150080 |
| sw03-p4 | Q6 | 374400 |
| sw03-p4 | Q7 | 400640 |
| sw03-p5 | Q6 | 303680 |
| sw03-p5 | Q7 | 224640 |
| sw04-p4 | Q6 | 120000 |
| sw04-p4 | Q7 | 216960 |
| sw04-p5 | Q6 | 199680 |
| sw04-p5 | Q7 | 368640 |
| sw05-p4 | Q6 | 312000 |
| sw05-p4 | Q7 | 224640 |
| sw05-p5 | Q6 | 374400 |
| sw05-p5 | Q7 | 400640 |
| sw06-p4 | Q6 | 245760 |
| sw06-p4 | Q7 | 224640 |
| sw06-p5 | Q6 | 126720 |
| sw06-p5 | Q7 | 213120 |
| sw07-p4 | Q6 | 374400 |
| sw07-p4 | Q7 | 400640 |
| sw07-p5 | Q6 | 287040 |
| sw07-p5 | Q7 | 224640 |
| sw08-p2 | Q6 | 177600 |
| sw08-p2 | Q7 | 266240 |
| sw08-p4 | Q6 | 88320 |
| sw08-p4 | Q7 | 199680 |
| sw08-p5 | Q6 | 374400 |
| sw08-p5 | Q7 | 400640 |

## Candidate routes (P^cand = routes of the fixed flows above)

| route | PCPs carried | flows |
|---|---|---|
| S1->sw02->sw01->S3 | Q6 (1) | 1 |
| S1->sw02->sw04->sw06->sw08->S2 | Q7 (1) | 1 |
| S2->sw08->sw06->sw04->sw02->S1 | Q6 (2), Q7 (2) | 4 |
| S3->sw01->sw02->S1 | Q6 (2), Q7 (1) | 3 |
| S3->sw01->sw03->sw05->sw07->sw08->S2 | Q6 (1) | 1 |

## Per-link enlargement accounting

| link | sharing eta | route-safe slack (ns) | link budget (ns) | final slack (ns) | applied (ns) |
|---|---|---|---|---|---|
| S1-p0 | 2 | Q6:392569, Q7:46606 | 439176 | Q6:245147, Q7:46606 | Q6:251840, Q7:485760 |
| S3-p0 | 2 | Q6:54321, Q7:48800 | 103121 | Q6:54321, Q7:21062 | Q6:20480 |
| sw02-p2 | 2 | Q6:59703, Q7:61766 | 121468 | Q6:59703, Q7:39071 | Q6:15680, Q7:30400 |
| sw08-p2 | 2 | Q6:13702, Q7:34749 | 48451 | Q6:13702, Q7:32889 | Q6:411840, Q7:266240 |
| S2-p0 | 1 | Q6:13577, Q7:90372 | 103949 | Q6:13577, Q7:71655 | Q6:453120, Q7:247040 |
| sw01-p2 | 1 | Q6:93985, Q7:0 | 93985 | Q6:93985 | Q6:624960, Q7:162560 |
| sw01-p4 | 1 | Q6:7690, Q7:0 | 7690 | Q6:7690 | Q6:512960, Q7:237120 |
| sw01-p5 | 1 | Q6:12038, Q7:12529 | 24567 | Q6:12038, Q7:10064 | Q6:368640, Q7:229120 |
| sw02-p4 | 1 | Q6:0, Q7:12331 | 12331 | Q7:12331 | Q6:199680, Q7:529920 |
| sw02-p5 | 1 | Q6:70827, Q7:0 | 70827 | Q6:70827 | Q6:624960, Q7:162560 |
| sw03-p5 | 1 | Q6:6930, Q7:0 | 6930 | Q6:6930 | Q6:512960, Q7:237120 |
| sw04-p4 | 1 | Q6:11677, Q7:78642 | 90319 | Q6:11677, Q7:62485 | Q6:408960, Q7:259520 |
| sw04-p5 | 1 | Q6:0, Q7:10554 | 10554 | Q7:10554 | Q6:199680, Q7:509440 |
| sw05-p4 | 1 | Q6:6245, Q7:0 | 6245 | Q6:6245 | Q6:512960, Q7:237120 |
| sw06-p4 | 1 | Q6:0, Q7:9034 | 9034 | Q7:9034 | Q6:258240, Q7:460160 |
| sw06-p5 | 1 | Q6:10043, Q7:68434 | 78477 | Q6:10043, Q7:54488 | Q6:420800, Q7:253120 |
| sw07-p5 | 1 | Q6:5628, Q7:0 | 5628 | Q6:5628 | Q6:479680, Q7:237120 |
| sw08-p4 | 1 | Q6:8637, Q7:59551 | 68189 | Q6:8637, Q7:47514 | Q6:387520, Q7:237120 |

Total applied: **14646400 ns** across 22 port(s). Network total slack now banked: **14731200 ns**. GCL_size overflow: 0.

## Per-port GCL entries: before (SMT) vs. after (heuristic-enlarged)

| port | SMT entries | enlarged entries | GCL_size |
|---|---|---|---|
| sw01-p2 | 3 | 9 | 255 |
| sw01-p4 | 9 | 18 | 255 |
| sw01-p5 | 21 | 32 | 255 |
| sw02-p2 | 37 | 29 | 255 |
| sw02-p4 | 9 | 20 | 255 |
| sw02-p5 | 3 | 9 | 255 |
| sw03-p4 | 1 | 18 | 255 |
| sw03-p5 | 9 | 18 | 255 |
| sw04-p4 | 17 | 18 | 255 |
| sw04-p5 | 9 | 20 | 255 |
| sw05-p4 | 9 | 18 | 255 |
| sw05-p5 | 1 | 18 | 255 |
| sw06-p4 | 9 | 21 | 255 |
| sw06-p5 | 17 | 19 | 255 |
| sw07-p4 | 1 | 18 | 255 |
| sw07-p5 | 9 | 22 | 255 |
| sw08-p2 | 17 | 28 | 255 |
| sw08-p4 | 17 | 18 | 255 |
| sw08-p5 | 1 | 18 | 255 |

## Flows

| flow | route | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|
| s0(id=1 S3->S1) | S3->sw01->sw02->S1 | 7 | 0 | 29200 | yes |
| s1(id=2 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | 6 | 0 | 43280 | yes |
| s2(id=3 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | - | - | - | no |
| s3(id=4 S1->S3) | S1->sw02->sw01->S3 | 6 | 24960 | 26000 | yes |
| s4(id=5 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | - | - | - | no |
| s5(id=6 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | 6 | 24960 | 33040 | yes |
| s6(id=7 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | 7 | 49920 | 39440 | yes |
| s7(id=8 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | - | - | - | no |
| s8(id=9 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 6 | 24960 | 54160 | yes |
| s9(id=10 S1->S3) | S1->sw02->sw01->S3 | - | - | - | no |
| s10(id=11 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | - | - | - | no |
| s11(id=12 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | 7 | 74880 | 42000 | yes |
| s12(id=13 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | - | - | - | no |
| s13(id=14 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 7 | 0 | 33040 | yes |
| s14(id=15 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | - | - | - | no |
| s15(id=16 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | - | - | - | no |
| s16(id=17 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | - | - | - | no |
| s17(id=18 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | - | - | - | no |
| s18(id=19 S3->S1) | S3->sw01->sw02->S1 | 6 | 74880 | 29200 | yes |
| s19(id=20 S3->S1) | S3->sw01->sw02->S1 | 6 | 49920 | 24720 | yes |

## Per-hop windows (slack_ns > 0 means this window was enlarged)

| flow | egress port | queue | psi (ns) | delta (ns) |
|---|---|---|---|---|
| s0(id=1 S3->S1) | S3-p0 | Q7 | 0 | 12480 |
| s0(id=1 S3->S1) | sw01-p5 | Q7 | 8320 | 12480 |
| s0(id=1 S3->S1) | sw02-p2 | Q7 | 16640 | 12480 |
| s1(id=2 S2->S1) | S2-p0 | Q6 | 0 | 12480 |
| s1(id=2 S2->S1) | sw08-p4 | Q6 | 7680 | 12480 |
| s1(id=2 S2->S1) | sw06-p5 | Q6 | 15360 | 12480 |
| s1(id=2 S2->S1) | sw04-p4 | Q6 | 23040 | 12480 |
| s1(id=2 S2->S1) | sw02-p2 | Q6 | 30720 | 12480 |
| s3(id=4 S1->S3) | S1-p0 | Q6 | 24960 | 12480 |
| s3(id=4 S1->S3) | sw02-p5 | Q6 | 31680 | 12480 |
| s3(id=4 S1->S3) | sw01-p2 | Q6 | 38400 | 12480 |
| s5(id=6 S2->S1) | S2-p0 | Q6 | 24960 | 12480 |
| s5(id=6 S2->S1) | sw08-p4 | Q6 | 30080 | 12480 |
| s5(id=6 S2->S1) | sw06-p5 | Q6 | 35200 | 12480 |
| s5(id=6 S2->S1) | sw04-p4 | Q6 | 40320 | 12480 |
| s5(id=6 S2->S1) | sw02-p2 | Q6 | 45440 | 12480 |
| s6(id=7 S2->S1) | S2-p0 | Q7 | 49920 | 12480 |
| s6(id=7 S2->S1) | sw08-p4 | Q7 | 56640 | 12480 |
| s6(id=7 S2->S1) | sw06-p5 | Q7 | 63360 | 12480 |
| s6(id=7 S2->S1) | sw04-p4 | Q7 | 70080 | 12480 |
| s6(id=7 S2->S1) | sw02-p2 | Q7 | 76800 | 12480 |
| s8(id=9 S3->S2) | S3-p0 | Q6 | 24960 | 12480 |
| s8(id=9 S3->S2) | sw01-p4 | Q6 | 33280 | 12480 |
| s8(id=9 S3->S2) | sw03-p5 | Q6 | 41600 | 12480 |
| s8(id=9 S3->S2) | sw05-p4 | Q6 | 49920 | 12480 |
| s8(id=9 S3->S2) | sw07-p5 | Q6 | 58240 | 12480 |
| s8(id=9 S3->S2) | sw08-p2 | Q6 | 66560 | 12480 |
| s11(id=12 S2->S1) | S2-p0 | Q7 | 74880 | 12480 |
| s11(id=12 S2->S1) | sw08-p4 | Q7 | 80000 | 12480 |
| s11(id=12 S2->S1) | sw06-p5 | Q7 | 85120 | 12480 |
| s11(id=12 S2->S1) | sw04-p4 | Q7 | 90240 | 12480 |
| s11(id=12 S2->S1) | sw02-p2 | Q7 | 104320 | 12480 |
| s13(id=14 S1->S2) | S1-p0 | Q7 | 0 | 12480 |
| s13(id=14 S1->S2) | sw02-p4 | Q7 | 5120 | 12480 |
| s13(id=14 S1->S2) | sw04-p5 | Q7 | 10240 | 12480 |
| s13(id=14 S1->S2) | sw06-p4 | Q7 | 15360 | 12480 |
| s13(id=14 S1->S2) | sw08-p2 | Q7 | 20480 | 12480 |
| s18(id=19 S3->S1) | S3-p0 | Q6 | 74880 | 12480 |
| s18(id=19 S3->S1) | sw01-p5 | Q6 | 83200 | 12480 |
| s18(id=19 S3->S1) | sw02-p2 | Q6 | 91520 | 12480 |
| s19(id=20 S3->S1) | S3-p0 | Q6 | 49920 | 12480 |
| s19(id=20 S3->S1) | sw01-p5 | Q6 | 56000 | 12480 |
| s19(id=20 S3->S1) | sw02-p2 | Q6 | 62080 | 12480 |

## Constraint check

- C1-C7, C9: OK
- seed-integrity (no SMT-fixed flow's placement changed): OK

## GCL per egress port

### sw01-p2  (9 entries, util 1.5600 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 25920 0x7F # 01111111   Q6
sgs 499200 0x40 # 01000000   Q6
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
sgs 20800 0x7F # 01111111   Q6
sgs 75200 0x40 # 01000000   Q6
sgs 41600 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 75200 0x40 # 01000000   Q6
sgs 41600 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 75200 0x40 # 01000000   Q6
sgs 41600 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 41920 0x40 # 01000000   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw01-p5  (32 entries, util 15.6000 %)

```
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 6080 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 14720 0xBF # 10111111   Q7
sgs 64000 0x40 # 01000000   Q6
sgs 2880 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 6080 0x3F # 00111111   BE
sgs 91200 0x40 # 01000000   Q6
sgs 2880 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 6080 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 14720 0xBF # 10111111   Q7
sgs 64000 0x40 # 01000000   Q6
sgs 2880 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 29120 0x7F # 01111111   Q6
sgs 6080 0x3F # 00111111   BE
sgs 82880 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (29 entries, util 28.0800 %)

```
sgs 16640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 1600 0x3F # 00111111   BE
sgs 43840 0x40 # 01000000   Q6
sgs 2240 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 2240 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 42880 0x80 # 10000000   Q7
sgs 69440 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 1600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 18880 0x3F # 00111111   BE
sgs 18560 0x40 # 01000000   Q6
sgs 136000 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 1600 0x3F # 00111111   BE
sgs 43840 0x40 # 01000000   Q6
sgs 16960 0x3F # 00111111   BE
sgs 17280 0x40 # 01000000   Q6
sgs 107840 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 1600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 18880 0x3F # 00111111   BE
sgs 17280 0x40 # 01000000   Q6
sgs 120640 0x3F # 00111111   BE
```

### sw02-p4  (20 entries, util 6.2400 %)

```
sgs 5120 0x3F # 00111111   BE
sgs 50240 0x80 # 10000000   Q7
sgs 44800 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 5120 0x3F # 00111111   BE
sgs 50240 0x80 # 10000000   Q7
sgs 44800 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 5120 0x3F # 00111111   BE
sgs 50240 0x80 # 10000000   Q7
sgs 44800 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 5120 0x3F # 00111111   BE
sgs 45120 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p5  (9 entries, util 1.5600 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 19200 0x7F # 01111111   Q6
sgs 505920 0x40 # 01000000   Q6
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

### sw03-p5  (18 entries, util 6.2400 %)

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

### sw04-p4  (18 entries, util 12.4800 %)

```
sgs 23040 0x7F # 01111111   Q6
sgs 29760 0x40 # 01000000   Q6
sgs 17280 0xBF # 10111111   Q7
sgs 75200 0x80 # 10000000   Q7
sgs 4800 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 122240 0x40 # 01000000   Q6
sgs 4800 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 122240 0x40 # 01000000   Q6
sgs 4800 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 99200 0x40 # 01000000   Q6
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (20 entries, util 6.2400 %)

```
sgs 10240 0x3F # 00111111   BE
sgs 50240 0x80 # 10000000   Q7
sgs 39680 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 10240 0x3F # 00111111   BE
sgs 50240 0x80 # 10000000   Q7
sgs 39680 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 10240 0x3F # 00111111   BE
sgs 50240 0x80 # 10000000   Q7
sgs 39680 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 10240 0x3F # 00111111   BE
sgs 40000 0x80 # 10000000   Q7
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (18 entries, util 6.2400 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 75200 0x40 # 01000000   Q6
sgs 24960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 75200 0x40 # 01000000   Q6
sgs 24960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 75200 0x40 # 01000000   Q6
sgs 24960 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 25280 0x40 # 01000000   Q6
sgs 24960 0xBF # 10111111   Q7
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

### sw06-p4  (21 entries, util 6.2400 %)

```
sgs 12480 0x40 # 01000000   Q6
sgs 2880 0x3F # 00111111   BE
sgs 75200 0x80 # 10000000   Q7
sgs 9600 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 75200 0x80 # 10000000   Q7
sgs 9600 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 75200 0x80 # 10000000   Q7
sgs 9600 0x3F # 00111111   BE
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 59840 0x80 # 10000000   Q7
sgs 24960 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (19 entries, util 12.4800 %)

```
sgs 15360 0x7F # 01111111   Q6
sgs 32320 0x40 # 01000000   Q6
sgs 2240 0x3F # 00111111   BE
sgs 13440 0xBF # 10111111   Q7
sgs 74240 0x80 # 10000000   Q7
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 122240 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 122240 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 106880 0x40 # 01000000   Q6
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

### sw07-p5  (22 entries, util 6.2400 %)

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

### sw08-p2  (28 entries, util 12.4800 %)

```
sgs 20480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 16960 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 76160 0x40 # 01000000   Q6
sgs 7360 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 16960 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 76160 0x40 # 01000000   Q6
sgs 7360 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 16960 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 76160 0x40 # 01000000   Q6
sgs 7360 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 20480 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 16960 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 55680 0x40 # 01000000   Q6
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p4  (18 entries, util 12.4800 %)

```
sgs 7680 0x3F # 00111111   BE
sgs 34880 0x40 # 01000000   Q6
sgs 14080 0x3F # 00111111   BE
sgs 73280 0x80 # 10000000   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 7680 0x3F # 00111111   BE
sgs 122240 0x40 # 01000000   Q6
sgs 20160 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 7680 0x3F # 00111111   BE
sgs 122240 0x40 # 01000000   Q6
sgs 20160 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 7680 0x3F # 00111111   BE
sgs 114560 0x40 # 01000000   Q6
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

