#!/usr/bin/python
def factorial(n):
    if n < 1:
        return 1
    else:
        number = n * factorial(n-1)
        return number

print(factorial(1))
