#!/usr/bin/env python3

import os
from os import listdir

#path = "../Snippets/"
dirs = os.listdir()

def main():
	outputFile= open("../index-2.html","w+")
	for file in dirs:
		insideFile=open(file, "r")
		# read the data from file1 and file2 and write it in file3 
		outputFile.write(insideFile.read()) 
		# Add '\n' to enter data of file2 from next line 
		outputFile.write("\n") 

	outputFile.close()

if __name__== "__main__":
	main()

# References
# https://www.geeksforgeeks.org/python-program-to-merge-two-files-into-a-third-file/
# https://www.tutorialspoint.com/python/os_listdir.htm 
# https://www.guru99.com/reading-and-writing-files-in-python.html
# Indentation: https://stackoverflow.com/questions/492387/indentationerror-unindent-does-not-match-any-outer-indentation-level