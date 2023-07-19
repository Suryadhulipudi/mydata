#Method-1 Extract Ip addresses ane bytes transferred
import re

def extract_ip_bytes(log_file):
    ip_bytes = {}

    with open(log_file, 'r') as file:
        for line in file:
            # Use regular expressions to find IP addresses and bytes transferred
            matches = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?(\d+)$', line)

            for match in matches:
                ip = match[0]
                bytes_transferred = int(match[1])

                if ip in ip_bytes:
                    ip_bytes[ip] += bytes_transferred
                else:
                    ip_bytes[ip] = bytes_transferred

    return ip_bytes

# Example log file path
log_file = 'example.log'

# Extract IP addresses and bytes transferred from log file
ip_bytes = extract_ip_bytes(log_file)

# Print the extracted IP addresses and corresponding bytes transferred
print("IP Addresses and Bytes Transferred:")
for ip, bytes_transferred in ip_bytes.items():
    print(f"IP: {ip}, Bytes Transferred: {bytes_transferred}")

#Method-2
import re

def extract_ip_addresses(log_file):
    ip_addresses = set()

    with open(log_file, 'r') as file:
        for line in file:
            # Use regular expression to find IP addresses
            matches = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line)
            ip_addresses.update(matches)

    return ip_addresses

# Example log file path
log_file = 'example.log'

# Extract IP addresses from log file
ip_addresses = extract_ip_addresses(log_file)

# Print the extracted IP addresses
print("IP Addresses:")
for ip_address in ip_addresses:
    print(ip_address)



#Method-3
# importing the module
import re
  
# opening and reading the file 
with open('C:/Users/user/Desktop/New Text Document.txt') as fh:
   fstring = fh.readlines()
  
# declaring the regex pattern for IP addresses
pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
  
# initializing the list object
lst=[]
  
# extracting the IP addresses
for line in fstring:
   lst.append(pattern.search(line)[0])
  
# displaying the extracted IP addresses
print(lst)
