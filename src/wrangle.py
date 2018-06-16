import csv
from pathlib import Path

DATA_DIR = Path('files', 'data')
DEST_PATH = DATA_DIR.joinpath('global-temps-data.wrangled.csv')
SRC_PATH = DATA_DIR.joinpath('global-temps-data.original.txt')
HEADERS = ['year','annual_mean','lowess']

def read_and_wrangle():
    data = []
    with open(SRC_PATH, 'r') as _s:
        src = csv.reader(_s, delimiter='\t')
        for row in src:
            data.append(row)
    return data

def write_data(data):
    with open(DEST_PATH, 'w') as _d:
        dest = csv.writer(_d)
        dest.writerow(HEADERS)
        for d in data:
            dest.writerow(d)


if __name__ == '__main__':
    data = read_and_wrangle()
    write_data(data)

    print("Wrote", len(data), "rows to:", DEST_PATH)


