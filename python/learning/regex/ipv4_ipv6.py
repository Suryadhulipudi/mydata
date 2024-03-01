To find all IPv4 and IPv6 addresses in a log file, you can use regular expressions in Python. Below is a Python script that demonstrates how to achieve this:

```python
import re

def find_ip_addresses(log_file):
    ipv4_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    ipv6_pattern = r'(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}'
    ipv4_addresses = set()
    ipv6_addresses = set()

    with open(log_file, 'r') as file:
        for line in file:
            ipv4_addresses.update(re.findall(ipv4_pattern, line))
            ipv6_addresses.update(re.findall(ipv6_pattern, line))

    return ipv4_addresses, ipv6_addresses

if __name__ == "__main__":
    log_file = "your_log_file.log"
    ipv4_addresses, ipv6_addresses = find_ip_addresses(log_file)

    print("IPv4 Addresses:")
    for ip in ipv4_addresses:
        print(ip)

    print("\nIPv6 Addresses:")
    for ip in ipv6_addresses:
        print(ip)
```

Replace `"your_log_file.log"` with the path to your log file.

This script defines a function `find_ip_addresses(log_file)` that takes a log file as input and returns two sets containing IPv4 and IPv6 addresses found in the log file. It reads each line of the log file, searches for IPv4 and IPv6 addresses using regular expressions, and updates the respective sets.

When you run this script, it will print out all the IPv4 and IPv6 addresses found in the log file. You can further customize the regular expressions if your log file contains different formats of IP addresses.
