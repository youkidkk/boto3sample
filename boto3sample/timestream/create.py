import boto3
from botocore.config import Config

DATABASE_NAME = "sampleDB"
TABLE_NAME = "sample_tbl"


client = boto3.client(
    "timestream-write",
    config=Config(
        read_timeout=20,
        max_pool_connections=5000,
        retries={"max_attempts": 10},
    ),
)

try:
    res = client.create_database(
        DatabaseName=DATABASE_NAME,
        # KmsKeyId='string',
        # Tags=[
        #     {
        #         'Key': 'string',
        #         'Value': 'string'
        #     },
        # ]
    )
    print(res)
except client.exceptions.ConflictException as ex:
    print(ex)

try:
    res = client.create_table(
        DatabaseName=DATABASE_NAME,
        TableName=TABLE_NAME,
        RetentionProperties={
            "MemoryStoreRetentionPeriodInHours": 12,
            "MagneticStoreRetentionPeriodInDays": 5,
        },
        Tags=[
            {
                "Key": "sample",
                "Value": "sample value",
            }
        ],
        MagneticStoreWriteProperties={
            "EnableMagneticStoreWrites": True,
            # "MagneticStoreRejectedDataLocation": {
            #     "S3Configuration": {
            #         "BucketName": "string",
            #         "ObjectKeyPrefix": "string",
            #         "EncryptionOption": "SSE_S3" | "SSE_KMS",
            #         "KmsKeyId": "string",
            #     }
            # },
        },
    )
except client.exceptions.ConflictException as ex:
    print(ex)
