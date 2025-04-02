genre_results = ['rap', 'classical', 'rock', 'rock', 'country', 'rap', 'rock', 'latin', 'country', 'k-pop', 'pop', 'rap', 'rock', 'k-pop',  'rap', 'k-pop', 'rock', 'rap', 'latin', 'pop', 'pop', 'classical', 'pop', 'country', 'rock', 'classical', 'country', 'pop', 'rap', 'latin']

# find all of the genres of music that the users submitted without duplicates by creating a set from genre_results with a variable named survey_genres.
survey_genres = set(genre_results)
print(survey_genres)

# create a new set called survey_abbreviated which stores the first three letters of each genre found in the survey results without duplication
survey_abbreviated = {'rap', 'cla', 'roc','k-p', 'lat', 'pop', 'cou'}
print(survey_abbreviated)


top_genres = ['rap', 'rock', 'pop']
# create a frozenset called frozen_top_genres from the top_genres data.
frozen_top_genres = frozenset(top_genres)
print(frozen_top_genres)

song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electric']}

user_tag_1 = 'warm'
user_tag_2 = 'exciting'
user_tag_3 = 'electric'

# create a new set called tag_set from the original song’s tags located in song_data.
tag_set = set(song_data['Retro Words'])

# Next, add the three user tag strings to tag_set.
tag_set.add(user_tag_1)
tag_set.add(user_tag_2)
tag_set.add(user_tag_3)

# or tag_set.update([user_tag_1, user_tag_2, user_tag_3])

# update song_data so that the value of the key, 'Retro Words' is equal to the updated tag set.
song_data = {'Retro Words': tag_set}
print(song_data)

song_data_users = {'Retro Words': ['pop', 'onion', 'warm', 'helloworld', 'happy', 'spam', 'electric']}

# Create a set called tag_set and store the tag data for 'Retro Words'.
tag_set = set(song_data_users['Retro Words'])

# remove tags unrelated to music
tag_set.remove('onion')
tag_set.remove('helloworld')
tag_set.remove('spam')

# replace the value of the key, 'Retro Words' inside of song_data_users so that it is equal to the updated tag set
song_data_users = {'Retro Words': tag_set}
print(song_data_users)

allowed_tags = ['pop', 'hip-hop', 'rap', 'dance', 'electronic', 'latin', 'indie', 'alternative rock', 'classical', 'k-pop', 'country', 'rock', 'metal', 'jazz', 'exciting', 'sad', 'happy', 'upbeat', 'party', 'synth', 'rhythmic', 'emotional', 'relationship', 'warm', 'guitar', 'fiddle', 'romance', 'chill', 'swing']

song_data_users = {'Retro Words': ['pop', 'explosion', 'hammer', 'bomb', 'warm', 'due', 'writer', 'happy', 'horrible', 'electric', 'mushroom', 'shed']}

# store the tag data from song_data_users into a set called tag_set.
tag_set = set(song_data_users['Retro Words'])

# Create a list called bad_tags. Then, iterate through each element of tag_set, adding tags to bad_tags that don’t belong.
bad_tags = []
for tag in tag_set:
    if tag not in allowed_tags:
        bad_tags.append(tag)

# Now, let’s remove all the incorrect tags from tag_set. Using the collected bad_tags, write another loop to iterate over each of the tags in bad_tags, and remove the elements from tag_set so we have only the allowed tags.
for tag in bad_tags:
    tag_set.remove(tag)
print(tag_set)

# Now, let’s remove all the incorrect tags from tag_set. Using the collected bad_tags, write another loop to iterate over each of the tags in bad_tags, and remove the elements from tag_set so we have only the allowed tags.
song_data_users['Retro Words'] = tag_set
print(song_data_users)

# SET UNION
song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electronic'],
             'Wait For Limit': ['rap', 'upbeat', 'romance'],
             'Stomping Cue': ['country', 'fiddle', 'party'],
             'Lowkey Space': ['electronic', 'dance', 'synth']}

user_tag_data = {'Lowkey Space': ['party', 'synth', 'fast', 'upbeat'],
                 'Retro Words': ['happy', 'electronic', 'fun', 'exciting'],
                 'Wait For Limit': ['romance', 'chill', 'rap', 'rhythmic'], 
                 'Stomping Cue': ['country', 'swing', 'party', 'instrumental']}

# create an empty dictionary called new_song_data which will hold the merged tag data.
new_song_data = {}

# Loop over song_data.items() (all the items in song_data)
for key, val in song_data.items():
# On each iteration of the loop, create a set for each category of tags. This will require creating two new sets, one for song_data and one for user_tag_data.
    song_tag_set = set(val)
    user_tag_set = set(user_tag_data[key])
# create a new key inside of new_song_data for each category and set the value to be a union of the two new sets.
    new_song_data[key] = song_tag_set | user_tag_set

print(new_song_data)

# SET INTERSECTION
song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
             'Wait For Limit': ['rap', 'upbeat', 'romance'],
             'Stomping Cue': ['country', 'fiddle', 'party'],
             'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat'],
             'Back To Art': ['pop', 'sad', 'emotional', 'relationship'],
             'Blinding Era': ['rap', 'intense', 'moving', 'fast'],
             'Down To Green Hills': ['country', 'relaxing', 'vocal', 'emotional'],
             'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

user_recent_songs = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
                     'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat']}

# create a variable called tags_int that stores the intersection between the tags for the user_recent_songs two recent songs 'Retro Words' and 'Lowkey Space'.
tags_int = set(user_recent_songs['Retro Words']) & set(user_recent_songs['Lowkey Space'])

# Find all other songs in song_data which have these tags. Store the songs which have any matching tags into a dictionary called recommended_songs. Make sure that you do not add any songs which the user has listened to recently!
recommended_songs = {}
for key, val in song_data.items():
    for tag in val:
        if tag in tags_int:
            if key not in user_recent_songs:
                recommended_songs[key] = val

print(recommended_songs)


song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
             'Wait For Limit': ['rap', 'upbeat', 'romance', 'relationship'],
             'Stomping Cue': ['country', 'fiddle', 'party'],
             'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat'],
             'Back To Art': ['pop', 'sad', 'emotional', 'relationship'],
             'Blinding Era': ['rap', 'intense', 'moving', 'fast'],
             'Down To Green Hills': ['country', 'relaxing', 'vocal', 'emotional'],
             'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

user_liked_song = {'Back To Art': ['pop', 'sad', 'emotional', 'relationship']}
user_disliked_song = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth']}

# Create a new variable called tag_diff that is the set difference between the tags inside of the one song of user_liked_song and the one song of user_disliked_song. Don’t forget to convert the list of tags into a set to perform this operation!
tag_diff = set(user_liked_song['Back To Art']) - set(user_disliked_song['Retro Words'])

# Now that you know the difference in tags between the liked song and disliked song, use those tags to find any songs from song_data which contain them.
# Make sure not to include the liked and disliked songs. Store the newly found songs into a dictionary called recommended_songs.
recommended_songs = {}
for key, val in song_data.items():
    for tag in val:
        if tag in tag_diff:
            if key not in user_liked_song and key not in user_disliked_song:
                recommended_songs[key] = val

print(recommended_songs)

user_song_history = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
                     'Stomping Cue': ['country', 'fiddle', 'party'],
                     'Back To Art': ['pop', 'sad', 'emotional', 'relationship'],
                     'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

friend_song_history = {'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat'],
                     'Blinding Era': ['rap', 'intense', 'moving', 'fast'],
                     'Wait For Limit': ['rap', 'upbeat', 'romance', 'relationship'],
                     'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

# First, create a set called user_tags.
user_tags = set()
# Use a loop to populate the set to contain all of the tags from the songs in user_song_history
for key, val in user_song_history.items():
    user_tags.update(set(val))

# repeat the same logic in order to collect all of the tags from the friend_song_history and store it in a set called friend_tags
friend_tags = set()
for key, val in friend_song_history.items():
    friend_tags.update(set(val))

# find the unique tags by getting the symmetric difference between user_tags and friend_tags. Store the result in a set called unique_tags and then print it!
unique_tags = user_tags ^ friend_tags
print(unique_tags)

music_tags = {'pop', 'warm', 'happy', 'electronic', 'synth', 'dance', 'upbeat'}

# create a frozenset called my_tags which contains the elements: 'pop', 'electronic', 'relaxing', 'slow', and 'synth'.
my_tags = frozenset(['pop', 'electronic', 'relaxing', 'slow', 'synth'])

# Try finding the union of music_tags and my_tags, but make sure to return the result as a frozenset. Store the result in a variable called frozen_tag_union
frozen_tag_union = my_tags | music_tags
print(frozen_tag_union)

# store the intersection of music_tags and my_tags into a variable called regular_tag_intersect. Make sure that it is stored as a normal set this time.
regular_tag_intersect = music_tags & my_tags
print(regular_tag_intersect)

# try finding the difference of my_tags with music_tags. Store this result in a variable called frozen_tag_difference. The type of the result should be a frozenset.
frozen_tag_difference = my_tags - music_tags
print(frozen_tag_difference)

# get the symmetric difference of music_tags with my_tags and store it in a variable called regular_tag_sd. The result should should be a set and not a frozenset
regular_tag_sd = music_tags ^ my_tags
print(regular_tag_sd)
