import boto3
from pprint import pprint

# Get client
client = boto3.client('ec2',region_name='ap-south-1')

# Get all instances for the client
all_instances = client.describe_instances()

# Get instance id for required instance
instance_id = all_instances['Reservations'][1]['Instances'][0]['InstanceId']

# Get instance by instance id
instance = client.describe_instances(InstanceIds=[instance_id])

# Get instance status
instance_status = instance['Reservations'][0]['Instances'][0]['State']['Name']

pprint(instance_status)

