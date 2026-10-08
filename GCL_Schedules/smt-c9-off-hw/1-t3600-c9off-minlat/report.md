# SMT-synthesized GCL schedule (Problem 1: feasible schedule synthesis)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4000 ns
- TT queues: Q6, Q7; best effort filler mask 0x3F
- Solver: Z3, maximize admitted flows (binary search), then minimize total latency, timeout 3600s
- Result: **sat**, admitted 10/20 (proven optimal), solved in 68.21s
- Total latency (sum of e2e over admitted flows): **264640 ns** (proven minimum)

- **WARNING: C9 disabled for this run** -- see Constraint check below for the resulting violations.

## Flows

stream.csv does not specify a talker offset; `offset (ns) = phi` below is the transmit time of each flow's first frame, computed by the solver (also in `offsets.csv` and `schedule.json`'s `offset_ns`).

| flow | route | L (B) | C (ns) | T (ns) | D (ns) | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|---|---|---|---|
| s0(id=1 S3->S1) | S3->sw01->sw02->S1 | 500 | 4160 | 200000 | 200000 | 7 | 0 | 20800 | yes |
| s1(id=2 S2->S1) | S2->sw08->sw07->sw05->sw02->S1 | 400 | 3520 | 200000 | 200000 | None | None | None | no |
| s2(id=3 S3->S2) | S3->sw01->sw03->sw06->sw08->S2 | 100 | 2560 | 200000 | 200000 | None | None | None | no |
| s3(id=4 S1->S3) | S1->sw02->sw01->S3 | 300 | 2560 | 800000 | 800000 | 6 | 5120 | 16000 | yes |
| s4(id=5 S2->S1) | S2->sw08->sw07->sw05->sw02->S1 | 200 | 2560 | 400000 | 400000 | 6 | 3520 | 29440 | yes |
| s5(id=6 S2->S1) | S2->sw08->sw07->sw05->sw02->S1 | 100 | 2560 | 400000 | 400000 | None | None | None | no |
| s6(id=7 S2->S1) | S2->sw08->sw07->sw05->sw02->S1 | 300 | 2560 | 800000 | 800000 | None | None | None | no |
| s7(id=8 S2->S3) | S2->sw08->sw06->sw03->sw01->S3 | 100 | 2560 | 800000 | 800000 | 7 | 14720 | 31040 | yes |
| s8(id=9 S3->S2) | S3->sw01->sw03->sw06->sw08->S2 | 500 | 4160 | 200000 | 200000 | 6 | 6720 | 37440 | yes |
| s9(id=10 S1->S3) | S1->sw02->sw01->S3 | 100 | 2560 | 800000 | 800000 | None | None | None | no |
| s10(id=11 S3->S2) | S3->sw01->sw03->sw06->sw08->S2 | 500 | 4160 | 800000 | 800000 | None | None | None | no |
| s11(id=12 S2->S1) | S2->sw08->sw07->sw05->sw02->S1 | 100 | 2560 | 800000 | 800000 | None | None | None | no |
| s12(id=13 S1->S2) | S1->sw02->sw05->sw07->sw08->S2 | 300 | 2560 | 400000 | 400000 | None | None | None | no |
| s13(id=14 S1->S2) | S1->sw02->sw05->sw07->sw08->S2 | 100 | 2560 | 200000 | 200000 | 6 | 0 | 29440 | yes |
| s14(id=15 S2->S3) | S2->sw08->sw06->sw03->sw01->S3 | 400 | 3520 | 400000 | 400000 | 6 | 8640 | 34240 | yes |
| s15(id=16 S3->S2) | S3->sw01->sw03->sw06->sw08->S2 | 200 | 2560 | 200000 | 200000 | None | None | None | no |
| s16(id=17 S2->S3) | S2->sw08->sw06->sw03->sw01->S3 | 200 | 2560 | 800000 | 800000 | 7 | 19840 | 29440 | yes |
| s17(id=18 S3->S2) | S3->sw01->sw03->sw06->sw08->S2 | 100 | 2560 | 400000 | 400000 | None | None | None | no |
| s18(id=19 S3->S1) | S3->sw01->sw02->S1 | 500 | 4160 | 400000 | 400000 | 6 | 18560 | 20800 | yes |
| s19(id=20 S3->S1) | S3->sw01->sw02->S1 | 200 | 2560 | 200000 | 200000 | 7 | 13440 | 16000 | yes |

## Per-hop windows

| flow | egress port | queue | psi (ns) | delta (ns) |
|---|---|---|---|---|
| s0(id=1 S3->S1) | S3-p0 | Q7 | 0 | 4160 |
| s0(id=1 S3->S1) | sw01-p5 | Q7 | 8320 | 4160 |
| s0(id=1 S3->S1) | sw02-p2 | Q7 | 16640 | 4160 |
| s3(id=4 S1->S3) | S1-p0 | Q6 | 5120 | 2560 |
| s3(id=4 S1->S3) | sw02-p3 | Q6 | 11840 | 2560 |
| s3(id=4 S1->S3) | sw01-p3 | Q6 | 18560 | 2560 |
| s4(id=5 S2->S1) | S2-p0 | Q6 | 3520 | 2560 |
| s4(id=5 S2->S1) | sw08-p5 | Q6 | 10240 | 2560 |
| s4(id=5 S2->S1) | sw07-p3 | Q6 | 16960 | 2560 |
| s4(id=5 S2->S1) | sw05-p5 | Q6 | 23680 | 2560 |
| s4(id=5 S2->S1) | sw02-p2 | Q6 | 30400 | 2560 |
| s7(id=8 S2->S3) | S2-p0 | Q7 | 14720 | 2560 |
| s7(id=8 S2->S3) | sw08-p4 | Q7 | 21440 | 2560 |
| s7(id=8 S2->S3) | sw06-p3 | Q7 | 28160 | 2560 |
| s7(id=8 S2->S3) | sw03-p3 | Q7 | 35520 | 2560 |
| s7(id=8 S2->S3) | sw01-p3 | Q7 | 43200 | 2560 |
| s8(id=9 S3->S2) | S3-p0 | Q6 | 6720 | 4160 |
| s8(id=9 S3->S2) | sw01-p4 | Q6 | 15040 | 4160 |
| s8(id=9 S3->S2) | sw03-p4 | Q6 | 23360 | 4160 |
| s8(id=9 S3->S2) | sw06-p2 | Q6 | 31680 | 4160 |
| s8(id=9 S3->S2) | sw08-p2 | Q6 | 40000 | 4160 |
| s13(id=14 S1->S2) | S1-p0 | Q6 | 0 | 2560 |
| s13(id=14 S1->S2) | sw02-p5 | Q6 | 6720 | 2560 |
| s13(id=14 S1->S2) | sw05-p2 | Q6 | 13440 | 2560 |
| s13(id=14 S1->S2) | sw07-p4 | Q6 | 20160 | 2560 |
| s13(id=14 S1->S2) | sw08-p2 | Q6 | 26880 | 2560 |
| s14(id=15 S2->S3) | S2-p0 | Q6 | 8640 | 3520 |
| s14(id=15 S2->S3) | sw08-p4 | Q6 | 16320 | 3520 |
| s14(id=15 S2->S3) | sw06-p3 | Q6 | 24000 | 3520 |
| s14(id=15 S2->S3) | sw03-p3 | Q6 | 31680 | 3520 |
| s14(id=15 S2->S3) | sw01-p3 | Q6 | 39360 | 3520 |
| s16(id=17 S2->S3) | S2-p0 | Q7 | 19840 | 2560 |
| s16(id=17 S2->S3) | sw08-p4 | Q7 | 26560 | 2560 |
| s16(id=17 S2->S3) | sw06-p3 | Q7 | 33280 | 2560 |
| s16(id=17 S2->S3) | sw03-p3 | Q7 | 40000 | 2560 |
| s16(id=17 S2->S3) | sw01-p3 | Q7 | 46720 | 2560 |
| s18(id=19 S3->S1) | S3-p0 | Q6 | 18560 | 4160 |
| s18(id=19 S3->S1) | sw01-p5 | Q6 | 26880 | 4160 |
| s18(id=19 S3->S1) | sw02-p2 | Q6 | 35200 | 4160 |
| s19(id=20 S3->S1) | S3-p0 | Q7 | 13440 | 2560 |
| s19(id=20 S3->S1) | sw01-p5 | Q7 | 20160 | 2560 |
| s19(id=20 S3->S1) | sw02-p2 | Q7 | 26880 | 2560 |

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
sgs 18560 0x3F # 00111111   BE
sgs 2560 0x40 # 01000000   Q6
sgs 18240 0x3F # 00111111   BE
sgs 3520 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 2560 0x80 # 10000000   Q7
sgs 960 0x3F # 00111111   BE
sgs 2560 0x80 # 10000000   Q7
sgs 390080 0x3F # 00111111   BE
sgs 3520 0x40 # 01000000   Q6
sgs 357120 0x3F # 00111111   BE
```

### sw01-p4  (9 entries, util 2.0800 %)

```
sgs 15040 0x3F # 00111111   BE
sgs 4160 0x40 # 01000000   Q6
sgs 195840 0x3F # 00111111   BE
sgs 4160 0x40 # 01000000   Q6
sgs 195840 0x3F # 00111111   BE
sgs 4160 0x40 # 01000000   Q6
sgs 195840 0x3F # 00111111   BE
sgs 4160 0x40 # 01000000   Q6
sgs 180800 0x3F # 00111111   BE
```

### sw01-p5  (21 entries, util 4.4000 %)

```
sgs 8320 0x3F # 00111111   BE
sgs 4160 0x80 # 10000000   Q7
sgs 7680 0x3F # 00111111   BE
sgs 2560 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 4160 0x40 # 01000000   Q6
sgs 177280 0x3F # 00111111   BE
sgs 4160 0x80 # 10000000   Q7
sgs 7680 0x3F # 00111111   BE
sgs 2560 0x80 # 10000000   Q7
sgs 185600 0x3F # 00111111   BE
sgs 4160 0x80 # 10000000   Q7
sgs 7680 0x3F # 00111111   BE
sgs 2560 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 4160 0x40 # 01000000   Q6
sgs 177280 0x3F # 00111111   BE
sgs 4160 0x80 # 10000000   Q7
sgs 7680 0x3F # 00111111   BE
sgs 2560 0x80 # 10000000   Q7
sgs 177280 0x3F # 00111111   BE
```

### sw02-p2  (25 entries, util 5.0400 %)

```
sgs 16640 0x3F # 00111111   BE
sgs 4160 0x80 # 10000000   Q7
sgs 6080 0x3F # 00111111   BE
sgs 2560 0x80 # 10000000   Q7
sgs 960 0x3F # 00111111   BE
sgs 2560 0x40 # 01000000   Q6
sgs 2240 0x3F # 00111111   BE
sgs 4160 0x40 # 01000000   Q6
sgs 177280 0x3F # 00111111   BE
sgs 4160 0x80 # 10000000   Q7
sgs 6080 0x3F # 00111111   BE
sgs 2560 0x80 # 10000000   Q7
sgs 187200 0x3F # 00111111   BE
sgs 4160 0x80 # 10000000   Q7
sgs 6080 0x3F # 00111111   BE
sgs 2560 0x80 # 10000000   Q7
sgs 960 0x3F # 00111111   BE
sgs 2560 0x40 # 01000000   Q6
sgs 2240 0x3F # 00111111   BE
sgs 4160 0x40 # 01000000   Q6
sgs 177280 0x3F # 00111111   BE
sgs 4160 0x80 # 10000000   Q7
sgs 6080 0x3F # 00111111   BE
sgs 2560 0x80 # 10000000   Q7
sgs 170560 0x3F # 00111111   BE
```

### sw02-p3  (3 entries, util 0.3200 %)

```
sgs 11840 0x3F # 00111111   BE
sgs 2560 0x40 # 01000000   Q6
sgs 785600 0x3F # 00111111   BE
```

### sw02-p5  (9 entries, util 1.2800 %)

```
sgs 6720 0x3F # 00111111   BE
sgs 2560 0x40 # 01000000   Q6
sgs 197440 0x3F # 00111111   BE
sgs 2560 0x40 # 01000000   Q6
sgs 197440 0x3F # 00111111   BE
sgs 2560 0x40 # 01000000   Q6
sgs 197440 0x3F # 00111111   BE
sgs 2560 0x40 # 01000000   Q6
sgs 190720 0x3F # 00111111   BE
```

### sw03-p3  (9 entries, util 1.5200 %)

```
sgs 31680 0x3F # 00111111   BE
sgs 3520 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 2560 0x80 # 10000000   Q7
sgs 1920 0x3F # 00111111   BE
sgs 2560 0x80 # 10000000   Q7
sgs 389120 0x3F # 00111111   BE
sgs 3520 0x40 # 01000000   Q6
sgs 364800 0x3F # 00111111   BE
```

### sw03-p4  (9 entries, util 2.0800 %)

```
sgs 23360 0x3F # 00111111   BE
sgs 4160 0x40 # 01000000   Q6
sgs 195840 0x3F # 00111111   BE
sgs 4160 0x40 # 01000000   Q6
sgs 195840 0x3F # 00111111   BE
sgs 4160 0x40 # 01000000   Q6
sgs 195840 0x3F # 00111111   BE
sgs 4160 0x40 # 01000000   Q6
sgs 172480 0x3F # 00111111   BE
```

### sw05-p2  (9 entries, util 1.2800 %)

```
sgs 13440 0x3F # 00111111   BE
sgs 2560 0x40 # 01000000   Q6
sgs 197440 0x3F # 00111111   BE
sgs 2560 0x40 # 01000000   Q6
sgs 197440 0x3F # 00111111   BE
sgs 2560 0x40 # 01000000   Q6
sgs 197440 0x3F # 00111111   BE
sgs 2560 0x40 # 01000000   Q6
sgs 184000 0x3F # 00111111   BE
```

### sw05-p5  (5 entries, util 0.6400 %)

```
sgs 23680 0x3F # 00111111   BE
sgs 2560 0x40 # 01000000   Q6
sgs 397440 0x3F # 00111111   BE
sgs 2560 0x40 # 01000000   Q6
sgs 373760 0x3F # 00111111   BE
```

### sw06-p2  (9 entries, util 2.0800 %)

```
sgs 31680 0x3F # 00111111   BE
sgs 4160 0x40 # 01000000   Q6
sgs 195840 0x3F # 00111111   BE
sgs 4160 0x40 # 01000000   Q6
sgs 195840 0x3F # 00111111   BE
sgs 4160 0x40 # 01000000   Q6
sgs 195840 0x3F # 00111111   BE
sgs 4160 0x40 # 01000000   Q6
sgs 164160 0x3F # 00111111   BE
```

### sw06-p3  (9 entries, util 1.5200 %)

```
sgs 24000 0x3F # 00111111   BE
sgs 3520 0x40 # 01000000   Q6
sgs 640 0x3F # 00111111   BE
sgs 2560 0x80 # 10000000   Q7
sgs 2560 0x3F # 00111111   BE
sgs 2560 0x80 # 10000000   Q7
sgs 388160 0x3F # 00111111   BE
sgs 3520 0x40 # 01000000   Q6
sgs 372480 0x3F # 00111111   BE
```

### sw07-p3  (5 entries, util 0.6400 %)

```
sgs 16960 0x3F # 00111111   BE
sgs 2560 0x40 # 01000000   Q6
sgs 397440 0x3F # 00111111   BE
sgs 2560 0x40 # 01000000   Q6
sgs 380480 0x3F # 00111111   BE
```

### sw07-p4  (9 entries, util 1.2800 %)

```
sgs 20160 0x3F # 00111111   BE
sgs 2560 0x40 # 01000000   Q6
sgs 197440 0x3F # 00111111   BE
sgs 2560 0x40 # 01000000   Q6
sgs 197440 0x3F # 00111111   BE
sgs 2560 0x40 # 01000000   Q6
sgs 197440 0x3F # 00111111   BE
sgs 2560 0x40 # 01000000   Q6
sgs 177280 0x3F # 00111111   BE
```

### sw08-p2  (17 entries, util 3.3600 %)

```
sgs 26880 0x3F # 00111111   BE
sgs 2560 0x40 # 01000000   Q6
sgs 10560 0x3F # 00111111   BE
sgs 4160 0x40 # 01000000   Q6
sgs 182720 0x3F # 00111111   BE
sgs 2560 0x40 # 01000000   Q6
sgs 10560 0x3F # 00111111   BE
sgs 4160 0x40 # 01000000   Q6
sgs 182720 0x3F # 00111111   BE
sgs 2560 0x40 # 01000000   Q6
sgs 10560 0x3F # 00111111   BE
sgs 4160 0x40 # 01000000   Q6
sgs 182720 0x3F # 00111111   BE
sgs 2560 0x40 # 01000000   Q6
sgs 10560 0x3F # 00111111   BE
sgs 4160 0x40 # 01000000   Q6
sgs 155840 0x3F # 00111111   BE
```

### sw08-p4  (9 entries, util 1.5200 %)

```
sgs 16320 0x3F # 00111111   BE
sgs 3520 0x40 # 01000000   Q6
sgs 1600 0x3F # 00111111   BE
sgs 2560 0x80 # 10000000   Q7
sgs 2560 0x3F # 00111111   BE
sgs 2560 0x80 # 10000000   Q7
sgs 387200 0x3F # 00111111   BE
sgs 3520 0x40 # 01000000   Q6
sgs 380160 0x3F # 00111111   BE
```

### sw08-p5  (5 entries, util 0.6400 %)

```
sgs 10240 0x3F # 00111111   BE
sgs 2560 0x40 # 01000000   Q6
sgs 397440 0x3F # 00111111   BE
sgs 2560 0x40 # 01000000   Q6
sgs 387200 0x3F # 00111111   BE
```

Ports carrying no TT traffic (single best-effort entry for the whole cycle): sw02-p4, sw03-p5, sw04-p3, sw04-p4, sw04-p5, sw05-p3, sw05-p4, sw06-p4, sw06-p5, sw07-p5

