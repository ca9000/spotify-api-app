from create_file import create_csv
from spotify_api import SpotifyAPI

spotify = SpotifyAPI()
column, rows = spotify.get_search("NF", search_type='track')

create_csv("data.csv", "write", column, rows)
