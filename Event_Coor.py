guests = {}
def read_guestlist(file_name):
  text_file = open(file_name, 'r')
  while True:
    line_data = text_file.readline().strip().split(",")
    if len(line_data) < 2:
    # If no more lines, close file
      text_file.close()
      break
    name = line_data[0]
    age = int(line_data[1])
    g = yield name, age
    if g is not None:
      name = g[0]
      age = g[1]
      yield name,age
    guests[name] = age
  
names = read_guestlist('guest_list.txt')

#prints the names from 1 to 10 using next()
for i in range(10):
  print(next(names))

#iterates through the first 10 guests
print(names.send(['Jane', 35]))

#prints the rest of the names
for n in names:
  print(n)

age_21 = (guest for guest in guests if guests[guest] >= 21)

#prints the names with age >= 21
for name in age_21:
  print(name)

#create 3 tables with 5 seats at each
def table_1():
  for i in range(1, 6):
    yield ("Chicken", "Table 1", "{}".format(i))

def table_2():
 for i in range(1, 6):
   yield ("Beef", "Table 2", "{}".format(i))

def table_3():
  for i in range(1, 6):
    yield ("Fish", "Table 3", "{}".format(i))

#combine the list of tables
def tables():
  yield from table_1()
  yield from table_2()
  yield from table_3()

#create a function which yields a table 
def assign_table(t):
  for table in t:
    yield table

#connected generator which assigns a table from each fn()
guest_table = assign_table(tables())

#yield the name along with a table for each guest
def assign_guest(guests, guest_table):
  for guest in guests:
    yield guest, next(guest_table)

#print the final results
for a in assign_guest(guests, guest_table):
  print(a)
