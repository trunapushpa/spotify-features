import csv
import json
import os

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = 'b46646c01eed427696758b5a2588eff8'
client_secret = '87072aa12d634429a14c6fa2c7b41b0f'
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace = False

playlists_yearwise = open("western_playlists.txt", 'r').read().splitlines()
year = 0
for playlist_link in playlists_yearwise:
    playlist = sp.playlist_tracks(playlist_link, limit=100)
    ids = []
    file = open(os.path.join("western_track_details", "20{:02d}.csv".format(year)), "w", newline='')
    writer = csv.writer(file)
    writer.writerow(["Song", "Artists", "Release Date", "Popularity"])
    print(year)
    for item in playlist['items']:
        cur_id = item['track']['id']
        if not cur_id:
            continue
        ids.append(cur_id)
        track_ret = sp.track(cur_id)
        artists = []
        for artist in track_ret['artists']:
            artists.append(artist['name'])
        try:
            writer.writerow([track_ret['name'], artists, track_ret["album"]["release_date"], track_ret["popularity"]])
        except:
            continue
    features = sp.audio_features(tracks=ids)
    file = os.path.join("western_jsons", "20{:02d}.json".format(year))
    output_file = open(file=file, mode='w', encoding='utf-8')
    json.dump(obj=features, fp=output_file, indent=4)
    year = year + 1
