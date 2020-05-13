from bs4 import BeautifulSoup
import requests
from urllib import parse
import lxml
import re
from pprint import pprint
import sys
import pandas as pd

linkList = set()
df = pd.DataFrame(columns=['Company', 'P/E TTM'])

ticker = input('What ticker do you want to lookup? ').upper()
url = f'https://finance.yahoo.com/quote/{ticker}?p={ticker}&.tsrc=fin-srch'
html = requests.get(url)
try:
    bs = BeautifulSoup(html.text, 'lxml')
except Exception as e:
    print(f'url error: {e}')

def get_links(url=url):
    try:
        global linkList
        html = requests.get(url)
        bs = BeautifulSoup(html.text, 'lxml')
        for link in bs.findAll('a'):# TODO:
            if 'href' in link.attrs:
                linkList.add(f'https://finance.yahoo.com{link.attrs["href"]}')
    except AttributeError:
        print('Attribute could not be found')
    except Exception as e:
        print(f'get_links functions error: {e}')
    return linkList

def get_ratios(url=url):
    try:
        ticker = bs.h1.text
        pe_ratio = bs.find('span', text=re.compile('.*PE.*'))

        global df
        df = df.append({'Company': ticker, 'P/E TTM': pe_ratio.parent.next_sibling.text}, ignore_index=True)
        df.index.name = 'id'
        # print(df)
    except Exception as e:
        print(f'get_ratios function error: {e}')

def main():
    # get_links()
    # get_ratios()
    for i in get_links():
        get_ratios(i)
    print(df)

if __name__ == '__main__':
    main()
