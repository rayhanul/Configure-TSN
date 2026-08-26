#!/bin/bash

# if [ "$#" -ne 1 ]; then
#     echo "Usage: $0 <SUFFIX>"
#     exit 1
# fi

# SUFFIX=$1


# Define the username to login to the servers
USER="ubuntu"

# Define the directory where the log files are stored on the servers
REMOTE_DIR="/home/ubuntu"

# Define the local directory where you want to save the log files
LOCAL_DIR="/home/chuanyu/Code/time-sensitive-network-testbed/data/0826"

# Iterate over the IP range
# for i in $(seq 9 16)
# do
#   # Construct the server IP
#   SERVER="192.168.50.$i"
  
#   # Use scp to copy the .log files from the server to the local machine
#   FILES=$(sshpass -p '1234567809' ssh -o StrictHostKeyChecking=no "${USER}@${SERVER}" "ls ${REMOTE_DIR}/*.log")
  
#   # Copy each file individually and add the provided suffix
#   for FILE in $FILES
#   do
#     BASENAME=$(basename $FILE)
#     sshpass -p '1234567809' scp -o StrictHostKeyChecking=no "${USER}@${SERVER}:${FILE}" "${LOCAL_DIR}/${BASENAME%.log}_${SUFFIX}.log"
#   done
# done

for i in $(seq 9 16)
do
  # Construct the server IP
  SERVER="192.168.50.$i"
  
  # Use scp to copy the .log files from the server to the local machine
  sshpass -p '1234567809' scp -o StrictHostKeyChecking=no "${USER}@${SERVER}:${REMOTE_DIR}/*.log" $LOCAL_DIR
done