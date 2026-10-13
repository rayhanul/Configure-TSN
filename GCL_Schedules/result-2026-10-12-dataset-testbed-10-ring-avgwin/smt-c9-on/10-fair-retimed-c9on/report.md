# SMT-synthesized GCL schedule (Problem 1: feasible schedule synthesis)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- TT queues: Q6, Q7; best effort filler mask 0x3F
- **Retimed from `result/result-2026-10-12-dataset-testbed-10-ring-avgwin/smt-c9-off/10-t3600-c9off-minlat/schedule.json`**: flow set, routes, and release_offset pinned to exactly what that run admitted; only phi (window timing) is being re-solved here, under this run's own constraint set.
- Solver: Z3, maximize admitted flows (binary search), then minimize total latency, timeout 3600s
- Result: **sat**, admitted 11/11 (proven optimal), solved in 5.43s
- Total latency (sum of e2e over admitted flows): **413040 ns** (proven minimum)

## Flows

stream.csv does not specify a talker offset; `offset (ns) = phi` below is the transmit time of each flow's first frame, computed by the solver (also in `offsets.csv` and `schedule.json`'s `offset_ns`).

| flow | route | L (B) | C (ns) | T (ns) | D (ns) | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|---|---|---|---|
| s0(id=1 S3->S1) | S3->sw01->sw02->S1 | 400 | 12480 | 400000 | 400000 | 6 | 24960 | 27920 | yes |
| s2(id=3 S1->S3) | S1->sw02->sw01->S3 | 400 | 12480 | 200000 | 200000 | 6 | 0 | 27920 | yes |
| s4(id=5 S3->S1) | S3->sw01->sw02->S1 | 400 | 12480 | 800000 | 800000 | 7 | 74880 | 31120 | yes |
| s6(id=7 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 200 | 12480 | 200000 | 200000 | 7 | 0 | 42960 | yes |
| s8(id=9 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 400 | 12480 | 200000 | 200000 | 7 | 0 | 50960 | yes |
| s9(id=10 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | 400 | 12480 | 800000 | 800000 | 6 | 49920 | 43280 | yes |
| s10(id=11 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 200 | 12480 | 400000 | 400000 | 7 | 24960 | 42960 | yes |
| s11(id=12 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 500 | 12480 | 200000 | 200000 | 7 | 24960 | 45840 | yes |
| s14(id=15 S3->S1) | S3->sw01->sw02->S1 | 300 | 12480 | 400000 | 400000 | 6 | 49920 | 26000 | yes |
| s16(id=17 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 400 | 12480 | 800000 | 800000 | 6 | 74880 | 43280 | yes |
| s17(id=18 S1->S3) | S1->sw02->sw01->S3 | 200 | 12480 | 400000 | 400000 | 6 | 49920 | 30800 | yes |

## Per-hop windows

| flow | egress port | queue | psi (ns) | delta (ns) |
|---|---|---|---|---|
| s0(id=1 S3->S1) | S3-p0 | Q6 | 24960 | 12480 |
| s0(id=1 S3->S1) | sw01-p5 | Q6 | 32640 | 12480 |
| s0(id=1 S3->S1) | sw02-p2 | Q6 | 40320 | 12480 |
| s2(id=3 S1->S3) | S1-p0 | Q6 | 0 | 12480 |
| s2(id=3 S1->S3) | sw02-p5 | Q6 | 7680 | 12480 |
| s2(id=3 S1->S3) | sw01-p2 | Q6 | 15360 | 12480 |
| s4(id=5 S3->S1) | S3-p0 | Q7 | 74880 | 12480 |
| s4(id=5 S3->S1) | sw01-p5 | Q7 | 82560 | 12480 |
| s4(id=5 S3->S1) | sw02-p2 | Q7 | 93440 | 12480 |
| s6(id=7 S2->S3) | S2-p0 | Q7 | 0 | 12480 |
| s6(id=7 S2->S3) | sw08-p5 | Q7 | 6080 | 12480 |
| s6(id=7 S2->S3) | sw07-p4 | Q7 | 12160 | 12480 |
| s6(id=7 S2->S3) | sw05-p5 | Q7 | 18240 | 12480 |
| s6(id=7 S2->S3) | sw03-p4 | Q7 | 24320 | 12480 |
| s6(id=7 S2->S3) | sw01-p2 | Q7 | 30400 | 12480 |
| s8(id=9 S3->S2) | S3-p0 | Q7 | 0 | 12480 |
| s8(id=9 S3->S2) | sw01-p4 | Q7 | 7680 | 12480 |
| s8(id=9 S3->S2) | sw03-p5 | Q7 | 15360 | 12480 |
| s8(id=9 S3->S2) | sw05-p4 | Q7 | 23040 | 12480 |
| s8(id=9 S3->S2) | sw07-p5 | Q7 | 30720 | 12480 |
| s8(id=9 S3->S2) | sw08-p2 | Q7 | 38400 | 12480 |
| s9(id=10 S2->S1) | S2-p0 | Q6 | 49920 | 12480 |
| s9(id=10 S2->S1) | sw08-p4 | Q6 | 57600 | 12480 |
| s9(id=10 S2->S1) | sw06-p5 | Q6 | 65280 | 12480 |
| s9(id=10 S2->S1) | sw04-p4 | Q6 | 72960 | 12480 |
| s9(id=10 S2->S1) | sw02-p2 | Q6 | 80640 | 12480 |
| s10(id=11 S2->S3) | S2-p0 | Q7 | 24960 | 12480 |
| s10(id=11 S2->S3) | sw08-p5 | Q7 | 31040 | 12480 |
| s10(id=11 S2->S3) | sw07-p4 | Q7 | 37120 | 12480 |
| s10(id=11 S2->S3) | sw05-p5 | Q7 | 43200 | 12480 |
| s10(id=11 S2->S3) | sw03-p4 | Q7 | 49280 | 12480 |
| s10(id=11 S2->S3) | sw01-p2 | Q7 | 55360 | 12480 |
| s11(id=12 S1->S2) | S1-p0 | Q7 | 24960 | 12480 |
| s11(id=12 S1->S2) | sw02-p4 | Q7 | 33280 | 12480 |
| s11(id=12 S1->S2) | sw04-p5 | Q7 | 41600 | 12480 |
| s11(id=12 S1->S2) | sw06-p4 | Q7 | 49920 | 12480 |
| s11(id=12 S1->S2) | sw08-p2 | Q7 | 58240 | 12480 |
| s14(id=15 S3->S1) | S3-p0 | Q6 | 49920 | 12480 |
| s14(id=15 S3->S1) | sw01-p5 | Q6 | 56640 | 12480 |
| s14(id=15 S3->S1) | sw02-p2 | Q6 | 63360 | 12480 |
| s16(id=17 S1->S2) | S1-p0 | Q6 | 74880 | 12480 |
| s16(id=17 S1->S2) | sw02-p4 | Q6 | 82560 | 12480 |
| s16(id=17 S1->S2) | sw04-p5 | Q6 | 90240 | 12480 |
| s16(id=17 S1->S2) | sw06-p4 | Q6 | 97920 | 12480 |
| s16(id=17 S1->S2) | sw08-p2 | Q6 | 105600 | 12480 |
| s17(id=18 S1->S3) | S1-p0 | Q6 | 49920 | 12480 |
| s17(id=18 S1->S3) | sw02-p5 | Q6 | 56000 | 12480 |
| s17(id=18 S1->S3) | sw01-p2 | Q6 | 68160 | 12480 |

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

### sw01-p2  (25 entries, util 18.7200 %)

```
sgs 15360 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 2560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 134720 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 2560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 172480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 2560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 134720 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 2560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 157120 0x3F # 00111111   BE
```

### sw01-p4  (9 entries, util 6.2400 %)

```
sgs 7680 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 179840 0x3F # 00111111   BE
```

### sw01-p5  (11 entries, util 7.8000 %)

```
sgs 32640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 11520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 13440 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 337600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 11520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 330880 0x3F # 00111111   BE
```

### sw02-p2  (13 entries, util 9.3600 %)

```
sgs 40320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 10560 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 4800 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 334400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 10560 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 324160 0x3F # 00111111   BE
```

### sw02-p4  (11 entries, util 7.8000 %)

```
sgs 33280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 36800 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 138240 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 154240 0x3F # 00111111   BE
```

### sw02-p5  (13 entries, util 9.3600 %)

```
sgs 7680 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 35840 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 139200 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 35840 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 139200 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 179840 0x3F # 00111111   BE
```

### sw03-p4  (13 entries, util 9.3600 %)

```
sgs 24320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 162560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 162560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 163200 0x3F # 00111111   BE
```

### sw03-p5  (9 entries, util 6.2400 %)

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

### sw04-p4  (3 entries, util 1.5600 %)

```
sgs 72960 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 714560 0x3F # 00111111   BE
```

### sw04-p5  (11 entries, util 7.8000 %)

```
sgs 41600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 36160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 138880 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 145920 0x3F # 00111111   BE
```

### sw05-p4  (9 entries, util 6.2400 %)

```
sgs 23040 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 164480 0x3F # 00111111   BE
```

### sw05-p5  (13 entries, util 9.3600 %)

```
sgs 18240 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 162560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 162560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 169280 0x3F # 00111111   BE
```

### sw06-p4  (11 entries, util 7.8000 %)

```
sgs 49920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 35520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 139520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 137600 0x3F # 00111111   BE
```

### sw06-p5  (3 entries, util 1.5600 %)

```
sgs 65280 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 722240 0x3F # 00111111   BE
```

### sw07-p4  (13 entries, util 9.3600 %)

```
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 162560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 162560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 175360 0x3F # 00111111   BE
```

### sw07-p5  (9 entries, util 6.2400 %)

```
sgs 30720 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 156800 0x3F # 00111111   BE
```

### sw08-p2  (19 entries, util 14.0400 %)

```
sgs 38400 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 7360 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 34880 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 120320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 7360 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 167680 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 7360 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 167680 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 7360 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 129280 0x3F # 00111111   BE
```

### sw08-p4  (3 entries, util 1.5600 %)

```
sgs 57600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 729920 0x3F # 00111111   BE
```

### sw08-p5  (13 entries, util 9.3600 %)

```
sgs 6080 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 162560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 162560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 181440 0x3F # 00111111   BE
```

