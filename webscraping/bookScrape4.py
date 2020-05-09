from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import lxml

html = urlopen('http://pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html.read(), 'lxml')
images = bs.find_all('img', {'src': re.compile('\.\./img/gifts/img.*\.jpg')})
for image in images:
    print(image['src'])

# tagsWithManyAttr = bs.findAll(lambda tag: len(tag.attrs) > 1)
# for tag in tagsWithManyAttr:
#     print(tag)
