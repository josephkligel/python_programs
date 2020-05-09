from urllib.request import urlopen
from bs4 import BeautifulSoup
import re, lxml

html = urlopen('https://wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html.read(), 'lxml')
# for link in bs.findAll('a'):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])
# print('<'+'-'*20+'>')
# print(bs.a['id'])
for link in bs.find('div', {'id': 'bodyContent'}).findAll('a', href=re.compile('^(/wiki/)((?!:).)*$')):
    if 'href' in link.attrs:
        print(link.attrs['href'])
