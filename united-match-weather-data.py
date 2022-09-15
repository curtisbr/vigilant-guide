# tools
import pandas as pd

metar2018 = pd.read_csv('data/metar-2018.csv', parse_dates=['DATE'])
# metar2019 = pd.read_csv('data/metar-2019.csv')
metar2018['DATE'] = pd.to_datetime(metar2018['DATE'], utc=['True'])
print('metar data...')
metar2018['STATIONDATETIME'] = metar2018['STATION'].astype('string') + metar2018['DATE'].astype('string')
metar2018 = metar2018.sort_values(by='STATIONDATETIME')
print(metar2018.STATIONDATETIME)

stations = pd.read_csv('data/station-list.csv')
stations['CALL_SIGN'] = stations['CALL_SIGN'].str.replace(' ', '')
stations['CALL_SIGN'] = stations['CALL_SIGN'].str[-3:]
print('stations...')
print(stations)


united = pd.read_csv('data/united/united-flights-matching.csv', parse_dates=['DESTOBSERVATIONTIME'])
united['DEST'] = united['DEST'].str.replace(' ', '')
# united['DESTOBSERVATIONTIME'] = united['DESTOBSERVATIONTIME'].str.replace(' ', '')
# united['DESTOBSERVATIONTIME'] = united['DESTOBSERVATIONTIME'].str.replace('T', ' ')
# united['DESTOBSERVATIONTIME'] = united['DESTOBSERVATIONTIME'].str.replace('Z', '')
united['DESTOBSERVATIONTIME'] = pd.to_datetime(united['DESTOBSERVATIONTIME'], utc='True')
print('united data...')
print(united.DESTOBSERVATIONTIME)

united_merge = pd.merge(united, stations, how='left', left_on='DEST', right_on='CALL_SIGN')
del united_merge[united_merge.columns[0]]
united_merge = united_merge.drop(columns=['count', 'CALL_SIGN'])
united_merge['STATIONDATETIME'] = united_merge['STATION'].astype('string') + united_merge['DESTOBSERVATIONTIME'].astype('string')
united_merge = united_merge.sort_values(by='STATIONDATETIME')
print(united_merge.STATIONDATETIME)

print('united data plus station ID...')
print(united_merge)
united_merge.to_csv('data/united/united_merge.csv')
print('file saved to /data/united/united_merge.csv')

data = pd.merge_asof(left=united_merge, right=metar2018, left_on='STATIONDATETIME', right_on='STATIONDATETIME', direction='nearest')
print('match data...')
print(data)

# data.to_csv('data/united/united-metar.csv')
# print('file saved to /data/united/united-metar.csv')