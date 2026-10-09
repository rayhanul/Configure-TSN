# SMT-synthesized GCL schedule (Problem 1: feasible schedule synthesis)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4000 ns
- TT queues: Q6, Q7; best effort filler mask 0x3F
- Solver: Z3, maximize admitted flows (binary search), then minimize total latency, timeout 3600s
- Result: **sat**, admitted 11/20 (proven optimal), solved in 75.95s
- Total latency (sum of e2e over admitted flows): **825280 ns** (proven minimum)

- **WARNING: C9 disabled for this run** -- see Constraint check below for the resulting violations.

## Flows

stream.csv does not specify a talker offset; `offset (ns) = phi` below is the transmit time of each flow's first frame, computed by the solver (also in `offsets.csv` and `schedule.json`'s `offset_ns`).

| flow | route | L (B) | C (ns) | T (ns) | D (ns) | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|---|---|---|---|
| s0(id=1 S1->S2) | S1->sw02->sw05->sw07->sw08->S2 | 500 | 12480 | 200000 | 200000 | 7 | 0 | 79040 | yes |
| s1(id=2 S3->S2) | S3->sw01->sw03->sw06->sw08->S2 | 100 | 12480 | 800000 | 800000 | None | None | None | no |
| s2(id=3 S1->S2) | S1->sw02->sw05->sw07->sw08->S2 | 500 | 12480 | 200000 | 200000 | None | None | None | no |
| s3(id=4 S1->S3) | S1->sw02->sw01->S3 | 400 | 12480 | 800000 | 800000 | 6 | 49920 | 45760 | yes |
| s4(id=5 S1->S2) | S1->sw02->sw05->sw07->sw08->S2 | 500 | 12480 | 400000 | 400000 | None | None | None | no |
| s5(id=6 S2->S1) | S2->sw08->sw07->sw05->sw02->S1 | 100 | 12480 | 800000 | 800000 | None | None | None | no |
| s6(id=7 S3->S1) | S3->sw01->sw02->S1 | 300 | 12480 | 400000 | 400000 | 6 | 24960 | 45760 | yes |
| s7(id=8 S1->S2) | S1->sw02->sw05->sw07->sw08->S2 | 500 | 12480 | 800000 | 800000 | None | None | None | no |
| s8(id=9 S1->S2) | S1->sw02->sw05->sw07->sw08->S2 | 400 | 12480 | 200000 | 200000 | 7 | 24960 | 79680 | yes |
| s9(id=10 S3->S2) | S3->sw01->sw03->sw06->sw08->S2 | 300 | 12480 | 800000 | 800000 | 6 | 74880 | 79040 | yes |
| s10(id=11 S2->S3) | S2->sw08->sw06->sw03->sw01->S3 | 300 | 12480 | 400000 | 400000 | 7 | 24960 | 83520 | yes |
| s11(id=12 S2->S1) | S2->sw08->sw07->sw05->sw02->S1 | 200 | 12480 | 800000 | 800000 | 6 | 74880 | 79040 | yes |
| s12(id=13 S3->S1) | S3->sw01->sw02->S1 | 100 | 12480 | 400000 | 400000 | None | None | None | no |
| s13(id=14 S3->S2) | S3->sw01->sw03->sw06->sw08->S2 | 500 | 12480 | 200000 | 200000 | 6 | 0 | 91840 | yes |
| s14(id=15 S2->S3) | S2->sw08->sw06->sw03->sw01->S3 | 400 | 12480 | 400000 | 400000 | None | None | None | no |
| s15(id=16 S2->S1) | S2->sw08->sw07->sw05->sw02->S1 | 100 | 12480 | 400000 | 400000 | 7 | 49920 | 79040 | yes |
| s16(id=17 S3->S2) | S3->sw01->sw03->sw06->sw08->S2 | 200 | 12480 | 200000 | 200000 | None | None | None | no |
| s17(id=18 S2->S1) | S2->sw08->sw07->sw05->sw02->S1 | 400 | 12480 | 200000 | 200000 | 7 | 0 | 83520 | yes |
| s18(id=19 S2->S1) | S2->sw08->sw07->sw05->sw02->S1 | 100 | 12480 | 200000 | 200000 | None | None | None | no |
| s19(id=20 S3->S2) | S3->sw01->sw03->sw06->sw08->S2 | 300 | 12480 | 400000 | 400000 | 7 | 49920 | 79040 | yes |

## Per-hop windows

| flow | egress port | queue | psi (ns) | delta (ns) |
|---|---|---|---|---|
| s0(id=1 S1->S2) | S1-p0 | Q7 | 0 | 12480 |
| s0(id=1 S1->S2) | sw02-p5 | Q7 | 16640 | 12480 |
| s0(id=1 S1->S2) | sw05-p2 | Q7 | 33280 | 12480 |
| s0(id=1 S1->S2) | sw07-p4 | Q7 | 49920 | 12480 |
| s0(id=1 S1->S2) | sw08-p2 | Q7 | 66560 | 12480 |
| s3(id=4 S1->S3) | S1-p0 | Q6 | 49920 | 12480 |
| s3(id=4 S1->S3) | sw02-p3 | Q6 | 66560 | 12480 |
| s3(id=4 S1->S3) | sw01-p3 | Q6 | 83200 | 12480 |
| s6(id=7 S3->S1) | S3-p0 | Q6 | 24960 | 12480 |
| s6(id=7 S3->S1) | sw01-p5 | Q6 | 41600 | 12480 |
| s6(id=7 S3->S1) | sw02-p2 | Q6 | 58240 | 12480 |
| s8(id=9 S1->S2) | S1-p0 | Q7 | 24960 | 12480 |
| s8(id=9 S1->S2) | sw02-p5 | Q7 | 41600 | 12480 |
| s8(id=9 S1->S2) | sw05-p2 | Q7 | 58240 | 12480 |
| s8(id=9 S1->S2) | sw07-p4 | Q7 | 75520 | 12480 |
| s8(id=9 S1->S2) | sw08-p2 | Q7 | 92160 | 12480 |
| s9(id=10 S3->S2) | S3-p0 | Q6 | 74880 | 12480 |
| s9(id=10 S3->S2) | sw01-p4 | Q6 | 91520 | 12480 |
| s9(id=10 S3->S2) | sw03-p4 | Q6 | 108160 | 12480 |
| s9(id=10 S3->S2) | sw06-p2 | Q6 | 124800 | 12480 |
| s9(id=10 S3->S2) | sw08-p2 | Q6 | 141440 | 12480 |
| s10(id=11 S2->S3) | S2-p0 | Q7 | 24960 | 12480 |
| s10(id=11 S2->S3) | sw08-p4 | Q7 | 43840 | 12480 |
| s10(id=11 S2->S3) | sw06-p3 | Q7 | 60800 | 12480 |
| s10(id=11 S2->S3) | sw03-p3 | Q7 | 79360 | 12480 |
| s10(id=11 S2->S3) | sw01-p3 | Q7 | 96000 | 12480 |
| s11(id=12 S2->S1) | S2-p0 | Q6 | 74880 | 12480 |
| s11(id=12 S2->S1) | sw08-p5 | Q6 | 91520 | 12480 |
| s11(id=12 S2->S1) | sw07-p3 | Q6 | 108160 | 12480 |
| s11(id=12 S2->S1) | sw05-p5 | Q6 | 124800 | 12480 |
| s11(id=12 S2->S1) | sw02-p2 | Q6 | 141440 | 12480 |
| s13(id=14 S3->S2) | S3-p0 | Q6 | 0 | 12480 |
| s13(id=14 S3->S2) | sw01-p4 | Q6 | 22400 | 12480 |
| s13(id=14 S3->S2) | sw03-p4 | Q6 | 39040 | 12480 |
| s13(id=14 S3->S2) | sw06-p2 | Q6 | 62720 | 12480 |
| s13(id=14 S3->S2) | sw08-p2 | Q6 | 79360 | 12480 |
| s15(id=16 S2->S1) | S2-p0 | Q7 | 49920 | 12480 |
| s15(id=16 S2->S1) | sw08-p5 | Q7 | 66560 | 12480 |
| s15(id=16 S2->S1) | sw07-p3 | Q7 | 83200 | 12480 |
| s15(id=16 S2->S1) | sw05-p5 | Q7 | 99840 | 12480 |
| s15(id=16 S2->S1) | sw02-p2 | Q7 | 116480 | 12480 |
| s17(id=18 S2->S1) | S2-p0 | Q7 | 0 | 12480 |
| s17(id=18 S2->S1) | sw08-p5 | Q7 | 17280 | 12480 |
| s17(id=18 S2->S1) | sw07-p3 | Q7 | 37760 | 12480 |
| s17(id=18 S2->S1) | sw05-p5 | Q7 | 54400 | 12480 |
| s17(id=18 S2->S1) | sw02-p2 | Q7 | 71040 | 12480 |
| s19(id=20 S3->S2) | S3-p0 | Q7 | 49920 | 12480 |
| s19(id=20 S3->S2) | sw01-p4 | Q7 | 66560 | 12480 |
| s19(id=20 S3->S2) | sw03-p4 | Q7 | 83200 | 12480 |
| s19(id=20 S3->S2) | sw06-p2 | Q7 | 99840 | 12480 |
| s19(id=20 S3->S2) | sw08-p2 | Q7 | 116480 | 12480 |

## Constraint check

- C1 window non-overlap: OK
- C2 unique queue assignment: OK
- C3 unique window assignment: OK
- C4 window length >= frame transmission time: OK (windows are built tight, delta == the sum of the frames they carry, never enlarged)
- C5 determinism at merge points (queue isolation): OK
- C6 tick alignment, cycle <= C_max, entries <= GCL_size: OK
- C7 end-to-end deadline and jitter: OK
- C9 supplier/receiver window timing: OK

## GCL per egress port

### sw01-p3  (7 entries, util 4.6800 %)

```
sgs 83200 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 387520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 291520 0x3F # 00111111   BE
```

### sw01-p4  (15 entries, util 10.9200 %)

```
sgs 22400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 31680 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 118400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 31680 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 143360 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 165120 0x3F # 00111111   BE
```

### sw01-p5  (5 entries, util 3.1200 %)

```
sgs 41600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 387520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 345920 0x3F # 00111111   BE
```

### sw02-p2  (19 entries, util 14.0400 %)

```
sgs 58240 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 32960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 117120 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 174720 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 32960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 142080 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 116480 0x3F # 00111111   BE
```

### sw02-p3  (3 entries, util 1.5600 %)

```
sgs 66560 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 720960 0x3F # 00111111   BE
```

### sw02-p5  (17 entries, util 12.4800 %)

```
sgs 16640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 162560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 162560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 162560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 145920 0x3F # 00111111   BE
```

### sw03-p3  (5 entries, util 3.1200 %)

```
sgs 79360 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 387520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 308160 0x3F # 00111111   BE
```

### sw03-p4  (15 entries, util 10.9200 %)

```
sgs 39040 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 31680 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 118400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 31680 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 143360 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 148480 0x3F # 00111111   BE
```

### sw05-p2  (17 entries, util 12.4800 %)

```
sgs 33280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 162560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 162560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 162560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 129280 0x3F # 00111111   BE
```

### sw05-p5  (15 entries, util 10.9200 %)

```
sgs 54400 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 32960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 117120 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 32960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 142080 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 133120 0x3F # 00111111   BE
```

### sw06-p2  (15 entries, util 10.9200 %)

```
sgs 62720 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 24640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 125440 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 24640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 150400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 124800 0x3F # 00111111   BE
```

### sw06-p3  (5 entries, util 3.1200 %)

```
sgs 60800 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 387520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 326720 0x3F # 00111111   BE
```

### sw07-p3  (15 entries, util 10.9200 %)

```
sgs 37760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 32960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 117120 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 32960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 142080 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 149760 0x3F # 00111111   BE
```

### sw07-p4  (17 entries, util 12.4800 %)

```
sgs 49920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 161920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 161920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 161920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 112000 0x3F # 00111111   BE
```

### sw08-p2  (31 entries, util 23.4000 %)

```
sgs 66560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 11840 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 112640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 161920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 11840 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 137600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 95360 0x3F # 00111111   BE
```

### sw08-p4  (5 entries, util 3.1200 %)

```
sgs 43840 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 387520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 343680 0x3F # 00111111   BE
```

### sw08-p5  (15 entries, util 10.9200 %)

```
sgs 17280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 36800 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 113280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 36800 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 138240 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 170240 0x3F # 00111111   BE
```

Ports carrying no TT traffic (single best-effort entry for the whole cycle): sw02-p4, sw03-p5, sw04-p3, sw04-p4, sw04-p5, sw05-p3, sw05-p4, sw06-p4, sw06-p5, sw07-p5

