import csv
from os import read
import requests
from bs4 import BeautifulSoup
def scrape_data(url):

    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.content, 'html5lib')
    mydivs = soup.find_all("div", {"class": "orderweb__47414d10"})
    for data in mydivs:
        print(data.ul.li.div.p.text)
    # print(mydivs.ul.li)
    # print(mydivs.ul.li.div.p.text)
    
    
  

if __name__=="__main__":
    url = "https://deliveroo.co.uk/menu/london/soho/wingmans-soho"
    scrape_data(url)