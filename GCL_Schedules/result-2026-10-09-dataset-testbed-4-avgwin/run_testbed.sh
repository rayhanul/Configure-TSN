#!/usr/bin/env bash
# Regenerate the testbed results of this dataset (result-2026-10-09-dataset-testbed-4-avgwin):
# deploys every package here on the physical testbed, one by one, 30 s of traffic each, then writes
# TESTBED_RESULTS_<date>.md in this folder. Per-package reports: <group>/<package>/results/results-<date>[_n]/.
#
#   S3_PW=... S1_PW=... ./run_testbed.sh              # all 10 packages (~1h45)
#   S3_PW=... S1_PW=... ./run_testbed.sh rl-c9-off    # only these groups
#
# Before: gPTP synced and launch time on, on S1/S2/S3 (time-sync-gptp/gptp.sh launchtime on).
# Options (TOPO, DURATION, S2_PW): see ../run_testbed.sh.
HERE=$(cd "$(dirname "$0")" && pwd)
exec "$HERE/../run_testbed.sh" "$HERE" "$@"
