from bs4 import BeautifulSoup
import requests
file_name = "d1.txt"
file = open(file_name, 'wb')
index_url = "https://horriblesubs.info/api.php?method=getshows&type=show&showid=347&nextid=0"
response = requests.get(index_url)
soup = BeautifulSoup(response.text,'html.parser')
print(soup)

