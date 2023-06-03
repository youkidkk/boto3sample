import random
import time

import boto3
from botocore.config import Config

DATABASE_NAME = "sampleDB"
TABLE_NAME = "sample_tbl"


dimensions = [
    [
        {"Name": "Name", "Value": "Taro"},
        {"Name": "Age", "Value": "30"},
    ],
    [
        {"Name": "Name", "Value": "Jiro"},
        {"Name": "Age", "Value": "20"},
    ],
    [
        {"Name": "Name", "Value": "Hanako"},
        {"Name": "Age", "Value": "25"},
    ],
]

client = boto3.client(
    "timestream-write",
    config=Config(
        read_timeout=20,
        max_pool_connections=5000,
        retries={"max_attempts": 10},
    ),
)
for _ in range(10):
    current_time = str(round(time.time() * 1000))

    records = []
    for dms in dimensions:
        records.append(
            {
                "Dimensions": dms,
                "MeasureName": "Temperature",
                "MeasureValue": str(36.0 + random.randint(0, 10) / 10),
                "MeasureValueType": "DOUBLE",
                "Time": current_time,
            }
        )

    res = client.write_records(
        DatabaseName=DATABASE_NAME,
        TableName=TABLE_NAME,
        Records=records,
        CommonAttributes={},
    )
    print(res)
    time.sleep(1)
