#!/usr/bin/python3
"""
A module that adds 2 integers
It returns the addition of the integers which is an integer
"""

def add_integer(a, b=98):
    """A function that adds two integers
    It checks if the arguments are integers of floats
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')
    if type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return a + b
