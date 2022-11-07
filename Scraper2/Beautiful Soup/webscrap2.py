from bs4 import BeautifulSoup
import requests
import csv 
url = "https://www.flipkart.com/search?q=camera&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
response = requests.get(url)
htmlcontent = response.content
soup = BeautifulSoup(htmlcontent,'html.parser')
with open('housing.csv', 'w',encoding="utf8",newline='') as f:
    thewriter = csv.writer(f)
    header = ['Title','Price','Images',]
    thewriter.writerow(header)
    for d in soup.find_all('div',attrs={'class':'_2kHMtA'}):
        title = d.find('div',attrs={'class':'_4rR01T'})
        title = title.string
        price = d.find('div',attrs={'class':'_1_WHN1'})
        price = price.string
        image = d.find('img',attrs={'class':'_3exPp9'})
        images= image.get('src')
        info = [title,price,images]
        thewriter.writerow(info)
    
    
