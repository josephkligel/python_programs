import os
import sys

class Environment:
    def __init__(self):
        self._environ = os.environ
    
    def getEnvironment(self):
        for k,v in self._environ.items():
            print(f'{k}: {v}')

    def getPath(self):
        for item in os.getenv('PATH').split(':'):
            print(item)

    def getHome(self):
        print(self._environ['HOME'])

    def getVar(self, varName):
        print(self._environ[varName])

def program():
    env = Environment()

    print('This program displays the environment:')
    print('1. Path')
    print('2. Home')
    print('3. Other')
    print('4. All')
    print('5. Exit')
    choice = int(input('What environment variable do you want? '))
    if choice == 1:
        env.getPath()
    elif choice == 2:
        env.getHome()
    elif choice == 3:
        varName = input('What variable do you want? ')
        env.getVar(varName)
    elif choice == 4:
        env.getEnvironment()
    else:
        sys.exit()

def command():
    argc = len(sys.argv)
    env = Environment()
    if argc == 1:
        env.getEnvironment()
    elif argc >= 2:
        option = sys.argv[1]
        if option == '--path':
            env.getPath()
        elif option == '--home':
            env.getHome()

if __name__ == '__main__':
            program()
        
