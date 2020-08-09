import os
import requests

path = "/data/feedback"
for file in os.listdir(path):
    f = open(os.path.join(path, file))
    sum = {}
    num = f.readlines()
    sum["title"] = num[0].strip()
    sum["name"] = num[1].strip()
    sum["date"] = num[2].strip()
    sum["feedback"] = num[3].strip()
    f.close()
    response = requests.post("http://34.72.135.168/feedback/", json=sum)
    print(response.status_code)
