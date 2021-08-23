#!/bin/python
import re

#removes any line of the program that boils down to only a print statment
def remove_print(fname):
	try:
		f = open(fname,'r')
	except:
		print('[WARNING] unable to read from the file "' + fname + '"')
		return False
	#buffer the lines because we will very promptly overide the file
	lines = f.readlines()	
	f.close()
	
	try:
		f = open(fname,'w')
	except:
		print('[ERROR] unable to write to the file "' + fname + '"')
		return False
	
	for line in lines:	
		if not is_print(line):
			f.write(line)
	f.close()

#returns true if the string is a print statement
def is_print(string):
	exp = re.compile('^\s*print')
	return exp.match(string) != None 

if __name__ == '__main__':
	from sys import argv	
	for file in argv[1:]:
		remove_print(file)
