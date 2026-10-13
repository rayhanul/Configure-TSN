# Reconfiguration-free admission (Problem 3)

- Cycle time (= hyperperiod): **800000 ns**
- Link rate 1.00 Gb/s, tick 320 ns, GCL_size 255, bridge delay 4020 ns
- Frozen schedule W loaded from: **result/result-2026-10-13-dataset-testbed-13-tree-avgwin/rl-c9-on/13-matrix-c9on**

## Admission: W (before) vs. after this run's arrivals

| | admitted | of total |
|---|---|---|
| W (base, unchanged) | 11 | 11 |
| + this run's arrivals | 17 | 39 |

Every arrival admitted here required **zero** window-boundary changes -- see the GCL-entry table below (unchanged from W by construction) and the window-boundary integrity check. No previously-admitted flow was rerouted.

## Arrivals

| id | src->dst | RS(s) size | admitted | route | queue | phi_s (ns) | e2e (ns) | rerouted to make room | reason if rejected |
|---|---|---|---|---|---|---|---|---|---|
| 7 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 16 | S1->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 11 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 1 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q6 | 111040 | 109120 | - | - |
| 12 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 18 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 6 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q7 | 49920 | 140800 | - | - |
| 4 | S2->S3 | - | yes | S2->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 87360 | 92160 | - | - |
| 2 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q6 | 12480 | 125120 | - | - |
| 32 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 40 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 42 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 49 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q6 | 37440 | 112960 | - | - |
| 22 | S2->S3 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 48 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 | 74880 | 111040 | - | - |
| 26 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q7 | 87360 | 300480 | - | - |
| 31 | S1->S3 | - | yes | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 212480 | 148160 | - | - |
| 37 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q7 | 150080 | 437760 | - | - |
| 44 | S1->S3 | - | yes | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | Q6 | 224960 | 148160 | - | - |
| 25 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 36 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 41 | S1->S2 | - | yes | S1->sw02->sw04->sw06->sw08->S2 | Q6 | 237440 | 111360 | - | - |
| 45 | S3->S2 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->S2 | Q7 | 350080 | 235840 | - | - |
| 23 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q6 | 123520 | 184640 | - | - |
| 24 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q6 | 212480 | 108800 | - | - |
| 29 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q6 | 224960 | 108800 | - | - |
| 38 | S1->S3 | - | yes | S1->sw02->sw04->sw06->sw08->sw07->sw05->sw03->sw01->S3 | Q7 | 62400 | 308800 | - | - |
| 46 | S3->S1 | - | yes | S3->sw01->sw03->sw05->sw07->sw08->sw06->sw04->sw02->S1 | Q6 | 237440 | 108800 | - | - |
| 47 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 30 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 34 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 35 | S2->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 39 | S1->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 21 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 28 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 33 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 43 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 50 | S3->S2 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |
| 27 | S3->S1 | - | no | - | - | - | - | - | no route in RS(s) / queue / window assignment satisfies C1-C7,C9 without changing any window boundary |

## Per-port GCL entries (should equal W exactly)

| port | W entries | after arrivals | GCL_size |
|---|---|---|---|
| sw01-p2 | 23 | 23 | 255 |
| sw01-p4 | 19 | 19 | 255 |
| sw02-p2 | 28 | 28 | 255 |
| sw02-p4 | 21 | 21 | 255 |
| sw03-p4 | 25 | 25 | 255 |
| sw03-p5 | 22 | 22 | 255 |
| sw04-p4 | 34 | 34 | 255 |
| sw04-p5 | 23 | 23 | 255 |
| sw05-p4 | 22 | 22 | 255 |
| sw05-p5 | 25 | 25 | 255 |
| sw06-p4 | 24 | 24 | 255 |
| sw06-p5 | 32 | 32 | 255 |
| sw07-p4 | 25 | 25 | 255 |
| sw07-p5 | 19 | 19 | 255 |
| sw08-p2 | 28 | 28 | 255 |
| sw08-p4 | 29 | 29 | 255 |
| sw08-p5 | 28 | 28 | 255 |

## Per-hop windows used by newly admitted flows

| flow | egress port | queue | psi (ns, unchanged) | delta (ns, unchanged) |
|---|---|---|---|---|
| s20(id=1 S3->S2) | S3-p0 | Q6 | 111040 | 12480 |
| s20(id=1 S3->S2) | sw01-p4 | Q6 | 119360 | 12480 |
| s20(id=1 S3->S2) | sw03-p5 | Q6 | 127680 | 12480 |
| s20(id=1 S3->S2) | sw05-p4 | Q6 | 136000 | 12480 |
| s20(id=1 S3->S2) | sw07-p5 | Q6 | 200000 | 12480 |
| s20(id=1 S3->S2) | sw08-p2 | Q6 | 207680 | 12480 |
| s23(id=6 S3->S1) | S3-p0 | Q7 | 49920 | 12480 |
| s23(id=6 S3->S1) | sw01-p4 | Q7 | 57600 | 12480 |
| s23(id=6 S3->S1) | sw03-p5 | Q7 | 65280 | 12480 |
| s23(id=6 S3->S1) | sw05-p4 | Q7 | 72960 | 12480 |
| s23(id=6 S3->S1) | sw07-p5 | Q7 | 80640 | 12480 |
| s23(id=6 S3->S1) | sw08-p4 | Q7 | 155200 | 12480 |
| s23(id=6 S3->S1) | sw06-p5 | Q7 | 162880 | 12480 |
| s23(id=6 S3->S1) | sw04-p4 | Q7 | 170560 | 12480 |
| s23(id=6 S3->S1) | sw02-p2 | Q7 | 178240 | 12480 |
| s22(id=4 S2->S3) | S2-p0 | Q7 | 87360 | 12480 |
| s22(id=4 S2->S3) | sw08-p5 | Q7 | 140160 | 12480 |
| s22(id=4 S2->S3) | sw07-p4 | Q7 | 146880 | 12480 |
| s22(id=4 S2->S3) | sw05-p5 | Q7 | 153600 | 12480 |
| s22(id=4 S2->S3) | sw03-p4 | Q7 | 160320 | 12480 |
| s22(id=4 S2->S3) | sw01-p2 | Q7 | 167040 | 12480 |
| s21(id=2 S1->S2) | S1-p0 | Q6 | 12480 | 12480 |
| s21(id=2 S1->S2) | sw02-p4 | Q6 | 20160 | 12480 |
| s21(id=2 S1->S2) | sw04-p5 | Q6 | 26240 | 12480 |
| s21(id=2 S1->S2) | sw06-p4 | Q6 | 102080 | 12480 |
| s21(id=2 S1->S2) | sw08-p2 | Q6 | 125120 | 12480 |
| s57(id=49 S1->S2) | S1-p0 | Q6 | 37440 | 12480 |
| s57(id=49 S1->S2) | sw02-p4 | Q6 | 104960 | 12480 |
| s57(id=49 S1->S2) | sw04-p5 | Q6 | 110080 | 12480 |
| s57(id=49 S1->S2) | sw06-p4 | Q6 | 132800 | 12480 |
| s57(id=49 S1->S2) | sw08-p2 | Q6 | 137920 | 12480 |
| s56(id=48 S3->S2) | S3-p0 | Q7 | 74880 | 12480 |
| s56(id=48 S3->S2) | sw01-p4 | Q7 | 83200 | 12480 |
| s56(id=48 S3->S2) | sw03-p5 | Q7 | 91520 | 12480 |
| s56(id=48 S3->S2) | sw05-p4 | Q7 | 99840 | 12480 |
| s56(id=48 S3->S2) | sw07-p5 | Q7 | 108160 | 12480 |
| s56(id=48 S3->S2) | sw08-p2 | Q7 | 173440 | 12480 |
| s34(id=26 S3->S1) | S3-p0 | Q7 | 87360 | 12480 |
| s34(id=26 S3->S1) | sw01-p4 | Q7 | 95680 | 12480 |
| s34(id=26 S3->S1) | sw03-p5 | Q7 | 104000 | 12480 |
| s34(id=26 S3->S1) | sw05-p4 | Q7 | 112320 | 12480 |
| s34(id=26 S3->S1) | sw07-p5 | Q7 | 344320 | 12480 |
| s34(id=26 S3->S1) | sw08-p4 | Q7 | 355200 | 12480 |
| s34(id=26 S3->S1) | sw06-p5 | Q7 | 361920 | 12480 |
| s34(id=26 S3->S1) | sw04-p4 | Q7 | 368640 | 12480 |
| s34(id=26 S3->S1) | sw02-p2 | Q7 | 375360 | 12480 |
| s39(id=31 S1->S3) | S1-p0 | Q6 | 212480 | 12480 |
| s39(id=31 S1->S3) | sw02-p4 | Q6 | 220160 | 12480 |
| s39(id=31 S1->S3) | sw04-p5 | Q6 | 227840 | 12480 |
| s39(id=31 S1->S3) | sw06-p4 | Q6 | 302080 | 12480 |
| s39(id=31 S1->S3) | sw08-p5 | Q6 | 317440 | 12480 |
| s39(id=31 S1->S3) | sw07-p4 | Q6 | 325120 | 12480 |
| s39(id=31 S1->S3) | sw05-p5 | Q6 | 332800 | 12480 |
| s39(id=31 S1->S3) | sw03-p4 | Q6 | 340480 | 12480 |
| s39(id=31 S1->S3) | sw01-p2 | Q6 | 348160 | 12480 |
| s45(id=37 S3->S1) | S3-p0 | Q7 | 150080 | 12480 |
| s45(id=37 S3->S1) | sw01-p4 | Q7 | 156160 | 12480 |
| s45(id=37 S3->S1) | sw03-p5 | Q7 | 162240 | 12480 |
| s45(id=37 S3->S1) | sw05-p4 | Q7 | 350080 | 12480 |
| s45(id=37 S3->S1) | sw07-p5 | Q7 | 544320 | 12480 |
| s45(id=37 S3->S1) | sw08-p4 | Q7 | 555200 | 12480 |
| s45(id=37 S3->S1) | sw06-p5 | Q7 | 561920 | 12480 |
| s45(id=37 S3->S1) | sw04-p4 | Q7 | 568640 | 12480 |
| s45(id=37 S3->S1) | sw02-p2 | Q7 | 575360 | 12480 |
| s52(id=44 S1->S3) | S1-p0 | Q6 | 224960 | 12480 |
| s52(id=44 S1->S3) | sw02-p4 | Q6 | 232640 | 12480 |
| s52(id=44 S1->S3) | sw04-p5 | Q6 | 307200 | 12480 |
| s52(id=44 S1->S3) | sw06-p4 | Q6 | 314880 | 12480 |
| s52(id=44 S1->S3) | sw08-p5 | Q6 | 329920 | 12480 |
| s52(id=44 S1->S3) | sw07-p4 | Q6 | 337600 | 12480 |
| s52(id=44 S1->S3) | sw05-p5 | Q6 | 345280 | 12480 |
| s52(id=44 S1->S3) | sw03-p4 | Q6 | 352960 | 12480 |
| s52(id=44 S1->S3) | sw01-p2 | Q6 | 360640 | 12480 |
| s49(id=41 S1->S2) | S1-p0 | Q6 | 237440 | 12480 |
| s49(id=41 S1->S2) | sw02-p4 | Q6 | 311040 | 12480 |
| s49(id=41 S1->S2) | sw04-p5 | Q6 | 319680 | 12480 |
| s49(id=41 S1->S2) | sw06-p4 | Q6 | 328000 | 12480 |
| s49(id=41 S1->S2) | sw08-p2 | Q6 | 336320 | 12480 |
| s53(id=45 S3->S2) | S3-p0 | Q7 | 350080 | 12480 |
| s53(id=45 S3->S2) | sw01-p4 | Q7 | 356800 | 12480 |
| s53(id=45 S3->S2) | sw03-p5 | Q7 | 363520 | 12480 |
| s53(id=45 S3->S2) | sw05-p4 | Q7 | 550080 | 12480 |
| s53(id=45 S3->S2) | sw07-p5 | Q7 | 556800 | 12480 |
| s53(id=45 S3->S2) | sw08-p2 | Q7 | 573440 | 12480 |
| s31(id=23 S3->S1) | S3-p0 | Q6 | 123520 | 12480 |
| s31(id=23 S3->S1) | sw01-p4 | Q6 | 131840 | 12480 |
| s31(id=23 S3->S1) | sw03-p5 | Q6 | 200000 | 12480 |
| s31(id=23 S3->S1) | sw05-p4 | Q6 | 207680 | 12480 |
| s31(id=23 S3->S1) | sw07-p5 | Q6 | 215360 | 12480 |
| s31(id=23 S3->S1) | sw08-p4 | Q6 | 223040 | 12480 |
| s31(id=23 S3->S1) | sw06-p5 | Q6 | 230720 | 12480 |
| s31(id=23 S3->S1) | sw04-p4 | Q6 | 288000 | 12480 |
| s31(id=23 S3->S1) | sw02-p2 | Q6 | 295680 | 12480 |
| s32(id=24 S3->S1) | S3-p0 | Q6 | 212480 | 12480 |
| s32(id=24 S3->S1) | sw01-p4 | Q6 | 220800 | 12480 |
| s32(id=24 S3->S1) | sw03-p5 | Q6 | 229120 | 12480 |
| s32(id=24 S3->S1) | sw05-p4 | Q6 | 237440 | 12480 |
| s32(id=24 S3->S1) | sw07-p5 | Q6 | 245760 | 12480 |
| s32(id=24 S3->S1) | sw08-p4 | Q6 | 271360 | 12480 |
| s32(id=24 S3->S1) | sw06-p5 | Q6 | 291840 | 12480 |
| s32(id=24 S3->S1) | sw04-p4 | Q6 | 300480 | 12480 |
| s32(id=24 S3->S1) | sw02-p2 | Q6 | 308800 | 12480 |
| s37(id=29 S3->S1) | S3-p0 | Q6 | 224960 | 12480 |
| s37(id=29 S3->S1) | sw01-p4 | Q6 | 233280 | 12480 |
| s37(id=29 S3->S1) | sw03-p5 | Q6 | 241600 | 12480 |
| s37(id=29 S3->S1) | sw05-p4 | Q6 | 249920 | 12480 |
| s37(id=29 S3->S1) | sw07-p5 | Q6 | 279040 | 12480 |
| s37(id=29 S3->S1) | sw08-p4 | Q6 | 290560 | 12480 |
| s37(id=29 S3->S1) | sw06-p5 | Q6 | 304320 | 12480 |
| s37(id=29 S3->S1) | sw04-p4 | Q6 | 312960 | 12480 |
| s37(id=29 S3->S1) | sw02-p2 | Q6 | 321280 | 12480 |
| s46(id=38 S1->S3) | S1-p0 | Q7 | 62400 | 12480 |
| s46(id=38 S1->S3) | sw02-p4 | Q7 | 69440 | 12480 |
| s46(id=38 S1->S3) | sw04-p5 | Q7 | 152960 | 12480 |
| s46(id=38 S1->S3) | sw06-p4 | Q7 | 159680 | 12480 |
| s46(id=38 S1->S3) | sw08-p5 | Q7 | 166400 | 12480 |
| s46(id=38 S1->S3) | sw07-p4 | Q7 | 173120 | 12480 |
| s46(id=38 S1->S3) | sw05-p5 | Q7 | 179840 | 12480 |
| s46(id=38 S1->S3) | sw03-p4 | Q7 | 186560 | 12480 |
| s46(id=38 S1->S3) | sw01-p2 | Q7 | 193280 | 12480 |
| s54(id=46 S3->S1) | S3-p0 | Q6 | 237440 | 12480 |
| s54(id=46 S3->S1) | sw01-p4 | Q6 | 245760 | 12480 |
| s54(id=46 S3->S1) | sw03-p5 | Q6 | 254080 | 12480 |
| s54(id=46 S3->S1) | sw05-p4 | Q6 | 284480 | 12480 |
| s54(id=46 S3->S1) | sw07-p5 | Q6 | 291520 | 12480 |
| s54(id=46 S3->S1) | sw08-p4 | Q6 | 303040 | 12480 |
| s54(id=46 S3->S1) | sw06-p5 | Q6 | 316800 | 12480 |
| s54(id=46 S3->S1) | sw04-p4 | Q6 | 325440 | 12480 |
| s54(id=46 S3->S1) | sw02-p2 | Q6 | 333760 | 12480 |

## Constraint check

- C1-C7, C9: OK
- window-boundary integrity (no window's psi/delta changed anywhere): OK

## GCL per egress port

### sw01-p2  (23 entries, util 23.4000 %)

```
sgs 55360 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 18560 0xBF # 10111111   Q7
sgs 25280 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 25920 0x40 # 01000000   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 40320 0x80 # 10000000   Q7
sgs 48000 0x7F # 01111111   Q6
sgs 35840 0x40 # 01000000   Q6
sgs 48000 0x7F # 01111111   Q6
sgs 68160 0x40 # 01000000   Q6
sgs 48000 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 18560 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 13120 0x7F # 01111111   Q6
sgs 95360 0x40 # 01000000   Q6
sgs 48000 0x7F # 01111111   Q6
sgs 35840 0x40 # 01000000   Q6
sgs 48000 0x7F # 01111111   Q6
sgs 12800 0x40 # 01000000   Q6
sgs 48000 0xBF # 10111111   Q7
```

### sw01-p4  (19 entries, util 35.8800 %)

```
sgs 8320 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 22720 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 14720 0xBF # 10111111   Q7
sgs 48640 0x80 # 10000000   Q7
sgs 30720 0x7F # 01111111   Q6
sgs 58240 0xBF # 10111111   Q7
sgs 111040 0x40 # 01000000   Q6
sgs 30720 0x7F # 01111111   Q6
sgs 58240 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 22720 0x7F # 01111111   Q6
sgs 75840 0x40 # 01000000   Q6
sgs 30720 0x7F # 01111111   Q6
sgs 58240 0xBF # 10111111   Q7
sgs 102720 0x40 # 01000000   Q6
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw02-p2  (28 entries, util 26.5200 %)

```
sgs 26880 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 43840 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 1920 0x3F # 00111111   BE
sgs 52480 0x40 # 01000000   Q6
sgs 24640 0xBF # 10111111   Q7
sgs 26880 0x7F # 01111111   Q6
sgs 17280 0x80 # 10000000   Q7
sgs 51520 0xBF # 10111111   Q7
sgs 79680 0x40 # 01000000   Q6
sgs 24640 0xBF # 10111111   Q7
sgs 26880 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 43840 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 66880 0x80 # 10000000   Q7
sgs 24640 0xBF # 10111111   Q7
sgs 26880 0x7F # 01111111   Q6
sgs 17280 0x80 # 10000000   Q7
sgs 51520 0xBF # 10111111   Q7
sgs 52800 0x40 # 01000000   Q6
sgs 51520 0xBF # 10111111   Q7
```

### sw02-p4  (21 entries, util 23.4000 %)

```
sgs 6080 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 1600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 36800 0x80 # 10000000   Q7
sgs 35520 0xBF # 10111111   Q7
sgs 46400 0x40 # 01000000   Q6
sgs 54720 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 1600 0x3F # 00111111   BE
sgs 131200 0x40 # 01000000   Q6
sgs 54720 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 1600 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 118720 0x80 # 10000000   Q7
sgs 54720 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 1600 0x3F # 00111111   BE
sgs 125120 0x40 # 01000000   Q6
sgs 54720 0xBF # 10111111   Q7
```

### sw03-p4  (25 entries, util 23.4000 %)

```
sgs 49280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 16960 0xBF # 10111111   Q7
sgs 25280 0x80 # 10000000   Q7
sgs 1280 0x3F # 00111111   BE
sgs 27520 0x40 # 01000000   Q6
sgs 27520 0x7F # 01111111   Q6
sgs 40960 0x80 # 10000000   Q7
sgs 48000 0x7F # 01111111   Q6
sgs 36480 0x40 # 01000000   Q6
sgs 14400 0xBF # 10111111   Q7
sgs 33600 0x7F # 01111111   Q6
sgs 67520 0x40 # 01000000   Q6
sgs 48000 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 16960 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 14080 0x7F # 01111111   Q6
sgs 96000 0x40 # 01000000   Q6
sgs 48000 0x7F # 01111111   Q6
sgs 36480 0x40 # 01000000   Q6
sgs 14400 0xBF # 10111111   Q7
sgs 33600 0x7F # 01111111   Q6
sgs 18240 0x40 # 01000000   Q6
sgs 48000 0xBF # 10111111   Q7
```

### sw03-p5  (22 entries, util 35.8800 %)

```
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 20480 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 16960 0xBF # 10111111   Q7
sgs 48640 0x80 # 10000000   Q7
sgs 22400 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 111040 0x40 # 01000000   Q6
sgs 22400 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 20480 0x7F # 01111111   Q6
sgs 78080 0x40 # 01000000   Q6
sgs 22400 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 16640 0x7F # 01111111   Q6
sgs 94400 0x40 # 01000000   Q6
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw04-p4  (34 entries, util 26.5200 %)

```
sgs 20160 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 17280 0x7F # 01111111   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 1920 0x3F # 00111111   BE
sgs 53440 0x40 # 01000000   Q6
sgs 31360 0xBF # 10111111   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 16320 0x80 # 10000000   Q7
sgs 13440 0x7F # 01111111   Q6
sgs 38080 0xBF # 10111111   Q7
sgs 80640 0x40 # 01000000   Q6
sgs 31360 0xBF # 10111111   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 17280 0x7F # 01111111   Q6
sgs 24960 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 320 0x3F # 00111111   BE
sgs 67840 0x80 # 10000000   Q7
sgs 31360 0xBF # 10111111   Q7
sgs 20160 0x7F # 01111111   Q6
sgs 16320 0x80 # 10000000   Q7
sgs 13440 0x7F # 01111111   Q6
sgs 38080 0xBF # 10111111   Q7
sgs 60480 0x40 # 01000000   Q6
sgs 51520 0xBF # 10111111   Q7
```

### sw04-p5  (23 entries, util 23.4000 %)

```
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 15680 0x7F # 01111111   Q6
sgs 34240 0x80 # 10000000   Q7
sgs 12160 0x3F # 00111111   BE
sgs 66240 0x40 # 01000000   Q6
sgs 59200 0xBF # 10111111   Q7
sgs 15360 0x80 # 10000000   Q7
sgs 22400 0x7F # 01111111   Q6
sgs 36800 0xBF # 10111111   Q7
sgs 66240 0x40 # 01000000   Q6
sgs 59200 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 15680 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 33920 0xBF # 10111111   Q7
sgs 66240 0x40 # 01000000   Q6
sgs 59200 0xBF # 10111111   Q7
sgs 15360 0x80 # 10000000   Q7
sgs 22400 0x7F # 01111111   Q6
sgs 36800 0xBF # 10111111   Q7
sgs 54080 0x40 # 01000000   Q6
sgs 59200 0xBF # 10111111   Q7
```

### sw05-p4  (22 entries, util 35.8800 %)

```
sgs 24960 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 18240 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 19200 0xBF # 10111111   Q7
sgs 48640 0x80 # 10000000   Q7
sgs 14080 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 111040 0x40 # 01000000   Q6
sgs 14080 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 18240 0x7F # 01111111   Q6
sgs 80320 0x40 # 01000000   Q6
sgs 14080 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
sgs 24960 0x7F # 01111111   Q6
sgs 86080 0x40 # 01000000   Q6
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw05-p5  (25 entries, util 23.4000 %)

```
sgs 43200 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 15360 0xBF # 10111111   Q7
sgs 25280 0x80 # 10000000   Q7
sgs 2240 0x3F # 00111111   BE
sgs 29120 0x40 # 01000000   Q6
sgs 25920 0x7F # 01111111   Q6
sgs 41600 0x80 # 10000000   Q7
sgs 48000 0x7F # 01111111   Q6
sgs 37120 0x40 # 01000000   Q6
sgs 19840 0xBF # 10111111   Q7
sgs 28160 0x7F # 01111111   Q6
sgs 66880 0x40 # 01000000   Q6
sgs 48000 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 15360 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 15040 0xBF # 10111111   Q7
sgs 96640 0x40 # 01000000   Q6
sgs 48000 0x7F # 01111111   Q6
sgs 37120 0x40 # 01000000   Q6
sgs 19840 0xBF # 10111111   Q7
sgs 28160 0x7F # 01111111   Q6
sgs 23680 0x40 # 01000000   Q6
sgs 48000 0xBF # 10111111   Q7
```

### sw06-p4  (24 entries, util 23.4000 %)

```
sgs 18240 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 17280 0x7F # 01111111   Q6
sgs 31680 0x80 # 10000000   Q7
sgs 22400 0xBF # 10111111   Q7
sgs 56960 0x40 # 01000000   Q6
sgs 40960 0xBF # 10111111   Q7
sgs 18240 0x7F # 01111111   Q6
sgs 24640 0x80 # 10000000   Q7
sgs 59200 0xBF # 10111111   Q7
sgs 56960 0x40 # 01000000   Q6
sgs 40960 0xBF # 10111111   Q7
sgs 18240 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 17280 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 41600 0xBF # 10111111   Q7
sgs 56960 0x40 # 01000000   Q6
sgs 40960 0xBF # 10111111   Q7
sgs 18240 0x7F # 01111111   Q6
sgs 24640 0x80 # 10000000   Q7
sgs 59200 0xBF # 10111111   Q7
sgs 38720 0x40 # 01000000   Q6
sgs 59200 0xBF # 10111111   Q7
```

### sw06-p5  (32 entries, util 26.5200 %)

```
sgs 13440 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24000 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 1600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 1920 0x3F # 00111111   BE
sgs 54400 0x40 # 01000000   Q6
sgs 38080 0xBF # 10111111   Q7
sgs 13440 0x7F # 01111111   Q6
sgs 14080 0x80 # 10000000   Q7
sgs 22400 0x7F # 01111111   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 82880 0x40 # 01000000   Q6
sgs 38080 0xBF # 10111111   Q7
sgs 13440 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 24000 0x7F # 01111111   Q6
sgs 16640 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 1600 0x3F # 00111111   BE
sgs 68800 0x80 # 10000000   Q7
sgs 38080 0xBF # 10111111   Q7
sgs 13440 0x7F # 01111111   Q6
sgs 14080 0x80 # 10000000   Q7
sgs 22400 0x7F # 01111111   Q6
sgs 29120 0xBF # 10111111   Q7
sgs 69440 0x40 # 01000000   Q6
sgs 51520 0xBF # 10111111   Q7
```

### sw07-p4  (25 entries, util 23.4000 %)

```
sgs 37120 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 13760 0xBF # 10111111   Q7
sgs 27840 0x80 # 10000000   Q7
sgs 640 0x3F # 00111111   BE
sgs 30720 0x40 # 01000000   Q6
sgs 24320 0x7F # 01111111   Q6
sgs 42240 0x80 # 10000000   Q7
sgs 48000 0x7F # 01111111   Q6
sgs 37760 0x40 # 01000000   Q6
sgs 25280 0xBF # 10111111   Q7
sgs 22720 0x7F # 01111111   Q6
sgs 66240 0x40 # 01000000   Q6
sgs 48000 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 13760 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 16000 0xBF # 10111111   Q7
sgs 97280 0x40 # 01000000   Q6
sgs 48000 0x7F # 01111111   Q6
sgs 37760 0x40 # 01000000   Q6
sgs 25280 0xBF # 10111111   Q7
sgs 22720 0x7F # 01111111   Q6
sgs 29120 0x40 # 01000000   Q6
sgs 48000 0xBF # 10111111   Q7
```

### sw07-p5  (19 entries, util 35.8800 %)

```
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 16000 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 21440 0xBF # 10111111   Q7
sgs 48640 0x80 # 10000000   Q7
sgs 55680 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 111040 0x40 # 01000000   Q6
sgs 55680 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 16000 0xBF # 10111111   Q7
sgs 82560 0x40 # 01000000   Q6
sgs 55680 0xBF # 10111111   Q7
sgs 33280 0x7F # 01111111   Q6
sgs 77760 0x40 # 01000000   Q6
sgs 39040 0x7F # 01111111   Q6
sgs 49920 0xBF # 10111111   Q7
```

### sw08-p2  (28 entries, util 31.2000 %)

```
sgs 24320 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 4800 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 13760 0xBF # 10111111   Q7
sgs 12480 0x40 # 01000000   Q6
sgs 23680 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 8640 0x3F # 00111111   BE
sgs 48320 0x40 # 01000000   Q6
sgs 26560 0xBF # 10111111   Q7
sgs 24320 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 4800 0x3F # 00111111   BE
sgs 131840 0x40 # 01000000   Q6
sgs 26560 0xBF # 10111111   Q7
sgs 24320 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 4800 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 13760 0xBF # 10111111   Q7
sgs 105600 0x40 # 01000000   Q6
sgs 26560 0xBF # 10111111   Q7
sgs 24320 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 4800 0x3F # 00111111   BE
sgs 107520 0x40 # 01000000   Q6
sgs 50880 0xBF # 10111111   Q7
```

### sw08-p4  (29 entries, util 26.5200 %)

```
sgs 6720 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 39040 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 1600 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 1920 0x3F # 00111111   BE
sgs 55360 0x40 # 01000000   Q6
sgs 51520 0xBF # 10111111   Q7
sgs 13120 0x80 # 10000000   Q7
sgs 30080 0x7F # 01111111   Q6
sgs 21440 0xBF # 10111111   Q7
sgs 83840 0x40 # 01000000   Q6
sgs 51520 0xBF # 10111111   Q7
sgs 12480 0x80 # 10000000   Q7
sgs 39040 0x7F # 01111111   Q6
sgs 12480 0x80 # 10000000   Q7
sgs 640 0x3F # 00111111   BE
sgs 12480 0x40 # 01000000   Q6
sgs 1600 0x3F # 00111111   BE
sgs 69760 0x80 # 10000000   Q7
sgs 51520 0xBF # 10111111   Q7
sgs 13120 0x80 # 10000000   Q7
sgs 30080 0x7F # 01111111   Q6
sgs 21440 0xBF # 10111111   Q7
sgs 77120 0x40 # 01000000   Q6
sgs 51520 0xBF # 10111111   Q7
```

### sw08-p5  (28 entries, util 23.4000 %)

```
sgs 31040 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12160 0x3F # 00111111   BE
sgs 29120 0x80 # 10000000   Q7
sgs 320 0x3F # 00111111   BE
sgs 32320 0x40 # 01000000   Q6
sgs 22720 0x7F # 01111111   Q6
sgs 42880 0x80 # 10000000   Q7
sgs 16960 0xBF # 10111111   Q7
sgs 31040 0x7F # 01111111   Q6
sgs 38400 0x40 # 01000000   Q6
sgs 30720 0xBF # 10111111   Q7
sgs 17280 0x7F # 01111111   Q6
sgs 65600 0x40 # 01000000   Q6
sgs 16960 0xBF # 10111111   Q7
sgs 31040 0x7F # 01111111   Q6
sgs 12480 0x40 # 01000000   Q6
sgs 12160 0x3F # 00111111   BE
sgs 12480 0x80 # 10000000   Q7
sgs 16960 0xBF # 10111111   Q7
sgs 97920 0x40 # 01000000   Q6
sgs 16960 0xBF # 10111111   Q7
sgs 31040 0x7F # 01111111   Q6
sgs 38400 0x40 # 01000000   Q6
sgs 30720 0xBF # 10111111   Q7
sgs 17280 0x7F # 01111111   Q6
sgs 34560 0x40 # 01000000   Q6
sgs 48000 0xBF # 10111111   Q7
```

