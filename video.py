import json
import os
import matplotlib.pyplot as plt
import cv2

video_name = 'video.avi'

for year in range(0, 21):
    features_array = json.load(open(os.path.join("indian_jsons", "20{:02d}.json".format(year)), 'r'))
    valence = []
    energy = []
    for num, song in enumerate(features_array):
        if num > 50:
            break
        energy.append((song["energy"] - .5) * 6)
        valence.append((song["valence"] - .5) * 6)
    plt.clf()
    plt.scatter(valence, energy, label="Songs", color="blue", marker=".", s=50)
    plt.xlabel('Valence')
    plt.ylabel('Arousal')
    plt.legend = None

    plt.title("20{:02d}".format(year))
    plt.xlim(-3, 3)
    plt.ylim(-3, 3)
    plt.savefig(os.path.join("figs", "20{:02d}.png".format(year)))

images = [img for img in os.listdir("figs") if img.endswith(".png")]
frame = cv2.imread(os.path.join("figs", images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, 2, (width, height))

for image in images:
    video.write(cv2.imread(os.path.join("figs", image)))

cv2.destroyAllWindows()
video.release()
