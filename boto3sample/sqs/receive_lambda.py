def lambda_handler(event, context):
    for record in event["Records"]:
        print(str(record))
