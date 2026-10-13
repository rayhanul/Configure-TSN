# SMT-synthesized GCL schedule (Problem 1: feasible schedule synthesis)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- TT queues: Q6, Q7; best effort filler mask 0x3F
- **Retimed from `result/result-2026-10-12-dataset-testbed-8-ring-avgwin/smt-c9-off/8-t3600-c9off-minlat/schedule.json`**: flow set, routes, and release_offset pinned to exactly what that run admitted; only phi (window timing) is being re-solved here, under this run's own constraint set.
- Solver: Z3, maximize admitted flows (binary search), then minimize total latency, timeout 3600s
- Result: **sat**, admitted 10/10 (proven optimal), solved in 3.08s
- Total latency (sum of e2e over admitted flows): **346080 ns** (proven minimum)

## Flows

stream.csv does not specify a talker offset; `offset (ns) = phi` below is the transmit time of each flow's first frame, computed by the solver (also in `offsets.csv` and `schedule.json`'s `offset_ns`).

| flow | route | L (B) | C (ns) | T (ns) | D (ns) | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|---|---|---|---|
| s1(id=2 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | 100 | 12480 | 400000 | 400000 | 7 | 37440 | 40720 | yes |
| s4(id=5 S1->S3) | S1->sw02->sw01->S3 | 100 | 12480 | 800000 | 800000 | 6 | 87360 | 22800 | yes |
| s5(id=6 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 100 | 12480 | 200000 | 200000 | 7 | 0 | 48080 | yes |
| s8(id=9 S3->S1) | S3->sw01->sw02->S1 | 100 | 12480 | 400000 | 400000 | 6 | 12480 | 22800 | yes |
| s9(id=10 S1->S3) | S1->sw02->sw01->S3 | 100 | 12480 | 200000 | 200000 | 6 | 12480 | 22800 | yes |
| s11(id=12 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 500 | 12480 | 800000 | 800000 | 6 | 62400 | 60560 | yes |
| s12(id=13 S3->S1) | S3->sw01->sw02->S1 | 200 | 12480 | 800000 | 800000 | 7 | 62400 | 28560 | yes |
| s17(id=18 S3->S1) | S3->sw01->sw02->S1 | 400 | 12480 | 400000 | 400000 | 6 | 37440 | 27920 | yes |
| s18(id=19 S1->S3) | S1->sw02->sw01->S3 | 300 | 12480 | 400000 | 400000 | 7 | 62400 | 26000 | yes |
| s19(id=20 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 500 | 12480 | 200000 | 200000 | 7 | 37440 | 45840 | yes |

## Per-hop windows

| flow | egress port | queue | psi (ns) | delta (ns) |
|---|---|---|---|---|
| s1(id=2 S2->S1) | S2-p0 | Q7 | 37440 | 12480 |
| s1(id=2 S2->S1) | sw08-p4 | Q7 | 42560 | 12480 |
| s1(id=2 S2->S1) | sw06-p5 | Q7 | 55360 | 12480 |
| s1(id=2 S2->S1) | sw04-p4 | Q7 | 60480 | 12480 |
| s1(id=2 S2->S1) | sw02-p2 | Q7 | 65600 | 12480 |
| s4(id=5 S1->S3) | S1-p0 | Q6 | 87360 | 12480 |
| s4(id=5 S1->S3) | sw02-p5 | Q6 | 92480 | 12480 |
| s4(id=5 S1->S3) | sw01-p2 | Q6 | 97600 | 12480 |
| s5(id=6 S2->S3) | S2-p0 | Q7 | 0 | 12480 |
| s5(id=6 S2->S3) | sw08-p5 | Q7 | 5120 | 12480 |
| s5(id=6 S2->S3) | sw07-p4 | Q7 | 20160 | 12480 |
| s5(id=6 S2->S3) | sw05-p5 | Q7 | 25280 | 12480 |
| s5(id=6 S2->S3) | sw03-p4 | Q7 | 30400 | 12480 |
| s5(id=6 S2->S3) | sw01-p2 | Q7 | 35520 | 12480 |
| s8(id=9 S3->S1) | S3-p0 | Q6 | 12480 | 12480 |
| s8(id=9 S3->S1) | sw01-p5 | Q6 | 17600 | 12480 |
| s8(id=9 S3->S1) | sw02-p2 | Q6 | 22720 | 12480 |
| s9(id=10 S1->S3) | S1-p0 | Q6 | 12480 | 12480 |
| s9(id=10 S1->S3) | sw02-p5 | Q6 | 17600 | 12480 |
| s9(id=10 S1->S3) | sw01-p2 | Q6 | 22720 | 12480 |
| s11(id=12 S2->S3) | S2-p0 | Q6 | 62400 | 12480 |
| s11(id=12 S2->S3) | sw08-p5 | Q6 | 70720 | 12480 |
| s11(id=12 S2->S3) | sw07-p4 | Q6 | 79040 | 12480 |
| s11(id=12 S2->S3) | sw05-p5 | Q6 | 87360 | 12480 |
| s11(id=12 S2->S3) | sw03-p4 | Q6 | 95680 | 12480 |
| s11(id=12 S2->S3) | sw01-p2 | Q6 | 110400 | 12480 |
| s12(id=13 S3->S1) | S3-p0 | Q7 | 62400 | 12480 |
| s12(id=13 S3->S1) | sw01-p5 | Q7 | 68480 | 12480 |
| s12(id=13 S3->S1) | sw02-p2 | Q7 | 78400 | 12480 |
| s17(id=18 S3->S1) | S3-p0 | Q6 | 37440 | 12480 |
| s17(id=18 S3->S1) | sw01-p5 | Q6 | 45120 | 12480 |
| s17(id=18 S3->S1) | sw02-p2 | Q6 | 52800 | 12480 |
| s18(id=19 S1->S3) | S1-p0 | Q7 | 62400 | 12480 |
| s18(id=19 S1->S3) | sw02-p5 | Q7 | 69120 | 12480 |
| s18(id=19 S1->S3) | sw01-p2 | Q7 | 75840 | 12480 |
| s19(id=20 S1->S2) | S1-p0 | Q7 | 37440 | 12480 |
| s19(id=20 S1->S2) | sw02-p4 | Q7 | 45760 | 12480 |
| s19(id=20 S1->S2) | sw04-p5 | Q7 | 54080 | 12480 |
| s19(id=20 S1->S2) | sw06-p4 | Q7 | 62400 | 12480 |
| s19(id=20 S1->S2) | sw08-p2 | Q7 | 70720 | 12480 |

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
sgs 22720 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 27840 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 9280 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 99840 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 174720 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 27840 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 134400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 152000 0x3F # 00111111   BE
```

### sw01-p5  (11 entries, util 7.8000 %)

```
sgs 17600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 15040 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 10880 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 336640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 15040 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 342400 0x3F # 00111111   BE
```

### sw02-p2  (15 entries, util 10.9200 %)

```
sgs 22720 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 17600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 331840 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 17600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 321920 0x3F # 00111111   BE
```

### sw02-p4  (9 entries, util 6.2400 %)

```
sgs 45760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 141760 0x3F # 00111111   BE
```

### sw02-p5  (15 entries, util 10.9200 %)

```
sgs 17600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 39040 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 10880 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 112640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 39040 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 136000 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 169920 0x3F # 00111111   BE
```

### sw03-p4  (11 entries, util 7.8000 %)

```
sgs 30400 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 52800 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 122240 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 157120 0x3F # 00111111   BE
```

### sw04-p4  (5 entries, util 3.1200 %)

```
sgs 60480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 387520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 327040 0x3F # 00111111   BE
```

### sw04-p5  (9 entries, util 6.2400 %)

```
sgs 54080 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 133440 0x3F # 00111111   BE
```

### sw05-p5  (11 entries, util 7.8000 %)

```
sgs 25280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 49600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 125440 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 162240 0x3F # 00111111   BE
```

### sw06-p4  (9 entries, util 6.2400 %)

```
sgs 62400 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 125120 0x3F # 00111111   BE
```

### sw06-p5  (5 entries, util 3.1200 %)

```
sgs 55360 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 387520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 332160 0x3F # 00111111   BE
```

### sw07-p4  (11 entries, util 7.8000 %)

```
sgs 20160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 46400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 128640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 167360 0x3F # 00111111   BE
```

### sw08-p2  (9 entries, util 6.2400 %)

```
sgs 70720 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 116800 0x3F # 00111111   BE
```

### sw08-p4  (5 entries, util 3.1200 %)

```
sgs 42560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 387520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 344960 0x3F # 00111111   BE
```

### sw08-p5  (11 entries, util 7.8000 %)

```
sgs 5120 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 53120 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 121920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 182400 0x3F # 00111111   BE
```

Ports carrying no TT traffic (single best-effort entry for the whole cycle): sw01-p4, sw03-p5, sw05-p4, sw07-p5

