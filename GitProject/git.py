import os

class Git():
    def __init__(url):
        # No use yet
        self.gitUrl = url
    
    @staticmethod
    def clone(gitUrl, directory='.'):
        os.system(f'git -C {directory} clone {gitUrl}')
    
    @staticmethod
    def push(directory='.'):
        addCmd = f'git -C {directory} add -A;'
        commitCmd = f'git -C {directory} commit -m "Using GitProject program to push";'
        pushCmd = f'git -C {directory} push;'
        os.system(f'{addCmd}{commitCmd}{pushCmd}')

    @staticmethod
    def pull(directory='.'):
        os.system(f'git -C {directory} pull')

    @staticmethod
    def setToken(directory='.'):
        command = f'git -C {directory} remote set-url'\
                ' origin'\
                ' https://'\
                f'{os.getenv("token")}'\
                '@github.com/zigjag/'\
                f'{os.path.basename(directory)}'\
                '.git'
        os.system(command)
        #print(command)
