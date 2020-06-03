import re
import operator
import sys
import csv

errs=dict()
users=dict()


f=open("syslog.log")
for line in f:
                  
    e=re.search(r"(INFO|ERROR) ([\w' ]+)[\d\[\]#]* \((\w+[\.\w+]*)\)$", line)
    if e is None:
        continue
    
    if "ERROR" in e[1]:    
        errs[e[2]]=errs.get(e[2],0)+1
        if e[3] not in users:
            users[e[3]]={"INFO":0,"ERROR":1}
        else:
            users[e[3]]["ERROR"] += 1
    else :
        if e[3] not in users:
            users[e[3]]={"INFO":1,"ERROR":0}
        else:
            users[e[3]]["INFO"] += 1
    
f.close()

errs= [("Error", "Count")] + sorted(errs.items(),key=operator.itemgetter(1), reverse=True)
users= sorted(users.items())
f=open("error_message.csv","w")
for file in errs:
    sum=file[0]+", "+str(file[1])+"\n"
    f.write(sum)
f.close()
f=open("user_statistics.csv","w")
f.write("Username, INFO, ERROR\n")
for file in users:
    sum=file[0]+", "+str(file[1].get("INFO"))+", "+str(file[1].get("ERROR"))+"\n"
    f.write(sum)
f.close()





