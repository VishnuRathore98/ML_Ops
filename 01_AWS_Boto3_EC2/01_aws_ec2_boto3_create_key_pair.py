import boto3

ec2 = boto3.client('ec2')

ec2_description = ec2.describe_instances()

key_pair = ec2.create_key_pair(KeyName='ec2_boto3')

with open('<path>/ec2_boto3_key_pair.pem', 'w') as fp:
    fp.write(key_pair['KeyMaterial'])

print("key pair created successfully!")
