#!/usr/bin/python3

class Student:
	def __init__(self):
		self.name = "Joseph"
		self.age = 29
		self.marks = 95
		print("Init has been called for the instance called " + self.name)

	def talk(self):
		print("Name: ", self.name)
		print("Age: ", self.age)
		print("Marks: ", self.marks)

s1 = Student()
s2 = Student()
