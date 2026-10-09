# SMT-synthesized GCL schedule (Problem 1: feasible schedule synthesis)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4000 ns
- TT queues: Q6, Q7; best effort filler mask 0x3F
- **Retimed from `result/result-2026-10-08-dataset-testbed-2/smt-c9-off/2-t3600-c9off-minlat/schedule.json`**: flow set, routes, and release_offset pinned to exactly what that run admitted; only phi (window timing) is being re-solved here, under this run's own constraint set.
- Solver: Z3, maximize admitted flows (binary search), then minimize total latency, timeout 3600s
- Result: **sat**, admitted 11/11 (proven optimal), solved in 8.12s
- Total latency (sum of e2e over admitted flows): **317120 ns** (proven minimum)

## Flows

stream.csv does not specify a talker offset; `offset (ns) = phi` below is the transmit time of each flow's first frame, computed by the solver (also in `offsets.csv` and `schedule.json`'s `offset_ns`).

| flow | route | L (B) | C (ns) | T (ns) | D (ns) | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|---|---|---|---|
| s0(id=1 S1->S2) | S1->sw02->sw05->sw07->sw08->S2 | 500 | 12480 | 200000 | 200000 | 7 | 0 | 41920 | yes |
| s3(id=4 S1->S3) | S1->sw02->sw01->S3 | 400 | 12480 | 800000 | 800000 | 6 | 49920 | 20800 | yes |
| s6(id=7 S3->S1) | S3->sw01->sw02->S1 | 300 | 12480 | 400000 | 400000 | 7 | 24960 | 20800 | yes |
| s8(id=9 S1->S2) | S1->sw02->sw05->sw07->sw08->S2 | 400 | 12480 | 200000 | 200000 | 6 | 24960 | 29760 | yes |
| s9(id=10 S3->S2) | S3->sw01->sw03->sw06->sw08->S2 | 300 | 12480 | 800000 | 800000 | 6 | 74880 | 29120 | yes |
| s10(id=11 S2->S3) | S2->sw08->sw06->sw03->sw01->S3 | 300 | 12480 | 400000 | 400000 | 7 | 24960 | 29120 | yes |
| s11(id=12 S2->S1) | S2->sw08->sw07->sw05->sw02->S1 | 200 | 12480 | 800000 | 800000 | 7 | 74880 | 29120 | yes |
| s13(id=14 S3->S2) | S3->sw01->sw03->sw06->sw08->S2 | 500 | 12480 | 200000 | 200000 | 6 | 0 | 29120 | yes |
| s15(id=16 S2->S1) | S2->sw08->sw07->sw05->sw02->S1 | 100 | 12480 | 400000 | 400000 | 6 | 49920 | 29120 | yes |
| s17(id=18 S2->S1) | S2->sw08->sw07->sw05->sw02->S1 | 400 | 12480 | 200000 | 200000 | 6 | 0 | 29120 | yes |
| s19(id=20 S3->S2) | S3->sw01->sw03->sw06->sw08->S2 | 300 | 12480 | 400000 | 400000 | 6 | 49920 | 29120 | yes |

## Per-hop windows

| flow | egress port | queue | psi (ns) | delta (ns) |
|---|---|---|---|---|
| s0(id=1 S1->S2) | S1-p0 | Q7 | 0 | 12480 |
| s0(id=1 S1->S2) | sw02-p5 | Q7 | 4160 | 12480 |
| s0(id=1 S1->S2) | sw05-p2 | Q7 | 8320 | 12480 |
| s0(id=1 S1->S2) | sw07-p4 | Q7 | 12800 | 12480 |
| s0(id=1 S1->S2) | sw08-p2 | Q7 | 29440 | 12480 |
| s3(id=4 S1->S3) | S1-p0 | Q6 | 49920 | 12480 |
| s3(id=4 S1->S3) | sw02-p3 | Q6 | 54080 | 12480 |
| s3(id=4 S1->S3) | sw01-p3 | Q6 | 58240 | 12480 |
| s6(id=7 S3->S1) | S3-p0 | Q7 | 24960 | 12480 |
| s6(id=7 S3->S1) | sw01-p5 | Q7 | 29120 | 12480 |
| s6(id=7 S3->S1) | sw02-p2 | Q7 | 33280 | 12480 |
| s8(id=9 S1->S2) | S1-p0 | Q6 | 24960 | 12480 |
| s8(id=9 S1->S2) | sw02-p5 | Q6 | 29120 | 12480 |
| s8(id=9 S1->S2) | sw05-p2 | Q6 | 33280 | 12480 |
| s8(id=9 S1->S2) | sw07-p4 | Q6 | 37440 | 12480 |
| s8(id=9 S1->S2) | sw08-p2 | Q6 | 42240 | 12480 |
| s9(id=10 S3->S2) | S3-p0 | Q6 | 74880 | 12480 |
| s9(id=10 S3->S2) | sw01-p4 | Q6 | 79040 | 12480 |
| s9(id=10 S3->S2) | sw03-p4 | Q6 | 83200 | 12480 |
| s9(id=10 S3->S2) | sw06-p2 | Q6 | 87360 | 12480 |
| s9(id=10 S3->S2) | sw08-p2 | Q6 | 91520 | 12480 |
| s10(id=11 S2->S3) | S2-p0 | Q7 | 24960 | 12480 |
| s10(id=11 S2->S3) | sw08-p4 | Q7 | 29120 | 12480 |
| s10(id=11 S2->S3) | sw06-p3 | Q7 | 33280 | 12480 |
| s10(id=11 S2->S3) | sw03-p3 | Q7 | 37440 | 12480 |
| s10(id=11 S2->S3) | sw01-p3 | Q7 | 41600 | 12480 |
| s11(id=12 S2->S1) | S2-p0 | Q7 | 74880 | 12480 |
| s11(id=12 S2->S1) | sw08-p5 | Q7 | 79040 | 12480 |
| s11(id=12 S2->S1) | sw07-p3 | Q7 | 83200 | 12480 |
| s11(id=12 S2->S1) | sw05-p5 | Q7 | 87360 | 12480 |
| s11(id=12 S2->S1) | sw02-p2 | Q7 | 91520 | 12480 |
| s13(id=14 S3->S2) | S3-p0 | Q6 | 0 | 12480 |
| s13(id=14 S3->S2) | sw01-p4 | Q6 | 4160 | 12480 |
| s13(id=14 S3->S2) | sw03-p4 | Q6 | 8320 | 12480 |
| s13(id=14 S3->S2) | sw06-p2 | Q6 | 12480 | 12480 |
| s13(id=14 S3->S2) | sw08-p2 | Q6 | 16640 | 12480 |
| s15(id=16 S2->S1) | S2-p0 | Q6 | 49920 | 12480 |
| s15(id=16 S2->S1) | sw08-p5 | Q6 | 54080 | 12480 |
| s15(id=16 S2->S1) | sw07-p3 | Q6 | 58240 | 12480 |
| s15(id=16 S2->S1) | sw05-p5 | Q6 | 62400 | 12480 |
| s15(id=16 S2->S1) | sw02-p2 | Q6 | 66560 | 12480 |
| s17(id=18 S2->S1) | S2-p0 | Q6 | 0 | 12480 |
| s17(id=18 S2->S1) | sw08-p5 | Q6 | 4160 | 12480 |
| s17(id=18 S2->S1) | sw07-p3 | Q6 | 8320 | 12480 |
| s17(id=18 S2->S1) | sw05-p5 | Q6 | 12480 | 12480 |
| s17(id=18 S2->S1) | sw02-p2 | Q6 | 16640 | 12480 |
| s19(id=20 S3->S2) | S3-p0 | Q6 | 49920 | 12480 |
| s19(id=20 S3->S2) | sw01-p4 | Q6 | 54080 | 12480 |
| s19(id=20 S3->S2) | sw03-p4 | Q6 | 58240 | 12480 |
| s19(id=20 S3->S2) | sw06-p2 | Q6 | 62400 | 12480 |
| s19(id=20 S3->S2) | sw08-p2 | Q6 | 66560 | 12480 |

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
sgs 41600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 370880 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 345920 0x3F # 00111111   BE
```

### sw01-p4  (15 entries, util 10.9200 %)

```
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 112640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 137600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 183360 0x3F # 00111111   BE
```

### sw01-p5  (5 entries, util 3.1200 %)

```
sgs 29120 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 387520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 358400 0x3F # 00111111   BE
```

### sw02-p2  (19 entries, util 14.0400 %)

```
sgs 16640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 20800 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 112640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 20800 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 137600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 170880 0x3F # 00111111   BE
```

### sw02-p3  (3 entries, util 1.5600 %)

```
sgs 54080 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 733440 0x3F # 00111111   BE
```

### sw02-p5  (17 entries, util 12.4800 %)

```
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 162560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 162560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 162560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 158400 0x3F # 00111111   BE
```

### sw03-p3  (5 entries, util 3.1200 %)

```
sgs 37440 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 387520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 350080 0x3F # 00111111   BE
```

### sw03-p4  (15 entries, util 10.9200 %)

```
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 112640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 137600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 179200 0x3F # 00111111   BE
```

### sw05-p2  (17 entries, util 12.4800 %)

```
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 162560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 162560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 162560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 154240 0x3F # 00111111   BE
```

### sw05-p5  (15 entries, util 10.9200 %)

```
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 112640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 137600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 175040 0x3F # 00111111   BE
```

### sw06-p2  (15 entries, util 10.9200 %)

```
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 112640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 137600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 175040 0x3F # 00111111   BE
```

### sw06-p3  (5 entries, util 3.1200 %)

```
sgs 33280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 387520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 354240 0x3F # 00111111   BE
```

### sw07-p3  (15 entries, util 10.9200 %)

```
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 112640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 137600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 179200 0x3F # 00111111   BE
```

### sw07-p4  (17 entries, util 12.4800 %)

```
sgs 12800 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 162880 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 162880 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 162880 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 150080 0x3F # 00111111   BE
```

### sw08-p2  (31 entries, util 23.4000 %)

```
sgs 16640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 11840 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 112640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 161920 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 11840 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 137600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 145280 0x3F # 00111111   BE
```

### sw08-p4  (5 entries, util 3.1200 %)

```
sgs 29120 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 387520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 358400 0x3F # 00111111   BE
```

### sw08-p5  (15 entries, util 10.9200 %)

```
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 112640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 37440 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 137600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 183360 0x3F # 00111111   BE
```

Ports carrying no TT traffic (single best-effort entry for the whole cycle): sw02-p4, sw03-p5, sw04-p3, sw04-p4, sw04-p5, sw05-p3, sw05-p4, sw06-p4, sw06-p5, sw07-p5

