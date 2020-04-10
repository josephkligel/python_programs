#!/usr/bin/python3

from os import *

options = {
	1: "Postman",
	2: "Robo3t",
	3: "Mega"
}

print("What program would you like to open?")
for k,v in options.items():
	print(str(k) + ")",v);

num = int(input("Type number here: "))

if(num == 1):
	system("/opt/Postman/Postman");
elif(num == 2):
	system("/opt/robo3t-1.3.1/bin/robo3t");
elif(num == 3):
	system("/opt/MegaBasterdLinux.run");
else:
	print("Invalid input. Try again.")
