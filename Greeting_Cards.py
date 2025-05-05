# Checkpoint 1a -  import the contextlib modules @contextmanager decorator
from contextlib import contextmanager
# Checkpoint 1b - create a decorated function named generic that takes in card type, sender’s name, and recipient arguments.
@contextmanager
def generic(card_type, sender, receiver):
# Checkpoint 2a - create a variable to store a call of the open() built-in function that opens up a generic card type based on the card type parameter in read mode.
  card_file = open(card_type, 'r')
# Checkpoint 2b - create a variable to store a call of the open() built-in function that creates (and opens) a new card named with the following pattern: < sender_name >_generic.txt.
# Use the sender name parameter from the function definition. Open the file in write mode since we will need to write a new card to the file.
  order = open(f"{sender}_generic.txt","w")
# Checkpoint 3 - Inside the generic() context manager use the try/finally clause to yield a file so that it creates the following template custom card:
# Dear < receiver >
# < text from the generic template card > 
# Sincerely, < sender >
# Make sure to use '\n' to create line breaks!

  try:
    order.write(f"Dear {receiver}, \n")
    order.write(card_file.read())
    order.write(f"\nSincerely, {sender} \n")
    yield order
# Checkpoint 4 - Finally, make sure to close both files after usage!
  finally:
    card_file.close()
    order.close()

# Checkpoint 5 - Use a with statement to generate this order. Have the with statement confirm the card is created by printing 'Card Generated!'
with generic("thankyou_card.txt", "Mwenda", "Amanda") as order1:
  print('Card Generated!')

# Checkpoint 6 - Use a with statement to open and read the file you just created in the last step.
with open("Mwenda_generic.txt", "r") as first_order:
  print(first_order.read())

# Checkpoint 7 -  create a class called personalized
class personalized:
# Checkpoint 8a - write a __init__ method that takes the sender’s and receiver’s names and saves them as attributes.
  def __init__(self, sender, receiver):
    self.sender_name = sender
    self.receiver_name = receiver
# Checkpoint 8b - Add one more attribute that stores a newly opened (or created) file in write mode with the format < sender_name >_personalized.txt.
    self.file = open(f"{sender}_personalized.txt", "w")
# Checkpoint 9 - Make an __enter__ method that writes the receiver’s name to the opened file and returns that file. The format we write to the file should look like this: Dear < receiver>.
def __enter__(self):
    self.file.write(f"Dear {self.receiver}, \n \n")
    return self.file
# Checkpoint 10 - Create an __exit__ method that writes "Sincerely" followed by the sender’s name on the open file and then closes the file!
def __exit__(self, exc_type, exc_value, traceback):
    self.file.write(f"\n \n Sincerely, \n {self.sender}")
    self.file.close()

# Checkpoint 11 - Use the context manager with a with statement to generate an order for a customer 'John' who requested an order for a personalized card for his close friend 'Michael'.
with personalized("John", "Michael") as order2:
  order2.write("I am so proud of you! Being your friend for all these years has been nothing but a blessing. I don’t say it often but I just wanted to let you know that you inspire me and I love you! All the best. Always.")

# Checkpoint 12 - Create a nested with statement that generates Josiah's generic birthday card order for his colleague 'Remy' and personalized card order for his sister 'Ester' in one call.
with generic("thankyou_card.txt", "Josiah", "Remy") as order3, personalized("Josiah", "Ester") as order4:
  order4.write("Happy Birthday!! I love you to the moon and back. Even though you’re a pain sometimes, you’re a pain I can't live without. I am incredibly proud of you and grateful to have you as a sister. Cheers to 25!! You’re getting old!")
