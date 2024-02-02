import boto3

def find_open_security_groups():
    # Create an EC2 client
    ec2_client = boto3.client('ec2')

    # Describe all security groups in the AWS account
    response = ec2_client.describe_security_groups()

    # Iterate through each security group and check for open rules
    for security_group in response['SecurityGroups']:
        group_id = security_group['GroupId']
        group_name = security_group.get('GroupName', 'N/A')
        description = security_group.get('Description', 'N/A')

        # Check for open rules in the security group
        open_rules = check_open_security_group_rules(security_group)

        if open_rules:
            print(f"Open Security Group found: {group_name} ({group_id}) - {description}")

def check_open_security_group_rules(security_group):
    open_rules = []

    for rule in security_group.get('IpPermissions', []):
        # Check if the rule allows traffic from anywhere (0.0.0.0/0)
        for ip_range in rule.get('IpRanges', []):
            if ip_range['CidrIp'] == '0.0.0.0/0':
                open_rules.append(rule)

    return open_rules

if __name__ == "__main__":
    find_open_security_groups()
