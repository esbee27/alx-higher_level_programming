#!/usr/bin/python3
"""Writes a script to a text file
Returns the number of character written
"""


def write_file(filename="", text=""):
    """Writes a string and returns the number of str"""

    with open(filename, 'w+') as f:
        return f.write(text)
