
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def calculate():
	print("Choose what type of calculation you would like to perform")
	print("0: Exit Calculator")
	print("1: add")
	print("2: subtract")
	print("3: multiply")
	print("4: divide")

	num = int(input("Type number here: "))
    x = float(input("\nFirst number to calculate: "))
    y = float(input("Second number to calculate: "))

	if num == 0:
		exit()
	elif num == 1:
        print(x,'+',y,'=', add(x, y))
	elif num == 2:
		print(x,'-',y,'=', subtract(x, y))
	elif num == 3:
		print(x,'*',y,'=', multiply(x, y))
	elif num == 4:
		print(x,'/',y,'=', divide(x, y))
	else:
		print("Invalid input")

	while(num > 0):
		__calculate()

calculate()
