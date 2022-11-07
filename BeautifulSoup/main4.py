import csv
from os import read
import requests
from bs4 import BeautifulSoup
def scrape_data(url):

    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.content, 'html5lib')
    mydivs = soup.find("div", {"class": "quote"})
    mydivs2 = soup.find("div", {"class": "tags"})
    for a in mydivs2:
        print(a.text)
    data = mydivs2.a['href']
    print(data)
    


if __name__=="__main__":
    url = "http://quotes.toscrape.com/page/1/"
    scrape_data(url)