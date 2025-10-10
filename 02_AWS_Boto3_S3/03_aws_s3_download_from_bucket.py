import boto3
import os

s3_client = boto3.client('s3', region_name='ap-south-1')

bucket_name = 'test93839'

file_to_download = 'index.html'

path_to_download = './data/download/index.html'

# check if path_to_download exists
if not os.path.exists(os.path.dirname(path_to_download)):
    # if not then create the dir 
    os.makedirs(os.path.dirname(path_to_download))

# download the file from s3 to local 
s3_client.download_file(bucket_name, file_to_download, path_to_download)
