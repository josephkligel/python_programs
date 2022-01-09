import os
import sys
import re
from pprint import pprint

def find_files(filename, search_path=lambda: os.getcwd):
    regex = re.compile(filename)
    result = []

    for root, subdir, files in os.walk(search_path):
        """if filename in files:
            result.append(os.path.join(root, filename))
        """
        for file in files:
            if regex.match(file):
                result.append(os.path.join(root, filename))

    return result

def write_results(result):
    with open('result.txt', 'w') as fw:
        print('Writing found results to result.txt...')
        fw.writelines("\n".join(result))


if __name__ == '__main__':
    filename = sys.argv[1]
    if len(sys.argv) > 2:
        result = find_files(filename, sys.argv[2])
        write_results(result)
        print(*result, sep='\n')
    else:
        result = find_files(filename)
        write_results(result)
        print(*result, sep='\n')

