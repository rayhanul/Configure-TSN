# GCL update timing, 2026-10-08 14:02

Testbed: 8 TTTech switches, CNC S2 on sw08 via the management LAN. 20 repetitions per row; values are median (p5-p95) in ms. GCL per port: each port's own OperControlList (gates unchanged). TCP_NODELAY: off.

SSH session setup per switch (once, not part of any update): sw01 236, sw02 158, sw03 161, sw04 139, sw05 129, sw06 127, sw07 120, sw08 125 ms.

## Network update time

update = first command sent -> last port running the new GCL (its ConfigChangeTime). commands = first command sent -> last result back at the CNC. mixed = time old and new GCLs coexist in the network (last - first ConfigChangeTime). send / switch = sums over all ports of command-send time and exact on-switch time.

| topology | switches | ports | strategy | mode | update | commands | mixed | send (sum) | switch (sum) | live ports |
|---|---|---|---|---|---|---|---|---|---|---|
| 1-switch | 1 | 4 | sequential | immediate | 389.0 (337.4-398.7) | 393.0 (340.7-402.4) | 312.0 (261.6-322.4) | 131.6 (88.9-133.0) | 248.1 (240.4-256.9) | 80/80 |
| 1-switch | 1 | 4 | parallel | immediate | 388.9 (375.7-410.6) | 393.5 (379.8-415.5) | 312.8 (305.6-339.2) | 131.4 (129.1-133.2) | 248.2 (236.9-267.2) | 80/80 |
| 1-switch | 1 | 4 | batched | immediate | 264.6 (256.8-291.7) | 268.9 (261.1-296.1) | 189.2 (184.0-208.8) | 16.9 (15.7-19.4) | 248.0 (241.3-274.6) | 80/80 |
| line-4 | 4 | 8 | sequential | immediate | 762.4 (707.7-827.2) | 765.8 (712.6-832.0) | 679.6 (632.8-748.8) | 226.0 (188.7-238.3) | 524.4 (459.8-571.6) | 160/160 |
| line-4 | 4 | 8 | parallel | immediate | 205.9 (195.3-343.4) | 210.4 (199.8-347.1) | 134.4 (127.2-274.4) | 231.4 (221.6-236.4) | 477.5 (457.8-615.0) | 160/160 |
| line-4 | 4 | 8 | batched | immediate | 141.4 (137.5-172.8) | 146.9 (142.4-176.9) | 74.8 (64.8-106.4) | 65.0 (59.6-68.2) | 476.2 (461.4-542.8) | 160/160 |
| ring-4 | 4 | 9 | sequential | immediate | 889.2 (828.2-1001.1) | 894.1 (833.2-1005.4) | 813.6 (755.2-907.2) | 281.6 (239.5-291.7) | 578.6 (533.9-680.5) | 180/180 |
| ring-4 | 4 | 9 | parallel | immediate | 243.5 (231.3-260.9) | 248.0 (235.9-266.0) | 175.2 (156.8-189.6) | 287.4 (248.3-291.9) | 554.4 (524.5-579.5) | 180/180 |
| ring-4 | 4 | 9 | batched | immediate | 178.5 (168.5-205.7) | 182.5 (174.0-210.8) | 108.8 (101.6-132.8) | 64.1 (58.9-70.7) | 530.9 (506.9-589.6) | 180/180 |
| star-5 | 5 | 9 | sequential | immediate | 809.4 (777.3-975.8) | 813.0 (782.2-980.9) | 735.6 (706.4-786.4) | 235.2 (194.8-240.2) | 559.5 (544.1-713.0) | 180/180 |
| star-5 | 5 | 9 | parallel | immediate | 354.5 (343.6-526.2) | 358.3 (347.3-530.0) | 281.6 (272.0-448.8) | 210.6 (204.3-221.9) | 578.1 (553.8-757.6) | 180/180 |
| star-5 | 5 | 9 | batched | immediate | 290.7 (265.2-303.4) | 294.5 (269.5-307.1) | 215.2 (187.2-228.8) | 84.3 (71.7-102.7) | 606.3 (574.0-693.3) | 180/180 |
| grid-6 | 6 | 18 | sequential | immediate | 1704.2 (1646.9-1835.4) | 1708.5 (1650.9-1839.9) | 1638.8 (1572.8-1772.8) | 521.9 (508.6-549.3) | 1111.6 (1080.9-1262.0) | 360/360 |
| grid-6 | 6 | 18 | parallel | immediate | 394.4 (385.5-516.4) | 398.7 (390.8-522.3) | 324.0 (318.4-451.2) | 535.6 (514.8-570.7) | 1128.8 (1064.4-1312.2) | 360/360 |
| grid-6 | 6 | 18 | batched | immediate | 302.9 (264.6-463.5) | 307.6 (270.2-468.4) | 234.8 (190.4-388.0) | 114.2 (109.2-136.4) | 1168.1 (1104.6-1373.9) | 360/360 |
| mesh-8 | 8 | 27 | sequential | immediate | 2578.2 (2523.8-2754.7) | 2582.0 (2528.5-2761.0) | 2514.8 (2461.6-2688.0) | 759.3 (706.1-820.4) | 1716.2 (1667.0-1883.2) | 540/540 |
| mesh-8 | 8 | 27 | parallel | immediate | 415.9 (377.2-454.4) | 420.4 (381.8-461.2) | 351.2 (312.8-388.0) | 742.8 (691.5-831.7) | 1669.7 (1617.6-1724.3) | 540/540 |
| mesh-8 | 8 | 27 | batched | immediate | 293.6 (281.3-318.5) | 298.9 (285.4-321.9) | 227.6 (216.0-249.6) | 152.6 (101.7-170.2) | 1649.1 (1600.0-1708.1) | 540/540 |

## Per port: where the time goes

send = CNC issues the command -> the switch starts running it (channel open + exec request + shell start). switch = exact time on the switch: upload (write the list to a file) + `tsntool st wrcl` + `tsntool st configure`. activation = configure issued -> hardware runs the new list (ConfigChangeTime). return = result back at the CNC. Per-port send counts only the first port of a batched command.

| strategy | mode | send | chan open | exec req | shell start | upload | wrcl | configure | switch | activation | return | RTT |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| sequential | immediate | 13.52 | 1.58 | 2.65 | 8.72 | 47.43 | 6.87 | 7.39 | 62.04 | 6.51 | 3.22 | 86.97 |
| parallel | immediate | 15.88 | 3.67 | 2.72 | 8.66 | 46.42 | 6.87 | 7.30 | 60.86 | 6.49 | 3.29 | 86.66 |
| batched | immediate | 15.41 | 3.04 | 3.57 | 8.57 | 46.96 | 6.87 | 7.98 | 61.51 | 6.57 | 3.26 | 176.33 |
