import os
from glob import glob

def main():
    path = str(input("""What folder would you like to get a file list of?
        (Include full path uptil the trailing forward slash.) """))
    for file in getListOfFiles(path):
        print(file)

def getListOfFiles(path='/home/jkligel/Downloads'):
    fileList = []
    for file in glob(path+'/**', recursive=True):
        fileList.append(file)
    return fileList

if __name__ == '__main__':
    main()
