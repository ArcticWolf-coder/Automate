import requests
import os

path = ""
path += "supplier-data/images/"
url = "http://localhost/upload/"

for i in os.listdir(path):
    if "jpeg" in i:
        with open(path + i, "rb") as opened:
            r = requests.post(url, files={"file": opened})

