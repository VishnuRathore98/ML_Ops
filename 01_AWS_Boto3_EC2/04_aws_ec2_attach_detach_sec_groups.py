import boto3
from pprint import pprint

client = boto3.client('ec2', region_name='ap-south-1')

des_sec_grp = client.describe_security_groups()

des_instances = client.describe_instances()

instance_id = des_instances['Reservations'][1]['Instances'][0]['InstanceId']

default_sec_gid = des_sec_grp['SecurityGroups'][0]['GroupId']

ssh_sec_gid = des_sec_grp['SecurityGroups'][-1]['GroupId']

# attach both default and ssh security groups
#client.modify_instance_attribute(InstanceId=instance_id, Groups=[default_sec_gid, ssh_sec_gid])

# attach only default and detach ssh security group
client.modify_instance_attribute(InstanceId=instance_id, Groups=[default_sec_gid])

# attach only ssh and detach default security group
#client.modify_instance_attribute(InstanceId=instance_id, Groups=[ssh_sec_gid])

print("Security Groups updated\n")
pprint({"instance_id":instance_id})
pprint({"default_security_group_id":default_sec_gid})
pprint({"ssh_sec_gid":ssh_sec_gid})
