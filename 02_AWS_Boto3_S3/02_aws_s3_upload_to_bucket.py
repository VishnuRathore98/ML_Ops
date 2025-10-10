import boto3
import os

s3_client = boto3.client('s3', region_name='ap-south-1')

# bucket to upoad to 
bucket_name = 'test93839'

# file to upload
file_path = './index.html'

# extracts just the file or folder name from a full path — removing the directory part.
object_name = os.path.basename(file_path)

# upload to bucket
s3_client.upload_file(file_path, bucket_name, object_name)

# list all objects in s3
response = s3_client.list_objects_v2(Bucket=bucket_name)

for obj in response['Contents']:
    print(obj)
