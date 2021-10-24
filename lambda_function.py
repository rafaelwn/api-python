import boto3

def lambda_handler(event, context): 
    
    # https://docs.aws.amazon.com/pt_br/lambda/latest/dg/services-apigateway-tutorial.html

    s3 = boto3.client('s3')

    fileName = event['file_name']
    data = event['data']
    returnType = event['return_type']

    fileObject = s3.get_object(
        Bucket='arn:aws:s3-object-lambda:us-east-1:123412341234:accesspoint/myolap',
        Key=fileName
    )
    # Retorna o conteudo do arquivo
    #return transformed['Body'].read().decode('utf-8')
    return fileObject