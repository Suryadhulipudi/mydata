import ssl
import socket
from datetime import datetime

def check_ssl_certificate(hostname, port=443):
    try:
        # Create a socket connection to the server
        context = ssl.create_default_context()
        with socket.create_connection((hostname, port)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                # Retrieve and print certificate information
                cert = ssock.getpeercert()
                print(f"Certificate Information for {hostname}:\n")
                print(f"Subject: {cert['subject']}")
                print(f"Issuer: {cert['issuer']}")
                print(f"Valid From: {datetime.utcfromtimestamp(cert['notBefore'])}")
                print(f"Valid Until: {datetime.utcfromtimestamp(cert['notAfter'])}")
                
                # Check if the certificate is still valid
                if datetime.utcnow() > datetime.utcfromtimestamp(cert['notAfter']):
                    print("\nCertificate has expired!")
                else:
                    print("\nCertificate is still valid.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Replace 'example.com' with the desired website
    website = 'example.com'
    check_ssl_certificate(website)
