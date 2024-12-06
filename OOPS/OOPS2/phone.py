## phone class seperated
# import items class to use
from items import Item

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
