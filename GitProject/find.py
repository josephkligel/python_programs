import os
import sys
import re
from pathlib import Path

# Find file by name and return the result
# Typically used to find directories containing .git subfolders
def find(filename, search_path=os.getcwd()):
    pathObj = Path(search_path).glob(f'**/*{filename}')
    result = [str(item.parent) for item in pathObj]
    return result

# Write the results to results.txt
def write_results(result):
    parent = Path(__file__).parent
    resultsFile = parent.joinpath('results.txt')
    with open(resultsFile, 'w') as fw:
        print('Writing found results to result.txt...')
        fw.writelines("\n".join(result))

# Main function calls script as a stand-alone provided a filename as an argument
# Results of finding are written to results.txt in the current working directory
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

