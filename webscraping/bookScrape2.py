from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'lxml')

# for child in bs.find('table', {'id': 'giftList'}).children:
#     print(child)
print([sibling for sibling in bs.find('table', {'id': 'giftList'}).tr.next_siblings])
