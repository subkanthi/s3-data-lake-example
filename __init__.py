
import sys
import etl_processor.etl_processor as etlp;

S3_JSON_BUCKET_NAME = 'newyorktrips-partitioned'
S3_PARQUET_BUCKET_NAME = 'newyorktrips-partitioned-parquet'

def main():
    if len(sys.argv[1]) == 0:
        print("Pass a valid filename argument")


    # print command line arguments
    for arg in sys.argv[1:]:

        # This is used to do a ETL job
        # on the CSV file and create the data lake files in JSON format
        # The data lake is created in S3.
        etlp.EtlProcessor().parse_data_return_json(arg, S3_JSON_BUCKET_NAME)

        etlp.EtlProcessor().parse_data_return_parquet(arg, S3_PARQUET_BUCKET_NAME)

if __name__ == "__main__":
    main()