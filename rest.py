import pandas
rest = pandas.read_csv('in/tables/dataset_items.csv', encoding='utf-8')
rest = rest[['id', 'name', 'latitude', 'longitude', 'rating']]
rest = rest.dropna(subset=['latitude', 'longitude', 'rating'])
rest=rest[rest['rating'] >= 4]
rest=rest[rest['latitude'].between(49.1181261, 49.2926669, inclusive='both')]
restaurace=rest[rest['longitude'].between(16.4350306, 16.7197311, inclusive='both')]
restaurace.to_csv('out/tables/rest.csv', index=False)
