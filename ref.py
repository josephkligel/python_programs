#!/usr/bin/python3

from os import *
from reflist import list

def selection():
  print("What text would you like to edit?")
  i = 1
  for k, v in list.items():
    print("\t%d: %s" % (i, str(k)))
    i += 1

  num = int(input("Type number here: "))
  edit(num)

def edit(num):
    index = num - 1
    # return system("nano %s" % (v["default"]))

selection()
