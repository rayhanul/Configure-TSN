"""Rerun datasets 11 and 12 with longer MSTP settling and verified connectivity."""
import datetime
import getpass
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

TASK = Path(__file__).resolve().parent
REPO = TASK.parents[1]
GROUPS = ['smt-c9-off', 'smt-c9-on', 'heuristic-c9-off', 'heuristic-c9-on',
          'rl-c9-off', 'rl-c9-on', 'prob3-heuristic-c9-off', 'prob3-heuristic-c9-on',
          'prob3-rl-c9-off', 'prob3-rl-c9-on']


def status(message):
    line = datetime.datetime.now().isoformat(timespec='seconds') + ' ' + message
    print(line, flush=True)
    with (TASK / 'progress.log').open('a') as fh:
        fh.write(line + '\n')


def main():
    sys.path.insert(0, str(REPO / 'Network-Configure-Manager'))
    import configureManager as cm
    source = REPO.parent / 'RL-TSN/data/dataset-testbed/network-topology-rtas-2027-tree.json'
    topo = json.loads(source.read_text())
    s3 = os.environ.get('S3_PW') or getpass.getpass('S3 sudo password: ')
    s1 = os.environ.get('S1_PW') or topo['S1'].get('password', '')
    if s1 in ('PROMPT', 'ASK', ''):
        s1 = getpass.getpass('S1 sudo password: ')
    client = cm.ssh_connect(topo['S3']['ip'], topo['S3']['username'], s3)
    stdin, out, err = client.exec_command("sudo -S -p '' true", timeout=15)
    stdin.write(s3 + '\n'); stdin.flush(); stdin.channel.shutdown_write()
    error = err.read().decode(); rc = out.channel.recv_exit_status(); client.close()
    if rc:
        raise RuntimeError('S3 authentication failed')
    ids = [int(value) for value in os.environ.get('DATASET_IDS', '11,12').split(',')]
    suffix = os.environ.get('RERUN_SUFFIX', 'tree-quiet60')
    for i in ids:
        original = REPO / f'GCL_Schedules/result-2026-10-13-dataset-testbed-{i}-tree-avgwin'
        dest = REPO / f'GCL_Schedules/rerun-dataset-{i}-{suffix}'
        dest.mkdir(exist_ok=True)
        for group in GROUPS:
            for pkg in (original / group).iterdir():
                if not (pkg / 'schedule.json').exists():
                    continue
                target = dest / group / pkg.name
                target.mkdir(parents=True, exist_ok=True)
                if not (target / 'schedule.json').exists():
                    for file in pkg.iterdir():
                        if file.is_file() and file.name not in ('basetime.json', 'endpoints.json', 'stream-realizable.csv'):
                            shutil.copy2(file, target / file.name)
                    shutil.copytree(pkg / 'gcl', target / 'gcl')
        for name in ('physical-topology.json', 'validation.json', 'run_config.env'):
            shutil.copy2(original / name, dest / name)
        shutil.copy2(original / 'TESTBED_RESULTS_2026-10-13.md', dest / 'ORIGINAL_TESTBED_RESULTS.md')
        env = dict(os.environ, S1_PW=s1, S2_PW='', S3_PW=s3,
                   TOPO=str(dest / 'physical-topology.json'), TASK_ROOT=str(TASK),
                   STP_QUIET='60', DURATION='30', TZ='America/New_York',
                   PYTHONDONTWRITEBYTECODE='1', PYTHONUNBUFFERED='1')
        pending = [group for group in GROUPS if not list((dest / group).glob('*/results/*/results.md'))]
        if not pending:
            status(f'Dataset {i}: all ten reruns already complete')
            continue
        status(f'Dataset {i}: {len(pending)} pending sequential reruns starting; quiet=60s, traffic=30s')
        with (dest / 'benchmark-console.log').open('a') as log:
            r = subprocess.run(['bash', str(TASK / 'run_testbed_batched.sh'), str(dest), *pending],
                               cwd=REPO, env=env, stdout=log, stderr=subprocess.STDOUT)
        count = len(list(dest.glob('*/*/results/*/results.md')))
        if r.returncode or count != 10:
            raise RuntimeError(f'Dataset {i}: incomplete rerun ({count}/10 reports, rc={r.returncode})')
        status(f'Dataset {i}: all ten reruns complete')
    status(f'COMPLETE: datasets {ids} reruns complete; last package remains active')


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        status('FAILED: ' + str(exc))
        raise
