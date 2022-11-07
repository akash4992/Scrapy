import bs4
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
link='https://www.flipkart.com/search?q=tv&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_8_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_8_0_na_na_na&as-pos=8&as-type=TRENDING&suggestionId=tv&requestId=9c9fa553-b7e5-454b-a65b-bbb7a9c74a29'

page = requests.get(link)
# print(page.content)
soup = bs(page.content, 'html.parser')
# print(soup.prettify())

name=soup.find('div',class_="_4rR01T")
# print(name.text)

rating = soup.find('div',class_='_3LWZlK')
# print(rating.text)
specification=soup.find('div',class_="fMghEO")

price=soup.find('div',class_='_30jeq3 _1_WHN1')


products=[]          
prices=[]                
ratings=[]             
os = []             
hd = []               
for data in soup.findAll('div',class_='_3pLy-c row'):
    name = soup.find('div',class_="_4rR01T")
    products.append((name.text))
    rating = soup.find('div',class_='_3LWZlK')
    ratings.append(rating.text)
    price=data.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
    prices.append(price.text)
    specification = data.find('div', attrs={'class':'fMghEO'})
    for each in specification:
            spec=each.find_all('li',class_='rgWa7D')
            os.append(spec[0].text)
            hd.append(spec[1].text)

# print(len(products))
# print(len(price))
# print(len(ratings))
# print(len(os))
# print(len(hd))

df=pd.DataFrame({'Product Name':products,'OS':os,"Resolution":hd,'Price':prices,'Rating':ratings})
df.to_csv('flipkart.csv')