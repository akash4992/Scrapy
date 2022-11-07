from pickletools import optimize
from bs4 import BeautifulSoup
import requests
import re
import json
import pandas as pd

headers = {
        'X-Requested-With': 'XMLHttpRequest'
}
url = 'https://librivox.org/advanced_search?title=&author=&reader=&keywords=&genre_id=0&status=all&project_type=either&recorded_language=&sort_order=alpha&search_page=1&search_form=advanced&q=The Time machine'
response = requests.get(url,headers=headers)
data = response.json()
authors = []
titles = []
soup = BeautifulSoup(data['results'],'lxml')
book_titles = soup.select('h3 >a')
book_author  = soup.select('p >a')
for auth in book_author:
    authors.append(auth.text)
for item in book_titles:
    titles.append(item.text)

raw_data = {'title':titles,'author':authors}
columns = ['title','author']
df = pd.DataFrame(raw_data,columns=columns)
df.to_csv('librivox.csv')