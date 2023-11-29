import json
movie = {
    "title":"Girl, interrupted",
    "year": 1999,
    "actor":{"leading":"Winona Ryder","supporting":"Angelina Jolie"},
    "oscar":True,
    "genre": "psychological thriller"
}

with open('favourite.json', 'w', encoding = 'utf-8') as file:
    json.dump(movie, file, indent = 4)