import requests
import json
def login():
    s = requests.session()
    payload = {
    "email": "akash.dhiman@drishinfo.com",
    "password": "dhiman$729"
    }
    res = s.post('https://api.giggl.app/v1/auth',json=payload)
    data = s.headers.update({'autherization':json.loads(res.content)['token']})
    return data

sess = login()
print(sess)
#r = sess.patch('https://api.giggl.app/v1/users/@me',json={'location':'Sweden'})
#print(r.content)