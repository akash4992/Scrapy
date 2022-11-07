
import requests
import json
from bs4 import BeautifulSoup
import datetime
import pandas as pd
import creds
login_url = ('https://the-internet.herokuapp.com/authenticate')
secure_url = ('https://the-internet.herokuapp.com/secure')
payload = {
    'username': creds.username,
    'password': creds.password
}
r = requests.post(login_url,data=payload)

r2 = requests.get(secure_url)
titles = []
content = []

with requests.session() as s:
    s.post(login_url,data=payload)
    r = s.get(secure_url)
    soup = BeautifulSoup(r.content,'html.parser')
    data2 = soup.find("div",class_="example")
    title = data2.find('h2')
    titles.append(title.text)
    data = soup.find("h4",class_="subheader")
    content.append(data.text)

raw_data = {'title':titles,'content':content}
columns = ['title','content']

df = pd.DataFrame(raw_data,columns=columns)
df.to_csv('data2.csv')