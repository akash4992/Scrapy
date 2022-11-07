import json 
json_string = '''
        {
        "name":"akash",
        "age":25,
        "ismarried":true,
        "salary":1000.0,
        "isshavinggirlfriend":null
        }
    '''
emp_dict = json.loads(json_string)
# print(emp_dict)
#print(type(emp_dict))
# print('Employee Name:',emp_dict['name'])
# print('Employee Age:',emp_dict['age'])
# print('Employee Salary:',emp_dict['salary'])
# print('Employee Is Married:',emp_dict['ismarried'])
# print('Employee Is Having Girlfiend:',emp_dict['isshavinggirlfriend'])

for k,v in emp_dict.items():
    print('{}:{}'.format(k,v))