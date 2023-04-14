import os

# Git class for each git remote url found
class Git():
    # Initialize Git object with a provided remote url
    def __init__(url):
        # No use yet
        self.gitUrl = url
    
    # Clone repo given the provided url parameter
    @staticmethod
    def clone(gitUrl, directory='.'):
        os.system(f'git -C {directory} clone {gitUrl}')
    
    # Push current working directory or directory provided
    @staticmethod
    def push(directory='.'):
        addCmd = f'git -C {directory} add -A;'
        commitCmd = f'git -C {directory} commit -m "Using GitProject program to push";'
        pushCmd = f'git -C {directory} push;'
        os.system(f'{addCmd}{commitCmd}{pushCmd}')

    # Pull cwd or directory provided
    @staticmethod
    def pull(directory='.'):
        os.system(f'git -C {directory} pull')

    # Set token for current working/provided git directory using git set-url functionality
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
