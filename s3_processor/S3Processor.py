import boto3 as boto3

# Class to write objects to s3.
class S3Processor:
    def __init__(self, s3_bucket_name):
        print("S3 Bucket name" + s3_bucket_name)
        self.bucket_name = s3_bucket_name
        self.s3 = boto3.resource('s3')

    # The following partition is similar to
    # HIVE Partition
    # s3: // yourBucket / pathToTable / < PARTITION_COLUMN_NAME >= < VALUE > / < PARTITION_COLUMN_NAME >= < VALUE > /
    def createPartition(self, column_name, column_value):
        pass


    # We are converting every row in the CSV to an object
    def writeObject(self, data, key):
        object = self.s3.Object(self.bucket_name, key)
        object.put(Body=data)
       # object.put(Body=some_binary_data)

    # function to create a key in this following format
    # key1=value1/key2=value2
    def createS3Key(self, column_name_dict):
        s3key = ''
        for key, value in column_name_dict.items():
            s3key = key + '=' + value + '/'
        print(s3key)
        return s3key



