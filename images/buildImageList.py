#!/usr/bin/env python3

import os
from os import listdir
import codecs

#path = "../Snippets/"
dirs = sorted(os.listdir())

def main():
    writeFile= open("../snippets/5-body-images.html","w+")
    startImg = """<img class=\"img-large\" src=\"images/"""
    endImg = """\">"""

    for file in dirs:
        img_list = [".jpg",".JPG",".JPEG",".jpeg",".png",".PNG"] # list of image files
        if file.endswith(tuple(img_list)): # Reading only image files
            # This is a loop for each file.
            # It reads each file and reads the content to the writeFile, then adds a line break ("\n")
            writeFile.write(startImg)
            writeFile.write(file)
            writeFile.write(endImg)
            writeFile.write("\r\n")
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