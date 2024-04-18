#!/usr/bin/python3
"""Reads a file to stdout
The file is filename
"""

def read_file(filename=""):
    with open(filename, encoding = "UTF-8") as f:
        read_data = f.read()
        print(read_data, end="")
