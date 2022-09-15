# import
import pandas as pd

df = pd.read_csv('data/united/united-merge.csv', encoding_errors='ignore', index_col=None, header=0)

stations = pd.Series(df.DEST.unique())

unique = stations.merge(df, how='left')

# Single DF is saved to the path in CSV format, without index column
# data.to_csv('data/united/united-stations-testing.csv', index=False)

