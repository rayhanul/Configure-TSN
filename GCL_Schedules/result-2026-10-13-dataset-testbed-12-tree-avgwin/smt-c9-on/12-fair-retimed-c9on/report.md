# SMT-synthesized GCL schedule (Problem 1: feasible schedule synthesis)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- TT queues: Q6, Q7; best effort filler mask 0x3F
- **Retimed from `result/result-2026-10-13-dataset-testbed-12-tree-avgwin/smt-c9-off/12-t3600-c9off-minlat/schedule.json`**: flow set, routes, and release_offset pinned to exactly what that run admitted; only phi (window timing) is being re-solved here, under this run's own constraint set.
- Solver: Z3, maximize admitted flows (binary search), then minimize total latency, timeout 3600s
- Result: **sat**, admitted 11/11 (proven optimal), solved in 14.37s
- Total latency (sum of e2e over admitted flows): **600880 ns** (proven minimum)

## Flows

stream.csv does not specify a talker offset; `offset (ns) = phi` below is the transmit time of each flow's first frame, computed by the solver (also in `offsets.csv` and `schedule.json`'s `offset_ns`).

| flow | route | L (B) | C (ns) | T (ns) | D (ns) | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|---|---|---|---|
| s1(id=2 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 400 | 12480 | 200000 | 200000 | 6 | 0 | 50960 | yes |
| s3(id=4 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | 300 | 12480 | 800000 | 800000 | 6 | 74880 | 66320 | yes |
| s4(id=5 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 100 | 12480 | 200000 | 200000 | 7 | 0 | 38160 | yes |
| s6(id=7 S3->S1) | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | 500 | 12480 | 800000 | 800000 | 6 | 49920 | 79120 | yes |
| s7(id=8 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | 300 | 12480 | 200000 | 200000 | 7 | 0 | 39440 | yes |
| s8(id=9 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 200 | 12480 | 400000 | 400000 | 6 | 24960 | 42960 | yes |
| s10(id=11 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | 300 | 12480 | 800000 | 800000 | 7 | 37440 | 39440 | yes |
| s11(id=12 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | 500 | 12480 | 200000 | 200000 | 6 | 24960 | 79120 | yes |
| s13(id=14 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 200 | 12480 | 400000 | 400000 | 7 | 49920 | 36880 | yes |
| s17(id=18 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 300 | 12480 | 800000 | 800000 | 6 | 62400 | 54480 | yes |
| s18(id=19 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | 400 | 12480 | 800000 | 800000 | 6 | 99840 | 74000 | yes |

## Per-hop windows

| flow | egress port | queue | psi (ns) | delta (ns) |
|---|---|---|---|---|
| s1(id=2 S1->S2) | S1-p0 | Q6 | 0 | 12480 |
| s1(id=2 S1->S2) | sw02-p4 | Q6 | 7680 | 12480 |
| s1(id=2 S1->S2) | sw04-p5 | Q6 | 15360 | 12480 |
| s1(id=2 S1->S2) | sw06-p4 | Q6 | 23040 | 12480 |
| s1(id=2 S1->S2) | sw08-p2 | Q6 | 38400 | 12480 |
| s3(id=4 S1->S3) | S1-p0 | Q6 | 74880 | 12480 |
| s3(id=4 S1->S3) | sw02-p4 | Q6 | 81600 | 12480 |
| s3(id=4 S1->S3) | sw04-p5 | Q6 | 88320 | 12480 |
| s3(id=4 S1->S3) | sw06-p4 | Q6 | 95040 | 12480 |
| s3(id=4 S1->S3) | sw08-p5 | Q6 | 101760 | 12480 |
| s3(id=4 S1->S3) | sw07-p4 | Q6 | 108480 | 12480 |
| s3(id=4 S1->S3) | sw05-p5 | Q6 | 115200 | 12480 |
| s3(id=4 S1->S3) | sw03-p4 | Q6 | 121920 | 12480 |
| s3(id=4 S1->S3) | sw01-p2 | Q6 | 128640 | 12480 |
| s4(id=5 S3->S2) | S3-p0 | Q7 | 0 | 12480 |
| s4(id=5 S3->S2) | sw01-p4 | Q7 | 5120 | 12480 |
| s4(id=5 S3->S2) | sw03-p5 | Q7 | 10240 | 12480 |
| s4(id=5 S3->S2) | sw05-p4 | Q7 | 15360 | 12480 |
| s4(id=5 S3->S2) | sw07-p5 | Q7 | 20480 | 12480 |
| s4(id=5 S3->S2) | sw08-p2 | Q7 | 25600 | 12480 |
| s6(id=7 S3->S1) | S3-p0 | Q6 | 49920 | 12480 |
| s6(id=7 S3->S1) | sw01-p4 | Q6 | 58240 | 12480 |
| s6(id=7 S3->S1) | sw03-p5 | Q6 | 66560 | 12480 |
| s6(id=7 S3->S1) | sw05-p4 | Q6 | 74880 | 12480 |
| s6(id=7 S3->S1) | sw07-p5 | Q6 | 83200 | 12480 |
| s6(id=7 S3->S1) | sw08-p4 | Q6 | 91520 | 12480 |
| s6(id=7 S3->S1) | sw06-p5 | Q6 | 99840 | 12480 |
| s6(id=7 S3->S1) | sw04-p4 | Q6 | 108160 | 12480 |
| s6(id=7 S3->S1) | sw02-p2 | Q6 | 116480 | 12480 |
| s7(id=8 S2->S1) | S2-p0 | Q7 | 0 | 12480 |
| s7(id=8 S2->S1) | sw08-p4 | Q7 | 6720 | 12480 |
| s7(id=8 S2->S1) | sw06-p5 | Q7 | 13440 | 12480 |
| s7(id=8 S2->S1) | sw04-p4 | Q7 | 20160 | 12480 |
| s7(id=8 S2->S1) | sw02-p2 | Q7 | 26880 | 12480 |
| s8(id=9 S3->S2) | S3-p0 | Q6 | 24960 | 12480 |
| s8(id=9 S3->S2) | sw01-p4 | Q6 | 31040 | 12480 |
| s8(id=9 S3->S2) | sw03-p5 | Q6 | 37120 | 12480 |
| s8(id=9 S3->S2) | sw05-p4 | Q6 | 43200 | 12480 |
| s8(id=9 S3->S2) | sw07-p5 | Q6 | 49280 | 12480 |
| s8(id=9 S3->S2) | sw08-p2 | Q6 | 55360 | 12480 |
| s10(id=11 S2->S1) | S2-p0 | Q7 | 37440 | 12480 |
| s10(id=11 S2->S1) | sw08-p4 | Q7 | 44160 | 12480 |
| s10(id=11 S2->S1) | sw06-p5 | Q7 | 50880 | 12480 |
| s10(id=11 S2->S1) | sw04-p4 | Q7 | 57600 | 12480 |
| s10(id=11 S2->S1) | sw02-p2 | Q7 | 64320 | 12480 |
| s11(id=12 S1->S3) | S1-p0 | Q6 | 24960 | 12480 |
| s11(id=12 S1->S3) | sw02-p4 | Q6 | 33280 | 12480 |
| s11(id=12 S1->S3) | sw04-p5 | Q6 | 41600 | 12480 |
| s11(id=12 S1->S3) | sw06-p4 | Q6 | 49920 | 12480 |
| s11(id=12 S1->S3) | sw08-p5 | Q6 | 58240 | 12480 |
| s11(id=12 S1->S3) | sw07-p4 | Q6 | 66560 | 12480 |
| s11(id=12 S1->S3) | sw05-p5 | Q6 | 74880 | 12480 |
| s11(id=12 S1->S3) | sw03-p4 | Q6 | 83200 | 12480 |
| s11(id=12 S1->S3) | sw01-p2 | Q6 | 91520 | 12480 |
| s13(id=14 S1->S2) | S1-p0 | Q7 | 49920 | 12480 |
| s13(id=14 S1->S2) | sw02-p4 | Q7 | 56000 | 12480 |
| s13(id=14 S1->S2) | sw04-p5 | Q7 | 62080 | 12480 |
| s13(id=14 S1->S2) | sw06-p4 | Q7 | 68160 | 12480 |
| s13(id=14 S1->S2) | sw08-p2 | Q7 | 74240 | 12480 |
| s17(id=18 S2->S3) | S2-p0 | Q6 | 62400 | 12480 |
| s17(id=18 S2->S3) | sw08-p5 | Q6 | 71040 | 12480 |
| s17(id=18 S2->S3) | sw07-p4 | Q6 | 79360 | 12480 |
| s17(id=18 S2->S3) | sw05-p5 | Q6 | 87680 | 12480 |
| s17(id=18 S2->S3) | sw03-p4 | Q6 | 96000 | 12480 |
| s17(id=18 S2->S3) | sw01-p2 | Q6 | 104320 | 12480 |
| s18(id=19 S1->S3) | S1-p0 | Q6 | 99840 | 12480 |
| s18(id=19 S1->S3) | sw02-p4 | Q6 | 107520 | 12480 |
| s18(id=19 S1->S3) | sw04-p5 | Q6 | 115200 | 12480 |
| s18(id=19 S1->S3) | sw06-p4 | Q6 | 122880 | 12480 |
| s18(id=19 S1->S3) | sw08-p5 | Q6 | 130560 | 12480 |
| s18(id=19 S1->S3) | sw07-p4 | Q6 | 138240 | 12480 |
| s18(id=19 S1->S3) | sw05-p5 | Q6 | 145920 | 12480 |
| s18(id=19 S1->S3) | sw03-p4 | Q6 | 153600 | 12480 |
| s18(id=19 S1->S3) | sw01-p2 | Q6 | 161280 | 12480 |

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

### sw01-p2  (15 entries, util 10.9200 %)

```
sgs 91520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 11840 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 20160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 117760 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 96000 0x3F # 00111111   BE
```

### sw01-p4  (15 entries, util 10.9200 %)

```
sgs 5120 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13440 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 14720 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 134400 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13440 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 161600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 182400 0x3F # 00111111   BE
```

### sw02-p2  (13 entries, util 9.3600 %)

```
sgs 26880 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 39680 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 97920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 160640 0x3F # 00111111   BE
```

### sw02-p4  (25 entries, util 18.7200 %)

```
sgs 7680 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 13120 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 10240 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 13440 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 87680 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 13120 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 161920 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 13120 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 10240 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 139200 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 13120 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 154240 0x3F # 00111111   BE
```

### sw03-p4  (15 entries, util 10.9200 %)

```
sgs 83200 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 13440 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 19200 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 117120 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 104320 0x3F # 00111111   BE
```

### sw03-p5  (15 entries, util 10.9200 %)

```
sgs 10240 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 14400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 16960 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 131200 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 14400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 160640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 177280 0x3F # 00111111   BE
```

### sw04-p4  (13 entries, util 9.3600 %)

```
sgs 20160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 38080 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 99520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 167360 0x3F # 00111111   BE
```

### sw04-p5  (25 entries, util 18.7200 %)

```
sgs 15360 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 13760 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 8000 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13760 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 87680 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 13760 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 161280 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 13760 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 8000 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 140800 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 13760 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 145920 0x3F # 00111111   BE
```

### sw05-p4  (15 entries, util 10.9200 %)

```
sgs 15360 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 15360 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 19200 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 128000 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 15360 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 159680 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 172160 0x3F # 00111111   BE
```

### sw05-p5  (15 entries, util 10.9200 %)

```
sgs 74880 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 15040 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 18240 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 116480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 112640 0x3F # 00111111   BE
```

### sw06-p4  (25 entries, util 18.7200 %)

```
sgs 23040 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 14400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 15360 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 87680 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 160640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 142400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 137600 0x3F # 00111111   BE
```

### sw06-p5  (13 entries, util 9.3600 %)

```
sgs 13440 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 36480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 101120 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 174080 0x3F # 00111111   BE
```

### sw07-p4  (15 entries, util 10.9200 %)

```
sgs 66560 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 16640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 17280 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 115840 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 120960 0x3F # 00111111   BE
```

### sw07-p5  (15 entries, util 10.9200 %)

```
sgs 20480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 16320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 21440 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 124800 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 16320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 158720 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 167040 0x3F # 00111111   BE
```

### sw08-p2  (25 entries, util 18.7200 %)

```
sgs 25600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 4480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 6400 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 138880 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 174720 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 4480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 6400 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 138880 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 149120 0x3F # 00111111   BE
```

### sw08-p4  (13 entries, util 9.3600 %)

```
sgs 6720 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 34880 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 102720 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 180800 0x3F # 00111111   BE
```

### sw08-p5  (15 entries, util 10.9200 %)

```
sgs 58240 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 18240 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 16320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 115200 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 129280 0x3F # 00111111   BE
```

