import os
import boto3

def lambda_handler(event, context): 
    
    # https://docs.aws.amazon.com/pt_br/lambda/latest/dg/services-apigateway-tutorial.html

    s3 = boto3.client('s3')
    bucket = os.environ['AWS_BUCKET']
    expire = os.environ['EXPIRE_IN']

    fileName = event['headers']['file_name']
    data = event['headers']['data']
    #returnType = event['headers']['return_type']

    urlFile = s3.generate_presigned_url(
    ClientMethod='get_object', 
    Params={'Bucket': bucket, 'Key': fileName},
    ExpiresIn=int(expire))    

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": {
            "url": urlFile
        }
    }


def lambda_handler_download_file(event, context): 
    
    # https://docs.aws.amazon.com/pt_br/lambda/latest/dg/services-apigateway-tutorial.html
    # bucket ex.: 'arn:aws:s3-object-lambda:us-east-1:123412341234:accesspoint/myolap'

    s3 = boto3.client('s3')
    bucket = os.environ['AWS_BUCKET']

    fileName = event['file_name']
    data = event['data']
    returnType = event['return_type']

    fileObject = s3.get_object(
        Bucket=bucket,
        Key=fileName + ".csv"
    )

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/CSV",
            "content-disposition" : "attachment; filename=\"" + fileName + ".csv\""
        },
        "body": fileObject['Body'].read().decode('utf-8')
    }