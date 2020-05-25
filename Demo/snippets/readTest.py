#!/usr/bin/env python3

import os
from os import listdir
import codecs

#path = "../Snippets/"
dirs = sorted(os.listdir("."))

def main():
	f= open("readTest.txt","w+")
	for file in dirs:
		if file.endswith(".html"):
			f.write(file)
			f.write("\r\n")
	f.close()

if __name__== "__main__":
	main()

# References
# https://www.geeksforgeeks.org/python-program-to-merge-two-files-into-a-third-file/
# https://www.geeksforgeeks.org/python-os-listdir-method/
# https://www.tutorialspoint.com/python/os_listdir.htm 
# Reading and Writing FileS: https://www.guru99.com/reading-and-writing-files-in-python.html
# Indentation: https://stackoverflow.com/questions/492387/indentationerror-unindent-does-not-match-any-outer-indentation-level
# Selecting only specific files: https://www.pythonforbeginners.com/code-snippets-source-code/python-os-listdir-and-endswith