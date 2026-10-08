# GCL update timing, 2026-10-08 13:56

Testbed: 8 TTTech switches, CNC S2 on sw08 via the management LAN. 20 repetitions per row; values are median (p5-p95) in ms. GCL per port: each port's own OperControlList (gates unchanged). TCP_NODELAY: on.

SSH session setup per switch (once, not part of any update): sw01 227, sw02 126, sw03 125, sw04 134, sw05 140, sw06 127, sw07 123, sw08 124 ms.

## Network update time

update = first command sent -> last port running the new GCL (its ConfigChangeTime). commands = first command sent -> last result back at the CNC. mixed = time old and new GCLs coexist in the network (last - first ConfigChangeTime). send / switch = sums over all ports of command-send time and exact on-switch time.

| topology | switches | ports | strategy | mode | update | commands | mixed | send (sum) | switch (sum) | live ports |
|---|---|---|---|---|---|---|---|---|---|---|
| 1-switch | 1 | 4 | sequential | immediate | 310.0 (303.2-349.0) | 314.0 (307.4-353.3) | 236.0 (228.8-263.2) | 52.1 (50.0-65.3) | 249.2 (243.6-274.7) | 80/80 |
| 1-switch | 1 | 4 | parallel | immediate | 341.4 (301.8-361.5) | 345.7 (305.0-366.1) | 260.4 (227.2-269.6) | 59.9 (50.7-66.8) | 268.9 (241.0-285.7) | 80/80 |
| 1-switch | 1 | 4 | batched | immediate | 262.6 (257.1-594.2) | 266.6 (262.1-599.1) | 187.6 (183.2-210.4) | 17.0 (16.0-17.5) | 247.1 (242.4-579.0) | 80/80 |
| line-4 | 4 | 8 | sequential | immediate | 651.7 (637.1-682.9) | 656.1 (642.0-687.3) | 570.8 (557.6-598.4) | 101.8 (99.8-105.4) | 528.2 (510.8-555.4) | 160/160 |
| line-4 | 4 | 8 | parallel | immediate | 175.1 (170.0-190.8) | 179.8 (174.5-194.4) | 99.6 (95.2-112.0) | 115.1 (107.7-121.4) | 517.9 (498.8-548.9) | 160/160 |
| line-4 | 4 | 8 | batched | immediate | 163.2 (152.8-183.7) | 169.1 (157.3-187.9) | 91.2 (79.2-104.8) | 68.4 (63.3-76.0) | 528.2 (502.2-554.6) | 160/160 |
| ring-4 | 4 | 9 | sequential | immediate | 714.4 (630.4-798.7) | 718.8 (634.0-803.0) | 629.6 (559.2-716.8) | 119.2 (112.3-125.0) | 567.3 (491.5-653.1) | 180/180 |
| ring-4 | 4 | 9 | parallel | immediate | 208.8 (195.2-232.5) | 213.2 (199.6-237.0) | 140.0 (129.6-161.6) | 123.3 (117.7-131.0) | 528.9 (500.9-553.0) | 180/180 |
| ring-4 | 4 | 9 | batched | immediate | 176.7 (169.7-207.0) | 181.8 (174.3-211.4) | 108.8 (103.2-143.2) | 63.8 (61.4-67.4) | 529.0 (496.5-560.2) | 180/180 |
| star-5 | 5 | 9 | sequential | immediate | 699.3 (677.7-822.6) | 704.4 (682.2-825.9) | 630.0 (609.6-752.8) | 115.5 (111.9-135.6) | 555.1 (536.3-693.7) | 180/180 |
| star-5 | 5 | 9 | parallel | immediate | 323.6 (305.4-368.3) | 327.8 (309.4-373.0) | 253.6 (235.2-302.4) | 136.6 (120.2-153.1) | 587.0 (553.2-781.8) | 180/180 |
| star-5 | 5 | 9 | batched | immediate | 266.3 (256.5-286.5) | 271.3 (260.6-292.2) | 194.8 (183.2-215.2) | 80.1 (75.2-96.1) | 562.8 (544.7-595.6) | 180/180 |
| grid-6 | 6 | 18 | sequential | immediate | 1418.3 (1371.1-1601.0) | 1422.4 (1375.9-1606.1) | 1349.6 (1307.2-1538.4) | 237.1 (229.4-246.8) | 1118.1 (1076.6-1294.0) | 360/360 |
| grid-6 | 6 | 18 | parallel | immediate | 320.6 (306.7-364.6) | 324.6 (310.9-370.7) | 248.0 (233.6-288.8) | 269.5 (254.3-304.8) | 1146.8 (1094.9-1247.4) | 360/360 |
| grid-6 | 6 | 18 | batched | immediate | 296.6 (262.3-308.4) | 302.4 (266.8-314.7) | 230.0 (196.0-246.4) | 110.5 (101.8-124.1) | 1120.6 (1074.6-1177.5) | 360/360 |
| mesh-8 | 8 | 27 | sequential | immediate | 2143.9 (2067.0-2228.0) | 2149.0 (2072.0-2232.2) | 2080.8 (2004.8-2164.0) | 355.4 (341.4-393.6) | 1687.7 (1632.5-1734.7) | 540/540 |
| mesh-8 | 8 | 27 | parallel | immediate | 346.2 (314.5-493.4) | 350.5 (317.9-497.4) | 281.2 (252.0-426.4) | 388.9 (340.0-443.9) | 1624.5 (1588.9-1809.1) | 540/540 |
| mesh-8 | 8 | 27 | batched | immediate | 275.9 (269.4-317.0) | 280.1 (273.9-321.5) | 209.6 (204.8-252.8) | 149.6 (138.6-163.7) | 1624.4 (1598.6-1700.6) | 540/540 |

## Per port: where the time goes

send = CNC issues the command -> the switch starts running it (channel open + exec request + shell start). switch = exact time on the switch: upload (write the list to a file) + `tsntool st wrcl` + `tsntool st configure`. activation = configure issued -> hardware runs the new list (ConfigChangeTime). return = result back at the CNC. Per-port send counts only the first port of a batched command.

| strategy | mode | send | chan open | exec req | shell start | upload | wrcl | configure | switch | activation | return | RTT |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| sequential | immediate | 12.67 | 1.35 | 2.61 | 8.69 | 46.99 | 6.86 | 7.33 | 61.51 | 6.50 | 3.18 | 77.80 |
| parallel | immediate | 14.09 | 1.89 | 2.80 | 8.61 | 46.22 | 6.89 | 7.77 | 60.85 | 6.55 | 3.37 | 79.34 |
| batched | immediate | 15.13 | 2.99 | 3.76 | 8.36 | 46.14 | 6.86 | 7.60 | 60.69 | 6.50 | 3.19 | 175.36 |
