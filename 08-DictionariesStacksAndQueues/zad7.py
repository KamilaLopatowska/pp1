person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"}
   }

print(person)
print(person['name'])
print(person["hobby"])
person["surname"] = 'Nowak'
person["married"] = not person['married']
person['gender'] = 'male'
person["hobby"].append('bicycle') #person['hobby'] += ['bicycle']
print(person)
person['phone']['work phone'] = '313131444'
print(person)