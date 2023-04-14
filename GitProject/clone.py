from git import Git

# Stand-alone script to call on Git class and clone a directory
def clone(urlStr, directory):
    git = Git(urlStr)
    git.clone(directory)
