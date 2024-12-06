# class


class User:
    # constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
    
    def greeting(self):
        return f"My name is {self.name} and I'm {self.age} years old"
    
    def hasBirthday(self):
        self.age += 1
    

# Inheritance - extends parent class
class Costumer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.bal = 0
    
    def setBal(self, bal):
        self.bal = bal
    
    def greeting(self):
        return f"My name is {self.name} and my balance is {self.bal}"

# init user object
obj = User("Harsh", "test@gmail.com", 18)

harsh = Costumer("Harsh", "test@gmail.com", 18)
harsh.setBal(80000000)

# call parent func from base
print(harsh.greeting())

print(obj.name)

obj.hasBirthday()
print(obj.greeting())
print(harsh.greeting())