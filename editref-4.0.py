#!/usr/bin/python3

from os import system, walk, path
import json
import fnmatch
import sys
import re

indexcheck = {}

def main():
    selection()

def selection():
  print("What text would you like to edit?")
  print("\t0: Add new text")

  i = 1
  with open('/home/jkligel/python_programs/reflist.json', 'r') as fh:
      data = json.load(fh)
      for k,v in data.items():
          indexcheck[i] = k
          if i == 10:
              print("-------Specific Text Guides-------")
              print('\t%d: %s' % (i, k))
          else:
              print('\t%d: %s' % (i, k))
          i+=1

  num = int(input("Type number here: "))
  edit(num, indexcheck, data)

def edit(num, indexcheck, data):
    if num == 0:
        add_to_lst(data)
    else:
        for k, v in indexcheck.items():
            if num == k:
                for key, value in data.items():
                    if v == key:
                        return system("vim %s" % (value["default"]))

def add_to_lst(data):
    textfile = input("Type name of textfile here, include extension: ")
    if textfile == '':
        print("\n---------Nothing added---------\n")
        main()
    else:
        text_location = input("Type file location only here, no ending slash or file name: ")
        name, ext = textfile.split('.', 1)
        data[name.capitalize()] = {'file': textfile, 'default': text_location+'/'+textfile}
        with open('/home/jkligel/python_programs/reflist.json', 'w') as fh:
            json.dump(data, fh)
        main()

def search_for_file(pattern):
    result = []
    for root, dirs, files in walk('/'):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                return True
            else:
                full_file_name = os.path.join('/home/jkligel/Desktop',pattern)
                new_file = open(full_file_name, 'w')
                new_file.close()
                system('vim %s' % (full_file_name))

if len(sys.argv) < 2:
    main()
else:
    with open('/home/jkligel/python_programs/reflist.json') as fh:
        datalist = json.load(fh)
    argument = sys.argv[1]

    if argument in datalist:
        system(f'vim {datalist[argument]["default"]}')
    else:
        print(f"{argument} is not in the reflist")
        print(f'Choose one of these:\n{list(datalist.keys())}')
