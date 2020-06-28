#!/usr/bin/env python
from bs4 import BeautifulSoup
import lxml
import requests
import json

def getRepos():
    url = 'https://github.com/zigjag?tab=repositories'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    
    repoList = [i.getText().strip() for i in soup.select('#user-repositories-list > ul > li > div.col-10.col-lg-9.d-inline-block > div.d-inline-block.mb-1 > h3 > a')]
    return repoList

def writeToJson(repoList):
    with open('repoList.json', 'w') as fh:
        repoDict = {i:f'https://github.com/zigjag/{i}.git' for i in repoList}

        print('Writing repolist to json file...')
        json.dump(repoDict, fh, indent=4)
    print('Done writing. Exiting...')


if __name__ == '__main__':
    writeToJson(getRepos())
