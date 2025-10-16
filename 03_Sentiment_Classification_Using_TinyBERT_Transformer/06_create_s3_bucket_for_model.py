import boto3

s3_client = boto3.client('s3', region_name='ap-south-1')

bucket_name = "mlops-vpsr"

def create_bucket(bucket_name):
    response = s3_client.list_buckets()
    buckets = [bucket['Name'] for bucket in response['Buckets']]
    if bucket_name not in buckets:
        s3_client.create_bucket(Bucket=bucket_name,
                                CreateBucketConfiguration={'LocationConstraint':'ap-south-1'})
        print("bucket created successfully!")
    else:
        print("bucket already exists!")

create_bucket(bucket_name)
