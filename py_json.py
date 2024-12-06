import json

# sample json

userJson = '{"name": "Harsh Vardhan", "email": "harsh@example.com", "age": 18}'

# parse to dict
user = json.loads(userJson)
print(user, type(user))

# extract info
print(user['name'])

# dict to json
car = {"make": "Ford", "model": "Mustang", "year": 1970}
print(car, type(car))

carJson = json.dumps(car)
print(carJson, type(carJson))