import json


myfile = open("/home/dr74/Python/website_read/pandass/filedata.json", 'r')
read_obj = myfile.read()
obj = json.loads(read_obj)
# print(obj['First_Name'])
# print(obj['Last_Name'])
print(obj.get('Last_Name'))
list1 = obj['Address']
# print(list1[0])
# print(len(list1))
for i in range(len(list1)):
    print(list1[i].get('street'))
for o in obj['Address']:
    print(o.get('street'))

for k,v in obj.items():
    print("the value {}:{}".format(k,v))