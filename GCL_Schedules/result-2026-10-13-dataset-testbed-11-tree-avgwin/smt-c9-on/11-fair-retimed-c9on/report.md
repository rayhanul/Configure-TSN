# SMT-synthesized GCL schedule (Problem 1: feasible schedule synthesis)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- TT queues: Q6, Q7; best effort filler mask 0x3F
- **Retimed from `result/result-2026-10-13-dataset-testbed-11-tree-avgwin/smt-c9-off/11-t3600-c9off-minlat/schedule.json`**: flow set, routes, and release_offset pinned to exactly what that run admitted; only phi (window timing) is being re-solved here, under this run's own constraint set.
- Solver: Z3, maximize admitted flows (binary search), then minimize total latency, timeout 3600s
- Result: **sat**, admitted 10/10 (proven optimal), solved in 11.82s
- Total latency (sum of e2e over admitted flows): **492320 ns** (proven minimum)

## Flows

stream.csv does not specify a talker offset; `offset (ns) = phi` below is the transmit time of each flow's first frame, computed by the solver (also in `offsets.csv` and `schedule.json`'s `offset_ns`).

| flow | route | L (B) | C (ns) | T (ns) | D (ns) | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|---|---|---|---|
| s0(id=1 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 500 | 12480 | 200000 | 200000 | 7 | 0 | 45840 | yes |
| s1(id=2 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 400 | 12480 | 200000 | 200000 | 7 | 0 | 58640 | yes |
| s2(id=3 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 500 | 12480 | 400000 | 400000 | 6 | 24960 | 46480 | yes |
| s4(id=5 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | 200 | 12480 | 200000 | 200000 | 6 | 0 | 36880 | yes |
| s6(id=7 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | 300 | 12480 | 800000 | 800000 | 6 | 37440 | 39440 | yes |
| s7(id=8 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 500 | 12480 | 200000 | 200000 | 7 | 24960 | 59280 | yes |
| s8(id=9 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 100 | 12480 | 800000 | 800000 | 6 | 74880 | 38160 | yes |
| s9(id=10 S3->S1) | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | 300 | 12480 | 400000 | 400000 | 7 | 49920 | 66320 | yes |
| s17(id=18 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 500 | 12480 | 800000 | 800000 | 7 | 62400 | 54160 | yes |
| s19(id=20 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 500 | 12480 | 400000 | 400000 | 6 | 49920 | 47120 | yes |

## Per-hop windows

| flow | egress port | queue | psi (ns) | delta (ns) |
|---|---|---|---|---|
| s0(id=1 S1->S2) | S1-p0 | Q7 | 0 | 12480 |
| s0(id=1 S1->S2) | sw02-p4 | Q7 | 8320 | 12480 |
| s0(id=1 S1->S2) | sw04-p5 | Q7 | 16640 | 12480 |
| s0(id=1 S1->S2) | sw06-p4 | Q7 | 24960 | 12480 |
| s0(id=1 S1->S2) | sw08-p2 | Q7 | 33280 | 12480 |
| s1(id=2 S3->S2) | S3-p0 | Q7 | 0 | 12480 |
| s1(id=2 S3->S2) | sw01-p4 | Q7 | 15360 | 12480 |
| s1(id=2 S3->S2) | sw03-p5 | Q7 | 23040 | 12480 |
| s1(id=2 S3->S2) | sw05-p4 | Q7 | 30720 | 12480 |
| s1(id=2 S3->S2) | sw07-p5 | Q7 | 38400 | 12480 |
| s1(id=2 S3->S2) | sw08-p2 | Q7 | 46080 | 12480 |
| s2(id=3 S1->S2) | S1-p0 | Q6 | 24960 | 12480 |
| s2(id=3 S1->S2) | sw02-p4 | Q6 | 33280 | 12480 |
| s2(id=3 S1->S2) | sw04-p5 | Q6 | 41600 | 12480 |
| s2(id=3 S1->S2) | sw06-p4 | Q6 | 49920 | 12480 |
| s2(id=3 S1->S2) | sw08-p2 | Q6 | 58880 | 12480 |
| s4(id=5 S2->S1) | S2-p0 | Q6 | 0 | 12480 |
| s4(id=5 S2->S1) | sw08-p4 | Q6 | 6080 | 12480 |
| s4(id=5 S2->S1) | sw06-p5 | Q6 | 12160 | 12480 |
| s4(id=5 S2->S1) | sw04-p4 | Q6 | 18240 | 12480 |
| s4(id=5 S2->S1) | sw02-p2 | Q6 | 24320 | 12480 |
| s6(id=7 S2->S1) | S2-p0 | Q6 | 37440 | 12480 |
| s6(id=7 S2->S1) | sw08-p4 | Q6 | 44160 | 12480 |
| s6(id=7 S2->S1) | sw06-p5 | Q6 | 50880 | 12480 |
| s6(id=7 S2->S1) | sw04-p4 | Q6 | 57600 | 12480 |
| s6(id=7 S2->S1) | sw02-p2 | Q6 | 64320 | 12480 |
| s7(id=8 S3->S2) | S3-p0 | Q7 | 24960 | 12480 |
| s7(id=8 S3->S2) | sw01-p4 | Q7 | 35200 | 12480 |
| s7(id=8 S3->S2) | sw03-p5 | Q7 | 43520 | 12480 |
| s7(id=8 S3->S2) | sw05-p4 | Q7 | 51840 | 12480 |
| s7(id=8 S3->S2) | sw07-p5 | Q7 | 60160 | 12480 |
| s7(id=8 S3->S2) | sw08-p2 | Q7 | 71680 | 12480 |
| s8(id=9 S3->S2) | S3-p0 | Q6 | 74880 | 12480 |
| s8(id=9 S3->S2) | sw01-p4 | Q6 | 80000 | 12480 |
| s8(id=9 S3->S2) | sw03-p5 | Q6 | 85120 | 12480 |
| s8(id=9 S3->S2) | sw05-p4 | Q6 | 90240 | 12480 |
| s8(id=9 S3->S2) | sw07-p5 | Q6 | 95360 | 12480 |
| s8(id=9 S3->S2) | sw08-p2 | Q6 | 100480 | 12480 |
| s9(id=10 S3->S1) | S3-p0 | Q7 | 49920 | 12480 |
| s9(id=10 S3->S1) | sw01-p4 | Q7 | 56640 | 12480 |
| s9(id=10 S3->S1) | sw03-p5 | Q7 | 63360 | 12480 |
| s9(id=10 S3->S1) | sw05-p4 | Q7 | 70080 | 12480 |
| s9(id=10 S3->S1) | sw07-p5 | Q7 | 76800 | 12480 |
| s9(id=10 S3->S1) | sw08-p4 | Q7 | 83520 | 12480 |
| s9(id=10 S3->S1) | sw06-p5 | Q7 | 90240 | 12480 |
| s9(id=10 S3->S1) | sw04-p4 | Q7 | 96960 | 12480 |
| s9(id=10 S3->S1) | sw02-p2 | Q7 | 103680 | 12480 |
| s17(id=18 S2->S3) | S2-p0 | Q7 | 62400 | 12480 |
| s17(id=18 S2->S3) | sw08-p5 | Q7 | 70720 | 12480 |
| s17(id=18 S2->S3) | sw07-p4 | Q7 | 79040 | 12480 |
| s17(id=18 S2->S3) | sw05-p5 | Q7 | 87360 | 12480 |
| s17(id=18 S2->S3) | sw03-p4 | Q7 | 95680 | 12480 |
| s17(id=18 S2->S3) | sw01-p2 | Q7 | 104000 | 12480 |
| s19(id=20 S1->S2) | S1-p0 | Q6 | 49920 | 12480 |
| s19(id=20 S1->S2) | sw02-p4 | Q6 | 58240 | 12480 |
| s19(id=20 S1->S2) | sw04-p5 | Q6 | 66560 | 12480 |
| s19(id=20 S1->S2) | sw06-p4 | Q6 | 74880 | 12480 |
| s19(id=20 S1->S2) | sw08-p2 | Q6 | 84480 | 12480 |

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
sgs 104000 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 683520 0x3F # 00111111   BE
```

### sw01-p4  (23 entries, util 17.1600 %)

```
sgs 15360 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 7360 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 8960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 10880 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 122880 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 7360 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 167680 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 7360 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 8960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 146240 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 7360 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 152320 0x3F # 00111111   BE
```

### sw02-p2  (15 entries, util 10.9200 %)

```
sgs 24320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 27520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 26880 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 108160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 66880 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 108160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 163200 0x3F # 00111111   BE
```

### sw02-p4  (17 entries, util 12.4800 %)

```
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 137600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 137600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 179200 0x3F # 00111111   BE
```

### sw03-p4  (3 entries, util 1.5600 %)

```
sgs 95680 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 691840 0x3F # 00111111   BE
```

### sw03-p5  (23 entries, util 17.1600 %)

```
sgs 23040 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 8000 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 7360 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 9280 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 125440 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 8000 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 167040 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 8000 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 7360 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 147200 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 8000 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 144000 0x3F # 00111111   BE
```

### sw04-p4  (15 entries, util 10.9200 %)

```
sgs 18240 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 26880 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 26880 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 108800 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 66240 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 108800 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 169280 0x3F # 00111111   BE
```

### sw04-p5  (17 entries, util 12.4800 %)

```
sgs 16640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 137600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 137600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 170880 0x3F # 00111111   BE
```

### sw05-p4  (23 entries, util 17.1600 %)

```
sgs 30720 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 8640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 5760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 7680 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 128000 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 8640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 166400 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 8640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 5760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 148160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 8640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 135680 0x3F # 00111111   BE
```

### sw05-p5  (3 entries, util 1.5600 %)

```
sgs 87360 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 700160 0x3F # 00111111   BE
```

### sw06-p4  (17 entries, util 12.4800 %)

```
sgs 24960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 137600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 137600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 162560 0x3F # 00111111   BE
```

### sw06-p5  (15 entries, util 10.9200 %)

```
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 26240 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 26880 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 109440 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 65600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 109440 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 175360 0x3F # 00111111   BE
```

### sw07-p4  (3 entries, util 1.5600 %)

```
sgs 79040 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 708480 0x3F # 00111111   BE
```

### sw07-p5  (23 entries, util 17.1600 %)

```
sgs 38400 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 9280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 6080 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 130560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 9280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 165760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 9280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 149120 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 9280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 127360 0x3F # 00111111   BE
```

### sw08-p2  (35 entries, util 26.5200 %)

```
sgs 33280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 3520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 120320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 149120 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 136320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 115840 0x3F # 00111111   BE
```

### sw08-p4  (15 entries, util 10.9200 %)

```
sgs 6080 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 25600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 26880 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 110080 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 64960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 110080 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 181440 0x3F # 00111111   BE
```

### sw08-p5  (3 entries, util 1.5600 %)

```
sgs 70720 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 716800 0x3F # 00111111   BE
```

