import json
from pathlib import Path

TASK = Path(__file__).resolve().parent
CONFIGURE = TASK.parents[1]
rows = []
links = []
validation = []
# Datasets 4 and 5 ran on the same tree topology earlier, before validation.json existed.
EARLIER = {4: 'result-2026-10-10-dataset-testbed-4-saf', 5: 'result-2026-10-10-dataset-testbed-5-avgwin'}
for i in [4, 5, 11, 12, 13]:
    root = CONFIGURE / 'GCL_Schedules' / EARLIER.get(i, f'result-2026-10-13-dataset-testbed-{i}-tree-avgwin')
    reports = sorted(root.glob('TESTBED_RESULTS_*.md'))
    if not reports:
        raise SystemExit(f'Dataset {i}: no combined physical report')
    report = reports[-1]
    if i in EARLIER:
        links.append(f'- [Dataset {i}]({report.relative_to(TASK.parent).as_posix()})')
        count = 0
        for line in report.read_text().splitlines():
            parts = [s.strip() for s in line.split('|')[1:-1]]
            if len(parts) == 9 and parts[0].isdigit():
                rows.append('| ' + str(i) + ' | ' + ' | '.join(parts[1:]) + ' |')
                count += 1
        if count != 10:
            raise SystemExit(f'Dataset {i}: only {count}/10 table rows')
        continue
    checks = json.loads((root / 'validation.json').read_text())
    if len(checks) != 10:
        raise SystemExit(f'Dataset {i}: expected ten validation records')
    validation.extend(checks)
    note = "Independent export validation is recorded in [validation.json](validation.json) and each package's `independent-verification.log`. Admission latency-report consistency failures remain; measured delivery does not establish deadline guarantees."
    content = report.read_text()
    if note not in content:
        lines = content.splitlines()
        lines.insert(2, note + '\n')
        report.write_text('\n'.join(lines) + '\n')
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
text = '''# Tree datasets 4, 5, 11–13: physical benchmark comparison

Five distinct traffic draws (datasets 4 and 5 run 2026-10-10/11; 11–13 with seeds 47–49 run 2026-10-13), same eight-switch tree topology and hardware profile. Each dataset contains 20 initial flows and 30 additional flows. The previous scheduling pipeline was retained, including one million RL steps, C9 off/on, max overlay, three-frame minimum windows, average-size new windows, and per-instance admission.

Fifty schedule packages were deployed sequentially. Each package was checked for live GCLs, admitted with VLAN/MSTP configuration, checked for spanning-tree quiet and route connectivity, and measured with 30 seconds of traffic on all end stations.

The existing admission latency-report validation limitations remain; see each result directory's `validation.json` and package `independent-verification.log`. Physical measurements are single trials, not proof of deadline guarantees.

| Dataset | Package | Scheduled / offered | Sent | Received | Lost | Deadline misses (%) | Latency min / avg / max (µs) | Jitter best / avg / worst (µs) |
|---|---|---|---|---|---|---|---|---|
''' + '\n'.join(rows) + '\n\nFull dataset reports:\n\n' + '\n'.join(links) + '\n'
# Links are relative to this file, which sits one directory beneath GCL_Schedules.
text = text.replace('](result-', '](../result-')
passed = sum(v['independent-verification'] == 0 for v in validation)
replay = sum(v['hardware-replay'] == 0 for v in validation)
text = text.replace('The existing admission latency-report validation limitations remain;',
    f'For datasets 11–13, hardware replay passed for {replay}/30 packages; independent export validation passed for {passed}/30. The existing admission latency-report validation limitations remain;')
state = TASK / 'deployment-state.json'
if state.exists():
    active = json.loads(state.read_text())
    matches = sum(v['matches_package'] for v in active['operational_readback'])
    final_rows = [row for row in rows if row.startswith('| 13 | Problem 3 RL C9-on |')]
    if len(final_rows) != 1:
        raise SystemExit('Missing final active package measurement')
    parts = [s.strip() for s in final_rows[0].split('|')[1:-1]]
    summary = (f"Active final package: dataset 13, Problem 3 RL C9-on, {active['scheduled_flows']} scheduled flows; "
        f"{matches}/17 operational GCLs matched the exported schedule. Final 30-second trial: "
        f"{parts[4]} received of {parts[3]} sent, {parts[5]} lost, deadline misses {parts[6]}. "
        "See [deployment-state.json](deployment-state.json).\n\n")
    text = text.replace('Five distinct traffic draws', summary + 'Five distinct traffic draws')
(TASK / 'BENCHMARK_RESULTS.md').write_text(text)
print(TASK / 'BENCHMARK_RESULTS.md')
