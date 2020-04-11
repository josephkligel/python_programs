from bs4 import BeautifulSoup
import requests
import os

url = requests.get('https://en.wikipedia.org/wiki/List_of_Seinfeld_characters')
soup = BeautifulSoup(url.text, 'html.parser')

table = soup.find('table', {'class': 'wikitable'})
for row in table.tbody.find_all('tr'):
    if row.find('td') == None:
        pass
    else:
        character = row.find_all('td')[0].text
        with open('seinfield_chars.txt', 'a') as fh:
            fh.write(character+'\n')
