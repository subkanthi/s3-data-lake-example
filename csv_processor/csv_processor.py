import pandas as pd


class CsvProcessor:
    # Function to read columns from csv file
    # and return a pandas dataframe
    def parse_csv(self, csv_file_name):
        df = pd.read_csv(csv_file_name, error_bad_lines=False)
        #print(df)
        for col in df.columns:
            print(col)
        return df