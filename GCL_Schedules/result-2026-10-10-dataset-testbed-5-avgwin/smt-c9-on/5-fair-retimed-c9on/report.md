# SMT-synthesized GCL schedule (Problem 1: feasible schedule synthesis)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- TT queues: Q6, Q7; best effort filler mask 0x3F
- **Retimed from `result/result-2026-10-10-dataset-testbed-5-avgwin/smt-c9-off/5-t3600-c9off-minlat/schedule.json`**: flow set, routes, and release_offset pinned to exactly what that run admitted; only phi (window timing) is being re-solved here, under this run's own constraint set.
- Solver: Z3, maximize admitted flows (binary search), then minimize total latency, timeout 3600s
- Result: **sat**, admitted 10/10 (proven optimal), solved in 11.80s
- Total latency (sum of e2e over admitted flows): **504160 ns** (proven minimum)

## Flows

stream.csv does not specify a talker offset; `offset (ns) = phi` below is the transmit time of each flow's first frame, computed by the solver (also in `offsets.csv` and `schedule.json`'s `offset_ns`).

| flow | route | L (B) | C (ns) | T (ns) | D (ns) | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|---|---|---|---|
| s1(id=2 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 300 | 12480 | 200000 | 200000 | 7 | 0 | 46160 | yes |
| s2(id=3 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 100 | 12480 | 800000 | 800000 | 7 | 62400 | 56720 | yes |
| s4(id=5 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 100 | 12480 | 800000 | 800000 | 7 | 62400 | 38160 | yes |
| s8(id=9 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | 500 | 12480 | 400000 | 400000 | 6 | 37440 | 45840 | yes |
| s9(id=10 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 500 | 12480 | 200000 | 200000 | 6 | 0 | 45840 | yes |
| s11(id=12 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 500 | 12480 | 200000 | 200000 | 6 | 12480 | 54160 | yes |
| s12(id=13 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | 400 | 12480 | 800000 | 800000 | 7 | 87360 | 74000 | yes |
| s15(id=16 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 200 | 12480 | 800000 | 800000 | 6 | 62400 | 43920 | yes |
| s16(id=17 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 400 | 12480 | 400000 | 400000 | 7 | 37440 | 43280 | yes |
| s18(id=19 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 500 | 12480 | 400000 | 400000 | 6 | 37440 | 56080 | yes |

## Per-hop windows

| flow | egress port | queue | psi (ns) | delta (ns) |
|---|---|---|---|---|
| s1(id=2 S2->S3) | S2-p0 | Q7 | 0 | 12480 |
| s1(id=2 S2->S3) | sw08-p5 | Q7 | 6720 | 12480 |
| s1(id=2 S2->S3) | sw07-p4 | Q7 | 13440 | 12480 |
| s1(id=2 S2->S3) | sw05-p5 | Q7 | 20160 | 12480 |
| s1(id=2 S2->S3) | sw03-p4 | Q7 | 26880 | 12480 |
| s1(id=2 S2->S3) | sw01-p2 | Q7 | 33600 | 12480 |
| s2(id=3 S1->S2) | S1-p0 | Q7 | 62400 | 12480 |
| s2(id=3 S1->S2) | sw02-p4 | Q7 | 67520 | 12480 |
| s2(id=3 S1->S2) | sw04-p5 | Q7 | 72640 | 12480 |
| s2(id=3 S1->S2) | sw06-p4 | Q7 | 77760 | 12480 |
| s2(id=3 S1->S2) | sw08-p2 | Q7 | 106560 | 12480 |
| s4(id=5 S2->S3) | S2-p0 | Q7 | 62400 | 12480 |
| s4(id=5 S2->S3) | sw08-p5 | Q7 | 67520 | 12480 |
| s4(id=5 S2->S3) | sw07-p4 | Q7 | 72640 | 12480 |
| s4(id=5 S2->S3) | sw05-p5 | Q7 | 77760 | 12480 |
| s4(id=5 S2->S3) | sw03-p4 | Q7 | 82880 | 12480 |
| s4(id=5 S2->S3) | sw01-p2 | Q7 | 88000 | 12480 |
| s8(id=9 S2->S1) | S2-p0 | Q6 | 37440 | 12480 |
| s8(id=9 S2->S1) | sw08-p4 | Q6 | 45760 | 12480 |
| s8(id=9 S2->S1) | sw06-p5 | Q6 | 54080 | 12480 |
| s8(id=9 S2->S1) | sw04-p4 | Q6 | 62400 | 12480 |
| s8(id=9 S2->S1) | sw02-p2 | Q6 | 70720 | 12480 |
| s9(id=10 S1->S2) | S1-p0 | Q6 | 0 | 12480 |
| s9(id=10 S1->S2) | sw02-p4 | Q6 | 8320 | 12480 |
| s9(id=10 S1->S2) | sw04-p5 | Q6 | 16640 | 12480 |
| s9(id=10 S1->S2) | sw06-p4 | Q6 | 24960 | 12480 |
| s9(id=10 S1->S2) | sw08-p2 | Q6 | 33280 | 12480 |
| s11(id=12 S3->S2) | S3-p0 | Q6 | 12480 | 12480 |
| s11(id=12 S3->S2) | sw01-p4 | Q6 | 20800 | 12480 |
| s11(id=12 S3->S2) | sw03-p5 | Q6 | 29120 | 12480 |
| s11(id=12 S3->S2) | sw05-p4 | Q6 | 37440 | 12480 |
| s11(id=12 S3->S2) | sw07-p5 | Q6 | 45760 | 12480 |
| s11(id=12 S3->S2) | sw08-p2 | Q6 | 54080 | 12480 |
| s12(id=13 S1->S3) | S1-p0 | Q7 | 87360 | 12480 |
| s12(id=13 S1->S3) | sw02-p4 | Q7 | 95040 | 12480 |
| s12(id=13 S1->S3) | sw04-p5 | Q7 | 102720 | 12480 |
| s12(id=13 S1->S3) | sw06-p4 | Q7 | 110400 | 12480 |
| s12(id=13 S1->S3) | sw08-p5 | Q7 | 118080 | 12480 |
| s12(id=13 S1->S3) | sw07-p4 | Q7 | 125760 | 12480 |
| s12(id=13 S1->S3) | sw05-p5 | Q7 | 133440 | 12480 |
| s12(id=13 S1->S3) | sw03-p4 | Q7 | 141120 | 12480 |
| s12(id=13 S1->S3) | sw01-p2 | Q7 | 148800 | 12480 |
| s15(id=16 S3->S2) | S3-p0 | Q6 | 62400 | 12480 |
| s15(id=16 S3->S2) | sw01-p4 | Q6 | 68480 | 12480 |
| s15(id=16 S3->S2) | sw03-p5 | Q6 | 74560 | 12480 |
| s15(id=16 S3->S2) | sw05-p4 | Q6 | 80640 | 12480 |
| s15(id=16 S3->S2) | sw07-p5 | Q6 | 87680 | 12480 |
| s15(id=16 S3->S2) | sw08-p2 | Q6 | 93760 | 12480 |
| s16(id=17 S1->S2) | S1-p0 | Q7 | 37440 | 12480 |
| s16(id=17 S1->S2) | sw02-p4 | Q7 | 45120 | 12480 |
| s16(id=17 S1->S2) | sw04-p5 | Q7 | 52800 | 12480 |
| s16(id=17 S1->S2) | sw06-p4 | Q7 | 60480 | 12480 |
| s16(id=17 S1->S2) | sw08-p2 | Q7 | 68160 | 12480 |
| s18(id=19 S3->S2) | S3-p0 | Q6 | 37440 | 12480 |
| s18(id=19 S3->S2) | sw01-p4 | Q6 | 47680 | 12480 |
| s18(id=19 S3->S2) | sw03-p5 | Q6 | 56000 | 12480 |
| s18(id=19 S3->S2) | sw05-p4 | Q6 | 64320 | 12480 |
| s18(id=19 S3->S2) | sw07-p5 | Q6 | 72640 | 12480 |
| s18(id=19 S3->S2) | sw08-p2 | Q6 | 80960 | 12480 |

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

### sw01-p2  (13 entries, util 9.3600 %)

```
sgs 33600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 41920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 48320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 72320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 153920 0x3F # 00111111   BE
```

### sw01-p4  (15 entries, util 10.9200 %)

```
sgs 20800 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 139840 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 160640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 166720 0x3F # 00111111   BE
```

### sw02-p2  (5 entries, util 3.1200 %)

```
sgs 70720 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 387520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 316800 0x3F # 00111111   BE
```

### sw02-p4  (17 entries, util 12.4800 %)

```
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 24320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 9920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 15040 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 100800 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 24320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 150720 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 179200 0x3F # 00111111   BE
```

### sw03-p4  (13 entries, util 9.3600 %)

```
sgs 26880 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 43520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 45760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 73280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 160640 0x3F # 00111111   BE
```

### sw03-p5  (15 entries, util 10.9200 %)

```
sgs 29120 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 6080 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 142080 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 160640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 158400 0x3F # 00111111   BE
```

### sw04-p4  (5 entries, util 3.1200 %)

```
sgs 62400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 387520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 325120 0x3F # 00111111   BE
```

### sw04-p5  (17 entries, util 12.4800 %)

```
sgs 16640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 23680 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 7360 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 17600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 101440 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 23680 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 151360 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 170880 0x3F # 00111111   BE
```

### sw05-p4  (15 entries, util 10.9200 %)

```
sgs 37440 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 3840 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 144320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 160640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 150080 0x3F # 00111111   BE
```

### sw05-p5  (13 entries, util 9.3600 %)

```
sgs 20160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 45120 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 43200 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 74240 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 167360 0x3F # 00111111   BE
```

### sw06-p4  (17 entries, util 12.4800 %)

```
sgs 24960 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 23040 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 4800 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 20160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 102080 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 23040 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 152000 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 162560 0x3F # 00111111   BE
```

### sw06-p5  (5 entries, util 3.1200 %)

```
sgs 54080 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 387520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 333440 0x3F # 00111111   BE
```

### sw07-p4  (13 entries, util 9.3600 %)

```
sgs 13440 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 46720 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 40640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 75200 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 174080 0x3F # 00111111   BE
```

### sw07-p5  (15 entries, util 10.9200 %)

```
sgs 45760 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 2560 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 145600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 160640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 141760 0x3F # 00111111   BE
```

### sw08-p2  (29 entries, util 21.8400 %)

```
sgs 33280 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 1600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 114240 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 166720 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 1600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 139840 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 133440 0x3F # 00111111   BE
```

### sw08-p4  (5 entries, util 3.1200 %)

```
sgs 45760 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 387520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 341760 0x3F # 00111111   BE
```

### sw08-p5  (13 entries, util 9.3600 %)

```
sgs 6720 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 48320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 38080 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 76160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 180800 0x3F # 00111111   BE
```

