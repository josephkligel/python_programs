#!/usr/bin/python3
from os import *

indexes = {
	1: "Todolist",
	2: "Bash reference",
	3: "Python programming index",
	4: "C programming reference"
}

print("What reference text would you like to edit?")
for k,v in indexes.items():
	print(k,v, sep = ') ')
number = int(input("Type number here: "))

if (number == 1):
	system("nano -l /home/jkligel/bin/todolist.txt")
elif(number == 2):
	system("nano -l /home/jkligel/bin/bashref.txt")
elif(number == 3):
	system("nano -l /home/jkligel/python_programs/pyIndex.txt")
elif(number == 4):
	system("nano -l /home/jkligel/c_programs/cref.txt")
else:
	print("Invalid input. Try again.")
