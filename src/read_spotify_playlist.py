from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import json

#Login to spotify as the app
client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#Michelle's playlist for me'
playlist_id = 'spotfiy:user:spotifycharts:playlist:2XM8f66Ls7HteE14OErG65?si=3me0NPEXTsCz9zZ_nUOugA'
results = sp.playlist(playlist_id)
filter1 = results['tracks']
filter2 = filter1['items']
songs = []
for x in range(len(filter2)):
    song_name = filter2[x]['track']['name']
    artist_name = filter2[x]['track']['artists'][0]['name']
    album_name = filter2[x]['track']['album']['name']
    songs.append([song_name, artist_name, album_name])
search_list = []
for song in songs:
    key = song[0] + ":" + song[1] + ":" + song[2]
    print(key)
    search_list.append(key)
#print(json.dumps(results, indent=4))
