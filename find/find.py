import os
import sys
from pprint import pprint

def find_files(filename, search_path=os.getcwd()):
    result = []

    for root, subdir, files in os.walk(search_path):
        if filename in files:
            result.append(os.path.abspath(filename))

    return result

if __name__ == '__main__':
    filename = sys.argv[1]
    if len(sys.argv) > 2:
        print(*find_files(filename, sys.argv[2]), sep='\n')
    else:
        print(*find_files(filename), sep='\n')
