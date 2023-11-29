countries = [
    {"name":"Poland", "population":38000000},
    {'name': 'Australia', 'population' : 25000000},
    {'name': 'Germany', 'population' : 40000000},
    {'name': 'Iceland', 'population' : 3},
    {'name': 'France', 'population' : '0 humans'}
]
i = 0
print(f'{"COUNTRY":10}{"POPULATION":5}')
while i < len(countries):
    print(f'{countries[i]["name"]:10} {countries[i]["population"]:<10}')
    i += 1