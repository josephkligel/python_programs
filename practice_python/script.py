result = None
x = int(input("Number 1: "))
y = int(input("Number 2: "))

try:
    result = x / y
except Exception as e:
    print("An error has been found", type(e))
else:
    print("Inside Else")
finally:
    print("Inside finally")

print("----------New Line---------")
print("Result = ", result)
