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

def writeToJson(repoList=gitRepos()):
    with open('remoteRepoList.json') as fr:
        repoDict = json.load(fr)

    with open('remoteRepoList.json', 'w') as fh:
        for i in repoList:
            if i not in repoDict:
                print(f'Adding {i} repo to repoDict')
                repoDict[i] = f'https://github.com/zigjag/{i}.git' 

        print('Writing a list of repos to json file...')
        json.dump(repoDict, fh, indent=4)
    print('Done writing. Exiting...')


if __name__ == '__main__':
    writeToJson(getRepos())
