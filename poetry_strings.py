poem_title = "spring storm"
poem_title_fixed = poem_title.title()
print(poem_title)
print(poem_title_fixed)  #gives title proper upper cases

poem_author = "William Carlos Williams"
poem_author_fixed = poem_author.upper()
print(poem_author)
print(poem_author_fixed) #all caps author's name



line_one = "The sky has given over"
line_one_words = line_one.split()
print(line_one_words) #prints each word as it's own list



authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(',') # creates a list with a space between each name

print(author_names)

author_last_names = [] # looking at the index of the list

for name in author_names: #to iterate through all the names in the .split() string
  author_last_names.append(name.split()[-1]) #edit the new variable to add each last name from the prior split list to the new variable
"""steps
#call the new list name - author_last_names
#add .append() to author_last_names to add author_names to author_last_names
#in (add temp variable from the loop)
#(add .split() to split up the names from author_names string)
#index outside the function of split but in append function to only get the last names
""" 

print(author_last_names)


#ie using escape squences

# when there is anything outside of quotes and there 
# is a \ it means continue on to the long string below
spring_storm_text = \
"""The sky has given over 
its bitterness. 
Out of the dark change 
all day long 
rain falls and falls 
as if it would never end. 
Still the snow keeps 
its hold on the ground. 
But water, water 
from a thousand runnels! 
It collects swiftly, 
dappled with black 
cuts a way for itself 
through green ice in the gutters. 
Drop after drop it falls 
from the withered grass-stems 
of the overhanging embankment."""

spring_storm_lines = spring_storm_text.split('\n')
print(spring_storm_lines)

spring_storm_line = spring_storm_text.split('\t')
print(spring_storm_line)

#joining strings
reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]
reapers_line_one = ' '.join(reapers_line_one_words) #the ' ' puts spaces between the words otherwise it is all one word
print(reapers_line_one)

#you can use any string as the delimiter. '\n', '\t', ' ', ','
winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']

winter_trees_full = '\n'.join(winter_trees_lines)

print(winter_trees_full)


#replace
toomer_bio = \
"""
Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his 
literary career, was born in Washington, D.C. in 1894. Jean is the son 
of Nathan Tomer was a mixed-race freedman, born into slavery in 1839 
in Chatham County, North Carolina. Jean Tomer is most well known for his 
first book Cane, which vividly portrays the life of African-Americans 
in southern farmlands.
"""
toomer_bio_fixed = toomer_bio.replace('Tomer', 'Toomer')
print(toomer_bio_fixed)

#find
god_wills_it_line_one = "The very earth will disown you"
disown_placement = god_wills_it_line_one.find("disown")

print(disown_placement)


#FORMAT

def poem_title_card(title, poet):
  # \"{}\" means to include this set of quotation marks when the title is printed
  poem = "The poem \"{}\" is written by {}.".format(title, poet)
  return poem

print(poem_title_card("I Hear America Singing","Walt Whitman"))

def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date = publishing_date, author = author, title = title, original_work = original_work)
  return poem_desc

author = "Shel Silverstein"
title = "My Beard"
original_work = "Where the Sidewalk Ends"
publishing_date = "1974"

my_beard_description = poem_description(publishing_date, author, title, original_work)

print(my_beard_description)


#REVIEW
highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

# print(highlighted_poems)

highlighted_poems_list = highlighted_poems.split(',')

# print(highlighted_poems_list)

highlighted_poems_stripped = []

for poem in highlighted_poems_list:
  highlighted_poems_stripped.append(poem.strip())
  
# print(highlighted_poems_stripped)

highlighted_poems_details = []

for poem in highlighted_poems_stripped:
  highlighted_poems_details.append(poem.split(':'))
  
titles = []
poets = []
dates = []

for poem in highlighted_poems_details:
  titles.append(poem[0])
  poets.append(poem[1])
  dates.append(poem[2])
  

#Finally, write a for loop that uses .format() to print out the following string for each poem:
# Hint
# To print out the desired statement for each poem, you’ll need to use a for loop to iterate 
# over the length of any of the lists (since they all have the same length). Inside the loop, 
# use the .format() method to replace TITLE, POET, and DATE with the corresponding elements 
# from the titles, poets, and dates lists at the current index. 
for i in range(0,len(highlighted_poems_details)):
    print('The poem {} was published by {} in {}'.format(titles[i], poets[i], dates[i]))

    
