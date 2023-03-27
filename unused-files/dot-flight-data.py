# load tools
import csv
import pandas as pd

c = ['FlightDate',
     'Operating_Airline ',
     'Tail_Number',
     'Flight_Number_Operating_Airline',
     'Origin',
     'Dest',
     'CRSDepTime',
     'DepTime',
     'DepDelay',
     'DepDelayMinutes',
     'CRSArrTime',
     'ArrTime',
     'ArrDelay',
     'ArrDelayMinutes',
     'CarrierDelay',
     'WeatherDelay',
     'NASDelay',
     'SecurityDelay',
     'LateAircraftDelay',
     'Cancelled',
     'Diverted']

path = 'data/flights/On_Time_Marketing_Carrier_On_Time_Performance_Beginning_January_2018_2018_' + '1' + '/On_Time_Marketing_Carrier_On_Time_Performance_(Beginning_January_2018)_2018_1.csv'

file_list = []

for row in cf:
    file_list.append('data/2018/' + row['stationid'] + '.csv')
    file_list.append('data/2019/' + row['stationid'] + '.csv')

f = pd.read_csv(path, usecols=c)

print(f.shape)