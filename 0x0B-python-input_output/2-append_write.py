#!/usr/bin/python3
"""Appends a str to a file"""

def append_write(filename="", text=""):
    """Appends a str"""

    with open(filename, 'a+') as f:
        return f.write(text)
