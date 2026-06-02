# #!/bin/bash

# if [ "$#" -lt 3 ]; then
#     echo "Usage: $0 <ip> <interface> <config_file>"
#     echo "Example: $0 192.168.0.4 sw0p2 sw0p2.cfg"
#     exit 1
# fi

# IP="$1"
# INTERFACE="$2"
# CONFIG_FILE="$3"
# USER="root"
# REPEAT=100

# CSV_FILE="wrcl_${INTERFACE}_execution_times.csv"

# echo "iteration,ip,interface,config_file,exit_status,execution_time_seconds" > "$CSV_FILE"

# for i in $(seq 1 $REPEAT); do
#     echo "Running iteration $i/$REPEAT on $IP, interface=$INTERFACE, config=$CONFIG_FILE..."

#     output=$(python3 run-tsn-config-cnc.py \
#         --ip "$IP" \
#         --user "$USER" \
#         --cmd "tsntool st wrcl $INTERFACE $CONFIG_FILE" 2>&1)

#     exit_status=$(echo "$output" | awk -F: '/Exit status/ {gsub(/^[ \t]+/, "", $2); print $2}')
#     exec_time=$(echo "$output" | awk -F: '/CNC time/ {gsub(/^[ \t]+/, "", $2); gsub(/ seconds/, "", $2); print $2}')

#     if [ -z "$exit_status" ]; then
#         exit_status="NA"
#     fi

#     if [ -z "$exec_time" ]; then
#         exec_time="NA"
#     fi

#     echo "$i,$IP,$INTERFACE,$CONFIG_FILE,$exit_status,$exec_time" >> "$CSV_FILE"
# done

# echo "Done. Results saved in $CSV_FILE"





#!/bin/bash

if [ "$#" -lt 3 ]; then
    echo "Usage: $0 <ip> <interface> <config_file>"
    echo "Example: $0 192.168.0.4 sw0p2 sw0p2.cfg"
    exit 1
fi

IP="$1"
INTERFACE="$2"
CONFIG_FILE="$3"
USER="root"
REPEAT=100
GAP=10

CSV_FILE="wrcl_${IP}_${INTERFACE}_execution_times.csv"

echo "iteration,ip,interface,config_file,exit_status,execution_time_seconds" > "$CSV_FILE"

echo "Starting WRCL test..."
echo "IP          : $IP"
echo "Interface   : $INTERFACE"
echo "Config file : $CONFIG_FILE"
echo "Repeat      : $REPEAT"
echo "Gap         : $GAP seconds"
echo "CSV file    : $CSV_FILE"
echo

for i in $(seq 1 $REPEAT); do
    echo "Running iteration $i/$REPEAT..."

    output=$(timeout 30s python3 run-tsn-config-cnc.py \
        --ip "$IP" \
        --user "$USER" \
        --cmd "tsntool st wrcl $INTERFACE $CONFIG_FILE" 2>&1)

    cmd_status=$?

    exit_status=$(echo "$output" | awk -F: '/Exit status/ {gsub(/^[ \t]+/, "", $2); print $2}')
    exec_time=$(echo "$output" | awk -F: '/CNC time/ {gsub(/^[ \t]+/, "", $2); gsub(/ seconds/, "", $2); print $2}')

    if [ "$cmd_status" -eq 124 ]; then
        echo "Iteration $i timed out."
        exit_status="TIMEOUT"
        exec_time="NA"
    fi

    if [ -z "$exit_status" ]; then
        exit_status="NA"
    fi

    if [ -z "$exec_time" ]; then
        exec_time="NA"
    fi

    echo "$i,$IP,$INTERFACE,$CONFIG_FILE,$exit_status,$exec_time" >> "$CSV_FILE"

    echo "Result: exit_status=$exit_status, time=$exec_time"

    # if [ "$i" -lt "$REPEAT" ]; then
    #     echo "Waiting $GAP seconds before next run..."
    #     sleep "$GAP"
    # fi
done

echo
echo "Done. Results saved in $CSV_FILE"




