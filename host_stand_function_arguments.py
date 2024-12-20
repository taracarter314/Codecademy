



# table numbers are changed from lists to dictionaries and adding more items to table 1
# table changed again to include a tuple in the table dictionary to diferentiate customer vs order
tables = {
  1: {
    'name': 'Jiho',
    'vip_status': False,
    'order': {
      'drinks': 'Orange Juice, Apple Juice',
      'food_items': 'Pancakes',
      'total': [534.50, 20.0, 5]
    }
  },
  2: {},
  3: {},
  4: {},
  5: {},
  6: {},
  7: {},
}

# Write your code below: 
def assign_table(table_number, name, vip_status=False): # adding False here sets a default of False for vip_status so we don't have to add this parameter unless the guest is a vip_tatus needs to be True

# assigning customers to their table_name, name, and vip_status
  # tables[table_number] = [name, vip_status]

# adjustments made now that each table is a dictionary
  tables[table_number]['name'] = name
  tables[table_number]['vip_status'] = vip_status
  tables[table_number]['order'] = {}

#use of positional argument
assign_table(6, 'Yoni', False )
#print(tables)

#use of keyword argument
assign_table(table_number=3, name='Martha', vip_status=True)
#print(tables)

#see comment at def assign_tables coupled with default value practice below
assign_table(4, 'Karla')
#print(tables)

#new information at table 6 gets replaced
assign_table(6, 'Tara', True)
#print(tables)

#move Yoni to table 7
assign_table(7, 'Yoni')
print(tables)

#new info to table 2
assign_table(2, 'Douglas', True)
print('--- tables with Douglas --- \n', tables)

# take orders function and using variable number of arguments using *
def print_order(*order_items):
  print(order_items)
print_order('Orange Juice', 'Apple Juice', 'Scrambled Eggs', 'Pancakes') #this is the output

# Inside of our function, access the nested order key for the specific table (using the 
# table_number argument) from tables and set it to the order_items parameter.
def assign_and_print_order(table_number, *order_items):
  tables[table_number]['order'] = order_items
  # use a for loop to print every ordered item so the kitchen knows what to make
  for item in order_items:
    print(item)

# add a new guest
assign_table(2, 'Arwa', True)
# Arwa wants to order
assign_and_print_order(2, 'Steak', 'Seabass', 'Wine Bottle')
print(tables) 

# seperate food orders from drink orders
def assign_food_items(table_number, **order_items):
  print(order_items)
  food = order_items.get('food')
  drinks = order_items.get('drinks')
  tables[table_number]['order']['food_items'] = food
  tables[table_number]['order']['drinks'] = drinks

print(food)
print(drinks)

# Example Call
assign_food_items(food='Pancakes, Poached Egg', drinks='Water')

print('\n --- tables after update --- \n')

assign_food_items(2, food='Seabass, Gnocchi, Pizza', drinks='Margarita, Water')
print(tables)

#use an unpacking variable or *arg
def calculate_price_per_person(total, tip, split):
  total_tip = total * (tip/100)
  split_price = (total + total_tip) / split
  print(split_price)

table_7_total = [534.50, 20.0, 5]

calculate_price_per_person(*table_7_total)
