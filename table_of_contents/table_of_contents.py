#!/usr/bin/python3
from os import *

tocs = {
	1: "Bash Table of Contents",
	2: "Python Table of Contents",
	3: "C Table of Contents",
        4: "Node Table of Contents",
        5: "React Table of Contents"
}
print("What table of contents text file would you like to edit?")

for k,v in tocs.items():
	print(k,v, sep=") ")

number = int(input("Type number here: "))

if (number == 1):
    system("vim $HOME/bin/README.md")
elif (number == 2):
    system("vim $HOME/python_programs/README.md")
elif (number == 3):
    system("vim $HOME/c_programs/README.md")
elif (number == 4):
    system("vim $HOME/node/README.md")
elif (number == 5):
    system("vim $HOME/Github/react/README.md")
else:
	print("Invalid Input. Try again.")
