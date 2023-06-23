#!/bin/bash

# Check if jq is installed
if ! command -v jq >/dev/null; then
    echo "jq is not installed. Please install jq to run this script."
    exit 1
fi

# JSON file path
json_file="example.json"

# Parse and extract data using jq
data=$(jq '.' "$json_file")

# Print the extracted data
echo "$data"
