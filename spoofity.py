import sys
from subprocess import Popen, PIPE
import dbus
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

def authorize():

    cred = json.load(open('credentials.json'))
    client_id = cred['ID']
    client_secret = cred['Secret']
    user = cred['User']
    uri = cred['redirect_uri']
    scope = 'user-library-read'

    tok = util.prompt_for_user_token(user, scope, client_id=client_id, client_secret=client_secret,\
        redirect_uri=uri)    
    return spotipy.Spotify(auth=tok)

def main(argv):
    spotify = authorize()
    res = spotify.search(q=argv[0])
    print(res)

if __name__ == '__main__':
    main(sys.argv[1:])
