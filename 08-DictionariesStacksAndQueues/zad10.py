import json

with open("data.json", 'r') as file:
    data = json.load(file)
    i = 0
    while i < len(data):
        print(data[i])
        i += 1
