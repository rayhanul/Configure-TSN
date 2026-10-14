"""Read operational GCLs after the final tree benchmark and record deployment."""
import concurrent.futures
import json
from pathlib import Path
import re
import sys

TASK = Path(__file__).resolve().parent
CONFIGURE = TASK.parents[1]
ROOT = CONFIGURE / 'GCL_Schedules/rerun-dataset-11-tree-rstp-settled'
PACKAGE = ROOT / 'prob3-rl-c9-on/11-rl-c9on-matrix'
sys.path.insert(0, str(CONFIGURE / 'Network-Configure-Manager'))
import configureManager as cm


def entries(value):
    return [(int(interval), int(mask, 0)) for interval, mask in re.findall(
        r'^\s*sgs\s+(\d+)\s+(0x[0-9A-Fa-f]+|\d+)\s*(?:#.*)?$', value, re.M)]


def main():
    topo = json.loads((ROOT / 'physical-topology.json').read_text())
    configs = sorted((PACKAGE / 'gcl').glob('*.cfg'))
    if len(configs) != 17:
        raise RuntimeError(f'Expected 17 connected ports, found {len(configs)}')

    def check(cfg):
        switch, port = cfg.stem.split('-')
        node = topo[switch]
        client = cm.ssh_connect(node['ip'], node.get('username', 'root'), '')
        try:
            _, out, err = client.exec_command(f'tsntool st rdocl sw0{port}', timeout=30)
            live = out.read().decode()
            error = err.read().decode()
            rc = out.channel.recv_exit_status()
            _, state_out, state_err = client.exec_command(f'mstpctl showportdetail br0 sw0{port}', timeout=30)
            state = state_out.read().decode()
            state_error = state_err.read().decode()
            state_rc = state_out.channel.recv_exit_status()
        finally:
            client.close()
        expected = entries(cfg.read_text())
        actual = entries(live)
        if rc or not expected or actual != expected:
            raise RuntimeError(f'{cfg.stem}: operational GCL mismatch, rc={rc}: {error}')
        if state_rc or not re.search(r'\bstate\s+forwarding\b', state):
            raise RuntimeError(f'{cfg.stem}: CIST port is not forwarding: {state_error} {state}')
        return {'port': cfg.stem, 'entries': len(actual), 'matches_package': True, 'forwarding': True}

    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        checks = list(pool.map(check, configs))
    schedule = json.loads((PACKAGE / 'schedule.json').read_text())
    result = {
        'active_package': str(PACKAGE.relative_to(CONFIGURE)),
        'scheduled_flows': sum(bool(f.get('scheduled')) for f in schedule['flows']),
        'cycle_ns': schedule['cycle_ns'],
        'operational_readback': checks,
        'completed_datasets': [11, 12],
        'completed_final_comparison_trials': 20,
        'completed_intermediate_trials': 10,
        'forwarding_protocol': 'RSTP / CIST',
        'traffic_duration_seconds_per_package': 30,
    }
    (TASK / 'deployment-state.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
