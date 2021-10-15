import pandas as pd
import sys

def main(path):
    # read excel file
    sheet_dict = pd.read_excel(path, sheet_name=None)
    rec_count = dict()
    for sheet in sheet_dict.keys():
        rec_count[sheet] = sheet_dict[sheet].shape[0]

    print(rec_count)


main('../sample_files/file_example_XLS_10.xls')