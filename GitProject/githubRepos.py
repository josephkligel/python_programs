from content import Content
import requests
import sys
import os

class GithubRepos(Content):
    def __init__(self, user='zigjag'):
        
        # Github api to get a list of all repos of a given user
        self.urlStr = f'https://api.github.com/users/{user}/repos'
        
        # Call parent init method to inherit its methods and attributes
        headers = {'Authorization': f'token {os.getenv("token")}'}
        super().__init__(self.urlStr, headers)
        
        # Get repo information
        self.repoData = self.response.json()
        self.repoUrls = [repo['clone_url'] for repo in self.repoData]

    def countRepos(self):
        print(f'----- {len(self.repoUrls)} Repos -----')

    def printRepos(self):
        for url in self.repoUrls:
            print(url)


if __name__ == '__main__':
    repos = GithubRepos()
    repos.countRepos()
    repos.printRepos()
