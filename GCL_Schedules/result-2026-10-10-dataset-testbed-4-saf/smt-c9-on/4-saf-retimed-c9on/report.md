# SMT-synthesized GCL schedule (Problem 1: feasible schedule synthesis)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- TT queues: Q6, Q7; best effort filler mask 0x3F
- **Retimed from `result/result-2026-10-09-dataset-testbed-4-avgwin/smt-c9-off/4-t3600-c9off-minlat/schedule.json`**: flow set, routes, and release_offset pinned to exactly what that run admitted; only phi (window timing) is being re-solved here, under this run's own constraint set.
- Solver: Z3, maximize admitted flows (binary search), then minimize total latency, timeout 600s
- Result: **sat**, admitted 11/11 (proven optimal), solved in 26.71s
- Total latency (sum of e2e over admitted flows): **582000 ns** (proven minimum)

## Flows

stream.csv does not specify a talker offset; `offset (ns) = phi` below is the transmit time of each flow's first frame, computed by the solver (also in `offsets.csv` and `schedule.json`'s `offset_ns`).

| flow | route | L (B) | C (ns) | T (ns) | D (ns) | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|---|---|---|---|
| s0(id=1 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 300 | 12480 | 400000 | 400000 | 7 | 24960 | 46160 | yes |
| s2(id=3 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 100 | 12480 | 400000 | 400000 | 7 | 24960 | 42000 | yes |
| s5(id=6 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | 300 | 12480 | 800000 | 800000 | 6 | 49920 | 66960 | yes |
| s7(id=8 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 500 | 12480 | 200000 | 200000 | 7 | 0 | 54160 | yes |
| s8(id=9 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | 400 | 12480 | 800000 | 800000 | 7 | 74880 | 74000 | yes |
| s9(id=10 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 400 | 12480 | 400000 | 400000 | 6 | 49920 | 50960 | yes |
| s12(id=13 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 400 | 12480 | 200000 | 200000 | 6 | 0 | 43280 | yes |
| s13(id=14 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 500 | 12480 | 200000 | 200000 | 6 | 0 | 56080 | yes |
| s17(id=18 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | 300 | 12480 | 800000 | 800000 | 6 | 74880 | 39440 | yes |
| s18(id=19 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 500 | 12480 | 400000 | 400000 | 6 | 49920 | 54160 | yes |
| s19(id=20 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | 100 | 12480 | 200000 | 200000 | 6 | 24960 | 54800 | yes |

## Per-hop windows

| flow | egress port | queue | psi (ns) | delta (ns) |
|---|---|---|---|---|
| s0(id=1 S3->S2) | S3-p0 | Q7 | 24960 | 12480 |
| s0(id=1 S3->S2) | sw01-p4 | Q7 | 31680 | 12480 |
| s0(id=1 S3->S2) | sw03-p5 | Q7 | 38400 | 12480 |
| s0(id=1 S3->S2) | sw05-p4 | Q7 | 45120 | 12480 |
| s0(id=1 S3->S2) | sw07-p5 | Q7 | 51840 | 12480 |
| s0(id=1 S3->S2) | sw08-p2 | Q7 | 58560 | 12480 |
| s2(id=3 S2->S3) | S2-p0 | Q7 | 24960 | 12480 |
| s2(id=3 S2->S3) | sw08-p5 | Q7 | 30080 | 12480 |
| s2(id=3 S2->S3) | sw07-p4 | Q7 | 35200 | 12480 |
| s2(id=3 S2->S3) | sw05-p5 | Q7 | 40320 | 12480 |
| s2(id=3 S2->S3) | sw03-p4 | Q7 | 46080 | 12480 |
| s2(id=3 S2->S3) | sw01-p2 | Q7 | 54400 | 12480 |
| s5(id=6 S1->S3) | S1-p0 | Q6 | 49920 | 12480 |
| s5(id=6 S1->S3) | sw02-p4 | Q6 | 56640 | 12480 |
| s5(id=6 S1->S3) | sw04-p5 | Q6 | 63360 | 12480 |
| s5(id=6 S1->S3) | sw06-p4 | Q6 | 70080 | 12480 |
| s5(id=6 S1->S3) | sw08-p5 | Q6 | 76800 | 12480 |
| s5(id=6 S1->S3) | sw07-p4 | Q6 | 83520 | 12480 |
| s5(id=6 S1->S3) | sw05-p5 | Q6 | 90240 | 12480 |
| s5(id=6 S1->S3) | sw03-p4 | Q6 | 96960 | 12480 |
| s5(id=6 S1->S3) | sw01-p2 | Q6 | 104320 | 12480 |
| s7(id=8 S2->S3) | S2-p0 | Q7 | 0 | 12480 |
| s7(id=8 S2->S3) | sw08-p5 | Q7 | 8320 | 12480 |
| s7(id=8 S2->S3) | sw07-p4 | Q7 | 16640 | 12480 |
| s7(id=8 S2->S3) | sw05-p5 | Q7 | 24960 | 12480 |
| s7(id=8 S2->S3) | sw03-p4 | Q7 | 33280 | 12480 |
| s7(id=8 S2->S3) | sw01-p2 | Q7 | 41600 | 12480 |
| s8(id=9 S1->S3) | S1-p0 | Q7 | 74880 | 12480 |
| s8(id=9 S1->S3) | sw02-p4 | Q7 | 82560 | 12480 |
| s8(id=9 S1->S3) | sw04-p5 | Q7 | 90240 | 12480 |
| s8(id=9 S1->S3) | sw06-p4 | Q7 | 97920 | 12480 |
| s8(id=9 S1->S3) | sw08-p5 | Q7 | 105600 | 12480 |
| s8(id=9 S1->S3) | sw07-p4 | Q7 | 113280 | 12480 |
| s8(id=9 S1->S3) | sw05-p5 | Q7 | 120960 | 12480 |
| s8(id=9 S1->S3) | sw03-p4 | Q7 | 128640 | 12480 |
| s8(id=9 S1->S3) | sw01-p2 | Q7 | 136320 | 12480 |
| s9(id=10 S3->S2) | S3-p0 | Q6 | 49920 | 12480 |
| s9(id=10 S3->S2) | sw01-p4 | Q6 | 57600 | 12480 |
| s9(id=10 S3->S2) | sw03-p5 | Q6 | 65280 | 12480 |
| s9(id=10 S3->S2) | sw05-p4 | Q6 | 72960 | 12480 |
| s9(id=10 S3->S2) | sw07-p5 | Q6 | 80640 | 12480 |
| s9(id=10 S3->S2) | sw08-p2 | Q6 | 88320 | 12480 |
| s12(id=13 S1->S2) | S1-p0 | Q6 | 0 | 12480 |
| s12(id=13 S1->S2) | sw02-p4 | Q6 | 7680 | 12480 |
| s12(id=13 S1->S2) | sw04-p5 | Q6 | 15360 | 12480 |
| s12(id=13 S1->S2) | sw06-p4 | Q6 | 23040 | 12480 |
| s12(id=13 S1->S2) | sw08-p2 | Q6 | 30720 | 12480 |
| s13(id=14 S3->S2) | S3-p0 | Q6 | 0 | 12480 |
| s13(id=14 S3->S2) | sw01-p4 | Q6 | 8640 | 12480 |
| s13(id=14 S3->S2) | sw03-p5 | Q6 | 16960 | 12480 |
| s13(id=14 S3->S2) | sw05-p4 | Q6 | 25280 | 12480 |
| s13(id=14 S3->S2) | sw07-p5 | Q6 | 33600 | 12480 |
| s13(id=14 S3->S2) | sw08-p2 | Q6 | 43520 | 12480 |
| s17(id=18 S2->S1) | S2-p0 | Q6 | 74880 | 12480 |
| s17(id=18 S2->S1) | sw08-p4 | Q6 | 81600 | 12480 |
| s17(id=18 S2->S1) | sw06-p5 | Q6 | 88320 | 12480 |
| s17(id=18 S2->S1) | sw04-p4 | Q6 | 95040 | 12480 |
| s17(id=18 S2->S1) | sw02-p2 | Q6 | 101760 | 12480 |
| s18(id=19 S2->S3) | S2-p0 | Q6 | 49920 | 12480 |
| s18(id=19 S2->S3) | sw08-p5 | Q6 | 58240 | 12480 |
| s18(id=19 S2->S3) | sw07-p4 | Q6 | 66560 | 12480 |
| s18(id=19 S2->S3) | sw05-p5 | Q6 | 74880 | 12480 |
| s18(id=19 S2->S3) | sw03-p4 | Q6 | 83200 | 12480 |
| s18(id=19 S2->S3) | sw01-p2 | Q6 | 91520 | 12480 |
| s19(id=20 S1->S3) | S1-p0 | Q6 | 24960 | 12480 |
| s19(id=20 S1->S3) | sw02-p4 | Q6 | 30080 | 12480 |
| s19(id=20 S1->S3) | sw04-p5 | Q6 | 35200 | 12480 |
| s19(id=20 S1->S3) | sw06-p4 | Q6 | 40320 | 12480 |
| s19(id=20 S1->S3) | sw08-p5 | Q6 | 45440 | 12480 |
| s19(id=20 S1->S3) | sw07-p4 | Q6 | 50560 | 12480 |
| s19(id=20 S1->S3) | sw05-p5 | Q6 | 55680 | 12480 |
| s19(id=20 S1->S3) | sw03-p4 | Q6 | 62080 | 12480 |
| s19(id=20 S1->S3) | sw01-p2 | Q6 | 67200 | 12480 |

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
sgs 41600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 11840 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 19520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 92800 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 161920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 11840 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 137600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 120320 0x3F # 00111111   BE
```

### sw01-p4  (17 entries, util 12.4800 %)

```
sgs 8640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 10560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13440 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 138560 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 10560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 13440 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 138560 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 178880 0x3F # 00111111   BE
```

### sw02-p2  (3 entries, util 1.5600 %)

```
sgs 101760 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 685760 0x3F # 00111111   BE
```

### sw02-p4  (21 entries, util 15.6000 %)

```
sgs 7680 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 9920 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 14080 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 13440 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 112640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 9920 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 165120 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 9920 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 165120 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 9920 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 157440 0x3F # 00111111   BE
```

### sw03-p4  (29 entries, util 21.8400 %)

```
sgs 33280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 3520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 8640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 1280 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 19200 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 92160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 16320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 158720 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 3520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 8640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 137600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 16320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 125440 0x3F # 00111111   BE
```

### sw03-p5  (17 entries, util 12.4800 %)

```
sgs 16960 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 8960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 14400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 139200 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 8960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 14400 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 139200 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 170560 0x3F # 00111111   BE
```

### sw04-p4  (3 entries, util 1.5600 %)

```
sgs 95040 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 692480 0x3F # 00111111   BE
```

### sw04-p5  (21 entries, util 15.6000 %)

```
sgs 15360 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 7360 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 15680 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 14400 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 112640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 7360 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 167680 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 7360 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 167680 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 7360 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 152320 0x3F # 00111111   BE
```

### sw05-p4  (17 entries, util 12.4800 %)

```
sgs 25280 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 7360 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 15360 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 139840 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 7360 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 15360 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 139840 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 162240 0x3F # 00111111   BE
```

### sw05-p5  (29 entries, util 21.8400 %)

```
sgs 24960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 2880 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 2880 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 6720 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 2880 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 18240 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 91520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 18240 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 156800 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 2880 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 2880 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 6720 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 137600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 18240 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 131840 0x3F # 00111111   BE
```

### sw06-p4  (21 entries, util 15.6000 %)

```
sgs 23040 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 4800 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 17280 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 15360 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 112640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 4800 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 170240 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 4800 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 170240 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 4800 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 147200 0x3F # 00111111   BE
```

### sw06-p5  (3 entries, util 1.5600 %)

```
sgs 88320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 699200 0x3F # 00111111   BE
```

### sw07-p4  (29 entries, util 21.8400 %)

```
sgs 16640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 6080 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 2880 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 3520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 4480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 17280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 90880 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 21440 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 153600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 6080 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 2880 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 3520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 137600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 21440 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 136960 0x3F # 00111111   BE
```

### sw07-p5  (17 entries, util 12.4800 %)

```
sgs 33600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 16320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 140480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 5760 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 16320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 140480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 153920 0x3F # 00111111   BE
```

### sw08-p2  (25 entries, util 18.7200 %)

```
sgs 30720 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 2560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 17280 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 129920 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 174720 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 2560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 17280 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 129920 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 144000 0x3F # 00111111   BE
```

### sw08-p4  (3 entries, util 1.5600 %)

```
sgs 81600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 705920 0x3F # 00111111   BE
```

### sw08-p5  (29 entries, util 21.8400 %)

```
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 9280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 2880 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 6080 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 16320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 90240 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 24640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 150400 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 9280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 2880 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 137600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 24640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 142080 0x3F # 00111111   BE
```

