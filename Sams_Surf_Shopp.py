# Write your code below:
import surfshop
import unittest
import datetime

class TestSurfShop(unittest.TestCase):
  # In your class, create a setup fixture that runs before every test. It should instantiate a new ShoppingCart object and assign it to an instance variable called self.cart. Your tests can then use self.cart to reference your instance of the ShoppingCart class.
  def setUp(self):
    self.cart = surfshop.ShoppingCart()

# commented out because of the for loop
  '''def test_add_surfboards_1(self):
    message = self.cart.add_surfboards(quantity=1)
    self.assertEqual(message, 'Successfully added 1 surfboard to cart!')

  def test_add_surfboards_2(self):
    message = self.cart.add_surfboards(quantity=2)
    self.assertEqual(message, 'Successfully added 2 surfboards to cart!')'''
# Parameterize the test you wrote in task 4 so that it runs 3 times, passing 2, 3, and 4 as the arguments to surfshop.add_surfboards(). This allows us to easily test a single function with a variety of inputs. Remember to modify the expected return value with the correct number of surfboards.
  def test_add_surfboards(self):
    for num in range(2, 5):
      with self.subTest(num=num):
        message = self.cart.add_surfboards(num)
        self.assertEqual(message, f'Successfully added {num} surfboards to cart!')
        self.cart = surfshop.ShoppingCart()

  @unittest.skip # used for offseason
  def test_too_many_boards(self):
    self.assertRaises(surfshop.TooManyBoardsError, self.cart.add_surfboards, 5)
    def ___str__(self):
      return 'Cart cannot have more than 4 surfboards in it!' 

  # error fixed at end of project instructions
  @unittest.expectedFailure
  def test_apply_local_discount(self):
    self.cart.apply_locals_discount()
    self.assertTrue(self.cart.locals_discount)
  
  def test_set_checkout_date(self):
    date = datetime.datetime.now()
    self.assertRaises(surfshop.CheckoutDateError, self.cart.set_checkout_date, date)

unittest.main()
