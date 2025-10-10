import boto3
import os

s3_client = boto3.client('s3', region_name='ap-south-1')

bucket_name = 'test93839'
dir_path = 'data/upload'
s3_prefix = 'data'

# walk through the data dir 
for root, dir, files in os.walk(dir_path):
    
    # recursively print the root, dir in it and files in it
    #print("root:", root, "\ndir:", dir, "\nfiles:", files)

    # create dir path for all available files 
    for file in files:
        file_path = os.path.join(root, file)
        # file_path = data/upload/test1.txt

        # Computes the relative path from one location to another
        rel_path = os.path.relpath(file_path, dir_path)
        # rel_path = test1.txt
        
        # Create file path for bucket
        s3_key = os.path.join(s3_prefix, rel_path)
        # s3_key = data/test1.txt

        # Get file from file_path, put on bucket_name at s3_key
        s3_client.upload_file(file_path, bucket_name, s3_key)
