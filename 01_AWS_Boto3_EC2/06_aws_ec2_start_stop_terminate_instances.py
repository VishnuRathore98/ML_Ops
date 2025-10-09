import boto3
import botocore
import time

# Get client
client = boto3.client('ec2',region_name='ap-south-1')

# Get all instances for the client
all_instances = client.describe_instances()

# Get instance id for required instance
instance_id = all_instances['Reservations'][1]['Instances'][0]['InstanceId']

def wait_for_status(instance_id, required_status):

    while True:
        # Get instance by instance id
        instance = client.describe_instances(InstanceIds=[instance_id])     
        # Get instance status
        instance_status = instance['Reservations'][0]['Instances'][0]['State']['Name']
        print(f'Current status: {instance_status}')

        if instance_status == required_status:
            print(f"Instance {instance_id}, {required_status} successfully!")
            break
        time.sleep(5)


def start_instance(instance_id):
    print(f'Starting {instance_id} ...')
    try:
        client.start_instances(InstanceIds=[instance_id])
        wait_for_status(instance_id, 'running')
    except botocore.exceptions.ClientError as e:
        print(e)

def stop_instance(instance_id):
    print(f'Stopping {instance_id} ...')
    try: 
        client.stop_instances(InstanceIds=[instance_id])
        wait_for_status(instance_id, 'stopped')
    except botocore.exceptions.ClientError as e:
        print(e)

def terminate_instance(instance_id):
    print(f'Termination for {instance_id} started...')
    try:
        client.terminate_instances(InstanceIds=[instance_id])
        wait_for_status(instance_id, 'terminated')
    except botocore.exceptions.ClientError as e:
        print(e)

#start_instance(instance_id)
#stop_instance(instance_id)
#terminate_instance(instance_id)
