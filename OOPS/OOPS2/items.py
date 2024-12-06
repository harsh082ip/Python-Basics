## Items class separated
import csv

class Item:
    # class attributes - can be accessed from instances
    pay_rate = 0.8  # pay rate after 20% discount
    all = []  # to append all self objects when creating

    # Instance attributes
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations
        assert price >= 0, f"Price {price} is not greater than 0"  # add custom error msg
        assert quantity >= 0, f"Quantity {quantity} is not greater than 0"

        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)  # append

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
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            # print("reader", reader, type(reader))
            # for r in reader:
            #     print("row", r, type(r))
            items = list(reader)
            # print("list", items, type(items))   -- optional for debugging purposes

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
