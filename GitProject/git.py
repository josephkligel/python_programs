import os

class Git():
    def __init__(url):
        self.gitUrl = url
    
    @staticmethod
    def clone(directory='.'):
        os.system(f'git -C {directory} clone {self.gitUrl}')
    
    @staticmethod
    def push(directory='.'):
        addCmd = 'git -C {directory} add -A'
        commitCmd = 'git -C {directory} commit -m "Using GitProject program to push"'
        pushCmd = 'git -C {directory} push'
        os.system(f'{addCmd}; {commitCmd}; {pushCmd}')

    @staticmethod
    def pull(directory='.'):
        os.system(f'git -C {directory} pull')

    @staticmethod
    def setToken(directory='.'):
        os.system(f"git remote set-url origin {os.getenv('token')}@github.com/zigjag/{os.path.basename(directory)}.git")
