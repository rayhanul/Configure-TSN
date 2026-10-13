import getpass
import json
import os
import subprocess
import sys
from pathlib import Path

repo = Path(__file__).resolve().parents[2]
root = Path(__file__).resolve().parent
sys.path.insert(0, str(repo / "Network-Configure-Manager"))
import configureManager as cm

topo = json.loads((root / "physical-topology.json").read_text())
secret = os.environ.get("S3_PW") or getpass.getpass("S3 sudo password: ")
s1_secret = os.environ.get("S1_PW") or getpass.getpass("S1 sudo password: ")
v = topo["S3"]
client = cm.ssh_connect(v["ip"], v["username"], secret)
stdin, stdout, stderr = client.exec_command("sudo -S -p '' true", timeout=10)
stdin.write(secret + "\n")
stdin.flush()
stdin.channel.shutdown_write()
err = stderr.read().decode()
rc = stdout.channel.recv_exit_status()
client.close()
if rc:
    sys.exit("S3 sudo authentication failed; benchmark not started.")
print("S3 sudo authentication verified.", flush=True)
env = dict(os.environ, S3_PW=secret, S1_PW=s1_secret, S2_PW="", TOPO=str(root / "physical-topology.json"), DURATION="30", STP_QUIET="15", TZ="America/New_York")
with (root / "benchmark-console.log").open("w") as log:
    result = subprocess.run(["bash", str(repo / "GCL_Schedules/run_testbed.sh"), str(root)], cwd=repo, env=env, stdout=log, stderr=subprocess.STDOUT)
print("Benchmark driver exit:", result.returncode, flush=True)
sys.exit(result.returncode)
