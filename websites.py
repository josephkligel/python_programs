#!/usr/bin/python3
from os import *

print("Where would you like to go?")
switcher = {
	1: "Google",
	2: "Yahoo",
	3: "Quora",
	4: "Reddit"
}
print(switcher.get("Choose a number"))
x = input("Type the number here: ")
print("You typed " + x)
