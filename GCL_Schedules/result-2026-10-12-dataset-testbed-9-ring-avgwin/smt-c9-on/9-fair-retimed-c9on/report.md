# SMT-synthesized GCL schedule (Problem 1: feasible schedule synthesis)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- TT queues: Q6, Q7; best effort filler mask 0x3F
- **Retimed from `result/result-2026-10-12-dataset-testbed-9-ring-avgwin/smt-c9-off/9-t3600-c9off-minlat/schedule.json`**: flow set, routes, and release_offset pinned to exactly what that run admitted; only phi (window timing) is being re-solved here, under this run's own constraint set.
- Solver: Z3, maximize admitted flows (binary search), then minimize total latency, timeout 3600s
- Result: **sat**, admitted 11/11 (proven optimal), solved in 8.90s
- Total latency (sum of e2e over admitted flows): **416560 ns** (proven minimum)

## Flows

stream.csv does not specify a talker offset; `offset (ns) = phi` below is the transmit time of each flow's first frame, computed by the solver (also in `offsets.csv` and `schedule.json`'s `offset_ns`).

| flow | route | L (B) | C (ns) | T (ns) | D (ns) | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|---|---|---|---|
| s0(id=1 S3->S1) | S3->sw01->sw02->S1 | 200 | 12480 | 800000 | 800000 | 6 | 62400 | 24720 | yes |
| s3(id=4 S3->S1) | S3->sw01->sw02->S1 | 100 | 12480 | 400000 | 400000 | 7 | 37440 | 33360 | yes |
| s5(id=6 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 100 | 12480 | 200000 | 200000 | 6 | 0 | 40720 | yes |
| s6(id=7 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | 100 | 12480 | 400000 | 400000 | 6 | 24960 | 33040 | yes |
| s7(id=8 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 400 | 12480 | 800000 | 800000 | 6 | 74880 | 50960 | yes |
| s8(id=9 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 500 | 12480 | 800000 | 800000 | 7 | 87360 | 54160 | yes |
| s9(id=10 S3->S1) | S3->sw01->sw02->S1 | 400 | 12480 | 200000 | 200000 | 6 | 12480 | 27920 | yes |
| s11(id=12 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 200 | 12480 | 800000 | 800000 | 6 | 24960 | 36880 | yes |
| s13(id=14 S1->S3) | S1->sw02->sw01->S3 | 400 | 12480 | 200000 | 200000 | 6 | 0 | 27920 | yes |
| s15(id=16 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | 500 | 12480 | 400000 | 400000 | 6 | 49920 | 50000 | yes |
| s19(id=20 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | 200 | 12480 | 800000 | 800000 | 6 | 99840 | 36880 | yes |

## Per-hop windows

| flow | egress port | queue | psi (ns) | delta (ns) |
|---|---|---|---|---|
| s0(id=1 S3->S1) | S3-p0 | Q6 | 62400 | 12480 |
| s0(id=1 S3->S1) | sw01-p5 | Q6 | 68480 | 12480 |
| s0(id=1 S3->S1) | sw02-p2 | Q6 | 74560 | 12480 |
| s3(id=4 S3->S1) | S3-p0 | Q7 | 37440 | 12480 |
| s3(id=4 S3->S1) | sw01-p5 | Q7 | 53120 | 12480 |
| s3(id=4 S3->S1) | sw02-p2 | Q7 | 58240 | 12480 |
| s5(id=6 S2->S3) | S2-p0 | Q6 | 0 | 12480 |
| s5(id=6 S2->S3) | sw08-p5 | Q6 | 5120 | 12480 |
| s5(id=6 S2->S3) | sw07-p4 | Q6 | 10240 | 12480 |
| s5(id=6 S2->S3) | sw05-p5 | Q6 | 15360 | 12480 |
| s5(id=6 S2->S3) | sw03-p4 | Q6 | 20480 | 12480 |
| s5(id=6 S2->S3) | sw01-p2 | Q6 | 28160 | 12480 |
| s6(id=7 S2->S1) | S2-p0 | Q6 | 24960 | 12480 |
| s6(id=7 S2->S1) | sw08-p4 | Q6 | 30080 | 12480 |
| s6(id=7 S2->S1) | sw06-p5 | Q6 | 35200 | 12480 |
| s6(id=7 S2->S1) | sw04-p4 | Q6 | 40320 | 12480 |
| s6(id=7 S2->S1) | sw02-p2 | Q6 | 45440 | 12480 |
| s7(id=8 S2->S3) | S2-p0 | Q6 | 74880 | 12480 |
| s7(id=8 S2->S3) | sw08-p5 | Q6 | 82560 | 12480 |
| s7(id=8 S2->S3) | sw07-p4 | Q6 | 90240 | 12480 |
| s7(id=8 S2->S3) | sw05-p5 | Q6 | 97920 | 12480 |
| s7(id=8 S2->S3) | sw03-p4 | Q6 | 105600 | 12480 |
| s7(id=8 S2->S3) | sw01-p2 | Q6 | 113280 | 12480 |
| s8(id=9 S3->S2) | S3-p0 | Q7 | 87360 | 12480 |
| s8(id=9 S3->S2) | sw01-p4 | Q7 | 95680 | 12480 |
| s8(id=9 S3->S2) | sw03-p5 | Q7 | 104000 | 12480 |
| s8(id=9 S3->S2) | sw05-p4 | Q7 | 112320 | 12480 |
| s8(id=9 S3->S2) | sw07-p5 | Q7 | 120640 | 12480 |
| s8(id=9 S3->S2) | sw08-p2 | Q7 | 128960 | 12480 |
| s9(id=10 S3->S1) | S3-p0 | Q6 | 12480 | 12480 |
| s9(id=10 S3->S1) | sw01-p5 | Q6 | 20160 | 12480 |
| s9(id=10 S3->S1) | sw02-p2 | Q6 | 27840 | 12480 |
| s11(id=12 S1->S2) | S1-p0 | Q6 | 24960 | 12480 |
| s11(id=12 S1->S2) | sw02-p4 | Q6 | 31040 | 12480 |
| s11(id=12 S1->S2) | sw04-p5 | Q6 | 37120 | 12480 |
| s11(id=12 S1->S2) | sw06-p4 | Q6 | 43200 | 12480 |
| s11(id=12 S1->S2) | sw08-p2 | Q6 | 49280 | 12480 |
| s13(id=14 S1->S3) | S1-p0 | Q6 | 0 | 12480 |
| s13(id=14 S1->S3) | sw02-p5 | Q6 | 7680 | 12480 |
| s13(id=14 S1->S3) | sw01-p2 | Q6 | 15360 | 12480 |
| s15(id=16 S2->S1) | S2-p0 | Q6 | 49920 | 12480 |
| s15(id=16 S2->S1) | sw08-p4 | Q6 | 60800 | 12480 |
| s15(id=16 S2->S1) | sw06-p5 | Q6 | 69120 | 12480 |
| s15(id=16 S2->S1) | sw04-p4 | Q6 | 77440 | 12480 |
| s15(id=16 S2->S1) | sw02-p2 | Q6 | 87360 | 12480 |
| s19(id=20 S2->S1) | S2-p0 | Q6 | 99840 | 12480 |
| s19(id=20 S2->S1) | sw08-p4 | Q6 | 105920 | 12480 |
| s19(id=20 S2->S1) | sw06-p5 | Q6 | 112000 | 12480 |
| s19(id=20 S2->S1) | sw04-p4 | Q6 | 118080 | 12480 |
| s19(id=20 S2->S1) | sw02-p2 | Q6 | 124160 | 12480 |

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

### sw01-p2  (19 entries, util 14.0400 %)

```
sgs 15360 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 72640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 89600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 174720 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 174720 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 159360 0x3F # 00111111   BE
```

### sw01-p4  (3 entries, util 1.5600 %)

```
sgs 95680 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 691840 0x3F # 00111111   BE
```

### sw01-p5  (15 entries, util 10.9200 %)

```
sgs 20160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 20480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 2880 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 139200 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 20480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 154560 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 167360 0x3F # 00111111   BE
```

### sw02-p2  (25 entries, util 18.7200 %)

```
sgs 27840 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 5120 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 3840 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 24320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 91200 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 5120 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 16640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 128000 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 159680 0x3F # 00111111   BE
```

### sw02-p4  (3 entries, util 1.5600 %)

```
sgs 31040 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 756480 0x3F # 00111111   BE
```

### sw02-p5  (9 entries, util 6.2400 %)

```
sgs 7680 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 179840 0x3F # 00111111   BE
```

### sw03-p4  (11 entries, util 7.8000 %)

```
sgs 20480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 72640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 102400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 167040 0x3F # 00111111   BE
```

### sw03-p5  (3 entries, util 1.5600 %)

```
sgs 104000 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 683520 0x3F # 00111111   BE
```

### sw04-p4  (11 entries, util 7.8000 %)

```
sgs 40320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 24640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 28160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 309760 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 24640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 310080 0x3F # 00111111   BE
```

### sw04-p5  (3 entries, util 1.5600 %)

```
sgs 37120 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 750400 0x3F # 00111111   BE
```

### sw05-p4  (3 entries, util 1.5600 %)

```
sgs 112320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 675200 0x3F # 00111111   BE
```

### sw05-p5  (11 entries, util 7.8000 %)

```
sgs 15360 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 70080 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 104960 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 172160 0x3F # 00111111   BE
```

### sw06-p4  (3 entries, util 1.5600 %)

```
sgs 43200 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 744320 0x3F # 00111111   BE
```

### sw06-p5  (11 entries, util 7.8000 %)

```
sgs 35200 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 21440 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 30400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 310720 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 21440 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 318400 0x3F # 00111111   BE
```

### sw07-p4  (11 entries, util 7.8000 %)

```
sgs 10240 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 67520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 107520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 177280 0x3F # 00111111   BE
```

### sw07-p5  (3 entries, util 1.5600 %)

```
sgs 120640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 666880 0x3F # 00111111   BE
```

### sw08-p2  (5 entries, util 3.1200 %)

```
sgs 49280 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 67200 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 658560 0x3F # 00111111   BE
```

### sw08-p4  (11 entries, util 7.8000 %)

```
sgs 30080 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 18240 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 32640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 311680 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 18240 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 326720 0x3F # 00111111   BE
```

### sw08-p5  (11 entries, util 7.8000 %)

```
sgs 5120 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 64960 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 110080 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 182400 0x3F # 00111111   BE
```

