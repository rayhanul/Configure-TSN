# SMT-synthesized GCL schedule (Problem 1: feasible schedule synthesis)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- TT queues: Q6, Q7; best effort filler mask 0x3F
- **Retimed from `result/result-2026-10-12-dataset-testbed-7-ring-avgwin/smt-c9-off/7-t3600-c9off-minlat/schedule.json`**: flow set, routes, and release_offset pinned to exactly what that run admitted; only phi (window timing) is being re-solved here, under this run's own constraint set.
- Solver: Z3, maximize admitted flows (binary search), then minimize total latency, timeout 3600s
- Result: **sat**, admitted 11/11 (proven optimal), solved in 6.60s
- Total latency (sum of e2e over admitted flows): **421680 ns** (proven minimum)

## Flows

stream.csv does not specify a talker offset; `offset (ns) = phi` below is the transmit time of each flow's first frame, computed by the solver (also in `offsets.csv` and `schedule.json`'s `offset_ns`).

| flow | route | L (B) | C (ns) | T (ns) | D (ns) | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|---|---|---|---|
| s0(id=1 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 200 | 12480 | 200000 | 200000 | 7 | 0 | 36880 | yes |
| s2(id=3 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 500 | 12480 | 400000 | 400000 | 7 | 0 | 54160 | yes |
| s4(id=5 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 200 | 12480 | 800000 | 800000 | 7 | 74880 | 36880 | yes |
| s6(id=7 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | 500 | 12480 | 800000 | 800000 | 6 | 24960 | 45840 | yes |
| s7(id=8 S3->S1) | S3->sw01->sw02->S1 | 500 | 12480 | 400000 | 400000 | 7 | 49920 | 33680 | yes |
| s8(id=9 S3->S1) | S3->sw01->sw02->S1 | 100 | 12480 | 200000 | 200000 | 7 | 0 | 22800 | yes |
| s11(id=12 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 300 | 12480 | 200000 | 200000 | 6 | 24960 | 50960 | yes |
| s14(id=15 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 300 | 12480 | 400000 | 400000 | 6 | 49920 | 39440 | yes |
| s17(id=18 S3->S1) | S3->sw01->sw02->S1 | 300 | 12480 | 400000 | 400000 | 6 | 74880 | 26000 | yes |
| s18(id=19 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 200 | 12480 | 800000 | 800000 | 6 | 99840 | 36880 | yes |
| s19(id=20 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 100 | 12480 | 200000 | 200000 | 6 | 24960 | 38160 | yes |

## Per-hop windows

| flow | egress port | queue | psi (ns) | delta (ns) |
|---|---|---|---|---|
| s0(id=1 S1->S2) | S1-p0 | Q7 | 0 | 12480 |
| s0(id=1 S1->S2) | sw02-p4 | Q7 | 6080 | 12480 |
| s0(id=1 S1->S2) | sw04-p5 | Q7 | 12160 | 12480 |
| s0(id=1 S1->S2) | sw06-p4 | Q7 | 18240 | 12480 |
| s0(id=1 S1->S2) | sw08-p2 | Q7 | 24320 | 12480 |
| s2(id=3 S2->S3) | S2-p0 | Q7 | 0 | 12480 |
| s2(id=3 S2->S3) | sw08-p5 | Q7 | 8320 | 12480 |
| s2(id=3 S2->S3) | sw07-p4 | Q7 | 16640 | 12480 |
| s2(id=3 S2->S3) | sw05-p5 | Q7 | 24960 | 12480 |
| s2(id=3 S2->S3) | sw03-p4 | Q7 | 33280 | 12480 |
| s2(id=3 S2->S3) | sw01-p2 | Q7 | 41600 | 12480 |
| s4(id=5 S1->S2) | S1-p0 | Q7 | 74880 | 12480 |
| s4(id=5 S1->S2) | sw02-p4 | Q7 | 80960 | 12480 |
| s4(id=5 S1->S2) | sw04-p5 | Q7 | 87040 | 12480 |
| s4(id=5 S1->S2) | sw06-p4 | Q7 | 93120 | 12480 |
| s4(id=5 S1->S2) | sw08-p2 | Q7 | 99200 | 12480 |
| s6(id=7 S2->S1) | S2-p0 | Q6 | 24960 | 12480 |
| s6(id=7 S2->S1) | sw08-p4 | Q6 | 33280 | 12480 |
| s6(id=7 S2->S1) | sw06-p5 | Q6 | 41600 | 12480 |
| s6(id=7 S2->S1) | sw04-p4 | Q6 | 49920 | 12480 |
| s6(id=7 S2->S1) | sw02-p2 | Q6 | 58240 | 12480 |
| s7(id=8 S3->S1) | S3-p0 | Q7 | 49920 | 12480 |
| s7(id=8 S3->S1) | sw01-p5 | Q7 | 58240 | 12480 |
| s7(id=8 S3->S1) | sw02-p2 | Q7 | 71040 | 12480 |
| s8(id=9 S3->S1) | S3-p0 | Q7 | 0 | 12480 |
| s8(id=9 S3->S1) | sw01-p5 | Q7 | 5120 | 12480 |
| s8(id=9 S3->S1) | sw02-p2 | Q7 | 10240 | 12480 |
| s11(id=12 S1->S2) | S1-p0 | Q6 | 24960 | 12480 |
| s11(id=12 S1->S2) | sw02-p4 | Q6 | 31680 | 12480 |
| s11(id=12 S1->S2) | sw04-p5 | Q6 | 38400 | 12480 |
| s11(id=12 S1->S2) | sw06-p4 | Q6 | 47040 | 12480 |
| s11(id=12 S1->S2) | sw08-p2 | Q6 | 63360 | 12480 |
| s14(id=15 S1->S2) | S1-p0 | Q6 | 49920 | 12480 |
| s14(id=15 S1->S2) | sw02-p4 | Q6 | 56640 | 12480 |
| s14(id=15 S1->S2) | sw04-p5 | Q6 | 63360 | 12480 |
| s14(id=15 S1->S2) | sw06-p4 | Q6 | 70080 | 12480 |
| s14(id=15 S1->S2) | sw08-p2 | Q6 | 76800 | 12480 |
| s17(id=18 S3->S1) | S3-p0 | Q6 | 74880 | 12480 |
| s17(id=18 S3->S1) | sw01-p5 | Q6 | 81600 | 12480 |
| s17(id=18 S3->S1) | sw02-p2 | Q6 | 88320 | 12480 |
| s18(id=19 S1->S2) | S1-p0 | Q6 | 99840 | 12480 |
| s18(id=19 S1->S2) | sw02-p4 | Q6 | 105920 | 12480 |
| s18(id=19 S1->S2) | sw04-p5 | Q6 | 112000 | 12480 |
| s18(id=19 S1->S2) | sw06-p4 | Q6 | 118080 | 12480 |
| s18(id=19 S1->S2) | sw08-p2 | Q6 | 124160 | 12480 |
| s19(id=20 S3->S2) | S3-p0 | Q6 | 24960 | 12480 |
| s19(id=20 S3->S2) | sw01-p4 | Q6 | 30080 | 12480 |
| s19(id=20 S3->S2) | sw03-p5 | Q6 | 35200 | 12480 |
| s19(id=20 S3->S2) | sw05-p4 | Q6 | 40320 | 12480 |
| s19(id=20 S3->S2) | sw07-p5 | Q6 | 45440 | 12480 |
| s19(id=20 S3->S2) | sw08-p2 | Q6 | 50560 | 12480 |

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

### sw01-p2  (5 entries, util 3.1200 %)

```
sgs 41600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 387520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 345920 0x3F # 00111111   BE
```

### sw01-p4  (9 entries, util 6.2400 %)

```
sgs 30080 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 157440 0x3F # 00111111   BE
```

### sw01-p5  (17 entries, util 12.4800 %)

```
sgs 5120 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 40640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 10880 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 111040 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 40640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 10880 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 111040 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 182400 0x3F # 00111111   BE
```

### sw02-p2  (19 entries, util 14.0400 %)

```
sgs 10240 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 35520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 4800 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 109440 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 48320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 4800 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 109440 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 177280 0x3F # 00111111   BE
```

### sw02-p4  (25 entries, util 18.7200 %)

```
sgs 6080 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 11840 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 87680 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 161920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 136960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 155840 0x3F # 00111111   BE
```

### sw03-p4  (5 entries, util 3.1200 %)

```
sgs 33280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 387520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 354240 0x3F # 00111111   BE
```

### sw03-p5  (9 entries, util 6.2400 %)

```
sgs 35200 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 152320 0x3F # 00111111   BE
```

### sw04-p4  (3 entries, util 1.5600 %)

```
sgs 49920 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 737600 0x3F # 00111111   BE
```

### sw04-p5  (25 entries, util 18.7200 %)

```
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13760 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 11200 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 87680 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13760 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 161280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13760 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 136320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13760 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 149120 0x3F # 00111111   BE
```

### sw05-p4  (9 entries, util 6.2400 %)

```
sgs 40320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 147200 0x3F # 00111111   BE
```

### sw05-p5  (5 entries, util 3.1200 %)

```
sgs 24960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 387520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 362560 0x3F # 00111111   BE
```

### sw06-p4  (25 entries, util 18.7200 %)

```
sgs 18240 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 16320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 10560 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 10560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 87680 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 16320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 158720 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 16320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 10560 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 135680 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 16320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 140480 0x3F # 00111111   BE
```

### sw06-p5  (3 entries, util 1.5600 %)

```
sgs 41600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 745920 0x3F # 00111111   BE
```

### sw07-p4  (5 entries, util 3.1200 %)

```
sgs 16640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 387520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 370880 0x3F # 00111111   BE
```

### sw07-p5  (9 entries, util 6.2400 %)

```
sgs 45440 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 142080 0x3F # 00111111   BE
```

### sw08-p2  (33 entries, util 24.9600 %)

```
sgs 24320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13760 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 960 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 9920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 87680 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13760 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 148480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13760 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 960 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 135040 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13760 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 124160 0x3F # 00111111   BE
```

### sw08-p4  (3 entries, util 1.5600 %)

```
sgs 33280 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 754240 0x3F # 00111111   BE
```

### sw08-p5  (5 entries, util 3.1200 %)

```
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 387520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 379200 0x3F # 00111111   BE
```

Ports carrying no TT traffic (single best-effort entry for the whole cycle): sw02-p5

