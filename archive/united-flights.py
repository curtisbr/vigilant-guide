# tools
import pandas as pd

cols = ['FLIGHTDATE',
        'FLIGHTNO',
        'ORIGIN',
        'DEST',
        'DEPARTUREDATE_ZULU', # SCH DEPARTURE TIME
        'ARRIVALDATE_ZULU', # SCH ARRIVAL TIME
        'ORIGINOBSERVATIONTIME', # UA WX ORIGIN OBSERVED TIME
        'DESTOBSERVATIONTIME', # UA WX DEST OBSERVED TIME
        'OUT_ZULU', # ACTUAL DEPARTURE TIME
        'IN_ZULU'] # ACTUAL ARRIVAL TIME

flights = pd.read_excel('data/united/united-flights-2018-2019.xlsx')

flights.columns = flights.columns.str.replace(' ', '')
flights = flights[cols]

print(flights)

flights.to_csv('data/united/united-flights.csv')
