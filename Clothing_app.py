company_name = "Threads"
company_location = (-96.107239, 33.139080)
company_products = ['jean pants', 'cargo pants', 'athletic shorts', 'jean shorts', 'leggings', 'tshirts', 'tanks', 'blouses', 'dresses', 'accessories']
company_data = {'name': company_name, 'location': company_location, 'products': company_products}

from helper_functions import process_csv_supplies
from collections import *

# The first row is skipped since it only contains labels
csv_data = process_csv_supplies()[1:]

# create an empty deque called supplies_deque to separate the data into important and non-important items 
supplies_deque = deque()

# Using a for loop, read each item from csv_data. On each iteration, if the item is marked as important, append it to the front of supplies_deque, otherwise append it to the end.
for row in csv_data:
  if row[2] == 'important':
      supplies_deque.appendleft(tuple(row))
else:
  supplies_deque.append(tuple(row))

# create a new deque called ordered_important_supplies, Remove the first 25 important items from your supplies_deque, and append them to ordered_important_supplies 
ordered_important_supplies = deque()
for _ in range(25):
    ordered_important_supplies.append(supplies_deque.popleft())

# Repeat the same process for 10 unimportant items, create a new deque called ordered_unimportant_supplies, remove 10 low important items from your supplies_deque, and append them to ordered_unimportant_supplies.
ordered_unimportant_supplies = deque()
for _ in range(10):
    ordered_unimportant_supplies.append(supplies_deque.pop())

clothes = [('t-shirt', 'green', 'large', 9.99),
           ('jeans', 'blue', 'medium', 14.99),
           ('jacket', 'black', 'x-large', 19.99),
           ('t-shirt', 'grey', 'small', 8.99),
           ('shoes', 'white', '12', 24.99),
           ('t-shirt', 'grey', 'small', 8.99)]

# create a namedtuple subclass called ClothingItem with a typename of 'ClothingItem' and the field_name consisting of: 'type', 'color', 'size', and 'price' in that specific order.
# type of 'coat', a color of 'black', a size of 'small', and a price of 14.99.

ClothingItem = namedtuple('ClothingItem', ['type', 'color', 'size', 'price'])

# create a new object from the subclass ClothingItem called new_coat.
new_coat = ClothingItem('coat', 'black', 'small', 14.99)

# type of 'coat', a color of 'black', a size of 'small', and a price of 14.99.
coat_cost = new_coat.price

# create a new empty list called updated_clothes_data
updated_clothes_data = []

# for every piece of clothes data in the list of tuples, append a new ClothingItem object to updated_clothes_data while passing the data from the tuple into the new ClothingItem object.
for item in clothes:
  updated_clothes_data.append(ClothingItem(item[0], item[1], item[2], item[3]))

# print out updated_clothes_data to see the result!
print(updated_clothes_data)

order_data = [['Order: 1', 'purchased'],
              ['Order: 2', 'purchased'],
              ['Order: 3', 'purchased'],
              ['Order: 4', 'returned'],
              ['Order: 5', 'purchased'],
              ['Order: 6', 'canceled'],
              ['Order: 7', 'returned'],
              ['Order: 8', 'purchased'],
              ['Order: 9', 'returned'],
              ['Order: 10', 'canceled'],
              ['Order: 11', 'purchased'],
              ['Order: 12', 'returned'],
              ['Order: 13', 'purchased'],
              ['Order: 14', 'canceled'],
              ['Order: 15', 'purchased']]

# create a new object from that class called orders. Use the constructor to automatically convert the order_data into an OrderedDict
orders = OrderedDict(order_data) 

#  create two new lists called to_move and to_remove
to_move = []
to_remove = []

# Iterate through each item in orders and check what the status is.
for key, val in orders.items():
# If the status is 'returned' then add the key (order number string) to the to_move list. Otherwise, if the status is 'canceled' then add it to the to_remove list.
   if val == 'returned':
    to_move.append(key)
   elif val == 'canceled':
    to_remove.append(key)

# remove from orders, for every item in the to_remove list, .pop() the element from orders.
for item in to_remove:
  orders.pop(item)

# use the .move_to_end() method to push back any of the 'returned' orders from to_move to the end of orders.
for item in to_move:
  orders.move_to_end(item)

# print to output the orders to the console!
print(orders)

year_profit_data = [
    {'jan_profit': 15492.30, 'jan_holiday_profit': 2589.12},
    {'feb_profit': 17018.05, 'feb_holiday_profit': 3701.88},
    {'mar_profit': 11849.13},
    {'apr_profit': 9870.68},
    {'may_profit': 13662.34},
    {'jun_profit': 12903.54},
    {'jul_profit': 16965.08, 'jul_holiday_profit': 4360.21},
    {'aug_profit': 17685.69},
    {'sep_profit': 9815.57},
    {'oct_profit': 10318.28},
    {'nov_profit': 23295.43, 'nov_holiday_profit': 9896.55},
    {'dec_profit': 21920.19, 'dec_holiday_profit': 8060.79}
]

new_months_data = [
    {'jan_profit': 13977.85, 'jan_holiday_profit': 2176.43},
    {'feb_profit': 16692.15, 'feb_holiday_profit': 3239.74},
    {'mar_profit': 17524.35, 'mar_holiday_profit': 4301.92}
]

# create a new ChainMap called profit_map using the year_profit_data list.
# Remember that a ChainMap accepts a variable number of arguments so we need to expand the list (*) so the constructor will read them as individual arguments instead of one single argument. 
profit_map = ChainMap(*year_profit_data)

# Create a function called get_profits
def get_profits(input_map):
# Make this function return the two variables: the standard profit first and the holiday profit second.
# calculate the sum of the standard profits (keys not containing 'holiday') and the holiday profits (keys containing 'holiday') in two different variables.
  total_standard_profit = 0.0
  total_holiday_profit = 0.0

  for key in input_map.keys():
    if 'holiday' in key:
      total_holiday_profit += input_map[key]
    else:
      total_standard_profit += input_map[key]

  return total_standard_profit, total_holiday_profit
# call the function using the profit_map and store the results in variables called last_year_standard_profit and last_year_holiday_profit.
last_year_standard_profit, last_year_holiday_profit = get_profits(profit_map)

# Add the new mappings to the profit_map so that the old January - March months are still in the ChainMap, but accessing those keys will return data for the most recent three months.
for item in new_months_data:
    profit_map = profit_map.new_child(item)
# Call the get_profits function on the profit_map again and store the results in current_year_standard_profit and current_year_holiday_profit to calculate the sum of the most recent 12 months of profit data.
current_year_standard_profit, current_year_holiday_profit = get_profits(profit_map)

# Calculate the difference for the standard and holiday profits and store them in variables called year_diff_standard_profit and year_diff_holiday_profit. Print your results.
year_diff_standard_profit = current_year_standard_profit - last_year_standard_profit
year_diff_holiday_profit = current_year_holiday_profit - last_year_holiday_profit 

print(year_diff_standard_profit)
print(year_diff_holiday_profit)

opening_inventory = ['shoes', 'shoes', 'skirt', 'jeans', 'blouse', 'shoes', 't-shirt', 'dress', 'jeans', 'blouse', 'skirt', 'skirt', 'shorts', 'jeans', 'dress', 't-shirt', 'dress', 'blouse', 't-shirt', 'dress', 'dress', 'dress', 'jeans', 'dress', 'blouse']

closing_inventory = ['shoes', 'skirt', 'jeans', 'blouse', 'dress', 'skirt', 'shorts', 'jeans', 'dress', 'dress', 'jeans', 'dress', 'blouse']

# define a function called find_amount_sold with three parameters: opening, closing, and item. Add the keyword return inside of the function. 
def find_amount_sold(opening, closing, item):
# Inside of our new function, and before it returns, create a variable called opening_count and store a Counter object passing in the opening parameter as the counter’s input.
  opening_count = Counter(opening)
# Then, create a variable called closing_count which stores a Counter object and passes in the closing parameter into the Counter.  
  closing_count = Counter(closing)
# use the .subtract() method to subtract the closing counted data from the opening counted data in order to get the amount sold for every item.
  opening_count.subtract(closing_count)
# - Using the parameter item, access the item’s inventory from the opening_count Counter object and return it.
  return opening_count[item]

# test the function by calling it with opening_inventory as the first argument, closing_inventory as the second argument, and t-shirt as the third argument, Store the result in a variable called tshirts_sold, print results
tshirts_sold = find_amount_sold(opening_inventory, closing_inventory, 't-shirt')
print(tshirts_sold)

data = {'order_4829': {'type': 't-shirt', 'size': 'large', 'price': 9.99, 'order_status': 'processing'},
        'order_6184': {'type': 'pants', 'size': 'medium', 'price': 14.99, 'order_status': 'complete'},
        'order_2905': {'type': 'shoes', 'size': 12, 'price': 22.50, 'order_status': 'complete'},
        'order_7378': {'type': 'jacket', 'size': 'large', 'price': 24.99, 'order_status': 'processing'}}

# create a new class which inherits from the UserDict class and name it OrderProcessingDict
class OrderProcessingDict(UserDict):
# The .clean_orders() method should search for any keys called ‘order_status’ and if value is equal to 'complete', remove the entire order from the dictionary.
   def clean_orders(self):
    to_del = []
    
    for key, val in self.data.items():
      if val['order_status'] == 'complete':
        to_del.append(key)

    for item in to_del:
      del self.data[item]

# try creating an instance of it called process_dict while passing data into the constructor.
process_dict = OrderProcessingDict(data)
# call the .clean_orders() method to automatically clean the orders inside.
process_dict.clean_orders()
# print your custom dictionary 
print(process_dict)

overstock_items = [['shirt_103985', 15.99],
                    ['pants_906841', 19.99],
                    ['pants_765321', 15.99],
                    ['shoes_948059', 29.99],
                    ['shoes_356864', 9.99],
                    ['shirt_865327', 10.99],
                    ['shorts_086853', 9.99],
                    ['pants_267953', 21.99],
                    ['dress_976264', 32.99],
                    ['shoes_135786', 17.99],
                    ['skirt_196543', 12.99],
                    ['jacket_976535', 26.99],
                    ['pants_086367', 30.99],
                    ['dress_357896', 29.99],
                    ['shoes_157895', 14.99]]
 
# create a new deque called split_prices.
split_prices = deque()

# use a for loop to iterate through every clothes item in the overstock_items list.
for item in overstock_items:
#  If the price is greater than 20 dollars, append the item to the front of split_prices, otherwise append it to the back of split_prices. Print to console.
  if item[1] > 20.0:
    split_prices.appendleft(item)
  else:
    split_prices.append(item)
  print(split_prices)

# create a namedtuple subclass called ClothesBundle. Set the typename to ClothesBundle and the field_names to bundle_items and bundle_price.
ClothesBundle = namedtuple('ClothesBundle', ['bundle_items', 'bundle_price'])

# create an empty list called bundles
bundles = []

# Use a loop to continue iterating as long as there are at least 5 elements left in split_prices.
while len(split_prices) >= 5:
# On each iteration, append a new ClothesBundle object to the bundles list. The ClothesBundle object will be created by making a bundle of three cheap items and two expensive items using the pop method.
# This can be accomplished using a new list by popping from the back of split_prices three times, and then popping from the front of split_prices twice. 
  bundle_list = [split_prices.pop(), split_prices.pop(), split_prices.pop(), split_prices.popleft(),split_prices.popleft()]
# Calculate the sum of the prices for the bundle and store that as the bundle_price in the ClothesBundle.
  calc_price = sum(b[1] for b in bundle_list)
  bundles.append(ClothesBundle(bundle_list, calc_price))

# Create a new list called promoted_bundles
promoted_bundles = []
# For every bundle in bundles which has a total value of over 100 dollars, add that bundle to promoted_bundles.
for bundle in bundles:
  if bundle.bundle_price > 100:
    promoted_bundles.append(bundle)

# print out the list of promoted_bundles to see the result!
print(promoted_bundles)







