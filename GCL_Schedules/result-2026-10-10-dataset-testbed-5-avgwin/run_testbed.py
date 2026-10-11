#!/usr/bin/env python3
"""Validate node sudo access, then run the established ten-package testbed sweep."""
import json
import os
from pathlib import Path
import subprocess
import sys

BASE = Path(__file__).resolve().parent
REPO = BASE.parent.parent
TOPO = Path(os.environ.get("TOPO", str(REPO / "network-topology/network-topology-rtas-2027-tree.json"))).resolve()
sys.path.insert(0, str(REPO / "Spawning-Flows"))
import run_experiment as rx


def main():
    topo = json.loads(TOPO.read_text())
    for name in ("S1", "S2", "S3"):
        node = rx.Node(name, topo)
        try:
            code, _, _ = node.run("true", sudo=True, timeout=15)
            if code:
                raise SystemExit(f"{name}: sudo access unavailable; no deployment started.")
        finally:
            if node.client:
                node.client.close()
        print(f"{name}: sudo access OK", flush=True)
    env = os.environ.copy()
    env["TOPO"] = str(TOPO)
    env["PYTHONUNBUFFERED"] = "1"
    for name in ("S1", "S2", "S3"):
        env.setdefault(f"{name}_PW", topo[name].get("password", ""))
    with (BASE / "testbed_driver.log").open("a") as log:
        return subprocess.call(
            ["bash", "-e", "-o", "pipefail", str(BASE.parent / "run_testbed.sh"), str(BASE), *sys.argv[1:]],
            cwd=REPO, env=env, stdout=log, stderr=subprocess.STDOUT,
        )


if __name__ == "__main__":
    sys.exit(main())
