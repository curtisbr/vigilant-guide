import pandas as pd

stations = pd.read_csv('data/united/station-list-t.csv', header=None, index_col=False, dtype={0:'str', 1:'float'})

stations[stations.columns[1]] = stations[stations.columns[1]].astype(int)

stations = stations.sort_values(stations.columns[0])


#stations = stations.drop(stations.columns[[0, 1, 2, 3, 4, 5, 6, 7]], axis=1)

print(stations.head())
stations.to_csv('data/united/station-list.csv', index=False, header=None)



