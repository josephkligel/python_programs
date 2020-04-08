#!/usr/bin/python3

from os import system, walk, path
import json
import fnmatch

indexcheck = {}

def main():
    selection()

def selection():
  print("What text would you like to edit?")
  print("\t0: Add new text")

  i = 1
  with open('reflist.json', 'r') as fh:
      data = json.load(fh)
      for k,v in data.items():
          indexcheck[i] = k
          if i >= 10:
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
                        return system("nano %s" % (value["default"]))

def add_to_lst(data):
    textfile = input("Type name of text name here, include extension: ")
    if textfile == '' or text_location == '':
        print("\n---------Nothing added---------\n")
        main()
    else:
        text_location = input("Type location of text file here, include textfile name in the location: ")
        name, ext = textfile.split('.', 1)
        data[name.capitalize()] = {'file': textfile, 'default': text_location}
        with open('reflist.json', 'w') as fh:
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
                system('nano %s' % (full_file_name))


if __name__ == '__main__':
    main()
