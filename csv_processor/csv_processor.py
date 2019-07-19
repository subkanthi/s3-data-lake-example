import pandas as pd
from csv_processor import columnNames
from s3_processor import S3Processor


class CsvProcessor:
    # Function to read columns from csv file
    # and return a pandas dataframe
    def parse_csv(self, csv_file_name):
        df = pd.read_csv(csv_file_name, error_bad_lines=False)
        #print(df)
        #for col in df.columns:
            #print(col)
        for index, row in df.iterrows():
            #print(row[columnNames.columnNames.DESTINATION_LAT], row[columnNames.columnNames.DESTINATION_LONG])
            recordedTime = row[columnNames.columnNames.RECORDED_TIME]
            mtaLineNumber = row[columnNames.columnNames.PUBLISHED_LINE]
            columnNamesDict = dict()
            columnNamesDict[columnNames.columnNames.RECORDED_TIME] = recordedTime
            columnNamesDict[columnNames.columnNames.PUBLISHED_LINE] = mtaLineNumber

            # Writing the s3 partition based on HIVE partition
            s3Key = S3Processor.S3Processor('newyorktrips-partitioned').createS3Key( columnNamesDict)
            print(s3Key)
        return df