import pandas
byty = pandas.read_csv('in/tables/data-items.csv', encoding='utf-8')

byty = byty[['data_localUniqueId', 'data_offerType', 'data_type', 'data_livingArea', 'data_price', 'data_gpsCoord_lat', 'data_gpsCoord_lon', 'data_title', 'data_address', 'data_url']]
byty = pandas.concat([byty[byty['data_type'] == 'house'], byty[byty['data_type'] == 'apartment']], ignore_index=True)

byty = byty[byty['data_gpsCoord_lat'].between(49.1181261, 49.2926669, inclusive='both')]
byty = byty[byty['data_gpsCoord_lon'].between(16.4350306, 16.7197311, inclusive='both')]

byty = byty.rename(columns={'data_localUniqueId' : 'id', 'data_gpsCoord_lat' : 'lat', 'data_gpsCoord_lon' : 'lon', 'data_offerType' : 'offer_type', 'data_livingArea' : 'living_area', 'data_type' : 'type', 'data_price' : 'price', 'data_title' : 'title', 'data_address' : 'address', 'data_url' : 'url'})
byty = byty.dropna(subset = ['price'])

byty.to_csv('out/tables/byty.csv', index=False)
