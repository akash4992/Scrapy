import json
from textwrap import indent
people_string = '''
   {
       "people": [
           {
                "name": "john smith",
                "phone": "615-555-7164",
                "email": ["akash@gmail.com","rohit@gmail.com"] ,
                "has_lisence": false
            },
            {
                "name": "john Doe",
                "phone": "615-666-7164",
                "email": ["soni@gmail.com","jassi@gmail.com"] ,
                "has_lisence": true
            }

        ]    
   }
'''


data = json.loads(people_string)
#print(data)


# print(type(data['people']))

for person in data['people']:
    del person['phone']


new_string = json.dumps(data,indent=2,sort_keys=True)
print(new_string)