import boto3

queue_name = "sample"
resource = boto3.resource("sqs")

try:
    queue = resource.get_queue_by_name(QueueName=queue_name)
except Exception as e:
    print(e)
    queue = resource.create_queue(QueueName=queue_name)

while True:
    msgs = queue.receive_messages(
        MessageAttributeNames=["DateTime"], MaxNumberOfMessages=10
    )
    if msgs:
        for msg in msgs:
            print(msg.message_attributes["DateTime"]["StringValue"], msg.body)
            msg.delete()
    else:
        break
