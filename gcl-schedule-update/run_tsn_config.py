#!/usr/bin/env python3

import argparse
import time
import sys
import socket
import paramiko


def connect_without_password(ip, username, port=22):
    print(f"[INFO] Connecting to TSN switch at {ip} using SSH none authentication...")

    sock = socket.create_connection((ip, port), timeout=10)

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


def run_commands_on_switch(ip, username, commands):
    ssh = connect_without_password(ip, username)

    total_start_time = time.perf_counter()
    command_times = []

    for cmd in commands:
        print(f"\n[RUNNING] {cmd}")

        start_time = time.perf_counter()

        stdin, stdout, stderr = ssh.exec_command(cmd)

        exit_status = stdout.channel.recv_exit_status()

        end_time = time.perf_counter()
        elapsed_time = end_time - start_time

        output = stdout.read().decode(errors="replace")
        error = stderr.read().decode(errors="replace")

        if output:
            print("[OUTPUT]")
            print(output)

        if error:
            print("[ERROR]")
            print(error)

        print(f"[EXIT STATUS] {exit_status}")
        print(f"[COMMAND TIME] {elapsed_time:.6f} seconds")

        command_times.append((cmd, elapsed_time, exit_status))

        if exit_status != 0:
            print("[WARNING] Command returned non-zero exit status.")

    total_end_time = time.perf_counter()
    total_elapsed_time = total_end_time - total_start_time

    ssh.close()

    print("\n" + "=" * 60)
    print("GCL REPLACEMENT TIME REPORT")
    print("=" * 60)

    for index, (cmd, elapsed_time, exit_status) in enumerate(command_times, start=1):
        print(f"Command {index}: {cmd}")
        print(f"Time     : {elapsed_time:.6f} seconds")
        print(f"Status   : {exit_status}")
        print("-" * 60)

    if len(command_times) >= 2:
        second_cmd, second_time, second_status = command_times[1]
        print(f"Second command: {second_cmd}")
        print(f"Second command time: {second_time:.6f} seconds")
        print(f"Second command status: {second_status}")
        print("-" * 60)

    print(f"Total time for all commands: {total_elapsed_time:.6f} seconds")
    print("=" * 60)

    print("\n[INFO] SSH connection closed.")


def main():
    parser = argparse.ArgumentParser(
        description="Run TSN switch commands over SSH none authentication and report execution time"
    )

    parser.add_argument("--ip", required=True, help="TSN switch IP address")
    parser.add_argument("--user", required=True, help="SSH username")

    parser.add_argument(
        "--cmd",
        action="append",
        required=True,
        help="Command to run on the TSN switch. Use --cmd multiple times for multiple commands."
    )

    args = parser.parse_args()

    commands = args.cmd

    if not commands:
        print("[ERROR] No commands provided.")
        sys.exit(1)

    run_commands_on_switch(
        ip=args.ip,
        username=args.user,
        commands=commands
    )


if __name__ == "__main__":
    main()