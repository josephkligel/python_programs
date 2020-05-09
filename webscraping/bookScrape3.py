from urllib.request import urlopen
from bs4 import BeautifulSoup
import lxml

html = urlopen('https://pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html.read(), 'lxml')
print(bs.find('img', {'src': '../img/gifts/img1.jpg'}).parent.previous_sibling.getText())
