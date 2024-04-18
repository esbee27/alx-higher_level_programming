#!/usr/bin/python3
"""Reads a file to stdout
The file is filename
"""


def read_file(filename=""):
    """Reads a text file and prints to stdout

    Args:
        filename: the file to be read
    """

    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
