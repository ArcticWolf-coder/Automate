import re
import operator

line = "May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)"
r=re.search(r"ticky: INFO: ([\w ]*) ", line)
print(r[1])
line = "May 27 11:45:40 ubuntu.local ticky: ERROR: Error creating ticket [#1234] (username)"
r=re.search(r"ticky: ERROR: ([\w ]*) ", line)
print(r[1])

fruit = {"oranges": 3, "apples": 5, "bananas": 7, "pears": 2}
fruit["orange"]=int(fruit.get("orange"))+1
f=sorted(fruit.items())

print(f)
f=sorted(fruit.items(),key=operator.itemgetter(1), reverse=True)
print(f)

