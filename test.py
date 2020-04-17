import csv
import os

import spotipy
import pprint
from spotipy.oauth2 import SpotifyClientCredentials

client_id = 'b46646c01eed427696758b5a2588eff8'
client_secret = '87072aa12d634429a14c6fa2c7b41b0f'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace = False

# Get track list from playlists
# playlists_file = "indian_playlists.txt"
# playlists = open(playlists_file, 'r').read().splitlines()
# for year, playlist in enumerate(playlists):
#     print(year)
#     tracks = sp.playlist_tracks(playlist)
#     final = ""
#     for i in tracks['items']:
#         final += i['track']['external_urls']['spotify']
#         final += '\n'
#     file = os.path.join("indian_txts", "20{:02d}.txt".format(year))
#     open(file, 'w').writelines(final)

for year in range(0, 21):
    # Read input tracks list for current year
    file = os.path.join("indian_txts", "20{:02d}.txt".format(year))
    track_links = open(file, 'r').read().splitlines()
    file = open(os.path.join("indian_track_details", "20{:02d}.csv".format(year)), "w", newline='')
    writer = csv.writer(file)
    writer.writerow(["Song", "Artists", "Release Date", "Popularity"])
    print(year)
    for track in track_links:
        track_ret = sp.track(track)
        artists = []
        for artist in track_ret['artists']:
            artists.append(artist['name'])
        writer.writerow([track_ret['name'], artists, track_ret["album"]["release_date"], track_ret["popularity"]])


# result = sp.search(type="track", q="year:2000", limit=50)
# pprint.PrettyPrinter(indent=2).pprint(result)
# for item in result['tracks']['items']:
    # print(item['id'], " ", item['popularity'], " ", item['name'])

# tracks = sp.tracks(tracks=["0gzu5mm36VJH2Zqu8sQPTf"], market='IN')
# pprint.PrettyPrinter(indent=2).pprint(tracks)

# features = sp.audio_features("spotify:track:0gzu5mm36VJH2Zqu8sQPTf")
# pprint.PrettyPrinter(indent=2).pprint(features)

# categs = sp.category_playlists(country='IN', category_id='')
# pprint.PrettyPrinter(indent=2).pprint(categs)
