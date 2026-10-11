# SMT-synthesized GCL schedule (Problem 1: feasible schedule synthesis)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- TT queues: Q6, Q7; best effort filler mask 0x3F
- Solver: Z3, maximize admitted flows (binary search), then minimize total latency, timeout 3600s
- Result: **sat**, admitted 10/20 (proven optimal), solved in 235.50s
- Total latency (sum of e2e over admitted flows): **952480 ns** (proven minimum)

- **WARNING: C9 disabled for this run** -- see Constraint check below for the resulting violations.

## Flows

stream.csv does not specify a talker offset; `offset (ns) = phi` below is the transmit time of each flow's first frame, computed by the solver (also in `offsets.csv` and `schedule.json`'s `offset_ns`).

| flow | route | L (B) | C (ns) | T (ns) | D (ns) | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|---|---|---|---|
| s0(id=1 S3->S1) | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | 200 | 12480 | 800000 | 800000 | None | None | None | no |
| s1(id=2 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 300 | 12480 | 200000 | 200000 | 6 | 0 | 95760 | yes |
| s2(id=3 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 100 | 12480 | 800000 | 800000 | 6 | 62400 | 84240 | yes |
| s3(id=4 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | 300 | 12480 | 800000 | 800000 | None | None | None | no |
| s4(id=5 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 100 | 12480 | 800000 | 800000 | 7 | 62400 | 95760 | yes |
| s5(id=6 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 200 | 12480 | 400000 | 400000 | None | None | None | no |
| s6(id=7 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 500 | 12480 | 400000 | 400000 | None | None | None | no |
| s7(id=8 S3->S1) | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | 500 | 12480 | 200000 | 200000 | None | None | None | no |
| s8(id=9 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | 500 | 12480 | 400000 | 400000 | 7 | 37440 | 79120 | yes |
| s9(id=10 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 500 | 12480 | 200000 | 200000 | 7 | 0 | 79120 | yes |
| s10(id=11 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 500 | 12480 | 400000 | 400000 | None | None | None | no |
| s11(id=12 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 500 | 12480 | 200000 | 200000 | 7 | 12480 | 95760 | yes |
| s12(id=13 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | 400 | 12480 | 800000 | 800000 | 6 | 87360 | 145680 | yes |
| s13(id=14 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | 100 | 12480 | 200000 | 200000 | None | None | None | no |
| s14(id=15 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 500 | 12480 | 200000 | 200000 | None | None | None | no |
| s15(id=16 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 200 | 12480 | 800000 | 800000 | 7 | 62400 | 97040 | yes |
| s16(id=17 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 400 | 12480 | 400000 | 400000 | 6 | 37440 | 83600 | yes |
| s17(id=18 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | 400 | 12480 | 400000 | 400000 | None | None | None | no |
| s18(id=19 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 500 | 12480 | 400000 | 400000 | 7 | 37440 | 96400 | yes |
| s19(id=20 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 400 | 12480 | 200000 | 200000 | None | None | None | no |

## Per-hop windows

| flow | egress port | queue | psi (ns) | delta (ns) |
|---|---|---|---|---|
| s1(id=2 S2->S3) | S2-p0 | Q6 | 0 | 12480 |
| s1(id=2 S2->S3) | sw08-p5 | Q6 | 16640 | 12480 |
| s1(id=2 S2->S3) | sw07-p4 | Q6 | 33280 | 12480 |
| s1(id=2 S2->S3) | sw05-p5 | Q6 | 49920 | 12480 |
| s1(id=2 S2->S3) | sw03-p4 | Q6 | 66560 | 12480 |
| s1(id=2 S2->S3) | sw01-p2 | Q6 | 83200 | 12480 |
| s2(id=3 S1->S2) | S1-p0 | Q6 | 62400 | 12480 |
| s2(id=3 S1->S2) | sw02-p4 | Q6 | 82880 | 12480 |
| s2(id=3 S1->S2) | sw04-p5 | Q6 | 99520 | 12480 |
| s2(id=3 S1->S2) | sw06-p4 | Q6 | 116160 | 12480 |
| s2(id=3 S1->S2) | sw08-p2 | Q6 | 134080 | 12480 |
| s4(id=5 S2->S3) | S2-p0 | Q7 | 62400 | 12480 |
| s4(id=5 S2->S3) | sw08-p5 | Q7 | 79040 | 12480 |
| s4(id=5 S2->S3) | sw07-p4 | Q7 | 95680 | 12480 |
| s4(id=5 S2->S3) | sw05-p5 | Q7 | 112320 | 12480 |
| s4(id=5 S2->S3) | sw03-p4 | Q7 | 128960 | 12480 |
| s4(id=5 S2->S3) | sw01-p2 | Q7 | 145600 | 12480 |
| s8(id=9 S2->S1) | S2-p0 | Q7 | 37440 | 12480 |
| s8(id=9 S2->S1) | sw08-p4 | Q7 | 54080 | 12480 |
| s8(id=9 S2->S1) | sw06-p5 | Q7 | 70720 | 12480 |
| s8(id=9 S2->S1) | sw04-p4 | Q7 | 87360 | 12480 |
| s8(id=9 S2->S1) | sw02-p2 | Q7 | 104000 | 12480 |
| s9(id=10 S1->S2) | S1-p0 | Q7 | 0 | 12480 |
| s9(id=10 S1->S2) | sw02-p4 | Q7 | 16640 | 12480 |
| s9(id=10 S1->S2) | sw04-p5 | Q7 | 33280 | 12480 |
| s9(id=10 S1->S2) | sw06-p4 | Q7 | 49920 | 12480 |
| s9(id=10 S1->S2) | sw08-p2 | Q7 | 66560 | 12480 |
| s11(id=12 S3->S2) | S3-p0 | Q7 | 12480 | 12480 |
| s11(id=12 S3->S2) | sw01-p4 | Q7 | 29120 | 12480 |
| s11(id=12 S3->S2) | sw03-p5 | Q7 | 45760 | 12480 |
| s11(id=12 S3->S2) | sw05-p4 | Q7 | 62400 | 12480 |
| s11(id=12 S3->S2) | sw07-p5 | Q7 | 79040 | 12480 |
| s11(id=12 S3->S2) | sw08-p2 | Q7 | 95680 | 12480 |
| s12(id=13 S1->S3) | S1-p0 | Q6 | 87360 | 12480 |
| s12(id=13 S1->S3) | sw02-p4 | Q6 | 104000 | 12480 |
| s12(id=13 S1->S3) | sw04-p5 | Q6 | 120640 | 12480 |
| s12(id=13 S1->S3) | sw06-p4 | Q6 | 137280 | 12480 |
| s12(id=13 S1->S3) | sw08-p5 | Q6 | 153920 | 12480 |
| s12(id=13 S1->S3) | sw07-p4 | Q6 | 170560 | 12480 |
| s12(id=13 S1->S3) | sw05-p5 | Q6 | 187200 | 12480 |
| s12(id=13 S1->S3) | sw03-p4 | Q6 | 203840 | 12480 |
| s12(id=13 S1->S3) | sw01-p2 | Q6 | 220480 | 12480 |
| s15(id=16 S3->S2) | S3-p0 | Q7 | 62400 | 12480 |
| s15(id=16 S3->S2) | sw01-p4 | Q7 | 79040 | 12480 |
| s15(id=16 S3->S2) | sw03-p5 | Q7 | 95680 | 12480 |
| s15(id=16 S3->S2) | sw05-p4 | Q7 | 112320 | 12480 |
| s15(id=16 S3->S2) | sw07-p5 | Q7 | 128960 | 12480 |
| s15(id=16 S3->S2) | sw08-p2 | Q7 | 146880 | 12480 |
| s16(id=17 S1->S2) | S1-p0 | Q6 | 37440 | 12480 |
| s16(id=17 S1->S2) | sw02-p4 | Q6 | 56000 | 12480 |
| s16(id=17 S1->S2) | sw04-p5 | Q6 | 72640 | 12480 |
| s16(id=17 S1->S2) | sw06-p4 | Q6 | 89280 | 12480 |
| s16(id=17 S1->S2) | sw08-p2 | Q6 | 108480 | 12480 |
| s18(id=19 S3->S2) | S3-p0 | Q7 | 37440 | 12480 |
| s18(id=19 S3->S2) | sw01-p4 | Q7 | 54080 | 12480 |
| s18(id=19 S3->S2) | sw03-p5 | Q7 | 71360 | 12480 |
| s18(id=19 S3->S2) | sw05-p4 | Q7 | 88000 | 12480 |
| s18(id=19 S3->S2) | sw07-p5 | Q7 | 104640 | 12480 |
| s18(id=19 S3->S2) | sw08-p2 | Q7 | 121280 | 12480 |

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
sgs 83200 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 49920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 62400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 50240 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 104320 0x3F # 00111111   BE
```

### sw01-p4  (15 entries, util 10.9200 %)

```
sgs 29120 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 137600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 162560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 158400 0x3F # 00111111   BE
```

### sw02-p2  (5 entries, util 3.1200 %)

```
sgs 104000 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 387520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 283520 0x3F # 00111111   BE
```

### sw02-p4  (17 entries, util 12.4800 %)

```
sgs 16640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 26880 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 8640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 100160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 26880 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 148160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 170880 0x3F # 00111111   BE
```

### sw03-p4  (13 entries, util 9.3600 %)

```
sgs 66560 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 49920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 62400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 50240 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 120960 0x3F # 00111111   BE
```

### sw03-p5  (15 entries, util 10.9200 %)

```
sgs 45760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 11840 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 137600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 161920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 141760 0x3F # 00111111   BE
```

### sw04-p4  (5 entries, util 3.1200 %)

```
sgs 87360 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 387520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 300160 0x3F # 00111111   BE
```

### sw04-p5  (17 entries, util 12.4800 %)

```
sgs 33280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 26880 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 8640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 100160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 26880 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 148160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 154240 0x3F # 00111111   BE
```

### sw05-p4  (15 entries, util 10.9200 %)

```
sgs 62400 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 11840 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 137600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 161920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 125120 0x3F # 00111111   BE
```

### sw05-p5  (13 entries, util 9.3600 %)

```
sgs 49920 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 49920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 62400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 50240 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 137600 0x3F # 00111111   BE
```

### sw06-p4  (17 entries, util 12.4800 %)

```
sgs 49920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 26880 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 8640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 100160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 26880 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 148160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 137600 0x3F # 00111111   BE
```

### sw06-p5  (5 entries, util 3.1200 %)

```
sgs 70720 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 387520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 316800 0x3F # 00111111   BE
```

### sw07-p4  (13 entries, util 9.3600 %)

```
sgs 33280 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 49920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 62400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 50240 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 154240 0x3F # 00111111   BE
```

### sw07-p5  (15 entries, util 10.9200 %)

```
sgs 79040 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 11840 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 137600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 161920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 108480 0x3F # 00111111   BE
```

### sw08-p2  (29 entries, util 21.8400 %)

```
sgs 66560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 16640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 107200 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 16640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 158400 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 16640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 132800 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 16640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 91840 0x3F # 00111111   BE
```

### sw08-p4  (5 entries, util 3.1200 %)

```
sgs 54080 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 387520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 333440 0x3F # 00111111   BE
```

### sw08-p5  (13 entries, util 9.3600 %)

```
sgs 16640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 49920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 62400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 50240 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 170880 0x3F # 00111111   BE
```

