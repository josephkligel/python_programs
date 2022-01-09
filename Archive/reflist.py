#!/usr/bin/python3

lst = {
	"Todolist": {
		"file": "todolist.txt",
		"default": "$HOME/Github/Programmapedia/todolist.txt",
		"arg": 'todo'
		},
	"Bash Reference": {
		"file": "bashref.txt",
		"default": "$HOME/Github/Programmapedia/bashref.txt",
		"arg": 'bash'
		},
	"C Programming Reference": {
		"file": "cref.txt",
		"default": "$HOME/Github/Programmapedia/cref.txt",
		"arg": 'c'
		},
	"CSS Reference": {
		"file": "cssref.txt",
		"default": "$HOME/Github/Programmapedia/cssref.txt",
		"arg": 'css'
		},
	"Git Reference": {
		"file": "gitref.txt",
		"default": "$HOME/Github/Programmapedia/gitref.txt",
		"arg": 'git'
		},
	"HTML Reference": {
		"file": "htmlref.txt",
		"default": "$HOME/Github/Programmapedia/htmlref.txt",
		"arg": 'html'
		},
	"Nodejs Reference": {
		"file": "noderef.txt",
		"default": "$HOME/Github/Programmapedia/noderef.txt",
		"arg": 'node'
		},
	"Python Index": {
		"file": "pyIndex.txt",
		"default": "$HOME/Github/Programmapedia/pyIndex.txt",
		"arg": 'py'
		},
	"JavaScript Reference":{
		"file": "jsref.txt",
		"default": "$HOME/Github/Programmapedia/jsref.txt",
		"arg": 'js'
		}
}

def add_to_list():
	new_file_value = str(input("What is the name of this text file? "))
	new_default_value = str(input("Type the location of the file including its name here: "))
	with open(new_default_value) as file:
		new_key = file.readline()[2:].strip()
	list.update({new_key: {"file": new_file_value, "default": new_default_value}})
	# with open("/home/jkligel/python_programs/reflist.py", 'a') as file:
	# 	file.write(list[new_key] = {"file": new_file_value, "default": new_default_value})
