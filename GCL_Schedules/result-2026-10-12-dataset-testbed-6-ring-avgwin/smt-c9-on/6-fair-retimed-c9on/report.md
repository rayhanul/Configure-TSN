# SMT-synthesized GCL schedule (Problem 1: feasible schedule synthesis)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- TT queues: Q6, Q7; best effort filler mask 0x3F
- **Retimed from `result/result-2026-10-12-dataset-testbed-6-ring-avgwin/smt-c9-off/6-t3600-c9off-minlat/schedule.json`**: flow set, routes, and release_offset pinned to exactly what that run admitted; only phi (window timing) is being re-solved here, under this run's own constraint set.
- Solver: Z3, maximize admitted flows (binary search), then minimize total latency, timeout 3600s
- Result: **sat**, admitted 10/10 (proven optimal), solved in 2.26s
- Total latency (sum of e2e over admitted flows): **354080 ns** (proven minimum)

## Flows

stream.csv does not specify a talker offset; `offset (ns) = phi` below is the transmit time of each flow's first frame, computed by the solver (also in `offsets.csv` and `schedule.json`'s `offset_ns`).

| flow | route | L (B) | C (ns) | T (ns) | D (ns) | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|---|---|---|---|
| s0(id=1 S3->S1) | S3->sw01->sw02->S1 | 500 | 12480 | 200000 | 200000 | 7 | 0 | 29200 | yes |
| s1(id=2 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | 400 | 12480 | 200000 | 200000 | 6 | 0 | 43280 | yes |
| s3(id=4 S1->S3) | S1->sw02->sw01->S3 | 300 | 12480 | 800000 | 800000 | 6 | 24960 | 26000 | yes |
| s5(id=6 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | 100 | 12480 | 400000 | 400000 | 6 | 24960 | 33040 | yes |
| s6(id=7 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | 300 | 12480 | 800000 | 800000 | 7 | 49920 | 39440 | yes |
| s8(id=9 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 500 | 12480 | 200000 | 200000 | 6 | 24960 | 54160 | yes |
| s11(id=12 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | 100 | 12480 | 800000 | 800000 | 7 | 74880 | 42000 | yes |
| s13(id=14 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 100 | 12480 | 200000 | 200000 | 7 | 0 | 33040 | yes |
| s18(id=19 S3->S1) | S3->sw01->sw02->S1 | 500 | 12480 | 400000 | 400000 | 6 | 74880 | 29200 | yes |
| s19(id=20 S3->S1) | S3->sw01->sw02->S1 | 200 | 12480 | 200000 | 200000 | 6 | 49920 | 24720 | yes |

## Per-hop windows

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

- C1 window non-overlap: OK
- C2 unique queue assignment: OK
- C3 unique window assignment: OK
- C4 window length >= frame transmission time: OK (windows are built tight, delta == the sum of the frames they carry, never enlarged)
- C5 determinism at merge points (queue isolation): OK
- C6 tick alignment, cycle <= C_max, entries <= GCL_size: OK
- C7 end-to-end deadline and jitter: OK
- C9 supplier/receiver window timing: OK

## GCL per egress port

### sw01-p2  (3 entries, util 1.5600 %)

```
sgs 38400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 749120 0x3F # 00111111   BE
```

### sw01-p4  (9 entries, util 6.2400 %)

```
sgs 33280 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 154240 0x3F # 00111111   BE
```

### sw01-p5  (21 entries, util 15.6000 %)

```
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 35200 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 14720 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 112640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 35200 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 139840 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 35200 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 14720 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 112640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 35200 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 131520 0x3F # 00111111   BE
```

### sw02-p2  (37 entries, util 28.0800 %)

```
sgs 16640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 1600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 2240 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 2240 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 2240 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 99840 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 1600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 18880 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 142080 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 1600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 2240 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 16960 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 112640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 1600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 18880 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 125440 0x3F # 00111111   BE
```

### sw02-p4  (9 entries, util 6.2400 %)

```
sgs 5120 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 182400 0x3F # 00111111   BE
```

### sw02-p5  (3 entries, util 1.5600 %)

```
sgs 31680 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 755840 0x3F # 00111111   BE
```

### sw03-p5  (9 entries, util 6.2400 %)

```
sgs 41600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 145920 0x3F # 00111111   BE
```

### sw04-p4  (17 entries, util 12.4800 %)

```
sgs 23040 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 4800 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 17280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 7680 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 120320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 4800 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 170240 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 164480 0x3F # 00111111   BE
```

### sw04-p5  (9 entries, util 6.2400 %)

```
sgs 10240 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 177280 0x3F # 00111111   BE
```

### sw05-p4  (9 entries, util 6.2400 %)

```
sgs 49920 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 137600 0x3F # 00111111   BE
```

### sw06-p4  (9 entries, util 6.2400 %)

```
sgs 15360 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 172160 0x3F # 00111111   BE
```

### sw06-p5  (17 entries, util 12.4800 %)

```
sgs 15360 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 7360 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 15680 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 9280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 117760 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 7360 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 167680 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 172160 0x3F # 00111111   BE
```

### sw07-p5  (9 entries, util 6.2400 %)

```
sgs 58240 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 129280 0x3F # 00111111   BE
```

### sw08-p2  (17 entries, util 12.4800 %)

```
sgs 20480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 33600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 141440 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 33600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 141440 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 33600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 141440 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 33600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 120960 0x3F # 00111111   BE
```

### sw08-p4  (17 entries, util 12.4800 %)

```
sgs 7680 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 9920 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 14080 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 10880 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 115200 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 9920 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 165120 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 179840 0x3F # 00111111   BE
```

Ports carrying no TT traffic (single best-effort entry for the whole cycle): sw03-p4, sw05-p5, sw07-p4, sw08-p5

