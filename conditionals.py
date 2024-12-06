# if / else

x = 10 
y = 5

if x > y:
    print(x, "x is greater")
else:
    print(y, "y is greater")
    
    
# elif 
if x > y:
    print(x, "x is greater")
elif x == y:
    print("x is equal to y")
else:
    print(y, "y is greater")
    
# nested if 
if x > 2:
    if x <= 10:
        print("x is greater than 2 but less than 10")

# use 'and' instead
if x > 2 and x <= 10:
    print("x is greater than 2 but less than 10")

# or - only one cond should be true
if x > 2 or x <= 10:
    print("x is greater than 2 but less than 10")

# not 
if not(x == y):
    print("x is not equal to y")

# membership operators 

nums = [1, 2, 3, 4, 5]
# in
if x in nums:
    print("x is in nums")
else:
    print("x is not in nums")
    
# not in
if x not in nums:
    print("x is not in nums")
else:
    print("x is in nums")
    
    
# is 
if x is y:
    print("x is y")
else:
    print("x is not y")