def get_daily_movie():
    print('Retrieving the movie set to play on today\'s flight...')
    return ['Parasite', 'Nomadland', 'Roma', 'Black Widow', 'Spiral']


def get_licensed_movies():
    print('Retrieving the list of licenses movies from the database...')
    licensed_movies = ['Parasite', 'Nomadland', 'Roma']
    return licensed_movies


def get_wifi_status():
    print('Checking WiFi signal...')
    print('WiFi is active')
    return True

def get_device_temp():
    print('Reading the temperature of the entertainment system device...')
    return 40

def get_maximum_display_brightness():
    print('Calculating maximum display brightness in nits...')
    return 399.99999999
