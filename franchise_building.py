# Part One - Making the Menus

# task 1 - create Menu class
class Menu:
 
# Task 2 - Give Menu a constructor with the five parameters self, name, items, start_time, and end_time.
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time 

# Task 7 - Give our Menu class a string representation method that will tell you the name of the menu. Also, indicate in this representation when the menu is available.
  def __repr__(self): # string representation
    return self.name + " menu available from " + str(self.start_time) + "hr to " + str(self.end_time) + "hr."
# Task 8 Try out our string representation. If you call print(brunch)
    brunch = Menu("brunch", items, 11, 16) # creates the brunch variable
    print(brunch)

# Task 9  Give Menu a method .calculate_bill() that has two parameters: self, and purchased_items. 
  def calculate_bill(self, purchased_items):
    # Task 9 part 2 - Have calculate_bill return the total price of a purchase consisiting of all the items in purchased_items:
    total = 0 # so each item purchased can be added to the calculated bill
    for i in purchased_items: #iterating through list gives us the full availability of the list
      total += self.items.get(i, 0) # updates the total price and allows us to select which key value pairs needed for the calculated_bill
    return total #returns calculated_bill's total

# Task 3 Let’s create our first menu: brunch. Brunch is served from 11am to 4pm.
items = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}
brunch = Menu("brunch", items, 11, 16)
print(brunch)

# Task 4 - Let’s create our second menu item early_bird. Early-bird Dinners are served from 3pm to 6pm.
items2 = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}
early_bird = Menu("early-bird", items2, 15, 18)

# Task 5 - Let’s create our third menu, dinner. Dinner is served from 5pm to 11pm. 
items3 = {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}
dinner = Menu("dinner", items3, 17, 23)

# Task 6 - And let’s create our last menu, kids. The kids menu is available from 11am until 9pm. 
items4 = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}
kids = Menu("kids", items4, 11, 21)

# Task 10 - Test out Menu.calculate_bill(). We have a breakfast order for one order of pancakes, one order of home fries, and one coffee. Pass that into brunch.calculate_bill() and print out the price.
print("The price of a breakfast order for one order of pancakes, one order of home fries, and one coffee is: " + str(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))) # adds the values together because of the +

# Task 11 - What about an early-bird purchase? Our last guests ordered the salumeria plate and the vegan mushroom ravioli. Calculate the bill with .calculate_bill().
print("The price of a salumeria plate and the vegan mushroom ravioli is: " + str( early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']) ))

# Part Two - Creating the Franchises

# Task 12 - Create a franchise class
class Franchise:

# Task 13 - Give the Franchise class a constructor. Take in an address, and assign it to self.address. Also take in a list of menus and assign it to self.menus.
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

# Task 15 - Give our Franchises a string representation so that we’ll be able to tell them apart. If we print out a Franchise it should tell us the address of the restaurant.
  def __repr__(self):
    return "the address of the restaurant is: " + self.address

# Task 16 - Give Franchise an .available_menus() method that takes in a time parameter and returns a list of the Menu objects that are available at that time.    
  def available_menus(self, time):
    menu_list = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        menu_list.append(menu)
    return menu_list
    
# Task 14 - create the franchise variables and pass in all four menus along with these addresses to define flagship_store and new_installment.
flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])
print(flagship_store)
new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])
print(new_installment)

# Task 17 - Let’s test out our .available_menus() method! Call it with 12 noon as an argument and print out the results.
print(flagship_store.available_menus(12))

# Task 18 - See what is printed if we call .available_menus() with 5pm as an argument and print out the results. Remember use military time
print(new_installment.available_menus(17))

# Part Three - Creating Businesses!

# Task 19 - Creating a restaurant that sells arepas! First let’s define a Business class. 
class Business:

# Task 20 - Give Business a constructor. A Business needs a name and a list of franchises.
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

# Task 21 - Let’s create our first Business. The name is "Basta Fazoolin' with my Heart" and the two franchises are flagship_store and new_installment. 
first_business = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

# Task 22 - we’ll need a menu. The items for our Take a’ Arepa available from 10am until 8pm and save this to a variable called arepas_menu
arepas_menu = Menu("arepa",{'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}, 10, 20)

# Task 23 - Our new restaurant is located at "189 Fitzgerald Avenue". Save the Franchise object to a variable called arepas_place.
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

# Task 24 - Now let’s make our new Business! The business is called "Take a' Arepa"!
new_business = Business("Take a' Arepa!", [arepas_place])

print(new_business.name)
print(new_business.franchises[0])
