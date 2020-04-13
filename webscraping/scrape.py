import requests
from bs4 import BeautifulSoup
import lxml
import pandas as pd

url = requests.get("http://quotes.toscrape.com/")
soup = BeautifulSoup(url.text, 'lxml')
quotes = soup.findAll('span', class_='text')
authors = soup.findAll('small', class_='author')
tags = soup.findAll('div', class_='tags')

# dct = {}
for i in range(len(quotes)):
    print(quotes[i].text, authors[i].text, sep='--')
    print('Tags: ')
    for tag in tags[i].findAll('a', class_='tag'):
        print('\t' + tag.text)
    print('\n')
