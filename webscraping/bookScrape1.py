from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import lxml

def getTitle(url):
    try:
        html = urlopen(url)
        bs = BeautifulSoup(html.read(), 'lxml')
        title = bs.body.h1
    except HTTPError as e:
        print('Connection was not made')
        return None
    except AttributeError as e:
        print("Attribute cannot be found")
        return None
    return title

title = getTitle('https://www.pythonscraping.com/pages/page1.html')
if title == None:
    print('Title could not be found')
else:
    print(title.Text)
