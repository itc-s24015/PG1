
prefectures = ['hokkaido', 'hokkaido', 'tokyo', 'kanagawa']
cities = ['sapporo', 'hakodate', 'minato', 'yokohama']

populations = [100, 200, 300, 400]
population_dict = {(state,city): population for state, city, population in zip(prefectures, cities, populations)}
print(population_dict)
