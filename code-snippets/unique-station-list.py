# import
import pandas as pd
import os
import csv

# define path to data
path = '../data/2021/'

# creates list of .csv files in path and print list for user confirmation
file_list = [path + f for f in os.listdir(path) if f.endswith('.csv')]
print(file_list)
# input("Press Enter to continue...")

# creates empty list to include the content of each file converted to pandas DF
csv_data = []

# columns to use
cols = ['STATION', 'NAME', 'LATITUDE', 'LONGITUDE', 'CALL_SIGN']

# reads each (sorted) file in file_list, converts it to pandas DF and appends it to the csv_list
for file in sorted(file_list):
    csv_file = pd.read_csv(file, usecols=lambda c: c in cols, encoding_errors='ignore', index_col=None, header=0)
    csv_data.append(csv_file)
    print(file)

# merges single pandas DFs into a single DF, index is refreshed
print('merging data...')
data = pd.concat(csv_data, ignore_index=True)

# find unique stations
data = data.groupby(['STATION', 'CALL_SIGN']).size().reset_index().rename(columns={0: 'count'})
data = data[(data.CALL_SIGN != 99999) & (data.CALL_SIGN != '99999')].reset_index(drop='True')

print('data complete... saving file...')
# Single DF is saved to the path in CSV format, without index column
data.to_csv('station-list-edited.csv', index=False)
print('file saved')

'''
file = open('unique-stations.csv' , 'r')
station_list = list(csv.reader(file, delimiter=','))
file.close()
print(station_list)

with open("unique-stations.csv", "r") as source:
    reader = csv.reader(source)

    with open("station-list-edited.csv", "w") as result:
        writer = csv.writer(result)
        for r in reader:
            # Use CSV Index to remove a column from CSV
            # r[0] = r['index'] r[3] = r['count']
            writer.writerow((r[1], r[2]))
'''
