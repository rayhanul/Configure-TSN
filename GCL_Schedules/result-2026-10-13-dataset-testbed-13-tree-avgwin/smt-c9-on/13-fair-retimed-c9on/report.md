# SMT-synthesized GCL schedule (Problem 1: feasible schedule synthesis)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- TT queues: Q6, Q7; best effort filler mask 0x3F
- **Retimed from `result/result-2026-10-13-dataset-testbed-13-tree-avgwin/smt-c9-off/13-t3600-c9off-minlat/schedule.json`**: flow set, routes, and release_offset pinned to exactly what that run admitted; only phi (window timing) is being re-solved here, under this run's own constraint set.
- Solver: Z3, maximize admitted flows (binary search), then minimize total latency, timeout 3600s
- Result: **sat**, admitted 11/11 (proven optimal), solved in 10.33s
- Total latency (sum of e2e over admitted flows): **540080 ns** (proven minimum)

## Flows

stream.csv does not specify a talker offset; `offset (ns) = phi` below is the transmit time of each flow's first frame, computed by the solver (also in `offsets.csv` and `schedule.json`'s `offset_ns`).

| flow | route | L (B) | C (ns) | T (ns) | D (ns) | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|---|---|---|---|
| s2(id=3 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | 400 | 12480 | 400000 | 400000 | 7 | 24960 | 74000 | yes |
| s4(id=5 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 500 | 12480 | 200000 | 200000 | 6 | 0 | 54160 | yes |
| s7(id=8 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 500 | 12480 | 800000 | 800000 | 7 | 62400 | 54160 | yes |
| s8(id=9 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 200 | 12480 | 400000 | 400000 | 6 | 37440 | 42960 | yes |
| s9(id=10 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | 300 | 12480 | 200000 | 200000 | 7 | 0 | 39440 | yes |
| s12(id=13 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | 500 | 12480 | 400000 | 400000 | 7 | 49920 | 45840 | yes |
| s13(id=14 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 200 | 12480 | 200000 | 200000 | 7 | 0 | 36880 | yes |
| s14(id=15 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | 100 | 12480 | 800000 | 800000 | 7 | 49920 | 61840 | yes |
| s16(id=17 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 100 | 12480 | 800000 | 800000 | 6 | 99840 | 38160 | yes |
| s18(id=19 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 200 | 12480 | 200000 | 200000 | 6 | 24960 | 42960 | yes |
| s19(id=20 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 300 | 12480 | 400000 | 400000 | 6 | 74880 | 49680 | yes |

## Per-hop windows

| flow | egress port | queue | psi (ns) | delta (ns) |
|---|---|---|---|---|
| s2(id=3 S1->S3) | S1-p0 | Q7 | 24960 | 12480 |
| s2(id=3 S1->S3) | sw02-p4 | Q7 | 32640 | 12480 |
| s2(id=3 S1->S3) | sw04-p5 | Q7 | 40320 | 12480 |
| s2(id=3 S1->S3) | sw06-p4 | Q7 | 48000 | 12480 |
| s2(id=3 S1->S3) | sw08-p5 | Q7 | 55680 | 12480 |
| s2(id=3 S1->S3) | sw07-p4 | Q7 | 63360 | 12480 |
| s2(id=3 S1->S3) | sw05-p5 | Q7 | 71040 | 12480 |
| s2(id=3 S1->S3) | sw03-p4 | Q7 | 78720 | 12480 |
| s2(id=3 S1->S3) | sw01-p2 | Q7 | 86400 | 12480 |
| s4(id=5 S3->S2) | S3-p0 | Q6 | 0 | 12480 |
| s4(id=5 S3->S2) | sw01-p4 | Q6 | 8320 | 12480 |
| s4(id=5 S3->S2) | sw03-p5 | Q6 | 16640 | 12480 |
| s4(id=5 S3->S2) | sw05-p4 | Q6 | 24960 | 12480 |
| s4(id=5 S3->S2) | sw07-p5 | Q6 | 33280 | 12480 |
| s4(id=5 S3->S2) | sw08-p2 | Q6 | 41600 | 12480 |
| s7(id=8 S3->S2) | S3-p0 | Q7 | 62400 | 12480 |
| s7(id=8 S3->S2) | sw01-p4 | Q7 | 70720 | 12480 |
| s7(id=8 S3->S2) | sw03-p5 | Q7 | 79040 | 12480 |
| s7(id=8 S3->S2) | sw05-p4 | Q7 | 87360 | 12480 |
| s7(id=8 S3->S2) | sw07-p5 | Q7 | 95680 | 12480 |
| s7(id=8 S3->S2) | sw08-p2 | Q7 | 104000 | 12480 |
| s8(id=9 S3->S2) | S3-p0 | Q6 | 37440 | 12480 |
| s8(id=9 S3->S2) | sw01-p4 | Q6 | 43520 | 12480 |
| s8(id=9 S3->S2) | sw03-p5 | Q6 | 49600 | 12480 |
| s8(id=9 S3->S2) | sw05-p4 | Q6 | 55680 | 12480 |
| s8(id=9 S3->S2) | sw07-p5 | Q6 | 61760 | 12480 |
| s8(id=9 S3->S2) | sw08-p2 | Q6 | 67840 | 12480 |
| s9(id=10 S2->S1) | S2-p0 | Q7 | 0 | 12480 |
| s9(id=10 S2->S1) | sw08-p4 | Q7 | 6720 | 12480 |
| s9(id=10 S2->S1) | sw06-p5 | Q7 | 13440 | 12480 |
| s9(id=10 S2->S1) | sw04-p4 | Q7 | 20160 | 12480 |
| s9(id=10 S2->S1) | sw02-p2 | Q7 | 26880 | 12480 |
| s12(id=13 S2->S1) | S2-p0 | Q7 | 49920 | 12480 |
| s12(id=13 S2->S1) | sw08-p4 | Q7 | 58240 | 12480 |
| s12(id=13 S2->S1) | sw06-p5 | Q7 | 66560 | 12480 |
| s12(id=13 S2->S1) | sw04-p4 | Q7 | 74880 | 12480 |
| s12(id=13 S2->S1) | sw02-p2 | Q7 | 83200 | 12480 |
| s13(id=14 S1->S2) | S1-p0 | Q7 | 0 | 12480 |
| s13(id=14 S1->S2) | sw02-p4 | Q7 | 6080 | 12480 |
| s13(id=14 S1->S2) | sw04-p5 | Q7 | 12160 | 12480 |
| s13(id=14 S1->S2) | sw06-p4 | Q7 | 18240 | 12480 |
| s13(id=14 S1->S2) | sw08-p2 | Q7 | 24320 | 12480 |
| s14(id=15 S1->S3) | S1-p0 | Q7 | 49920 | 12480 |
| s14(id=15 S1->S3) | sw02-p4 | Q7 | 56960 | 12480 |
| s14(id=15 S1->S3) | sw04-p5 | Q7 | 62080 | 12480 |
| s14(id=15 S1->S3) | sw06-p4 | Q7 | 67200 | 12480 |
| s14(id=15 S1->S3) | sw08-p5 | Q7 | 72320 | 12480 |
| s14(id=15 S1->S3) | sw07-p4 | Q7 | 78720 | 12480 |
| s14(id=15 S1->S3) | sw05-p5 | Q7 | 83840 | 12480 |
| s14(id=15 S1->S3) | sw03-p4 | Q7 | 91520 | 12480 |
| s14(id=15 S1->S3) | sw01-p2 | Q7 | 99200 | 12480 |
| s16(id=17 S2->S3) | S2-p0 | Q6 | 99840 | 12480 |
| s16(id=17 S2->S3) | sw08-p5 | Q6 | 104960 | 12480 |
| s16(id=17 S2->S3) | sw07-p4 | Q6 | 110080 | 12480 |
| s16(id=17 S2->S3) | sw05-p5 | Q6 | 115200 | 12480 |
| s16(id=17 S2->S3) | sw03-p4 | Q6 | 120320 | 12480 |
| s16(id=17 S2->S3) | sw01-p2 | Q6 | 125440 | 12480 |
| s18(id=19 S2->S3) | S2-p0 | Q6 | 24960 | 12480 |
| s18(id=19 S2->S3) | sw08-p5 | Q6 | 31040 | 12480 |
| s18(id=19 S2->S3) | sw07-p4 | Q6 | 37120 | 12480 |
| s18(id=19 S2->S3) | sw05-p5 | Q6 | 43200 | 12480 |
| s18(id=19 S2->S3) | sw03-p4 | Q6 | 49280 | 12480 |
| s18(id=19 S2->S3) | sw01-p2 | Q6 | 55360 | 12480 |
| s19(id=20 S2->S3) | S2-p0 | Q6 | 74880 | 12480 |
| s19(id=20 S2->S3) | sw08-p5 | Q6 | 85120 | 12480 |
| s19(id=20 S2->S3) | sw07-p4 | Q6 | 91840 | 12480 |
| s19(id=20 S2->S3) | sw05-p5 | Q6 | 98560 | 12480 |
| s19(id=20 S2->S3) | sw03-p4 | Q6 | 105280 | 12480 |
| s19(id=20 S2->S3) | sw01-p2 | Q6 | 112000 | 12480 |

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

### sw01-p2  (21 entries, util 15.6000 %)

```
sgs 55360 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 18560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 960 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 117440 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 18560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 130880 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 132160 0x3F # 00111111   BE
```

### sw01-p4  (15 entries, util 10.9200 %)

```
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 22720 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 14720 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 125120 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 22720 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 152320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 179200 0x3F # 00111111   BE
```

### sw02-p2  (13 entries, util 9.3600 %)

```
sgs 26880 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 43840 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 131200 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 43840 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 131200 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 160640 0x3F # 00111111   BE
```

### sw02-p4  (15 entries, util 10.9200 %)

```
sgs 6080 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 14080 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 11840 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 136640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 14080 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 160960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 181440 0x3F # 00111111   BE
```

### sw03-p4  (21 entries, util 15.6000 %)

```
sgs 49280 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 16960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 1280 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 2560 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 116480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 16960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 14080 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 131520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 138240 0x3F # 00111111   BE
```

### sw03-p5  (15 entries, util 10.9200 %)

```
sgs 16640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 20480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 16960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 125120 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 20480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 154560 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 170880 0x3F # 00111111   BE
```

### sw04-p4  (13 entries, util 9.3600 %)

```
sgs 20160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 42240 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 132800 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 42240 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 132800 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 167360 0x3F # 00111111   BE
```

### sw04-p5  (15 entries, util 10.9200 %)

```
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 15680 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 9280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 137600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 15680 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 159360 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 175360 0x3F # 00111111   BE
```

### sw05-p4  (15 entries, util 10.9200 %)

```
sgs 24960 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 18240 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 19200 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 125120 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 18240 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 156800 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 162560 0x3F # 00111111   BE
```

### sw05-p5  (21 entries, util 15.6000 %)

```
sgs 43200 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 15360 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 2240 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 115520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 15360 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 15040 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 132160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 144320 0x3F # 00111111   BE
```

### sw06-p4  (15 entries, util 10.9200 %)

```
sgs 18240 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 17280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 6720 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 138560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 17280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 157760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 169280 0x3F # 00111111   BE
```

### sw06-p5  (13 entries, util 9.3600 %)

```
sgs 13440 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 40640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 134400 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 40640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 134400 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 174080 0x3F # 00111111   BE
```

### sw07-p4  (21 entries, util 15.6000 %)

```
sgs 37120 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 13760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 2880 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 114560 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 13760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 16000 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 132800 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 150400 0x3F # 00111111   BE
```

### sw07-p5  (15 entries, util 10.9200 %)

```
sgs 33280 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 16000 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 21440 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 125120 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 16000 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 159040 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 154240 0x3F # 00111111   BE
```

### sw08-p2  (23 entries, util 17.1600 %)

```
sgs 24320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 4800 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 13760 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 23680 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 107840 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 4800 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 170240 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 4800 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 13760 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 144000 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 4800 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 145920 0x3F # 00111111   BE
```

### sw08-p4  (13 entries, util 9.3600 %)

```
sgs 6720 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 39040 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 136000 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 39040 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 136000 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 180800 0x3F # 00111111   BE
```

### sw08-p5  (21 entries, util 15.6000 %)

```
sgs 31040 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 7360 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 113600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 16960 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 133440 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 156480 0x3F # 00111111   BE
```

