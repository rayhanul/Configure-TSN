#!/usr/bin/env python3

import argparse
import csv
import os
import statistics
import matplotlib.pyplot as plt
import numpy as np


def read_csv_file(csv_file, only_success=False):
    iterations = []
    execution_times_ms = []
    exit_statuses = []

    with open(csv_file, "r") as file:
        reader = csv.DictReader(file)

        required_columns = ["iteration", "execution_time_seconds"]
        for col in required_columns:
            if col not in reader.fieldnames:
                raise ValueError(f"{csv_file} is missing required column: {col}")

        label = None

        for row in reader:
            exit_status = row.get("exit_status", "").strip()

            if only_success and exit_status != "0":
                continue

            time_value = row["execution_time_seconds"].strip()

            if not time_value or time_value == "NA":
                continue

            iteration = int(row["iteration"])
            execution_time_ms = float(time_value) * 1000.0

            iterations.append(iteration)
            execution_times_ms.append(execution_time_ms)
            exit_statuses.append(exit_status)

            if label is None:
                ip = row.get("ip", "").strip()
                interface = row.get("interface", "").strip()
                config_file = row.get("config_file", "").strip()

                if ip and interface:
                    label = f"{ip}-{interface}"
                else:
                    label = os.path.basename(csv_file)

        if label is None:
            label = os.path.basename(csv_file)

    return {
        "file": csv_file,
        "label": label,
        "iterations": iterations,
        "times_ms": execution_times_ms,
        "exit_statuses": exit_statuses,
    }


def plot_line_chart(datasets, output_file):
    plt.figure(figsize=(10, 5))

    for data in datasets:
        plt.plot(
            data["iterations"],
            data["times_ms"],
            marker="o",
            markersize=3,
            linewidth=1.5,
            label=data["label"]
        )

    plt.xlabel("Number of Iteration")
    plt.ylabel("Execution Time (ms)")
    plt.title("TSN Command Execution Time Across Iterations")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_file, dpi=300)
    plt.show()


def plot_average_bar_chart(datasets, output_file):
    labels = []
    averages = []

    for data in datasets:
        if not data["times_ms"]:
            continue

        labels.append(data["label"])
        averages.append(statistics.mean(data["times_ms"]))

    plt.figure(figsize=(8, 5))

    x = np.arange(len(labels)) * 0.6
    bar_width = 0.2
    
    bars = plt.bar(x, averages, width=bar_width)

    plt.xlabel("Number of TSN switches")
    plt.ylabel("Average Execution Time (ms)")
    plt.title("Average TSN Command Execution Time")
    plt.grid(axis="y", linestyle="--", alpha=0.5)

    plt.xticks(x, labels, rotation=45, ha="right")
    
    for bar, avg in zip(bars, averages):
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            f"{avg:.3f} ms",
            ha="center",
            va="bottom"
        )

    plt.tight_layout()
    plt.savefig(output_file, dpi=300)
    plt.show()


def print_summary(datasets):
    print("=" * 70)
    print("Execution Time Summary")
    print("=" * 70)

    for data in datasets:
        times = data["times_ms"]

        if not times:
            print(f"{data['label']}: No valid execution times found.")
            continue

        avg = statistics.mean(times)
        min_time = min(times)
        max_time = max(times)

        print(f"File        : {data['file']}")
        print(f"Label       : {data['label']}")
        print(f"Samples     : {len(times)}")
        print(f"Average     : {avg:.3f} ms")
        print(f"Minimum     : {min_time:.3f} ms")
        print(f"Maximum     : {max_time:.3f} ms")

        if len(times) > 1:
            std_dev = statistics.stdev(times)
            print(f"Std dev     : {std_dev:.3f} ms")

        print("-" * 70)


def main():
    parser = argparse.ArgumentParser(
        description="Plot TSN command execution times from three CSV files"
    )

    parser.add_argument(
        "csv_files",
        nargs=3,
        help="Three CSV files containing execution_time_seconds column"
    )

    parser.add_argument(
        "--only-success",
        action="store_true",
        help="Use only rows where exit_status is 0"
    )

    parser.add_argument(
        "--line-output",
        default="execution_time_line_chart.png",
        help="Output file for line chart"
    )

    parser.add_argument(
        "--bar-output",
        default="average_execution_time_bar_chart.png",
        help="Output file for average bar chart"
    )

    args = parser.parse_args()

    datasets = []

    for csv_file in args.csv_files:
        if not os.path.exists(csv_file):
            raise FileNotFoundError(f"File not found: {csv_file}")

        data = read_csv_file(csv_file, only_success=args.only_success)
        datasets.append(data)

    print_summary(datasets)

    plot_line_chart(datasets, args.line_output)
    plot_average_bar_chart(datasets, args.bar_output)

    print(f"Line chart saved as: {args.line_output}")
    print(f"Bar chart saved as : {args.bar_output}")


if __name__ == "__main__":
    main()