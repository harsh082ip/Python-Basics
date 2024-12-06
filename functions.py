# functions

def sayHello(name="demo_name"):
    print(f"Hello {name}")
    
sayHello("Harsh")

# return  values
def getSum(num1, num2):
    total = num1 + num2
    return total

sum = getSum(3, 4)
print(sum)

# lambda functions - anonymous functions - 
# take any num of arguments but can only have one expression

getSub = lambda num1, num2 : num1 - num2
print(getSub(12, 3))  