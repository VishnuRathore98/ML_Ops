import boto3
from pprint import pprint

s3_client = boto3.client('s3', region_name='ap-south-1')

bucket_name = 'test93839'

buckets = s3_client.list_buckets()

pprint(buckets['Buckets'])

s3_client.create_bucket(
    Bucket=bucket_name, 
    CreateBucketConfiguration={'LocationConstraint':'ap-south-1'}
)

pprint(buckets['Buckets'])

