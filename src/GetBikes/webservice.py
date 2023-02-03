import os
import json
import boto3
from boto3.dynamodb.conditions import Key

def lambda_handler(message, context):
    
    print("DEBUG Message: " + str(message))
    print("DEBUG Context: " + str(context))
    
    if ('pathParameters' not in message or
            message['httpMethod'] != 'GET'):
        return {
            'statusCode': 400,
            'headers': {},
            'body': json.dumps({'msg': 'Bad Request'})
        }

    table_name = os.environ.get('TABLE', 'Bikes')
    region = os.environ.get('REGION', 'eu-west-1')
    aws_environment = os.environ.get('AWSENV', 'AWS')

    dynamodb = boto3.resource('dynamodb',region_name=region)

    table = dynamodb.Table(table_name)
    vin = message['pathParameters']['vin']

    response = table.query(KeyConditionExpression=Key('vin').eq(vin))
    print("DEBUG Response: " + str(response))

    return {
        'statusCode': 200,
        'headers': {},
        'body': json.dumps(response['Items'])
    }

