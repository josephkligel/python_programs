#!/usr/bin/python3
from os import system, walk, path
import json, time, fnmatch

def clear_screen():
    system('clear')

def main():
    selection()

def selection():
  print("What text would you like to edit?")
  print("\t0: Add new text")

  i = 1
  with open('/home/jkligel/python_programs/reflist.json', 'r') as fh:
      data = json.load(fh)

  index_checker = dict(enumerate(data.items(), 1))
  for k, v in index_checker.items():
      if int(k) == 10:
          print(7*'-'+'Specific Text Guides'+7*'-')
          print(f'\t{k}: {v[0]}')
      else:
          print(f'\t{k}: {v[0]}')
  num = int(input("Type number here: "))
  for k, v in index_checker.items():
      if num == 0:
          add_to_lst(data)
      elif num == k:
          system(f'nano {v[1]["default"]}')
      # elif num != k:
      #     print('\nNo such number. Try again.\n')
      #     time.sleep(1)
      #     clear_screen()
      #     main()

def add_to_lst(data):
    textfile = input("Type name of textfile here, include extension: ")
    if textfile == '':
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
