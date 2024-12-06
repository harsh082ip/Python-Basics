#

fruits = ("apple", "oranges", "kiwi")

# using constructor
fruits2 = tuple(("apple", "oranges", "kiwi"))

print(fruits, fruits2, type(fruits2), type(fruits))

# for single assignment, needs a comma in the last
test = ("harsh",)
print(test, type(test))

# cannot chnage
# fruits[0] = "test"


# sets - unordered, unindexed, no-duplicates

# Create set
fruits_set = {"apple", "oranges", "mangos"}
print(fruits_set, type(fruits_set))

# check for an element by val
print("apple" in fruits_set)

# add
fruits_set.add("bananas")
print(fruits_set)

# remove
fruits_set.remove("bananas")
print(fruits_set)

# duplicating will not give any error, it just not add it twice
fruits_set.add("apple")
print(fruits_set)


# clear
fruits_set.clear()
print(fruits_set)



# del
del fruits_set
# print(fruits_set)