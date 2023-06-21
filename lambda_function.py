import json
import uuid
import boto3
from decimal import Decimal


def lambda_handler(event, context):
    body = json.loads(event["Records"][0]["body"])
    message = json.loads(body["Message"])

    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table("people")

    table.put_item(
        Item={
            "id": str(uuid.uuid4()),
            "content": message
        }
    )

    return {"statusCode": 200, "body": json.dumps("the request was successful")}