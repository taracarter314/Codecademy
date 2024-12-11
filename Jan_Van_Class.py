class Grade:
  minimum_passing = 65
  
  def __init__(self, score):
    self.score = score

# Define a class named Student
class Student:
  # Add a constructor for Student. Have the constructor take in two parameters: a name and a year.
  def __init__(self, name, year):
    # Save those two as attributes .name and .year.
    self.name = name
    self.year = year
  # In the body of the constructor for Student, declare self.grades as an empty list.
    self.grades = []
  
  # Add an .add_grade() method to Student that takes a parameter, grade.
  def add_grade(self, grade):
    # .add_grade() should verify that grade is of type Grade
    if type(grade) is Grade:
      # if so, add it to the Student‘s .grades.
      self.grades.append(grade) 


  # Create three instances of the Student class below and take outside the constructor
roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

# Create a Grade class, with .minimum_passing as an attribute set to 65.
class Grade:
 minimum_passing = 65 #like a variable specific to the class?
 def __init__(self, score):
  self.score = score
# Create a new Grade with a score of 100 and add it to pieter‘s .grades attribute using .add_grade().
pieter.add_grade(Grade(100))
