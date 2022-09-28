# tool import
import csv
import pandas as pd

# create file list united destination airport weather stations to pul data from
file_list = []
with open('data/united/station-list.csv') as f:
    cf = csv.DictReader(f, fieldnames=['airport', 'stationid'])
    for row in cf:
        file_list.append('data/2018/' + row['stationid'] + '.csv')
        file_list.append('data/2019/' + row['stationid'] + '.csv')

# creates empty list to include the content of each file converted to pandas DF
csv_list = []

# reads each (sorted) file in file_list, converts it to pandas DF and appends it to the csv_list
cols = ['STATION', 'DATE', 'REPORT_TYPE', 'REM', 'WND', 'CIG', 'VIS', 'TMP', 'DEW', 'SLP']
dtypes = {'STATION': int, 'REPORT_TYPE': object, 'REM': object}
for file in sorted(file_list):
    csv_file = pd.read_csv(file, parse_dates=['DATE'], usecols=lambda c: c in cols, encoding_errors='ignore',
                           index_col=None, header=0)
    csv_15 = csv_file[csv_file['REPORT_TYPE'] == 'FM-15']
    csv_16 = csv_file[csv_file['REPORT_TYPE'] == 'FM-16']
    csv_file = pd.concat([csv_15, csv_16], axis=0, ignore_index=True)
    csv_list.append(csv_file)
    print(file)

# merges single pandas DFs into a single DF, index is refreshed
print('merging data...')
csv_merged = pd.concat(csv_list, ignore_index=True)
print(csv_merged.info())

# Single DF is saved to the path in CSV format, without index column
csv_merged.to_csv('data/united/united-metar-data.csv', index=False)
print('data/united/united-metar-data.csv')
