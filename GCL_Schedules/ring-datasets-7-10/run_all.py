"""Solve four ring datasets, validate exports, then benchmark forty packages."""
import concurrent.futures
import csv
import datetime
import getpass
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

TASK = Path(__file__).resolve().parent
CONFIGURE = TASK.parents[1]
RL = CONFIGURE.parent / 'RL-TSN'
TOPO = RL / 'data/dataset-testbed/network-topology-rtas-2027-ring.json'
IDS = [7, 8, 9, 10]
GROUPS = ['smt-c9-off', 'smt-c9-on', 'heuristic-c9-off', 'heuristic-c9-on', 'rl-c9-off', 'rl-c9-on', 'prob3-heuristic-c9-off', 'prob3-heuristic-c9-on', 'prob3-rl-c9-off', 'prob3-rl-c9-on']

def tag(i):
    return f'2026-10-12-dataset-testbed-{i}-ring-avgwin'

def status(message):
    print(datetime.datetime.now().isoformat(timespec='seconds'), message, flush=True)
    with (TASK / 'progress.log').open('a') as fh:
        fh.write(datetime.datetime.now().isoformat(timespec='seconds') + ' ' + message + '\n')

def solve(i):
    status(f'Dataset {i}: solving started')
    env = dict(os.environ, THREADS_PER_JOB='1', TZ='America/New_York', PYTHONDONTWRITEBYTECODE='1')
    with (RL / f'logs/run_{tag(i)}.log').open('w') as log:
        r = subprocess.run(['bash', 'scripts/run_matrix_2026-09-30_testbed-minwin3-pip-avgwin-smt1h-rl1M.sh', tag(i), str(i), str(i)], cwd=RL, env=env, stdout=log, stderr=subprocess.STDOUT)
    root = RL / f'result/result-{tag(i)}'
    packages = sorted(root.glob('*/*/schedule.json'))
    if r.returncode or len(packages) != 10:
        raise RuntimeError(f'Dataset {i}: pipeline failed/incomplete ({len(packages)}/10 exports, rc={r.returncode})')
    rows = list(csv.reader((root / f'matrix_rows/{i}.csv').open()))
    if len(rows) != 6 or any(len(row) != 5 or not row[3].isdigit() for row in rows):
        raise RuntimeError(f'Dataset {i}: missing scheduling/admission result: {rows}')
    validation = []
    for schedule in packages:
        pkg = schedule.parent
        outcomes = {}
        for name, cmd in [
            ('independent-verification', ['python3', str(RL / 'verify.py'), '--out', str(pkg)]),
            ('hardware-replay', ['python3', str(CONFIGURE / 'deploy-GCL/check_schedule.py'), '--pkg', str(pkg), '--guard-ns', '12400']),
        ]:
            r = subprocess.run(cmd, cwd=RL, capture_output=True, text=True, env=env)
            (pkg / f'{name}.log').write_text(r.stdout + r.stderr)
            outcomes[name] = r.returncode
        validation.append({'package': str(pkg.relative_to(root)), **outcomes})
    (root / 'validation.json').write_text(json.dumps(validation, indent=2) + '\n')
    status(f'Dataset {i}: all ten exports complete and validation recorded')
    return root

def main():
    sys.path.insert(0, str(CONFIGURE / 'Network-Configure-Manager'))
    import configureManager as cm
    topo = json.loads(TOPO.read_text())
    secret = os.environ.get('S3_PW') or getpass.getpass('S3 sudo password: ')
    s1_secret = os.environ.get('S1_PW') or getpass.getpass('S1 sudo password: ')
    v = topo['S3']
    client = cm.ssh_connect(v['ip'], v['username'], secret)
    stdin, stdout, stderr = client.exec_command("sudo -S -p '' true", timeout=10)
    stdin.write(secret + '\n'); stdin.flush(); stdin.channel.shutdown_write()
    err = stderr.read().decode(); rc = stdout.channel.recv_exit_status(); client.close()
    if rc:
        raise RuntimeError('S3 sudo authentication failed; no solve/deployment started')
    status('Authentication verified. Solving four datasets with two concurrent jobs, one CPU thread per job.')
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        solved = dict(zip(IDS, pool.map(solve, IDS)))
    status('All four datasets solved. Starting sequential physical benchmarks.')
    for i in IDS:
        src = solved[i]
        dst = CONFIGURE / f'GCL_Schedules/result-{tag(i)}'
        dst.mkdir(exist_ok=True)
        for group in GROUPS:
            shutil.copytree(src / group, dst / group, dirs_exist_ok=True)
        for name in ['run_config.env', 'validation.json']:
            shutil.copy2(src / name, dst / name)
        shutil.copy2(TOPO, dst / 'physical-topology.json')
        backup = dst / 'before-deployment'; backup.mkdir(exist_ok=True)
        statefile = CONFIGURE / 'Network-Configure-Manager/.tsn_state.json'
        if statefile.exists():
            shutil.copy2(statefile, backup / 'tsn_state.json')
        for sw, v in topo.items():
            if v['type'] != 'sw':
                continue
            client = cm.ssh_connect(v['ip'], v.get('username', 'root'), v.get('password', ''))
            _, out, err = client.exec_command('bridge -j vlan show; mstpctl showmstconfid br0; mstpctl showportdetail br0; for p in sw0p2 sw0p3 sw0p4 sw0p5; do echo PORT=$p; tsntool st show $p; tsntool st rdocl $p; done', timeout=30)
            (backup / f'{sw}.txt').write_text(out.read().decode() + err.read().decode()); client.close()
        env = dict(os.environ, S3_PW=secret, S1_PW=s1_secret, S2_PW='', TOPO=str(dst / 'physical-topology.json'), TASK_ROOT=str(TASK), DURATION='30', STP_QUIET='15', TZ='America/New_York', PYTHONDONTWRITEBYTECODE='1', PYTHONUNBUFFERED='1')
        status(f'Dataset {i}: physical benchmark started')
        with (dst / 'benchmark-console.log').open('w') as log:
            r = subprocess.run(['bash', str(TASK / 'run_testbed_batched.sh'), str(dst)], cwd=CONFIGURE, env=env, stdout=log, stderr=subprocess.STDOUT)
        reports = list(dst.glob('*/*/results/*/results.md'))
        if r.returncode or len(reports) != 10:
            raise RuntimeError(f'Dataset {i}: physical benchmark incomplete ({len(reports)}/10 reports, rc={r.returncode}); see {dst}/benchmark-console.log')
        status(f'Dataset {i}: all ten physical benchmarks complete')
    status('COMPLETE: datasets 7–10 solved; all forty physical benchmarks complete. Last package remains active.')

if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        status('FAILED: ' + str(exc))
        raise
