# load tools
import pandas as pd
import os

path = 'data/2021/'

# creates list with files to merge based on name convention
file_list = [path + f for f in os.listdir(path) if f.endswith('.csv')]

# print list for validation, wait for user input before continue
print(file_list)
input("Press Enter to continue...")

# creates empty list to include the content of each file converted to pandas DF
csv_list = []

# defines cols and dtypes
cols = ['STATION', 'NAME', 'LATITUDE', 'LONGITUDE' 'CALL_SIGN',]
#dtypes = {'STATION': int, 'NAME': object, 'CALL_SIGN': object}

# reads each (sorted) file in file_list, converts it to pandas DF, filters for CALL_SIGN and REPORT_TYPE, and appends it to the csv_list
for file in sorted(file_list):
    csv_file = pd.read_csv(file, usecols=lambda c: c in cols, encoding_errors='ignore', index_col=None, header=0)
#    csv_file = csv_file.drop(csv_file[csv_file.CALL_SIGN == '99999'])# | csv_file.CALL_SIGN == '99999'])
#    csv_file = csv_file.drop(csv_file[csv_file.CALL_SIGN == '99999'])
#    df = df.drop(df[(df.score < 50) & (df.score > 20)].index)
#    stations = csv_file.CALL_SIGN.unique()
#    print('stations:',stations)
#    print('rows added:',csv_file.shape)
#    print('###########################################################')
    csv_list.append(csv_file)
    print(file)
'auni'
# merges single pandas DFs into a single DF, index is refreshed
# pd.info(csv_list)
print('merging data...')
csv_merged = pd.concat(csv_list, ignore_index=True)
# pd.info(csv_merged)
print(csv_merged.info())

# print(csv_merged.shape)
# print(csv_merged.CALL_SIGN.unique())
print('data complete... saving file...')

# Single DF is saved to the path in CSV format, without index column
csv_merged.to_csv('data/unique-stations.csv', index=False)
print('file saved')
