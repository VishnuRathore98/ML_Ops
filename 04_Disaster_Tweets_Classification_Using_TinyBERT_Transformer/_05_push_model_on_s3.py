import boto3
import os

s3_client = boto3.client('s3',region_name='ap-south-1')
bucket_name = "mlops-vpsr"
model_path="TinyBERT-disaster-tweets-analysis"
s3_prefix="ml-models/TinyBERT-disaster-tweets-analysis"

def upload_model(model_path, s3_prefix):
    for root, dirs, files in os.walk(model_path):
        for file in files:
            file_path = os.path.join(root, file)
            rel_path = os.path.relpath(file_path, model_path)
            s3_key = os.path.join(s3_prefix, rel_path)

            s3_client.upload_file(file_path, bucket_name, s3_key)

upload_model(model_path, s3_prefix)

print(f"Model uploaded successfully at {s3_prefix}")
