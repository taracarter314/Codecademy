letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

zipped_lists = zip(letters, points)
# use .upper and .lower to include both upper and lower case letters
letters_to_points = {key.upper(): value for key, value in zipped_lists}
letters_to_points.update({key.lower(): value for key, value in zipped_lists})
letters_to_points[" "] = 0

## Function to calculate the score of a word
# by summing the points of its letters

def score_word (word):
  point_total = 0
  for letter in word:
    point_total += letters_to_points[letter]
  return point_total

brownie_points = score_word("BROWNIE")
print(brownie_points)

player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

player_to_points ={}

for player, words in player_to_words.items():
  player_points = 0
  for word in words:
     player_to_points[player] = player_to_points.get(player, 0) + score_word(word.replace(',', '').replace(' ', ''))
print(player_to_points)

# check if the player exists in player_to_words before appending a word to avoid errors

def play_word(player, word):
  if player in player_to_words:
    player_to_words[player].append(word)
  else:
    player_to_words[player] = [word]

