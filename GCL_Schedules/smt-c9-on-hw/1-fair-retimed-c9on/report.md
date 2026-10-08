# SMT-synthesized GCL schedule (Problem 1: feasible schedule synthesis)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4000 ns
- TT queues: Q6, Q7; best effort filler mask 0x3F
- **Retimed from `result/result-dataset-testbed-hw/smt-c9-off/1-t3600-c9off-minlat/schedule.json`**: flow set, routes, and release_offset pinned to exactly what that run admitted; only phi (window timing) is being re-solved here, under this run's own constraint set.
- Solver: Z3, maximize admitted flows (binary search), then minimize total latency, timeout 3600s
- Result: **sat**, admitted 10/10 (proven optimal), solved in 4.43s
- Total latency (sum of e2e over admitted flows): **165760 ns** (proven minimum)

## Flows

stream.csv does not specify a talker offset; `offset (ns) = phi` below is the transmit time of each flow's first frame, computed by the solver (also in `offsets.csv` and `schedule.json`'s `offset_ns`).

| flow | route | L (B) | C (ns) | T (ns) | D (ns) | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|---|---|---|---|
| s0(id=1 S3->S1) | S3->sw01->sw02->S1 | 500 | 4160 | 200000 | 200000 | 6 | 0 | 12480 | yes |
| s3(id=4 S1->S3) | S1->sw02->sw01->S3 | 300 | 2560 | 800000 | 800000 | 7 | 5120 | 10880 | yes |
| s4(id=5 S2->S1) | S2->sw08->sw07->sw05->sw02->S1 | 200 | 2560 | 400000 | 400000 | 6 | 3520 | 19200 | yes |
| s7(id=8 S2->S3) | S2->sw08->sw06->sw03->sw01->S3 | 100 | 2560 | 800000 | 800000 | 6 | 14720 | 19200 | yes |
| s8(id=9 S3->S2) | S3->sw01->sw03->sw06->sw08->S2 | 500 | 4160 | 200000 | 200000 | 7 | 6720 | 20800 | yes |
| s13(id=14 S1->S2) | S1->sw02->sw05->sw07->sw08->S2 | 100 | 2560 | 200000 | 200000 | 6 | 0 | 19200 | yes |
| s14(id=15 S2->S3) | S2->sw08->sw06->sw03->sw01->S3 | 400 | 3520 | 400000 | 400000 | 7 | 8640 | 20160 | yes |
| s16(id=17 S2->S3) | S2->sw08->sw06->sw03->sw01->S3 | 200 | 2560 | 800000 | 800000 | 6 | 19840 | 19200 | yes |
| s18(id=19 S3->S1) | S3->sw01->sw02->S1 | 500 | 4160 | 400000 | 400000 | 6 | 18560 | 12480 | yes |
| s19(id=20 S3->S1) | S3->sw01->sw02->S1 | 200 | 2560 | 200000 | 200000 | 7 | 13440 | 12160 | yes |

## Per-hop windows

| flow | egress port | queue | psi (ns) | delta (ns) |
|---|---|---|---|---|
| s0(id=1 S3->S1) | S3-p0 | Q6 | 0 | 4160 |
| s0(id=1 S3->S1) | sw01-p5 | Q6 | 4160 | 4160 |
| s0(id=1 S3->S1) | sw02-p2 | Q6 | 8320 | 4160 |
| s3(id=4 S1->S3) | S1-p0 | Q7 | 5120 | 2560 |
| s3(id=4 S1->S3) | sw02-p3 | Q7 | 9280 | 2560 |
| s3(id=4 S1->S3) | sw01-p3 | Q7 | 13440 | 2560 |
| s4(id=5 S2->S1) | S2-p0 | Q6 | 3520 | 2560 |
| s4(id=5 S2->S1) | sw08-p5 | Q6 | 7680 | 2560 |
| s4(id=5 S2->S1) | sw07-p3 | Q6 | 11840 | 2560 |
| s4(id=5 S2->S1) | sw05-p5 | Q6 | 16000 | 2560 |
| s4(id=5 S2->S1) | sw02-p2 | Q6 | 20160 | 2560 |
| s7(id=8 S2->S3) | S2-p0 | Q6 | 14720 | 2560 |
| s7(id=8 S2->S3) | sw08-p4 | Q6 | 18880 | 2560 |
| s7(id=8 S2->S3) | sw06-p3 | Q6 | 23040 | 2560 |
| s7(id=8 S2->S3) | sw03-p3 | Q6 | 27200 | 2560 |
| s7(id=8 S2->S3) | sw01-p3 | Q6 | 31360 | 2560 |
| s8(id=9 S3->S2) | S3-p0 | Q7 | 6720 | 4160 |
| s8(id=9 S3->S2) | sw01-p4 | Q7 | 10880 | 4160 |
| s8(id=9 S3->S2) | sw03-p4 | Q7 | 15040 | 4160 |
| s8(id=9 S3->S2) | sw06-p2 | Q7 | 19200 | 4160 |
| s8(id=9 S3->S2) | sw08-p2 | Q7 | 23360 | 4160 |
| s13(id=14 S1->S2) | S1-p0 | Q6 | 0 | 2560 |
| s13(id=14 S1->S2) | sw02-p5 | Q6 | 4160 | 2560 |
| s13(id=14 S1->S2) | sw05-p2 | Q6 | 8320 | 2560 |
| s13(id=14 S1->S2) | sw07-p4 | Q6 | 12480 | 2560 |
| s13(id=14 S1->S2) | sw08-p2 | Q6 | 16640 | 2560 |
| s14(id=15 S2->S3) | S2-p0 | Q7 | 8640 | 3520 |
| s14(id=15 S2->S3) | sw08-p4 | Q7 | 12800 | 3520 |
| s14(id=15 S2->S3) | sw06-p3 | Q7 | 16960 | 3520 |
| s14(id=15 S2->S3) | sw03-p3 | Q7 | 21120 | 3520 |
| s14(id=15 S2->S3) | sw01-p3 | Q7 | 25280 | 3520 |
| s16(id=17 S2->S3) | S2-p0 | Q6 | 19840 | 2560 |
| s16(id=17 S2->S3) | sw08-p4 | Q6 | 24000 | 2560 |
| s16(id=17 S2->S3) | sw06-p3 | Q6 | 28160 | 2560 |
| s16(id=17 S2->S3) | sw03-p3 | Q6 | 32320 | 2560 |
| s16(id=17 S2->S3) | sw01-p3 | Q6 | 36480 | 2560 |
| s18(id=19 S3->S1) | S3-p0 | Q6 | 18560 | 4160 |
| s18(id=19 S3->S1) | sw01-p5 | Q6 | 22720 | 4160 |
| s18(id=19 S3->S1) | sw02-p2 | Q6 | 26880 | 4160 |
| s19(id=20 S3->S1) | S3-p0 | Q7 | 13440 | 2560 |
| s19(id=20 S3->S1) | sw01-p5 | Q7 | 18880 | 2560 |
| s19(id=20 S3->S1) | sw02-p2 | Q7 | 23040 | 2560 |

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

### sw01-p3  (11 entries, util 1.8400 %)

```
sgs 13440 0x3F # 00111111   BE
sgs 2560 0x80 # 10000000   Q7
sgs 9280 0x3F # 00111111   BE
sgs 3520 0x80 # 10000000   Q7
sgs 2560 0x3F # 00111111   BE
sgs 2560 0x40 # 01000000   Q6
sgs 2560 0x3F # 00111111   BE
sgs 2560 0x40 # 01000000   Q6
sgs 386240 0x3F # 00111111   BE
sgs 3520 0x80 # 10000000   Q7
sgs 371200 0x3F # 00111111   BE
```

### sw01-p4  (9 entries, util 2.0800 %)

```
sgs 10880 0x3F # 00111111   BE
sgs 4160 0x80 # 10000000   Q7
sgs 195840 0x3F # 00111111   BE
sgs 4160 0x80 # 10000000   Q7
sgs 195840 0x3F # 00111111   BE
sgs 4160 0x80 # 10000000   Q7
sgs 195840 0x3F # 00111111   BE
sgs 4160 0x80 # 10000000   Q7
sgs 184960 0x3F # 00111111   BE
```

### sw01-p5  (21 entries, util 4.4000 %)

```
sgs 4160 0x3F # 00111111   BE
sgs 4160 0x40 # 01000000   Q6
sgs 10560 0x3F # 00111111   BE
sgs 2560 0x80 # 10000000   Q7
sgs 1280 0x3F # 00111111   BE
sgs 4160 0x40 # 01000000   Q6
sgs 177280 0x3F # 00111111   BE
sgs 4160 0x40 # 01000000   Q6
sgs 10560 0x3F # 00111111   BE
sgs 2560 0x80 # 10000000   Q7
sgs 182720 0x3F # 00111111   BE
sgs 4160 0x40 # 01000000   Q6
sgs 10560 0x3F # 00111111   BE
sgs 2560 0x80 # 10000000   Q7
sgs 1280 0x3F # 00111111   BE
sgs 4160 0x40 # 01000000   Q6
sgs 177280 0x3F # 00111111   BE
sgs 4160 0x40 # 01000000   Q6
sgs 10560 0x3F # 00111111   BE
sgs 2560 0x80 # 10000000   Q7
sgs 178560 0x3F # 00111111   BE
```

### sw02-p2  (25 entries, util 5.0400 %)

```
sgs 8320 0x3F # 00111111   BE
sgs 4160 0x40 # 01000000   Q6
sgs 7680 0x3F # 00111111   BE
sgs 2560 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 2560 0x80 # 10000000   Q7
sgs 1280 0x3F # 00111111   BE
sgs 4160 0x40 # 01000000   Q6
sgs 177280 0x3F # 00111111   BE
sgs 4160 0x40 # 01000000   Q6
sgs 10560 0x3F # 00111111   BE
sgs 2560 0x80 # 10000000   Q7
sgs 182720 0x3F # 00111111   BE
sgs 4160 0x40 # 01000000   Q6
sgs 7680 0x3F # 00111111   BE
sgs 2560 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 2560 0x80 # 10000000   Q7
sgs 1280 0x3F # 00111111   BE
sgs 4160 0x40 # 01000000   Q6
sgs 177280 0x3F # 00111111   BE
sgs 4160 0x40 # 01000000   Q6
sgs 10560 0x3F # 00111111   BE
sgs 2560 0x80 # 10000000   Q7
sgs 174400 0x3F # 00111111   BE
```

### sw02-p3  (3 entries, util 0.3200 %)

```
sgs 9280 0x3F # 00111111   BE
sgs 2560 0x80 # 10000000   Q7
sgs 788160 0x3F # 00111111   BE
```

### sw02-p5  (9 entries, util 1.2800 %)

```
sgs 4160 0x3F # 00111111   BE
sgs 2560 0x40 # 01000000   Q6
sgs 197440 0x3F # 00111111   BE
sgs 2560 0x40 # 01000000   Q6
sgs 197440 0x3F # 00111111   BE
sgs 2560 0x40 # 01000000   Q6
sgs 197440 0x3F # 00111111   BE
sgs 2560 0x40 # 01000000   Q6
sgs 193280 0x3F # 00111111   BE
```

### sw03-p3  (9 entries, util 1.5200 %)

```
sgs 21120 0x3F # 00111111   BE
sgs 3520 0x80 # 10000000   Q7
sgs 2560 0x3F # 00111111   BE
sgs 2560 0x40 # 01000000   Q6
sgs 2560 0x3F # 00111111   BE
sgs 2560 0x40 # 01000000   Q6
sgs 386240 0x3F # 00111111   BE
sgs 3520 0x80 # 10000000   Q7
sgs 375360 0x3F # 00111111   BE
```

### sw03-p4  (9 entries, util 2.0800 %)

```
sgs 15040 0x3F # 00111111   BE
sgs 4160 0x80 # 10000000   Q7
sgs 195840 0x3F # 00111111   BE
sgs 4160 0x80 # 10000000   Q7
sgs 195840 0x3F # 00111111   BE
sgs 4160 0x80 # 10000000   Q7
sgs 195840 0x3F # 00111111   BE
sgs 4160 0x80 # 10000000   Q7
sgs 180800 0x3F # 00111111   BE
```

### sw05-p2  (9 entries, util 1.2800 %)

```
sgs 8320 0x3F # 00111111   BE
sgs 2560 0x40 # 01000000   Q6
sgs 197440 0x3F # 00111111   BE
sgs 2560 0x40 # 01000000   Q6
sgs 197440 0x3F # 00111111   BE
sgs 2560 0x40 # 01000000   Q6
sgs 197440 0x3F # 00111111   BE
sgs 2560 0x40 # 01000000   Q6
sgs 189120 0x3F # 00111111   BE
```

### sw05-p5  (5 entries, util 0.6400 %)

```
sgs 16000 0x3F # 00111111   BE
sgs 2560 0x40 # 01000000   Q6
sgs 397440 0x3F # 00111111   BE
sgs 2560 0x40 # 01000000   Q6
sgs 381440 0x3F # 00111111   BE
```

### sw06-p2  (9 entries, util 2.0800 %)

```
sgs 19200 0x3F # 00111111   BE
sgs 4160 0x80 # 10000000   Q7
sgs 195840 0x3F # 00111111   BE
sgs 4160 0x80 # 10000000   Q7
sgs 195840 0x3F # 00111111   BE
sgs 4160 0x80 # 10000000   Q7
sgs 195840 0x3F # 00111111   BE
sgs 4160 0x80 # 10000000   Q7
sgs 176640 0x3F # 00111111   BE
```

### sw06-p3  (9 entries, util 1.5200 %)

```
sgs 16960 0x3F # 00111111   BE
sgs 3520 0x80 # 10000000   Q7
sgs 2560 0x3F # 00111111   BE
sgs 2560 0x40 # 01000000   Q6
sgs 2560 0x3F # 00111111   BE
sgs 2560 0x40 # 01000000   Q6
sgs 386240 0x3F # 00111111   BE
sgs 3520 0x80 # 10000000   Q7
sgs 379520 0x3F # 00111111   BE
```

### sw07-p3  (5 entries, util 0.6400 %)

```
sgs 11840 0x3F # 00111111   BE
sgs 2560 0x40 # 01000000   Q6
sgs 397440 0x3F # 00111111   BE
sgs 2560 0x40 # 01000000   Q6
sgs 385600 0x3F # 00111111   BE
```

### sw07-p4  (9 entries, util 1.2800 %)

```
sgs 12480 0x3F # 00111111   BE
sgs 2560 0x40 # 01000000   Q6
sgs 197440 0x3F # 00111111   BE
sgs 2560 0x40 # 01000000   Q6
sgs 197440 0x3F # 00111111   BE
sgs 2560 0x40 # 01000000   Q6
sgs 197440 0x3F # 00111111   BE
sgs 2560 0x40 # 01000000   Q6
sgs 184960 0x3F # 00111111   BE
```

### sw08-p2  (17 entries, util 3.3600 %)

```
sgs 16640 0x3F # 00111111   BE
sgs 2560 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 4160 0x80 # 10000000   Q7
sgs 189120 0x3F # 00111111   BE
sgs 2560 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 4160 0x80 # 10000000   Q7
sgs 189120 0x3F # 00111111   BE
sgs 2560 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 4160 0x80 # 10000000   Q7
sgs 189120 0x3F # 00111111   BE
sgs 2560 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 4160 0x80 # 10000000   Q7
sgs 172480 0x3F # 00111111   BE
```

### sw08-p4  (9 entries, util 1.5200 %)

```
sgs 12800 0x3F # 00111111   BE
sgs 3520 0x80 # 10000000   Q7
sgs 2560 0x3F # 00111111   BE
sgs 2560 0x40 # 01000000   Q6
sgs 2560 0x3F # 00111111   BE
sgs 2560 0x40 # 01000000   Q6
sgs 386240 0x3F # 00111111   BE
sgs 3520 0x80 # 10000000   Q7
sgs 383680 0x3F # 00111111   BE
```

### sw08-p5  (5 entries, util 0.6400 %)

```
sgs 7680 0x3F # 00111111   BE
sgs 2560 0x40 # 01000000   Q6
sgs 397440 0x3F # 00111111   BE
sgs 2560 0x40 # 01000000   Q6
sgs 389760 0x3F # 00111111   BE
```

Ports carrying no TT traffic (single best-effort entry for the whole cycle): sw02-p4, sw03-p5, sw04-p3, sw04-p4, sw04-p5, sw05-p3, sw05-p4, sw06-p4, sw06-p5, sw07-p5

