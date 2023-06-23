#!/bin/bash

# Define the numbers
numbers=(5 2 9 1 3)

# Perform bubble sort
n=${#numbers[@]}
for ((i = 0; i < n-1; i++)); do
    for ((j = 0; j < n-i-1; j++)); do
        if (( numbers[j] > numbers[j+1] )); then
            # Swap numbers[j] and numbers[j+1]
            temp=${numbers[j]}
            numbers[j]=${numbers[j+1]}
            numbers[j+1]=$temp
        fi
    done
done

# Print the sorted numbers
for number in "${numbers[@]}"; do
    echo "$number"
done
