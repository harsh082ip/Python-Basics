name = "18"
age = 18

print("Hello! My name is " + name + " and I'm " + str(age) + " years old")


# arguements by position
print("Hello! My name is {name} and I'm {age} years old".format(name=name, age=age))

# F-strings
print(f"Hello! My name is {name} and I'm {age} years old")

# capitalize
print(name.capitalize())

# all uppercase
print(name.upper())

# all lower
print(name.lower())

# len 
print(len(name))

# replace
test = "hello world"
print(test.replace("world", "everyone"))


# count
sub = "h"
print(name.count(sub))

#split
arr = test.split()
print(arr , type(arr), len(arr))

# is_numeric
print(name.isnumeric())