# Heuristic-enlarged GCL schedule (Problem 2: window enlargement)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Time-sensitive PCPs considered: [6, 7]
- Seeded from SMT run: **result/result-2026-10-10-dataset-testbed-4-saf/smt-c9-on/4-saf-retimed-c9on**

## Admission (unchanged by this package -- it only widens windows)

SMT-fixed flows: **11**/11. This package never admits a flow itself; it banks slack for a later admission pass (`prob_3_admit`, Problem 3) to use.

## Opportunistic idle top-up (Step 7 -- see enlarge.py)

Total: **9515840 ns**, drawn from idle capacity on ports at or below utilisation 0.2, independent of any route's deadline-slack budget.

| port | queue | applied (ns) |
|---|---|---|
| S1-p0 | Q6 | 547520 |
| S1-p0 | Q7 | 94400 |
| S2-p0 | Q6 | 235840 |
| S2-p0 | Q7 | 406080 |
| S3-p0 | Q6 | 659200 |
| S3-p0 | Q7 | 1280 |
| sw01-p4 | Q6 | 650880 |
| sw01-p4 | Q7 | 6720 |
| sw02-p2 | Q6 | 602240 |
| sw02-p4 | Q6 | 543040 |
| sw02-p4 | Q7 | 95040 |
| sw03-p5 | Q6 | 642560 |
| sw03-p5 | Q7 | 11520 |
| sw04-p4 | Q6 | 618560 |
| sw04-p5 | Q6 | 537920 |
| sw04-p5 | Q7 | 95680 |
| sw05-p4 | Q6 | 633920 |
| sw05-p4 | Q7 | 16320 |
| sw06-p4 | Q6 | 532160 |
| sw06-p4 | Q7 | 96320 |
| sw06-p5 | Q6 | 633920 |
| sw07-p5 | Q6 | 624960 |
| sw07-p5 | Q7 | 20160 |
| sw08-p2 | Q6 | 561280 |
| sw08-p4 | Q6 | 648320 |

## Opportunistic window creation (Step 8 -- see enlarge.py)

**4** brand-new window(s) opened, **49920 ns** total, on ports at or below utilisation 0.2 whose TT queue had zero windows before this run.

| port | queue | size (ns) |
|---|---|---|
| sw02-p2 | Q7 | 12480 |
| sw04-p4 | Q7 | 12480 |
| sw06-p5 | Q7 | 12480 |
| sw08-p4 | Q7 | 12480 |

## Best-effort gap equalization (Step 9 -- see enlarge.py)

**4724480 ns** given back from Steps 7/8's growth so each port's leftover non-TAS gaps land close to equal, instead of one gap staying huge while a neighbour is squeezed to the bare 1-tick C10 minimum.

| port | given back (ns) |
|---|---|
| S3-p0 | 360960 |
| sw01-p4 | 359040 |
| sw03-p5 | 357760 |
| sw05-p4 | 356480 |
| sw07-p5 | 355200 |
| S2-p0 | 336320 |
| S1-p0 | 319360 |
| sw02-p4 | 311680 |
| sw04-p5 | 304000 |
| sw06-p4 | 296320 |
| sw02-p2 | 262400 |
| sw04-p4 | 262400 |
| sw06-p5 | 262400 |
| sw08-p4 | 262400 |
| sw08-p2 | 240640 |
| sw03-p4 | 17920 |
| sw05-p5 | 16960 |
| sw01-p2 | 15680 |
| sw07-p4 | 14080 |
| sw08-p5 | 12480 |

## Opportunistic overlay window creation (Step 10 -- see enlarge.py)

**29** new overlay window(s), **4726080 ns** total, carved out of already-open best-effort spans on ports at or below utilisation 0.2 -- best-effort stays reachable inside each one (gate mask keeps its BE bits set), so none of this is closed off from BE.

| port | queue | size (ns) |
|---|---|---|
| S1-p0 | Q6 | 62400 |
| S1-p0 | Q7 | 212160 |
| S2-p0 | Q6 | 124160 |
| S2-p0 | Q7 | 212160 |
| S3-p0 | Q6 | 161280 |
| S3-p0 | Q7 | 199680 |
| sw01-p4 | Q6 | 85440 |
| sw01-p4 | Q7 | 199680 |
| sw02-p2 | Q6 | 149760 |
| sw02-p2 | Q7 | 200320 |
| sw02-p4 | Q7 | 213120 |
| sw03-p5 | Q6 | 95680 |
| sw03-p5 | Q7 | 228480 |
| sw04-p4 | Q6 | 149760 |
| sw04-p4 | Q7 | 195200 |
| sw04-p5 | Q6 | 61440 |
| sw04-p5 | Q7 | 215040 |
| sw05-p4 | Q6 | 128960 |
| sw05-p4 | Q7 | 230400 |
| sw06-p4 | Q6 | 92160 |
| sw06-p4 | Q7 | 196800 |
| sw06-p5 | Q6 | 149760 |
| sw06-p5 | Q7 | 188480 |
| sw07-p5 | Q6 | 162240 |
| sw07-p5 | Q7 | 215040 |
| sw08-p2 | Q6 | 122880 |
| sw08-p2 | Q7 | 142080 |
| sw08-p4 | Q6 | 149760 |
| sw08-p4 | Q7 | 181760 |

## Candidate routes (P^cand = routes of the fixed flows above)

| route | PCPs carried | flows |
|---|---|---|
| S1->sw02->sw04->sw06->sw08->S2 | Q6 (1) | 1 |
| S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | Q6 (2), Q7 (1) | 3 |
| S2->sw08->sw06->sw04->sw02->S1 | Q6 (1) | 1 |
| S2->sw08->sw07->sw05->sw03->sw01->S3 | Q6 (1), Q7 (2) | 3 |
| S3->sw01->sw03->sw05->sw07->sw08->S2 | Q6 (2), Q7 (1) | 3 |

## Per-link enlargement accounting

| link | sharing eta | route-safe slack (ns) | link budget (ns) | final slack (ns) | applied (ns) |
|---|---|---|---|---|---|
| S1-p0 | 2 | Q6:15116, Q7:46314 | 61430 | Q6:15116, Q7:18298 | Q6:366720, Q7:263680 |
| S2-p0 | 2 | Q6:37361, Q7:19018 | 56378 | Q6:27132, Q7:19018 | Q6:237440, Q7:450240 |
| sw01-p2 | 2 | Q6:15183, Q7:22057 | 37240 | Q6:15183, Q7:19894 | Q6:5760, Q7:13440 |
| sw02-p4 | 2 | Q6:11962, Q7:41953 | 53914 | Q6:11962, Q7:17624 | Q6:304320, Q7:264640 |
| sw03-p4 | 2 | Q6:12015, Q7:18221 | 30236 | Q6:12015, Q7:16475 | Q6:4800, Q7:5440 |
| sw04-p5 | 2 | Q6:9466, Q7:38114 | 47580 | Q6:9466, Q7:17031 | Q6:365760, Q7:266560 |
| sw05-p5 | 2 | Q6:9508, Q7:15052 | 24560 | Q6:9508, Q7:13643 | Q6:3840, Q7:1920 |
| sw06-p4 | 2 | Q6:7490, Q7:34722 | 42213 | Q6:7490, Q7:16502 | Q6:396480, Q7:248320 |
| sw07-p4 | 2 | Q6:7524, Q7:12434 | 19958 | Q6:7524, Q7:11298 | Q6:2880, Q7:1600 |
| sw08-p2 | 2 | Q6:23882, Q7:94025 | 117907 | Q6:23882, Q7:53954 | Q6:501760, Q7:142080 |
| sw08-p5 | 2 | Q6:6646, Q7:10272 | 16917 | Q6:6646, Q7:9298 | Q6:1920, Q7:1280 |
| S3-p0 | 1 | Q6:16137, Q7:38155 | 54292 | Q6:16137, Q7:23930 | Q6:500480, Q7:199680 |
| sw01-p4 | 1 | Q6:13967, Q7:32552 | 46519 | Q6:13967, Q7:20339 | Q6:417920, Q7:199680 |
| sw02-p2 | 1 | Q6:83805, Q7:0 | 83805 | Q6:83805 | Q6:573120, Q7:212800 |
| sw03-p5 | 1 | Q6:12090, Q7:27771 | 39861 | Q6:12090, Q7:17286 | Q6:421120, Q7:228480 |
| sw04-p4 | 1 | Q6:74094, Q7:0 | 74094 | Q6:74094 | Q6:579840, Q7:207680 |
| sw05-p4 | 1 | Q6:10465, Q7:23693 | 34158 | Q6:10465, Q7:14691 | Q6:447360, Q7:230400 |
| sw06-p5 | 1 | Q6:65508, Q7:0 | 65508 | Q6:65508 | Q6:586560, Q7:200960 |
| sw07-p5 | 1 | Q6:9058, Q7:20214 | 29271 | Q6:9058, Q7:12486 | Q6:473600, Q7:215040 |
| sw08-p4 | 1 | Q6:57916, Q7:0 | 57916 | Q6:57916 | Q6:593280, Q7:194240 |

Total applied: **10333120 ns** across 20 port(s). Network total slack now banked: **10537600 ns**. GCL_size overflow: 0.

## Per-port GCL entries: before (SMT) vs. after (heuristic-enlarged)

| port | SMT entries | enlarged entries | GCL_size |
|---|---|---|---|
| sw01-p2 | 29 | 19 | 255 |
| sw01-p4 | 17 | 24 | 255 |
| sw02-p2 | 3 | 11 | 255 |
| sw02-p4 | 21 | 20 | 255 |
| sw03-p4 | 29 | 19 | 255 |
| sw03-p5 | 17 | 24 | 255 |
| sw04-p4 | 3 | 10 | 255 |
| sw04-p5 | 21 | 18 | 255 |
| sw05-p4 | 17 | 24 | 255 |
| sw05-p5 | 29 | 19 | 255 |
| sw06-p4 | 21 | 17 | 255 |
| sw06-p5 | 3 | 10 | 255 |
| sw07-p4 | 29 | 19 | 255 |
| sw07-p5 | 17 | 21 | 255 |
| sw08-p2 | 25 | 20 | 255 |
| sw08-p4 | 3 | 10 | 255 |
| sw08-p5 | 29 | 19 | 255 |

## Flows

| flow | route | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|
| s0(id=1 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 7 | 24960 | 46160 | yes |
| s1(id=2 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | - | - | - | no |
| s2(id=3 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 7 | 24960 | 42000 | yes |
| s3(id=4 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | - | - | - | no |
| s4(id=5 S3->S1) | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | - | - | - | no |
| s5(id=6 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | 6 | 49920 | 66960 | yes |
| s6(id=7 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | - | - | - | no |
| s7(id=8 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 7 | 0 | 54160 | yes |
| s8(id=9 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | 7 | 74880 | 74000 | yes |
| s9(id=10 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 6 | 49920 | 50960 | yes |
| s10(id=11 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | - | - | - | no |
| s11(id=12 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | - | - | - | no |
| s12(id=13 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 6 | 0 | 43280 | yes |
| s13(id=14 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 6 | 0 | 56080 | yes |
| s14(id=15 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | - | - | - | no |
| s15(id=16 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | - | - | - | no |
| s16(id=17 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | - | - | - | no |
| s17(id=18 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | 6 | 74880 | 39440 | yes |
| s18(id=19 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 6 | 49920 | 54160 | yes |
| s19(id=20 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | 6 | 24960 | 54800 | yes |

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
sgs 19520 0x3F # 00111111   BE
sgs 25920 0x80 # 10000000   Q7
sgs 79360 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0x3F # 00111111   BE
sgs 14400 0x40 # 01000000   Q6
sgs 160000 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 38720 0x40 # 01000000   Q6
sgs 135680 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0x3F # 00111111   BE
sgs 14400 0x40 # 01000000   Q6
sgs 118400 0x3F # 00111111   BE
```

### sw01-p4  (24 entries, util 12.4800 %)

```
sgs 8640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 10560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13440 0x3F # 00111111   BE
sgs 73280 0x40 # 01000000   Q6
sgs 19200 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 8640 0x3F # 00111111   BE
sgs 122240 0x40 # 01000000   Q6
sgs 19200 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 8640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 10560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13440 0x3F # 00111111   BE
sgs 73280 0x40 # 01000000   Q6
sgs 19200 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 8640 0x3F # 00111111   BE
sgs 113600 0x40 # 01000000   Q6
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (11 entries, util 1.5600 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 1600 0x3F # 00111111   BE
sgs 435840 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p4  (20 entries, util 15.6000 %)

```
sgs 7680 0x3F # 00111111   BE
sgs 34880 0x40 # 01000000   Q6
sgs 14080 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 13440 0xBF # 10111111   Q7
sgs 64000 0x80 # 10000000   Q7
sgs 3520 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 7680 0x3F # 00111111   BE
sgs 138880 0x40 # 01000000   Q6
sgs 3520 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 7680 0x3F # 00111111   BE
sgs 138880 0x40 # 01000000   Q6
sgs 3520 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 7680 0x3F # 00111111   BE
sgs 131200 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

### sw03-p4  (19 entries, util 21.8400 %)

```
sgs 33280 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 3520 0x3F # 00111111   BE
sgs 47360 0x40 # 01000000   Q6
sgs 19200 0x3F # 00111111   BE
sgs 17920 0x80 # 10000000   Q7
sgs 86720 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 16320 0x3F # 00111111   BE
sgs 14080 0x40 # 01000000   Q6
sgs 157120 0x3F # 00111111   BE
sgs 25280 0x80 # 10000000   Q7
sgs 3520 0x3F # 00111111   BE
sgs 35200 0x40 # 01000000   Q6
sgs 136000 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 16320 0x3F # 00111111   BE
sgs 14080 0x40 # 01000000   Q6
sgs 123840 0x3F # 00111111   BE
```

### sw03-p5  (24 entries, util 12.4800 %)

```
sgs 16960 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 8960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 14400 0xBF # 10111111   Q7
sgs 73920 0x40 # 01000000   Q6
sgs 10880 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 16960 0x7F # 01111111   Q6
sgs 122240 0x40 # 01000000   Q6
sgs 10880 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 16960 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 8960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 14400 0xBF # 10111111   Q7
sgs 73920 0x40 # 01000000   Q6
sgs 10880 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 16960 0x7F # 01111111   Q6
sgs 105280 0x40 # 01000000   Q6
sgs 27840 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p4  (10 entries, util 1.5600 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 45120 0xBF # 10111111   Q7
sgs 442560 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p5  (18 entries, util 15.6000 %)

```
sgs 15360 0x7F # 01111111   Q6
sgs 32320 0x40 # 01000000   Q6
sgs 2240 0x3F # 00111111   BE
sgs 13440 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0xBF # 10111111   Q7
sgs 64000 0x80 # 10000000   Q7
sgs 45760 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 138880 0x40 # 01000000   Q6
sgs 45760 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 138880 0x40 # 01000000   Q6
sgs 45760 0xBF # 10111111   Q7
sgs 15360 0x7F # 01111111   Q6
sgs 123520 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p4  (24 entries, util 12.4800 %)

```
sgs 25280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 7360 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 15360 0xBF # 10111111   Q7
sgs 74560 0x40 # 01000000   Q6
sgs 2560 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 25280 0x7F # 01111111   Q6
sgs 122240 0x40 # 01000000   Q6
sgs 2560 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
sgs 25280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 7360 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 15360 0xBF # 10111111   Q7
sgs 74560 0x40 # 01000000   Q6
sgs 2560 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
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
sgs 18240 0x3F # 00111111   BE
sgs 14400 0x80 # 10000000   Q7
sgs 89600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 18240 0x3F # 00111111   BE
sgs 13760 0x40 # 01000000   Q6
sgs 155520 0x3F # 00111111   BE
sgs 27840 0x80 # 10000000   Q7
sgs 2880 0x3F # 00111111   BE
sgs 32960 0x40 # 01000000   Q6
sgs 136320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 18240 0x3F # 00111111   BE
sgs 13760 0x40 # 01000000   Q6
sgs 130560 0x3F # 00111111   BE
```

### sw06-p4  (17 entries, util 15.6000 %)

```
sgs 23040 0x7F # 01111111   Q6
sgs 29760 0x40 # 01000000   Q6
sgs 17280 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 15360 0xBF # 10111111   Q7
sgs 64000 0x80 # 10000000   Q7
sgs 38080 0xBF # 10111111   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 138880 0x40 # 01000000   Q6
sgs 38080 0xBF # 10111111   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 138880 0x40 # 01000000   Q6
sgs 38080 0xBF # 10111111   Q7
sgs 23040 0x7F # 01111111   Q6
sgs 115840 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 49920 0xBF # 10111111   Q7
```

### sw06-p5  (10 entries, util 1.5600 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 38400 0xBF # 10111111   Q7
sgs 449280 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw07-p4  (19 entries, util 21.8400 %)

```
sgs 16640 0x3F # 00111111   BE
sgs 31040 0x80 # 10000000   Q7
sgs 2880 0x3F # 00111111   BE
sgs 45440 0x40 # 01000000   Q6
sgs 17280 0x3F # 00111111   BE
sgs 14080 0x80 # 10000000   Q7
sgs 89280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 21440 0x3F # 00111111   BE
sgs 13440 0x40 # 01000000   Q6
sgs 152640 0x3F # 00111111   BE
sgs 31040 0x80 # 10000000   Q7
sgs 2880 0x3F # 00111111   BE
sgs 29440 0x40 # 01000000   Q6
sgs 136640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 21440 0x3F # 00111111   BE
sgs 13440 0x40 # 01000000   Q6
sgs 136000 0x3F # 00111111   BE
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
sgs 17280 0xBF # 10111111   Q7
sgs 92480 0x40 # 01000000   Q6
sgs 19200 0xBF # 10111111   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 150080 0x40 # 01000000   Q6
sgs 19200 0xBF # 10111111   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 25280 0x40 # 01000000   Q6
sgs 2560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 17280 0xBF # 10111111   Q7
sgs 92480 0x40 # 01000000   Q6
sgs 19200 0xBF # 10111111   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 119360 0x40 # 01000000   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p4  (10 entries, util 1.5600 %)

```
sgs 12480 0x80 # 10000000   Q7
sgs 37440 0x7F # 01111111   Q6
sgs 31680 0xBF # 10111111   Q7
sgs 456000 0x40 # 01000000   Q6
sgs 12480 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 50240 0xBF # 10111111   Q7
sgs 49920 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p5  (19 entries, util 21.8400 %)

```
sgs 8320 0x3F # 00111111   BE
sgs 34240 0x80 # 10000000   Q7
sgs 2880 0x3F # 00111111   BE
sgs 43840 0x40 # 01000000   Q6
sgs 16320 0x3F # 00111111   BE
sgs 13760 0x80 # 10000000   Q7
sgs 88960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 24640 0x3F # 00111111   BE
sgs 13120 0x40 # 01000000   Q6
sgs 149760 0x3F # 00111111   BE
sgs 34240 0x80 # 10000000   Q7
sgs 2880 0x3F # 00111111   BE
sgs 25920 0x40 # 01000000   Q6
sgs 136960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 24640 0x3F # 00111111   BE
sgs 13120 0x40 # 01000000   Q6
sgs 141440 0x3F # 00111111   BE
```

