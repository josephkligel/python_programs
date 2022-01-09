#!/usr/bin/python3
import os
import fnmatch

def find(pattern, path='/'):
	result = []
	for root, dirs, files in os.walk(path):
		for name in files:
			if fnmatch.fnmatch(name, pattern):
				result.append(os.path.join(root,name))
	return result

def open_file(fileList):
	answer = input('\nWould you like to open a file (yes/no)? ')
	if answer.lower() == 'y' or answer.lower() == 'yes':
		num = int(input('What file would you like to open?\nChoose a number of the file name: '))
		for index, file in fileList:
			if num == int(index):
				os.system(f'vim {str(file)}')
	else:
		print('Goodbye')
		exit()

def main():
	pattern = input('What would you like to find? ')
	path = input('What location would you like to search through? ')

	fileList = list(enumerate(find(pattern, path), 1))
	for index, file in fileList:
		print(index, file, sep=') ')
	open_file(fileList)

if __name__ == '__main__':
	main()
