from git import Git

def clone(urlStr, directory):
    git = Git(urlStr)
    git.clone(directory)
