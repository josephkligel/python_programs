from bs4 import BeautifulSoup
import requests

url = 'https://scrapingclub.com/exercise/list_basic/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
items = soup.findAll('div', class_='col-lg-4')
pageLinks = sorted([i.get('href') for i in soup.findAll('a', class_='page-link')])
pageLinks[0] = '?page=1'

count = 1
for i in pageLinks:
    newUrl = url + i
    response = requests.get(newUrl)
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.findAll('div', class_='col-lg-4')
    for i in items:
        try:
            itemName = i.h4.text.strip()
            itemPrice = i.h5.text.strip()
            print(f'{count}) {itemName}: {itemPrice}')
            count+=1
        except AttributeError:
            continue
