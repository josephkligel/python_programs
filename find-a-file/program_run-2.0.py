import json
import os, sys
from find_a_file import find

found_dict = json.load(open('found_files.json', 'r'))
enumeratedDict = {}

print("What program would you like to open?")
for c,i in enumerate(found_dict.items()):
        enumeratedDict[c] = i
        print(f'\t{str(c)}. {i[0]}')

num = int(input("\nType number here: "))

for k, v in enumeratedDict.items():
    if num == 0:
        search_file = input(str('What file are you looking for (type only name and extension)? '))
        find(search_file) # no startDir was added. It will look in /home/jkligel directoriy
        sys.exit()
    elif num == int(k):
        os.system(f'{v[1]}')
