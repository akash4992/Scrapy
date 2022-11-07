from bs4 import BeautifulSoup
import requests
import csv 
import dryscrape
import pandas as pd
session = dryscrape.Session()
url = "https://avi.im/stuff/js-or-no-js.html"
session.visit(url)
response = session.body()
soup = BeautifulSoup(response)
text = soup.find(id="intro-text")
print(text)

