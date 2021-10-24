import boto3

s3 = boto3.client('s3')

url = s3.generate_presigned_url(
    ClientMethod='get_object', 
    Params={'Bucket': 'BUCKET_NAME', 'Key': 's3.txt'},
    ExpiresIn=3600)

print('Object processed by S3 Object Lambda:')

transformed = s3.get_object(
  Bucket='arn:aws:s3-object-lambda:us-east-1:123412341234:accesspoint/myolap',
  Key='s3.txt')

print(transformed['Body'].read().decode('utf-8'))

print(url)
