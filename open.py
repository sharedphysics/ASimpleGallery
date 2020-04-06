#!/usr/bin/env python3
import os
import webbrowser

webbrowser.open('file://' + os.path.realpath("index.html"))

# References
# Opening a local page in browser: https://stackoverflow.com/questions/22004498/webbrowser-open-in-python