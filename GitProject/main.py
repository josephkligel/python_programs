from githubRepos import GithubRepos
from git import Git
from find import find
import sys
import os

# Global variables
local_repo_directory = os.getenv('HOME')

# Main functions called from options provided to this script

## Find all local git directories and return them as a list
def get_local_repos(search_path='.'):
    return find('.git', search_path)

## Clone all repos from the GithubRepos object automatically to the current directory
def cloneAll(destination='.'):
    repos = GithubRepos()
    for repoUrl in repos.repoUrls:
        Git.clone(repoUrl, destination)

## Set token for GitHub interaction. Depricated
def setToken(local_repos):
    for repo in local_repos:
        Git.setToken(repo)

## Add all, commit, and push the changes of the local repos remotely
def pushAll(local_repos):
    for repo in local_repos:
        Git.push(repo)

## Pull changes from remote repos to the local repos
def pullAll(local_repos):
    for repo in local_repos:
        Git.pull(repo)

# Execute the code below if main.py was called directly
if __name__ == '__main__':
    # Create list of local repos from the get_local_repos function
    local_repos = get_local_repos(local_repo_directory)

    # Ensure length of arguments is 2 or more
    # Then check the argument for the provided keyword
    # and execute the function corresponding to the keyword 
    if len(sys.argv) >= 2:
        argument = sys.argv[1]
        if argument == 'set-token':
            setToken(local_repos)
        elif argument == 'clone':
            cloneAll(local_repo_directory)
        elif argument == 'push':
            pushAll(local_repos)
        elif argument == 'pull':
            pullAll(local_repos)
    else:
        print('Please choose a correct option')
