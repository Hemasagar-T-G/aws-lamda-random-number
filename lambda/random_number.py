import json
import random

def lambda_handler(event, context):
    number = random.randint(1, 100)
    return {
        'statusCode': 200,
        'body': json.dumps({'random_number': number})
    }
