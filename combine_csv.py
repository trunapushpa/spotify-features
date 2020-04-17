import os
import pandas as pd
import glob

path = 'western_track_details'
all_files = glob.glob(os.path.join(path, "*.csv"))

writer = pd.ExcelWriter('westerntracks.xlsx', engine='xlsxwriter')

for f in all_files:
    df = pd.read_csv(f)
    df.to_excel(writer, sheet_name=os.path.splitext(os.path.basename(f))[0], index=False)

writer.save()
