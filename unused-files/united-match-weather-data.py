# tools
import pandas as pd

# read metar data from 2018-2020, merge into one data frame
metar = pd.read_csv('data/united/united-metar-data.csv', parse_dates=['DATE'])
metar['DATE'] = pd.to_datetime(metar['DATE'], utc='True')
print('metar data...')
print(metar['DATE'])


# read united station list
stations = pd.read_csv('data/united/station-list.csv', header=None, dtype={0: str, 1: str})
stations.rename(columns={0: 'CALL_SIGN', 1: 'STATION'})
stations[1] = stations[1].str.zfill(11)
print('stations...')
print(stations)

# read united flight data
flights = pd.read_csv('data/united/united-flights.csv', parse_dates=['DESTOBSERVATIONTIME'])
flights['DEST'] = flights['DEST'].str.replace(' ', '')
flights['DATE'] = pd.to_datetime(flights['DESTOBSERVATIONTIME'], utc='True')
print('flight data...')
print(flights[{'DATE', 'DEST'}])

# merge united destination and station call sign to matching weather station ID
flights = pd.merge(flights, stations, how='left', left_on='DEST', right_on=0)
del flights[flights.columns[0]]
print('united data plus station ID...')
print(flights)
# united_merge.to_csv('data/united/prelim/united-flights.csv')


# merge METAR string into
data = pd.merge_asof(left=flights, right=metar, on='DATE', direction='nearest', left_by=1, right_by='STATION')

# data.to_csv('data/united/united-metar.csv')
# print('file saved to /data/united/united-metar.csv')