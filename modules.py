# default modukes
import datetime
# import sub module
from datetime import date
import time

from camelcase import CamelCase

today = date.today()
print(today)

timestamp = time.time()
print(timestamp)

from time import time
print(time())

c = CamelCase()
print(c.hump("harsh vardhan"))


# custom import
import validator
from validator import validate_email

email = "test@gmail.com"
res = validator.validate_email(email)

if res:
    print("Email is good")
else:
    print("Email is bad")