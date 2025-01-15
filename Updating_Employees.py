# Exercise 1
# Define a class called Employee
class Employee():
# Define a class variable new_id and set it equal to 1
  new_id = 1
# Each Employee instance will need its own unique ID.
# Inside the Employee class Define an __init__() method
  def __init__(self):
# Inside __init__(), define self.id and set it equal to the class variable new_id
    self.id = Employee.new_id
# Lastly, increment new_id by 1
    Employee.new_id += 1

# Now create a function to output the instance id.
# Inside the Employee Class, define a say_id() mehtod
  def say_id(self):
#Inside say_id(), output the string "My id is " and then the instance id.
    print("My id is {}.".format(self.id))

# Lastly, create 2 employees and have them give their ids.
# Outside of the Employee class:
# Define the variable e1 and set it to an instance of Employee
e1 = Employee()
# Define the variable e2 and set it to an instance of Employee
e2 = Employee()
# Have both e1 and e2 output their ids
e1.say_id()
e2.say_id()


# Exercise 2 - Intro to Inheritance
class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

# Create an Admin class that inherits from the Employee class
class Admin(Employee):
# Inside the body of the class insert the pass statement
  pass

e1 = Employee()
e2 = Employee()
e3 = Admin()
e3.say_id()


# Exercise 3 - Override Methods
class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

class Admin(Employee):
# Define a method say_id()
  def say_id(self):
# Inside the method, output "I am an Admin"
    print("I am an Admin")

e1 = Employee()
e2 = Employee()
e3 = Admin()
# Now when you call .say_id() with e3 you should see the .say_id() method output from Admin
e3.say_id()


# Exercise 4 - using super ()
class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

class Admin(Employee):
  def say_id(self):
# new code
# inside the Admin class Add a line that also calls the Employee class .say_id() method
    def __init__(self):
      super.__init__(Admin.say_id)
    print("I am an admin.")

e1 = Employee()
e2 = Employee()
e3 = Admin()
e3.say_id()


# Exercise 5 - Inheritance Part 1
class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

class Admin(Employee):
  def say_id(self):
    super().say_id()
    print("I am an admin.")

# Define a Manager class and have it inherit from the Admin class
class Manager(Admin):
# Inside the Manager class, define a method say_id() that outputs that they are in charge.
  def say_id(self):
    print("I am in charge!")
# Inside the .say_id() method of Manager:
# Call the Admin class .say_id() method
    super().say_id()

e1 = Employee()
e2 = Employee()
e3 = Admin()
# Define a variable e4 and set it to an instance of the Manager class
e4 = Manager()
# Call the .say_id() method of the instance in e4
e4.say_id()


# Exercise 6 - Inheritance Part 2
class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

class User:
  def __init__(self, username, role="Customer"):
    self.username = username
    self.role = role

  def say_user_info(self):
    print("My username is {}".format(self.username))
    print("My role is {}".format(self.role))

# Have the Admin class inherit from the User class alongside the Employee class. Be sure to have the Employee class listed first in the Admin class definition.
class Admin(Employee, User):
  def __init__(self):
#Inside the .__init__() method of the Admin class:
# Call the .__init__() method of the User class
# Pass the Admin class instance, id and the string "Admin" as arguments to the .__init__() method call    
    super().__init__()
    User.__init__(self, self.id, "Admin")

  def say_id(self):
    super().say_id()
    print("I am an admin.")

e1 = Employee()
e2 = Employee()
e3 = Admin()
# Call the .say_user_info() method using the Admin instance in e3
e3.say_user_info()


# Exercise 7 - Utilizing Polymorphism
class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

class Admin(Employee):
  def say_id(self):
    super().say_id()
    print("I am an admin.")

class Manager(Admin):
  def say_id(self):
    super().say_id()
    print("I am in charge!")

# Define a variable meeting and set it equal to a list that contains an instance of each class, Employee(), Admin() and Manager()
# Using a for loop iterate through the list meeting
# Using your defined loop variable, call the .say_id() method on each instance in the list
meeting = [Employee(), Admin(), Manager()]
for m in meeting:
  m.say_id()


# Exercise 8 Dunder Methods
class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

class Meeting:
  def __init__(self):
    self.attendees = []
  
  def __add__(self, employee):
    print("ID {} added.".format(employee.id))
    self.attendees.append(employee)

# Inside the Meeting class, overload the len() operation by defining a __len__() dunder method
  def __len__(self): 
# Inside the __len__() definition, return the lenght ofthe attribute attendees 
    return len(self.attendees)
  
# Now add three employees to a meeting:   

e1 = Employee()
e2 = Employee()
e3 = Employee()
m1 = Meeting()
# Using the Meeting instance m1, add each of the employee instances e1, e2, and e3. Use one line for each employee instance.
m1 + e1
m1 + e2
m1 + e3
# Output the length of meeting instance m1
print(len(m1))


# Exercise 9 - Abstraction
# The abstract class AbstractEmployee is defined. It has all the logic that has previously existed in the Employee class, except that the .say_id() method is not implemented and has the @abstractmethod decorator.
from abc import ABC, abstractmethod

class AbstractEmployee(ABC):
  new_id = 1
  def __init__(self):
    self.id = AbstractEmployee.new_id
    AbstractEmployee.new_id += 1

  @abstractmethod
  def say_id(self):
    pass

# Make the Employee class inherit from the AbstractEmployee class
class Employee(AbstractEmployee):
# Define a say_id() method that outputs a message with self.id
  def say_id(self):
    print("The variable is {}".format(self.id))

e1 = Employee()
e1.say_id()


# Exercise 10 - Encapsulation
# The Employee class contains one attribute id
class Employee():
    def __init__(self):
        self.id = None
# Define the single underscore variable_id and set it equal to whatever you want
        self._id = None
# Define the double underscore variable __id and set it equal to whatever you want
        self.__id = None
        
# An instance variable e is defined and then passed to the function dir() which is output to the console.
e = Employee()
# dir() is a built-in Python function that returns a list of all class members, including dunder methods.
print(dir(e))


# Exercise 12 - Getters, Setters, and Deleters
# Using a getter, setter, and the single underscore naming convention, the employees of the company will now be able to use their names. 
class Employee():
  new_id = 1
  def __init__(self, name=None):
    self.id = Employee.new_id
    Employee.new_id += 1
# The single underscore attribute _name has been added to the Employee class. Names default to None unless a string argument is passed during instantiation.
    self._name = name

# Inside the employee class define a getter method called get_name() that returns the class attribute _name.
  def get_name(self):
    return self._name
# Define a setter method set_name that has an additional parameter for the name string and sets the class attribute _name.
def set_name(self, new_name):
    self._name = new_name
# Define a deleter method del_name that deletes the attribute.
def del_name(self):
    del self._name

#testing code below
e1 = Employee("Maisy")
e2 = Employee()
print(e1.get_name())

e2.set_name("Fluffy")
print(e2.get_name())

e2.del_name()
print(e2.get_name())
