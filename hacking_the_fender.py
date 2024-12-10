# reading in the passwords
import csv
# create a list of users
compromised_users = []
# Pass the password_file object holder to our CSV reader for parsing
with open('passwords.csv') as password_file:
  password_csv = csv.DictReader(password_file)
#  iterate through each of the lines in the CSV.
  for password_row in password_csv:
  # print statement includes the usernames of those whose passwords were compromised
  #  print(password_row['Username'])
    compromised_users.append(password_row["Username"])
# iterate through compromised_users and write comprmised_user in new variable compromised_user_file
with open('compromised_users.txt', 'w') as compromised_user_file:
  for compromised_user in compromised_users:
    compromised_user_file.write(compromised_user + '\n')

# Create a JSON file with a message for the boss
import json
with open('boss_message.json', 'w') as boss_message:
  boss_message_dict = {"recipient": "The Boss", "message": "Mission Success"} 
  json.dump(boss_message_dict, boss_message)

with open("new_passwords.csv", 'w') as new_passwords_obj:
  slash_null_sig = '''
  _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
'''            
  new_passwords_obj.write(slash_null_sig)
