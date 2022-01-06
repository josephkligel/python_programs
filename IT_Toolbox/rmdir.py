import os
import sys

def rmdir(dirName):
    os.rmdir(dirName)

if __name__ == '__main__':
    options = sys.argv[2:]
    print('Removing directory...')
    os.rmdir(sys.argv[1])
    if '--check' in options:
        for line in os.listdir():
            print(line)
