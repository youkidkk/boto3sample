from datetime import datetime

import boto3

queue_name = "sample"
resource = boto3.resource("sqs")

try:
    queue = resource.get_queue_by_name(QueueName=queue_name)
except Exception as e:
    print(e)
    queue = resource.create_queue(QueueName=queue_name)

for _ in range(5):
    res = queue.send_message(
        MessageBody="Hello Boto3 SQS",
        MessageAttributes={
            "DateTime": {"StringValue": str(datetime.now()), "DataType": "String"}
        },
    )
    print(res)
