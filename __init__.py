
import sys
import csv_processor.csv_processor as csvp;

def main():
    if len(sys.argv[1]) == 0:
        print("Pass a valid filename argument")


    # print command line arguments
    for arg in sys.argv[1:]:
        print("Filename: " + arg)
        csvp.CsvProcessor().parse_csv(arg)



if __name__ == "__main__":
    main()