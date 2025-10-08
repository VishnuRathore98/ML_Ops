from pprint import pprint

import boto3

client = boto3.client('ec2', region_name='ap-south-1')

# List available security groups
list_sec_groups = client.describe_security_groups()

# Create security group
sec_group = client.create_security_group(
    GroupName='boto3_security_group',
    Description='A security group created using boto3'
)

sec_group_id = sec_group['GroupId']

pprint('Security Group: ',sec_group)

# Attach inbound(ingress) rules, here for ssh 
in_rules = client.authorize_security_group_ingress(
    GroupId = sec_group_id,
    IpPermissions = [
        {
            'IpProtocol':'tcp',
            'FromPort':22,
            'ToPort':22,
            'IpRanges':[{'CidrIp':'0.0.0.0/0'}]
        }
    ]
) 

pprint('In Rules: ', in_rules)
