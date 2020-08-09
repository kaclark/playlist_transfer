from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys
import pprint

if len(sys.argv) > 1:
    search_str = sys.argv[1]
else:
    search_str = 'Radiohead'
#read input argv
#pull out song name for search
s_song_name = search_str.split(':')[0]
print(s_song_name)
s_artist_name = search_str.split(':')[1]
s_album_name = search_str.split(':')[2]

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
#search for song
results = sp.search(s_song_name)

filter1 = results['tracks']
filter2 = filter1['items']
#gather search results
songs = []
for x in range(len(filter2)):
    
    song_name = filter2[x]['name']
    
    ars = []
    artists = filter2[x]['artists']
    for y, artist in enumerate(artists):
        ars.append(artists[y]['name'])
    all_artists = " ".join(ars)

    album_name = filter2[x]['album']['name']
    sp_id = filter2[x]['uri'].split(':')[-1]
    songs.append([song_name, all_artists, album_name, sp_id])

#filter results for requested song
match_found = False
for song in songs:
    if song[0] == s_song_name and song[1] in s_artist_name and song[2] == s_album_name:
        print("Song found! Spotify track id is: " + str(song[3]))
        match_found = True
if match_found == False:
    print("Match not found")
#pprint.pprint(result)
