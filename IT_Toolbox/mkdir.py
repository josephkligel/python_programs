import os
import sys

def mkdir(dirName):
    os.mkdir(dirName)

if __name__ == '__main__':
    print('Making directory...')
    os.mkdir(sys.argv[1])
