from bs4 import BeautifulSoup
import urllib
import sys, requests, lxml, os, re

if len(sys.argv) > 1:
    booktitle = ''.join(sys.argv[1:])
else:
    booktitle = 'Huckleberry Finn' #TODO

def get_book(booktitle):
    url = 'https://libgen.is/search.php?req='+booktitle
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
 
    links = []
    for link in soup.select('a[title=""]'):
        if booktitle in link.getText():
            links.append('https://libgen.is/' + link.get('href'))
    download(links[0])

def download(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    title = soup.select_one('a[title="Gen.lib.rus.ec"]').get('href')
    
    res = requests.get(title)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')
    downloadLink = soup.select_one('a').get('href')
    print('Downloading', downloadLink)
    pdf = requests.get(downloadLink)

    with open(booktitle + '.pdf', 'wb') as fh:
        fh.write(pdf.content)

get_book(booktitle)
