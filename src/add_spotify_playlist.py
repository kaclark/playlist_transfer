import argparse
import logging
import spotipy.util as util
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
logger = logging.getLogger('add_spotify_playlist')
logging.basicConfig(level='DEBUG')
scope = 'playlist-modify-public'

def get_args():
    parser = argparse.ArgumentParser(description='Adds track to user playlist')
    parser.add_argument('-u', '--usr', required=True, help='User who will have playlist accessed')
    parser.add_argument('-t', '--tids', action='append', required=True, help='Track ids')
    parser.add_argument('-p', '--playlist', required=True, help='Playlist to add track to')
    return parser.parse_args()

def main():
    args = get_args()
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, cache_path="C:/Users/12283/Documents/GitHub/playlist_transfer/cache"))
    sp.user_playlist_add_tracks(args.usr, args.playlist, args.tids) 
    #This isn't a method?'
    #sp.playlist_add_items(args.playlist, args.tids)

if __name__ == '__main__':
    main()
