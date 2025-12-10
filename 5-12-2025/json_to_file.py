import json

with open(r'cars.json', 'r') as file:
    data = json.load(file)
print(data)