import os
import sys

class Environment:
    def __init__(self):
        self._environ = os.environ
    
    def getEnvironment(self):
        for k,v in sorted(os.environ.items()):
            print(f'{k}: {v}')

    def getPath(self):
        for item in os.getenv('PATH').split(':'):
            print(item)

    def getHome(self):
        print(self._environ['HOME'])

if __name__ == '__main__':
    argc = len(sys.argv)
    #print(argc)
    env = Environment()
    if argc == 1:
        env.getEnvironment()
    elif argc >= 2:
        option = sys.argv[1]
        if option == '--path':
            env.getPath()
        elif option == '--home':
            env.getHome()
            
        
        
