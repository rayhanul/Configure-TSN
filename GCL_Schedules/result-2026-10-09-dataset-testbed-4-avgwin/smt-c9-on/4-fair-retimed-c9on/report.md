# SMT-synthesized GCL schedule (Problem 1: feasible schedule synthesis)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- TT queues: Q6, Q7; best effort filler mask 0x3F
- **Retimed from `result/result-2026-10-09-dataset-testbed-4-avgwin/smt-c9-off/4-t3600-c9off-minlat/schedule.json`**: flow set, routes, and release_offset pinned to exactly what that run admitted; only phi (window timing) is being re-solved here, under this run's own constraint set.
- Solver: Z3, maximize admitted flows (binary search), then minimize total latency, timeout 3600s
- Result: **sat**, admitted 11/11 (proven optimal), solved in 14.21s
- Total latency (sum of e2e over admitted flows): **406640 ns** (proven minimum)

## Flows

stream.csv does not specify a talker offset; `offset (ns) = phi` below is the transmit time of each flow's first frame, computed by the solver (also in `offsets.csv` and `schedule.json`'s `offset_ns`).

| flow | route | L (B) | C (ns) | T (ns) | D (ns) | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|---|---|---|---|
| s0(id=1 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 300 | 12480 | 400000 | 400000 | 6 | 24960 | 33360 | yes |
| s2(id=3 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 100 | 12480 | 400000 | 400000 | 7 | 24960 | 33360 | yes |
| s5(id=6 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | 300 | 12480 | 800000 | 800000 | 7 | 49920 | 46800 | yes |
| s7(id=8 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 500 | 12480 | 200000 | 200000 | 7 | 0 | 33360 | yes |
| s8(id=9 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | 400 | 12480 | 800000 | 800000 | 6 | 74880 | 45840 | yes |
| s9(id=10 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 400 | 12480 | 400000 | 400000 | 6 | 49920 | 33360 | yes |
| s12(id=13 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 400 | 12480 | 200000 | 200000 | 7 | 0 | 29200 | yes |
| s13(id=14 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 500 | 12480 | 200000 | 200000 | 7 | 0 | 42000 | yes |
| s17(id=18 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | 300 | 12480 | 800000 | 800000 | 7 | 74880 | 29200 | yes |
| s18(id=19 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 500 | 12480 | 400000 | 400000 | 6 | 49920 | 34000 | yes |
| s19(id=20 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | 100 | 12480 | 200000 | 200000 | 7 | 24960 | 46160 | yes |

## Per-hop windows

| flow | egress port | queue | psi (ns) | delta (ns) |
|---|---|---|---|---|
| s0(id=1 S3->S2) | S3-p0 | Q6 | 24960 | 12480 |
| s0(id=1 S3->S2) | sw01-p4 | Q6 | 29120 | 12480 |
| s0(id=1 S3->S2) | sw03-p5 | Q6 | 33280 | 12480 |
| s0(id=1 S3->S2) | sw05-p4 | Q6 | 37440 | 12480 |
| s0(id=1 S3->S2) | sw07-p5 | Q6 | 41600 | 12480 |
| s0(id=1 S3->S2) | sw08-p2 | Q6 | 45760 | 12480 |
| s2(id=3 S2->S3) | S2-p0 | Q7 | 24960 | 12480 |
| s2(id=3 S2->S3) | sw08-p5 | Q7 | 29120 | 12480 |
| s2(id=3 S2->S3) | sw07-p4 | Q7 | 33280 | 12480 |
| s2(id=3 S2->S3) | sw05-p5 | Q7 | 37440 | 12480 |
| s2(id=3 S2->S3) | sw03-p4 | Q7 | 41600 | 12480 |
| s2(id=3 S2->S3) | sw01-p2 | Q7 | 45760 | 12480 |
| s5(id=6 S1->S3) | S1-p0 | Q7 | 49920 | 12480 |
| s5(id=6 S1->S3) | sw02-p4 | Q7 | 54080 | 12480 |
| s5(id=6 S1->S3) | sw04-p5 | Q7 | 58240 | 12480 |
| s5(id=6 S1->S3) | sw06-p4 | Q7 | 62400 | 12480 |
| s5(id=6 S1->S3) | sw08-p5 | Q7 | 67520 | 12480 |
| s5(id=6 S1->S3) | sw07-p4 | Q7 | 71680 | 12480 |
| s5(id=6 S1->S3) | sw05-p5 | Q7 | 75840 | 12480 |
| s5(id=6 S1->S3) | sw03-p4 | Q7 | 80000 | 12480 |
| s5(id=6 S1->S3) | sw01-p2 | Q7 | 84160 | 12480 |
| s7(id=8 S2->S3) | S2-p0 | Q7 | 0 | 12480 |
| s7(id=8 S2->S3) | sw08-p5 | Q7 | 4160 | 12480 |
| s7(id=8 S2->S3) | sw07-p4 | Q7 | 8320 | 12480 |
| s7(id=8 S2->S3) | sw05-p5 | Q7 | 12480 | 12480 |
| s7(id=8 S2->S3) | sw03-p4 | Q7 | 16640 | 12480 |
| s7(id=8 S2->S3) | sw01-p2 | Q7 | 20800 | 12480 |
| s8(id=9 S1->S3) | S1-p0 | Q6 | 74880 | 12480 |
| s8(id=9 S1->S3) | sw02-p4 | Q6 | 79040 | 12480 |
| s8(id=9 S1->S3) | sw04-p5 | Q6 | 83200 | 12480 |
| s8(id=9 S1->S3) | sw06-p4 | Q6 | 87360 | 12480 |
| s8(id=9 S1->S3) | sw08-p5 | Q6 | 91520 | 12480 |
| s8(id=9 S1->S3) | sw07-p4 | Q6 | 95680 | 12480 |
| s8(id=9 S1->S3) | sw05-p5 | Q6 | 99840 | 12480 |
| s8(id=9 S1->S3) | sw03-p4 | Q6 | 104000 | 12480 |
| s8(id=9 S1->S3) | sw01-p2 | Q6 | 108160 | 12480 |
| s9(id=10 S3->S2) | S3-p0 | Q6 | 49920 | 12480 |
| s9(id=10 S3->S2) | sw01-p4 | Q6 | 54080 | 12480 |
| s9(id=10 S3->S2) | sw03-p5 | Q6 | 58240 | 12480 |
| s9(id=10 S3->S2) | sw05-p4 | Q6 | 62400 | 12480 |
| s9(id=10 S3->S2) | sw07-p5 | Q6 | 66560 | 12480 |
| s9(id=10 S3->S2) | sw08-p2 | Q6 | 70720 | 12480 |
| s12(id=13 S1->S2) | S1-p0 | Q7 | 0 | 12480 |
| s12(id=13 S1->S2) | sw02-p4 | Q7 | 4160 | 12480 |
| s12(id=13 S1->S2) | sw04-p5 | Q7 | 8320 | 12480 |
| s12(id=13 S1->S2) | sw06-p4 | Q7 | 12480 | 12480 |
| s12(id=13 S1->S2) | sw08-p2 | Q7 | 16640 | 12480 |
| s13(id=14 S3->S2) | S3-p0 | Q7 | 0 | 12480 |
| s13(id=14 S3->S2) | sw01-p4 | Q7 | 4480 | 12480 |
| s13(id=14 S3->S2) | sw03-p5 | Q7 | 8640 | 12480 |
| s13(id=14 S3->S2) | sw05-p4 | Q7 | 12800 | 12480 |
| s13(id=14 S3->S2) | sw07-p5 | Q7 | 25280 | 12480 |
| s13(id=14 S3->S2) | sw08-p2 | Q7 | 29440 | 12480 |
| s17(id=18 S2->S1) | S2-p0 | Q7 | 74880 | 12480 |
| s17(id=18 S2->S1) | sw08-p4 | Q7 | 79040 | 12480 |
| s17(id=18 S2->S1) | sw06-p5 | Q7 | 83200 | 12480 |
| s17(id=18 S2->S1) | sw04-p4 | Q7 | 87360 | 12480 |
| s17(id=18 S2->S1) | sw02-p2 | Q7 | 91520 | 12480 |
| s18(id=19 S2->S3) | S2-p0 | Q6 | 49920 | 12480 |
| s18(id=19 S2->S3) | sw08-p5 | Q6 | 54720 | 12480 |
| s18(id=19 S2->S3) | sw07-p4 | Q6 | 58880 | 12480 |
| s18(id=19 S2->S3) | sw05-p5 | Q6 | 63040 | 12480 |
| s18(id=19 S2->S3) | sw03-p4 | Q6 | 67200 | 12480 |
| s18(id=19 S2->S3) | sw01-p2 | Q6 | 71360 | 12480 |
| s19(id=20 S1->S3) | S1-p0 | Q7 | 24960 | 12480 |
| s19(id=20 S1->S3) | sw02-p4 | Q7 | 29120 | 12480 |
| s19(id=20 S1->S3) | sw04-p5 | Q7 | 33600 | 12480 |
| s19(id=20 S1->S3) | sw06-p4 | Q7 | 37760 | 12480 |
| s19(id=20 S1->S3) | sw08-p5 | Q7 | 41920 | 12480 |
| s19(id=20 S1->S3) | sw07-p4 | Q7 | 46080 | 12480 |
| s19(id=20 S1->S3) | sw05-p5 | Q7 | 50240 | 12480 |
| s19(id=20 S1->S3) | sw03-p4 | Q7 | 54400 | 12480 |
| s19(id=20 S1->S3) | sw01-p2 | Q7 | 58560 | 12480 |

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

### sw01-p2  (29 entries, util 21.8400 %)

```
sgs 20800 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 11520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 100160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 149760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 136960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 128960 0x3F # 00111111   BE
```

### sw01-p4  (17 entries, util 12.4800 %)

```
sgs 4480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 137920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 137920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 183040 0x3F # 00111111   BE
```

### sw02-p2  (3 entries, util 1.5600 %)

```
sgs 91520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 696000 0x3F # 00111111   BE
```

### sw02-p4  (21 entries, util 15.6000 %)

```
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 112640 0x3F # 00111111   BE
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
sgs 158400 0x3F # 00111111   BE
```

### sw03-p4  (29 entries, util 21.8400 %)

```
sgs 16640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 11520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 100160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 149760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 136960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 133120 0x3F # 00111111   BE
```

### sw03-p5  (17 entries, util 12.4800 %)

```
sgs 8640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 137920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 137920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 178880 0x3F # 00111111   BE
```

### sw04-p4  (3 entries, util 1.5600 %)

```
sgs 87360 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 700160 0x3F # 00111111   BE
```

### sw04-p5  (21 entries, util 15.6000 %)

```
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 112640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 162240 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 162240 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 153920 0x3F # 00111111   BE
```

### sw05-p4  (17 entries, util 12.4800 %)

```
sgs 12800 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 137920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 137920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 174720 0x3F # 00111111   BE
```

### sw05-p5  (29 entries, util 21.8400 %)

```
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 11520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 100160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 149760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 136960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 137280 0x3F # 00111111   BE
```

### sw06-p4  (21 entries, util 15.6000 %)

```
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 112640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 162240 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 162240 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12800 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 149760 0x3F # 00111111   BE
```

### sw06-p5  (3 entries, util 1.5600 %)

```
sgs 83200 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 704320 0x3F # 00111111   BE
```

### sw07-p4  (29 entries, util 21.8400 %)

```
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 11520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 100160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 149760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 136960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 141440 0x3F # 00111111   BE
```

### sw07-p5  (17 entries, util 12.4800 %)

```
sgs 25280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 3840 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 146240 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 3840 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 146240 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 162240 0x3F # 00111111   BE
```

### sw08-p2  (25 entries, util 18.7200 %)

```
sgs 16640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 3840 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 133440 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 174720 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 3840 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 133440 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 158080 0x3F # 00111111   BE
```

### sw08-p4  (3 entries, util 1.5600 %)

```
sgs 79040 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 708480 0x3F # 00111111   BE
```

### sw08-p5  (29 entries, util 21.8400 %)

```
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 11520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 100160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 149760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 136960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 25280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 145600 0x3F # 00111111   BE
```

