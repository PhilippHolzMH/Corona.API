import logging
import boto3
from botocore.exceptions import ClientError
s3_client = boto3.client('s3', 'eu-central-1')

def create_bucket(bucket_name, region,s3_client):
    try:
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True
   
   