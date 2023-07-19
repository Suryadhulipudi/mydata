#!/bin/bash

# Prompt the user for input
read -p "Enter your name: " name

# Create a directory with the user's name
mkdir "$name"
echo "Created directory: $name"

# Change to the user's directory
cd "$name"

# Download a file from a remote server
wget https://example.com/file.txt
echo "Downloaded file.txt"

# Extract information from the downloaded file
count=$(grep -c 'keyword' file.txt)
echo "Occurrences of 'keyword': $count"

# Perform some calculations
total=0
for num in {1..10}; do
    ((total+=num))
done
echo "Total: $total"

# Display a message based on the time of day
hour=$(date +%H)
if ((hour >= 0 && hour < 12)); then
    echo "Good morning, $name!"
elif ((hour >= 12 && hour < 18)); then
    echo "Good afternoon, $name!"
else
    echo "Good evening, $name!"
fi

# Clean up temporary files
rm file.txt
echo "Removed file.txt"

# Display a farewell message
echo "Script execution complete. Goodbye, $name!"
