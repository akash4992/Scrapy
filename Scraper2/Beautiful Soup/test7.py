from ctypes.wintypes import HMODULE
import requests
from bs4 import BeautifulSoup
import datetime
import pandas as pd
cookies = {
    'ASP.NET_SessionId': 'bhykfvrhwu0x1rpcu3op0ldt',
    '_accessToken': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1bmlxdWVfbmFtZSI6IjcwNjEyODk0OSIsIlVUWSI6IlMiLCJyb2xlIjpbIjUiLCIxMDEiXSwiU0lEIjoiMjIiLCJUSUQiOiI3MDYxMjg5NDkiLCJJQUwiOiJGYWxzZSIsIkFJRCI6IjAiLCJPSUQiOiIwIiwiaXNzIjoiaHR0cHM6Ly9hdXRoLmd1cnUuY29tLyIsImF1ZCI6Imh0dHBzOi8vd3d3Lmd1cnUuY29tL2FwaSIsImV4cCI6MTk3OTM3NjM0NiwibmJmIjoxNjYzNzU3MTQ2fQ.zOOVpg8JlbA9If5tR7Swr-Hs4LKj0Xpg1D6RvyD93Fw',
    '_refreshToken': '',
    '_clientID': '706128949',
    'visid_incap_1227176': 'ZCL2eHf5R9GyXp7idA0/w1nrKmMAAAAAQUIPAAAAAACz3ixwBMFtqh6mqP8V1SCr',
    'nlbi_1227176': '6nScN3pRhBm5veIBmoY5nwAAAABB7C7xmF/A9RTGTGRGvws5',
    'incap_ses_737_1227176': 'yK1QU5a6aFI9v/Z4n1o6ClrrKmMAAAAAqEaEqXBfUcS0HFwnU+7H4w==',
    '_gcl_au': '1.1.81552868.1663757149',
    '_gid': 'GA1.2.1550264273.1663757149',
    '_dc_gtm_UA-433689-4': '1',
    'AWSALB': 'ncKSjctHDh2rXxSGLRZA9KIXg08lSZckZuES5fNkbjX3LUxqbcx2a3RpGwg0LjBNdhvvLhQjeDADuHTSZkOH6ojvfIuPWsNAwjt+MQZlyxZJiG8fPwzYIG6jQ0fF',
    'AWSALBCORS': 'ncKSjctHDh2rXxSGLRZA9KIXg08lSZckZuES5fNkbjX3LUxqbcx2a3RpGwg0LjBNdhvvLhQjeDADuHTSZkOH6ojvfIuPWsNAwjt+MQZlyxZJiG8fPwzYIG6jQ0fF',
    '_ga_6DQ0MCG0VT': 'GS1.1.1663757149.1.1.1663757220.60.0.0',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Wed+Sep+21+2022+16%3A17%3A00+GMT%2B0530+(India+Standard+Time)&version=6.33.0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0&AwaitingReconsent=false',
    '_ga': 'GA1.2.958333966.1663757149',
}

headers = {
    'authority': 'www.guru.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'ASP.NET_SessionId=bhykfvrhwu0x1rpcu3op0ldt; _accessToken=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1bmlxdWVfbmFtZSI6IjcwNjEyODk0OSIsIlVUWSI6IlMiLCJyb2xlIjpbIjUiLCIxMDEiXSwiU0lEIjoiMjIiLCJUSUQiOiI3MDYxMjg5NDkiLCJJQUwiOiJGYWxzZSIsIkFJRCI6IjAiLCJPSUQiOiIwIiwiaXNzIjoiaHR0cHM6Ly9hdXRoLmd1cnUuY29tLyIsImF1ZCI6Imh0dHBzOi8vd3d3Lmd1cnUuY29tL2FwaSIsImV4cCI6MTk3OTM3NjM0NiwibmJmIjoxNjYzNzU3MTQ2fQ.zOOVpg8JlbA9If5tR7Swr-Hs4LKj0Xpg1D6RvyD93Fw; _refreshToken=; _clientID=706128949; visid_incap_1227176=ZCL2eHf5R9GyXp7idA0/w1nrKmMAAAAAQUIPAAAAAACz3ixwBMFtqh6mqP8V1SCr; nlbi_1227176=6nScN3pRhBm5veIBmoY5nwAAAABB7C7xmF/A9RTGTGRGvws5; incap_ses_737_1227176=yK1QU5a6aFI9v/Z4n1o6ClrrKmMAAAAAqEaEqXBfUcS0HFwnU+7H4w==; _gcl_au=1.1.81552868.1663757149; _gid=GA1.2.1550264273.1663757149; _dc_gtm_UA-433689-4=1; AWSALB=ncKSjctHDh2rXxSGLRZA9KIXg08lSZckZuES5fNkbjX3LUxqbcx2a3RpGwg0LjBNdhvvLhQjeDADuHTSZkOH6ojvfIuPWsNAwjt+MQZlyxZJiG8fPwzYIG6jQ0fF; AWSALBCORS=ncKSjctHDh2rXxSGLRZA9KIXg08lSZckZuES5fNkbjX3LUxqbcx2a3RpGwg0LjBNdhvvLhQjeDADuHTSZkOH6ojvfIuPWsNAwjt+MQZlyxZJiG8fPwzYIG6jQ0fF; _ga_6DQ0MCG0VT=GS1.1.1663757149.1.1.1663757220.60.0.0; OptanonConsent=isGpcEnabled=0&datestamp=Wed+Sep+21+2022+16%3A17%3A00+GMT%2B0530+(India+Standard+Time)&version=6.33.0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0&AwaitingReconsent=false; _ga=GA1.2.958333966.1663757149',
    'referer': 'https://www.guru.com/',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
}

response = requests.get('https://www.guru.com/d/jobs/', cookies=cookies, headers=headers)
soup = BeautifulSoup(response.content,'html.parser')
# author_element =  soup.find("h2",class_="jobRecord__title")
titles = soup.select('h2 >a')

for title in titles:
    print(title.text)