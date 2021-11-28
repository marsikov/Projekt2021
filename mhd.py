import pandas
mhd = pandas.read_csv('Public_transport_stops.csv', encoding='utf-8')
mhd1 = mhd[mhd['zone_id'] == 100]
mhd2 = mhd[mhd['zone_id'] == 101]
mhd3 = pandas.concat([mhd1, mhd2], ignore_index=True)
mhd4 = mhd3[['ObjectId', 'stop_name', 'latitude', 'longitude']]
mhd4 = mhd4.rename(columns={'ObjectId' : 'id'})
mhd4.to_csv('mhd.csv', index=False)
