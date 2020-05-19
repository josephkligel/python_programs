#!/usr/bin/python3
from os import *

tocs = {
	1: "Bash Table of Contents",
	2: "Python Table of Contents",
	3: "C Table of Contents"
}
print("What table of contents text file would you like to edit?")

for k,v in tocs.items():
	print(k,v, sep=") ")

number = int(input("Type number here: "))

if (number == 1):
	system("nano -l $HOME/bin/README.md")
elif (number == 2):
	system("nano -l $HOME/python_programs/README.md")
elif (number == 3):
	system("nano -l $HOME/c_programs/README.md")
else:
	print("Invalid Input. Try again.")
