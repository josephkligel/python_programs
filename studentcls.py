#!/usr/bin/python3

class Student:
	def __init__(self, flag):
		self.flag = flag
		self.name = "Joseph"
		self.age = 29
		self.marks = 95
		if(self.flag):
			print("Instance created at memory address " + str(id(self)))

	def talk(self):
		print("Name: ", self.name)
		print("Age: ", self.age)
		print("Marks: ", self.marks)

s1 = Student(flag=True)
s2 = Student(flag=False)
