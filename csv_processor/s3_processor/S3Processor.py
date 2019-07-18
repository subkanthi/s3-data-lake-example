import boto3 as boto


# Class to write objects to s3.
class S3Processor:
    def __init__(self, s3_bucket_name):
        print("S3 Bucket name" + s3_bucket_name)
        self.bucket_name = s3_bucket_name


    # The following partition is similar to
    # HIVE Partition
    # s3: // yourBucket / pathToTable / < PARTITION_COLUMN_NAME >= < VALUE > / < PARTITION_COLUMN_NAME >= < VALUE > /
    def createPartition(self, column_name, column_value):
        pass


    # We are converting every row in the CSV to an object
    def writeObject(self, object):