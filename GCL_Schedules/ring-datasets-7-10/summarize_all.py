import json
from pathlib import Path

TASK = Path(__file__).resolve().parent
CONFIGURE = TASK.parents[1]
rows = []
links = []
for i in range(7, 11):
    root = CONFIGURE / f'GCL_Schedules/result-2026-10-12-dataset-testbed-{i}-ring-avgwin'
    reports = sorted(root.glob('TESTBED_RESULTS_*.md'))
    if not reports:
        raise SystemExit(f'Dataset {i}: no combined physical report')
    report = reports[-1]
    links.append(f'- [Dataset {i}]({report.relative_to(TASK.parent).as_posix()})')
    count = 0
    for line in report.read_text().splitlines():
        if line.startswith('| ') and len(line.split('|')) == 11:
            parts = [s.strip() for s in line.split('|')[1:-1]]
            if parts[0].isdigit():
                rows.append('| ' + str(i) + ' | ' + ' | '.join(parts[1:]) + ' |')
                count += 1
    if count != 10:
        raise SystemExit(f'Dataset {i}: only {count}/10 table rows')
text = '''# Ring datasets 7–10: physical benchmark comparison

Four distinct traffic draws (seeds 43–46), same eight-switch ring topology and hardware profile. Each dataset contains 20 initial flows and 30 additional flows. The previous scheduling pipeline was retained, including one million RL steps, C9 off/on, max overlay, three-frame minimum windows, average-size new windows, and per-instance admission.

Forty schedule packages were deployed sequentially. Each package was checked for live GCLs, admitted with VLAN/MSTP configuration, checked for spanning-tree quiet and route connectivity, and measured with 30 seconds of traffic on all end stations.

The existing admission latency-report validation limitations remain; see each result directory's `validation.json` and package `independent-verification.log`. Physical measurements are single trials, not proof of deadline guarantees.

| Dataset | Package | Scheduled / offered | Sent | Received | Lost | Deadline misses (%) | Latency min / avg / max (µs) | Jitter best / avg / worst (µs) |
|---|---|---|---|---|---|---|---|---|
''' + '\n'.join(rows) + '\n\nFull dataset reports:\n\n' + '\n'.join(links) + '\n'
# Links are relative to this file, which sits one directory beneath GCL_Schedules.
text = text.replace('](result-', '](../result-')
(TASK / 'BENCHMARK_RESULTS.md').write_text(text)
print(TASK / 'BENCHMARK_RESULTS.md')
