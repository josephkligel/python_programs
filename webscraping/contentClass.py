import requests
import lxml
from bs4 import BeautifulSoup

class Content:
    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body

def getPage(url):
    req = requests.get(url)
    return BeautifulSoup(req.text, 'lxml')
    
def scrapeNYTimes(url):
    bs = getPage(url)
    title = bs.find('h1').text
    lines = bs.find_all('p', class_='css-nnwssh')
    body = '\n'.join([line.text for line in lines])
#    body = bs.find('section', class_='meteredContent').text
    return Content(url, title, body)

def scrapeBrookings(url):
    bs = getPage(url)
    title = bs.find('h1').text
    body = bs.find('div', {'class': 'post-body'}).text
    return Content(url, title, body)

url = 'https://www.brookings.edu/blog/future-development/2018/01/26/delivering-inclusive-urban-access-3-uncomfortable-truths/'

content = scrapeBrookings(url)
print(f'Title: {content.title}')
print(f'URL: {content.url}\n')
print(content.body)

url = 'https://www.nytimes.com/2018/01/25/opinion/sunday/silicon-valley-immortality.html'

content = scrapeNYTimes(url)
print(f'Title: {content.title}')
print(f'URL: {content.url}\n')
print(content.body)
