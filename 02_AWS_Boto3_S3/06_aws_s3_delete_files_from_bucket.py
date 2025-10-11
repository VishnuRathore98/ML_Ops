import boto3
from pprint import pprint

s3_client = boto3.client('s3', region_name='ap-south-1')

bucket_name = 'test93839'
s3_prefix = 'data'

# Delete files and objects
# list all the objects in bucket
response = s3_client.list_objects_v2(Bucket=bucket_name)

# pprint(response)

# Check if there are Contents in bucket
if 'Contents' in response:
    # Iterate over them (each object)
    for obj in response['Contents']:
        # pprint(obj)
        # Delete each object one by one 
        print(f"Deleting {obj['Key']}...")
        s3_client.delete_object(Bucket=bucket_name, Key=obj['Key'])

# Now that bucket is empty we can delete that 
print(f"Deleting bucket: {bucket_name}...")
s3_client.delete_bucket(Bucket=bucket_name)
