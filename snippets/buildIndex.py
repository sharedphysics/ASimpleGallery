#!/usr/bin/env python3

import os
from os import listdir
import codecs

#path = "../Snippets/"
dirs = sorted(os.listdir())

def main():
	writeFile= open("../index.html","w+")
	for file in dirs:
		if file.endswith(".html"): # Reading only .html files
			# This is a loop for each file.
			# It reads each file and reads the content to the writeFile, then adds a line break ("\n")
			readFile=codecs.open(file, 'rb', encoding='utf-8')
			writeFile.write(readFile.read()) 
			writeFile.write("\n") 
	writeFile.close()

if __name__== "__main__":
	main()

# References
# https://www.geeksforgeeks.org/python-program-to-merge-two-files-into-a-third-file/
# https://www.tutorialspoint.com/python/os_listdir.htm 
# https://www.guru99.com/reading-and-writing-files-in-python.html
# Indentation: https://stackoverflow.com/questions/492387/indentationerror-unindent-does-not-match-any-outer-indentation-level
# Selecting only specific files: https://www.pythonforbeginners.com/code-snippets-source-code/python-os-listdir-and-endswith
# I/O Errors and CSVs: https://stackoverflow.com/questions/18952716/valueerror-i-o-operation-on-closed-file
# Sorting listdir(): https://www.reddit.com/r/learnpython/comments/3xg6ba/help_making_oslistdir_return_items_in_order/