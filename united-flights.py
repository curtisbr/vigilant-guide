# tools
import pandas as pd

cols = ['FLIGHTDATE',
        'FLIGHTNO',
        'DEST',
        'DESTOBSERVATIONTIME']

flights = pd.read_excel('data/united/united-flights-2018-2019.xlsx')

flights.columns = flights.columns.str.replace(' ', '')
flights = flights[cols]

print(flights)

flights.to_csv('data/united/united-flights.csv')
