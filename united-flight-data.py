# tools
import pandas as pd

cols = ['FLIGHTDATE',
        'DEST',
        'DESTOBSERVATIONTIME']

united_flights = pd.read_excel('data/united/united-flights-2018-2019.xlsx')

united_flights.columns = united_flights.columns.str.replace(' ', '')
united_flights = united_flights[cols]

print(united_flights)

united_flights.to_csv('data/united/united-flights-matching.csv')
