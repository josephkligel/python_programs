#!/usr/bin/python3

def std(name, cls, **marks):
	print("Name: ", name)
	print("Class: ", cls)
#	print("Marks: ", marks)
	for k,v in marks.items():
		print(k, "Marks: ",  v)

std(name="Joseph", cls=10, english=90, math=95, physics=94)
