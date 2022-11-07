from curses.ascii import SO
from pickletools import optimize
from bs4 import BeautifulSoup
import requests
import re
import json

response = requests.get('http://quotes.toscrape.com/js/')
soup = BeautifulSoup(response.text,'lxml')
scrapt_tag = soup.find('script',src=None)
pattern = "var data = (.+?);\n"
raw_data = re.findall(pattern,scrapt_tag.string,re.S)
if raw_data:
    data = json.loads(raw_data[0])
new_data = data[0]
my_data = new_data['author']
