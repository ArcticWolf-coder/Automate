import os, requests, json

path=""
path+="supplier-data/descriptions"

for i in os.listdir(path):
    sum={}
    if "txt" in i:
        f = open(os.path.join(path, i))
        num = f.readlines()
        sum["name"]=num[0].strip()
        n=num[1].strip()
        sum["weight"]=int(n.split(" ")[0])
        sum["description"]=num[2].strip()
        sum["image_name"]=i.strip(".txt")+".jpeg"
        f.close()
        response = requests.post("http://35.192.36.244/fruits",json=sum)
        print(response.status_code)