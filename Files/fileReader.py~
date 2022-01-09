import sys
from file import File

class fileReader:
    def __init__(self, fileStr):
        self.fileObj = File(fileStr)

    def read(self):
        with open(self.fileObj.path, 'r') as fr:
            for line in fr:
                print(line)

    def strip(self):
        with open(self.fileObj.path, 'r') as fr:
            for line in fr:
                if line == '\n':
                    continue
                else:
                    print(line.strip())


if __name__ == '__main__':
    argc = len(sys.argv)
    if argc >= 2:
        fr = fileReader(sys.argv[1])
        if sys.argv[2] == "--strip":
            fr.strip()
        else:
            fr.read()

