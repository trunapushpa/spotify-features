import json
import os

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = 'b46646c01eed427696758b5a2588eff8'
client_secret = '87072aa12d634429a14c6fa2c7b41b0f'
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace = False

for year in range(8, 15):

    # Read input tracks list for current year
    file = os.path.join("indian_txts", "20{:02d}.txt".format(year))
    track_links = open(file, 'r').read().splitlines()

    # Extract Features
    features = sp.audio_features(tracks=track_links)
    file = os.path.join("indian_jsons", "20{:02d}.json".format(year))
    output_file = open(file=file, mode='w', encoding='utf-8')
    json.dump(obj=features, fp=output_file, indent=4)
