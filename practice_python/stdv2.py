#!/usr/bin/python3

n = input('Name: ')
a = input('Age: ')
ma = input('Marks: ')

class Student:
	def __init__(self, n, a, **m):
		self.name = n
		self.age = a
		self.marks = m

	def display(self):
		print("Hello", self.name)
		print("Your age is", self.age)
		print("Your marks", self.marks)

s1 = Student(n, a, m = ma, English = 85) 
s1.display()
