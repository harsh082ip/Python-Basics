# unorered, changeable, indexed, no duplicates


# Create dict
person = {
    'first_name': 'Harsh Vardhan',
    'last_name': 'Singh',
    'age': 30
}

# Use constructor
# person2 = dict(first_name='Sara', last_name='Williams')

# Get value
print(person['first_name'])
print(person.get('last_name'))

# Add key/value
person['phone'] = '+91 9555489012'

# Get dict keys
print(person.keys())

# Get dict items
print(person.items())


'''
SOME NOTES ON COPY

    person.copy() is a shallow copy, meaning it only creates a 
    new copy of the dictionary itself. If the dictionary contains 
    nested objects (like lists or other dictionaries), those nested 
    objects are shared between the original and the copy. To make 
    a completely independent copy (deep copy), you can use the copy module:

'''

print("----copy----")
# Copy dict
person2 = person.copy()
print(person2)
person2['city'] = 'Boston'
print(person2)

# remove item
del(person['age'])
person.pop('phone')
print(person)


# Clear
person.clear()

# Get length
print(len(person2))

# List of dict
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 25}
]

print(people[1]['name'])
print(people)
print(type(people[0]))

# but this is a list only
print(type(people))

# get specific
print(people[1]['name'], type(people[1]["name"]))