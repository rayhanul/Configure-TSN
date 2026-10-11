# Dataset 5 physical testbed deployment

Status: COMPLETE. All ten packages deployed on 17/17 ports and measured for 30 seconds each. Full summary: SUMMARY_REPORT_2026-10-11.md; per-flow results: TESTBED_RESULTS_2026-10-11.md. Final active package: prob3-rl-c9-on/5-rl-c9on-matrix.

All ten deployment schedule.json files match the RL-TSN source result files byte for byte. All ten packages passed deploy-GCL/check_schedule.py hardware replay at processing delays of 2100, 3000, and 4020 ns. Every schedule uses store_and_forward=true, including C9-on.

| Group | Scheduled flows | Hardware replay |
|---|---:|---|
| SMT C9-off | 10 | PASS |
| SMT C9-on | 10 | PASS |
| Heuristic C9-off | 10 | PASS |
| Heuristic C9-on | 10 | PASS |
| RL C9-off | 10 | PASS |
| RL C9-on | 10 | PASS |
| Problem 3 heuristic C9-off | 24 | PASS |
| Problem 3 heuristic C9-on | 28 | PASS |
| Problem 3 RL C9-off | 25 | PASS |
| Problem 3 RL C9-on | 29 | PASS |

S1 and S2 sudo checks passed. S3 SSH access works. Its original configured sudo credential failed; a session-only credential supplied by the user passed the sudo check. PTP services are active on all three hosts; ETF queues use 600000 ns delta, and socket priorities 5 and 7 map to the same launch-time queue. No traffic generator was running on any host during preflight.

All ten per-flow measurements and the combined final summary are saved.

The prepared run_testbed.py checks sudo access before invoking the established GCL_Schedules/run_testbed.sh workflow. Once S3 sudo access is available, run:

```bash
python3 GCL_Schedules/result-2026-10-10-dataset-testbed-5-avgwin/run_testbed.py
```

This deploys all ten packages sequentially, admits their VLAN/MSTP flows, waits for spanning-tree stability, pings routes, and sends 30 seconds of hardware-timed traffic per package. Logs go to testbed_driver.log and testbed-logs/. The established workflow generates TESTBED_RESULTS_<date>.md from collected per-flow results.
