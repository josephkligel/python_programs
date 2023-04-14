from content import Content
import requests
import sys
import os
from pathlib import Path

# Class to scrape GitHub repos using Content class
class GithubRepos(Content):
    def __init__(self, user='josephkligel'):
        
        # Github api to get a list of all repos of a given user
        self.urlStr = f'https://api.github.com/users/{user}/repos'
        
        # Call parent init method to inherit its methods and attributes
        #headers = {'Authorization': f'token {os.getenv("token")}'}
        super().__init__(self.urlStr)
        
        # Get repo information
        self.repoData = self.response.json()
        self.repoUrls = [repo['clone_url'] for repo in self.repoData]
        # Write repos to text
        self.writeRepos()

    def countRepos(self):
        print(f'----- {len(self.repoUrls)} Repos -----')

    def printRepos(self):
        for url in self.repoUrls:
            print(url)

    def writeRepos(self):
        parent = Path(__file__).parent
        reposFile = parent.joinpath('repos.txt')
        with open(reposFile, 'w') as fw:
            print('Writing repos to text file...')
            fw.writelines('\n'.join(self.repoUrls))

# Call class a stand-alone script
if __name__ == '__main__':
    repos = GithubRepos()
    repos.countRepos()
    repos.printRepos()
