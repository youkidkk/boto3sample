import boto3

DATABASE_NAME = "sampleDB"
TABLE_NAME = "sample_tbl"

client = boto3.client("timestream-query")

query_str = (
    f"SELECT time, Name, Age, measure_value::double as Temperature "
    f"FROM {DATABASE_NAME}.{TABLE_NAME} "
    "WHERE time between ago(60m) and now() ORDER BY time DESC LIMIT 50 "
)

next_token = None
while True:
    if next_token is None:
        res = client.query(QueryString=query_str, MaxRows=3)
    else:
        res = client.query(QueryString=query_str, MaxRows=3, NextToken=next_token)

    columns = list(map(lambda d: d.get("Name"), res.get("ColumnInfo")))
    rows = res.get("Rows")
    next_token = res.get("NextToken")

    print(f"Rows: {len(rows)}")
    if len(rows) > 0:
        for row in rows:
            record = {}
            for i, c in enumerate(columns):
                record[c] = row.get("Data")[i].get("ScalarValue")
            print(record)
    if next_token is None:
        break
    print(f"NextToken: {next_token[:10]}...")
