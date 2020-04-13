import requests
from bs4 import BeautifulSoup

url = requests.get('https://scrapingclub.com/exercise/list_basic/')
html = BeautifulSoup(url.text, 'lxml')

pageLinks = sorted({i.get('href') for i in html.findAll('a', class_='page-link')})
print(pageLinks)
