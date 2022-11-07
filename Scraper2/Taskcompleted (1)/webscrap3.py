from bs4 import BeautifulSoup
import requests
import csv 
import pandas as pd
url = "https://www.flipkart.com/search?q=camera&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
response = requests.get(url)
htmlcontent = response.content
soup = BeautifulSoup(htmlcontent,'html.parser')

titles = []
prices = []
images = []

for d in soup.find_all('div',attrs={'class':'_2kHMtA'}):
    title = d.find('div',attrs={'class':'_4rR01T'})
    title = title.string
    titles.append(title)

    price = d.find('div',attrs={'class':'_1_WHN1'})
    price = price.string
    prices.append(price)
    image = d.find('img',attrs={'class':'_3exPp9'})
    image= image.get('src')
    images.append(image)
    
    
    
raw_data = {'title':titles,'price':prices,'image':images}
columns = ['title','price','image']
df = pd.DataFrame(raw_data,columns=columns)
df.to_csv('data.csv')