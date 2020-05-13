#/usr/bin/python3

import sys

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


def ask_for_number_args():
	x = float(input("\nFirst number to calculate: "))
	y = float(input("Second number to calculate: "))
	return x, y

def check_number(num):
	if num == 0:
		sys.exit()
	else:
		x, y = ask_for_number_args()
		if num == 1:
        		print(x,'+',y,'=', add(x, y))
		elif num == 2:
			print(x,'-',y,'=', subtract(x, y))
		elif num == 3:
			print(x,'*',y,'=', multiply(x, y))
		elif num == 4:
			print(x,'/',y,'=', divide(x, y))
		else:
			print("Invalid input")

def calculate():
	print("Choose what type of calculation you would like to perform")
	print("0: Exit Calculator")
	print("1: add")
	print("2: subtract")
	print("3: multiply")
	print("4: divide")

	num = int(input("Type number here: "))
	check_number(num)

	while(num > 0):
		print()
		print("------------New Calculation------------")
		calculate()


calculate()
