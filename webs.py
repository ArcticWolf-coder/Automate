import json
import requests

#json
people = [
    {
        "name": "Sabrina Green",
        "username": "sgreen",
        "phone": {
            "office": "802-867-5309",
            "cell": "802-867-5310"
        },
        "department": "IT Infrastructure",
        "role": "Systems Administrator"
    },
    {
        "name": "Eli Jones",
        "username": "ejones",
        "phone": {
            "office": "684-348-1127"
        },
        "department": "IT Infrastructure",
        "role": "IT Specialist"
    },
]

with open('people.json', 'w') as people_json:
    json.dump(people, people_json, indent=2)

with open('people.json', 'r') as people_json:
    pupils = json.load(people_json)

print(pupils)

#requests GET
response = requests.get('https://www.google.com' ) 
print(response.status_code) #OR .ok as boolean
print(response.text[:50])
print(response.request.url)

#requests POST
p = {"description": "white kitten",
    "name": "Snowball", "age_months": 6}
response = requests.post("https://example.com/path/to/api", json=p)
print(response.request.body)
response.raise_for_status
