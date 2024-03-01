import boto3

def list_public_s3_buckets():
    # Create an S3 client
    s3_client = boto3.client('s3')

    # List all S3 buckets
    response = s3_client.list_buckets()

    # Iterate through each bucket and check for public access
    for bucket in response['Buckets']:
        bucket_name = bucket['Name']

        # Check if the bucket has public access
        public_access = check_bucket_public_access(s3_client, bucket_name)

        if public_access:
            print(f"S3 Bucket '{bucket_name}' has public access.")

def check_bucket_public_access(s3_client, bucket_name):
    # Get the bucket policy
    try:
        response = s3_client.get_bucket_policy_status(Bucket=bucket_name)
        return response['PolicyStatus']['IsPublic']
    except s3_client.exceptions.NoSuchBucketPolicy:
        return False

if __name__ == "__main__":
    list_public_s3_buckets()
