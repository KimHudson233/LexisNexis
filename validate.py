import io
import boto3

def verify():
    s3_client = boto3.client('s3', endpoint_url='http://localhost:4566', region_name='us-east-1',
                         aws_secret_access_key='x', aws_access_key_id='x')
    
    # https://docs.aws.amazon.com/boto3/latest/reference/services/s3/client/create_bucket.html
    bucket_name = 'kims-bucket'
    print('Creating bucket');
    s3_client.create_bucket(Bucket=bucket_name)
    
    # https://docs.aws.amazon.com/boto3/latest/reference/services/s3/client/list_buckets.html
    response = s3_client.list_buckets()
    bucket_names = [b.get('Name') for b in response.get('Buckets', [])]
    print('Buckets: ' + ', '.join(bucket_names))

    # https://docs.aws.amazon.com/boto3/latest/reference/services/s3/client/upload_file.html
    print('Adding file by upload')
    s3_client.upload_file('README.md', bucket_name, 'README-upload.md')

    # https://docs.aws.amazon.com/boto3/latest/reference/services/s3/client/put_object.html
    print('Adding file by put')
    s3_client.put_object(Bucket=bucket_name, Key='README-put.md', Body=open('README.md', 'rb'))

    # https://docs.aws.amazon.com/boto3/latest/reference/services/s3/client/list_objects.html
    response = s3_client.list_objects(Bucket=bucket_name)
    object_keys = [c.get('Key') for c in response.get('Contents', [])]
    print('Objects: ' + ', '.join(object_keys))

    # https://docs.aws.amazon.com/boto3/latest/reference/services/s3/client/get_object.html
    print('Reading objects')
    for key in object_keys:
        response = s3_client.get_object(Bucket=bucket_name, Key=key)
        print('  ' + key + ' size = ' + str(len(response.get('Body').read().decode('utf-8'))))

    # https://docs.aws.amazon.com/boto3/latest/reference/services/s3/client/delete_object.html
    print('Deleting objects')
    for key in object_keys:
        s3_client.delete_object(Bucket=bucket_name, Key=key)

    # https://docs.aws.amazon.com/boto3/latest/reference/services/s3/client/delete_bucket.html
    print('Deleting buckets')
    for bucket in bucket_names:
        s3_client.delete_bucket(Bucket=bucket)

if __name__ == '__main__':
    verify()
