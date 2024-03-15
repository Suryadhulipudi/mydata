def is_sparse(num):
    binary = bin(num)[2:]  # Convert number to binary string, omitting '0b' prefix
    for i in range(len(binary) - 1):
        if binary[i] == '1' and binary[i + 1] == '1':
            return False
    return True

# Test cases
print(is_sparse(21))  # Output: True (10101 is sparse)
print(is_sparse(22))  # Output: False (10110 is not sparse)
