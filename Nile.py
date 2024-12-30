from nile import get_distance, format_price, SHIPPING_PRICES  
from test import test_function  
  
def calculate_shipping_cost(from_coords, to_coords, shipping_type='Overnight'):  
   """  
   Calculate the shipping cost based on the distance and shipping type.  
  
   Args:  
      from_coords (tuple): The coordinates of the starting point.  
      to_coords (tuple): The coordinates of the destination.  
      shipping_type (str, optional): The type of shipping. Defaults to 'Overnight'.  
  
   Returns:  
      float: The formatted shipping cost.  
   """  
   distance = get_distance(*from_coords, *to_coords)  
   shipping_rate = SHIPPING_PRICES[shipping_type]  
   price = distance * shipping_rate  
   return format_price(price)  
  
test_function(calculate_shipping_cost)

class Driver:  
   def __init__(self, salary, speed):  
      self.salary = salary  
      self.speed = speed  
  
def calculate_driver_cost(distance, *drivers):  
   """  
   Calculate the cost of hiring a driver based on the distance and driver's speed.  
  
   Args:  
      distance (float): The distance to be traveled.  
      *drivers (Driver): Variable number of Driver objects.  
  
   Returns:  
      tuple: The cheapest driver and their cost.  
   """  
   cheapest_driver = None  
   cheapest_driver_price = float('inf')  
  
   for driver in drivers:  
      driver_time = distance / driver.speed  
      driver_price = driver.salary * driver_time  
  
      if driver_price < cheapest_driver_price:  
        cheapest_driver = driver  
        cheapest_driver_price = driver_price  
  
   return cheapest_driver, cheapest_driver_price  
  
# Test the function by calling  
# test_function(calculate_driver_cost)

class Trip:  
   def __init__(self, cost, driver):  
      self.cost = cost  
      self.driver = driver  
  
def calculate_money_made(**trips):  
   """  
   Calculate the total money made from a series of trips.  
  
   Args:  
      **trips (Trip): Variable number of Trip objects.  
  
   Returns:  
      float: The total money made.  
   """  
   total_money_made = 0  
  
   for trip_id, trip in trips.items():  
      trip_revenue = trip.cost - trip.driver.cost  
      total_money_made += trip_revenue  
  
   return total_money_made  
  
# Test the function by calling  
# test_function(calculate_money_made)

# Create drivers  
driver1 = Driver(10, 50)  
driver2 = Driver(15, 60)  
  
# Calculate driver cost  
cheapest_driver, cheapest_driver_price = calculate_driver_cost(100, driver1, driver2)  
print(f"Cheapest driver: {cheapest_driver.salary}, Cost: {cheapest_driver_price}")  
  
# Create trips  
trip1 = Trip(100, driver1)  
trip2 = Trip(150, driver2)  
  
# Calculate money made  
total_money_made = calculate_money_made(trip1=trip1, trip2=trip2)  
print(f"Total money made: {total_money_made}")

