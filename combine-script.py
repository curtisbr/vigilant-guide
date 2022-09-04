# load tools
import pandas as pd
import os

# step 1: defines path to csv files
year = input("Define year to combine:")
path = 'data/'+year+'/'
print("load .csv files from "+path)
print("combined file will save to data/merged-"+year+".csv")
input("Press Enter to continue...")

# step 2: creates list with files to merge based on name convention
file_list = [path + f for f in os.listdir(path) if f.endswith('.csv')]

# step 3: print list for validation, wait for user input before continue
print(file_list)
input("Press Enter to continue...")

# step 4: creates empty list to include the content of each file converted to pandas DF
csv_list = []

# step 5: defines cols and dtypes to consider
cols = ['STATION', 'SOURCE', 'DATE', 'LATITUDE', 'LONGITUDE', 'ELEVATION', 'NAME', 'REPORT_TYPE', 'CALL_SIGN', 'WND', 'CIG', 'VIS', 'TMP', 'DEW', 'SLP', 'REM']

## bringing all cols in as strings to avoid errors
dtypes = {'STATION': object, 'SOURCE': object, 'LATITUDE': object, 'LONGITUDE': object, 'ELEVATION': object, 'NAME': object, 'REPORT_TYPE': object, 'CALL_SIGN': object, 'WND': object, 'CIG': object, 'VIS': object, 'TMP': object, 'DEW': object, 'SLP': object, 'REM': object}

# step 6: reads each (sorted) file in file_list, converts it to pandas DF and appends it to the csv_list
for file in sorted(file_list):
    csv_file = pd.read_csv(file, parse_dates=['DATE'], usecols=lambda c: c in cols, encoding_errors='ignore', index_col=None, header=0)
    csv_file = csv_file[csv_file['CALL_SIGN']!=99999]
    csv_file = csv_file[csv_file['CALL_SIGN']!='99999']
    csv_15 = csv_file[csv_file['REPORT_TYPE']=='FM-15']
    csv_16 = csv_file[csv_file['REPORT_TYPE']=='FM-16']
    csv_file = pd.concat([csv_15, csv_16], axis=0, ignore_index=True)
    stations = csv_file.CALL_SIGN.unique()
    print(stations)
    print('rows added: ',csv_file.shape)
    print('###########################################################')
    csv_list.append(csv_file)
    print(file)

# step 7: merges single pandas DFs into a single DF, index is refreshed
print('merging data...')
csv_merged = pd.concat(csv_list, ignore_index=True)
print('data merged, saving file')
print(csv_merged.shape)
print(csv_merged.CALL_SIGN.unique())

# step 8: Single DF is saved to the path in CSV format, without index column
csv_merged.to_csv('data/merged-'+year+'.csv', index=False)
print('file saved to /data/merged-'+year+'.csv')
