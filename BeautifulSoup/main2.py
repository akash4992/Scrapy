import csv
from os import read
import requests
from bs4 import BeautifulSoup
def scrape_data(url):

    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.content, 'html.parser')
    mydivs = soup.find_all("div", {"class": "orderweb__47414d10"})

    for tag in mydivs:
        data = tag.select("ul")
        for tag in data:
            all_li = tag.find_all('li')
            all_div = all_li[0].select('div')
            for p_tag in all_div:
                all_p_tag = p_tag.select('p')
                for read_text in all_p_tag:
                    for r in read_text:
                        final_read = r.replace("… placeholder text …", ' ')
                        print(final_read)
if __name__=="__main__":
    url = "https://deliveroo.co.uk/menu/london/soho/wingmans-soho"
    scrape_data(url)