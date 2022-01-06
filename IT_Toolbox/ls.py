import os
import sys

def ls(dirName=None):
    for line in os.listdir(dirName):
        print(line)

if __name__ == '__main__':
    ls()
