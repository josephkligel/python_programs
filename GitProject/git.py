import os

class Git():
    def __init__(self, url):
        self.gitUrl = url

    def clone(self, directory='.'):
        os.system(f'git -C {directory} clone {self.gitUrl}')
