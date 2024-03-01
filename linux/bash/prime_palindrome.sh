#!/bin/bash

# Function to check if a number is prime
is_prime() {
    num=$1
    if [ $num -lt 2 ]; then
        return 1
    fi
    for (( i=2; i*i<=$num; i++ )); do
        if [ $((num % i)) -eq 0 ]; then
            return 1
        fi
    done
    return 0
}

# Function to check if a number is palindrome
is_palindrome() {
    num=$1
    reverse=0
    original=$num
    while [ $num -gt 0 ]; do
        digit=$((num % 10))
        reverse=$((reverse * 10 + digit))
        num=$((num / 10))
    done
    if [ $original -eq $reverse ]; then
        return 0
    else
        return 1
    fi
}

# Main script
read -p "Enter a number: " num
if is_prime $num && is_palindrome $num; then
    echo "$num is both prime and palindrome."
elif is_prime $num; then
    echo "$num is prime but not palindrome."
elif is_palindrome $num; then
    echo "$num is palindrome but not prime."
else
    echo "$num is neither prime nor palindrome."
fi
