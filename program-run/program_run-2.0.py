#!/usr/bin/env python3
import json
import os, sys
from lib.find_a_file import find

found_json = open(os.path.join(os.path.dirname(__file__), 'lib/found_files.json'))
found_dict = json.load(found_json)

found_json.close()

enumeratedDict = {}

print("What program would you like to open?")
for c,i in enumerate(found_dict.items()):
        enumeratedDict[c] = i
        print(f'\t{str(c)}. {i[0]}')

num = int(input("\nType number here: "))

for k, v in enumeratedDict.items():
    if num == 0:
        search_file = input(str('What file are you looking for (type only name and extension)? '))
        find(search_file) # no startDir was added. It will look in /home/jkligel directory
        sys.exit()
    elif num == int(k):
        os.system(f'{v[1]}')
