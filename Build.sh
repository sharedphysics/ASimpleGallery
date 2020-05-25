#!/bin/sh

# Read the images directory and wrap the images in HTML
printf "\033[0;32m  Starting Build Process \033[0m\n" 

# Read the images directory and wrap the images in HTML
printf "\033[0;32m  ... Building Your Gallery... \033[0m\n" 
cd images
python3 buildImageList.py
python3 optimizations.py
python3 buildImageList-withsubdirectory.py

# Combine various html snippets into one core index.html file
printf "\033[0;32m  ... Compiling HTML files... \033[0m\n" 
cd ../snippets/
python3 buildIndex.py

# Go back and launch the page locally for testing
cd ../
python3 open.py

# Just a tooltip to let you know the script is running.
printf "\033[0;32m  All good! Launching site. \033[0m\n" 