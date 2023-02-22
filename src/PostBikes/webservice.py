from ast import Param
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
            message['httpMethod'] != 'POST'):
        return {
            'statusCode': 400,
            'headers': {},
            'body': json.dumps({'msg': 'Bad Request'})
        }

    bike_info = json.loads(message['body'])
    vin = random.choices(string.ascii_uppercase + string.digits, k=6)
    vin = ''.join(vin)
    
    table_name = os.environ.get('TABLE', "Bikes")
    region = os.environ.get('REGION', 'eu-west-1')
    aws_environment = os.environ.get('AWSENV', 'AWS')

    item = {
        'vin': vin,
        'brand': bike_info['brand'],
        'model': bike_info['model']
    }

    dynamodb = boto3.resource('dynamodb',region_name=region)
    table = dynamodb.Table(table_name)
    response = table.put_item(TableName=table_name,Item=item)

    print("DEBUG Response: " + str(response))
   
    return {
        'statusCode': 200,
        'headers': {
            'headers': {
            "x-custom-version" : "2.1"
            },
        },
        'body': json.dumps({'msg': 'Bike updated '.join(vin)})
    }

