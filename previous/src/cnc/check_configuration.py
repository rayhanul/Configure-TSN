import paramiko
import pandas as pd
import json
from tqdm import tqdm
import argparse
import os

from previous.src.cnc.main import find_unique_file


def load_json(file_path):
    with open(file_path, "r") as f:
        return json.load(f)


def check_ssh_connection(ip, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(ip, username=username, password=password)
        ssh.close()
        return True
    except Exception as e:
        print(f"Failed to connect to {ip}: {e}")
        return False


def check_remote_file(ssh, remote_path):
    stdin, stdout, stderr = ssh.exec_command(f"ls {remote_path}")
    if stdout.channel.recv_exit_status() == 0:
        return True
    else:
        return False



def check_input_stream_file(stream_file_path):
    df = pd.read_csv(stream_file_path)
    if df.empty:
        print(f"The input stream file {stream_file_path} is empty")
        return False
    # Check if the columns are correct
    required_columns = ["id", "src", "dst", "size", "period", "deadline", "jitter"]
    if not all(col in df.columns for col in required_columns):
        print(
            f"The input stream file {stream_file_path} is missing some required columns"
        )
        return False

    # Check if dst column is wrapped by []
    if not all(
        df["dst"].str.startswith("[") and df["dst"].str.endswith("]")
        for col in df["dst"]
    ):
        print(f"The dst column in {stream_file_path} is not wrapped by []")
        return False

    # Check if deadline is less than period
    if not all(df["deadline"] < df["period"]):
        print(f"The deadline is not less than period in {stream_file_path}")
        return False

    # Check if id is unique and continuous
    if not df["id"].is_unique:
        print(f"The id column in {stream_file_path} is not unique")
        return False
    if not df["id"].equals(pd.RangeIndex(start=0, stop=len(df))):
        print(f"The id column in {stream_file_path} is not continuous")
        return False

    return True

def check_input_schedule_file(schedule_folder):
    offset_file = find_unique_file(schedule_folder, "*OFFSET.csv")
    if offset_file is None:     
        print(f"No OFFSET.csv file found in {schedule_folder}")
        return False
    route_file = find_unique_file(schedule_folder, "*ROUTE.csv")
    if route_file is None:
        print(f"No ROUTE.csv file found in {schedule_folder}")
        return False
    queue_file = find_unique_file(schedule_folder, "*QUEUE.csv")
    if queue_file is None:
        print(f"No QUEUE.csv file found in {schedule_folder}")
        return False
    gcl_file = find_unique_file(schedule_folder, "*GCL.csv")
    if gcl_file is None:
        print(f"No GCL.csv file found in {schedule_folder}")
        return False
    return True


def main():
    # Add command-line arguments
    parser = argparse.ArgumentParser(description="Configuration Checker")
    parser.add_argument(
        "--topology",
        type=str,
        default="conf.json",
        help="Path to the topology file (conf.json)",
    )
    parser.add_argument(
        "--stream",
        type=str,
        default="stream.csv",
        help="Path to the stream file (stream.csv)",
    )
    parser.add_argument(
        "--config_folder",
        type=str,
        default="./",
        help="Local folder where configuration files are located",
    )
    args = parser.parse_args()

    # Load the configuration (topology) file
    if not os.path.exists(args.topology):
        print(f"Topology file '{args.topology}' not found")
        return

    # Check for the presence of stream.csv
    if not os.path.exists(args.stream):
        print(f"Stream file '{args.stream}' not found")
        return

    config = load_json(args.topology)
    all_checks_passed = True

    # Check SSH connections to all entities
    print("[Step 1] Checking SSH connections...")
    for entity_name, entity_info in tqdm(config.items()):
        print("Checking SSH connection to ", entity_name, " IP: ", entity_info["ip"])
        ip = entity_info["ip"]
        username = entity_info["username"]
        password = entity_info["password"]
        if not check_ssh_connection(ip, username, password):
            print(f"Cannot connect to {entity_name} ({ip})")
            all_checks_passed = False

    # Check if the input .csv files are valid
    print("\n[Step 2] Checking input .csv files...")
    if not check_input_stream_file(args.stream):
        all_checks_passed = False

    # Check if the schedule files are valid
    print("\n[Step 3] Checking schedule files...")
    if not check_input_schedule_file(args.config_folder):
        all_checks_passed = False

    if all_checks_passed:
        print("\nAll configurations are correct and servers are accessible.")
    else:
        print("\nSome configurations are missing or servers are inaccessible.")


if __name__ == "__main__":
    main()
