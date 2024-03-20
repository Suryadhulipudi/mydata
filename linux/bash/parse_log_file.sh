#!/bin/bash

# Get the raw output logs from the URL
raw_logs=$(curl -s https://coderbyte.com/api/challenges/logs/web-logs-raw)

# Loop through each log item
while IFS= read -r log_item; do
    # Check if the log item contains the string 'coderbyte heroku/router'
    if [[ $log_item == *"coderbyte heroku/router"* ]]; then
        # Extract request_id and fwd from the log item
        request_id=$(echo "$log_item" | grep -oP 'request_id=\K[^ ]+')
        fwd=$(echo "$log_item" | grep -oP 'fwd=\K[^ ]+')
        
        # Check if fwd value is MASKED
        if [[ "$fwd" == "MASKED" ]]; then
            # Print request_id with [M] at the end
            echo "$request_id [M]"
        else
            # Print request_id with fwd value in the format [fwd_value]
            echo "$request_id [$fwd]"
        fi
    fi
done <<< "$raw_logs"
