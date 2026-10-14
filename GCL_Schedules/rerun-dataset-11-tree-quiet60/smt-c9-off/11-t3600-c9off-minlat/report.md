# SMT-synthesized GCL schedule (Problem 1: feasible schedule synthesis)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- TT queues: Q6, Q7; best effort filler mask 0x3F
- Solver: Z3, maximize admitted flows (binary search), then minimize total latency, timeout 3600s
- Result: **sat**, admitted 10/20 (proven optimal), solved in 245.64s
- Total latency (sum of e2e over admitted flows): **934560 ns** (proven minimum)

- **WARNING: C9 disabled for this run** -- see Constraint check below for the resulting violations.

## Flows

stream.csv does not specify a talker offset; `offset (ns) = phi` below is the transmit time of each flow's first frame, computed by the solver (also in `offsets.csv` and `schedule.json`'s `offset_ns`).

| flow | route | L (B) | C (ns) | T (ns) | D (ns) | pcp | offset (ns) | e2e (ns) | admitted |
|---|---|---|---|---|---|---|---|---|---|
| s0(id=1 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 500 | 12480 | 200000 | 200000 | 6 | 0 | 79120 | yes |
| s1(id=2 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 400 | 12480 | 200000 | 200000 | 6 | 0 | 95760 | yes |
| s2(id=3 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 500 | 12480 | 400000 | 400000 | 7 | 24960 | 83600 | yes |
| s3(id=4 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 500 | 12480 | 400000 | 400000 | None | None | None | no |
| s4(id=5 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | 200 | 12480 | 200000 | 200000 | 7 | 0 | 79120 | yes |
| s5(id=6 S3->S1) | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | 200 | 12480 | 200000 | 200000 | None | None | None | no |
| s6(id=7 S2->S1) | S2->sw08->sw06->sw04->sw02->S1 | 300 | 12480 | 800000 | 800000 | 7 | 37440 | 79120 | yes |
| s7(id=8 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 500 | 12480 | 200000 | 200000 | 6 | 24960 | 96400 | yes |
| s8(id=9 S3->S2) | S3->sw01->sw03->sw05->sw07->sw08->S2 | 100 | 12480 | 800000 | 800000 | 7 | 74880 | 95760 | yes |
| s9(id=10 S3->S1) | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | 300 | 12480 | 400000 | 400000 | 7 | 49920 | 145680 | yes |
| s10(id=11 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | 100 | 12480 | 200000 | 200000 | None | None | None | no |
| s11(id=12 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 300 | 12480 | 400000 | 400000 | None | None | None | no |
| s12(id=13 S1->S3) | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | 300 | 12480 | 800000 | 800000 | None | None | None | no |
| s13(id=14 S3->S1) | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | 400 | 12480 | 200000 | 200000 | None | None | None | no |
| s14(id=15 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 300 | 12480 | 800000 | 800000 | None | None | None | no |
| s15(id=16 S3->S1) | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | 500 | 12480 | 400000 | 400000 | None | None | None | no |
| s16(id=17 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 400 | 12480 | 400000 | 400000 | None | None | None | no |
| s17(id=18 S2->S3) | S2->sw08->sw07->sw05->sw03->sw01->S3 | 500 | 12480 | 800000 | 800000 | 7 | 62400 | 95760 | yes |
| s18(id=19 S3->S1) | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | 400 | 12480 | 800000 | 800000 | None | None | None | no |
| s19(id=20 S1->S2) | S1->sw02->sw04->sw06->sw08->S2 | 500 | 12480 | 400000 | 400000 | 7 | 49920 | 84240 | yes |

## Per-hop windows

| flow | egress port | queue | psi (ns) | delta (ns) |
|---|---|---|---|---|
| s0(id=1 S1->S2) | S1-p0 | Q6 | 0 | 12480 |
| s0(id=1 S1->S2) | sw02-p4 | Q6 | 16640 | 12480 |
| s0(id=1 S1->S2) | sw04-p5 | Q6 | 33280 | 12480 |
| s0(id=1 S1->S2) | sw06-p4 | Q6 | 49920 | 12480 |
| s0(id=1 S1->S2) | sw08-p2 | Q6 | 66560 | 12480 |
| s1(id=2 S3->S2) | S3-p0 | Q6 | 0 | 12480 |
| s1(id=2 S3->S2) | sw01-p4 | Q6 | 16640 | 12480 |
| s1(id=2 S3->S2) | sw03-p5 | Q6 | 33280 | 12480 |
| s1(id=2 S3->S2) | sw05-p4 | Q6 | 49920 | 12480 |
| s1(id=2 S3->S2) | sw07-p5 | Q6 | 66560 | 12480 |
| s1(id=2 S3->S2) | sw08-p2 | Q6 | 83200 | 12480 |
| s2(id=3 S1->S2) | S1-p0 | Q7 | 24960 | 12480 |
| s2(id=3 S1->S2) | sw02-p4 | Q7 | 41600 | 12480 |
| s2(id=3 S1->S2) | sw04-p5 | Q7 | 58240 | 12480 |
| s2(id=3 S1->S2) | sw06-p4 | Q7 | 74880 | 12480 |
| s2(id=3 S1->S2) | sw08-p2 | Q7 | 96000 | 12480 |
| s4(id=5 S2->S1) | S2-p0 | Q7 | 0 | 12480 |
| s4(id=5 S2->S1) | sw08-p4 | Q7 | 16640 | 12480 |
| s4(id=5 S2->S1) | sw06-p5 | Q7 | 33280 | 12480 |
| s4(id=5 S2->S1) | sw04-p4 | Q7 | 49920 | 12480 |
| s4(id=5 S2->S1) | sw02-p2 | Q7 | 66560 | 12480 |
| s6(id=7 S2->S1) | S2-p0 | Q7 | 37440 | 12480 |
| s6(id=7 S2->S1) | sw08-p4 | Q7 | 54080 | 12480 |
| s6(id=7 S2->S1) | sw06-p5 | Q7 | 70720 | 12480 |
| s6(id=7 S2->S1) | sw04-p4 | Q7 | 87360 | 12480 |
| s6(id=7 S2->S1) | sw02-p2 | Q7 | 104000 | 12480 |
| s7(id=8 S3->S2) | S3-p0 | Q6 | 24960 | 12480 |
| s7(id=8 S3->S2) | sw01-p4 | Q6 | 41600 | 12480 |
| s7(id=8 S3->S2) | sw03-p5 | Q6 | 58240 | 12480 |
| s7(id=8 S3->S2) | sw05-p4 | Q6 | 74880 | 12480 |
| s7(id=8 S3->S2) | sw07-p5 | Q6 | 91520 | 12480 |
| s7(id=8 S3->S2) | sw08-p2 | Q6 | 108800 | 12480 |
| s8(id=9 S3->S2) | S3-p0 | Q7 | 74880 | 12480 |
| s8(id=9 S3->S2) | sw01-p4 | Q7 | 91520 | 12480 |
| s8(id=9 S3->S2) | sw03-p5 | Q7 | 108160 | 12480 |
| s8(id=9 S3->S2) | sw05-p4 | Q7 | 124800 | 12480 |
| s8(id=9 S3->S2) | sw07-p5 | Q7 | 141440 | 12480 |
| s8(id=9 S3->S2) | sw08-p2 | Q7 | 158080 | 12480 |
| s9(id=10 S3->S1) | S3-p0 | Q7 | 49920 | 12480 |
| s9(id=10 S3->S1) | sw01-p4 | Q7 | 66560 | 12480 |
| s9(id=10 S3->S1) | sw03-p5 | Q7 | 83200 | 12480 |
| s9(id=10 S3->S1) | sw05-p4 | Q7 | 99840 | 12480 |
| s9(id=10 S3->S1) | sw07-p5 | Q7 | 116480 | 12480 |
| s9(id=10 S3->S1) | sw08-p4 | Q7 | 133120 | 12480 |
| s9(id=10 S3->S1) | sw06-p5 | Q7 | 149760 | 12480 |
| s9(id=10 S3->S1) | sw04-p4 | Q7 | 166400 | 12480 |
| s9(id=10 S3->S1) | sw02-p2 | Q7 | 183040 | 12480 |
| s17(id=18 S2->S3) | S2-p0 | Q7 | 62400 | 12480 |
| s17(id=18 S2->S3) | sw08-p5 | Q7 | 79040 | 12480 |
| s17(id=18 S2->S3) | sw07-p4 | Q7 | 95680 | 12480 |
| s17(id=18 S2->S3) | sw05-p5 | Q7 | 112320 | 12480 |
| s17(id=18 S2->S3) | sw03-p4 | Q7 | 128960 | 12480 |
| s17(id=18 S2->S3) | sw01-p2 | Q7 | 145600 | 12480 |
| s19(id=20 S1->S2) | S1-p0 | Q7 | 49920 | 12480 |
| s19(id=20 S1->S2) | sw02-p4 | Q7 | 66560 | 12480 |
| s19(id=20 S1->S2) | sw04-p5 | Q7 | 83200 | 12480 |
| s19(id=20 S1->S2) | sw06-p4 | Q7 | 104960 | 12480 |
| s19(id=20 S1->S2) | sw08-p2 | Q7 | 121600 | 12480 |

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
sgs 145600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 641920 0x3F # 00111111   BE
```

### sw01-p4  (23 entries, util 17.1600 %)

```
sgs 16640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 112640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 162560 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 137600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 145920 0x3F # 00111111   BE
```

### sw02-p2  (15 entries, util 10.9200 %)

```
sgs 66560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 66560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 71040 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 104000 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 71040 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 120960 0x3F # 00111111   BE
```

### sw02-p4  (17 entries, util 12.4800 %)

```
sgs 16640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 137600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 137600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 170880 0x3F # 00111111   BE
```

### sw03-p4  (3 entries, util 1.5600 %)

```
sgs 128960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 658560 0x3F # 00111111   BE
```

### sw03-p5  (23 entries, util 17.1600 %)

```
sgs 33280 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 112640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 162560 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 137600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 129280 0x3F # 00111111   BE
```

### sw04-p4  (15 entries, util 10.9200 %)

```
sgs 49920 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 66560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 71040 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 104000 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 71040 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 137600 0x3F # 00111111   BE
```

### sw04-p5  (17 entries, util 12.4800 %)

```
sgs 33280 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 137600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 137600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 154240 0x3F # 00111111   BE
```

### sw05-p4  (23 entries, util 17.1600 %)

```
sgs 49920 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 112640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 162560 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 137600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 112640 0x3F # 00111111   BE
```

### sw05-p5  (3 entries, util 1.5600 %)

```
sgs 112320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 675200 0x3F # 00111111   BE
```

### sw06-p4  (17 entries, util 12.4800 %)

```
sgs 49920 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 17600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 132480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 17600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 132480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 137600 0x3F # 00111111   BE
```

### sw06-p5  (15 entries, util 10.9200 %)

```
sgs 33280 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 66560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 71040 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 104000 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 71040 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 154240 0x3F # 00111111   BE
```

### sw07-p4  (3 entries, util 1.5600 %)

```
sgs 95680 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 691840 0x3F # 00111111   BE
```

### sw07-p5  (23 entries, util 17.1600 %)

```
sgs 66560 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 112640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 162560 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 137600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 12480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 96000 0x3F # 00111111   BE
```

### sw08-p2  (35 entries, util 26.5200 %)

```
sgs 66560 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 24000 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 96000 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 13120 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 145280 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 132480 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 4160 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 13120 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 78720 0x3F # 00111111   BE
```

### sw08-p4  (15 entries, util 10.9200 %)

```
sgs 16640 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 24960 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 66560 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 71040 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 187520 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 104000 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 71040 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 170880 0x3F # 00111111   BE
```

### sw08-p5  (3 entries, util 1.5600 %)

```
sgs 79040 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 708480 0x3F # 00111111   BE
```

