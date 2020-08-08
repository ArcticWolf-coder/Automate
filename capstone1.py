#!/usr/bin/env python3
import os
from PIL import Image
old=""
old+=os.path.expanduser('~')
old+="/images/"
new="/opt/icons/"

for i in os.listdir(old):
        if "." not in i[0]:
                im=Image.open(old+i)
                im.rotate(-90).resize((128,128)).convert("RGB").save(new+i.split(".")[0],"jpeg")
                im.close()
