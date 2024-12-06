rom datetime import datetime as dt
from decimal import Decimal
from random import choice
from random import randint
import custom_module
# prints the current date and time
print(dt.today().date())
print(dt.today().time())
#use base_cost in your calculation with Decimal
base_cost = Decimal('1000.00')
print(abs(-5))
# these next examples are the use of moodules and not functions like we learned before.
year = randint(100, 2023)

destinations = choice(['Athens', 'Rome', 'London', 'Egypt'])

message = custom_module.generate_time_travel_message

print(message) 
