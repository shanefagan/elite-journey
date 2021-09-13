import os
import requests
import glob

files_for_dl = (
    # "stations.json",
    "systems.csv",
    "commodities.json",
    "systems_populated.json",
)

files = glob.glob(os.path.join("data", "*"))
for f in files_for_dl:
    print(f"Downloading: {f}")
    f_data = requests.get(f"https://eddb.io/archive/v6/{f}", allow_redirects=True)
    with open(f"data/{f}", "w") as file_w:
        file_w.write(f_data.content.decode())
