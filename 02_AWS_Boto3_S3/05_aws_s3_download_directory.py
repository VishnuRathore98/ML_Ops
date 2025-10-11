import boto3
import os
from pprint import pprint

s3_client = boto3.client('s3', region_name='ap-south-1')

bucket_name = 'test93839'
local_path = 'data/download'
s3_prefix = 'data'

# Create the local path if does not exists
os.makedirs(local_path, exist_ok=True)

paginator = s3_client.get_paginator('list_objects_v2')

for result in paginator.paginate(Bucket=bucket_name, Prefix=s3_prefix):
    
    if 'Contents' in result:
        for key in result['Contents']:
            
            s3_key = key['Key']
            rel_path = os.path.relpath(s3_key,s3_prefix)
            local_file = os.path.join(local_path, rel_path)
            print("s3_key:",s3_key)
            print("rel_path",rel_path)
            print("local_path",local_file)
           
            # This will read the file from bucket 'test93839' from the provided
            # s3 file path i.e. 'data/test1.txt' and write to the specified file
            # locally i.e. 'data/download/test1.txt', it does not create file if
            # it does not already mentioned and exists.
            s3_client.download_file(bucket_name, s3_key, local_file)
