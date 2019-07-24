import pyarrow.parquet as pq
import pyarrow as pa
import boto3 as boto3

class ParquetProcessor:
    def __init__(self):
        pass

#write_pandas_parquet_to_s3(
       # df, "bucket", "folder/test/file.parquet", ".tmp/file.parquet")

    def  write_pandas_parquet_to_s3(self, df, bucketName, keyName, fileName):
        # dummy dataframe
        table = pa.Table.from_pandas(df)
        pq.write_table(table, fileName)

        # upload to s3
        s3 = boto3.client("s3")
        BucketName = bucketName
        with open(fileName, 'rb') as f:
            object_data = f.read()
            s3.put_object(Body=object_data, Bucket=BucketName, Key=keyName)