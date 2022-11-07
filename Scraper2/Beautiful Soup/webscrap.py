from bs4 import BeautifulSoup
import requests

url = "https://www.flipkart.com/search?q=camera&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
response = requests.get(url)
htmlcontent = response.content
soup = BeautifulSoup(htmlcontent,'html.parser')
# print(soup.title.text)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.title.parent.name)
# print(soup.p)
# print(soup.a)
# print(soup.find_all("a"))
# print(soup.find("a"))
# print(soup.find(id="productRating_LSTSAYF2WVCFRVYM6R2UQGCNV_SAYF2WVCFRVYM6R2_").text)
# for link in soup.find_all('a'):
#     print(link.get('href'))
# for link in soup.find_all('img'):
#     print(link.get('src'))
# product =  soup.find('div',class_='_4rR01T')
# print(product)
product =  soup.find('div',attrs={'class':'_4rR01T'})
print(product.string)