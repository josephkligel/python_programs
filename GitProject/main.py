from githubRepos import GithubRepos
from git import Git
from find import find
import sys
import os

def get_local_repos(search_path='.'):
    return find('.git', search_path)

def cloneAll(destination='.'):
    repos = GithubRepos()
    for repoUrl in repos.repoUrls:
        Git.clone(destination)

def setToken(local_repos):
    for repo in local_repos:
        Git.setToken(repo)

def pushAll(local_repos):
    for repo in local_repos:
        Git.push(repo)

def pullAll(local_repos):
    for repo in local_repos:
        Git.pull(repo)

def main():
    pass

if __name__ == '__main__':
    local_repos = get_local_repos('/home/jkligel/Github')
    setToken(local_repos)
    #pushAll(local_repos)
