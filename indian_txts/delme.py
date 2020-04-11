import os

for year in range(8, 15):
    ids = open("20{:02d}_m.txt".format(year), 'r').read().splitlines()
    final = ""
    for eid in ids:
        spl = eid.split("\"")
        final += "https://open.spotify.com/track/" + spl[3] + '\n'
    file = os.path.join("20{:02d}.txt".format(year))
    output_file = open(file=file, mode='w', encoding='utf-8')
    output_file.write(final)
