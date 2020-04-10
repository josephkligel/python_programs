import requests
from bs4 import BeautifulSoup

url = requests.get('https://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(url.text, 'html.parser')

nameList = bs.find_all('span', {'class': 'green'})
for name in nameList:
    print(name.text)
