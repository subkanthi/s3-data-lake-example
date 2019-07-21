import pandas as pd
from etl_processor import columnNames
from s3_processor import S3Processor


class EtlProcessor:

    # Function to read columns from csv file
    # and return a pandas dataframe
    def parse_data_return_json(self, csv_file_name, bucket_name):
        df = pd.read_csv(csv_file_name, error_bad_lines=False)
        for col in df.columns:
            print(col)
        for index, row in df.iterrows():
            s3Key = self.create_s3key_from_dataframe(bucket_name, row)
            row_json = row.to_json()
            self.s3Processor.writeObject(row_json, s3Key)
        return df

    # Function to read columns from csv file
    # and return a pandas dataframe
    def parse_data_return_parquet(self, csv_file_name, bucket_name):
        df = pd.read_csv(csv_file_name, error_bad_lines=False)
        for col in df.columns:
            print(col)
        for index, row in df.iterrows():
            s3Key = self.create_s3key_from_dataframe(bucket_name, row)
            row_json = row.to_frame()
            self.s3Processor.writeObject(row_json, s3Key)
        return df


    # Function to create s3Key from the data frame.
    # This is the HIVE partitioning key, we use
    # recorded time and the MTA Line Number
    def create_s3key_from_dataframe(self, bucket_name, row):
        recordedTime = row[columnNames.columnNames.RECORDED_TIME]
        mtaLineNumber = row[columnNames.columnNames.PUBLISHED_LINE]
        columnNamesDict = dict()
        columnNamesDict[columnNames.columnNames.RECORDED_TIME] = recordedTime
        columnNamesDict[columnNames.columnNames.PUBLISHED_LINE] = mtaLineNumber
        self.s3Processor = S3Processor.S3Processor(bucket_name)

        # Writing the s3 partition based on HIVE partition
        s3Key = self.s3Processor.createS3Key(columnNamesDict)

        return s3Key