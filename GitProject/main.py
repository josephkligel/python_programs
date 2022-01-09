from githubRepos import GithubRepos
from git import Git
import sys
import os

def clone(urlStr):
    git = Git(urlStr)
    git.clone('./test')

def main():
    repos = GithubRepos(token=sys.argv[1])
    for r in repos.repoUrls:
        clone(r)

if __name__ == '__main__':
    main()
