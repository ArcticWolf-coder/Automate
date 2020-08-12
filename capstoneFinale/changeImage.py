import os
from PIL import Image

path = ""
path += os.path.expanduser("~")
path += "/supplier-data/images"

for i in os.listdir(path):
    if "tiff" in i:
        im = Image.open(path + i)
        im.resize((600, 400)).convert("RGB").save(path + i.split(".")[0], "jpeg")
        im.close()
