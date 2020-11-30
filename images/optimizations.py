#!/usr/bin/env python3
import os
from os import walk
from os import listdir
import subprocess
import codecs
import urllib.parse
from urllib.parse import urlparse
import shutil

dirs = sorted(next(os.walk('.'))[1]) # This will get all of the subdirectories in a folder
#dirs = sorted(os.listdir()) # This will get all of the files and subdirectories in a folder

# print (dirs) # Test output

for folders in dirs:

    folders_string = folders.replace (' ', r'\ ') # This ensures that when we call a subprocess, the filepath is correctly passed for terminal.

    images = sorted(os.listdir(folders))
    #print (images) # Test output

    # Managing subdirectories for image optimizations:
    #    If the path exists, delete it (and contents) to start afresh
    #    Else, recreate it.
    if os.path.exists(folders + '/optimised'):
        shutil.rmtree(folders + '/optimised')
        os.makedirs(folders + '/optimised')
    if not os.path.exists(folders + '/optimised'):
        os.makedirs(folders + '/optimised')

    # Call ImageMagick
    #     This first syncs the images to a new folder for optimization
    #     Then we run the ImageMagick mogrify command to process the images down to a specifc size and optimizes weight.
    os.system ('rsync -avr --exclude=\'*/\' --exclude=\'*.html\' --exclude=\'*.txt\' --include=\'*.{jpg,JPG,jpeg,JPEG,png,PNG}\' ' + folders_string + '/* ' + folders_string + '/optimised/') 
    os.system ('magick mogrify -density 72 -thumbnail 1100x1100 -filter Triangle -define filter:support=2 -unsharp 0.25x0.08+8.3+0.045 -dither None -posterize 136 -quality 82 -define jpeg:fancy-upsampling=off -define png:compression-filter=5 -define png:compression-level=9 -define png:compression-strategy=1 -define png:exclude-chunk=all -interlace none -colorspace sRGB ' + folders_string + '/optimised/*.{jpg,JPG,jpeg,JPEG,PNG,png}')



'''
    images = sorted(os.listdir(folders))
    writeFile= open("../snippets/5-body-images.html","w+")
    startImg = """<img class=\"img-large\" src=\"images/"""
    endImg = """\">"""

    for imagefiles in images:
        if imagefiles.endswith(".jpg"): # Reading only .jpg files
            print (imagefiles)
            # This is a loop for each file.
            # It reads each file and reads the content to the writeFile, then adds a line break ("\n")
            #writeFile.write(startImg)
            #writeFile.write(file)
            #writeFile.write(endImg)
            #writeFile.write("\r\n")
    #writeFile.close()
''' 








'''
    writeFile= open("../snippets/3-body-images.html","w+")
    startImg = """<img class=\"img-large\" src=\"images/"""
    endImg = """\">"""

    for file in dirs:
        if file.endswith(".jpg"): # Reading only .jpg files
            # This is a loop for each file.
            # It reads each file and reads the content to the writeFile, then adds a line break ("\n")
            writeFile.write(startImg)
            writeFile.write(file)
            writeFile.write(endImg)
            writeFile.write("\r\n")
    writeFile.close()

'''




'''
def main():
    writeFile= open("../snippets/3-body-images.html","w+")
    startImg = """<img class=\"img-large\" src=\"images/"""
    endImg = """\">"""

    for file in dirs:
        if file.endswith(".jpg"): # Reading only .jpg files
            # This is a loop for each file.
            # It reads each file and reads the content to the writeFile, then adds a line break ("\n")
            writeFile.write(startImg)
            writeFile.write(file)
            writeFile.write(endImg)
            writeFile.write("\r\n")
    writeFile.close()

if __name__== "__main__":
    main()

''' 

'''
# References

Filtering correctly in terminal: https://rclone.org/filtering/

Getting subdirectories: https://stackoverflow.com/questions/973473/getting-a-list-of-all-subdirectories-in-the-current-directory
  https://www.geeksforgeeks.org/python-program-to-merge-two-files-into-a-third-file/
  https://www.tutorialspoint.com/python/os_listdir.htm 
  https://www.guru99.com/reading-and-writing-files-in-python.html
  Indentation: https://stackoverflow.com/questions/492387/indentationerror-unindent-does-not-match-any-outer-indentation-level
  Selecting only specific files: https://www.pythonforbeginners.com/code-snippets-source-code/python-os-listdir-and-endswith
  I/O Errors and CSVs: https://stackoverflow.com/questions/18952716/valueerror-i-o-operation-on-closed-file

  Creating subdirecxtoriers:  https://www.tutorialspoint.com/How-can-I-create-a-directory-if-it-does-not-exist-using-Python
  Removing directories: https://linuxize.com/post/python-delete-files-and-directories/
  Rsync only files, not directories: https://superuser.com/questions/458671/rsync-only-files-and-not-directories
'''