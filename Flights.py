#this file imports from entertainment.py / alerts.py / kiosk.py


flight_statuses = {
  903: 'Departed',
  834: 'Boarding',
  359: 'Delayed',
  128: 'On time',
  385: 'On time',
}

print('***Small World Air Flight Information***')
for flight, status in flight_statuses.items():
  print('Flight ' + ' status: ' + status)


#Checkin Kiosk
destinations = {
  'BUD': 'Budapest',
  'CMN': 'Casablanca',
  'IST': 'Istanbul'
}
print('Welcome to Small World Airlines!')
print('What is the airport code of your travel destination?')
destination = 'HND'

assert destination in destinations, 'Sorry, Small World currently does not fly to this destination!'

city_name = destinations[destination]
print('Great! Retrieving information for your flight to ...' + city_name)


# Find the exit
def get_nearest_exit(row_number):
  if row_number < 15:
    location = 'front'
  elif row_number < 30:
    location = 'middle'
  else:
    # Checkpoint 5
    location = 'back'
  return location

# Checkpoint 1
def test_row_1():
  assert get_nearest_exit(1) == 'front', 'The nearest exit to row 1 is in the front!'

# Checkpoint 2 
def test_row_20():
  assert get_nearest_exit(20) == 'middle', 'The nearest exit to row 20 is in the middle!'

#Checkpoint 3
def test_row_40():
  assert get_nearest_exit(40) == 'back', 'The nearest exit to row 40 is in the back!'

# Checkpoint 4
test_row_1()
test_row_20()
test_row_40()

# practiing unittesting
# Checkpoint 1
import unittest

def get_nearest_exit(row_number):
  if row_number < 15:
    location = 'front'
  elif row_number < 30:
    location = 'middle'
  else:
    # Checkpoint 6
    location = 'back'
  return location

# Checkpoint 2
class NearestExitTests(unittest.TestCase):
  # Checkpoint 3
  def test_row_1(self):
    self.assertEqual(get_nearest_exit(1), 'front', 'The nearest exit to row 1 is in the front!')
    
  # Checkpoint 3
  def test_row_20(self):
    self.assertEqual(get_nearest_exit(20), 'middle', 'The nearest exit to row 20 is in the middle!')
    
  # Checkpoint 3
  def test_row_40(self):
    self.assertEqual(get_nearest_exit(40), 'back', 'The nearest exit to row 40 is in the back!')

# Checkpoint 4
unittest.main()

#unittesting movies and wifi
import unittest
import entertainment

# Write your code below: 
class EntertainmentSystemTests(unittest.TestCase):

  def test_movie_license(self):
    daily_movie = entertainment.get_daily_movie()
    licensed_movies = entertainment.get_licensed_movies()
    self.assertIn(daily_movie, licensed_movies)

  def test_wifi_status(self):
    wifi_enabled = entertainment.get_wifi_status()
    self.assertTrue(wifi_enabled)

unittest.main()

# practicing quantatative testing
import unittest
import entertainment

class EntertainmentSystemTests(unittest.TestCase):

  def test_movie_license(self):
    daily_movie = entertainment.get_daily_movie()
    licensed_movies = entertainment.get_licensed_movies()
    self.assertIn(daily_movie, licensed_movies)

  def test_wifi_status(self):
    wifi_enabled = entertainment.get_wifi_status()
    self.assertTrue(wifi_enabled)

  # Checkpoint 1
  def test_maximum_display_brightness(self):
    brightness = entertainment.get_maximum_display_brightness()
    self.assertAlmostEqual(brightness, 400)

  # Checkpoint 2
  def test_device_temperature(self):
    device_temp = entertainment.get_device_temp()
    self.assertLess(device_temp, 35)
    
unittest.main()

# alerts testing

import unittest
import Alerts

# Checkpoint 1
class SystemAlertTests(unittest.TestCase):
    
  # Checkpoint 2
  def test_power_outage_alert(self):
    self.assertRaises(Alerts.PowerError, Alerts.power_outage_detected, True)
    
  # Checkpoint 3
  def test_water_levels_warning(self):
    self.assertWarns(Alerts.WaterLevelWarning, Alerts.water_levels_check, 150)

unittest.main()

#parameterizing tests
import unittest
import entertainment

class EntertainmentSystemTests(unittest.TestCase):

  def test_movie_license(self):
    # Checkpoint 1
    daily_movies = entertainment.get_daily_movies()
    licensed_movies = entertainment.get_licensed_movies()

    # Checkpoint 2
    for movie in daily_movies:
      print(movie)
      # Checkpoint 3 & 4
      with self.subTest(movie):
        self.assertIn(movie, licensed_movies)

unittest.main()


#tests for passenger check-in
import unittest
import Kiosk

class CheckInKioskTests(unittest.TestCase):

  def test_check_in_with_flight_number(self):
    print('Testing the check-in process based on flight number')

  def test_check_in_with_passport(self):
    print('Testing the check-in process based on passport')

  # Write your code below:
  @classmethod
  def setUpClass(cls):
    Kiosk.power_on_kiosk()

  @classmethod
  def tearDownClass(cls):
    Kiosk.power_off_kiosk()
  
  def setUp(self):
    Kiosk.return_to_welcome_page()
    

unittest.main()


# test skipping for regional planes that don't have entertainment systems
import unittest
import entertainment

class entertainmentSystemTests(unittest.TestCase):
  # Checkpoint 1
  @unittest.skipIf(entertainment.regional_jet(), 'Not available on regional jets')
  def test_movie_license(self):
    daily_movie = entertainment.get_daily_movie()
    licensed_movies = entertainment.get_licensed_movies()
    self.assertIn(daily_movie, licensed_movies)

  # Checkpoint 2
  @unittest.skipUnless(entertainment.regional_jet() is False, 'Not available on regional jets')
  def test_wifi_status(self):
    wifi_enabled = entertainment.get_wifi_status()
    self.assertTrue(wifi_enabled)

  # Checkpoint 3
  def test_device_temperature(self):
    if entertainment.regional_jet():
      self.skipTest('Not available on regional jets')
    device_temp = entertainment.get_device_temp()
    self.assertLess(device_temp, 35)

  # Checkpoint 3
  def test_maximum_display_brightness(self):
    if entertainment.regional_jet():
      self.skipTest('Not available on regional jets')
    brightness = entertainment.get_maximum_display_brightness()
    self.assertAlmostEqual(brightness, 400)


unittest.main()


#Use the expectedFailure decorator to mark this test as an expected failure!
import unittest
import feedback

class CustomerFeedbackTests(unittest.TestCase):

  # Write your code below:
  @unittest.expectedFailure

  def test_survey_form(self):
    self.assertEqual(feedback.issue_survey(), 'Success')

  def test_complaint_form(self):
    self.assertEqual(feedback.log_customer_complaint(), 'Success')

unittest.main()

