#!/usr/bin/env python3

import argparse
import time
import sys
import socket
import paramiko


def connect_without_password(ip, username, port=22):
    print(f"[INFO] Connecting to TSN switch at {ip} using SSH none authentication...")

    try:
        sock = socket.create_connection((ip, port), timeout=10)
    except Exception as e:
        print("[ERROR] Could not create TCP connection to switch.")
        print(f"[DETAILS] {e}")
        sys.exit(1)

    transport = paramiko.Transport(sock)
    transport.start_client(timeout=10)

    try:
        transport.auth_none(username)
    except paramiko.BadAuthenticationType as e:
        print("[ERROR] The switch did not accept SSH none authentication.")
        print("[ERROR] Allowed authentication types:", e.allowed_types)
        transport.close()
        sys.exit(1)
    except Exception as e:
        print("[ERROR] SSH none authentication failed.")
        print(f"[DETAILS] {e}")
        transport.close()
        sys.exit(1)

    if not transport.is_authenticated():
        print("[ERROR] SSH transport is not authenticated.")
        transport.close()
        sys.exit(1)

    ssh = paramiko.SSHClient()
    ssh._transport = transport

    print("[INFO] SSH connection established without password.")
    return ssh


def run_single_command_on_switch(ip, username, command):
    ssh = connect_without_password(ip, username)

    print("\n" + "=" * 60)
    print("CNC COMMAND EXECUTION")
    print("=" * 60)
    print(f"[COMMAND] {command}")

    # CNC-side start time: immediately before sending command over SSH
    cnc_start_time = time.perf_counter()

    try:
        stdin, stdout, stderr = ssh.exec_command(command)

        # Wait until remote command finishes
        exit_status = stdout.channel.recv_exit_status()

        # CNC-side end time: immediately after command completion is observed
        cnc_end_time = time.perf_counter()

    except Exception as e:
        cnc_end_time = time.perf_counter()
        ssh.close()

        print("[ERROR] Failed while executing command over SSH.")
        print(f"[DETAILS] {e}")
        print(f"[CNC ELAPSED TIME UNTIL FAILURE] {cnc_end_time - cnc_start_time:.6f} seconds")
        sys.exit(1)

    elapsed_time = cnc_end_time - cnc_start_time

    output = stdout.read().decode(errors="replace")
    error = stderr.read().decode(errors="replace")

    if output:
        print("\n[OUTPUT]")
        print(output)

    if error:
        print("\n[ERROR OUTPUT]")
        print(error)

    print("\n" + "=" * 60)
    print("CNC TO COMMAND COMPLETION TIME REPORT")
    print("=" * 60)
    print(f"Command     : {command}")
    print(f"Exit status : {exit_status}")
    print(f"CNC time    : {elapsed_time:.6f} seconds")
    print("=" * 60)

    if exit_status != 0:
        print("[WARNING] Command returned non-zero exit status.")

    ssh.close()
    print("\n[INFO] SSH connection closed.")


def main():
    parser = argparse.ArgumentParser(
        description="Run one TSN switch command over SSH none authentication and report CNC-to-completion time"
    )

    parser.add_argument("--ip", required=True, help="TSN switch IP address")
    parser.add_argument("--user", required=True, help="SSH username")
    parser.add_argument(
        "--cmd",
        required=True,
        help="Single command to run on the TSN switch"
    )

    args = parser.parse_args()

    run_single_command_on_switch(
        ip=args.ip,
        username=args.user,
        command=args.cmd
    )


if __name__ == "__main__":
    main()