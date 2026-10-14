"""Apply the existing configuration plan with ordered, batched SSH commands."""
import atexit
import re
import shlex
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / 'Network-Configure-Manager'))
import configureManager as cm

clients = {}

def tree_mstp(plans, topology, region='rtas_tree_cist', region_rev=1):
    """Use CIST for a connected tree: each endpoint route is already unique."""
    switches = sorted(n for n, v in topology.items() if v.get('type') == 'sw')
    edges = set()
    neighbors = {n: set() for n in switches}
    for n in switches:
        for value in topology[n].get('links', {}).values():
            peer = value.get('node') if isinstance(value, dict) else value
            if peer in neighbors:
                edges.add(tuple(sorted((n, peer))))
                neighbors[n].add(peer)
    seen, pending = set(), [switches[0]]
    while pending:
        n = pending.pop()
        if n not in seen:
            seen.add(n); pending.extend(neighbors[n] - seen)
    if len(seen) != len(switches) or len(edges) != len(switches) - 1:
        raise RuntimeError('CIST-only rerun requires a connected tree topology')
    result = {}
    for n in switches:
        bridge = cm.node_attr(topology, n, 'bridge', cm.DEFAULT_BRIDGE)
        prefix = cm.node_attr(topology, n, 'port_prefix', cm.DEFAULT_PORT_PREFIX)
        commands = [f'mstpctl setmstconfid {bridge} {region_rev} {region}',
                    f'mstpctl setvid2fid {bridge} 0:1-4094',
                    f'mstpctl setfid2mstid {bridge} 0:0-4095',
                    f'mstpctl setforcevers {bridge} rstp',
                    f'mstpctl settreeprio {bridge} 0 8']
        for port, value in sorted(topology[n].get('links', {}).items()):
            peer = value.get('node') if isinstance(value, dict) else value
            if peer:
                commands.extend([f'mstpctl setportp2p {bridge} {prefix}{port} yes',
                                 f'mstpctl settreeportcost {bridge} {prefix}{port} 0 0'])
        commands.append(f'mstpctl showmstconfid {bridge}')
        result[n] = commands
    return result

def close_clients():
    for client in clients.values():
        client.close()

atexit.register(close_clients)

def batched_ssh_run(host, user, password, commands):
    key = (host, user)
    if key not in clients:
        clients[key] = cm.ssh_connect(host, user, password)
    client = clients[key]
    script = []
    for i, command in enumerate(commands):
        script.append('printf "%s\\n" ' + shlex.quote(f'[{host}] RUN {command}'))
        script.append(command)
        script.append(f'rc=$?; printf "__TSN_RC_{i}:%s\\n" "$rc"')
    script = '\n'.join(script)
    full = 'sh -c ' + shlex.quote(script)
    if user != 'root':
        full = "sudo -S -p '' " + full
    stdin, stdout, stderr = client.exec_command(full, timeout=120)
    if user != 'root':
        stdin.write(password + '\n')
        stdin.flush()
    stdin.channel.shutdown_write()
    out, err = stdout.read().decode(), stderr.read().decode()
    rc = stdout.channel.recv_exit_status()
    results = {int(i): int(code) for i, code in re.findall(r'__TSN_RC_(\d+):(\d+)', out)}
    print(re.sub(r'^__TSN_RC_\d+:\d+\n?', '', out, flags=re.M), end='', flush=True)
    if err:
        print(err, end='', file=sys.stderr, flush=True)
    if rc or len(results) != len(commands):
        raise RuntimeError(f'{host}: incomplete command batch ({len(results)}/{len(commands)}, rc={rc})')
    failures = [(commands[i], code) for i, code in results.items() if code and not commands[i].startswith('mstpctl createtree ')]
    if failures:
        raise RuntimeError(f'{host}: configuration command failures: {failures}')

def parallel_apply_plan(plans, topology, mstp_plan=None, state_path=cm.DEFAULT_STATE_FILE, cnc=None):
    from concurrent.futures import ThreadPoolExecutor

    asked = cm.prompt_nodes(plans, topology, mstp_plan)
    if asked:
        cm.prompt_and_verify(asked, topology, cnc=cnc)
    credentials = {}
    for node in cm.involved_nodes(plans, mstp_plan):
        d = topology[node]
        credentials[node] = (d['ip'], d['username'], cm.resolve_password(node, d['ip'], d['username'], d.get('password')))

    def execute(item):
        node, commands = item
        host, user, password = credentials[node]
        if node == cnc:
            cm.run_local(commands, user, password)
        else:
            batched_ssh_run(host, user, password, commands)

    prior = cm.load_state(state_path)
    if prior:
        cm.run_teardown(prior, topology, label='remove old', cnc=cnc)
    by_node = {}
    for plan in plans:
        if plan.sender_cmds:
            by_node.setdefault(plan.src, []).extend(plan.sender_cmds)
        if plan.receiver_cmds:
            by_node.setdefault(plan.dst, []).extend(plan.receiver_cmds)
        for node, commands in plan.switch_cmds.items():
            by_node.setdefault(node, []).extend(commands)
    with ThreadPoolExecutor(max_workers=8) as pool:
        list(pool.map(execute, by_node.items()))
    if mstp_plan:
        with ThreadPoolExecutor(max_workers=8) as pool:
            list(pool.map(execute, mstp_plan.items()))
        cm.check_mst_region(mstp_plan, lambda node: credentials[node])
        import time
        print('Hardware settling: waiting 60 seconds after configuration', flush=True)
        time.sleep(60)
    if state_path:
        cm.save_state(state_path, cm.build_teardown(plans, topology))
        print(f'State saved to {state_path}', flush=True)

cm.ssh_run = batched_ssh_run
cm.apply_plan = parallel_apply_plan
cm.build_mstp = tree_mstp
if __name__ == '__main__':
    cm.main()
