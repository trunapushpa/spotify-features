import csv
import json
import os
import statistics

file = open("western.csv", "w", newline='')
writer = csv.writer(file)
writer.writerow(["year", "danceability", "energy", "key", "loudness", "speechiness",
                 "acousticness", "instrumentalness", "liveness", "valence", "tempo"])
for year in range(0, 21):
    features_array = json.load(open(os.path.join("western_jsons", "20{:02d}.json".format(year)), 'r'))
    danceability = []
    energy = []
    key = []
    loudness = []
    speechiness = []
    acousticness = []
    instrumentalness = []
    liveness = []
    valence = []
    tempo = []
    for song in features_array:
        danceability.append(song["danceability"])
        energy.append(song["energy"])
        key.append(song["key"])
        loudness.append(song["loudness"])
        speechiness.append(song["speechiness"])
        acousticness.append(song["acousticness"])
        instrumentalness.append(song["instrumentalness"])
        liveness.append(song["liveness"])
        valence.append(song["valence"])
        tempo.append(song["tempo"])

    writer.writerow(["20{:02d}".format(year),
                    statistics.mean(danceability),
                    statistics.mean(energy),
                    statistics.mean(key),
                    statistics.mean(loudness),
                    statistics.mean(speechiness),
                    statistics.mean(acousticness),
                    statistics.mean(instrumentalness),
                    statistics.mean(liveness),
                    statistics.mean(valence),
                    statistics.mean(tempo)])
