def directions_to_timesSq():
  print("Walk 4 mins to 34th St Herald Square train station.")
  print("Take the Northbound N, Q, R, or W train 1 stop.")
  print("Get off the Times Square 42nd Street stop.")
  print("Take lots of pictures!")

directions_to_timesSq()

#budget exercise 

def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time):
  
  car_rental_total = car_rental_rate * trip_time
  
  hotel_total = hotel_rate * trip_time - 10
  
  trip_total = car_rental_total + hotel_total + plane_ticket_price

  return trip_total

print(calculate_expenses(200, 100, 100, 5))
