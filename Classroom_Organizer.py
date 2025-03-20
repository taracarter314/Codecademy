# checkpoint 1 - Navigate to script.py and import the student_roster list from roster.py AND Create an iterator for the student_roster list and print out each student’s information using next().
from roster import student_roster
# Checkpoint 2
import itertools
import classroom_organizer
student_roster_iterator = iter(student_roster)

# Checkpoint 2 - First, we should create a custom class that will allow us to manage our classroom and students.You’ve been provided a file called classroom_organizer.py. Start defining out your custom ClassroomOrganizer class.
class ClassroomOrganizer:
  index = 0
  # Checkpoint 3 - Next, we want to create a simple way to run through morning roll call, by ordering all students by first name alphabetically. When you iterate on your ClassroomOrganizer object, it should return each student’s name one at a time on each next() call or for loop iteration. 
  # Define the iterator protocol for our ClassroomOrganizer class that can achieve this. Once defined, use either next() calls or a for loop on the ClassroomOrganizer object to print out the next student on the roll call.
  def __init__(self, stored_names):
    self.stored_names = self.sort_alphabetically(student_roster)
    
  def __next__(self):
    if self.index < len(self.sorted_names):
      message = "{}".format(self.sorted_names[self.index])
      self.index += 1
      return message
    else:
      raise StopIteration

# Checkpoint 4 - Using the itertools module, define a method within ClassroomOrganizer that will retrieve a final list of all tuple combinations of 2 students that can be seated at each table.
  def sort_alphabetically(self,students):
    names = []
    for student_info in students:
      name = student_info['name']
      names.append(name)
    return sorted(names)

# Checkpoint 5 - You are offering an afterschool program for those students whose favorite subjects are Math and Science.
# Your tables can fit 4 students at them. Retrieve a list of all 4 combinations of students whose favorite subjects are Math and Science.
# The get_students_with_subject() method can be used to retrieve iterables for each of the subjects.
def get_students_with_subject(self, subject):
    selected_students = []
    for student in student_roster:
      if student['favorite_subject'] == subject:
        selected_students.append((student['name'], subject))
    return selected_students

c = ClassroomOrganizer(stored_names=student_roster)

print(next(c))
    
