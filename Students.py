
def prize_generator():
  student_info = {
    "Joan Stark": 355,
    "Billy Mars": 45,
    "Tori Rivers": 18,
    "Kyle Newman": 25
  }

  for student in student_info:
    name = student
    id = student_info[name]
    if id % 3 == 0 and id % 5 == 0:
      yield student + " gets prize C"
    elif id % 3 == 0:
      yield student + " gets prize A"
    elif id % 5 == 0:
      yield student + " gets prize B"

prizes = prize_generator()
print(next(prizes))
print(next(prizes))
print(next(prizes))
print(next(prizes))

# Checkpoint 1 -We want to create a generator that will generate values of class standings: 'Freshman', 'Sophomore', 'Junior', and 'Senior'. The generator function should be named class_standing_generator.
def class_standing_generator():
  yield 'Freshman'
  yield 'Sophomore'
  yield 'Junior'
  yield 'Senior'

  # Checkpoint 2 - Initialize an iterator object called class_standings from calling class_standing_generator()
class_standings = class_standing_generator()

# Checkpoint 3 - Use a for loop to iterate through the class_standings iterator to print out each class standing value.
for standings in class_standings:
  print(standings)

def student_standing_generator():
  student_standings = ['Freshman','Senior', 'Junior', 'Freshman']



def student_standing_generator():
  student_standings = ['Freshman','Senior', 'Junior', 'Freshman']
# Checkpoint 1 - add a for loop that traverses through the student_standings list and yields 500 for each 'Freshman' value.
  for standing in student_standings:
    if standing == 'Freshman':
      yield 500
# Checkpoint 3 - Outside the function, retrieve the iterator object by calling student_standing_generator() and set it to a variable called standing_values.
standing_values = student_standing_generator()

# Checkpoint 3 - Print out the values within the returned standing_values generator using the Python built-in function next().
print(next(standing_values))
print(next(standing_values))

def cs_generator():
  for i in range(1,5):
    yield "Computer Science " + str(i)

# Checkpoint 1 Define a generator function called cs_generator(), retrieve a generator object by calling cs_generator() and set it to a variable called cs_courses. Print out the values within the iterator using a for loop.
cs_courses = cs_generator()
for courses in cs_courses:
  print(courses)

# Checkpoint 2 - After the for loop, create an iterator using a generator expression and put it in a variable called cs_generator_exp. The iterator should produce the same output as cs_generator(). Use range(1,5) within the generator expression to generate the course number.
cs_generator_exp = ("Computer Science {}".format(i) for i in range(1,5))

# Checkpooint 3 - Print out the values of the cs_generator_exp iterator object using a for loop.
for exp in cs_generator_exp:
  print(exp)

def student_counter():
  for i in range(1,5001):
    yield i

student_generator = student_counter()
for student_id in student_generator:
  if student_id ==101:
# Use the throw() method to throw a ValueError of “Invalid student ID” if the iterated student ID goes over 100
    student_generator.throw(ValueError, "Invalid student ID")
  print(student_id)

def student_counter():
  for i in range(1,5001):
    yield i

student_generator = student_counter()
for student_id in student_generator:
  print(student_id)
# Use the close() method to terminate the generator after 100 students.
  if student_id == 101:
    student_generator.close()

def science_students(x):
  for i in range(1,x+1):
    yield i

def non_science_students(x,y):
  for i in range(x,y+1):
    yield i

""" We want to retrieve student ids in the following order:
Science students with IDs 1-5
Non-science students with IDs 10-15
Non-science students with IDs 25-30
Use a connected generator function called combined_students that uses yield from statements to achieve this."""

def combined_students():
  yield from science_students(5)
  yield from non_science_students(10,15)
  yield from non_science_students(25,30)

# Call the combined_students() combined generator function and set it to a variable named student_generator. 
student_generator = combined_students()
for students in student_generator:
  print(students)

# First, complete the generator function called course_generator that can yield tuples of (Course name, Number students) for the above courses and the corresponding number of students. 
def course_generator():
    yield ("Computer Science", 5)
    yield ("Art", 10)
    yield ("Business", 15)

# Create a generator function called add_five_students that takes in an input variable called courses.
def add_five_students(courses):

# The add_five_students generator function should loop through the courses input object.
 for course, num_students in courses:

# On each iteration, it should yield a tuple containing the course name and number of students plus 5.
    yield (course, num_students + 5)

# use a nested generator to get the resulting generator that has the 5 added students to each course. Set it to a variable called increased_courses. Print out each course tuple in the resulting increased_courses generator using a for loop.
increased_courses = add_five_students(course_generator())
for course in increased_courses:
    print(course)


def summa():
    yield 'Summa Cum Laude'

def magna():
    yield 'Magna Cum Laude' 

def cum_laude():
    yield 'Cum Laude'

# Given a list of input GPAs, create a generator function called honors_generator that takes in 1 input argument named gpas that represents the list of GPAs from the variable gpas. The function should use yield from on each input GPA to determine the honors assignment.
def honors_generator(gpas):
  for gpa in gpas:
    if gpa > 3.9:
      yield from summa()
    elif gpa > 3.7:
      yield from magna()
    elif gpa > 3.5:
      yield from cum_laude()

# Create a generator function called graduation_countdown() that will countdown the number of days left before student graduation. It should take in as input days and yield one less day on each next() call, so the last value yielded is 0. Use a while loop for yielding and decrementing the day.
def graduation_countdown(days):
  while days >= 0:
    days_left = yield days
    if days_left != None:
      days = days_left
    else:
      days -= 1

# Create an equivalent generator expression called countdown_generator for the graduation_countdown generator function. It should generate the days in a descending order starting from the provided days value. Place the code after the days = 25 line.
days = 25
countdown_generator = (day for day in range(days, -1,-1))
# Call the graduation_countdown() function and set it to a variable called grad_days.
grad_days = graduation_countdown(days)
# Modify the graduation_countdown() generator function to accept values sent using send(). Use a local variable called days_left to store sent values. Use an if/else statement to check for sent values.
# On the 15th day of the graduation countdown, the school president announces that graduation will be moved up 5 days. Send a value of 10 to the grad_days generator when the 15th day in the countdown is reached.
for day in grad_days:
  if day == 15:
    grad_days.send(10)
  elif day == 3:
    grad_days.close()
# Iterate through grad_days generator to print the number of days left with a string of “Days Left: x” where x represents the countdown value.
  print("Days Left: " + str(day))

days = 25
gpas = [3.2, 4.0, 3.6, 2.9]
# Call the connected generator function honors_generator with the gpas list and set it to a variable called honors. 
honors = honors_generator(gpas)
# Loop through the honors generator and print out each honor_label value to see which honors labels will be generated given the gpas list.
for honor_label in honors:
  print(honor_label)
