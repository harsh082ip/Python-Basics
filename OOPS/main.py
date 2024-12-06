# class

'''
class Item:
    def calc_total_price(self):
        return self.price * self.quantity

item1 = Item()

item1.name = "Phone"
item1.price = 100
item1.quantity = 5
print(item1.calc_total_price())
'''
# class Item:
#     def calc_total_price(self, x, y):
#         return x * y

# item1 = Item()

# item1.name = "Phone"
# item1.price = 100
# item1.quantity = 5
# print(item1.calc_total_price(item1.price, item1.quantity))
import csv

class Item:
    # class attributes - can be accessed from instances
    pay_rate = 0.8 # pay rate after 20% discount
    all = [] # to append all self objects when creating
    # Instance attributes
    def __init__(self, name: str, price: float, quantity=0):  
        # Run validations
        assert price >= 0, f"Price {price} is not greater than 0"  # add custom error msg
        assert quantity >= 0, f"Quantity {quantity} is not greater than 0"
        
        self.name = name
        self.price = price
        self.quantity = quantity
         
        Item.all.append(self) # append

    def calc_total_price(self):
        print("I'm here")
        return self.price * self.quantity
    
    def apply_discount(self):
        # self.price = self.price * Item.pay_rate  # cannot access directly - not good for flexibility
        self.price = self.price * self.pay_rate
        # print("item.rate", Item.pay_rate)
        # return self.price
        
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r')  as f:
           
            reader = csv.DictReader(f)
            # print("reader", reader, type(reader))
            # for r in reader:
            #     print("row", r, type(r))
            items = list(reader)
            print("list", items, type(items))
        
        for item in items:
            Item(
                name=item.get("name"),
                price=float(item.get("price")),
                quantity=int(item.get("quantity"))
            )

    @staticmethod
    def is_integer(num):
        # count out floats with .0
        if isinstance(num, float):
            # print("here")
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):  # official string representation of an object
        # return f"Item('{self.name}, {self.price}, {self.quantity}')"
        return f"{self.__class__.__name__}('{self.name}, {self.price}, {self.quantity}')"

class Phone(Item):
    # copying the parent constructor - bad approach
    all = []
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        super().__init__(name, price, quantity)
        # Run validations
        assert price >= 0, f"Price {price} is not greater than 0"  # add custom error msg
        assert quantity >= 0, f"Quantity {quantity} is not greater than 0"
        assert quantity >= 0, f"brokenphones {broken_phones} is not greater than 0"

        ## NOT GOOD TO ASSIGN LIKE THIS - USE SUPER() TO ASSIGN ITEM attributes TO ITEM and
        ## PHONE attributes to PHONE
        # self.name = name
        # self.price = price
        # self.quantity = quantity

        # self assign to phone
        self.broken_phones = broken_phones

        Phone.all.append(self)  # append -- we can remove this to get a complete picture of all instances



item1 = Item(name="Phone", price=100, quantity=5)  # Proper data types
# print(item1.calc_total_price())

item2 = Item("Laptop", 1000, 3)
# we can still add objects to this instace
item2.hasNumKeys = False

# print(item1.calc_total_price())
# print(item2.calc_total_price())
print(item2.hasNumKeys)

### access pay_rate
# print(Item.pay_rate)
# print(item1.pay_rate)
# print(item2.pay_rate)

print(Item.__dict__) # All attributes for class level
print(item1.__dict__) # All atrrbutes for instace level

# apply discount
item1.apply_discount()
print("discount", item1.price)

# we can also change pay_rate for instance level
item2.pay_rate = 0.7
item2.apply_discount()
print("New discount", item2.price)

item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all)
# print(Item.all.__repr__) # display objects 
# print only name
for instance in Item.all:
    print(instance.name)
    
print(item1)

Item.instantiate_from_csv()
print(Item.all)
# print("-----with----")
# with open("items.csv", "r") as f:
#     read = f.readline()

# calling static method
print(Item.is_integer(10.0))
# can also call static method from instance level
print(item4.is_integer(232))

# calling phone constructor
phone1 = Phone("myphone", 500, 5, 1)
print("phone1 broken phones", phone1.broken_phones)
print("phone1 all",phone1.all)
print("phone1 repr", phone1.__repr__())
print("phone1 calculate price",phone1.calc_total_price())

# print all
print("Items all", Item.all)
print("Phone all", Phone.all)