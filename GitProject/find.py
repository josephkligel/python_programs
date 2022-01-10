import os
import sys
import re
from pathlib import Path

def find(filename, search_path=os.getcwd()):
    pathObj = Path(search_path).glob(f'**/*{filename}')
    result = [str(item.parent) for item in pathObj]
    return result

def write_results(result):
    parent = Path(__file__).parent
    resultsFile = parent.joinpath('results.txt')
    with open(resultsFile, 'w') as fw:
        print('Writing found results to result.txt...')
        fw.writelines("\n".join(result))

if __name__ == '__main__':
    filename = sys.argv[1]
    if len(sys.argv) > 2:
        result = find(filename, sys.argv[2])
        write_results(result)
        print(*result, sep='\n')
    else:
        result = find(filename)
        write_results(result)
        print(*result, sep='\n')

