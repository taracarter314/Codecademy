# create a class that will represent an employee of a company.
# Define a class called Employee
class Employee():
#Define a class variable new_id and set it equal to 1
  new_id = 1
# Each Employee instance will need its own unique ID. 
# Inside the Employee class:
# Define an __init__() method  
  def __init__(self):
# Inside __init__(), define self.id and set it equal to the 
# class variable new_id
    self.id = Employee.new_id
# Lastly, increment new_id by 1
    Employee.new_id += 1


# Now create a function to output the instance id.
# Inside the Employee class:
# Define a say_id() method
  def say_id(self):
# Inside say_id(), output the string "My id is " and then the instance id.
    print("My id is {}.".format(self.id))

# Practicing Inheritance
# Create an Admin class that inherits from the Employee class
class Admin(Employee):
# #Override Practice
# Inside the Admin class:
# Define a method say_id()
  def say_id(self):
# Inside the Admin class:
# Add a line that also calls the Employee class .say_id() method
    super().say_id()
    print("I am an Admin")
# Define a Manager class and have it inherit from the Admin class
class Manager(Admin):
# Inside the Manager class, define a method say_id() that outputs that they are in charge.
  def say_id(self):
    print("I'm in charge")
    super().say_id()
#output 
# I am in charge!
# My id is 4.
# I am an admin.



# Lastly, create 2 employees and have them give their ids.
# Outside of the Employee class:
# Define the variable e1 and set it to an instance of Employee
e1 = Employee()
# Define the variable e2 and set it to an instance of Employee
e2 = Employee
# test out your inheritance implementation.
# Define a variable e3 and set it to an instance of the Admin class
e3 = Admin()
## Define a variable e4 and set it to an instance of the Manager class
e4 = Manager()

# Have both e1 and e2 output their ids
e1.say_id()
e2.say_id()
# Now if you call the .say_id() method of the Admin instance in e3, you will 
# get output with the instance’s id.
e3.say_id()
# Call the .say_id() method of the instance in e4
e4.say_id()

