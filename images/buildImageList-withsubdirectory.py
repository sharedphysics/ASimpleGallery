#!/usr/bin/env python3

import os
from os import walk
from os import listdir
import subprocess
import codecs
import urllib.parse
from urllib.parse import urlparse
import shutil
from shutil import copy


dirs = sorted(next(os.walk('.'))[1]) # This will get all of the subdirectories in a folder
#dirs = sorted(os.listdir()) # This will get all of the files and subdirectories in a folder

# print (dirs) # Test to see What

# Define and create the hompage-based sidebar URLs based on subdirectories folder:
createSidebar = open("../snippets/3-sidebar-content.html","w+")
for folders in dirs:
    print (folders) # Test output
    urlEncodeFolders = urllib.parse.quote(folders) # Encode folder paths to work as URLs
    buildURL = """<a href=\"./images/""" + urlEncodeFolders + """/index.html\">""" + folders + """</a><br>"""
    createSidebar.write(buildURL + "\r\n")
createSidebar.close()    

# This will create the proper sidebar url structure for the sidebar in subdirectories
for folders in dirs:
    createSubDirSidebar = open("./"+folders+"/3-sidebar-content.txt","w+")
    '''# WIP: Creating a recursive list of folders. Probably should use create a list before I go into the foreach, but will see!
    urlEncodeSubDirFolders = urllib.parse.quote(folders) # Encode folder paths to work as URLs
    buildSubDirURL = """<a href=\"../../""" + urlEncodeSubDirFolders + """/\">""" + folders + """</a><br>"""
    createSubDirSidebar.write(buildSubDirURL + "\r\n")    
    '''
    createSubDirSidebar.write("<a href=\"../../index.html\">< Back</a><br><br>" + "\r\n")    
    createSubDirSidebar.close()


    # This will create the images list for subdirectories
    images = sorted(os.listdir(folders))
    createSubDirImagesList = open("./"+folders+"/5-body-images.txt","w+")
    createSubDirImagesList.write("<br>")
    for imagefiles in images:
        img_list = [".jpg",".JPG",".JPEG",".jpeg",".png",".PNG"] # list of image files
        if imagefiles.endswith(tuple(img_list)): # Reading only image files
            print (imagefiles) # Test output
            urlEncodeImages = urllib.parse.quote(imagefiles) # Encode folder paths to work as URLs
            createSubDirImagesList.write("""<a href=\"""" + urlEncodeImages + """\">""" + """<img class=\"img-large\" src=\"./optimised/""" + urlEncodeImages + """\"></a>""" + "\r\n")
    createSubDirImagesList.close()


    # This will copy all of the key html snippet files to the subdirecty folder to build the pages
    shutil.copy("../snippets/1-header.html", folders+"/1-header.txt")
    shutil.copy("../snippets/2-sidebar-start.html", folders+"/2-sidebar-start.txt")
    shutil.copy("../snippets/4-body-start.html", folders+"/4-body-start.txt")
    shutil.copy("../snippets/6-body-end.html", folders+"/6-body-end.txt")

    # This will compile the snippets into a index.html file
    writeIndex = open("./"+folders+"/index.html","w+")
    txtfileslist = sorted(os.listdir(folders))
    for txtfiles in txtfileslist:
        print (txtfiles)
        if txtfiles.endswith(".txt"): # Reading only .txt files
            readFile = codecs.open("./"+folders+"/"+txtfiles, 'rb', encoding='utf-8')
            writeIndex.write(readFile.read() + "\n") 
    writeIndex.close()


    # This will rename all of the optimised files to be url-friendly encodings. <-- TURN OUT, NOT NECCESSARY!
    '''
    optimisedimages = sorted(os.listdir(folders+"/optimised"))
    for optimisedimagefiles in optimisedimages:
        if optimisedimagefiles.endswith(".jpg"): # Reading only .jpg files
            #print (imagefiles) # Test output
            urlEncodeImage = urllib.parse.quote(optimisedimagefiles)
            os.rename(folders+"/optimised/"+optimisedimagefiles, folders+"/optimised/"+urlEncodeImage)
    '''


'''
# References

Getting subdirectories: https://stackoverflow.com/questions/973473/getting-a-list-of-all-subdirectories-in-the-current-directory
  https://www.geeksforgeeks.org/python-program-to-merge-two-files-into-a-third-file/
  https://www.tutorialspoint.com/python/os_listdir.htm 
  https://www.guru99.com/reading-and-writing-files-in-python.html
  Indentation: https://stackoverflow.com/questions/492387/indentationerror-unindent-does-not-match-any-outer-indentation-level
  Selecting only specific files: https://www.pythonforbeginners.com/code-snippets-source-code/python-os-listdir-and-endswith
  I/O Errors and CSVs: https://stackoverflow.com/questions/18952716/valueerror-i-o-operation-on-closed-file
  https://logbuffer.wordpress.com/2011/03/24/linux-copy-only-certain-filetypes-with-rsync-from-foldertree/
  https://stackoverflow.com/questions/123198/how-do-i-copy-a-file-in-python
'''