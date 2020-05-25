from urllib.request import urlopen
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import lxml
import argparse
import re
import sys
from pprint import pprint

parser = argparse.ArgumentParser(description='A web crawling program to collect external links from site')
parser.add_argument('-u', '--url', help='Type url address after flag. Make sure to include all beginning schemes.')
parser.add_argument('-d', '--depth', help='The max number of links that are to be found')
args = parser.parse_args()

def getExternalLinks(url, count=10):
    try:
        externalLinks = set()
        html = requests.get(url)
        bs = BeautifulSoup(html.text, 'lxml')
        for link in bs.findAll('a', href=re.compile('^(http|www).*$')):
            if link.attrs['href'] != None and link.attrs['href'] not in externalLinks:
                externalLinks.add(link.attrs['href'])
    except AttributeError as ae:
        print('No external links were found. Continuing.')
    except Exception as e:
        print('Error during the runtime of getExternalLinks: (%s)' % (e))
    pprint(externalLinks)
    return externalLinks



if len(sys.argv) < 2:
    print('-'*10 + 'No arguments' + '-'*10)
    url = str(input('Type string here (make sure to include schemes): '))
    depth = int(input('How many links do you want to be found? '))
    getExternalLinks(url, count=depth)
else:
    url = args.url or url.u
    depth = args.depth or args.d
    getExternalLinks(url, count=depth)
