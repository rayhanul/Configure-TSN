"""Compare every original trial with its single measured rerun."""
import hashlib
import json
from pathlib import Path
import sys

TASK = Path(__file__).resolve().parent
REPO = TASK.parents[1]
sys.path.insert(0, str(REPO / 'GCL_Schedules'))
import summarize_testbed as summary


def stats(pkg):
    reports = list(pkg.glob('results/results-*/results.md'))
    if len(reports) != 1:
        raise RuntimeError(f'{pkg}: expected exactly one measured trial, found {len(reports)}')
    return summary.package_stats(str(pkg), str(reports[0]))


def main():
    rows, totals, records = [], [], []
    for i in (11, 12):
        old = REPO / f'GCL_Schedules/result-2026-10-13-dataset-testbed-{i}-tree-avgwin'
        new = REPO / f'GCL_Schedules/rerun-dataset-{i}-tree-quiet60'
        final = REPO / f'GCL_Schedules/rerun-dataset-{i}-tree-rstp-settled'
        if final.exists():
            new = final
        aggregate = {kind: dict(sent=0, rx=0, lost=0, misses=0, zero_miss=0) for kind in ('original', 'rerun')}
        for group in summary.ORDER:
            packages = list((old / group).glob('*/schedule.json'))
            if len(packages) != 1:
                raise RuntimeError(f'{i}/{group}: ambiguous package')
            original = packages[0].parent
            rerun = new / group / original.name
            hashes = {}
            for file in [original / 'schedule.json', *sorted((original / 'gcl').glob('*.cfg'))]:
                relative = file.relative_to(original)
                if file.read_bytes() != (rerun / relative).read_bytes():
                    raise RuntimeError(f'{i}/{group}/{relative}: schedule changed')
                hashes[str(relative)] = hashlib.sha256(file.read_bytes()).hexdigest()
            a, b = stats(original), stats(rerun)
            for kind, s in (('original', a), ('rerun', b)):
                aggregate[kind]['sent'] += s['sent']
                aggregate[kind]['rx'] += s['rx']
                aggregate[kind]['lost'] += s['sent'] - s['rx']
                aggregate[kind]['misses'] += s['miss']
                aggregate[kind]['zero_miss'] += int(s['miss'] == 0)
            log = new / 'testbed-logs' / f'{group}_{original.name}.log'
            protocol = 'RSTP / CIST' if 'setforcevers br0 rstp' in log.read_text() else 'MSTP / CIST'
            settling = 60 if 'Hardware settling: waiting 60 seconds' in log.read_text() else 0
            records.append(dict(dataset=i, group=group, protocol=protocol, minimum_hardware_settling_seconds=settling, original=a, rerun=b, unchanged_file_sha256=hashes))
            rows.append(f"| {i} | {summary.label(group)} | {b['admitted']} | {protocol} | {a['sent']-a['rx']:,} → {b['sent']-b['rx']:,} | {a['miss']:,} → {b['miss']:,} | {b['ping']} | {b['lmax']:.1f} |")
        for kind in ('original', 'rerun'):
            s = aggregate[kind]
            totals.append(f"| {i} | {kind} | {s['sent']:,} | {s['rx']:,} | {s['lost']:,} | {s['misses']:,} | {s['zero_miss']} / 10 |")
    text = '''# Tree datasets 11 and 12: rerun comparison

Each final package received a 30-second trial after successful connectivity checks and 60 seconds of spanning-tree quiet. Schedules, admitted flows, GCL entries and traffic settings are unchanged; their hashes are recorded in comparison.json. The physical forwarding configuration maps traffic VLANs to CIST and uses RSTP, appropriate for this connected tree. Dataset 11 was rerun in full after this final configuration was established; its earlier intermediate trials are preserved in rerun-dataset-11-tree-quiet60. A minimum 60-second hardware-settling delay was added from dataset 12 heuristic C9-off onward and applies to the final dataset 11 pass. The first two dataset 12 trials used the quiet check without that minimum elapsed delay. These settings are recorded in comparison.json. See [ROOT_CAUSE.md](ROOT_CAUSE.md).

Original and intermediate measurements are preserved. Final trials were chosen by the documented configuration pass, never by measured performance. These are single trials, not a statistical guarantee. The existing admission export latency-report validation failures remain.

| Dataset | Trial | Sent | Received | Lost | Deadline misses | Packages with zero misses |
|---|---|---|---|---|---|---|
''' + '\n'.join(totals) + '''

| Dataset | Approach | Scheduled flows | Forwarding protocol | Lost: original → rerun | Misses: original → rerun | Rerun route pings | Rerun max latency (µs) |
|---|---|---|---|---|---|---|---|
''' + '\n'.join(rows) + '''

Hardware replay passes for 20/20 final packages. Independent export verification passes for 12/20; all eight admission exports retain the documented latency-report consistency failures.

Full measurement reports:

- [Dataset 11 final confirmation](../rerun-dataset-11-tree-rstp-settled/TESTBED_RESULTS_2026-10-13.md)
- [Dataset 12 rerun](../rerun-dataset-12-tree-quiet60/TESTBED_RESULTS_2026-10-13.md)
- [Dataset 11 intermediate trials](../rerun-dataset-11-tree-quiet60/TESTBED_RESULTS_2026-10-13.md)
- [Comparison data and unchanged schedule hashes](comparison.json)
'''
    state_file = TASK / 'deployment-state.json'
    if state_file.exists():
        state = json.loads(state_file.read_text())
        checked = sum(v['matches_package'] and v['forwarding'] for v in state['operational_readback'])
        text += (f"\nActive package: dataset 11 RL admission C9-on, {state['scheduled_flows']} flows; "
                 f"{checked}/17 operational GCLs match and ports are forwarding. "
                 "See [deployment-state.json](deployment-state.json).\n")
    (TASK / 'comparison.json').write_text(json.dumps(records, indent=2) + '\n')
    (TASK / 'RERUN_RESULTS.md').write_text(text)
    print(text)


if __name__ == '__main__':
    main()
