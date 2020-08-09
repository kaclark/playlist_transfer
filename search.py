from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys
import pprint

if len(sys.argv) > 1:
    search_str = sys.argv[1]
else:
    search_str = 'Radiohead'

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
results = sp.search(search_str)

#s_song_name = search_str.split(':')[0]
#s_artist_name = search_str.split(':')[1]
#s_album_name = search_str.split(':')[2]

filter1 = results['tracks']
filter2 = filter1['items']
songs = []
for x in range(len(filter2)):
    song_name = filter2[x]['track']['name']
    artist_name = filter2[x]['track']['artists'][0]['name']
    album_name = filter2[x]['track']['album']['name']
    songs.append([song_name, artist_name, album_name])

for song in songs:
    if song[0] == s_song_name and song[1] == s_artist_name and song[2] == s_album_name:
        print("Song found")
    else:
        print("Song not found")

#pprint.pprint(result)
