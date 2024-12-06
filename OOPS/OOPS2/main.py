## import Items and Phone
from items import Item
from phone import Phone

Item.instantiate_from_csv()
print(Item.all)