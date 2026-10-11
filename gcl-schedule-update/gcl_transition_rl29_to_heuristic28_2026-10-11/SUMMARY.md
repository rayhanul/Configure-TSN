# RL29 → heuristic28: GCL transition under continuous traffic

Three 30-second trials on S1, S2 and S3. All 29 current TT flows kept their RL send offsets, queue priorities, VLANs, endpoints and MSTP routes throughout each trial. At about +10 seconds, the CNC sent the Problem 3 heuristic C9-on GCL to all 17 affected ports of sw01–sw08, sequentially. All 17 ports activated in every trial. Original RL GCLs were restored after traffic stopped in each trial.

Before = traffic start to first GCL command; during = first command to last hardware ConfigChangeTime; after = the remainder. A lost packet is a sender-log entry with no matching receiver entry (flow ID + launch time). Received late packets are deadline misses, separately from loss.

| Trial | Update (ms) | Before lost / sent | During lost / sent | After lost / sent | Deadline misses before / during / after |
|---|---:|---:|---:|---:|---:|
| 1 | 1573.80 | 0 / 730,558 | 0 / 114,095 | 4 / 1,330,203 | 0 / 8,338 / 91,738 |
| 2 | 1694.82 | 0 / 730,140 | 0 / 122,863 | 0 / 1,321,955 | 0 / 9,021 / 91,164 |
| 3 | 1605.39 | 0 / 729,873 | 0 / 116,322 | 0 / 1,328,678 | 0 / 8,600 / 91,626 |

| Phase (all trials) | Sent | Lost | Loss % | Deadline misses | Switch queue drops |
|---|---:|---:|---:|---:|---:|
| before | 2,190,571 | 0 | 0.000000 | 0 | 0 |
| during update 1 | 353,280 | 0 | 0.000000 | 25,959 | 0 |
| after update 1 | 3,980,836 | 4 | 0.000100 | 274,528 | 0 |

## Affected switches

Packet columns below are end-to-end losses for flows whose route crosses that switch, classified by packet launch time. They overlap across switches and must not be summed or interpreted as identifying the switch that dropped a packet. Queue-drop columns are actual per-port hardware counter increases, summed within each switch.

| Switch | Ports | Routed flows | Activation window ms, median (min–max) | Before lost / sent | Network-transition lost / sent | Own-activation lost / sent | Queue drops before / during / after |
|---|---:|---:|---:|---:|---:|---:|---:|
| sw01 | 2 | 23 | 176.59 (176.20–190.82) | 0 / 1,661,814 | 0 / 268,016 | 0 / 29,883 | 0 / 0 / 0 |
| sw02 | 2 | 17 | 191.90 (190.37–219.54) | 0 / 1,208,552 | 0 / 194,885 | 0 / 23,995 | 0 / 0 / 0 |
| sw03 | 2 | 23 | 195.18 (189.61–203.73) | 0 / 1,661,814 | 0 / 268,016 | 0 / 32,354 | 0 / 0 / 0 |
| sw04 | 2 | 17 | 208.00 (161.30–230.08) | 0 / 1,208,552 | 0 / 194,885 | 0 / 23,960 | 0 / 0 / 0 |
| sw05 | 2 | 23 | 193.25 (190.22–207.57) | 0 / 1,661,814 | 0 / 268,016 | 0 / 32,483 | 0 / 0 / 0 |
| sw06 | 2 | 17 | 211.51 (188.30–219.04) | 0 / 1,208,552 | 0 / 194,885 | 0 / 24,737 | 0 / 0 / 0 |
| sw07 | 2 | 23 | 212.60 (207.15–219.10) | 0 / 1,661,814 | 0 / 268,016 | 0 / 35,114 | 0 / 0 / 0 |
| sw08 | 3 | 29 | 202.10 (183.85–229.98) | 0 / 2,190,571 | 0 / 353,280 | 0 / 44,625 | 0 / 0 / 0 |

Queue counters are sampled near phase boundaries, with each read bracketed by switch-clock timestamps saved in updates.json. Sampling adds overhead to the measured network transition. Queue counters include all traffic on the affected ports.

The target package does not admit these current RL flow IDs: [7, 8, 15, 38]. They continued transmitting as requested. Target GCLs and unchanged RL sender timing are a different steady state from deploying the heuristic package with its own flow selection and transmit offsets; after-phase deadline misses must be assessed separately from packet loss during activation.

## Sender continuity

Generators remained running through each update. Late host wakeups caused some scheduled releases to be skipped before socket submission. These are not included in sent-packet loss. Counts below are inferred from gaps between recorded launch times and exclude any skips before a flow's first or after its last logged send.

| Trial | Skipped releases before | During | After |
|---|---:|---:|---:|
| 1 | 120 | 0 | 24 |
| 2 | 0 | 4 | 38 |
| 3 | 23 | 60 | 44 |

Final live readback verified that all 17 ports match the initial RL GCLs and cycle times. No generator remains running on S1, S2 or S3. Evidence: final_gcl_snapshot.json and final_verification.json.

## Flows with loss or missed deadlines

| Flow | Admitted by target | Before lost / misses | During lost / misses | After lost / misses |
|---|---|---:|---:|---:|
| 7 | no | 0 / 0 | 0 / 10,826 | 0 / 137,264 |
| 8 | no | 0 / 0 | 0 / 15,133 | 1 / 137,264 |
| 12 | yes | 0 / 0 | 0 / 0 | 1 / 0 |
| 31 | yes | 0 / 0 | 0 / 0 | 1 / 0 |
| 43 | yes | 0 / 0 | 0 / 0 | 1 / 0 |

Host counter changes per run (receive-buffer errors and ETF drops; ETF may also count non-test control packets):

```json
[
  {
    "S1": {
      "rcvbuf": 0,
      "etf": 1
    },
    "S2": {
      "rcvbuf": 0,
      "etf": 0
    },
    "S3": {
      "rcvbuf": 0,
      "etf": 18
    }
  },
  {
    "S1": {
      "rcvbuf": 0,
      "etf": 1
    },
    "S2": {
      "rcvbuf": 0,
      "etf": 0
    },
    "S3": {
      "rcvbuf": 0,
      "etf": 15
    }
  },
  {
    "S1": {
      "rcvbuf": 0,
      "etf": 1
    },
    "S2": {
      "rcvbuf": 0,
      "etf": 0
    },
    "S3": {
      "rcvbuf": 0,
      "etf": 16
    }
  }
]
```

Raw run summaries and packet logs:

- Trial 1: [update-loss-2026-10-11](../../GCL_Schedules/result-2026-10-10-dataset-testbed-5-avgwin/prob3-rl-c9-on/5-rl-c9on-matrix/results/update-loss-2026-10-11/summary.md).
- Trial 2: [update-loss-2026-10-11_2](../../GCL_Schedules/result-2026-10-10-dataset-testbed-5-avgwin/prob3-rl-c9-on/5-rl-c9on-matrix/results/update-loss-2026-10-11_2/summary.md).
- Trial 3: [update-loss-2026-10-11_3](../../GCL_Schedules/result-2026-10-10-dataset-testbed-5-avgwin/prob3-rl-c9-on/5-rl-c9on-matrix/results/update-loss-2026-10-11_3/summary.md).

Machine-readable phase, switch and flow tables: phases.csv, switches.csv, flows.csv. Exact per-port activation timestamps: each run's ports.csv.
