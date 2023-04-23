# Boto3 is a popular Python library used for interacting with Amazon Web Services (AWS) 
# resources such as S3, EC2, DynamoDB, and many others. It provides a simple and intuitive 
# API for developers to manage and automate their AWS infrastructure using Python.

import boto3
import logging
import os


# Also Added these inline policies
# {
#     "Version": "2012-10-17",
#     "Statement": [
#         {
#             "Effect": "Allow",
#             "Action": [
#                 "s3:ListAllMyBuckets",
#                 "s3:ListBucket"
#             ],
#             "Resource": [
#                 "arn:aws:s3:::*"
#             ]
#         }
#     ]
# }
# {
#     "Version": "2012-10-17",
#     "Statement": [
#         {
#             "Effect": "Allow",
#             "Action": [
#                 "s3:CreateBucket"
#             ],
#             "Resource": [
#                 "arn:aws:s3:::your-bucket-name"
#             ]
#         }
#     ]
# }


# Read the list of existing buckets
def list_bucket():
    # Create bucket
    try:
        s3 = boto3.client('s3')
        response = s3.list_buckets()
        if response:
            for bucket in response['Buckets']:
                print(f'  {bucket["Name"]}')
    except Exception as e:
        logging.error(e)
        return False
    return True

## Create AWS S3 bucket using python boto3
def create_bucket(bucket_name, region=None):
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except Exception as e:
        logging.error(e)
        return False
    return True

# Upload a file from local system.
def upload_file(file_name, bucket, object_name=None):
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except Exception as e:
        logging.error(e)
        return False
    return True

# Download a file from a S3 bucket.
def download_file(file_name, bucket, object_name):
    s3_client = boto3.client('s3')
    try:
        s3_client.download_file(bucket, object_name, file_name)
    except Exception as e:
        logging.error(e)
        return False
    return True
 

# Listing Buckets
list_bucket()

# # Calling Create Bucket
result_create = create_bucket("steeleyedata", "ap-south-1")


# # Upload a file to bucket
result_upload = upload_file("D:/Steeleye/DLTINS_20210117_01of01.csv", "steeleyedata", "DLTINS_20210117_01of01.csv")

# Download a file from bucket
result_download = download_file("D:\Steeleye\Downloaded.csv", "steeleyedata", "DLTINS_20210117_01of01.csv")
