import os
import json
import random
import string
import boto3
from boto3.dynamodb.conditions import Key

def lambda_handler(message, context):
    
    print("DEBUG Message: " + str(message))
    print("DEBUG Context: " + str(context))

    if ('body' not in message or
            message['httpMethod'] != 'PUT'):
        return {
            'statusCode': 400,
            'headers': {},
            'body': json.dumps({'msg': 'Bad Request'})
        }
    
    bike_info = json.loads(message['body'])
    vin = message['pathParameters']['vin']
    
    table_name = os.environ.get('TABLE', "Bikes")
    region = os.environ.get('REGION', 'eu-west-1')
    aws_environment = os.environ.get('AWSENV', 'AWS')

    primary_key = {
        "vin" : vin,
        "brand" : bike_info['brand']
    }

    dynamodb = boto3.resource('dynamodb',region_name=region)
    table = dynamodb.Table(table_name)
    response = table.update_item(
        Key=primary_key,
        UpdateExpression="set model = :model",
        ExpressionAttributeValues={
            ':model': bike_info['model']
        },
        ReturnValues="UPDATED_NEW"
    )

    print("DEBUG Response: " + str(response))
   
    return {
        'statusCode': 201,
        'headers': {
            'headers': {
            "x-custom-version" : "2.1"
            },
        },
        'body': json.dumps({'msg': 'Bike created'+vin})
    }

